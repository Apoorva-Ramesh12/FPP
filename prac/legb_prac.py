# def leap(year):
#      return True if ((year%4==0 and year%100!=0) or year%400==0) else False
# # def leapy(n):
# #      return 1 if n%400==0 else 0 if n%100==0 else 1 if n%4==0 else 0

# print(leap(2016))


# x=10  #Global scope
# def foo():
#      y=20    #Local scope
#      print(x)
#      print(y)

# foo()


# def outer():
#      z=30 #Enclosing scope
#      def inner():
#           print(z) #Accessing variables from the enclosing scope
#      inner()
# outer()


# x=10 #Global scope
# def outer():
#      y=21  #Enclosing scope
#      def inner():
#           z=30  #Local scope
#           print(x+y+z)  #Accessing variables from multiple scopes
#      inner()
# outer()


# x=10
# def outer():
#      x=20
#      def inner():
#           print(x)
#      inner()
# outer()

# print(abs(-5))

# def outer():
#     global x
#     x=20
    
#     def inner():
#         global x
#         x=30
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)
    