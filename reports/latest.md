# 美股記憶體 / AI 硬體 / Mag 7 追蹤報告
日期：2026-11-18
執行時間：台灣時間 08:00（涵蓋 11/17 週二美股盤中、收盤與 Nvidia 財報後盤後，亞洲 11/17 收盤）

今日主要參考來源：Yahoo Finance（報價 API、Nvidia 財報直播）、StockAnalysis（收盤交叉核對）、TradingKey、StockTitan、Motley Fool、24/7 Wall St.、Reuters（經 MarketScreener 轉載）、Investing.com、TrendForce、Seoul Economic Daily、JKN、Trading Economics、GuruFocus／TradingView、Trefis、Admirals（總經日曆）。CNBC、NBC News 內文本日無法讀取（僅取標題）；Bloomberg／WSJ 僅能透過轉載與標題層級引用；ForexFactory／FinancialJuice 本日查無可用的 11/18 即時頁面，總經資料改以 Admirals 與 Reuters 轉載補足。
收盤價核對：MU $712.42（−0.92%）、SNDK $797.24（−1.47%）— 11/17 收盤；Yahoo 報價 API（regularMarketTime 為美東 16:00 收盤）與 StockAnalysis 歷史頁兩來源完全一致。儀表板 prices.json 原停在 11/16（排程於收盤前 20:17 UTC 執行），已手動「Run workflow」（#367）重跑，重跑後全部 20 檔已同步至 11/17 收盤。

## 1. 今日重點摘要

- **Nvidia Q3 FY27 財報大幅優於預期，盤後反彈**：營收 $1,158 億（年增 103%，市場預期約 $1,091 億）、資料中心 $1,076 億（年增 110%）、調整後 EPS $2.68（預期 $2.47）；Q4 營收指引 $1,300 億 ±3%（含多一週，不含中國資料中心）。NVDA 正常盤收 $155.46（−0.44%），盤後一度 +4% 以上（約 $159.9）。這是 Jensen Huang 11/12 辭任後首份財報，董事會表示無意讓黃仁勳復任 CEO。
- **記憶體股收盤前仍弱、盤後跟漲**：MU 收 $712.42（−0.92%，盤中一度低至 $666.88、跌破 $700），盤後約 +4.5%（StockTitan 美東 18:24）；SNDK 收 $797.24（−1.47%，盤中低點 $749.39）。兩檔 11 月迄今分別約 −22%／−32%。
- **費半止跌小漲**：SOX 收 9,642.88（+0.34%），前一日 −5.28%；但 Nasdaq 收 24,328（−0.74%，盤中最多跌約 2.1%、創 4 月來低）、S&P 500 收 7,340.53（−1.03%）、道瓊約 −1.6%。
- **NAND 現貨價急跌是新的利空訊號**：TrendForce（11/17）指 NAND 現貨價兩週內下跌約 20%；美銀指 512Gb wafer 現貨季減 32% 至 $14.30、1Tb 跌 19% 至 $24.90，並預估 1Q27 手機／PC NAND 合約價季減 5–10%。YMTC 在消費級市場搶市佔被點名為壓力來源之一，對 SNDK、Kioxia 衝擊最直接。
- **美國出口管制再收緊**：商務部 BIS 暫行最終規則（預定 11/19 刊登）新增對印尼、馬來西亞、新加坡、泰國、巴西出貨先進晶片的許可要求，並限縮晶圓代工／封裝廠對「先進邏輯晶片」推定的反駁空間，另管制遠端存取先進晶片。TSM 收 $359.69（−3.68%）、ASX 收 $31.83（−2.96%）。
- **亞洲記憶體股續挫**：11/17 KOSPI 收 4,968.48（−2.59%），九個月來首度跌破 5,000；三星 ₩190,300（−3.30%）、SK 海力士 ₩1,098,000（−1.96%，七個月來首度跌破 110 萬韓元）、Kioxia ¥7,966（−5.08%）。外資單日賣超韓股約 1.44 兆韓元。
- **AI capex 疑慮仍在**：SemiAnalysis 下修 2027 年 AI 資本支出預估由 $7,700 億至 $6,270 億（−19%），2028–2029 下修幅度更大；這是近兩個月半導體股回檔主因之一。費半自 9/30 起至 11/16 累跌約 24%，有望成為 2008 年以來最差的兩個月。
- **總經偏鷹**：美 10 年債殖利率仍在 5.1% 以上；CME FedWatch 顯示 12 月升息 1 碼機率約 95%。FOMC 會議紀要將於美東 11/18 14:00（台灣 11/19 03:00）公布；Anthropic IPO 預計 11/18 定價（區間 $70–78）、11/19 於 Nasdaq 掛牌，可能牽動 AI 資金流向。
- **法律風險**：美國法院 11/14 駁回三星、SK 海力士、美光 DRAM 價格操縱集體訴訟的駁回動議，訴訟續行（三星答辯期限 12/7）。

