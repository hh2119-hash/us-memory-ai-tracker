# 美股記憶體 / AI 硬體 / Mag 7 追蹤報告
日期：2026-11-04
執行時間：台灣時間 08:00

今日主要參考來源：Yahoo Finance（收盤價）、Bloomberg、24/7 Wall St.、TradingKey、HeyGoTrade、StockTitan、Korea Times、Seeking Alpha、MarketBeat（Reuters 專門搜尋當日請求被代理拒絕，未取得；ForexFactory / FinancialJuice 當日無可用結果，已略過）。
收盤價核對：MU $855.10（+2.58%）、SNDK $1,126.52（+4.78%）— 皆為 Yahoo 11/3 官方收盤；MU 另由 MarketBeat 當日標題（MU +2.6%）與 StockAnalysis（10/30 收 $884.74 與 Yahoo 一致）交叉佐證，SNDK 第二來源（StockAnalysis）抓取失敗，僅以 11/2 跌幅（-6.59%，HeyGoTrade）與 Yahoo 序列自洽驗證，**SNDK 11/3 收盤第二來源待確認**。儀表板 prices.json 原停在 11/2，已手動重跑 GitHub Actions（run #330，已排入佇列），結果見文末。

## 1. 今日重點摘要
1. **記憶體族群 11/3 技術性反彈，但仍處修正**：MU +2.58% 收 $855.10，SNDK +4.78% 收 $1,126.52，費半（SOX）前一日（11/2）曾創 4/29 以來最低收盤。10 月 Nasdaq 約 -5.2%、SOXX 約 -17%（來源：Alain Guillot 市場回顧）。
2. **Kioxia 展望是本波記憶體下殺的導火線**：Kioxia 表示 NAND 漲價幅度已由上一季約 70% 降至 9 月季度的中段 20% 區間，預期下一季價格大致持平；營業利益指引約 ¥2 兆，低於市場預期 ¥2.35 兆（TradingKey）。Kioxia 當日 -7.14%、MU -5.30%（10/30）。重點是「漲價放緩」而非「價格下跌」。
3. **Nasdaq 100 11/2 收 27,989.82，較 10/6 高點回落 10.4%，正式進入修正**；11/3 Nasdaq-100（QQQ）+0.62%、S&P 500（SPY）+0.31%、道瓊（DIA）-0.44%。10 年期美債殖利率約 4.91%，兩位聯準會官員上週表示利率可能需要上調以對抗通膨（StockTitan）。
4. **Marvell 宣布以全股票方式收購 Lumentum（11/2）**，股價 11/2 大跌約 13%，BofA 同時降評至 Neutral、目標價由 $400 下修至 $225；11/3 MRVL 僅 +0.33% 收 $171.97。
5. **Intel 10/29 Q4 營收指引 $150–160 億，低於市場預期 $170 億**，CEO 稱 PC 疲弱將持續到「記憶體供應與價格恢復正常」，管理層預期 PC 放緩至少延續到 2027 上半年——記憶體漲價對 PC 需求的負面回饋值得留意。
6. **Micron 授權回購 $351.6 億，最快 12/9 可開始執行**（CHIPS Act 限制到期）；目前約 5 倍遠期本益比、共識目標價 $1,562（24/7 Wall St.）。
7. **SNDK 8 拆 1 股票分割**：11/19 收盤後發股、11/20 起以分割後價格交易；公司 FQ1 營收 $110.3 億（+378% YoY）、毛利率 85.1%，FQ2 指引營收 $122–126 億（TradingKey）。
8. **AMD 11/3 盤後公布財報**：本次未能取得可靠的實際數字與盤後反應（搜尋結果混有舊季度報導），請待後續確認；AMD 結果將影響 AI 加速器族群情緒。
9. **Mag 7 11/3 漲跌互見**：MSFT +2.74%、META +2.36%、AMZN +2.06%、GOOGL +0.37%，AAPL -1.90%、TSLA -1.32%；NVDA +2.29% 收 $206.69。
10. 本週事件：11/4 財政部季度再融資公告、11/6 美國 10 月非農就業報告、11/17 Nasdaq-100 最大持股財報日（24/7 Wall St. 未點名，一般認為是 NVDA，日期待公司確認）。

## 2. 個股最新消息

