class menu:
    def __init__(self) :
        self.m={}
    def __add__(self,item):
        self.m[item[0]]=item[1]
        return self
    def show(self):
        print(self.m)
m = menu()
m+("aloo bun",10)+("cream bun",20)+("dosa",30)+("idly",40)
m.show()