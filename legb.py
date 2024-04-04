n = 9
def legb(func):
    n = 10
    def wrapped():
        print(n)
        print(print)
        func()
    return wrapped
@legb
def sdf():
    print("Bye")
sdf()
def legnb():
    z= 10
    def wrappedd():
        print(z)
        print(print)
    return wrappedd
x= legnb()
x()