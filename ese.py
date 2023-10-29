import json
import numpy as np

# mi creo una lista di tuple con i nomi e la seguenza di cifre associate
def modlist():
    for x in set_nomi:
        rand=np.random.randint(10000000, 100000000) # Genero casualmente un numero (codice identificati) che andrà associato univocamente ad un nome
        nome_codice.append([x, rand])   # aggiungo la coppia nome - codice identificativo all'array nome_codice
        for i in range(lung_logs):
            if lista_log[i][1] == x:
                lista_log[i][1] = rand


fin = open('logs_anonimizzato_1.json')
lista_log = json.load(fin)

lung_logs = len(lista_log)

set_nomi = set()  # Creo un set per salvare i nomi in maniera univoca
nome_codice = []  # Creo una lista dove andare a slvare le coppie nome - codice identificativo

# mi creo il set con tutti i nomi (set di nomi univoci dato che è un set :) )
# nel mentre mi elimino anche il terzo campo, come richiesto dalla traccia
for i in range(lung_logs):
    set_nomi.add(lista_log[i][1])
    lista_log[i].pop(2)

modlist()
fin.close()


lista_log = json.dumps(lista_log, indent=4)
with open('logs_anonimizzato_1_new.json','w')  as of:
    of.write(lista_log)


nome_codice = json.dumps(nome_codice, indent=1)
with open('nome_codice.json', 'w') as f:
    f.write(nome_codice)