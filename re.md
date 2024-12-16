這一課介紹如何利用SQL 的INSERT 語句將資料插入表中。
15.1 數據插入
毫無疑問，SELECT 是最常用的SQL 語句了，這就是前14 堂課都在講它的
原因。但是，還有其他3 個常用的SQL 語句需要學習。第一個是INSERT
（下一課介紹另外兩個）。
顧名思義，INSERT 用來將行插入（或新增）到資料庫表。插入有幾種
方式：
* 插入完整的行；
* 插入行的一部分；
* 插入某些查詢的結果。
以下逐一介紹這些內容。
提示：插入及系統安全
使用INSERT 語句可能需要客戶端/伺服器DBMS 中的特定安全權限。
在你試圖使用INSERT 前，你應該要確保自己有足夠的安全權限。
15.1.1 插入完整的行
把資料插入表中最簡單的方法是使用基本的INSERT 語法，它要求指定
表名和插入到新行中的值。下面舉個例子：
輸入▼
INSERT INTO Customers
VALUES(1000000006,
'Toy Land',
'123 Any Street',
'New York',
'NY',
'11111',
'USA',
NULL,
NULL);
分析▼
這個範例將一個新顧客插入到Customers 表中。儲存到表中每一列的數
據在VALUES 子句中給出，必須提供一個值給每一列。如果某列沒有值，
如上面的cust_contact 和cust_email 列，則應該使用NULL 值（假定
表允許對該列指定空值）。各列必須以它們在表定義中出現的次序填入。
提示：INTO 關鍵字
在某些SQL 實作中，跟在INSERT 之後的INTO 關鍵字是可選的。但
是，即使不一定需要，最好還是提供這個關鍵字，這樣做將確保SQL
程式碼在DBMS 之間可移植。
雖然這種語法很簡單，但並不安全，應該盡量避免使用。上面的SQL 語
句高度依賴表中列的定義次序，也依賴其容易取得的次序資訊。即
使可以得到這種次序訊息，也不能保證各列在下一次表結構變動後保持完全相同的次序。

因此，編寫依賴特定列次序的SQL 語句是很不安全
的，這樣做遲早會出問題。
寫出INSERT 語句的更安全（不過更煩瑣）的方法如下：

```
INSERT INTO Customers(cust_id,
cust_name,
cust_address,
cust_city,
cust_state,
cust_zip,
cust_country,
cust_contact,
cust_email)
VALUES(1000000006,
'Toy Land',
'123 Any Street',
'New York',
'NY',
'11111',
'USA',
NULL,
NULL);
```

這個範例與前一個INSERT 語句的工作完全相同，但在表名後面的括號裡
明確給出了列名。在插入行時，DBMS 將以VALUES 清單中的對應值填
入列表中的對應項。 VALUES 中的第一個值對應於第一個指定列名，第二
個值對應第二個列名，如此等等。
因為提供了列名，VALUES 必須以其指定的次序來匹配指定的列名，不一定
按各列出現在表中的實際次序。其優點是，即使表的結構改變，這條
INSERT 語句仍然能正確運作。

說明：不能插入同一筆記錄兩次
如果你嘗試了這個例子的兩種方法，會發現第二次產生了一條出錯消
息，說ID 為1000000006 的顧客已經存在。在第一課我們說過，主
鍵的值必須有唯一性，而cust_id 是主鍵，DBMS 不允許插入相同
cust_id 值的新行。下一個例子也是同樣的道理。要再嘗試另一種
插入方法，需要先刪除掉已經插入的記錄（下一課會講）。要么就別
嘗試新方法了，反正記錄已經插入好，你可以繼續往下學習。
下面的INSERT 語句填入所有欄位（與前面的一樣），但以不同的次序
填充。因為給了列名，所以插入結果仍然正確：
INSERT INTO Customers(cust_id,
cust_contact,
cust_email,
cust_name,
cust_address,
cust_city,
cust_state,
cust_zip)
VALUES(1000000006,
NULL,
NULL,
'Toy Land',
'123 Any Street',
'New York',
'NY',
'11111');
提示：總是使用列的列表
不要使用沒有明確給出列的INSERT 語句。給出列能使SQL 程式碼繼續
發揮作用，即使表結構發生了變化。

15.1.2 插入部分行
如所述，使用INSERT 的建議方法是明確給出表的列名。使用這種語
法，也可以省略列，這表示可以只給某些列提供值，給其他列不提供值。
請看下面的例子：
輸入▼
INSERT INTO Customers(cust_id,
cust_name,
cust_address,
cust_city,
cust_state,
cust_zip,
cust_country)
VALUES(1000000006,
'Toy Land',
'123 Any Street',
'New York',
'NY',
'11111',
'USA');
分析▼
在本課前面的例子中，沒有給cust_contact 和cust_email 這兩列提
供值。這表示沒必要在INSERT 語句中包含它們。因此，這裡的INSERT
語句省略了這兩個欄位及其對應的值。


