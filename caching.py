import os
import pickle
from _md5 import md5


def dict_pickle_cached(namespace='sspr'):
    def decorator(fn):
        cache_dictionary = {}

        def decorated(*args, **kwargs):
            key = '{}.{}'.format(namespace, fn.__name__)
            for arg in args:
                key += '.{}'.format(arg)
            for k in sorted(kwargs.keys()):
                key += '.{}-{}'.format(k, kwargs[k])
            key = md5(key.encode()).hexdigest()
            cache_file_path = os.path.join('cache', namespace, key)
            if cache_file_path in cache_dictionary:
                return cache_dictionary[cache_file_path]
            if os.path.exists(cache_file_path):
                result = pickle.load(open(cache_file_path, mode='rb'))
                cache_dictionary[cache_file_path] = result
                return result
            else:
                result = fn(*args, **kwargs)
                os.makedirs(os.path.dirname(cache_file_path), exist_ok=True)
                pickle.dump(result, open(cache_file_path, mode='wb'))
                cache_dictionary[cache_file_path] = result
                return result

        return decorated

    return decorator
