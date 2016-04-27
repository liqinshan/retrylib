# retry
一个Python装饰器，用于需要重试操作的场合。可以自定义重试次数，以及异常类型。

### Installation

执行命令：

`pip install git+https://github.com/davechina/retrylib.git`

### Example

```python
from retry import retry

@retry(max_retries=3, exceptions=(OSError, IOError), logger=None)
def test():
    pass
```



