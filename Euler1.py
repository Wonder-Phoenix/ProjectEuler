#Euler 1

x = 0
borne = 1000
somme = 0

while x < borne :
    somme += x
    x+=3
x = 0
while x < borne :
    if x%3!=0 :
        somme += x
    x+=5
    
print (somme)
