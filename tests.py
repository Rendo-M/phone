import pandas


def from_csv(file_name='tel.csv') -> list:    
    try:
        with open(file_name,'r', encoding='utf-8') as f:
            text = f.read()
        lst_str = text.split('\n')
        return [tuple(elem_str.split(',')) for elem_str in lst_str]
    except:
        return []
    
ds = pandas.DataFrame(from_csv())    
records = []
for i in range(len(ds)):
    res = []
    for j in ds.loc[i]:
        res.append(j)
    records.append(tuple(res))    
print(records)    

