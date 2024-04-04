def fibo(n):
   fibo = [0,1]
   if n<=0:
       return []
   if n==1:
       return [0,]
   i=2;
   while((k:=fibo[i-1]+fibo[i-2])<n):
       fibo.append(k)
       i+=1
   return fibo
def fibo(n):
   fibo = [0,1]
   if n<=0:
       return []
   if n==1:
       return [0,]
   i=2;
   while((k:=fibo[i-1]+fibo[i-2])<n):
       fibo.append(k)
       i+=1
   return fibo
 
print(fibo(100))