## 2. 個股最新消息

### SNDK / SanDisk
- 最新消息：連續第三天下跌，近兩日主要受 Nvidia CEO 風波、AI capex 下修與 NAND 現貨價急跌拖累。Motley Fool「Read Next」欄位出現「SanDisk 11/19 進行 1 拆 8 股票分割」標題，惟本日未能在公司公告確認，**待確認**。
- 股價：11/17 收盤 $797.24（−1.47%）；11/16 收盤 $809.11（−8.58%）。盤中區間 $749.39–$821.46。11 月迄今約 −32%。
- 重要新聞摘要：TrendForce 指 NAND 現貨價兩週跌約 20%，消費性需求疲弱、中國通路去庫存、YMTC 擴產；不過企業級 SSD 合約價 4Q26 仍預估季增 15–20%。
- 解讀：SNDK 營收結構中消費性與行動 NAND 比重高於 MU，現貨價反轉對其情緒衝擊最大；企業級 SSD（AI 推論儲存）仍是支撐點。Nvidia 財報強勁、Rubin 出貨放量，對 AI 儲存需求屬正面。
- 對股價可能影響：短線可望跟隨 Nvidia 盤後反彈；但若 NAND 合約價在 1Q27 確實轉跌，基本面敘事將由「缺貨漲價」轉為「週期見頂」，評價壓力仍大。
- 觀察重點：股票分割是否確認生效、NAND 合約價（12 月初報價）、企業級 SSD 訂單、YMTC IPO 與擴產進度。

### MU / Micron
- 最新消息：11/17 盤中跌破 $700 支撐（低點 $666.88），尾盤收斂；Nvidia 財報後盤後反彈約 4.5%。Motley Fool 指 12/9 起 CHIPS Act 對買回的限制放寬，公司可望加速庫藏股。
- 股價：11/17 收盤 $712.42（−0.92%）；11/16 收盤 $719.02（−7.62%）。52 週區間 $192.59–$1,255.00，自高點回落約 43%。
- 重要新聞摘要：Trefis 指 MU 目前本益比已低於 10 倍；FinanceFeeds 情境分析給出多頭 $798／空頭 $656 區間。美銀先前已將 MU 從首選名單移除（TIKR 報導，時間未精確確認）。
- 解讀：MU 的 DRAM/HBM 比重高，受 NAND 現貨跌價影響小於 SNDK；TrendForce 仍預期 4Q26 DRAM 合約價上漲（PC DRAM +13–18%）。Nvidia 上修資料中心與 Rubin 放量，對 HBM4 需求屬直接利多。目前股價主要受 AI capex 疑慮與高利率（10 年債 >5%）壓抑評價。
- 對股價可能影響：短線偏向技術性反彈；能否站回 $750–$780（11/13 收盤 $778.31）是關鍵。若跌破 $666 盤中低點，下一支撐看 $650 附近。
- 觀察重點：FQ1 財報（預計 12 月中下旬，以公司公告為準）、12/9 起買回動作、HBM4 出貨與定價、DRAM 合約價。

