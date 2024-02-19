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

---

@echo off

set "input_file=test.txt"
set "search_string=deployment.security.use.user.home.java.policy="
set "replacement_string=deployment.security.use.user.home.java.policy=True"

powershell -Command "(Get-Content %input_file%) -replace '(?m)^(%search_string%)', '%replacement_string%' | Set-Content %input_file%"

if %errorlevel% neq 0 (
    echo %search_string% not found, adding new line.
    echo %replacement_string% >> %input_file%
)

exit /b



echo. > filename


```
Synopsis
policytool [ -file ] [ filename ]

-file
Directs the policytool command to load a policy file.

filename
The name of the file to be loaded.

Examples:

Run the policy tool administrator utility:

policytool
Run the policytool command and load the specified file:

policytool -file mypolicyfile



Touch
NAME         top
       touch - change file timestamps
SYNOPSIS         top
       touch [OPTION]... FILE...
DESCRIPTION         top
       Update the access and modification times of each FILE to the
       current time.

       A FILE argument that does not exist is created empty, unless -c
       or -h is supplied.

       A FILE argument string of - is handled specially and causes touch
       to change the times of the file associated with standard output.

       Mandatory arguments to long options are mandatory for short
       options too.

       -a     change only the access time

       -c, --no-create
              do not create any files

       -d, --date=STRING
              parse STRING and use it instead of current time

       -f     (ignored)

       -h, --no-dereference
              affect each symbolic link instead of any referenced file
              (useful only on systems that can change the timestamps of
              a symlink)

       -m     change only the modification time

       -r, --reference=FILE
              use this file's times instead of current time

       -t STAMP
              use [[CC]YY]MMDDhhmm[.ss] instead of current time

       --time=WORD
              change the specified time: WORD is access, atime, or use:
              equivalent to -a WORD is modify or mtime: equivalent to -m

       --help display this help and exit

       --version
              output version information and exit

       Note that the -d and -t options accept different time-date
       formats.
```