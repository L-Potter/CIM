https://bugs.openjdk.org/browse/JDK-8187282
A survey on security-dev on its usage only revealed one user (IcedTea's PolicyEditor). Most users edit policy files as a `text file` directly and policytool does not really provide much additional function.
https://bugs.openjdk.org/browse/JDK-8173016
The `policytool` security tool is deprecated in JDK 9. It will be removed in a future release.

從java console看報出缺少哪些權限在添加至java.policy即可

Sun have changed the security behaviour of unsigned applets in 1.7.0_45 or 40.
They have now created and set a new deployment property:

deployment.security.use.user.home.java.policy=false
This means the user's .java.policy file is ignored by default.

either
A. Edit your deployment.properties and set the above property to true
The path for this is of the form: C:\Users\USERNAME\AppData\LocalLow\Sun\Java\Deployment\deployment.properties
Add a line like this anywhere in the file:

deployment.security.use.user.home.java.policy=true

or

B. Edit your JRE's central java.policy file and grant all permissions to your applet
The path for this is of the form: C:\Program Files (x86)\Java\jre7\lib\security\java.policy

HTH(hope this helps)!

---
Concept -> find  deployment.properties  -> add use.user.home.java.policy -> touch user's policy file -> open policytool

or 

find C:\Program Files (x86)\Java\jre7\lib\security\java.policy -> direct edit the file.


for TSMC odd Java Envirment,so Sad....
