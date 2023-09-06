class NotificationQueue(threading.Thread):  # 繼承自 threading.Thread 的類別是一個多執行緒的類別
    _ALL_TYPES_ = '__ALL__'
    _listeners = collections.defaultdict(set)  # type: DefaultDict[str, Set[Tuple[int, Callable]]] 用來存儲不同類型的通知的監聽器（listeners）這個變數的型別註解顯示它是一個字典，鍵是字串，值是集合（set），每個集合中包含了一組（Tuple）的整數和可調用物件（Callable）。
    _lock = threading.Lock()
    _cond = threading.Condition() # 條件變數（Condition），通常用於等待和通知條件的變化。self._cond.wait(release _cond key & wait) & self._cond.notify(通知等待called wait的執行緒將會被喚醒並繼續執行)
    _queue = collections.deque()  # type: Deque[Tuple[str, Any]] 
    _running = False  #表示通知佇列是否正在運行。
    _instance = None  # 用於start_queue保存 NotificationQueue 類別的唯一實例（Singleton 模式）
    # Singleton確保多個執行緒或部分程式碼都能夠訪問到同一個唯一實例，以確保資源的一致性和避免競爭條件的發生。在這個情況下，確保只有一個通知佇列實例是很重要的

    def __init__(self):
        super(NotificationQueue, self).__init__()  #super().__init__() 初始化多執行緒

    @classmethod
    def start_queue(cls):
        with cls._lock: # _lock 用於確保這個操作是線程安全的 with表示離開會自動釋放_lock key
            if cls._instance:
                # the queue thread is already running
                return
            cls._running = True
            cls._instance = NotificationQueue()  # 創建一個 NotificationQueue 實例
        cls.logger = logging.getLogger('notification_queue')  # type: ignore
        cls.logger.debug("starting notification queue")  # type: ignore
        cls._instance.start()  # 啟動這個實例的執行緒。https://docs.python.org/3/library/threading.html#threading.Thread.start 概念是threading.Thread(target=my_function)建構子(constructor) 對應一個thread, start表示trigger thread run 對應的target func & or def run 

