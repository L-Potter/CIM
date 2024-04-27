### Tomcat 
Tomcat 是一個開源的 Web 伺服器，它是 Apache 軟體基金會的一部分。Java Servlet 是 Java 語言的一部分，它是用於建立動態 Web 內容的技術。Tomcat 主要用於執行 Java Servlet，以及 Java Server Pages (JSP) 和其他 Java 技術，從而提供動態的 Web 內容。簡單來說，Tomcat 提供了一個執行 Java Servlet 的環境。

### Servlet
Servlet 是 Java 的類別，通常會被編譯成 .class 檔案，然後放在 Web 應用程式的 WAR (Web Application Archive) 檔案中。當部署 Web 應用程式到 Servlet 容器（如 Tomcat）時，容器會負責載入和執行這些 Servlet。所以，不需要將 Servlet 編譯成 JAR 檔案，只需將它們包含在 WAR 檔案中即可。

```Java
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/hello") //Java Servlet API Decorator 提供的注釋 @WebServlet，這是一種方便的方式來將 Servlet 映射到特定的 URL 上
public class MainServlet extends HttpServlet {

   @Override
   protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
       resp.setContentType("text/html");
       PrintWriter printWriter = resp.getWriter();
       printWriter.write("Hello!");
       printWriter.close();
   }
}
```

### WAR
WAR 檔案（Web Application Archive）是一種專門用於打包和部署 Java Web 應用程式的檔案格式。它可以包含 Servlet、JSP、HTML、JavaScript、CSS 等 Web 應用程式所需的所有檔案和資源。當您準備部署一個 Java Web 應用程式時，通常會將所有相關檔案打包成 WAR 檔案，然後部署到 Servlet 容器（如 Tomcat）中。


### JSP (Jinja)
JSP 檔案（JavaServer Pages）是一種用於建立動態 Web 內容的技術，它允許您在 HTML 中嵌入 Java 代碼。JSP 檔案通常包含 HTML 結構，並使用特殊的標籤（如 <% %> 和 <%= %>）嵌入 Java 代碼。當用戶訪問包含 JSP 檔案的網頁時，Servlet 容器會將 JSP 檔案編譯成 Java Servlet，然後執行它以生成動態的 HTML 內容。


### 負載平衡(Load Balance) 
* nginx
* openstack 


PATH: Java-Platform-Standard-Edition-8-Documentation-/docs/api/allclasses-noframe.html
* ObjectOutputStream
* ObjectInputStream
* FileInputStream
* ByteArrayOutputStream
* ByteArrayInputStream


### Serializable
在Java這樣支援物件導向的程式中撰寫程式，很多資料都是以物件的方式存在，在程式運行過後，您會希望將這些資料加以儲存，以供下次執行程式時使用，這時您可以使用ObjectInputStream、ObjectOutputStream來進行這項工作。

要被儲存的物件必須實作Serializable介面，說是實作，其實Serializable中並沒有規範任何必須實作的方法，所以這邊所謂實作的意義，其實像是對物件貼上一個標誌，代表該物件是可以序列化的（Serializable）。
```Java
import java.io.*;
public class Student implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private int score; 

    public Student() { 
        name = "N/A"; 
    } 

    public Student(String name, int score) { 
        this.name = name; 
        this.score = score; 
    } 

    public void setName(String name) {
        this.name = name;
    }
    
    public void setScore(int score) {
        this.score = score;
    }

    public String getName() { 
        return name; 
    } 

    public int getScore() { 
        return score; 
    } 

    public void showData() { 
        System.out.println("name: " + name); 
        System.out.println("score: " + score); 
    } 
} 
```
您要注意到serialVersionUID，這代表了可序列化物件的版本， 如果您沒有提供這個版本訊息，則會自動依類名稱、實現的介面、成員等訊息來產生，如果是自動產生的，則下次您更改了Student類，則自動產生的 serialVersionUID也會跟著變更，當反序列化時兩個serialVersionUID不相同的話，就會丟出 InvalidClassException，如果您想要維持版本訊息的一致，則要顯式宣告serialVersionUID。

