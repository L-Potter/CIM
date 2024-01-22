https://github.com/AdoptOpenJDK/IcedTea-Web

icetea-web/bin -> as follow batch file
* iweb-settings
* jawas
* policyeditor

first check: java -version
NO SE Runtime
set JAVA_HOME=icetea-web\openjdk8
set path=JAVA_HOME%\jre\bin;JAVA_HOME\bin;%path

java-version
openjdk version 
openjdk Runtime Environment


https://www.java.com/zh-TW/download/help/java_webstart_zh-tw.html

 
何謂 Java Web Start，以及啟動方式？
* Java Web Start 軟體允許您從 Web 下載並執行 Java 應用程式。Java Web Start 軟體：
* 提供輕鬆按一下即可啟動應用程式的功能
* 保證您執行的永遠是應用程式的最新版本
* 消除複雜的安裝或升級程序
取得 Java Web Start 軟體
自 Java 5.0 發行版本開始，Java Runtime Environment (JRE) 將包含 Java Web Start。這表示當您安裝 Java 時，將會自動安裝 Java Web Start。當第一次下載使用 Java Web Start 技術的 Java 應用程式時，會自動啟動 Java Web Start 軟體。Java Web Start 軟體會在您的電腦上本機快取 (儲存) 整個應用程式。這樣，由於所有需要的資源已經在本機可用，因此所有後續啟動幾乎會即刻執行。您每次啟動應用程式時，Java Web Start 軟體元件都會檢查應用程式的網站，查看是否有可用的新版本；如果有，將會自動下載並啟動該新版本。

從 Java 應用程式快取檢視器
Java Web Start 還提供可從「Java 控制面板」啟動的「應用程式快取檢視器」。快取檢視器可讓您直接啟動已下載的應用程式。

從桌面圖示
如果您經常使用某個應用程式，則可在桌面或「開始」功能表中建立捷徑。Java Web Start 可能會詢問您是否要在「開始」功能表中建立捷徑或項目。如果您回答「是」，以後不使用瀏覽器即可啟動應用程式。

從命令提示字元
您也可以鍵入 javaws jnlp_url (其中 jnlp_url是應用程式 jnlp 檔案的 URL)，從命令提示字元啟動應用程式。
移至開始 > 執行 > 鍵入 command
就會顯示命令提示字元視窗。
鍵入 javaws url_of_jnlp


iweb-settings:
https://manpages.ubuntu.com/manpages/jammy/man1/itweb-settings.1.html

itweb-settings - view and modify settings for javaws and the browser plugin
itweb-settings is a command line and a GUI program to modify and edit settings used by the
       IcedTea-Web implementation of javaws and the browser plugin

       If executed without any arguments, it starts up a GUI. Otherwise, it tries to do  what  is
       specified in the argument.

       The  command-line  allows  quickly  searching,  making  a  copy  of and modifying specific
       settings without having to hunt through a UI.

JNLP（Java Network Launch Protocol）：
JNLP 是一种 XML 文件格式，用于定义 Java Web Start 应用程序的启动和配置信息。它允许通过网络自动下载和启动 Java 应用程序，提供了一种机制，使用户能够从浏览器或桌面启动远程托管的 Java 应用程序。
JNLP 文件描述了应用程序的资源、代码库、启动参数等信息。当用户点击包含 JNLP 链接的网页链接时，浏览器会启动 Java Web Start（如果已安装），并使用 JNLP 文件指导如何下载和启动应用程序。
Java Web Start（JAWS）：
Java Web Start 是一种技术，允许通过网络启动、下载和管理 Java 应用程序。它使用 JNLP 文件来描述应用程序的配置，并提供了一种从远程服务器获取 Java 应用程序并在本地执行的机制。

debugging建議開啟 & java console show on startup


policy setting:


policyeditor
                   Show the GUI editor with no file opened.

policyeditor -file $XDG_CONFIG_HOME/icedtea-web/security/java.policy
                   Show GUI and opens the default policy file.

-defaultfile
                   Specifies that the default user-level policy file should be  opened.  This  is
                   the  file which is normally used by IcedTea-Web to make decisions about custom
                   policies  and  permissions  for  applets   at   runtime,   unless   configured
                   otherwise.(No argument expected)

-file policy_file
                   Specifies a policy file path to open. If exactly one argument is given, and it
                   is not this flag, it is interpreted as a file path to open, as  if  this  flag
                   was  given  first.  This  flag  exists  mostly  for  compatibility with Policy
                   Tool.(Exactly one argument expected)

policyeditor  is a GUI application with small command line support to view and edit applet
security policy settings used by the IcedTea-Web implementation of javaws and the  browser
plugin.   It  is  intended as a simpler, easier to use, and more accessible alternative to
the standard JDK Policy Tool.  Administrators  and  power  users  who  need  fine  grained
control over policy files should probably use Policy Tool instead of PolicyEditor.