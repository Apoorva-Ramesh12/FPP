def leap(year):
     return True if ((year%4==0 and year%100!=0) or year%400==0) else False
# def leapy(n):
#      return 1 if n%400==0 else 0 if n%100==0 else 1 if n%4==0 else 0

print(leap(2016))