### DELL / Dell
- 最新消息：本日暫無重大個別新聞。24/7 Wall St.（11/9）指 Dell 與 HPE 先前是 AI 伺服器贏家，但遭板塊拋售拖累，市場等待財報（預計 11 月下旬，日期以公司公告為準）。
- 股價：11/17 收盤 $322.79（+0.70%）；11/16 收盤 $320.55。
- 解讀：Nvidia 資料中心營收年增 110%、Rubin 放量，代表 AI 伺服器組裝需求仍強，對 Dell 的 AI 伺服器訂單與 backlog 是正面參考；但記憶體成本上升可能壓縮 PC/伺服器毛利。
- 對股價可能影響：Nvidia 財報對其屬中性偏多；財報前波動預期加大。
- 觀察重點：FQ3 財報的 AI 伺服器出貨、backlog、毛利率與記憶體成本轉嫁能力。

### ARM / Arm
- 最新消息：11/16 隨 AI 晶片股重挫約 8% 後，11/17 反彈；本日未查到明確個別催化劑，研判為超跌反彈。
- 股價：11/17 收盤 $183.39（+4.76%）；11/16 收盤 $175.05。
- 解讀：Nvidia Vera（Arm 架構 CPU）隨 Rubin 平台放量，對 Arm 授權與權利金屬長線正面。
- 對股價可能影響：Nvidia 財報後情緒改善，短線有延續反彈機會，但高評價使其對利率與 capex 消息敏感。
- 觀察重點：資料中心 CPU 權利金、與 Nvidia／雲端客製 CPU 合作進展。

### MRVL / Marvell
- 最新消息：Trefis（11/17）分析 11/16 跌逾 7% 原因為 AI 晶片拋售擴大；Motley Fool 指 MRVL 自 2026 高點已跌逾 50%。
- 股價：11/17 收盤 $148.74（+2.33%）；11/16 收盤 $145.36。
- 解讀：客製化 ASIC 與光通訊需求取決於雲端 capex，SemiAnalysis 下修 capex 預估對其衝擊直接；Nvidia 財報顯示 AI 支出未見明顯放緩，有助緩解疑慮。
- 對股價可能影響：短線跟隨 AI 板塊反彈；中期看財報（預計 12 月初）對客製 ASIC 營收的指引。
- 觀察重點：FQ3 財報日、客製 ASIC 客戶進展、光模組（800G/1.6T）出貨。

### NVDA / NVIDIA
- 最新消息：Q3 FY27（截至 10/25）營收 $1,158.4 億（年增 103%、季增 20%）；資料中心 $1,076 億（超大型雲端 $601 億、AI 雲／工業／企業 $475 億）；GAAP/調整後毛利率 74.8%/74.9%；調整後 EPS $2.68；自由現金流 $437.8 億。Q4 指引營收 $1,261–1,339 億（中位數 $1,300 億）、毛利率 71–72%。Vera Rubin 營收季增近 $200 億，Kress 稱出貨「開局強勁」。BigGo 報導回購授權提高至 $2,270 億（未經官方新聞稿核實）。
- 股價：11/17 收盤 $155.46（−0.44%）；盤後一度 +4% 以上（約 $159.9）。
- 重要新聞摘要：黃仁勳 11/12 因爭議辭任，CFO Colette Kress 任臨時 CEO；董事會表示無意讓其復任，FT 報導其盟友推動回歸。財報前至少 10 家券商降至持有，Bernstein 降至 Market Perform、目標價 $200。
- 解讀：基本面明顯未受領導層風波影響，Q4 毛利率指引下滑 3 個百分點反映 Rubin 初期量產成本；指引不含中國，加上新出口管制，中國仍是零貢獻。
- 對股價可能影響：財報有助止穩 AI 板塊情緒，但「治理風險折價」短期難完全消除。
- 觀察重點：CEO 遴選進度、Rubin 毛利率爬升、出口新規對東南亞出貨的影響。

### TSM / TSMC
- 最新消息：美國 BIS 新規限縮晶圓代工廠對先進邏輯晶片推定的反駁空間，增加客戶盡職調查負擔；GuruFocus 報導 TSM 盤中跌 4.26%。
- 股價：11/17 收盤 $359.69（−3.68%）；台股 2330 11/17 收 NT$2,170（−2.03%）。
- 解讀：屬合規成本上升而非直接營收損失；Nvidia 營收指引強勁、Rubin 供應鏈逾 150 家台灣夥伴，CoWoS 需求無虞。
- 對股價可能影響：短線受政策壓抑，中期仍由 AI 需求主導。
- 觀察重點：11/19 新規正式刊登內容、11 月營收（12 月上旬）、CoWoS 擴產。

