from bs4 import BeautifulSoup
import json


with open('source/PO2.html', 'r') as file:
    data = []
    html_doc = ''
    for line in file.readlines():
        html_doc += line
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    data_script = soup.find_all('script')
    is_print = False
    data_raw = data_script[-2].contents[0].split('\n')

    for line in data_raw:
        if 'ar2' in line:
            is_print = False
            break

        if 'item' in line:
            is_print = True
        if 'ds.push' in line:
            continue
        
        if is_print:
            try:
                start_pos = line.index('{') + 1
                end_pos = line.index('}')
            except ValueError:
                continue

            # print(line[start_pos:end_pos])
            data.append(line[start_pos:end_pos])

get_key = lambda x : x.split(':')[0]
get_value = lambda x : x.split(':')[1]

keys = []
vals = []
for i, d in enumerate(data):
    t_keys = []
    t_vals= []
    d = d.split(',')
    for f in d:
        t_keys.append(get_key(f))
        t_vals.append(get_value(f))
    keys.append(t_keys)
    vals.append(t_vals)

for v in vals:
    print(v)