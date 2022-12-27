ok=True
while ok:
    n=int(input("donner la taille de tableu :"))
    if 2<=n<=10:
        ok=False
alpha=["A","Z","E","R","T","Y","U","I","O","P","K","M","L","J","H","G","F","D","S","Q","W","X","C","V","B","N"]

from numpy import *
t=array([(str)]*20)

for i in range(n):
    a=True
    j=0
    while a:
        t[i]=input("t["+str(i)+"]=")
        # i need make codition: the first and the last catracter in the strings of the table is upper 
        if  (len(t[i])!=0) and t[i][j] in alpha  and t[i][len(t[i])] in alpha:
            j+=j+1
            a=False 

