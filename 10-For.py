lista_citta = ["milano", "roma", "napoli"]
for citta in lista_citta: # in pratica "per ogni citta in lista_citta" stampa citta
    print(citta)
stringa = "anguria" # per ogni lettera in stringa stampa lettera
for lettera in stringa:
    print(lettera)

for riga in range(6): # range(6) genera i numeri da 0 a 5
    for colonna in range (2 ): 
         print( "(" + str(riga) + ":" + str(colonna) + ")" )# stampa "Ciao!" 6 volte