@classmethod  #類別方法（classmethod），所以它可以由類別本身調用，而不需要實例化 NotificationQueue。
    def stop(cls):
        with cls._lock: # 操作是線程安全
            if not cls._instance:
                # the queue thread was not started
                return # 所以不需要執行停止操作
            instance = cls._instance
            cls._instance = None # 表示通知佇列的執行緒將被停止
            cls._running = False # 表示通知佇列的執行緒將被停止
        with cls._cond:  # 獲取 _cond 條件變數的鎖，這是一個標準的多執行緒同步機制，用於等待執行緒之間的通信
            cls._cond.notify()  # 通知佇列的執行緒在收到通知後能夠正確地停止
        cls.logger.debug("waiting for notification queue to finish")  # type: ignore
        instance.join()  # 等待通知佇列的執行緒執行完成。這個方法會__阻塞__直到執行緒結束運行。
        cls.logger.debug("notification queue stopped")  # type: ignore

 @classmethod
    def _registered_handler(cls, func, n_types):     #  檢查是否已經註冊了相同的事件監聽器（使用 _registered_handler 方法檢查）
        for _, reg_func in cls._listeners[n_types]:  #  _listeners 字典中key為 n_types 的對應value: 值是集合（set），每個集合中包含了一組（Tuple）的整數和可調用物件（Callable）
            if reg_func == func:
                return True
        return False

 @classmethod
    def register(cls, func, n_types=None, priority=1):   # 事件監聽器（listener）的，讓它們能夠接收特定類型的通知。
        """Registers function to listen for notifications

        If the second parameter `n_types` is omitted, the function in `func`
        parameter will be called for any type of notifications.

        Args:
            func (function): python function ex: def foo(val) 您希望註冊的事件監聽器，當特定類型的通知到達時，該函數將被調用。
            n_types (str|list): the single type to listen, or a list of types  要註冊的事件類型。如果不提供此參數，則該事件監聽器將被註冊為接收任何類型的通知。可以是一個字符串（表示單個事件類型）或一個事件類型的列表（表示多個事件類型）。
            priority (int): the priority level (1=max, +inf=min) 默認值為1，表示最高優先級
        """
        with cls._lock:
            if not n_types:
                n_types = [cls._ALL_TYPES_]
            elif isinstance(n_types, str):
                n_types = [n_types]
            elif not isinstance(n_types, list):
                raise Exception("n_types param is neither a string nor a list")
            for ev_type in n_types:
                if not cls._registered_handler(func, ev_type):
                    cls._listeners[ev_type].add((priority, func))
                    cls.logger.debug(  # type: ignore
                        "function %s was registered for events of type %s",
                        func, ev_type
                    )

    
    @classmethod
    def deregister(cls, func, n_types=None):
        # type: (Callable, Union[str, list, None]) -> None
        """Removes the listener function from this notification queue

        If the second parameter `n_types` is omitted, the function is removed
        from all event types, otherwise the function is removed only for the
        specified event types.

        Args:
            func (function): python function
            n_types (str|list): the single event type, or a list of event types
        """
        with cls._lock:
            if not n_types:
                n_types = list(cls._listeners.keys())
            elif isinstance(n_types, str):
                n_types = [n_types]
            elif not isinstance(n_types, list):
                raise Exception("n_types param is neither a string nor a list")
            for ev_type in n_types:
                listeners = cls._listeners[ev_type]
                to_remove = None
                for pr, fn in listeners:
                    if fn == func:  # python bound method(instancemethod) 把class instance傳入都是特定位置 故不同task register同一個func, n_types還是會通知，並在deregister不會砍錯，在task _complete呼叫_handle_task_finished callback func( deregister + )
                        to_remove = (pr, fn)
                        break
                if to_remove:
                    listeners.discard(to_remove)  # discard python remove set item
                    cls.logger.debug(  # type: ignore
                        "function %s was deregistered for events of type %s",
                        func, ev_type
                    )

    
    @classmethod
    def new_notification(cls, notify_type, notify_value):   # notify_type 是通知的類型，是一個字串; notify_value 是通知的值，可以是任何類型。
        # type: (str, Any) -> None
        with cls._cond:  # 確保多執行緒環境下的同步
            cls._queue.append((notify_type, notify_value)) # python thread safe data structure. 這確保了多個執行緒可以將通知添加到 _queue 中，而不會出現競爭條件或其他線程同時修改 _queue 的問題。
            cls._cond.notify()  # 通知等待中的執行緒，告知它們有新的通知可用。

    @classmethod
    def _notify_listeners(cls, events):
        for ev in events:
            notify_type, notify_value = ev   # events 是一個事件列表，每個事件是一對 (notify_type, notify_value)，表示事件類型和值。
            with cls._lock:
                listeners = list(cls._listeners[notify_type])     # 獲取相關事件類型的監聽器列表，包括特定事件類型的監聽器和
                listeners.extend(cls._listeners[cls._ALL_TYPES_]) # 通用（ALL_TYPES）事件類型的監聽器。
            listeners.sort(key=lambda lis: lis[0])                # 將這些監聽器列表合併，並根據其優先級排序。
            for listener in listeners:
                listener[1](notify_value)   # 並調用每個監聽器的函數callable部分（listener[1]），將通知值 notify_value 傳遞給它們。


     def run(self):
        self.logger.debug("notification queue started")  # type: ignore
        while self._running:
            private_buffer = []   # 創建一個空列表 private_buffer，用於存儲要處理的事件。
            self.logger.debug("processing queue: %s", len(self._queue))  # type: ignore
            try:
                while True:
                    private_buffer.append(self._queue.popleft())   # 進入無限循環，不斷從 _queue 中取出事件，直到 _queue 為空。
            except IndexError:
                pass
            self._notify_listeners(private_buffer)   # 當 _queue 為空時，捕獲 IndexError 錯誤
            with self._cond:   # 這是另一個循環，它在 _running 為 True 且 _queue 為空的情況下等待。這表示當 _queue 為空時，執行緒將被阻塞，直到有新的事件添加到 _queue 中對應new_notification 的 cls._cond.notify() 
                while self._running and not self._queue:
                    self._cond.wait()
        # flush remaining events
        self.logger.debug("flush remaining events: %s", len(self._queue))  # type: ignore
        self._notify_listeners(self._queue)
        self._queue.clear()
        self.logger.debug("notification queue finished")  # type: ignore

# 以上為complete task被new_notification append to self._queue，表示完成，並會在之前使用register定義如何從self._queue exec要如何動作callable object in _listeners.



class TaskExecutor(object):
    def __init__(self):
        self.logger = logging.getLogger('taskexec')
        self.task = None

    def init(self, task):
        self.task = task  # 建立 TaskExecutor 實例時，可以將一個 task 物件傳遞給它，以便 TaskExecutor 實例可以與特定的 task 關聯起來

    def start(self):
        self.logger.debug("executing task %s", self.task)
        try:
            self.task.fn(*self.task.fn_args, **self.task.fn_kwargs)  #  task object classmethod 
        except Exception as ex:
            self.logger.exception("Error while calling %s", self.task)
            self.finish(None, ex)

    def finish(self, ret_value, exception):
        if not exception:
            self.logger.debug("successfully finished task: %s", self.task)
        else:
            self.logger.debug("task finished with exception: %s", self.task)
        self.task._complete(ret_value, exception)  # task object classmethod 