### ASX / ASE Technology
- 最新消息：本日暫無重大個別新聞；隨出口管制新規（同樣涉及封裝廠）走弱。
- 股價：11/17 收盤 $31.83（−2.96%）。
- 解讀：先進封裝（CoWoS 外包、測試）受惠 Rubin 放量，新規增加合規成本。
- 觀察重點：先進封裝營收比重、11 月營收。

### Kioxia
- 最新消息：11/17 東京股價大跌，與 NAND 現貨價急跌、日股連四跌同步。
- 股價：11/17 收盤 ¥7,966（−5.08%）；日經 225 收 58,860（−1.34%）。
- 解讀：Kioxia 為純 NAND 廠，對現貨價與 YMTC 競爭最敏感。
- 觀察重點：NAND 合約價、與 SanDisk 合資廠產能規劃、YMTC 擴產。

### Samsung Electronics
- 最新消息：11/17 下跌 3.3%；Reuters 指新出口規則可能使三星晶圓代工面臨額外客戶盡職調查與許可；DRAM 價格操縱集體訴訟續行。
- 股價：11/17 收盤 ₩190,300（−3.30%）。
- 解讀：主要受外資撤出韓股與 AI 半導體拋售拖累；HBM4 供應 Nvidia 進度仍是中期主軸。
- 觀察重點：11/18 韓股是否跟隨 Nvidia 盤後反彈、HBM4 驗證與出貨。

### SK Hynix
- 最新消息：宣布 5 年投資 1.4 兆韓元扶植國內供應商（市場反應平淡）；七個月來首度跌破 110 萬韓元；ADR（SKHY）11/16 收 $122.18（−7.29%），掛牌後新低。
- 股價：11/17 收盤 ₩1,098,000（−1.96%）。
- 解讀：HBM 龍頭，Nvidia 資料中心與 Rubin 數據對其最直接；韓股融資比重高（三星與 SK 海力士占信用融資逾四分之一），波動放大。
- 觀察重點：HBM4 供應份額、韓股外資流向。

## 2-A. Mag 7 科技巨頭追蹤（AAPL／MSFT／GOOGL／AMZN／META／NVDA／TSLA）

| 公司代號 | 近期動態 | 11/17 收盤（參考值） | 解讀 |
|---|---|---|---|
| AAPL | 本日暫無重大更新；記憶體成本上升推高手機售價、延緩換機（TrendForce） | $351.91（−0.25%） | 記憶體漲價壓縮硬體毛利，也削弱消費級 NAND 需求 |
| MSFT | 隨大盤與 AI capex 疑慮走弱 | $506.24（−2.27%） | 市場對雲端 capex 回報更挑剔；Nvidia 超大型雲端營收 $601 億顯示採購仍強 |
| GOOGL | 本日暫無重大更新 | $280.20（−1.24%） | TPU 自研與 Nvidia 採購並行，capex 動向為記憶體需求關鍵 |
| AMZN | 本日暫無重大更新 | $257.89（+0.05%） | Trainium 與 AWS capex 為 HBM／企業 SSD 需求來源 |
| META | 隨科技股走弱 | $618.87（−1.20%） | 大規模 AI 資料中心建置仍是記憶體需求主力 |
| NVDA | Q3 營收 $1,158 億、Q4 指引 $1,300 億；CEO 換人風波 | $155.46（−0.44%），盤後 +3–4% | AI 硬體需求最上游指標，財報確認需求未降溫 |
| TSLA | 本日暫無重大更新 | $380.11（+0.10%） | AI 訓練算力採購對 GPU／記憶體屬邊際需求 |

**Mag 7 共同觀察**：Nvidia 財報顯示超大型雲端業者仍在大舉採購 AI 算力，與 SemiAnalysis 下修 capex 預估的敘事有落差，市場將在接下來各家財報與 2027 capex 指引中檢驗誰對。高利率（10 年債 >5%）同時壓抑大型科技股評價。價格為 11/17 收盤參考值，個股當日收盤總覽以儀表板為準。

