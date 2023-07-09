# autoreload.py

_exception = [None, None]

def raise_last_exception():
    global _exception
    if _exception[1] is not None:
        raise _exception[1]

def check_errors(fn):
    global _exception
    try:
        fn()
    except Exception as e:
        _exception = [e, e.__traceback__]
        return True
    return False

def wrapper(fn, *args, **kwargs):
    if not check_errors(fn):
        return fn(*args, **kwargs)
    else:
        raise_last_exception()
