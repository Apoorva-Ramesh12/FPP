class menu:
    def __init__(self) :
        self.m={}
    def add(self,item):
        self.m[item[0]]=item[1]
        return self
    def show(self):
        print(self.m)
m = menu()
m.add("idly",100)
m.add("vada",200)
m.add("sambar",100)
m.add("dosa",150)