## 3. 產業共同趨勢

- **DRAM／HBM**：TrendForce 預估 4Q26 PC DRAM 合約價漲 13–18%、整體 DRAM 合約價漲 10–15%，但現貨市場停滯。HBM 需求仍由 Nvidia Blackwell Ultra／Rubin 推動；Rubin 營收季增近 $200 億是 HBM4 放量的直接證據。DRAM 價格操縱集體訴訟續行為法律雜音。
- **NAND Flash（含 YMTC／CXMT）**：NAND 現貨價兩週跌約 20%，美銀預估 1Q27 手機／PC NAND 合約價季減 5–10%、企業級持平或微漲；TrendForce 仍預估 4Q26 企業級 SSD 合約價季增 15–20%。**YMTC／長江存儲**被點名在價格敏感的消費級市場擴大市佔、提升通用型 NAND 產出；Bloomberg 報導其上海 IPO 最快 1Q27，Reuters 指其第四座晶圓廠目標 70% 設備國產化（第三廠略高於 50%）。Counterpoint 先前指 YMTC 已躋身全球 NAND 第三並計畫進軍 DRAM。**CXMT／長鑫存儲**擴產亦被視為 DRAM 中長期供給變數。影響評估：對 Kioxia、SNDK 的消費級 NAND 報價壓力最大，MU 的 NAND 比重較低、受影響相對有限；企業級 SSD 暫時仍是西方廠商護城河。
- **AI Server／Data center capex**：Nvidia 資料中心年增 110%、Q4 指引季增約 12%，與 SemiAnalysis 下修 2027 capex 19% 的觀點形成多空拉鋸。
- **PC／手機需求**：記憶體成本推升終端售價，消費者延後換機、基本容量下修，消費級需求轉弱。
- **供應鏈與政策**：BIS 新規擴大至東南亞與巴西出貨許可、收緊代工／封裝廠責任，並管制遠端存取先進晶片；TSM、ASX、三星晶圓代工合規成本上升。
- **AI accelerator 生態**：MRVL 客製 ASIC 與光通訊、ARM 架構 CPU（Nvidia Vera）、TSM 先進製程與 CoWoS、ASX 先進封裝皆受惠 Rubin 放量，但短線都被 capex 疑慮與政策壓抑評價。

## 4. 新聞重要性分級

- **高重要性**：Nvidia Q3 財報與 Q4 指引優於預期；NAND 現貨價兩週跌 20%、美銀預估 1Q27 NAND 合約價轉跌；BIS 出口管制新規（11/19 刊登）；Nvidia CEO 辭任與治理風險。
- **中重要性**：SemiAnalysis 下修 AI capex；FOMC 會議紀要與 12 月升息預期；Anthropic IPO 定價；YMTC IPO 與擴產；KOSPI 跌破 5,000 與外資撤出；MU 12/9 起可加速買回。
- **低重要性**：SK 海力士 1.4 兆韓元供應商投資；DRAM 價格操縱訴訟進程；SNDK 股票分割（待確認）。

## 5. 需要持續追蹤的訊號（未來 1-2 週）

- **11/18（美東）**：FOMC 會議紀要（台灣 11/19 03:00）、Anthropic IPO 定價；亞洲記憶體股對 Nvidia 財報的反應。
- **11/19**：BIS 新規正式刊登；Anthropic 掛牌；SNDK 股票分割是否生效（待確認）。
- **11 月下旬**：Dell FQ3 財報（日期以公告為準）、HPE 財報；12 月初 Marvell 財報。
- **12/7–12/9**：三星集體訴訟答辯期限、FOMC 會議（市場預期升息 1 碼）、MU 買回限制放寬。
- **記憶體報價**：TrendForce 月底／12 月初 DRAM／NAND 合約價；NAND 現貨是否止跌。
- **HBM 供應**：HBM4 在 Rubin 平台的份額分配（SK 海力士／三星／美光）。
- **大廠 capex**：雲端業者對 2027 capex 的最新表態。
- **YMTC／長江存儲**：IPO 申報進度、第四座廠設備國產化與擴產、消費級 NAND 報價策略。

