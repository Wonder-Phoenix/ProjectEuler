#Euler 8

file = open("/Users/sophiemelique/Desktop/Euler8.txt")
chiffres = file.read()

chiffres = chiffres.replace("\n", "")

debut = 0
fin = 13
borne = len(chiffres)

def produit13(nb):
    produit = 1
    for c in nb:
        produit = produit*int(c)
    return produit

maxProduit = 0

while fin < borne :
    produit = produit13(chiffres[debut:fin])
    if maxProduit < produit:
        maxProduit = produit
    debut +=1
    fin +=1

print (maxProduit)
