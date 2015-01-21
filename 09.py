# Реализовать фабрику декораторов, инициализируемую с натуральным числом n,
# умножающие результат функции на n если операция применима, иначе возвращающих None.

# Фабрика
def multiple(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            try:
                return res*n
            except:
                return None
        return wrapper
    return decorator


#DEMO
@multiple(3)
def pack_to_list(a,b):
    return {'a':a, 'b':b}

@multiple(4)
def nothing_useful(n):
    return n

print(pack_to_list(1,4))
print(nothing_useful(2))