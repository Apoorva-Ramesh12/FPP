def cstodict(cs):
     dict = {}
     for i in cs.split(';'):
         key,value = i.split('=')
         dict[key]=value
     return dict
 
cs = "a=b;c=d;e=f;g=h"
cstodict(cs)

