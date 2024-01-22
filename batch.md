---
tags: IT
---
<style>
.highlight {color:red}
.elegant {color:blue}
</style>
# 資料來源: https://hackmd.io/@peterju/B1pUqd-5c
# 批次檔入門

<!-- - [第1次小考](https://hackmd.io/@peterju/rkBwY7Yzi)
- [第2次小考](https://hackmd.io/@peterju/r1UfiQSVs) -->
:::warning
本教學旨在介紹 Windows 下可進行自動化工作的【批次檔】該如何理解與掌握。
:::
在 Windows 作業系統下，原生就能進行<span class="elegant">自動化工作</span>的程式語言有3種選擇

- 批次檔(Batch file)
- WSH(Windows Scripting Host)
- PowerShell

為了達成作業系統下自動化執行程式的目的，Windows 作業系統很早就參考 Unix 採用了批次檔，但批次檔在歷經好多年的發展後相較於 Linux 的 Shell Script 生態系仍有不足，因此微軟在 Windows 98 時提出了依靠 Jscript 與 VBscript 來執行腳本語言的環境 WSH，後來更提出了建立在 .Net Framework 基礎上可跨平臺工作的自動化解決方案 PowerShell。

``` mermaid
graph LR

批次檔 --> WSH --> PowerShell
```

除了這些作業系統原生支援的 shell 之外，Windows 還可以安裝各式各樣的其它工具或語言來達成自動化的目的，例如

- 微軟自己的 Power Automate
- 第三方Windows平台自動化語言：AutoIt、AutoHotkey_L
- 跨平台的 Scripting 語言：PHP、Python、Ruby...

但不可否認的是批次檔並沒有在自動化工具的快速發展下消失，對於初學者而言，學習批次檔等同於學習 Windows 命令列環境(shell)的用法，Windows 環境目前有很多 Linux 的影子，例如導向、管線、指令與檔案名稱補齊...等，理解之後未來接觸 Linux 也有很大的幫助。

本著登高必自卑、行遠必自邇的學習次第，先學習批次檔基本功，用來幫助與處理日常的自動化需求， 未來再多樣化的學習各種 Script 語言，充分體會直譯式語言的魅力。
:::info
【自動化工作】

在此指的是為了自動化運作所需撰寫的程式語言，這些語言都必須搭配排定的工作(scaeduled task)來指定執行的時間，才能達成自動化的目的。
:::

## 1. 命令列特性
### 1.1 多行指令合併
要將分開多行的指令寫成一行，可利用 &
```bash=
dir & pause
```
### 1.2 顯示、設定與取用環境變數
1. 顯示環境變數
```bash=
set
```
2. 設定與取用環境變數
```bash=
set myname=Peter
echo %myname%
```
:::info
留意等號的左右不可有空白，因命令行會以空白作為命令與參數的分隔字元。
:::

### 1.3 目錄切換
CD指令是 change directory的縮寫，注意絕對路徑與相對路徑的差別，鍵入cd /?可得到更多的說明

1. 使用 /D 參數可以同時變更工作磁碟機及其工作目錄
```bash=
D: 
cd /d c:\windows\system32
```
2. 若路徑中含有空白字元時，請使用雙引號括起來
```bash=
cd "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
```
> 參考網頁：
> - [具有空格的長檔名或路徑需要引號](https://docs.microsoft.com/zh-tw/troubleshoot/windows-server/deployment/filenames-with-spaces-require-quotation-mark)

3. 顯示目前工作目錄
```bash=
cd
echo %cd%
```
4. 使用pushd儲存所在路徑，之後使用popd還原
```bash=
cd /d c:\windows\system32\drivers\etc
pushd %cd%
d:
popd
```
5. 顯示目前磁碟機
```bash=
echo %CD:~0,3%
```
:::info
以上的範例為字串的部分截取，詳情請參考 3.6字串的截取
:::

### 1.4 導向(Redirect)
導向有二種
1. 【輸出導向】，即命令的結果要輸出到哪裡？
    1. 檔案
    2. 控制碼
    3. 特殊裝置
```bash=
# 命令 > 作為輸出的檔案名稱
dir > list.txt
```
2. 【輸入導向】，即命令的輸入來自於哪裡？
    1. 檔案
    2. 控制碼
    3. 特殊裝置
```bash=
# 命令 < 作為輸入的檔案名稱
sort < list.txt
```
輸入導向與輸出導向作用在同一個命令上的範例：
```bash=
sort < list.txt > alphlist.txt
```
| 控制碼英文 | 控制碼數值 | 控制碼意義 |
| -------- | -------- | -------- |
| stdin    | 0     | 鍵盤輸入    |
| stdout    | 1    | 正常輸出至命令提示字元   |
| stderr    | 2     | 錯誤輸出至命令提示字元    |

輸出導向到檔案時，對於檔案來說有新建立與附加二種狀況
1. 新建立(>)
命令 > 檔案名稱
2. 附加(>>)
命令 >> 檔案名稱

### 1.5 命令的輸出
根據命令執行的結果是成功或失敗，會有2種輸出
    1. 標準輸出（1）
    2. 標準錯誤輸出（2）
    
| 命令 | 說明 |
| -------- | -------- |
|命令 2> 檔案名稱|將命令的標準錯誤輸出導向到檔案|
|命令 2>&1|將命令的標準錯誤輸出導向到標準輸出|
|命令 > 檔案名稱 2>&1|將命令的標準輸出與標準錯誤輸出全部導向到檔案|
    
```bash=
dir c: 1>cok.txt 2>cnotok.txt
dir f: 1>fok.txt 2>fnotok.txt
```

### 1.6 特殊裝置
Windows 效法了 Linux 作業系統將周邊裝置視為檔案的作法，至少有下列2種特殊裝置可視為檔案來運作
1. 主控台(CON)
代表【輸入】或【輸出】
```bash=
# 複製【輸入】到檔案
copy con newfile.txt
# 將檔案內容複製到【輸出】
copy newfile.txt con
# 將 set 指令的結果導向到輸出
set > con
# 將輸入的結果導向到 sort
sort < con
```
2. 黑洞(NUL)檔
每一個目錄都有一個黑洞檔，一般用來將指令的正常訊息導向至黑洞檔，使正常訊息不要顯示在螢幕上，然後配合判斷 errorlevel 或 %errorlevel%變數，寫入log
```bash=
ping 168.95.192.1 > nul
if errorlevel 1 echo ping target fail >> pinglog.txt
```
因為每一個目錄都有一個黑洞檔，因此我們也可以根據此原則寫出判斷某個目錄是否存在的判斷，例如：
```bash=
if not exist d:\temp\nul md c:\temp
if exist d:\temp\nul copy con d:\temp\test.txt
```
:::danger
但實務上因為判斷某個目錄是否存在太常用了，因此後來便可以省略判斷 nul，而直接判斷目錄本身了。
```bash=
if exist d:\temp copy con d:\temp\test.txt
```
:::

### 1.7 管線(Pipe)
將命令的輸出透過管線當作另一個命令的輸入

<table>
<tr><th>語法</th><th>指令</th></tr>
<tr><td>命令1 | 命令2</td><td>dir | sort</td></tr>
</table>

若要將指令的輸出複製到剪貼簿，可透過以下管線方式進行
```bash=
dir | clip
```

### 1.8 指令的 or 、and
表面上根據 or 、and 來判斷，實際上也是透過判斷回傳值來決定，從判斷前1個命令的成功或失敗來決定是否執行第2個命令
1. 命令1失敗才執行命令2 => 命令1 || 命令2
```bash=
ping 123.123.123.123 > nul || echo ping command fail
```
2. 命令1成功才執行命令2 => 命令1 && 命令2
```bash=
ping 168.95.192.1 > nul && echo %date%-%time% ping succeful >> pingTarget.log
```

### 1.9 暫停
- pause
程式暫停，提示按任意鍵繼續

```bash=
echo This Program is running...
pause
```
- timeout 秒數
程式暫停指定的秒數

```bash=
echo Please wait for a while...
timeout 6
```
### 1.10 過濾命令：find/findstr
find 命令可搜尋一或多個檔案中的文字字串，且區分大小寫。
- /I 當搜尋字串時，忽略字元的大小寫。
- /V 顯示所有不包含指定字串的行。

findstr 命令則更為強大，預設使用正規表示式進行搜尋。
- /S 在現存目錄及所有的子目錄中搜尋符合的檔案。
- /P 跳過沒有可列印字元的檔案。
```bash=
# 尋找 route print 輸出中，包含關鍵字（預設值）的行
route print | find "預設值"
# 尋找指定檔案中沒有關鍵字（#）的行
find /V "#" c:\Windows\System32\drivers\etc\hosts

# 尋找有1個關鍵字的行
findstr framerate test.cmd
# 尋找有2個關鍵字其中之一的行
findstr "framerate ffmpeg" test.cmd
# 尋找子目錄下所有檔案，且包含一個關鍵字，不分大小寫的行
findstr /s /i ffmpeg *.*
```
:::info
若在使用 findstr 時出現【FINDSTR: 寫入錯誤】的訊息，通常是因為傳回的文字包含了與目前的字碼不同的內容，例如包含了 UTF-8 的文字，此時可先下達 `chcp` 指令得知目前的字碼頁 (繁體中文是950、簡體中文是936)，然後更改字碼頁`chcp 65001`，完成 findstr 之後再更改回來 `chcp 950`。
:::

### 1.11 更改命令提示字元：prompt
請在命令提示字元視窗下練習輸入下面的指令，除了觀察提示字元的變化，並留意每呼叫一次cmd，可呼叫exit返回的特性。
```bash=
prompt Level1$g
cmd
prompt Level2$g
cmd
prompt Level3$g
exit
exit
```
:::info
可輸入prompt /? 來獲得更多的提示字元類型。
:::

## 2.批次檔基本認識
將命令提示字元(Command Prompt)中輸入的指令集結起來，輸入在文字檔中，用以批次執行，稱之為批次(Batch file)檔。

批次檔指令每行的長度預設為127個字元，執行後若要中斷可按下Ctrl+C。

命令提示字元預設的字碼頁為ANSI/BIG5編碼，因此檢視UTF-8編碼檔案時會出現亂碼，所以批次檔的編寫應盡量使用 ANSI 的編碼方式，建議使用 NotePad++ 之類的有顏色與語法提示的純文字編輯器編寫。

NotePad++目前編輯文字檔採用的編碼方式會在右下角提示
![](https://i.imgur.com/LNA08Xd.png)

建議透過功能表:編碼 / 轉換至ANSI 編碼格式
![](https://i.imgur.com/K5TdNgj.png)

便可將編碼轉換為 ANSI 格式。
![](https://i.imgur.com/B7mIP78.png)

若想使用 vscode 編輯器，因為 vscode 編輯器的預設編碼是 utf8，所以要配合批次檔在終端機預設的編碼是CP950(Big5/ANSI)的關係，我們可以加上以下設定到使用者或工作區的 settings.json
```json
{
    "files.autoGuessEncoding": true,
    "[bat]": {
        "files.encoding": "cp950",
        "files.autoGuessEncoding": true
    }
}
```
:::info
學習批次檔一般而言相當的簡單又直覺，怎樣算是學會呢，以本人的經驗，至少要將變數延遲展開特性與 for 迴圈指令給透徹了解才算是掌握了批次檔喔。
:::

### 2.1 副檔名
預設有下面這2種，在DOS與Windows 9x 時代副檔名為.bat，在Windows NT 之後則改用.cmd，表示在視窗模式下的命令提示字元(cmd.exe)執行

- bat
- cmd

### 2.2 註解方式
標準是使用 rem，但通常會使用2個或以上的冒號來當註解符號

- rem
- ::

### 2.3 標題
使用 title 可為執行批次檔的終端機加上標題，請參考下例：
```bash=
@echo off
title 主程式
dir
```

### 2.4 回應狀態(echo)
終端機預設會採用一問一答的回應模式，因此下達的指令都會顯示出來，若要關閉下達的命令，必須在命令之前加上 @ 符號，例如
```bash=
@dir
@pause
```
但指令多的時候，每一道命令前都要加上 @ 就顯得麻煩了，因此可在批次檔一開頭加上 `@echo off ` ，便可一次性的關閉回應了。
```bash=
@echo off
dir
pause
```
除此之外，echo還會被用來顯示字串與變數，例如
```bash=
@echo off
set /P myname=Please input your name:
echo Hello %myname%
echo.
echo Today is %date% %time%
pause
```
>- 停止下達的指令顯示在螢幕上 => echo off
>- 空一行 => echo.
>- 顯示當前目錄 => echo %cd%
>- 顯示日期 => echo %date%
>- 顯示時間 => echo %time%

### 2.5 判斷(if)
1. IF [NOT] string1==string2 命令
當指定的文字字串相符合時，則條件為真。大小寫視為不一致。
```bash=
set myname=Tom
if %myname%==Tom echo Hi, Tom
if not %myname%==Tom echo %myname% 你無法存取
```
2. IF [NOT] EXIST filename 命令
如果指定的檔名存在時，則條件為真。
```bash=
if exist c:\temp\nul echo 目錄TEMP存在
if not exist c:\temp\nul echo 目錄TEMP不存在
```
3. ELSE 子句
```
語法1：
    IF 判斷式 (
        命令1
    ) ELSE IF 判斷式 (
        命令2
    ) ELSE (
        命令3
    )

語法2：
    IF 判斷式 (命令1) ELSE IF 判斷式 (命令2) ELSE echo (命令3)
```
4. IF [NOT] define 變數 命令
根據變數是否已定義執行命令
```bash=
set myname=Tom
if defined myname echo %myname%
if not defined hername echo hername 未定義
```
5. IF 的其它判斷
以下介紹使用者輸入空值與不分大小寫的作法
```bash=
set yn=
set /p yn=以上正確否 (Y/N)?
if "%yn%"=="" goto :EOF
rem if /I %yn%==n goto q1
if /I "%yn%"=="n" goto q1
```

:::danger
if 在判斷使用者輸入時，若遇到使用者直接按Enter等於讓變數成為空值，此時會造成程式錯誤，因此請務必在進行變數輸入判斷時加上雙引號。
:::

### 2.6 回傳值
無論是在 Linux 下撰寫 shell script 或是在 Windows 下撰寫批次檔，最近一次程式執行的回傳值判斷，在撰寫工作自動化的 Script 檔時，是非常重要的技巧。

在Windows環境中的慣例是，若指令成功時傳回0，若錯誤時，依據錯誤的狀況會傳回 1 或以上的值，代表不同的錯誤狀況。

但並非所有指令都會根據正確或錯誤而有不同的回傳值，要用來判斷前請先測試一下。

```bash=
ping 168.95.192.1
echo %errorlevel%

ping 123.123.123.123
echo %errorlevel%
```

判斷回傳值錯誤的方式有2種

**1. 判斷錯誤等級變數 => if %errorlevel%==1**
```bash=
ping 123.123.123.123 > nul
if %errorlevel%==1 echo %date%-%time% ping command fail >> pingTarget.log
```
**2. 錯誤判斷子句 => if errorlevel 1**
if errorlevel 1 表示若回傳值大於等於1(>=1)， 當使用多個錯誤判斷子句時，一定要根據errorlevel遞減的順序來排列， 因為錯誤判斷子句有上述2個隱含意義，因此建議使用第1種判斷錯誤等級變數的方式為佳。

```bash=
ping 123.123.123.123 > nul
if errorlevel 1 goto ONE
if errorlevel 0 goto ZERO
goto END
:ZERO
 echo %date%-%time% ping command succeful >> pingTarget.log
 goto END
:ONE
 echo %date%-%time% ping command fail >> pingTarget.log
:END
```
### 2.7 命令列參數
假設在命令列鍵入了下列指令
```bash=
test.cmd c:\windows\notepad.exe c:\windows\write.exe
```

此時批次檔內部自動將命令列上的參數視為特別的變數如下表


| %0 (命令)| $1 (參數1)| %2 (參數2)|
| -------- | -------- | -------- |
| "test.cmd"| "c:\windows\notepad.exe"	| "c:\windows\write.exe" |

請以Notepad++編輯 test.cmd 並輸入下面的指令

```bash=
@echo off
echo command = %0
echo argument1 = %1
echo argument2 = %2
pause
```
存檔後，請在命令列執行以下指令
```bash=
test.cmd c:\windows\notepad.exe c:\windows\write.exe
```
### 2.8 擴充字元參數
承上例，若在批次檔內的命令列參數加上擴充字元之後，可額外得知參數的許多資訊，請參考下表

|  %1 |  %~1 |
| --- | --- |
|"c:\windows\notepad.exe"|c:\windows\notepad.exe|

|%~d1 (取得磁碟機代號)|%~p1 (取得路徑)|%~n1 (取得檔名)|%~x1 (取得副檔名)|
| ----- | --- | --- | --------- |
|c:| \Windows\ | notepad|.exe|

```bash=
rem 請注意【~】符號的作用
echo %1
echo %~1
echo %~d1
echo %~p1
echo %~n1
echo %~x1
```

常用功能：切換工作目錄至批次檔所在目錄
```bash=
cd /d "%~dp0"
```
逐項解釋如下：
- %0：代表批次檔完整路徑與檔名，並以雙引號包裹
- %~0：代表批次檔完整路徑與檔名，但無雙引號
- %~d0：其中的`~d` 代表取得 %0 的磁碟機代號
- %~p0：其中的`~p` 代表取得 %0 的路徑
- %~dp0：其中的`~dp` 代表取得 %0 的磁碟機代號+路徑

:::info
更多的擴充字元請輸入 call/? 或參考 http://inpega.blogspot.tw/2012/07/cd-dp0.html 來獲得。
:::

### 2.9 參數位移
若參數的數量不確定該如何處理呢，請看以下程式範例，主要判斷若 %1 存在，處理完後以 shift 將後面的參數往前位移。
```bash=
@echo off
cd /d "%~dp0"
:next
if exist "%~1" (
   echo 目前處理檔案："%~1" 
   shift
   goto next
) else (
   pause
   goto :EOF
)
```

### 2.10 跳行與結束程式
- goto 標籤 (須定義標籤，標籤須單獨一行，並以冒號開頭)
```bash=
if not exist c:\temp\nul goto newdir
cd /d c:\temp
del * /y
:newdir
mkdir c:\temp
```
- goto :eof (無須定義標籤，直接結束程式之意)
```bash=
set /p end=按 0 結束程式:
if %end%==0 goto :eof
```
- exit /b [回傳值]
使用 exit /b 可停止批次檔或副程式的執行，若結束後需要提供回傳值讓 if 指令 檢查 errorlevel 變數，可於其後加上想要的數值
```bash=
rem myping.cmd 168.95.192.1
@echo off
ping %1 > nul
if %errorlevel%==1 goto error
ping %1 ok
exit /b 0
:error
echo ping fail
exit /b 1
```

設定副程式結束後回傳值為 5
```bash=
@echo Off
call :setError
echo %errorlevel%
goto :eof

:setError
Exit /B 5
```
:::danger
若遇到終端機下游標消失問題，可至控制台/滑鼠下將【打字時隱藏指標】的勾取消試試。
![](https://i.imgur.com/4JEoBat.png =350x)
:::

## 3.批次檔的變數
### 3.1 設定變數
批次檔使用的變數就是作業系統的環境變數，一般來說都視為字串變數，而且是是全域變數，我們可以透過下面的指令觀察有哪些環境變數。
```bash=
set
```
設定變數時，一樣使用 set 指令，注意等號左右不能有空白。
```bash=
set myname=Peter
```
若設定的變數代表路徑時，因為路徑中可能包含空白字元，建議以雙引號含括起來較好，單純顯示沒問題，但在命令列解析時，因為會以空白當作參數分隔，若沒有用雙引號時，會被分開當成2個參數處理，造成錯誤。
```bash=
set ProgramPath="c:\Program Files (x86)"
```

### 3.2 取用變數
取用變數時，則需在變數前後加上%
```bash=
echo %myname%
```

### 3.3 取消變數
取消變數時，只需依照設定變數的方式，但值是空白即可
```bash=
set var=
```

### 3.4 變數的運算
set 使用 /a 參數，可使後面的敘述成為運算式，且只能處理整數的計算，無法處理小數。
```bash=
set var=6
set /a var+=3
```
需注意的是，若變數的值為08或09的時候，會被視為一個錯誤的8進位而其值為0，影響後續的計算
```bash=
set var=08
set /a var+=3
set var=09
set /a var+=3
```
:::info
set 運算式限制數字為 32 位元精確度(範圍是 -2147483648 到 214748364)
:::

### 3.5 變數的比較
因為大於(>)與小於(<)符號，在終端機中有【導向輸出】與【導向輸入】的用意，因此會改用關鍵字進行比較運算符，請參考下表：

|    比較運算符    |   意義   |
| -------------- | -------- |
|  EQU     | 等於 |
|  NEQ     | 不等於 |
|  LSS     | 小於 |
|  LEQ     | 小於等於 |
|  GTR     | 大於 |
|  GEQ     | 大於等於 |

```bash=
@echo off

rem 設定變數a = 10
set /A a=10

rem 顯示變數a的值
echo %a%

rem 使用==判斷變數a的值是否等於10
if %a% == 10 (
    echo a is 10
) else (
    echo a is not 10
)

rem 使用not及==判斷變數a的值是否不等於10
if not %a% == 10 (
    echo a is not 10
) else (
    echoa is 10
)

rem 使用 EQU 判斷變數a的值是否等於10
if %a% EQU 10 (
    echo a is 10
) else (
    echo a is not 10
)

rem 使用 NEQ 判斷變數a的值是否不等於10
if %a% NEQ 10 (
    echo a is not 10
) else (
    echo a is 10
)
```

### 3.6 輸入提示
set 使用 /p 參數，等號(=)開始到冒號(:)結束的一段文字將視為輸入的提示
```bash=
@echo off
:menu
echo 1.dir
echo 2.dir /w
echo 0.離開
set /p id=請輸入功能代碼:
if %id%==1 goto one
if %id%==2 goto two
if %id%==0 goto zero
:one
dir
goto menu
:two
dir /w
goto menu
:zero
```

### 3.7 字串的擷取
批次檔也可以像一般程式語言一樣，做到從字串的第n個位置開始擷取m個字元這件事

| 步驟 | %date% | %date:~0,4% |
| -------- | -------- | -------- |
|說明     | 當下日期變數     | 變數從第0位開始取4碼  |
|值     | 2015/10/17 週六   | 2015 |

上述說明的程式碼如下
```bash=
set today=%date:~0,4%/%date:~5,2%/%date:~8,2%
echo %today%
```

字串擷取符號說明
* 冒號(:)
* 波浪符號(~)
* 開始位置(從0開始)
* 逗號(，)
* 擷取幾個字元

### 3.8 字串的取代
批次檔也可以進行字串的取代，方式跟字串的擷取有點類似，下面的範例說明如何將(140.128.71.1)替換為[140.128.71.1]

| 步驟1 | %var% | %var:(=[% |
| -------- | -------- | -------- |
|說明     | var變數     | 將 ( 替換為 [ |
|值     | (140.128.71.1)   | [140.128.71.1) |

| 步驟2 | %result%| %result:)=]% |
| -------- | -------- | -------- |
|說明     | result變數(存放前一步驟的結果) | 將 ) 替換為 ]  |
|值     | [140.128.71.1)  | [140.128.71.1] |

上述說明的程式碼如下
```bash=
@echo off
set var=(140.128.71.1)
set result=%var:(=[%
set result=%result:)=]%
echo %result%
Pause
```
字串取代符號說明
* 冒號(:)
* 字串中想要被替換的子字串
* 等號(=)
* 替換後的子字串
:::info
其他的進階用法，請輸入 set /? 或參考 https://ss64.com/nt/set.html
:::

### 3.9 變數延遲展開
請猜一下底下這個範例會顯示的值是甚麼?
```bash=
@echo off 
set var=Peter
set var=John & echo %var%
timeout 6
```
結果居然是 Peter，因為針對第3行，批次檔的命令解譯器會先【取值】`echo %var%`，然後才進行【賦值】 `set var = John` 的關係，若要避免同時進行【取值】與【賦值】時，仍得到前一個變數的結果，必須開啟變數延遲展開(SetLocal enabledelayedexpansion)，才能如同一般程式語言循序處理變數，這個特性造成很多人無法正確駕馭批次檔的變數行為，甚為可惜。

若要正確取出此變數異動後的值 John ，必須<span class="highlight">啟用變數延遲展開(SetLocal EnableDelayedExpansion)</span>的功能，在開啟用變數延遲展開功能之後，取用變數的方式必須由 <span class="highlight">%var%</span> 更改為 <span class="highlight">!var!</span>，將範例修改如下
```bash=
@echo off
SetLocal EnableDelayedExpansion
set var=Peter
set var=John & echo !var!
timeout 6
```
可能你會說，我只要不使用 & 符號將【取值】與【賦值】寫在同一行就可以避開這個問題啦，但批次檔對於 if 與 for 的括號內的敘述，就是視為放在同一行的，請看以下範例
```bash=
@echo off
set var=Peter
if defined var (
   set var=John
   echo %var%
)
timeout 6
```
結果仍然是 Peter，因為第4-5行實際上會被視為放在同一行
`set var=John &   echo %var%`
因此必須如以下範例，加上變數延遲展開(SetLocal EnableDelayedExpansion)，與改變取值方式，才能避開這個問題。
```bash=
@echo off
SetLocal EnableDelayedExpansion
set var=Peter
if defined var (
   set var=John
   echo !var!
)
timeout 6
```
若要取消變數延遲展開，可下達指令
`SetLocal DisableDelayedExpansion`

## 4. 呼叫外部程式與副程式
### 4.1 呼叫外部程式
常用的呼叫外部程式有下列幾種方式
1. call 外部程式
2. cmd /c 外部指令
3. 開始一個新視窗執行程式 => start [program] [parameters]

**1. call 外部程式**
從批次檔中呼叫外部程式，外部程式執行完畢後返回批次檔繼續往下執行。在同一個 shell 環境下，可存取相同的環境變數。
> test.cmd
```bash=
@echo off
echo 01
call test1.cmd 02
echo 03
pause
```
> test1.cmd
```bash=
@echo off
echo %1
timeout 3
```
**2. cmd /c 外部指令**
呼叫一個新的shell程式(cmd)並於指令執行完成後結束這個 shell ，返回原來的shell環境。
```bash=
@echo off
cmd /c notepad.exe
exit
```
留意上述範例執行情形，在notepad.exe關閉以前，不會執行 exit 指令，因為指令尚未結束，還留在新的shell當中。

**3. 開始一個新視窗執行程式 => start [program] [parameters]**
因為 cmd /c 具有同步特性(會等外部程式執行完畢)，因此不太適合呼叫需與使用者互動的視窗程式，因為命令提示視窗會因等待而保持開啟，所以適合改用 start 來呼叫執行。
```bash=
@echo off
start notepad.exe
exit
```
:::info
使用 /wait 也可以改讓 start 具有同步特性，詳情參考 start /?
:::

### 4.2 呼叫副程式
批次檔的副程式呼叫也是利用 call 指令，不同的是 call 的對象不是外部程式 ，而是相同檔案中的標籤，也可以傳遞參數。

因為批次檔的副程式僅利用標籤代表區塊的開始，因此副程式都放在程式的尾部，之後就不要寫任何命令敘述了，代表區塊的結束。

因為批次檔循序讀取的特性，就算副程式沒有被呼叫，也會被當作標籤一般順序執行下來，因此在副程式之前通常要加上 `goto :EOF` 強制結束批次檔。

```bash=
@echo off
rem for迴圈使用方式請參考本手冊相關章節
for %%i in (*.dll *.exe) DO CALL :SubRoutin "%%i"
pause
goto :EOF

:SubRoutin
echo %1, %~n1, %~x1
```
> call :標籤 參數1 參數2...

## 5. for 迴圈
批次檔的 for 迴圈很重要，但有些特性比較隱晦，不容易駕馭，下面稍加整理需注意使用之處

1. for 迴圈初始化變數，在撰寫為批次檔時，請使用 %%variable，而在命令列執行時要改用 %variable。
2. for 迴圈初始化變數有大小寫的區分，所以 %%i 不同於 %%I。
3. for 迴圈內的變數可能會有取值異常的情形。

以下針對第3點取值異常的情形作一說明，迴圈的敘述通常是以下列格式撰寫，左括弧與 do 同一行，右括弧放在最後面獨立成行

```bash=
@echo off
set fname=none
for %%i in (*) do (
    set fname=%%i
    echo %fname%
)
pause
```

但其實批次檔會把迴圈內的敘述集結成一行變成
```bash=
for %%i in (*) do set fname=%%i & echo %fname%
```
因為集結成一行的關係，批次檔在命令解譯器進行直譯時，會對每一行敘述中的變數進行先取值後設定的動作，因此在迴圈中若要同時進行【取值】與【賦值】的動作，要記得使用 `SetLocal EnableDelayedExpansion`，範例如下：
```bash=
@echo off
SetLocal EnableDelayedExpansion
set fname=none
for %%i in (*) do (
    set fname=%%i
    echo !fname!
)
pause
```
詳情請參考 [3.9 變數延遲展開小節](#3.9-變數延遲展開)的說明。

:::info
批次檔中只要是利用括弧()分成多行撰寫的指令，實際上都看成一行，在括弧()裡面取用變數時，需特別留意是否需要開啟變數延遲展開(SetLocal EnableDelayedExpansion)功能。
:::

以下直接說明範例不特別解釋語法，細節請透過 for /? 學習

### 5.1 找出符合條件之檔案的 for 迴圈

**1. 顯示批次檔存在的目錄中所有符合 `.mp4 .avi *.mpg` 的檔案名稱**

```bash=
@echo off
for %%i in (*.mp4 *.avi *.mpg) DO echo %%i
```

**2. 顯示使用者目錄中的所有檔案名稱**
```bash=
for %i in (%userprofile%\*) DO @echo %i
```
> 此例必須直接在命令列輸入(注意變數名稱的差別)、環境變數 userprofile 代表使用者目錄

### 5.2 找出符合條件之目錄的 for /D 迴圈
顯示使用者目錄中的所有目錄名稱 此例必須直接在命令列輸入(注意變數名稱的差別)、環境變數 userprofile 代表使用者目錄
```bash=
for /D %i in (%userprofile%\*) DO @echo %i
```

### 5.3 遞迴搜尋指定的路徑下所有符合檔案的 for /R 迴圈
將 c:\temp\ 目錄與所有子目錄下的 *.bak 刪除
```bash=
@echo off
for /R c:\temp\ %%G in (*.bak) do del "%%G"
```
將 c:\temp\ 目錄與所有子目錄下的 mkv 與 mov 檔丟給副程式處理
```bash=
@echo off
for /r c:\temp\ %%i in (*.mkv *.mov) DO CALL :SubRoutin "%%i"
```

### 5.4 可以設定開始數值、增/減數值、停止數值的 for /L 迴圈
1. 顯示 0-100 的數字 (從0開始、遞增1、終止值100)
```bash=
@echo off
for /L %%i in (0 1 100) do echo %%i
```
2. 計算從1累加至100的和
```bash=
@echo off
set sum=0  
for /L %%i IN (100, -1, 1) DO set /a sum+=%%i 
echo %sum%
```
3. 啟用延遲環境變數擴充功能範例
```bash=
@echo off
SetLocal EnableDelayedExpansion 
for /L %%i in (1 1 5) do (
set var=%%i
echo !var!
)
timeout 6
```

### 5.5 逐行讀取文字檔的 for /F 迴圈
for /F 是迴圈中最重要的應用，因為它可以讀取檔案、讀取字串與讀取命令，分別說明如下：
**1. 讀取檔案：逐行讀取指定的檔案，然後依照分隔符號將內容賦值給指定變數**
範例：逐行讀取 test.ini 文字檔內容，以等號(=)為分隔，左邊給%%i，右邊給%%j
```bash=
@echo off
FOR /F "tokens=1,2 delims==" %%i IN (test.ini) DO set %%i=%%j
```
test.ini 內容如下
```bash=
account=john
passwd=a1234567890
```
上述指令執行完畢之後會有下列效果， 將原來必須放在批次檔內部的變數設定，放在外部的 ini 檔之後進行讀取，將程式碼與設定檔分離，可減少原始檔被亂改的機會
> set account=john
> set passwd=a1234567890

**2. 讀取字串：讀取字串或變數，然後依照分隔符號將內容賦值給指定變數**
範例1：讀取變數%date%, 以【斜線】與【空白】為分隔，依序給%%a、%%b、%%c三變數，再依照年/月/日的格式，儲存到 mydate 變數
```bash=
For /f "tokens=1-3 delims=/ " %%a in ("%date%") do set mydate=%%a/%%b/%%c
```
範例2：讀取變數 %time%, 以【空白】與【.】為分隔，依序給%%a、%%b、%%c三變數，再依照【時 分 秒】的格式，儲存到 mytime 變數
```bash=
For /f "tokens=1-3 delims=:." %%a in ("%time%") do set mytime=%%a %%b %%c
```

**3. 讀取命令：將命令執行的結果，做為 for /F 迴圈讀取的來源**
> 將命令執行的結果，做為 for /F 迴圈讀取的來源，須注意此命令須包含在單引號之間。

範例1：將命令 date /t 的執行結果, 以【斜線空白】(/ )為分隔，將內容依序賦值給%%a、%%b、%%c三變數，輸出年-月-日的格式
```bash=
for /F "tokens=1-3 delims=/ " %%a in ('date /t') do echo %%a-%%b-%%c
```
:::danger
請留意分隔符號後【空白】的作用時機
:::

範例2：將命令 sc query 的執行結果透過管線輸出給 find 指令，尋找包含有SERVICE_NAME字串的列，然後將第2欄的內容存到 %i 變數並顯示出來
```bash=
rem 此例必須直接在命令列輸入(注意變數名稱的差別)
for /f "tokens=2" %i in ('sc query ^| find /i "SERVICE_NAME"') do @echo %i
```
> sc query 命令會顯示目前系統所有的服務

:::danger
若命令中包含了管線 | ，則須在管線前方加上逸脫字元 ^，是為了避免被視為外層指令的管線符號。
:::

範例3：利用 findstr 過濾文字檔(.csv)包含有井字號(#)的列,然後 以逗號(,)為分隔，依序給%%I、%%J、%%K、%%L 4變數，然後再分別設定到有意義的變數中儲存
```bash=
rem 設定參數檔名與批次檔相同(.csv)
set cfg=%~n0.csv
FOR /F "tokens=1,2,3,4 delims=," %%I IN ('findstr /V [#] %cfg%') DO (
 set remoteDIR=%%I
 set localBackupFolder=%%J
 set RetentionDay=%%K
 set isCallCheckspace=%%L
)
```
與批次檔同名的csv檔，其內容如下
```csv=
#遠端備份名稱,本地端備份路徑,備份保留天數,是否檢查硬碟剩餘空間
myweb,C:\backup,20,Y
```

## 6. 技巧
1. 【echo 如何不換行】與【如何顯示一個空白字元】
```bash=
// 留意是否有雙引號與空白字元的位置
echo|set /p="[請輸入] " & echo|set /p=" :"
```
2. 如何讓一個變數內包含換行字元？
```bash=
@echo off
set LF=^&echo.
set tmp=%date%%LF%%time%
echo %tmp%

SetLocal EnableDelayedExpansion
set LF=^& echo.
set tmp=%date%!LF!!LF!!LF!%time%
echo %tmp%
```
3. 如何安裝 Windows子系統 Linux 版
輸入 wsl --install
```bash=
C:\Users\Administrator>wsl --install
正在安裝：虛擬機器平台
已完成安裝 虛擬機器平台。
正在安裝：Windows 子系統 Linux 版
已完成安裝 Windows 子系統 Linux 版。
正在安裝：Ubuntu
已完成安裝 Ubuntu。
已成功執行所要求的操作。請重新開機，變更才能生效。
```
4. 增加 readline 命令行編輯功能
- 下載：[Clink](https://github.com/chrisant996/clink/releases) 
- 其功能可參考這篇介紹：[clink：擴充cmd.exe成為Bash readline命令行的強大編輯功能](https://jdev.tw/blog/3919/bash-style-readline-for-cmd-exe)
- 間接的好處就是避免命令列游標會消失的問題

## 7. 練習


1. 請解釋此指令 `sort < list.txt > alphlist.txt`
2. 請解釋此指令 `if errorlevel 1 echo ping target fail >> pinglog.txt`
3. 請定義並顯示一個 today 的變數，其格式為月日年，例如10/12/2015
4. 請撰寫一個指令檔，提示使用者需輸入姓名與出生的西元年，輸入之後請顯示XXX您好，您的年齡為：n歲
5. 請以批次檔完成九九乘法表，顯示格式如下
```
2x1=2
2x2=4
.....
2x9=18
3x1=3
.....
9x9=81
```
6. 請解釋下列指令執行的結果
```bash=
@echo off
set val=1
echo %val%
(
set val=2
echo %val%
set val=3
echo %val%
)
echo %val%
pause
```
7. 請利用 route print、find 等指令，撰寫一個可顯示自己電腦IP的批次檔
8. 請將以下內容儲存為 source.txt，然後撰寫批次檔抓出其中的網站名稱
```
# appcmd list sites
SITE "Default Web Site" (id:1,bindings:http/*:80:,https/*:443:,state:Started)
SITE "轉學考新版2012_transs" (id:2,bindings:http/*:80:transs.ncut.edu.tw,state:Stopped)
SITE "停車證管理car" (id:3,bindings:http/*:80:car.ncut.edu.tw,state:Started)
SITE "綜合業務組trans" (id:4,bindings:http/*:80:trans.ncut.edu.tw,state:Stopped)
SITE "進修學院ncsc4" (id:6,bindings:http/*:80:ncsc.ncut.edu.tw,state:Started)
SITE "進修部shuky_cee" (id:7,bindings:http/*:80:cee.ncut.edu.tw,state:Started)
SITE "SSL_2016" (id:8,bindings:http/*:80:SSL_2016.ncut.edu.tw,state:Started)
SITE "SSL_2017" (id:9,bindings:http/*:80:SSL_2017.ncut.edu.tw,state:Started)
SITE "二技招生apply5" (id:10,bindings:http/*:80:apply.ncut.edu.tw,state:Stopped)
SITE "研教組gsee" (id:11,bindings:http/*:80:gsee.ncut.edu.tw,https/*:443:gsee.ncut.edu.tw,state:Started)
SITE "四技申請入學highschool8" (id:12,bindings:http/*:80:highschool.ncut.edu.tw,https/*:443:highschool.ncut.edu.tw,state:Started)
```
執行結果如下：
```
D:\>grepsite.cmd source.txt
--------------------
transs.ncut.edu.tw
car.ncut.edu.tw
trans.ncut.edu.tw
ncsc.ncut.edu.tw
cee.ncut.edu.tw
SSL_2016.ncut.edu.tw
SSL_2017.ncut.edu.tw
apply.ncut.edu.tw
gsee.ncut.edu.tw
highschool.ncut.edu.tw
--------------------
共10個網站

D:\>
```
ps.請留意檔案編碼

### 參考解答
:::spoiler
1. 將 list.txt 導向輸入給 sort 命令，sort命令排序處理之後，導向輸出到 alphlist.txt
2. 若前一個指令的回傳值大於等於1，則用附加的方式導向輸出 ping taret fail 字串到 pinglog.txt 檔案
3. quiz3.cmd
```bash=
@echo off
rem 答案1
set today=%date:~5,2%/%date:~8,2%/%date:~0,4%
echo %today%
rem 答案2
for /F "tokens=1,2,3 delims=/ " %%a in ('date /t') do set today=%%b-%%c-%%a
echo %today%
```
4. quiz4.cmd
```bash=
@echo off
set /p myname=請輸入您的姓名:
set /p mybiryear=請輸入您的出生西元年:
set /a myage=2015 - mybiryear
echo.
echo %myname%您好，您的年齡為：%myage%歲
pause
```
5. quiz5.cmd
```bash=
@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
for /L %%i in (2 1 9) do for /L %%j in (1 1 9) do (
 set /a sum=%%i*%%j
 echo %%ix%%j=!sum!
)
pause
```
6. 因為沒有啟用延遲環境變數擴充功能，因此在括弧內的取用(echo %val%)會先作用，因此中間的echo 回應都是1，最後才執行變數的賦值(set val=3)，所以最終echo的結果是3。
7. showip.cmd
```bash=
@echo off
rem route print | for /f "tokens=4" %i in ('find "0.0.0.0"') do @echo %i & exit /b
FOR /F "tokens=4 delims= " %%i in ('route print ^| find "0.0.0.0"') do echo %%i & goto NEXT
:NEXT
pause
```
:::

## 參考資源
* [如何利用批次檔(Batch)讀取指令執行的結果或文字檔案內容](https://blog.miniasp.com/post/2010/09/24/How-to-parse-text-from-file-or-command-using-Batch)
* [MSDN Library 使用批次檔](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc758944(v=ws.10)?redirectedfrom=MSDN)
* [Guide to Windows Batch Scripting](http://steve-jansen.github.io/guides/windows-batch-scripting/index.html)
* [Top 10 DOS Batch tips](https://weblogs.asp.net/jongalloway/top-10-dos-batch-tips-yes-dos-batch)
* [An A-Z Index of the Windows CMD command line](https://ss64.com/nt/)
* [Getting started with batch files](https://www.robvanderwoude.com/batchstart.php)
* [Batch Utilities](https://www.robvanderwoude.com/batchtools.php)

## 參考影片
- [我的 Windows 平台自動化經驗：基礎批次檔撰寫實務](https://www.youtube.com/watch?v=Kyd3Mmo1rhI)