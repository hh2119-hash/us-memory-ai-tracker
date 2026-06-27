#!/usr/bin/env python3
"""每日抓取追蹤清單股價，輸出 data/prices.json 供儀表板使用。

於 GitHub Actions 中執行（GitHub runner 具完整網路），使用 yfinance 取得資料。
每檔輸出多週期報酬率（當日/5日/10日/20日/YTD）與近一年收盤序列（供 sparkline）。
"""
import json
import os
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

import yfinance as yf

# 各市場交易時區與收盤時間（用來剔除「盤中尚未收盤」的當日 K 棒）
# 後綴 -> (時區, 收盤時, 收盤分)
MARKET_BY_SUFFIX = {
    ".T": ("Asia/Tokyo", 15, 0),    # 東京 09:00–15:00 JST
    ".KS": ("Asia/Seoul", 15, 30),  # 首爾 09:00–15:30 KST
}
US_MARKET = ("America/New_York", 16, 0)  # 美股 09:30–16:00 ET（含 ADR，如 ASX）


def market_for(symbol: str):
    for suf, info in MARKET_BY_SUFFIX.items():
        if symbol.endswith(suf):
            return info
    return US_MARKET


def drop_in_progress(symbol, closes):
    """若最後一根日 K 是「當日盤中、尚未收盤」，剔除之，確保只用已收盤價。

    這讓腳本在任何時間執行（含盤中手動觸發）都只會寫入已結算的收盤價，
    而非盤中跳動的即時價。
    """
    if len(closes) == 0:
        return closes
    tz_name, ch, cm = market_for(symbol)
    now = datetime.now(ZoneInfo(tz_name))
    last_date = closes.index[-1].date()
    market_close = now.replace(hour=ch, minute=cm, second=0, microsecond=0)
    if last_date == now.date() and now < market_close:
        return closes.iloc[:-1]
    return closes

# 追蹤清單：顯示名稱 -> Yahoo Finance 代碼
TICKERS = {
    "Micron (MU)": "MU",
    "SanDisk (SNDK)": "SNDK",
    "Dell (DELL)": "DELL",
    "Arm (ARM)": "ARM",
    "Marvell (MRVL)": "MRVL",
    "AMD (AMD)": "AMD",
    "Intel (INTC)": "INTC",
    "Broadcom (AVGO)": "AVGO",
    "NVIDIA (NVDA)": "NVDA",
    "TSMC (TSM)": "TSM",
    "ASE Tech (ASX)": "ASX",
    "Kioxia (285A.T)": "285A.T",
    "Samsung (005930.KS)": "005930.KS",
    "SK Hynix (000660.KS)": "000660.KS",
    # Mag 7 科技巨頭（NVDA 已列於上方）
    "Apple (AAPL)": "AAPL",
    "Microsoft (MSFT)": "MSFT",
    "Alphabet (GOOGL)": "GOOGL",
    "Amazon (AMZN)": "AMZN",
    "Meta (META)": "META",
    "Tesla (TSLA)": "TSLA",
}

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
OUT_FILE = os.path.join(OUT_DIR, "prices.json")


def pct_n_back(values, n):
    """近 n 個交易日報酬率（%）。"""
    if len(values) > n:
        base = values[-1 - n]
        if base:
            return round((values[-1] - base) / base * 100, 2)
    return None


_FX_CACHE = {}


def usd_per_unit(cur):
    """1 單位 cur 等於多少美元（USD=1；其他用即時匯率）。失敗回 None。"""
    if not cur or cur == "USD":
        return 1.0
    if cur in _FX_CACHE:
        return _FX_CACHE[cur]
    rate = None
    try:
        h = yf.Ticker(f"{cur}=X").history(period="5d")  # local per USD
        c = h["Close"].dropna()
        if len(c):
            local_per_usd = float(c.iloc[-1])
            rate = (1.0 / local_per_usd) if local_per_usd else None
    except Exception as e:  # noqa: BLE001
        print(f"  FX {cur}: {e}")
    _FX_CACHE[cur] = rate
    return rate


def fetch_fundamentals(symbol):
    """市值與『今年（2026）已公布季度淨利累計』，皆換算美元。任一失敗回 None，前端退回靜態值。"""
    out = {"mcap_usd": None, "ni_usd": None, "ni_asof": None}
    try:
        t = yf.Ticker(symbol)
        info = {}
        try:
            info = t.info or {}
        except Exception:  # noqa: BLE001
            info = {}

        # 市值（以交易幣別換成美元）
        mc = info.get("marketCap")
        r_mc = usd_per_unit(info.get("currency"))
        if mc and r_mc:
            out["mcap_usd"] = round(mc * r_mc)

        # 今年淨利（以財報幣別換成美元）
        fcur = info.get("financialCurrency") or info.get("currency")
        r_fin = usd_per_unit(fcur)
        qdf = None
        try:
            qdf = t.quarterly_income_stmt
        except Exception:  # noqa: BLE001
            qdf = None
        if qdf is not None and getattr(qdf, "empty", True) is False and r_fin:
            row = None
            for key in ("Net Income", "Net Income Common Stockholders", "NetIncome"):
                if key in qdf.index:
                    row = qdf.loc[key]
                    break
            if row is not None:
                total = 0.0
                last = None
                found = False
                for col in row.index:
                    yr = getattr(col, "year", None)
                    val = row[col]
                    if yr == 2026 and val == val:  # 非 NaN
                        total += float(val)
                        found = True
                        if last is None or col > last:
                            last = col
                if found:
                    out["ni_usd"] = round(total * r_fin)
                    out["ni_asof"] = f"{last.month}/{last.day}"
    except Exception as e:  # noqa: BLE001
        print(f"  fundamentals {symbol}: {e}")
    return out


def fetch_one(symbol: str):
    t = yf.Ticker(symbol)
    hist = t.history(period="1y", interval="1d", auto_adjust=False)
    if hist.empty:
        return None

    closes = hist["Close"].dropna()
    closes = drop_in_progress(symbol, closes)  # 只保留已收盤價，剔除盤中未收盤 K 棒
    if len(closes) == 0:
        return None
    dates = [d.strftime("%Y-%m-%d") for d in closes.index]
    values = [round(float(v), 2) for v in closes.values]
    last = values[-1]

    # YTD
    year = closes.index[-1].year
    ytd_base = next((v for d, v in zip(closes.index, values) if d.year == year), None)
    ytd = round((last - ytd_base) / ytd_base * 100, 2) if ytd_base else None

    out = {
        "symbol": symbol,
        "last": last,
        "ret_1d": pct_n_back(values, 1),
        "ret_5d": pct_n_back(values, 5),
        "ret_10d": pct_n_back(values, 10),
        "ret_20d": pct_n_back(values, 20),
        "ret_ytd": ytd,
        "dates": dates,
        "closes": values,
    }
    out.update(fetch_fundamentals(symbol))  # 市值、今年淨利（美元，自動刷新）
    return out


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tw = timezone(timedelta(hours=8))
    result = {
        "updated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "updated_at_tw": datetime.now(tw).strftime("%Y-%m-%d %H:%M 台灣時間"),
        "stocks": {},
    }

    for name, symbol in TICKERS.items():
        try:
            data = fetch_one(symbol)
            if data:
                result["stocks"][name] = data
                print(f"OK  {name} ({symbol}): last={data['last']}")
            else:
                print(f"WARN {name} ({symbol}): no data")
        except Exception as e:  # noqa: BLE001
            print(f"ERR {name} ({symbol}): {e}")

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"Wrote {OUT_FILE} ({len(result['stocks'])} stocks)")


if __name__ == "__main__":
    main()
