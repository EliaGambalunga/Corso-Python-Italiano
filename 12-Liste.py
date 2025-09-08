# la lista è una collezione di dati ordinata, modificabile e indicizzata. Permette duplicati.
# è la più flessibile tra le collezioni di dati
x =  ["milano", "roma", "napoli", "venezia"]
y = ["ciao", 9, 3.5, True] # una lista può contenere dati di tipi diversi

print [type(x)] # serve per vedere il tipo di dato contenuto nella variabile
print [len(x)] # serve per vedere la lunghezza della lista, cioè il numero di elementi che contiene
z = list(("a", "b", "c")) # si può creare una lista anche con la funzione list()
print(x(0)) # per accedere a un elemento della lista si usa l'indice tra parentesi quadre, che parte da 0
print(x(-1)) # per accedere all'ultimo elemento si può usare l'indice -1
print(x[1:3]) # per accedere a un intervallo di elementi 
