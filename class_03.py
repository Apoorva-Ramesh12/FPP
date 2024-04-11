class menu:
    def __init__(self) :
        self.m={}
    def __setitem__(self,itemname,itemprice):
        self.m[itemname]=itemprice
    def __getitem__(self,itemname):
        return self.m[itemname]
    def show(self):
        print(self.m)
m = menu()
m["idly"]=10
m["vada"]=20
m.show()