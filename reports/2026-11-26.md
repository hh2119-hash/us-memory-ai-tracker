# 美股記憶體 / AI 硬體 / Mag 7 追蹤報告
日期：2026-11-26
執行時間：台灣時間 08:00（實際 08:03 開始）

今日主要參考來源：Yahoo Finance（收盤價）、StockAnalysis（收盤價交叉驗證）、Bloomberg（標題/摘要）、Seoul Economic Daily、Digital Today、FN News、Investing.com、Longbridge、Motley Fool、Parameter、JournalArta、SEC EDGAR（NVIDIA 8-K）、Marvell IR、Tom's Hardware、TechRadar、Stocktwits 等。Reuters / WSJ / MarketWatch 專門網域搜尋今日遭搜尋代理拒絕，ForexFactory / FinancialJuice 本日查無可引用之即時頁面，故未列入。
收盤價核對：MU $601.25（−4.53%）、SNDK $73.61（−5.57%）— Yahoo 與 StockAnalysis 一致（11/25 收盤）；儀表板 prices.json 原落後（排程於收盤前 20:54 UTC 執行，MU 停在 11/24、SNDK 停在 11/19 $94.39），已手動 Run workflow 重跑（#384），重跑後 MU $601.25、SNDK $73.61 皆已同步至 11/25。

> 提醒：今天（11/26，週四）美國感恩節休市；11/27（週五）美股提早於美東 13:00 收盤。本報告股價以 11/25（週三）收盤為準。

## 1. 今日重點摘要

- **記憶體股遭「週期見頂」論調重擊**：BNP Paribas（Karl Ackerman）11/24 將 Micron 由 Outperform 降至 Neutral，目標價由 $1,700 腰斬至 $775，認為 DRAM/NAND 供需將於 2027 年中就恢復平衡（比原估早一年），並預估 MU 2028 年淨利比市場共識低 45%。MU 11/24 收 $629.79（−11.01%），11/25 再跌至 $601.25（−4.53%）。
- **NAND 報價轉弱是 SNDK 的核心利空**：TrendForce 下修 4Q26 NAND 合約價漲幅至 +8~13%（原 +15~20%），並預估 1Q27 NAND 合約價持平至 −5%、2Q27 起全面進入下行；BofA 指 512Gb NAND wafer 現貨週跌 12%、季跌 32%。SNDK 11/24 −11.13%、11/25 −5.57% 收 $73.61，距 6/25 高點 $291.88 已跌約 75%。
- **DRAM 與 NAND 分化**：DRAM 合約價仍在漲（TrendForce：4Q26 PC DRAM +13~18%、一般型 DRAM +10~15%），HBM 吃掉大量晶圓產能，TrendForce 認為 2027 年 DRAM 跌價不易出現——這是 MU 相對 SNDK 抗跌的關鍵。
- **輝達戲劇性一週**：11/23 輝達董事會一致決議讓 Jensen Huang 復任 CEO（SEC 8-K），NVDA 當天大漲約 31%；但 11/24（−5.86%）、11/25（−3.91%，收 $149.30）連兩天回吐。
- **Dell 財報亮眼但股價被 HPE 拖累**：Dell 3Q FY27 營收 $549 億（+103%），AI 伺服器營收 $220 億，AI backlog 達 $1,323 億，全年營收指引上調 $100 億至 $2,020 億；但 HPE 同日因 AI 伺服器利潤率指引偏弱重挫約 16%，DELL 11/24 盤中收跌 11.83%，11/25 小漲 0.60% 收 $297.06。
- **總經壓力**：10 月 PCE 年增 3.8%（符合預期但約為 Fed 目標兩倍），升息機率上升，加上新關稅提案與 AI 支出疑慮；11/25 Nasdaq 盤中一度重挫逾 4%，收盤收斂至 −0.62%（23,585.80），費半 −0.65%（8,774.86）。
- **韓股記憶體雙雄暴跌**：11/25 KOSPI −6.16% 至 4,697.51；Samsung −9.87%（₩170,700）、SK Hynix −11.05%（₩1,030,000），外資賣超約 1.9 兆韓元。
- **中國競爭變數未解**：YMTC 依 Counterpoint 2Q26 已以 14% 出貨市佔擠進 NAND 前三；中國雲端業者據報削減 2027 年企業級 SSD 訂單，NAND 供給增加（2027 bit supply +25~30%）是 SNDK、Kioxia、MU NAND 業務的中期壓力。