## 6. 前瞻觀點與分析師綜合看法

**(a) 多面向分析法綜合**
- ①基本面：Nvidia 財報證實 AI 算力需求仍高速成長，HBM 與企業級 SSD 需求有支撐；但消費性 NAND 已出現現貨跌價，記憶體「全面缺貨」敘事出現裂縫。
- ②估值面：MU 本益比已降至 10 倍以下（Trefis），SNDK 前瞻本益比在部分作者估算中甚低；若記憶體週期見頂，低本益比可能是「週期性陷阱」，市場正在用更低倍數反映 2027 獲利高峰風險。
- ③技術面與股價位階：MU 自 52 週高點 $1,255 回落約 43%，盤中跌破 $700 後收回；SNDK 11 月迄今約 −32%。費半連兩月大跌，短線超賣、反彈條件成形，但趨勢尚未扭轉。
- ④籌碼／資金面：韓股外資連日大賣、退休基金大量減碼；三星與 SK 海力士占韓股信用融資逾四分之一，去槓桿可能放大波動。美股方面多家券商下調 NVDA 至持有。
- ⑤產業循環位置：DRAM（HBM 帶動）仍處上行後段，NAND 消費級出現轉折跡象；整體記憶體循環可能處於「高峰附近、分化開始」階段。

**(b) 分析師目標價與評級綜合**
- NVDA：Bernstein（Stacy Rasgon）降至 Market Perform、目標價 $200；財報前至少 10 家降至持有；UBS（Tim Arcuri）認為市場假設「過於嚴苛」。
- MU：FinanceFeeds 情境區間多頭 $798／空頭 $656；美銀先前將 MU 自首選名單移除，高盛則維持強烈看多（TIKR 報導，時間未精確確認）。
- 記憶體整體：美銀對 NAND 轉趨保守（1Q27 合約價下跌）；TrendForce 仍看好 4Q26 DRAM 與企業級 SSD 價格。
- 本日未取得其他主要投行對 SNDK、DELL、MRVL 的最新目標價調整。

**(c) 情境推演（未來 6-12 個月）**
- 多頭（Bull）：Nvidia Rubin 放量順利、雲端 2027 capex 未如預期下修；HBM4 缺貨延續、NAND 現貨跌價僅屬短暫庫存調整；Fed 升息後見頂。→ MU、SNDK 收復 11 月跌幅，記憶體股重回高點區。
- 基準（Base）：AI 需求維持但 capex 成長放緩；DRAM／HBM 價格持平偏強、消費級 NAND 價格走跌；記憶體股區間震盪，個股分化（MU 優於 SNDK／Kioxia）。
- 空頭（Bear）：雲端業者大幅下修 2027 capex、NAND 與 DRAM 合約價雙雙轉跌、YMTC／CXMT 擴產加速、Fed 持續升息且 10 年債維持 5% 以上；記憶體週期提前反轉，股價再測今年中低位。

**(d) 關鍵前瞻催化劑時間軸**
- 近期（1-2 週）：FOMC 紀要、BIS 新規、Anthropic IPO、Dell 財報、NAND 現貨走勢。
- 1-2 個月：12 月 FOMC、MU FQ1 財報與 HBM4 指引、TrendForce 1Q27 合約價預估、Nvidia CEO 遴選。
- 中期：雲端業者 2027 capex 指引（1–2 月財報季）、YMTC IPO、Rubin Ultra 時程。

以上為綜合市場與分析師公開觀點及情境推演，非投資建議，個股估值偏高請自行評估風險。

## 7. 結論

今日最重要的變化是 Nvidia 交出遠優於預期的 Q3 財報與 $1,300 億 Q4 指引，暫時緩解了 AI 需求降溫與 CEO 風波的疑慮，帶動 MU、NVDA 盤後反彈約 4%。不過記憶體板塊出現新的分化訊號：NAND 現貨價兩週跌約 20%、美銀預估 1Q27 消費級 NAND 合約價轉跌，加上 YMTC 搶市佔，對 SNDK、Kioxia 壓力大於 MU。短線最值得關注的是 MU（能否站回 $750 以上）與 SNDK（NAND 報價與股票分割），以及亞洲記憶體股今日能否跟漲。需留意的風險包括 FOMC 偏鷹與 10 年債 5% 以上、BIS 出口管制新規、以及雲端 capex 下修敘事。