ObjectInputStream、ObjectOutputStream為InputStream、OutputStream加上了可以讓使用者寫入 物件、讀出物件的功能，在寫入物件時，我們使用writeObject()方法，讀出物件時我們使用readObject()方法，被讀出的物件都是以 Object的型態傳回，您必須將之轉換為物件原來的型態，才能正確的操作被讀回的物件，下面這個程式示範了如何簡單的儲存物件至"檔案"中，並將之再度讀回 ：
```Java
import java.io.*;
import java.util.*;
 
public class ObjectStreamDemo {
    public static void writeObjectsToFile(Object[] objs, String filename) { 
        File file = new File(filename);
        try { 
            ObjectOutputStream objOutputStream = 
                new ObjectOutputStream(new FileOutputStream(file)); 
            for(Object obj : objs) {
                objOutputStream.writeObject(obj); 
            }
            objOutputStream.close(); 
        } 
        catch(IOException e) { 
            e.printStackTrace(); 
        }
    }
    
    public static Object[] readObjectsFromFile(String filename) throws FileNotFoundException {
        File file = new File(filename); 
        if(!file.exists()) 
            throw new FileNotFoundException(); 
        List list = new ArrayList();
        try {
            FileInputStream fileInputStream = new FileInputStream(file);
            ObjectInputStream objInputStream = new ObjectInputStream(fileInputStream); 
             
            while(fileInputStream.available() > 0) {
                list.add(objInputStream.readObject());
            }
            objInputStream.close(); 
        } 
        catch(ClassNotFoundException e) { 
            e.printStackTrace(); 
        } 
        catch(IOException e) { 
            e.printStackTrace(); 
        }
 
        return list.toArray();
    }
 
    public static void appendObjectsToFile(
                           Object[] objs, String filename) 
                               throws FileNotFoundException {
  
        File file = new File(filename); 
        
        if(!file.exists()) 
             throw new FileNotFoundException(); 

        try { 
            ObjectOutputStream objOutputStream = 
               new ObjectOutputStream(new FileOutputStream(file, true)) { 
                    protected void writeStreamHeader() 
                                     throws IOException {} 
               };  
            for(Object obj : objs) {
                objOutputStream.writeObject(obj); 
            }
            objOutputStream.close(); 
        } 
        catch(IOException e) { 
            e.printStackTrace(); 
        } 
    }
    
    public static void main(String[] args) {
        Student[] students = {new Student("caterpillar", 90),
                              new Student("justin", 85)}; 
        // 寫入新檔
        writeObjectsToFile(students, "data.dat");
        try {
            // 讀取檔案資料
            Object[] objs = readObjectsFromFile("data.dat");
            for(Object obj : objs) {
                ((Student) obj).showData();
            }
            System.out.println();
            
            students = new Student[2];
            students[0] = new Student("momor", 100);
            students[1] = new Student("becky", 100);
            // 附加至檔案
            appendObjectsToFile(students, "data.dat");
            // 讀取檔案資料
            objs = readObjectsFromFile("data.dat");
            for(Object obj : objs) {
                ((Student) obj).showData();
            }
        }
        catch(FileNotFoundException e) {
            e.printStackTrace();
        }
    }
} 
```
物件被寫出時，會寫入物件的類別型態、類別署名（Class signature），static與被標誌為transient的成員則不會被寫入。

在這邊注意到以附加的形式寫入資料至檔案時，在試圖將物件附加至一個先前已寫入物件的檔案時，由於ObjectOutputStream在 寫入資料時，還會加上一個特別的標示頭，而讀取檔案時會檢查這個標示頭，如果一個檔案中被多次附加物件，那麼該檔案中會有多個標示頭，如此讀取檢查時就會 發現不一致，這會丟出StreamCorrupedException，為此，您重新定義ObjectOutputStream的writeStreamHeader()方法，如果是以附加的方式來寫入物件，就不寫入標示頭：
```Java
ObjectOutputStream objOutputStream =
    new ObjectOutputStream(
        new FileOutputStream(file, true)) {
            protected void writeStreamHeader()
                                 throws IOException {}
        }; 
```

 
將物件寫出或讀入並不僅限於檔案存取，您也可以用於網路的資料傳送，例如傳送整個物件資料或是影像檔案。