## 2. 個股最新消息

### SNDK / SanDisk
- 最新消息：TrendForce 下修 NAND 合約價預估、BNP 看空記憶體週期，SNDK 連兩日大跌；Evercore ISI 11/24 將目標價由 $200 降至 $175（維持 Outperform）。
- 股價或盤前盤後變化：11/25 收盤 $73.61（−5.57%）；11/24 收 $77.95（−11.13%）；11/23 收 $87.71（+10.69%）。五個交易日約跌 25%、一個月跌逾 58%。
- 重要新聞摘要：TrendForce 預估 1Q27 NAND 合約價 0~−5%、2Q27 起全面下行；BofA 預估 1Q27 通用型 NAND 合約價再跌 5~10%；中國雲端業者縮減 2027 年企業級 SSD 訂單。另 Form 144 文件顯示可能有內部人賣股。
- 解讀：SNDK 是純 NAND 標的，對報價轉折最敏感。市場已從「AI 推升 eSSD 需求」轉為交易「2027 NAND 供給過剩」，估值重設速度極快。
- 對股價可能影響：短線偏空，$72~73 附近為 20 日支撐測試區；若跌破，技術面下一個參考價位距離較遠。若 12 月 NAND 合約報價跌幅小於預期，可能出現技術性反彈。
- 觀察重點：12 月 TrendForce 1Q27 合約價更新、企業級 SSD 訂單、YMTC 擴產與報價策略、內部人申報。

### MU / Micron
- 最新消息：BNP Paribas 降評至 Neutral、目標價 $1,700→$775；UBS 亦下修目標價（依 Benzinga 標題）。
- 股價或盤前盤後變化：11/25 收盤 $601.25（−4.53%，盤中低點 $548.13）；11/24 收 $629.79（−11.01%）；11/23 收 $707.70（+19.04%）。距 6 月高點約跌 42%。
- 重要新聞摘要：Ackerman 理由四點——①2028 年超大規模業者 capex 風險；②Nvidia Vera Rubin Ultra 的 HBM 用量低於預期；③2026~27 年 PC/手機出貨下滑；④新晶圓產能投入。預估 MU 2029 年 EPS 谷底 $86。反方：Goldman Sachs、BofA 仍認為景氣至少延續到明年；Micron 管理層稱 2027 年 75% 供給已售出；TrendForce 認為 DRAM 緊俏延續到 2027 年。
- 解讀：市場現在交易的是「2028 年獲利懸崖」而非當下基本面——近期 DRAM 合約價仍漲、HBM 價格明年大幅上調，基本面短期依然強勁。股價波動反映的是週期頂部時間點的爭議。
- 對股價可能影響：短線高波動、偏弱整理；12/17 財報（FQ1）是關鍵，若指引與 2027 HBM 合約價確認強勁，有機會修復估值。
- 觀察重點：12/1 UBS 科技會議、12/17 FQ1 財報、HBM4 定價與 Rubin 配置、DRAM 合約價。

### DELL / Dell
- 最新消息：11/24 盤後公布 3Q FY27 財報，全面超預期。
- 股價或盤前盤後變化：11/25 收盤 $297.06（+0.60%）；11/24 收 $295.28（−11.83%，因 HPE 拖累），盤後一度 +4% 至 $307.19。
- 重要新聞摘要：營收 $549 億（+103% YoY），非 GAAP EPS $9.45（預期 $6.56）；AI 伺服器營收 $220 億（+291%），AI 訂單 $602 億，AI backlog $1,323 億；FY27 營收指引上調至 $2,020 億，FQ4 AI 伺服器營收約 $235 億；庫藏股授權增加 $250 億。隱憂：ISG 營業利益率預估由 17.0% 回落，AI 伺服器僅中個位數利潤率；存貨自年初增加 182% 至 $294 億。
- 解讀：「量」確認 AI 伺服器需求仍在擴張（對記憶體需求是利多），但「價」亮黃燈——記憶體成本上升壓縮 OEM 毛利，部分 AI 伺服器訂單據報漲價 25~45%。
- 對股價可能影響：財報利多被類股殺盤抵銷，短線震盪；中期取決於毛利率能否守住。
- 觀察重點：FQ4 利潤率、存貨去化、HPE/SMCI 同業動態、分析師目標價調整（Citi $600→$550、MS $511→$403）。

