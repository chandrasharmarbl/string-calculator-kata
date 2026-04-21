from functools import update_wrapper
import types

class CountCalls:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
        self._counts = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return types.MethodType(self, instance)

    def __call__(self, instance, *args, **kwargs):
        self._counts[instance] = self._counts.get(instance, 0) + 1
        return self.func(instance, *args, **kwargs)

    def get_count(self, instance):
        return self._counts.get(instance, 0)