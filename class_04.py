class menu:
    def __init__(self) :
        self.m={}
    def __setitem__(self,itemname,itemprice):
        self.m[itemname]=itemprice
    def __getitem__(self,itemname):
        return self.m[itemname]
    def __iter__(self):
        return self
    def __next__(self):
        return self.m.items()
    def show(self):
        for i in m:
            print(i)
m = menu()
m["idly"]=10
m["vada"]=20
m.show()
# for i in m:
#     print(i)

   