### ARM / Arm
- 最新消息：今日暫無重大個別公司更新；股價隨 AI 晶片類股波動。
- 股價或盤前盤後變化：11/25 收盤 $161.51（−0.03%）；11/24 收 $161.56；11/23 收 $176.67。11/25 盤中一度跌約 8%，收盤幾近平盤。
- 重要新聞摘要：11 月初財報後展望僅略優於預期，月內多次大跌（11/5、11/16）。
- 解讀：高估值 IP 授權股對 AI 情緒高度敏感，盤中大幅回收代表逢低買盤仍在。
- 對股價可能影響：跟隨 NVDA 與大盤風險偏好。
- 觀察重點：資料中心 CPU（Neoverse）授權進度、與 Nvidia 合作、軟銀相關消息。

### MRVL / Marvell
- 最新消息：將於 12/1（週二）美西時間 13:30 召開 3Q FY27 財報電話會議。
- 股價或盤前盤後變化：11/25 收盤 $130.93（−0.49%）；11/24 收 $131.57；11/23 收 $144.74。
- 重要新聞摘要：今日暫無重大更新。
- 解讀：財報前觀望；市場關注客製化 ASIC（AWS Trainium 等）與光通訊（800G/1.6T DSP）成長是否延續。
- 對股價可能影響：財報前後波動加大。
- 觀察重點：12/1 財報、資料中心營收、ASIC 客戶進度。

### NVDA / NVIDIA
- 最新消息：11/23 董事會一致決議 Jensen Huang 復任總裁、CEO 及董事，代理 CEO Colette Kress 回任 CFO；董事會成立「國家安全與出口管制委員會」，獨立董事對相關報導的調查持續。
- 股價或盤前盤後變化：11/25 收盤 $149.30（−3.91%，成交約 3.57 億股）；11/24 收 $155.38（−5.86%）；11/23 收 $165.05（約 +31%）；11/20 收 $125.53。
- 重要新聞摘要：11/25 盤中一度跌近 9%；市場擔憂治理問題、循環融資、中國營收曝險，CDS 利差接近歷史高位；但上季自由現金流逾 $400 億。
- 解讀：CEO 復任消除最大不確定性，但後續調查與出口管制風險仍在，股價從「事件交易」回歸 AI 需求與總經。
- 對股價可能影響：高波動；若調查無新利空，治理折價可望逐步收斂。
- 觀察重點：獨立調查結果、中國出口規則、GB300/Rubin 出貨節奏、HBM 用量。

### TSM / TSMC
- 最新消息：ADR 隨 AI 晶片股回落。
- 股價或盤前盤後變化：11/25 收盤 $342.34（−1.96%）；11/24 收 $349.20（−3.96%）；11/23 收 $363.60（+14%）。距 10/5 高點 $485.80 約跌 3 成。
- 重要新聞摘要：10 月營收 NT$5,868.9 億（+59.7% YoY）；11 月營收將於 12 月初公布；美國對中國高階晶片出口新規及 capex 規劃為壓力來源。
- 解讀：基本面（營收）強勁，股價受 AI 類股情緒與出口管制拖累。
- 對股價可能影響：短線跟隨費半；12 月初月營收可能是支撐。
- 觀察重點：11 月營收、CoWoS 擴產、先進製程報價、出口管制細節。

### ASX / ASE Technology
- 最新消息：今日暫無重大更新。
- 股價或盤前盤後變化：11/25 收盤 $29.49（+0.55%）；11/24 收 $29.33。
- 重要新聞摘要：今日暫無重大更新。
- 解讀：在類股殺盤中相對抗跌，封測/先進封裝（CoWoS 外包）題材提供支撐。
- 對股價可能影響：中性。
- 觀察重點：11 月營收、先進封裝產能與 Nvidia/TSMC 外包訂單。

