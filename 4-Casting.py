#significa predere il valore di un dato e convertirlo in un altro tipo di dato
#per esempio, se abbiamo un numero e vogliamo convertirlo in una stringa o viceversa
# si può usare per fare operazioni ne lquale si prevede di sommare una stringa e un numero
x = 5
y = "ciao"
# se proviamo a sommare un numero e una stringa, Python darà un erro
x = "ciao"
y = str(5) # converte il numero in stringa
# ora possiamo sommare la stringa e il numero convertito
z = x + y # "ciao5"
# se vogliamo convertire una stringa in un numero, possiamo usare int() o float()
x = "5"
y = int(x) # converte la stringa in un intero
z = float(x) # converte la stringa in un float
# ora possiamo fare operazioni con i numeri convertiti
x = 5
y = 2.5
z = x + y # somma tra un intero e un float