### SNDK / SanDisk
- 最新消息：FQ1（截至 10/2）營收創高 $110.3 億、調整後 EPS $49.51（高於指引 $44–46），資料中心營收 $48 億（+61%）、消費性營收季減 29%；FQ2 指引營收 $122–126 億、EPS $55–57；8 拆 1 分割 11/20 生效（TradingKey）。
- 股價：11/3 收 $1,126.52（+4.78%）；11/2 收 $1,075.08（-6.59%）；10/30 收 $1,150.89（-13.47%）。
- 重要新聞摘要：財報強勁，但夥伴 Kioxia 指出 NAND 漲價放緩，市場擔心「價格動能見頂」。24/7 Wall St. 引述共識目標價約 $2,143.83（17 Buy / 4 Strong Buy），但該站本身為推廣性質，數字僅供參考。
- 解讀：基本面（毛利 85%、長約 NBM）仍極強，股價下殺主因是漲價斜率變緩的預期修正。分割本身不改變價值，但常帶來散戶流動性題材。
- 對股價可能影響：短線受 NAND 報價與 Kioxia/Micron 連動；技術面支撐 $1,003（7 月低點）、壓力 $1,420（TradingKey）。
- 觀察重點：NAND 合約價 Q4/Q1 走勢、11/19–11/20 分割、YMTC 擴產、公司回購（尚餘約 $155 億授權）。

### MU / Micron
- 最新消息：11/2 因 Kioxia 展望與 AI 支出疑慮收 $833.59（-5.78%），11/3 反彈。回購授權增至 $351.6 億，最快 12/9 起執行；市值約 $9,400 億；FQ4 營收 $542.3 億（+379% YoY），超過 75% 出貨已簽約（HeyGoTrade / 24/7 Wall St.）。
- 股價：11/3 收 $855.10（+2.58%）；較 52 週高點 $1,255 低約 32%。
- 重要新聞摘要：以 FY2027 共識 EPS $176.50 計，遠期本益比不到 5 倍；49 位分析師共識目標價 $1,562。懷疑派認為記憶體循環接近高點。
- 解讀：估值極低反映市場對循環高點的定價；回購是下檔緩衝，但回購金額為授權上限而非承諾。
- 對股價可能影響：短線看 NAND/DRAM 報價、Kioxia 與 SK Hynix/Samsung 動向；12/9 前後回購題材。
- 觀察重點：12/9 回購、下次財報（預估 12 月下旬，日期以公司公告為準）、HBM4 出貨與定價、營運資本支出（Bloomberg 7/9 報導美國投資規模提升至 $2,500 億）。

### DELL / Dell
- 最新消息：本日無 Dell 個別重大新聞。
- 股價：11/3 收 $408.40（+3.98%）；10/30 -10.8%（$475.51→$424.30）、11/2 -7.4%（至 $392.78），兩日回檔約 17%。
- 重要新聞摘要：無新增個股消息；走勢隨 AI 伺服器/記憶體成本疑慮（Intel PC 展望偏弱、記憶體成本）波動。
- 解讀：Dell 同時是記憶體漲價的成本受害者與 AI 伺服器需求受惠者，最近回檔反映「毛利受壓」擔憂。
- 對股價可能影響：偏中性，看記憶體報價走勢與 AI 伺服器訂單。
- 觀察重點：下一次財報（通常 11 月底，請以公司公告為準）、AI 伺服器 backlog、PC 需求。

### ARM / Arm
- 最新消息：本日無重大個股消息。
- 股價：11/3 收 $202.49（+2.89%）；10/30 -10.0%、11/2 -4.5%。
- 解讀：隨 AI 晶片族群 beta 波動；Intel 與 AMD 的 PC 市場疲弱訊號對 PC 端授權權利金敘事有輕微壓力。
- 觀察重點：資料中心 Arm 架構滲透、客製 ASIC 專案、財報預告。

### MRVL / Marvell
- 最新消息：11/2 宣布全股票收購 Lumentum；BofA 降評至 Neutral、目標價 $400→$225（24/7 Wall St.）。
- 股價：11/3 收 $171.97（+0.33%）；11/2 收 $171.41（約 -12.7%）。
- 解讀：全股票併購造成稀釋與整合風險，買方股價通常承壓；strategic 面向是補強光通訊（AI 資料中心互連）。
- 觀察重點：交易條款與審查、分析師評等調整、客製 ASIC 訂單。

### NVDA / NVIDIA
- 最新消息：11/3 隨晶片股反彈，收 $206.69（+2.29%）；市場關注約 11/17 的財報（日期待確認），被視為 AI 資本支出疑慮的關鍵檢驗。
- 解讀：AI 支出「是否能獲得回報」是本輪修正的核心敘事（Oracle 宣布發行 $200 億債券與股票、股價 11/2 跌近 9%）。
- 觀察重點：11/17 財報、GB 系列出貨、客戶資本支出指引、AI 融資（債券發行）動向。