### Kioxia
- 最新消息：11/2 財報展望顯示需求趨於平穩，股價大跌；11/20 單日跌 11.66%；ORIX 預告 Q3 將認列約 1,900 億日圓 Kioxia 評價損失。
- 股價或盤前盤後變化：11/25 收盤 ¥6,895（儀表板資料）；11/26 東京盤進行中，收盤待確認。
- 重要新聞摘要：Kioxia HD 將自子公司取得 2.2 兆日圓股利（Investing.com 標題）；NAND 報價轉弱為主要壓力。
- 解讀：與 SNDK 同為 NAND 純標的，TrendForce 下修報價與 YMTC 市佔擴張是雙重壓力。
- 對股價可能影響：短線偏空、跟隨 SNDK。
- 觀察重點：NAND 合約價、BiCS 新世代量產、YMTC 競爭。

### Samsung Electronics
- 最新消息：11/25 股價重挫，市值跌破 1,000 兆韓元。
- 股價或盤前盤後變化：11/25 收盤 ₩170,700（−9.87%）；11/24 收 ₩189,400。11/26 首爾盤進行中。
- 重要新聞摘要：BNP 2028 記憶體過剩論、美股科技股下跌、外資大賣。韓國券商（KB）仍主張「W 型第二個底部」，建議持有至 1 月。
- 解讀：Samsung 有 HBM4 追趕題材，但 NAND 曝險與 P5 新產能（2028~30）也是 BNP 擔憂的供給來源。
- 對股價可能影響：短線偏弱、波動大。
- 觀察重點：HBM4 認證、P5 進度、外資動向。

### SK Hynix
- 最新消息：11/25 股價重挫逾 11%。
- 股價或盤前盤後變化：11/25 收盤 ₩1,030,000（−11.05%）；11/24 收 ₩1,158,000。11/26 首爾盤進行中。
- 重要新聞摘要：SK hynix 管理層仍認為短缺延續至 2030 年；HBM 價格明年據報最高漲 2.7 倍（Seoul Economic Daily 11/19）。
- 解讀：HBM 龍頭基本面最強，但作為記憶體權值股被 ETF/外資賣壓波及。
- 對股價可能影響：短線跟隨 MU；HBM4 合約確認是反轉關鍵。
- 觀察重點：HBM4 定價、Yongin 新廠時程、Nvidia Rubin 配置。

## 2-A. Mag 7 科技巨頭追蹤（AAPL／MSFT／GOOGL／AMZN／META／NVDA／TSLA）

| 公司代號 | 近期動態 | 股價（11/25 收盤，參考值） | 解讀 |
|---|---|---|---|
| AAPL | 七雄中唯一接近歷史高點（247wallst 11/18）；記憶體成本上升為硬體毛利隱憂 | $355.58（+0.43%） | 防禦性資金避風港；記憶體漲價影響 iPhone/Mac 毛利 |
| MSFT | AI capex 持續擴張，市場質疑投報 | $489.93（−1.25%） | Azure AI 需求是 HBM/伺服器最上游需求之一 |
| GOOGL | AI 支出疑慮下回落 | $273.10（−2.13%） | TPU 自研晶片帶動 ASIC（MRVL/AVGO）與 HBM 需求 |
| AMZN | 跌幅居七雄之首 | $244.43（−3.12%） | AWS capex 與 Trainium 進度連動 MRVL |
| META | 逆勢大漲 | $609.89（+3.40%） | 資金回補；其 2027 capex 指引對 AI 伺服器需求敏感 |
| NVDA | CEO 復任後連兩日回吐 | $149.30（−3.91%） | AI 加速器需求核心，HBM 用量直接影響 MU/SK Hynix |
| TSLA | 跟隨大盤小跌 | $380.14（−1.18%） | 與記憶體連動較低（Dojo/車用 DRAM） |

