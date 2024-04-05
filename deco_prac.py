# def decorator_func(func):
#     def wrapper_func():
#         print("Wrapper executed this").format(func.__name__)
#         return func
#     return wrapper_func
# @decorator_func
# def display():
#     print("Display function executed")
# print(display())

def decorator_func(func):
    def wrapper_func(*args,**kwargs):
        print("Wrapper executed this").format(func.__name__)
        return func(*args,**kwargs)
    return wrapper_func
@decorator_func
def display(name,age):
    print("Display function executed")
display("Apoorva",19)