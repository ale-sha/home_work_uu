import sys

def introspection_info(obj):
    dict_info = {
    'тип объекта' : type(obj).__name__,
    'атрибуты' : [],
    'методы' : [],
    'модуль' : sys.path,
    'адрес интерпретатора' : sys.executable,
    'размер' : sys.getsizeof(obj),
    'имя объекта' : obj.__name__ if not isinstance(obj, (str, int, tuple, list)) else 'Нет имени'
    }
    for attr in dir(obj):
        if not callable(getattr(obj, attr)) and not attr.startswith('__'):
            dict_info['атрибуты'].append(attr)
        else:
            dict_info['методы'].append(attr)
    return dict_info

number_info = introspection_info(sys)
print(number_info)