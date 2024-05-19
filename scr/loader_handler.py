__all__ = ['register', 'get_loader', 'get_names']
_loaders = {}


def register(name: str = 'nameless_loader'):
    def decorator(func):
        if not name:
            raise ValueError(f'Can not register loader. "{name}" is not valid loader name.')
        else:
            _loaders[name] = func
        return func
    return decorator


def get_loader(name: str):
    if not name:
        raise ValueError(f'Can not get loader. "{name}" is not valid loader name.')

    try:
        loader = _loaders[name]
    except KeyError:
        raise ValueError(f'Can not get loader. "{name}" not registered.')

    return loader


def get_names():
    return _loaders.keys()
