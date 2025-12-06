import time
import functools

def _format_time(seconds):
    """Helper to format time into human readable string."""
    if seconds < 1e-6:
        return f"{seconds * 1e9:.2f} ns"
    elif seconds < 1e-3:
        return f"{seconds * 1e6:.2f} µs"
    elif seconds < 1:
        return f"{seconds * 1e3:.2f} ms"
    else:
        return f"{seconds:.4f} s"

class monitor:
    """
    A dual-use timer: works as a decorator or context manager.
    """
    def __init__(self, func=None, label=None):
        self.func = func
        self.label = label
        self.start_time = None

    def __enter__(self):
        # Context manager entry
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Context manager exit
        elapsed = time.perf_counter() - self.start_time
        name = self.label if self.label else "Block"
        print(f"⏱️  [{name}] finished in {_format_time(elapsed)}")

    def __call__(self, *args, **kwargs):
        # Decorator logic
        if self.func is None:
            # This handles @monitor(label="My Label") usage
            self.func = args[0]
            return self
        
        @functools.wraps(self.func)
        def wrapper(*a, **kw):
            start = time.perf_counter()
            result = self.func(*a, **kw)
            elapsed = time.perf_counter() - start
            name = self.label if self.label else self.func.__name__
            print(f"⏱️  [{name}] finished in {_format_time(elapsed)}")
            return result
        return wrapper(*args, **kwargs)

# Allow using @monitor without parentheses
def timer(func=None, label=None):
    if func is None:
        return monitor(label=label)
    return monitor(func=func, label=label)(func)