### 來源連結

- NVDA：[TradingKey – Nvidia Q3 財報解析（11/17）](https://www.tradingkey.com/analysis/stocks/us-stocks/262309793-nvidia-earnings-report-q3-rubin-ramp-data-center-growth-revenue-guidance-gross-margin-tradingkey)、[Investing.com – NVIDIA Q3 FY27 slides](https://www.investing.com/news/company-news/nvidia-q3-fy27-slides-revenue-doubles-to-1158b-on-ai-demand-93CH-5034317)、[Yahoo Finance – Nvidia earnings live](https://finance.yahoo.com/technology/live/nvidia-live-updates-interim-ceo-kress-prepares-for-q3-earnings-with-huang-reportedly-planning-comeback-153114076.html)、[CNBC – Kress 專訪（標題）](https://www.cnbc.com/2026/11/17/nvidia-nvda-earnings-report-q3-2027.html)、[NBC News – 董事會不讓黃仁勳復任（標題）](https://www.nbcnews.com/business/business-news/live-blog/nvidia-stock-earnings-report-jensen-huang-rcna609804)、[BigGo – 回購授權 $2,270 億](https://finance.biggo.com/news/99c52df5-57c4-40d6-927d-32bd8ddfcaca)
- 盤勢：[Motley Fool – Stock Market Today 11/17](https://www.fool.com/coverage/stock-market-today/2026/11/17/stock-market-today-nov-17-nvidia-slides-ahead-of-earnings-but-soars-in-after-hours-trading/)、[StockTitan – 11/17 盤勢直播](https://www.stocktitan.net/articles/stock-market-today-live-november-17-2026)、[Reuters via MarketScreener – Wall St slips ahead of Nvidia, Anthropic IPO](https://www.marketscreener.com/news/wall-st-slips-ahead-of-nvidia-results-anthropic-ipo-ce785edcda8df725)、[TokenPost – Micron leads chip stocks lower](https://www.tokenpost.com/news/investing/59598)、[24/7 Wall St. – 半導體 2008 年來最差兩個月](https://247wallst.com/investing/2026/11/17/chip-stocks-are-having-their-worst-two-months-since-2008/)
- MU：[Motley Fool – Why Micron keeps going down](https://www.fool.com/investing/2026/11/17/why-micron-stock-keeps-on-going-down/)、[Motley Fool – Buy Micron before Dec. 9?](https://www.fool.com/investing/2026/11/17/should-you-buy-micron-stock-before-dec-9/)、[Trefis – Micron under 10x earnings](https://www.trefis.com/stock/mu/articles/625641/should-you-buy-micron-stock-at-under-ten-times-earnings/2026-11-17)、[FinanceFeeds – MU bull/bear](https://financefeeds.com/micron-mu-stock-719-tuesday-nvidia-results-tonight-bull-798-bear-656/)、[FX Leaders – Micron tests support below $700](https://www.fxleaders.com/news/2026/11/17/micron-stock-tests-support-below-700-as-big-tech-attack-weighs-on-chip-companies/)、[TIKR – Goldman vs BofA on Micron](https://www.tikr.com/blog/goldman-calls-micron-a-screaming-buy-bank-of-america-just-dropped-it-from-its-top-picks-whos-right)、[StockAnalysis – MU 歷史價](https://stockanalysis.com/stocks/mu/history/)
- SNDK：[Motley Fool – Why SanDisk keeps going down](https://www.fool.com/investing/2026/11/17/why-sandisk-stock-keeps-on-going-down/)、[Yahoo Finance – SNDK sliding after AI leadership exit](https://finance.yahoo.com/markets/stocks/articles/why-sandisk-sndk-stock-sliding-020722050.html)、[TradingKey – SNDK 11/16 跌 8.58%](https://www.tradingkey.com/news/market-movers/262307697-market-movers-sndk-20261116)、[StockAnalysis – SNDK 歷史價](https://stockanalysis.com/stocks/sndk/history/)
- DELL：[24/7 Wall St. – Dell and HPE earnings](https://247wallst.com/investing/2026/11/09/dell-and-hpe-were-ai-winners-until-the-selloff-can-earnings-put-them-back-on-track/)
- ARM／MRVL：[24/7 Wall St. – Arm and Marvell sink 8%](https://247wallst.com/investing/2026/11/16/arm-and-marvell-sink-8-as-ai-chip-selloff-deepens-ahead-of-nvidia-earnings-applied-materials-drops-5/)、[Trefis – Why Marvell fell over 7%](https://www.trefis.com/stock/mrvl/articles/625792/why-did-marvell-stock-fall-over-7/2026-11-17)、[Motley Fool – Marvell and Intel down 50%](https://www.fool.com/investing/2026/11/17/marvell-and-intel-are-both-down-at-least-50-from-their-2026-highs-only-1-is-a-stock-id-buy/)
- TSM／ASX／出口管制：[GuruFocus via TradingView – TSMC falls on new US rule](https://www.tradingview.com/news/gurufocus:7a67d7b94094b:0-tsmc-stocks-fall-4-26-as-new-us-rule-tightens-checks-on-chip-foundries/)、[Yahoo Finance – Samsung falls 3.3% as US tightens foundry rules](https://finance.yahoo.com/markets/stocks/articles/samsung-stocks-fall-3-3-190603328.html)
- Samsung／SK Hynix／Kioxia：[Seoul Economic Daily – KOSPI −3.59%](https://en.sedaily.com/economy/2026/11/17/samsung-sk-hynix-tumble-together-as-kospi-sinks-359-percent)、[JKN – SK Hynix 跌破 110 萬韓元](https://news.jkn.co.kr/editions/english/post/1102246)、[TradingKey – 日韓股市與 Kioxia](https://www.tradingkey.com/analysis/stocks/more/262308438-japan-korea-stocks-skhy-kospi-nikkei-samsung-skhynix-softbank-kioxia-nvda-boj-tradingkey)、[TradingKey – SK Hynix 1.4 兆韓元計畫](https://www.tradingkey.com/analysis/stocks/us-stocks/262308580-sk-hynix-1-4t-won-supply-plan-us-ai-chip-rules-stock-falls-tradingkey)、[Trading Economics – KOSPI](https://tradingeconomics.com/south-korea/stock-market)、[Korea JoongAng Daily – 信用融資集中](https://www.koreajoongangdaily.com/business/samsung-sk-hynix-account-for-more-than-onefourth-of-koreas-stock-market-credit-loans/12973242)
- 記憶體報價／YMTC：[TrendForce – NAND 現貨兩週跌 20%（11/17）](https://www.trendforce.com/news/2026/11/17/news-nand-spot-prices-reverse-course-sliding-20-in-2-weeks-amid-weak-consumer-demand-ymtc-competition/)、[Crypto Briefing – TrendForce PC DRAM 4Q26 +13–18%](https://cryptobriefing.com/trendforce-pc-dram-prices-rise-4q26/)、[Capital Times – DRAM 合約價 Q4 +10–15%](https://capitaltimes.asia/tech/semiconductors/dram-contract-prices-rise-spot-market-stalls-trendforce/)、[Counterpoint – YMTC IPO 與 NAND 第三](https://counterpointresearch.com/en/insights/ymtc-files-for-landmark-ipo-after-climbing-to-no-3-in-global-nand-race-with-dram-next)、[Quartz – YMTC 上海 IPO 最快 2027 初](https://qz.com/ymtc-shanghai-ipo-flash-memory-2027-111126)
- 總經：[Admirals – Fed 12 月升息押注、殖利率 5%](https://admiralmarkets.com/analytics/traders-blog/fed-december-rate-hike-treasury-yields-retail-sales)、[Admirals – FOMC 紀要 11/18](https://admiralmarkets.com/analytics/traders-blog/fomc-minutes-november-2026)、[FXStreet – Chip stocks fell ahead of Nvidia results](https://fxstreet.com/analysis/chip-stocks-fell-again-ahead-of-nvidias-first-results-without-huang-202611171035)
