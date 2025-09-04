x = ["milano", "roma", "napoli"]
i = 0
while i < 6: #finché i è minore di 6 esegue questo blocco di codice
    print(i) #stampa il valore di i
    i +=1 #incrementa i di 1
print("fine ciclo") #finché i è minore di 6 esegue questo blocco di codice

i = 0
while i < 6:
    print(i)
    if i == 3: #break interrompe il ciclo quando i raggiunge il valore di 3 
        break
    i +=1 #break interrompe il ciclo quando i raggiunge il valore di 3 quindi il valore di i non viene incrementato
print("fine ciclo")

i = 0
while i < 6:
    i +=1
    if i == 3: #continue salta il valore di 3 e continua il ciclo
        continue
    print(i) #stampa il valore di i
print("fine ciclo")

i = 0
while i < 6:
    i +=1
else: #else viene eseguito quando la condizione del while diventa falsa
    print("i non è più minore di 6")