# 執行序方式去執行 -> threading.thread(target=fn)
class ThreadedExecutor(TaskExecutor):
    def __init__(self):
        super(ThreadedExecutor, self).__init__()  # 建立 TaskExecutor 實例時，可以將一個 task 物件傳遞給它，以便 TaskExecutor 實例可以與特定的 task 關聯起來
        self._thread = threading.Thread(target=self._run) # thread start要執行callable func

    def start(self):
        self._thread.start()    #   threading package's start method

    # pylint: disable=broad-except
    def _run(self):
        TaskManager._task_local_data.task = self.task
        try:
            self.logger.debug("executing task %s", self.task)
            val = self.task.fn(*self.task.fn_args, **self.task.fn_kwargs)  # 執行task object's func
        except Exception as ex:
            self.logger.exception("Error while calling %s", self.task)
            self.finish(None, ex) # TaskExecutor's method
        else:
            self.finish(val, None) # TaskExecutor's method


class Task(object):
    def __init__(self, name, metadata, fn, args, kwargs, executor,
                 exception_handler=None):
        self.name = name
        self.metadata = metadata
        self.fn = fn
        self.fn_args = args
        self.fn_kwargs = kwargs
        self.executor = executor
        self.ex_handler = exception_handler
        self.running = False
        self.event = threading.Event()
        self.progress = None
        self.ret_value = None
        self._begin_time: Optional[float] = None
        self._end_time: Optional[float] = None
        self.duration = 0.0
        self.exception = None
        self.logger = logging.getLogger('task')
        self.lock = threading.Lock()

    def __hash__(self):
        return hash((self.name, tuple(sorted(self.metadata.items()))))      # 用於判斷是否有相同API被呼叫

    def __eq__(self, other):
        return self.name == other.name and self.metadata == other.metadata

    def __str__(self):
        return "Task(ns={}, md={})" \
               .format(self.name, self.metadata)

    def __repr__(self):
        return str(self)

    def _run(self): # 註冊callback func _handle_task_finished & type is cd_task_finished & pri = 100, by def register(cls, func, n_types=None, priority=1): 
        NotificationQueue.register(self._handle_task_finished, 'cd_task_finished', 100)  # NotificationQueue
        with self.lock:
            assert not self.running  # assert true == pass
            self.executor.init(self) # create the thread which be used as a executor 
            self.set_progress(0, in_lock=True)
            self._begin_time = time.time()
            self.running = True
        self.executor.start() # thread start : try self.task.fn -> self.task._complete

    def _complete(self, ret_value, exception=None):
        now = time.time()
        if exception and self.ex_handler:   # 當try self.task.fn except catch some error, 
            # pylint: disable=broad-except
            try:
                ret_value = self.ex_handler(exception, task=self)  # task 可以init 時候帶入對應的exception
            except Exception as ex:
                exception = ex
        with self.lock:
            assert self.running, "_complete cannot be called before _run"
            self._end_time = now
            self.ret_value = ret_value
            self.exception = exception
            self.duration = now - self.begin_time
            if not self.exception:
                self.set_progress(100, True)
        NotificationQueue.new_notification('cd_task_finished', self) # new_notification(cls, notify_type, notify_value): listener[1](notify_value) -> self._handle_task_finished(task) 故帶入Self作為parameter.
        self.logger.debug("execution of %s finished in: %s s", self,
                          self.duration)

    def _handle_task_finished(self, task):
        if self == task:
            NotificationQueue.deregister(self._handle_task_finished) # cls._listeners 移除
            self.event.set()

    def wait(self, timeout=None):
        with self.lock:
            assert self.running, "wait cannot be called before _run"
            ev = self.event

        success = ev.wait(timeout=timeout)
        with self.lock:
            if success:
                # the action executed within the timeout
                if self.exception:
                    # pylint: disable=raising-bad-type
                    # execution raised an exception
                    raise self.exception
                return TaskManager.VALUE_DONE, self.ret_value
            # the action is still executing
            return TaskManager.VALUE_EXECUTING, None

    def inc_progress(self, delta, in_lock=False):
        if not isinstance(delta, int) or delta < 0:
            raise Exception("Progress delta value must be a positive integer")
        if not in_lock:
            self.lock.acquire()
        prog = self.progress + delta  # type: ignore
        self.progress = prog if prog <= 100 else 100
        if not in_lock:
            self.lock.release()

    def set_progress(self, percentage, in_lock=False):
        if not isinstance(percentage, int) or percentage < 0 or percentage > 100:
            raise Exception("Progress value must be in percentage "
                            "(0 <= percentage <= 100)")
        if not in_lock:
            self.lock.acquire()
        self.progress = percentage
        if not in_lock:
            self.lock.release()

    @property
    def end_time(self) -> float:
        assert self._end_time is not None
        return self._end_time

    @property
    def begin_time(self) -> float:
        assert self._begin_time is not None
        return self._begin_time
