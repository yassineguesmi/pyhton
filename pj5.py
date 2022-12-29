#cette programme permat de inverser les chaine inclu dans le tableua t et stocké la dans le tableu ch1
#donner la taille de tableu t
ok=True
while ok:
    n=int(input("donner la taille de tableu :"))
    if 3<n<10:
        ok=False
#définié les tableu nécisaire
from numpy import *
t=array([(str)]*100)
ch1=array([(str)]*100)
#dremplacage la tableu t
for i in range(n):
    a=True
    while a:
        t[i]=input("t["+str(i)+"]=")
        if len(t[i])<10:
            a=False
#afficher le tableu t
for i in range(n):
    print(t[i],end="||")
#inverser les chaines de t et stoké dans ch1
for i in range(n):
    ch1[i]=""
    for j in range(len(t[i])):
        ch1[i]=ch1[i]+t[i][-(j+1)]
#afficher ch1
for i in range(n):
    print(ch1[i],end="||")
