def isleap(year):
     match year%4:
         case 0 if year%100!=0 or year%400==0:
             return True
         case _:
             return False
         
print(isleap(2016))