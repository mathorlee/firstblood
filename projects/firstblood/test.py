
# def add_log(func):
#     '''
#     '''
#     
#     def wrapper(a, b):
#         print 'begin add'
#         return func(a, b)
#     return wrapper
# 
# def add(a, b):
#     return a + b
# 
# print add(1, 3)
# 
# add = add_log(add)
# 
# print add(1, 4)
from functools import wraps

def retry(times):
    def wrapper(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):
            for i in range(times):
                try:
                    func(*args, **kwargs)
                    print '%s succeed.' % i
                    break
                except:
                    print '%s failed.' % i
        return wrapper2
    return wrapper

@retry(3)
def log(name):
    '''
    printlog
    '''
    raise Exception()
    print 'hello %s!' % name

log('lisongsong')
