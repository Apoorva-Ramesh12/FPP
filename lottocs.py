lot = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h')]
def lottocs(lot):
     cs=""
     for i in lot:
         cs +="=".join(i)+";"
     return cs.strip(';')
print(lottocs(lot))

