import functools

from .middleware import _thread_local

def disable_subdomain_middleware(fn):
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        prev = getattr(_thread_local, 'enabled', True)

        try:
            _thread_local.enabled = False
            return fn(*args, **kwargs)
        finally:
            _thread_local.enabled = prev

    return wrapped