注意：省略列
如果表格的定義允許，則可以在INSERT 作業中省略某些欄位。省略的列
必須滿足以下某個條件。
* 此欄位定義為允許NULL 值（無值或空值）。
* 在表格定義中給予預設值。這表示如果不給出值，將使用預設值。
注意：省略所需的值
如果表中不允許有NULL 值或預設值，這時卻省略了表中的值，
DBMS 就會產生錯誤訊息，對應的行不能成功插入。

15.1.3 插入檢索出的數據
INSERT 一般用來給表格插入具有指定列值的行。 INSERT 還有另一種形
式，可以利用它將SELECT 語句的結果插入表中，這就是所謂的INSERT
SELECT。顧名思義，它是由一條INSERT 語句和一條SELECT 語句組成的。
假如想把另一表中的顧客欄位合併到Customers 表中，不需要每次讀取一
行再將它用INSERT 插入，可以如下進行：
輸入▼
INSERT INTO Customers(cust_id,
cust_contact,
cust_email,
cust_name,
cust_address,
cust_city,
cust_state,
cust_zip,
cust_country)
SELECT cust_id,
cust_contact,
cust_email,cust_name,
cust_address,
cust_city,
cust_state,
cust_zip,
cust_country
FROM CustNew;
說明：新例子的說明
這個範例從一個名為CustNew 的表格中讀出資料並插入到Customers
表。為了試驗這個例子，應該先建立和填入CustNew 表。 CustNew
表的結構與附錄A 所述的Customers 表相同。在填充CustNew 時，
不應該使用已經在Customers 中使用過的cust_id 值（如果主鍵值重
復，後續的INSERT 操作將會失敗）。
分析▼
這個例子使用INSERT SELECT 從CustNew 將所有資料導入
Customers。 SELECT 語句從CustNew 檢索出要插入的值，而不是列出
它們。 SELECT 中所列的每一列對應於Customers 表名後面所跟的每一列。
這句語句將插入多少行呢？這依賴CustNew 表格有多少行。如果這個表
為空，則沒有行被插入（也不產生錯誤，因為操作仍然是合法的）。如果
這個表確實有數據，則所有數據將插入到Customers。

提示：INSERT SELECT 中的列名
為簡單起見，這個範例在INSERT 和SELECT 語句中使用了相同的欄位名稱。
但是，不一定要求列名符合。事實上，DBMS 一點也不關心SELECT
傳回的列名。它使用的是列的位置，因此SELECT 中的第一列（不管
其列名）將用來填入表格列中指定的第一列，第二列將用來填入表格列中
指定的第二列，如此等等。

INSERT SELECT 中SELECT 語句可以包含WHERE 子句，以過濾插入的資料。
提示：插入多行
INSERT 通常只會插入一行。若要插入多行，必須執行多個INSERT 語句。
INSERT SELECT 是例外，它可以用一條INSERT 插入多行，不管SELECT
語句傳回多少行，都會被INSERT 插入。
15.2 從一個表複製到另一個表
有一種資料插入不使用INSERT 語句。要將一個表格的內容複製到一個全
新的表（運行中建立的表），可以使用CREATE SELECT 語句（或在
SQL Server 裡也可用SELECT INTO 語句）。
說明：DB2 不支援
DB2 不支援這裡描述的CREATE SELECT。
與INSERT SELECT 將資料新增至已經存在的表不同，CREATE
SELECT 將資料複製到一個新表（有的DBMS 可以覆蓋已經存在的表，
這依賴於所使用的具體DBMS）。
以下的範例說明如何使用CREATE SELECT：

輸入▼
CREATE TABLE CustCopy AS SELECT * FROM Customers;
若是使用SQL Server，可以這麼寫：
輸入▼
SELECT * INTO CustCopy FROM Customers;

分析▼
這條SELECT 語句建立一個名為CustCopy 的新表，並把Customers 表
的整個內容複製到新表中。因為這裡使用的是SELECT *，所以會在
CustCopy 表中建立（並填入）與Customers 資料表的每一列相同的欄位。要
想只複製部分的列，可以明確給出列名，而不是使用*通配符。
在使用SELECT INTO 時，需要知道一些事情：
* 任何SELECT 選項和子句都可以使用，包括WHERE 和GROUP BY；
* 可利用聯結從多個表插入資料；
* 不管從多少個表中檢索數據，數據都只能插入到一個表中。
提示：進行表格的複製
SELECT INTO 是試驗新SQL 語句前進行表格複製的很好工具。先進行複
制，可在複製的資料上測試SQL 程式碼，而不會影響實際的資料。
說明：更多例子
如果想看INSERT 用法的更多例子，請參考附錄A 中給出的範例表填
充腳本。
15.3 小結
這一課介紹如何將行插入到資料庫表中。我們學習了使用INSERT 的幾
種方法，為什麼要明確使用列名，如何用INSERT SELECT 從其他表導
入行，如何用SELECT INTO 將行匯出到一個新表。下一課將講述如何使
用UPDATE 和DELETE 進一步操作表格資料。
