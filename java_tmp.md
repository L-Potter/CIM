import java.io.Serializable;

public class Person implements Serializable {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}


---

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class Client {
    public static void main(String[] args) throws IOException {
        // 創建一個 Person 物件
        Person person = new Person("Alice", 30);

        // 將 Person 物件序列化成位元組數組
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        ObjectOutputStream objectOutputStream = new ObjectOutputStream(byteArrayOutputStream);
        objectOutputStream.writeObject(person);
        objectOutputStream.close();

        byte[] data = byteArrayOutputStream.toByteArray();

        // 發送 HTTP 請求到 Servlet
        URL url = new URL("http://localhost:8080/YourServletURL");
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setDoOutput(true);
        connection.getOutputStream().write(data);

        // 讀取來自 Servlet 的響應（如果有）
        BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        reader.close();
    }
}

---

import java.io.*;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/YourServletURL")
public class YourServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 讀取客戶端傳遞過來的序列化資料
        ObjectInputStream objectInputStream = new ObjectInputStream(request.getInputStream());
        try {
            // 將序列化資料反序列化為 Person 物件
            Person person = (Person) objectInputStream.readObject();
            System.out.println("Received Person object: " + person.getName() + ", " + person.getAge());

            // 這裡可以對 Person 物件進行任何後續處理
            // 例如將其存儲到資料庫中或進行其他業務邏輯處理

            // 回傳一個回應給客戶端
            response.setContentType("text/plain");
            PrintWriter out = response.getWriter();
            out.println("Received Person object: " + person.getName() + ", " + person.getAge());
            out.close();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } finally {
            objectInputStream.close();
        }
    }
}
---
ByteArrayOutputStream 不是因為不同類型有不同的位元組長度，而是用於將數據寫入位元組數組中，以便在後續步驟中進行處理。

在上面的程式碼中，我們使用 ByteArrayOutputStream 來將序列化後的物件寫入位元組數組中，因為我們需要將它發送到 Servlet 端。ObjectOutputStream 將序列化後的物件寫入 ByteArrayOutputStream 中，然後我們可以通過調用 toByteArray 方法獲取這個位元組數組，進而將它發送到 Servlet 端。

簡而言之，ByteArrayOutputStream 的作用是提供一個位元組數組的輸出流，以便將數據寫入其中。

ObjectOutputStream 將序列化的位元組數據寫入到 ByteArrayOutputStream 中，因此序列化後的物件被存儲在記憶體中的位元組陣列中。這樣的設置通常用於將序列化後的物件傳輸到網路上的其他節點，或者在記憶體中進行臨時存儲，而不需要將其寫入到檔案系統中。

setContentType("application/octet-stream")：
這個設置告訴客戶端返回的內容是二進位數據流，但不指定具體的文件類型。