# Python Subprocess  & asyncio

Type: asyncio, python, subprocess
Created By: 建忠林

## RUN

[subprocess - Subprocess management - Python 3.11.0 documentation](https://docs.python.org/zh-tw/3/library/subprocess.html)

On Linux, subprocess defaults to using the vfork() system call internally when it is safe to do so rather than fork(). This greatly improves performance.

[vfork(2) - Linux manual page](https://man7.org/linux/man-pages/man2/vfork.2.html)

the parent remaining blocked until the child either terminates or calls execve

## Python Source Code

```python
# /usr/lib/python/subprocess.py
with Popen(*popenargs, **kwargs) as process:
        try:
            stdout, stderr = process.communicate(input, timeout=timeout)
```

### def communicate(self, input=None, timeout=None):

![Untitled](Python%20Subprocess%20&%20asyncio%206e14d9dc3ad14b579a1d68e0fe8ab590/Untitled.png)

[wait(2) - Linux manual page](https://man7.org/linux/man-pages/man2/wait.2.html)

```
wait(NULL) will block the parent process until any of its children has finished. If the child terminates before the parent process reaches wait(NULL) then the child process turns to a zombie process until its parent waits on it and its released from memory.

If the parent process doesn't wait for its child, and the parent finishes first, then the child process becomes an orphan and is assigned to init as its child. And init will wait and release the process entry in the process table.

In other words: the parent process will be blocked until the child process returns an exit status to the operating system which is then returned to the parent process. If the child finishes before the parent reaches wait(NULL) then it will read the exit status, release the process entry in the process table and continue execution until it finishes as well.
```

## Run 流程圖(POSIX VERSION)

![Untitled](Python%20Subprocess%20&%20asyncio%206e14d9dc3ad14b579a1d68e0fe8ab590/Untitled%201.png)

解釋:

run 其實是一個大封裝(先呼叫了Popen在call communicate)

popen (去呼叫vfork & execve)來產生一個新的process並執行execve(system call)

[execve(2) - Linux manual page](https://man7.org/linux/man-pages/man2/execve.2.html)

pathname must be either a binary executable, or a script

python是可以使用script方式去啟動或是execute python(binary executale)，我個人是不會再帶入shell=True.

communicate可以上面的得知會block parent process.

# Q: 有沒有更有效率的去呼叫多個python script

想法流程圖: 不要再call communicate時候block parent process.

![Untitled](Python%20Subprocess%20&%20asyncio%206e14d9dc3ad14b579a1d68e0fe8ab590/Untitled%202.png)

# A: 有，ASYNCIO

python asyncio.process *sample code*

[Subprocesses - Python 3.11.0 documentation](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.wait)

[Subprocesses - Python 3.11.0 documentation](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.wait)

```python
async def communicate(self, input=None):
				...
        await self.wait()
        return (stdout, stderr)
```

the Process.wait() method is asynchronous, whereas subprocess.Popen.wait() method is implemented as a blocking busy loop.

基於預設python compiler ( cpython ) 會有GIL問題會導致實際為不停地content switch，但是用於IO bound問題還是很有效率且好懂Code.

BTW. 如果使用exec 去執行是其他的腳本 e.g. another python script會有另一個python process 就沒有GIL問題，但是要考慮資源共享、效能等問題.