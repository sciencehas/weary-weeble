```python
import threading

class DjangoMainThread(threading.Thread):
    def __init__(self, target, args=(), kwargs={}):
        threading.Thread.__init__(self)
        self._target = target
        self._args = args
        self._kwargs = kwargs

    def run(self):
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        except Exception as e:
            print(f"Exception in thread {self.name}:\n{e}")

    def bootstrap_inner(self):
        try:
            self.run()
        except:
            raise

if __name__ == "__main__":
    # Example usage
    def print_hello():
        print("Hello, world!")

    thread = DjangoMainThread(target=print_hello)
    thread.start()
```