#!/usr/bin/env python3
"""每日抓取追蹤清單股價，輸出 data/prices.json 供儀表板使用。

於 GitHub Actions 中執行（GitHub runner 具完整網路），使用 yfinance 取得資料。
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
    "ASE Tech (ASX)": "ASX",
    "Kioxia (285A.T)": "285A.T",
    "Samsung (005930.KS)": "005930.KS",
    "SK Hynix (000660.KS)": "000660.KS",
}

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
OUT_FILE = os.path.join(OUT_DIR, "prices.json")


def fetch_one(symbol: str):
    """回傳近一年日線收盤序列與摘要統計。"""
    t = yf.Ticker(symbol)
    hist = t.history(period="1y", interval="1d", auto_adjust=False)
    if hist.empty:
        return None

    closes = hist["Close"].dropna()
    dates = [d.strftime("%Y-%m-%d") for d in closes.index]
    values = [round(float(v), 2) for v in closes.values]

    last = values[-1]
    prev = values[-2] if len(values) > 1 else last
    day_chg = round((last - prev) / prev * 100, 2) if prev else 0.0

    # 年初至今
    year = closes.index[-1].year
    ytd_base = None
    for d, v in zip(closes.index, values):
        if d.year == year:
            ytd_base = v
            break
    ytd_chg = round((last - ytd_base) / ytd_base * 100, 2) if ytd_base else None

    return {
        "symbol": symbol,
        "last": last,
        "day_change_pct": day_chg,
        "ytd_change_pct": ytd_chg,
        "high_52w": round(float(closes.max()), 2),
        "low_52w": round(float(closes.min()), 2),
        "dates": dates,
        "closes": values,
    }


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tw = timezone(timedelta(hours=8))
    now_tw = datetime.now(tw)

    result = {
        "updated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "updated_at_tw": now_tw.strftime("%Y-%m-%d %H:%M 台灣時間"),
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
