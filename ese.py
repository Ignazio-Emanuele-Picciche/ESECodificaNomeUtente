import json
from ast import literal_eval
import numpy as np

# mi creo una lista di tuple con i nomi e la seguenza di cifre associate
def modlist(lung_logs, new_list):
    for x in my_set:
        rand=np.random.randint(10000000, 100000000)
        my_list.append([x, rand])
        for i in range(lung_logs):
            if new_list[i][1] == x:
                new_list[i][1] = rand
    return new_list


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

modlist(lung_logs, new_list)
print(new_list)


fin.close()

# Salvo i log modificati in un nuovo file (cosi non tocco il file originale)
fin = open('C:\\Users\\ignaz\\Desktop\\UCBM\\Programmazione\\ESECodificaNomeUtente\\logs_anonimizzato_1_new.json','w')

fin.write('[')
for x in new_list:
    fin.write('\n'+str(x)+',')

fin.write('\n'+']')
fin.close()



# Stampo la lista di tuple per vedere come sono codificati i valori
for x in my_list:
    print(x)



