# 美股記憶體 / AI 硬體追蹤

每日自動追蹤以下標的的股價與中文新聞報告，並以互動式儀表板呈現。

**追蹤清單**：Micron (MU)、SanDisk (SNDK)、Dell (DELL)、Arm (ARM)、Kioxia (285A.T)、Samsung (005930.KS)、SK Hynix (000660.KS)

## 🔗 線上儀表板

啟用 GitHub Pages 後，網址為：
`https://<你的帳號>.github.io/us-memory-ai-tracker/`

## 📂 結構

```
├── index.html                    # 互動式儀表板（GitHub Pages）
├── data/prices.json              # 最新股價資料（Actions 自動更新）
├── reports/
│   ├── latest.md                 # 最新一份中文報告（儀表板讀取）
│   └── YYYY-MM-DD.md             # 每日報告存檔
├── scripts/
│   ├── update_prices.py          # 抓取 7 檔股價
│   └── requirements.txt
└── .github/workflows/daily-update.yml   # 每日排程（台灣 08:00 / 20:00）
```

## ⚙️ 自動更新機制

GitHub Actions（`.github/workflows/daily-update.yml`）以 cron `0 0,12 * * *`
（UTC 00:00 / 12:00，即台灣時間 08:00 / 20:00）每日執行，抓取最新股價、
重新產生 `data/prices.json` 並自動 commit。儀表板每次開啟即讀取最新資料。

> 股價圖表為全自動。每日「中文新聞報告」需另以排程任務產生後更新 `reports/latest.md`
> （AI 摘要無法在純 GitHub Actions 內完成）。

## 啟用步驟

1. Settings → Pages → Source 選 `main` 分支、根目錄 `/`，儲存。
2. Actions 頁籤確認 workflow 已啟用；可按 **Run workflow** 立即產生首份股價資料。

---
*資料僅供參考，非投資建議。*