### TSM / TSMC
- 最新消息：本日無重大個股消息。
- 股價：11/3 收 $404.80（+1.55%）。
- 解讀：先進製程與 CoWoS 產能是 AI 晶片供給瓶頸；短線隨半導體情緒波動。
- 觀察重點：月營收（通常每月 10 日前後公布）、CoWoS 產能、先進製程報價。

### ASX / ASE Technology
- 最新消息：本日無重大個股消息。
- 股價：11/3 收 $39.05（-0.31%），相對抗跌。
- 觀察重點：先進封裝（CoWoS 周邊）接單、封測稼動率。

### Kioxia
- 最新消息：發布財報與展望（11/2 前後）：NAND 漲幅降至中段 20%、下一季價格預期持平，營業利益指引約 ¥2 兆低於共識 ¥2.35 兆；CFO 稱主因出貨時點，部分訂單遞延。
- 股價：10/30 -7.14%；儀表板 11/2 參考值 ¥11,345（11/3 收盤未取得可靠數字）。
- 解讀：Kioxia 為 SNDK 製造夥伴，其「漲價放緩」訊號直接影響 SNDK、MU 的評價。公司同時表示資料中心需求仍強。
- 觀察重點：NAND 報價是否轉為持平/下降、YMTC 對價格的衝擊。

### Samsung Electronics
- 最新消息：本日未取得可靠的 11/3–11/4 個股新聞；Bloomberg 7/30 報導 Samsung 與 SK Hynix 公布創紀錄獲利。
- 股價：儀表板 11/2 參考值 ₩229,000（11/3 收盤待確認）。
- 觀察重點：HBM4 認證與出貨、DRAM/NAND 合約價、韓股外資動向。

### SK Hynix
- 最新消息：本日未取得可靠的 11/3–11/4 個股新聞；6 月起市值超越 Samsung 登上 KOSPI 第一（Korea Times 6/22）。
- 股價：儀表板 11/2 參考值 ₩1,472,000（11/3 收盤待確認）。
- 觀察重點：HBM 供應、Nvidia 訂單、與 Kioxia/Micron 同步的報價訊號。

## 2-A. Mag 7 科技巨頭追蹤

| 公司代號 | 近期動態 | 股價（11/3 收盤，Yahoo） | 解讀 |
|---|---|---|---|
| AAPL | 11/3 下跌 1.90%（約蒸發 $940 億市值） | $331.90（-1.90%） | 與記憶體成本壓力、PC/手機需求疑慮相關，需留意記憶體漲價對毛利影響 |
| MSFT | 隨 AI 概念反彈 | $520.99（+2.74%） | 雲端與 AI 資本支出指標股，反彈支持 AI 伺服器需求敘事 |
| GOOGL | 小幅上漲 | $280.03（+0.37%） | TPU/自研晶片與資料中心支出 |
| AMZN | 反彈 | $250.69（+2.06%） | AWS 資本支出影響 AI 伺服器與記憶體需求 |
| META | 反彈 | $621.03（+2.36%） | 資本支出規模為 AI 硬體最大需求來源之一 |
| NVDA | 晶片反彈 | $206.69（+2.29%） | 11/17 財報為關鍵 |
| TSLA | 下跌 | $398.50（-1.32%） | 與本清單連動較低 |

Mag 7 共同觀察：本輪修正的核心不是需求消失，而是市場懷疑 AI 資本支出的回報與融資方式（Oracle 發債/增資是代表）。Mag 7 反彈幅度顯示資金暫時回流，但如果 AI 資本支出指引下修，記憶體與 AI 伺服器鏈將首當其衝。價格為參考值並標明日期，個股當日收盤總覽以儀表板網頁為準。

