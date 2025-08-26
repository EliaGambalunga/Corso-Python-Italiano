x = 5
if x < 10:
     print("5 è minore di 10") # se la condizione è vera esegue questo blocco di codice che in questo caso è una sola stringa
     #finché l'indentazione è valida fa parte del blocco di codice quindi se ci sono più righe tutte devono essere indentate 
#operatori di comparazione
x == 5 #doppio uguale, restituisce True se x è uguale a 5
x != 5 #diverso, restituisce True se x è diverso da 5
x < 5 #minore, restituisce True se x è minore di 5
x > 5 #maggiore, restituisce True se x è maggiore di 5
x <= 5 #minore o uguale, restituisce True se x è minore o uguale a 5
x >= 5 #maggiore o uguale, restituisce True se x è maggiore o
# else e elif
y = 10
if x < y:
    print("x è minore di y")
else:
    print("x non è minore di y") #se la condizione è falsa esegue questo blocco di codice

if x < y:
    print("x è minore di y")
elif x == y:
    print("x è uguale a y") #se la prima condizione è falsa verifica questa condizione e se è vera esegue questo blocco di codice
# else e or
x = 4
if x < 5 and x > 0:
    print("x è compreso tra 0 e 5") #se entrambe le condizioni sono vere esegue questo blocco di codice
if x < 0 or x > 5:
    print("x non è compreso tra 0 e 5") #se una delle due condizioni è vera esegue questo blocco di codice
    #basta che 1 delle 3 condizioni sia vera per eseguire il blocco di codice
#not
if not(x < 5 ):
    print("x non è minore di 5") #se la condizione è falsa esegue questo blocco di codice
#versione shor hand 
if x < 5: print("x è minore di 5") #se la condizione è vera esegue questo blocco di codice che in questo caso è una sola stringa
#if annidati
x = 15
if x > 10:
    if x < 20:
         print("x è compreso tra 10 e 20")
else:
            print("x non è compreso tra 10 e 20")
         #se entrambe le condizioni sono vere esegue questo blocco di codice
        # in pratica se la prima condizione è vera verifica la seconda condizione e se è vera esegue questo blocco di codice
