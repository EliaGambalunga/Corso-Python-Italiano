x = "ciao" #doppi apici
y = 'mondo' #singoli apici
print("ciao mondo") # mando a schermo ciao mondo
x = """ciao
ciao ciao""" #tripli apici per piu righe
print(x[0]) #manda a schermo il primo carattere della stringa, se mettevo 1 mi mandava a schermo il secondo carattere, 2 il terzo e cosi via
print(x[0:3]) #manda a schermo i primi 3 caratteri della stringa, se mettevo 1:4 mi mandava a schermo il secondo, terzo e quarto carattere e cosi via
print(x[0:]) #manda a schermo tutta la stringa
print(x[:3]) #manda a schermo i primi 3 caratteri della stringa
print(x[-1]) #manda a schermo l'ultimo carattere della stringa
print(x[-3:]) #manda a schermo gli ultimi 3
#lo spazio conta come carattere
print(len(x)) #manda a schermo la lunghezza della stringa #si parte da 1 non da 0
print(x.count("c")) #manda a schermo quante volte c'è la lettera c nella stringa
print(x.find("o")) #manda a schermo la posizione della prima
print(x.lower()) #manda a schermo la stringa tutta in minuscolo
print(x.upper()) #manda a schermo la stringa tutta in maiuscolo
print(x.replace("ciao", "hello")) #manda a schermo la stringa sostituendo ciao con hello
print(x.split(" ")) #manda a schermo la stringa trasformandola in una lista, ogni volta che trova uno spazio crea un elemento nuovo) # il risultato sarà che ogni volta che nella stirnga si trova una lettera c,
#questa viene tolta e viene creato un nuovo elemento nella lista