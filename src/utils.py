from typing import Any


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

        
class SingletonSymbol(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        name = args[0]
        if name not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[name] = instance
        return cls._instances[name]