1. 畢業於長庚大學資訊工程學系
2. 多益成績為670分
3. 大學專題: 使用elasticSearch 作為搜尋引擎 並且使用flask 作為elasticsearch跟前端的 API。 資料來源使用selenium模擬使用者網站行為 有使用python & golang 兩種語言去實作

程式語言: Python(主要使用) Golang C++ C Java
開發環境: git, Ubuntu, Docker, K8S


工作經驗:
長庚大學人工智慧研究中心技士: 2020/8 - 2021/11
1. 負責管理與維護台達電機房系統，與廠商完成簡訊與Mail通知系統告知所有管理人員
2. 請購: GPU Server & 儲存系統 & 費米智慧家庭系統 & 教授個人專案(Lidar, Xilinx)等
4. 技術支援: 中心防火牆與Vlan設置，K8S, OpenStack障礙排除，資料庫架設，獨立完成X11 Forward讓同仁能在遠端情況下使用圖型化介面，具有即時性了解AI訓練情形

替代役: 2021/11-2022/4
調查局(安檢, 戒護, 行政文書處理)

國網中心: 2022/5 - 2023/5
專案人員
1. 參與平台維運跟開發(使用PHP, JavaScript開發)
   改善項目原先資料處理使用PHP(改為PYTHON: POPEN+ASYNCIO+TABULA最大化使用伺服器CPU效能，資料更新速度有明顯提升
   架設PHPMYSQL, MYSQL, APACHE2(PHP-FPM, Rewrite, SSL)
   優化下載檔案效能基於unbuffer sql request減少DB壓力來實現百萬筆資料下載無中斷

2. POC案
   主要技術: HPC實作聯邦式學習
   負責Web端: AUTHENTICATION_BACKENDS, REST_FRAMEWORK,SWAGGER導入與實現HTTP API介面用於後續開發與檢測

TSMC: 2023/5 - now
部門機台保養與T/S與修機，Parts上下機與盤點
申請單開立: 施工單, 電腦掃毒
報表整理: SPC, Uchart, KER...
值班: Area Team member, P3 Leader, 8月接ACC戰情

軟體部分: 
部門使用GUI程式權限有限制，使用Win Script自動化開啟在複製貼上權限跟檔案存擋，避免手動輸入的錯誤
在Siview & 報表在使用上帳密會有輸入錯誤上限, 密碼字串很長等，為了加速人員處理速度，使用python基於WIN32API SetFocus原理在不同的PID視窗做切換，Terminal作為簡易密碼輸入才切換原先視窗輸入帳密，替代原本無密碼確認的應用程式．
接戰情後要使用pywinauto 當中PIL實現監控以及調整已截圖到teams上
