#Euler 13

file = open("/Users/sophiemelique/Desktop/Euler13.txt")
chiffres = file.read()

listeChiffres = chiffres.split("\n")

somme = 0
for nb in listeChiffres :
    somme += int(nb)
    
sommeStr=str(somme)
print (somme)
print (sommeStr[:10])
