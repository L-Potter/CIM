Decorator :  
[ retry decorator code on github](https://github.com/invl/retry)

一些常見的decorator寫法，跟概念
```python
def catch_errors(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except (CommandError, RuntimeError) as exc:
            log.error('Error: ' + str(exc))
            sys.exit(1)
    return wrapped


def decorator(func):
        @wraps(func)
        def validate_args(*args, **kwargs):
            input_values = kwargs
            for key, type in validations:
                try:
                    type.valid(input_values[key])
                except ArgumentFormat as e:
                    raise DashboardException(msg=e,
                                             code='type_not_valid',
                                             component=component)
            return func(*args, **kwargs)
        return validate_args

def allow_empty_body(func):  # noqa: N802
    """
    The POST/PUT request methods decorated with ``@allow_empty_body``
    are allowed to send empty request body.
    """
    # pylint: disable=protected-access
    try:
        func._cp_config['tools.json_in.force'] = False
    except (AttributeError, KeyError):
        func._cp_config = {'tools.json_in.force': False}
    return func

class Router(object):
    def __init__(self, path, base_url=None, security_scope=None, secure=True):
        # ... 初始化...

    def __call__(self, cls):
        # 在這裡，cls 代表被裝飾的類別
        cls._cp_config = True

        # ...
        return cls
```
class方式類似於工廠方法模式（Factory Method Pattern），它允許你根據不同的參數或條件來創建不同的物件實例。在你的程式碼中，Router 類別的 \_\_call__ 方法充當了一種工廠方法，根據不同的參數來設定被裝飾的類別的屬性，從而產生不同的物件。

allow_empty_body只對函式的屬性進行了修改，而且這個 decorator 並不會修改函式的名稱、參數或返回值。因此，它不需要使用 @wraps(func) 這樣的裝飾器來確保被裝飾的函式的元資料保持不變。

@wraps(func) 主要用於確保裝飾後的函式具有與原始函式相同的名稱、參數和文檔字符串。這在某些情況下很重要，特別是當你的 decorator 修改了函式的行為，但你仍希望保持函式的元資料不變時。

在 Python 中，"meta" 通常是指元資料（metadata），它是描述數據的數據。以下是一些常見的元資料類型和在 Python 中使用的地方：

* 類的屬性和方法： 在類中，屬性和方法都可以被視為元資料。例如，類的屬性可以包含有關類的描述信息，而方法的文檔字符串可以提供關於方法用途和使用方法的信息。

* 註解和註釋： 在代碼中，你可以使用註解來添加關於代碼功能、目的和使用的說明。這些註解可以被視為代碼的元資料，幫助其他人理解你的代碼。

* 文檔字符串（Docstrings）： 文檔字符串是寫在函式、方法、類等定義的下方，用於描述其功能和用法。這些文檔字符串是元資料，可以通過 help() 函式或 IDE 的提示功能來查看。

* 模組屬性和函式： 模組中的屬性和函式也可以被視為元資料。它們可以提供有關模組的信息以及如何使用其中的功能。

* 裝飾器： 裝飾器是 Python 中的元資料工具之一。它們可以用於修改函式或類的行為，添加額外的功能，並保持原始函式的元資料不變。

* 類和模組屬性： 你可以在類和模組中添加自定義的屬性，用於存儲有關類或模組的信息，例如版本號、作者、創建日期等。

總之，元資料是描述數據的數據，可以在代碼中的各個地方使用。它們有助於提供額外的信息、說明和功能，使代碼更具可讀性、可維護性和可理解性。

---
## inspect package
Python 的 inspect 模組可以用來檢查函式的元資料，包括文檔字符串、參數、返回值等。這個模組提供了多個函式和類別來幫助你檢查函式的屬性和元資料。

以下是一些常用的 inspect 模組函式：

* inspect.getdoc(object): 返回對象（例如函式、類別）的文檔字符串，即文檔註釋。如果沒有文檔字符串，則返回 None。

* inspect.signature(func): 返回函式的簽名對象，該對象包含有關函式參數的信息。

* inspect.getargspec(func): 此函式在 Python 3.5 之前的版本中可用，用於獲取函式的參數列表、默認值和可變參數信息。

* inspect.getfullargspec(func): 此函式取代了 getargspec，在 Python 3.5 之後的版本中使用，提供更多參數的信息，如默認值、可變參數、注解等。

* inspect.getmembers(object): 返回對象的成員列表，例如函式的方法、屬性等。

通過這些函式，你可以在運行時獲取函式的元資料，從而實現更動態和通用的代碼處理。這在創建通用函式、自動文檔生成等情況下非常有用。
