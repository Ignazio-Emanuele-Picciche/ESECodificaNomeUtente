import json
from ast import literal_eval
import numpy as np

fin = open('C:\\Users\\ignaz\\Desktop\\UCBM\\Programmazione\\ESECodificaNomeUtente\\logs_anonimizzato_1.json')

lista_persone = json.load(fin)

lista_json = json.dumps(lista_persone, indent=4)
new_list=np.array(literal_eval(lista_json)).tolist()

lung_logs = len(new_list)
# lung_log = len(new_list[0])

my_set = set()
my_list = []

# mi creo il set con tutti i nomi (set di nomi univoci dato che è un set :) )
# nel mentre mi elimino anche il terzo campo, come richiesto dalla traccia
for i in range(lung_logs):
    my_set.add(new_list[i][1])
    new_list[i].pop(2)

# mi creo una lista di tuple con i nomi e la seguenza di cifre associate
for x in my_set:
    rand=np.random.randint(10000000, 100000000)
    my_list.append(tuple((x, rand)))
    for i in range(lung_logs):
        if new_list[i][1] == x:
            new_list[i][1] = rand


fin.close()

# Salvo i log modificati in un nuovo file (cosi non tocco il file originale)
fin = open('C:\\Users\\ignaz\\Desktop\\UCBM\\Programmazione\\ESECodificaNomeUtente\\logs_anonimizzato_1_new.json','w')
fin.write(str(new_list))
fin.close()



print('\n',my_list)