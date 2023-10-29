import json
import numpy as np

# In questa funzione creo una lista di coppie nome - codice identificativo. 
# Inoltre sostituisco anche il nome con il codice identificativo generato casualmente
def modlist():
    for x in set_nomi:
        rand=np.random.randint(10000000, 100000000) # Genero casualmente un numero (codice identificati) che andrà associato univocamente ad un nome
        nome_codice.append([x, rand])   # aggiungo la coppia nome - codice identificativo all'array nome_codice
        for i in range(lung_logs):
            if lista_log[i][1] == x:
                lista_log[i][1] = rand  # sostituisco il nome con il codice identificativo


# fin = open('logs_anonimizzato_1.json')
fin = open('logs_anonimizzato_2.json')
lista_log = json.load(fin) # leggo il file come array python

lung_logs = len(lista_log)  # salvo il numero dei log cosi da poterli iterare piu facilmente

set_nomi = set()  # Creo un set per salvare i nomi in maniera univoca
nome_codice = []  # Creo una lista dove andare a slvare le coppie nome - codice identificativo

for i in range(lung_logs):
    set_nomi.add(lista_log[i][1])   # aggingo ogni nome che trovo al set_nomi (il set li renderà univoci)
    # NB: in questo progamma non viene controllato se i nomi hanno maiuscole o spazi diversi, quindi nel set_nomi potrebbero essere salvati nomi duplicati
    # per risolvere questo problema dovremmo eliminare gli spazi e fare str.lower() per ogni nome

    lista_log[i].pop(2) # rimuovo il campo 'Utente coinvolo' come richiesto dalla traccia

modlist()   # richiamo la funzione
fin.close() # chiudo il file


json_object = json.dumps(lista_log, indent=4)   # trasformo l'array in un oggetto json
# salvo i nuovi log in un nuovo file, così da salvare il file originale
with open('logs_anonimizzato_2_new.json','w')  as of:
    of.write(json_object)   # scrivo nel file


json_object = json.dumps(nome_codice, indent=1) # trasformo l'array in un oggetto json
with open('nome_codice.json', 'w') as f:
    f.write(json_object)    # scrivo nel file