## 3. 產業共同趨勢
- **DRAM / HBM**：AI 需求持續造成供給吃緊；Bloomberg 與 TrendForce 一整年報導 DRAM、NAND 價格大幅上升，近期市場焦點轉為「漲幅是否放緩」。本日未取得最新 Q4 合約價明確數字。
- **NAND Flash / Memory pricing**：Kioxia 指出漲幅降至中段 20%、下一季持平，是最重要的邊際變化；Q1 2026 NAND 營收曾達創紀錄約 $460 億（EMSNow/Wccftech 報導）。
- **AI Server / Data center capex**：Oracle 籌資 $200 億、AI 回報疑慮是本輪回檔主因；Dell 與 Mag 7 的資本支出指引為下一步觀察點。
- **PC / Server demand**：Intel Q4 指引疲弱，並預期 PC 放緩至少到 2027 上半年；記憶體漲價抑制 PC 出貨。
- **半導體供應鏈 / AI accelerator**：Marvell-Lumentum 交易反映光互連整合趨勢；TSM 先進製程與 CoWoS 仍為瓶頸，ASX 先進封裝受惠。
- **YMTC / 長江存儲（中國變數）**：Counterpoint 數據顯示 YMTC NAND 營收市佔由 2025 Q1 的 8% 升至 Q4 的 11%；HSBC 估計其出貨量市佔 Q3 已達約 13%，接近 Micron 的 14%；武漢新產線可能於 2026 下半年啟動，並籌備 IPO（Korea Times 6/6）。**CXMT / 長鑫**：DRAM 市佔 2025 Q4 約 5%（去年同期 4%），上海 IPO 獲准約 300 億人民幣；技術落後商用 DRAM 約 3 年、HBM 約 4 年。HSBC 認為威脅「真實但不對稱」，最先衝擊成熟與消費性市場。對 SNDK、MU、Kioxia：若 NAND 漲價放緩疊加中國擴產，將壓縮報價上行空間。

## 4. 新聞重要性分級
- **高重要性**：Kioxia NAND 價格展望（漲幅放緩、下季持平）；Nasdaq 100 進入修正與 AI 支出疑慮；Marvell 收購 Lumentum 與 BofA 降評；SNDK 財報與 8 拆 1。
- **中重要性**：Micron $351.6 億回購授權（12/9 起）；Intel Q4 指引與 PC 疲弱；YMTC/CXMT 擴產與 IPO；AMD 財報（結果待確認）。
- **低重要性**：Mag 7 個別漲跌（AAPL、TSLA）；ASX、TSM 無個股新聞。

## 5. 需要持續追蹤的訊號（未來 1-2 週）
- 11/4 季度再融資公告、11/6 美國非農就業報告、美國期中選舉結果、聯準會官員言論（利率走向）。
- 11/17 財報（NVDA，日期待確認）；Dell 財報（預計 11 月底，待公司確認）。
- 11/19–11/20 SNDK 分割生效。
- TrendForce / DRAMeXchange 11 月合約價與 Q1 2027 報價預期。
- 12/9 Micron 回購可開始；Micron 下次財報日期。
- Kioxia、Samsung、SK Hynix 的 HBM4 與 NAND 報價評論。
- 分析師評等與目標價調整（特別是 MRVL、SNDK、MU）。
- YMTC IPO 與武漢新產線進度、美國出口管制動態。

## 6. 前瞻觀點與分析師綜合看法

**(a) 多面向分析**
- ①基本面：MU、SNDK 營收年增數倍、毛利率極高（SNDK 調整後 85.1%），訂單可見度高（MU 超過 75% 出貨已簽約）；但約三分之二成長來自價格上漲（24/7 Wall St. 對 SNDK 的說法），價格動能是關鍵變數。
- ②估值面：MU 遠期本益比約 5 倍（FY2027 共識 EPS $176.50），SNDK 遠期約 5 倍；Western Digital 約 17 倍。低本益比反映市場把盈利視為循環高峰；若報價持平，EPS 估值可能下修。
- ③技術面：MU 距高點約 -32%，SNDK 距 52 週高點約 -41%（以 24/7 Wall St. 提供的高點計），SNDK RSI 接近 30 的超賣區（TradingKey）；支撐 SNDK $1,003、$778，壓力 $1,420、$1,472。11/3 為反彈而非趨勢反轉確認。
- ④籌碼/資金面：10 月 SOXX 約 -17%，資金輪動至週期股與銀行（24/7 Wall St. 指出 11/2 多數板塊上漲）；MU 回購（12/9 起）與 SNDK 回購（剩約 $155 億授權）提供潛在買盤。
- ⑤產業循環位置：漲價「加速度」下降屬循環中後段訊號；AI 需求與長約使谷底風險低於過往循環，但 PC/手機端需求已出現壓抑（Intel 指引）。

**(b) 分析師目標價與評級**
- MU：49 位分析師共識目標價約 $1,562（24/7 Wall St. 11/3）；28 位分析師近 30 天上修 FY2027 EPS、2 位下修。
- SNDK：24/7 Wall St. 彙整共識目標價約 $2,143.83（17 Buy、4 Strong Buy），該站自家目標價 $1,458.63（多方情境 $2,408.84、空方 $1,070.05）；此站內容含推廣性質，僅供參考。
- MRVL：BofA 降至 Neutral，目標價 $400→$225（24/7 Wall St. 11/3）。
- 多空理由：多方看 AI 長約、供不應求與低估值；空方看漲價放緩、AI 支出回報疑慮、中國擴產與循環高點。