**Mag 7 共同觀察**：本週七雄走勢分歧（META、AAPL 收紅，AMZN、GOOGL、NVDA 走弱），反映市場對「AI 資本支出能否持續轉化為獲利」的分歧加深。Morgan Stanley 預估大型雲端 capex 2027 年約 $1.6 兆、2028 年約 $1.8 兆，若此預期不變，記憶體與 AI 伺服器需求的「量」仍有支撐；BNP 擔憂的是 2028 年 capex 成長放緩。註：價格為參考值，個股當日收盤總覽以儀表板網頁為準。

## 3. 產業共同趨勢

- **DRAM**：合約價仍上漲但漲幅收斂——TrendForce 4Q26 PC DRAM +13~18%、一般型 DRAM +10~15%；BofA 預估 4Q26 +8%、1Q27 +5%。DDR4 現貨小跌 1.43%（$44.25）。Counterpoint：3Q26 DRAM 營收年增 369%，市佔 Samsung 38%、SK hynix 29%、Micron 21%、CXMT 9%。
- **NAND Flash**：現貨價近幾週跌約 20%；TrendForce 1Q27 合約價 0~−5%、2Q27 全面下行；2027 NAND bit 供給 +25~30%，產業 capex +26.7% 至 $299 億。
- **YMTC / CXMT（中國競爭變數）**：YMTC 2Q26 出貨市佔 14%（Counterpoint），首度擠進前三並小幅超越 Kioxia；Digitimes（11/6）報導 YMTC 新廠目標使用最高 70% 國產設備；CXMT 已占 DRAM 市佔 9%。中國雲端業者縮減 2027 年企業級 SSD 訂單，等於把需求轉向國產供應，對 SNDK、Kioxia 的報價與市佔壓力最大，MU 的 NAND 業務次之。美國出口管制（11/17 新規）是雙面刃：限制 YMTC 先進設備取得，但也加速國產化。
- **HBM**：TrendForce 預估 HBM 占 DRAM 晶圓投片比重由 2026 年底 22% 升至 2027 年底 30%；HBM 單位晶圓用量是一般 DRAM 的 3~4 倍，擠壓一般型 DRAM 供給。爭議點在 Vera Rubin Ultra 的 HBM 用量（BNP 認為低於預期）。
- **AI Server**：Dell AI backlog $1,323 億、HPE 亦有大量積壓訂單，需求面仍強；但 OEM 利潤率受記憶體成本侵蝕。
- **PC / Server demand**：BNP 預估 2026~27 年 PC 與手機出貨下滑（記憶體漲價抑制終端需求）。
- **Data center capex**：大型雲端 2027 年 capex 預估約 $1.6 兆（MS）；市場擔憂 2028 年成長放緩。BNP 預估記憶體占 AI 資料中心支出比重明年見頂 40%，2030 年降至 27%。
- **供應鏈**：功率半導體據報因 AI 需求排擠進入配貨；中國鎵出口暫停措施 11/27 到期，值得留意後續。
- **AI accelerator**：NVDA 治理風險暫解；MRVL 客製化 ASIC/光通訊 12/1 財報；TSM CoWoS 產能仍是瓶頸；ASX 先進封裝受惠外包。

## 4. 新聞重要性分級

- **高重要性**：BNP 降評 MU 並提出 2027 年中供需平衡論；TrendForce 下修 NAND 合約價（1Q27 轉跌）；Nvidia CEO 復任（8-K）；Dell 財報 AI backlog $1,323 億與利潤率警訊；10 月 PCE 3.8% 推升升息疑慮；韓股記憶體雙雄單日暴跌約 10%。
- **中重要性**：Evercore 下調 SNDK 目標價；HPE 利潤率指引偏弱；中國雲端縮減 2027 eSSD 訂單；YMTC 市佔與國產設備擴廠；HBM 明年漲價報導。
- **低重要性**：ARM、MRVL、ASX 無個別新聞，僅隨類股波動；Kioxia 子公司股利為內部資金調度。

## 5. 需要持續追蹤的訊號（未來 1-2 週）

