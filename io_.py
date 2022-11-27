import pandas

def to_csv(file_name: str, records: list):
    text = []
    with open(file_name,'w', encoding='utf-8') as f:
        for record in records:
            text.append(','.join(record)+'\n')
        f.writelines(text)                                    

def from_csv(file_name='tel.csv') -> list:    
    try:
        with open(file_name,'r', encoding='utf-8') as f:
            text = f.read()
        lst_str = text.split('\n')
        return [tuple(elem_str.split(',')) for elem_str in lst_str]
    except:
        return []

def to_excel(file_name: str, records: list):
    ds = pandas.DataFrame(records)
    ds.to_excel(file_name)

def from_excel(file_name='tel.xlsx') -> list: 
    ds = pandas.read_excel(file_name)    
    records = []
    for i in range(len(ds)):
        res = []
        for j in ds.loc[i]:
            res.append(j)
        records.append(tuple(res[1:]))       
    return records
    

def save_data(dataclass):
    if dataclass.mode == 0:
        to_csv(dataclass.file_name+'.csv', dataclass.records)
    elif dataclass.mode == 1:
        to_excel(dataclass.file_name+'.xlsx', dataclass.records)
    
def load_data(dataclass):
    if dataclass.mode == 0:
        return from_csv(dataclass.file_name+'.csv')
    elif dataclass.mode == 1:
        return from_excel(dataclass.file_name+'.xlsx')