**(c) 情境推演（6–12 個月）**
- 多頭：NAND/DRAM 報價持續上行或高檔持平、HBM4 順利放量、NVDA 11/17 與 Mag 7 資本支出指引維持高檔、回購啟動 → MU、SNDK 估值修復，向分析師共識目標靠攏。
- 基準：報價高檔盤整、成長放緩但獲利仍創高，股價在區間震盪，由回購與財報支撐。
- 空頭：報價轉為下滑、AI 資本支出下修或融資受阻、YMTC/CXMT 擴產壓低價格、PC/手機需求持續萎縮 → 盈利預期下修，股價可能測試 SNDK $1,003 乃至 $778 等技術支撐。

**(d) 前瞻催化劑時間軸**
- 近期（1–2 週）：非農、期中選舉結果、財政部再融資、AMD 財報反應、TSMC 10 月營收。
- 1–2 個月：11/17 財報（NVDA，日期待確認）、11/19–20 SNDK 分割、Dell 財報、12/9 Micron 回購、Micron 12 月財報、Q1 2027 合約價談判。
- 中期：YMTC IPO 與新廠、CXMT IPO、HBM4 世代競爭、2027 上半年 PC 需求復甦與否、美國出口管制。

以上為綜合市場與分析師公開觀點及情境推演，非投資建議，個股估值偏高請自行評估風險。

## 7. 結論
昨日（11/3）記憶體與 AI 硬體股在連續下殺後技術性反彈，MU +2.58%、SNDK +4.78%，但 Nasdaq 100 仍處修正，關鍵變數是 Kioxia 提出的 NAND「漲價放緩」。短線最值得關注 SNDK（分割、財報、Kioxia 連動）、MU（12/9 回購）與 NVDA（11/17 財報）。風險包括 AI 資本支出回報疑慮、殖利率約 4.9% 與利率可能上調、PC 需求疲弱，以及 YMTC/CXMT 擴產。Samsung、SK Hynix、Kioxia 的 11/3 收盤與 AMD 財報細節本次未能確認，請以儀表板與後續報導為準。

### 來源連結
- [Stock Market Today Live, Nov 3 — StockTitan](https://www.stocktitan.net/articles/stock-market-today-live-november-3-2026)
- [Nasdaq 100 Officially in a Correction — 24/7 Wall St.](https://247wallst.com/investing/2026/11/03/the-nasdaq-100-is-now-officially-in-a-correction/)
- [AMD, Intel, Marvell chip bounce — 24/7 Wall St.](https://247wallst.com/investing/2026/11/03/amd-advances-5-intel-rises-4-marvell-gains-2-as-chip-stocks-bounce-ahead-of-amd-earnings/)
- [Micron under 5x earnings, $35B buyback — 24/7 Wall St.](https://247wallst.com/investing/2026/11/03/micron-now-trades-at-under-5-times-earnings-with-a-35-billion-buyback-weeks-away/)
- [Micron Stock (MU) Falls 5.8% as Memory Stocks Slide — HeyGoTrade](https://www.heygotrade.com/en/news/micron-mu-stock-news-november-3-2026/)
- [Sandisk Stock Forecast: Kioxia's NAND Warning — TradingKey (11/2)](https://www.tradingkey.com/analysis/stocks/us-stocks/262263726-sandisk-stock-forecast-kioxia-nand-warning-8-for-1-split-1003-support-november-2-2026-tradingkey)
- [SanDisk back in the spotlight — 24/7 Wall St. (11/2)](https://247wallst.com/investing/2026/11/02/sandisk-is-back-in-the-spotlight-heres-where-i-see-sndk-stock-heading-next/)
- [Stock Market Recap Nov 3 — Alain Guillot](https://www.alainguillot.com/stock-market-recap-november-3/)
- [Chinese memory firms edge closer to challenging Korea's chip giants — Korea Times](https://www.koreatimes.co.kr/business/companies/20260606/chinese-memory-firms-edge-closer-to-challenging-koreas-chip-giants)
- [Bloomberg: AI-driven memory chip shortage](https://www.bloomberg.com/graphics/2026-ai-boom-memory-chip-shortage/)
- [Bloomberg: Samsung, SK Hynix record profits (7/30)](https://www.bloomberg.com/news/articles/2026-07-30/samsung-sk-hynix-answer-ai-doubters-with-big-numbers-and-deals)
- [Bloomberg: Micron boosts US spending to $250B (7/9)](https://www.bloomberg.com/news/articles/2026-07-09/micron-boosts-us-spending-to-250-billion-amid-memory-demand)
- [Yahoo Finance — MU](https://finance.yahoo.com/quote/MU/)