- 11/27（週五）：美股半天交易；中國鎵出口暫停措施到期。
- 12/1（週二）：Marvell 3Q FY27 財報（美西 13:30 電話會議）；Micron 出席 UBS 科技會議。
- 12 月初：TSMC 11 月營收；TrendForce 12 月/1Q27 記憶體合約價更新。
- 12/17：Micron FQ1 FY27 財報（最關鍵催化劑）。
- 12 月 FOMC：PCE 偏高後的升息機率。
- 其他：分析師對 MU/SNDK 是否跟進降評、HBM4 合約定價、NAND/SSD 現貨價、Nvidia 獨立調查進度與出口管制、大廠 2027 capex 指引、YMTC/CXMT 擴產與 IPO 動態。

## 6. 前瞻觀點與分析師綜合看法

### (a) 多面向分析法綜合
1. **基本面**：短期仍強——DRAM 合約價續漲、HBM 售罄、Dell AI 營收翻倍、Micron 2027 年 75% 供給已售出。分歧在 2027 下半年至 2028：NAND 已先轉弱，DRAM 是否跟進是核心爭議。
2. **估值面**：記憶體股在週期高峰時通常本益比看起來「很便宜」，市場會用遠期（2028）獲利定價；BNP 2028 年淨利低於共識 45% 的預估，等於說明目前低本益比可能是「價值陷阱」。反之若 2028 獲利不崩，MU 現價對應的估值偏低。
3. **技術面與股價位階**：MU 距高點約 −42%、SNDK 約 −75%、TSM 約 −30%，皆跌破 50 日均線，屬空頭格局；但 11/23 單日 +19%（MU）、+31%（NVDA）顯示空單擁擠、反彈力道驚人。
4. **籌碼/資金面**：韓股外資單日賣超 1.9 兆韓元；Nomura 指出利率上升、信用利差擴大使資金轉向現金與公債；散戶在 Stocktwits 仍偏多。去槓桿階段波動放大。
5. **產業循環位置**：NAND 疑似已越過週期高點（報價先轉弱），DRAM 處於「價格仍漲但漲幅收斂」的高原期，HBM 仍在成長段。這種結構使 MU（DRAM/HBM 為主）相對 SNDK、Kioxia（純 NAND）有防禦性。

### (b) 分析師目標價與評級綜合
- **Micron**：BNP Paribas 降至 Neutral，目標價 $1,700→$775（11/24）；UBS 下修目標價（Benzinga 標題）；Goldman Sachs、BofA 仍偏多，認為景氣至少延續至 2027 年。
- **SanDisk**：Evercore ISI Outperform，目標價 $200→$175（11/24）；Rosenblatt Buy、$300（10/30）；Fox Advisors 11/2 降至 Equal-Weight；平均目標價約 $260（遠高於現價，顯示目標價尚未完全下修）。
- **Dell**：共識 Moderate Buy（14 買 7 持有），平均目標價約 $589；Citi Buy $600→$550；Morgan Stanley Hold $511→$403；Barclays Equal Weight。

### (c) 情境推演（未來 6-12 個月）
- **多頭（Bull）**：12/17 Micron 財報與指引強勁、HBM4 合約價大漲確認、大型雲端 2027 capex 上修；NAND 報價跌幅小於 5%。→ 記憶體股從超跌區大幅反彈，MU 可能回測前波區間。
- **基準（Base）**：DRAM/HBM 維持緊俏至 2027 年中，NAND 溫和下跌；Fed 暫不升息。→ MU 區間震盪、SNDK/Kioxia 低檔整理，類股分化。
- **空頭（Bear）**：PCE 持續偏高導致升息、AI capex 下修、中國供給（YMTC/CXMT）擴張加速、NAND 跌價擴大至 DRAM。→ 記憶體股進一步下探，SNDK 與 Kioxia 受創最深。

### (d) 關鍵前瞻催化劑時間軸
- **近期（1-2 週）**：MRVL 財報（12/1）、UBS 科技會議（12/1）、TSMC 11 月營收、TrendForce 報價更新。
- **1-2 個月**：Micron FQ1 財報（12/17）、12 月 FOMC、CES（1 月）、Samsung/SK hynix 4Q 財報（1 月底）、大型雲端 4Q 財報與 2027 capex 指引（1 月底~2 月）。
- **中期**：Nvidia Rubin 量產與 HBM4 配置、Samsung P5 / SK hynix Yongin 新產能時程、YMTC/CXMT 擴產與美國出口管制演變。

