#!/usr/bin/env python3
"""每日抓取追蹤清單股價，輸出 data/prices.json 供儀表板使用。

於 GitHub Actions 中執行（GitHub runner 具完整網路），使用 yfinance 取得資料。
每檔輸出多週期報酬率（當日/5日/10日/20日/YTD）與近一年收盤序列（供 sparkline）。
"""
import json
import os
from datetime import datetime, timezone, timedelta

import yfinance as yf

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
    "ASE Tech (ASX)": "ASX",
    "Kioxia (285A.T)": "285A.T",
    "Samsung (005930.KS)": "005930.KS",
    "SK Hynix (000660.KS)": "000660.KS",
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


def fetch_one(symbol: str):
    t = yf.Ticker(symbol)
    hist = t.history(period="1y", interval="1d", auto_adjust=False)
    if hist.empty:
        return None

    closes = hist["Close"].dropna()
    dates = [d.strftime("%Y-%m-%d") for d in closes.index]
    values = [round(float(v), 2) for v in closes.values]
    last = values[-1]

    # YTD
    year = closes.index[-1].year
    ytd_base = next((v for d, v in zip(closes.index, values) if d.year == year), None)
    ytd = round((last - ytd_base) / ytd_base * 100, 2) if ytd_base else None

    return {
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
