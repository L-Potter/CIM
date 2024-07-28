1. 畢業於長庚大學資訊工程學系
2. 多益成績為670分
3. 大學專題: 負責後端，使用elasticSearch 作為搜尋引擎 並且使用flask 作為elasticsearch跟前端的 API。 資料來源使用selenium自動化操作瀏覽器爬蟲．

程式語言: Python(主要使用) Golang C++ C Java
開發環境: git, Ubuntu, Docker, K8S


工作經驗:
長庚大學人工智慧研究中心技士: 2020/8 - 2021/11
1. 負責管理與維護台達電機房系統，與廠商完成簡訊與Mail通知系統告知所有管理人員
2. 請購: GPU Server & 儲存系統 & 費米智慧家庭系統 & 教授個人專案(Lidar, Xilinx)等
4. 技術支援: 中心防火牆與Vlan設置，K8S, OpenStack障礙排除，資料庫架設，獨立完成X11 Forward讓同仁使用container時能在遠端情況下使用圖型化介面，具有即時性了解AI訓練情形．

替代役: 2021/11-2022/4
調查局(安檢, 戒護, 行政文書處理)

國網中心: 2022/5 - 2023/5
專案人員
1. 參與平台維運跟開發(配合工程師使用PHP, JavaScript開發)
   改善項目原先資料處理使用PHP(改為PYTHON: POPEN+ASYNCIO+TABULA最大化使用伺服器CPU效能，資料更新速度有明顯提升)
   架設PHPMYSQL, MYSQL, APACHE2(PHP-FPM, Rewrite, SSL)
   優化下載檔案效能基於unbuffer sql request減少DB壓力來實現百萬筆資料下載無中斷
   MYSQL效能調整有io bound, cpu boubd, 使用explain & show processlist state查詢異常原因，因sql語法問題導致innodb使用filesort佔用儲存空間並讓apache2 socket無法建立導致網站停擺，短期解法為: 使用apparmor掛載mysql的tmp_dir到新的SSD空間，長期解法為upgrade to mysql 8建立index 來符合sql語法需求

3. POC案
   台灣衫2,3號應用iserver替代方案
   負責Web端: 使用Django's AUTHENTICATION_BACKENDS, REST_FRAMEWORK,SWAGGER導入與實現HTTP API介面用於後續開發與檢測

TSMC: 2023/5 - now
部門機台保養與T/S與修機，Parts上下機與盤點
申請單開立: 施工單, 電腦掃毒 等
報表整理: SPC, Uchart, KER...
值班: Area Team member, P3 BackUp Leader, 8月接ACC戰情

軟體部分: 
部門使用Java GUI預設程式權限有限制，使用Win batch Script自動化開啟在複製貼上權限跟檔案存擋，加速值班人員處理速度
在Siview & 報表在使用上帳密會有輸入錯誤上限, 密碼字串很長等，為了加速人員處理速度，使用python基於WIN32API SetFocus原理在不同的PID視窗做切換，Terminal作為簡易密碼輸入才切換原先視窗輸入帳密，替代原本無密碼確認的應用程式．
接戰情後: 預計使用pywinauto來monitor異常數值並用PIL截圖到teams戰情群組上