以上為綜合市場與分析師公開觀點及情境推演，非投資建議，個股估值偏高請自行評估風險。

## 7. 結論

本期最重要的變化是記憶體股從「AI 超級週期」轉為交易「週期見頂」：BNP 將 MU 目標價腰斬、TrendForce 確認 NAND 合約價 1Q27 轉跌，使 MU 兩日跌約 15%、SNDK 兩日跌約 16%（11/25 收盤 MU $601.25、SNDK $73.61）。短線最值得關注的是 MU（12/17 財報能否反駁 2028 年獲利懸崖論）與 MRVL（12/1 財報），NVDA 則在 CEO 復任後回歸基本面交易。需留意的風險包括 PCE 偏高引發升息、NAND 跌價擴散至 DRAM、中國 YMTC/CXMT 供給擴張，以及感恩節假期前後流動性偏低造成的劇烈波動。

### 來源連結
- 收盤價：[Yahoo Finance – MU](https://finance.yahoo.com/quote/MU/)、[StockAnalysis – MU 歷史價格](https://stockanalysis.com/stocks/mu/history/)、[StockAnalysis – SNDK 歷史價格](https://stockanalysis.com/stocks/sndk/history/)
- MU：[Seoul Economic Daily – BNP Sees DRAM, NAND Prices Falling From Mid-2027（11/25）](https://en.sedaily.com/world/2026/11/25/bnp-sees-dram-nand-prices-falling-from-mid-2027)、[Benzinga – UBS 降目標價、BNP 降評](https://www.benzinga.com/trading-ideas/movers/26/11/63626746/micron-stock-falls-as-ubs-cuts-price-target-bnp-paribas-downgrade-weighs)、[Schaeffer's – Micron Stock Plunges After Downgrade（11/25）](https://www.schaeffersresearch.com/content/news/2026/11/25/micron-stock-plunges-after-downgrade-steep-pt-cut)、[FX Leaders – TrendForce Says DRAM Stays Tight Through 2027（11/25）](https://www.fxleaders.com/news/2026/11/25/micron-stock-falls-ai-selloff-analyst-downgrades-mu/)、[Stocktwits – Micron downgrade, retail stays bullish](https://stocktwits.com/news-articles/markets/equity/mu-stock-falls-on-downgrade-retail-stays-bullish/c7zxAgKRP6)
- SNDK：[Parameter – SNDK Falls 8% After TrendForce Trims NAND Outlook（11/25）](https://parameter.io/sandisk-sndk-stock-falls-8-after-trendforce-trims-nand-price-outlook/)、[JournalArta – Sandisk Stock Slides（11/26）](https://journalarta.com/en/2026/11/26/sandisk-stock-slides-as-memory-supply-fears-hit-ai-trade/)、[Seeking Alpha – Sandisk: The Numbers Are Still Ridiculous](https://seekingalpha.com/article/4971114-sandisk-the-numbers-are-still-ridiculous)
- DELL：[Investing.com – Dell Q3 FY27 slides（11/24）](https://www.investing.com/news/company-news/dell-q3-fy27-slides-revenue-doubles-ai-backlog-hits-132b-93CH-5049313)、[Longbridge – Dell Q3 volume vs price（11/25）](https://longbridge.com/en/news/306698607)、[TechRepublic – Dell AI Server Revenue Hits $22B](https://www.techrepublic.com/article/news-dell-ai-server-revenue-q3-fy27-backlog/)
- NVDA：[SEC 8-K – NVIDIA Board Reinstates Jensen Huang（11/23）](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000090/nov23pressrelease.htm)、[Motley Fool – Stock Market Today Nov 25](https://www.fool.com/coverage/stock-market-today/2026/11/25/stock-market-today-nov-25-nvidia-slides-3-9-as-the-market-considers-hot-pce-inflation-data-and-new-tariff-proposals/)、[Yahoo Finance – Chip stocks tumble as Nvidia-led AI rally unravels（11/25）](https://finance.yahoo.com/technology/ai/articles/chip-stocks-tumble-nvidia-led-164900978.html)
- TSM：[JournalArta – TSMC Shares Slide（11/25）](https://journalarta.com/en/2026/11/25/tsmc-shares-slide-as-ai-chip-rally-stalls/)
- MRVL：[Marvell IR – 3Q FY27 財報電話會議公告](https://investor.marvell.com/news-events/press-releases/detail/1041/marvell-technology-inc-announces-conference-call-to-review-third-quarter-of-fiscal-year-2027-financial-results)
- ARM：[Motley Fool – Why Arm Holdings Plunged（11/16）](https://fool.com/investing/2026/11/16/why-arm-holdings-plunged-today)
- Samsung / SK Hynix：[FN News – KOSPI Falls Below 4,700（11/26）](https://en.fnnews.com/news/202611252233183012)、[Invezz – Samsung, SK Hynix tumble 10%（11/25）](https://invezz.com/ie/news/2026/11/25/samsung-sk-hynix-stocks-tumble-10percent-why-smart-money-is-heading-for-exits/)、[Seoul Economic Daily – HBM Prices to Jump Up to 2.7-Fold（11/19）](https://en.sedaily.com/business/2026/11/19/latest-hbm-prices-to-jump-up-to-27-fold-next-year)、[Seoul Economic Daily – Hold On Until January（11/23）](https://en.sedaily.com/market/2026/11/23/samsung-sk-hynix-investors-told-to-hold-on-until-january)
- Kioxia：[Bloomberg – Kioxia Shares Sink After Outlook（11/2）](https://www.bloomberg.com/news/articles/2026-11-02/kioxia-shares-tumble-after-outlook-suggests-demand-leveling-off)、[Global Banking & Finance – Kioxia falls 11.66%（11/20）](https://www.globalbankingandfinance.com/kioxia-holdings-285a-t-falls-2026-11-20/)、[Investing.com – Kioxia HD ¥2.2trn dividend](https://www.investing.com/news/company-news/kioxia-hd-to-receive-22trn-dividend-from-subsidiary-93CH-5050173)、[BigGo – ORIX Kioxia valuation loss](https://finance.biggo.com/news/JP_8591.T_2026-11-09)
- 記憶體報價：[Digital Today – NAND spot prices plunge 20%（11/25）](https://www.digitaltoday.co.kr/en/view/130658/nand-spot-prices-plunge-20-percent-dram-holds-up-memory-market-polarisation-seen-in-2027)、[Shattered – DRAM Prices PC Contract 13-18%（11/25）](https://shattered.io/dram-prices-pc-contract-13-18-percent-power-semiconductors-allocation-nov-25/)、[TechRadar – NAND prices could finally fall](https://www.techradar.com/pro/nand-prices-could-finally-be-set-to-fall-in-the-first-bit-of-good-news-for-component-fans-for-some-time-but-dram-is-refusing-to-budge-so-far&gsessionid=dEM-ikZDSO8cgQcaBVZGHwQQYkxLh2-GCB1ggc4qlYYNjEIhR7mMDg)
- YMTC / CXMT：[Tom's Hardware – YMTC breaks into top three NAND makers](https://www.tomshardware.com/tech-industry/ymtc-breaks-into-the-top-three-nand-makers-for-the-first-time)、[Digitimes – YMTC targets up to 70% Chinese tools（11/6）](https://www.digitimes.com/news/a20261106VL217/ymtc-nand-equipment-manufacturing.html)、[TipRanks – YMTC expands NAND production](https://www.tipranks.com/news/chinas-ymtc-expands-nand-production-should-micron-sandisk-and-sk-hynix-investors-worry)
- 總經/產業：[Bloomberg – Chip Stocks Slide as US Sets New Curbs on China's Compute Access（11/17）](https://www.bloomberg.com/news/articles/2026-11-17/chip-stocks-slide-as-us-sets-new-curbs-on-china-s-compute-access)、[Bloomberg – Investors Flee Chipmakers（11/6）](https://www.bloomberg.com/news/newsletters/2026-11-06/investors-flee-chipmakers-fearing-end-of-ai-boom)、[247wallst – Apple Is the Only Mag 7 Stock Near a Record（11/18）](https://247wallst.com/investing/2026/11/18/apple-is-the-only-magnificent-seven-stock-near-a-record/)
