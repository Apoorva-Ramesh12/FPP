# class test:
#     def __iter__(self):
#         print("In iter")
#         return self
#     def __next__(self):
#         print("In next")
#         return 1
    
# x=test()
# print(iter(x))
# print(x.__next__())
# for i in test():
#     raise StopIteration

# class fibo:
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         c=self.a
#         self.b=self.b,self.a+self.b
#         return c

# fib = fibo()
# for i in range(10):
#     print(next(fib))


# class fibo:
#     def __init__(self,n):
#         self.n=n
#         self.count=0
#         self.a=0
#         self.b=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count>self.n:
#             raise StopIteration
#         temp=self.a
#         self.a,self.b=self.b,self.a+self.b
#         self.count+=1
#         return temp
    
# x=fibo(6)
# for i in x:
#     print(i)
    
