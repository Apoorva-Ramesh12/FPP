# print(type(type))
# class a:
#     pass
# print(type(a))
# print(dir(type))
# print(type)
# class a:
#     pass
# x=a()
# print(x)
# print(dir(x))
# x.__class__
# x.__class__.__class__
# x.__dict__


# class x:
#     def __init__(self):
#         self.n=10

# class x:
#     def __init__(self):
#         self.n=10
# print(x)
# a=x()
# print(a.n)

class menu:
    def __init__(self) :
        self.m={}
    def __add__(self,item):
        self.m[item[0]]=item[1]
        return self
    def __setitem__(self,itemname,itemprice):
        self.m[itemname]=itemprice
    def __getitem__(self,itemname):
        return self.m[itemname]
    def show(self):
        print(self.m)
m = menu()
# m.add("idly",100)
# m.add("vada",200)
# m.add("sambar",100)
# m.add("dosa",150)
#m+("aloo bun",10)+("cream bun",20)+("dosa",30)+("idly",40)
m["vada"]=20
m.show()







    

