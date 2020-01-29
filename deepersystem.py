import json

p_man = []
p_wat = []
m = []
w = []
managers = []
watchers = []
with open('source_file_2.json') as f:
    data = json.loads(f.read())
    # print(data)


for i in range(0, len(data)):
    for x in range(0, len(data[i]['managers'])):
        m.append(data[i]['managers'][x])
        w.append(data[i]['watchers'][x])

m = list(set(m))  
w = list(set(w))

for i in m: # Elementos da minha lista
    for d in data: # elementos do Json
        if i in d['managers']:
            p_man.append(d['name'])

    p_man = list(set(p_man))
    
    managers.append({
        i: p_man
    })             


for i in w: # Elementos da minha lista
    for d in data: # elementos do Json
        if i in d['watchers']:
            p_wat.append(d['name'])
           

    p_wat = list(set(p_wat))

    watchers.append({
        i: p_wat
    })             

# js = json.dumps(managers)
# print(js)
with open('managers.json', 'w') as fl:
    json.dump(managers, fl, indent=2)

with open('watchers.json', 'w') as fl:
    json.dump(watchers, fl, indent=2)
