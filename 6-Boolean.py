x = True
y = False
# valori booleani, possono essere solo True o False
print(5<10) #manda a schermo True, che è un valore booleano
print(5>10) #manda a schermo False, che è un valore booleano
#quindi posso essere usati per fare confronti
if 5<10:
    print("5 è minore di 10") #se la condizione è vera allora viene eseguito il codice dentro l'if
else:
    print("5 è maggiore di 10") #se la condizione è falsa allora non viene eseguito il codice dentro l'if
#posso usare anche else per eseguire del codice se la condizione è falsa  
#posso anche valutare le variabili 
#esistono una serie di variabili che danno sempre False, le altre danno sempre True
#False: False, None, 0, 0.0, "", [], {}, set()
#True: True, qualsiasi altro valore diverso da quelli sopra
#esempio 
print(bool(0)) #manda a schermo False
print(bool(1)) #manda a schermo True