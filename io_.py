import pandas

def to_csv(file_name: str, records: list):
    records.to_csv(file_name)

def from_csv(file_name='tel.csv') -> list:    
    return pandas.read_csv(file_name)    
    
def to_excel(file_name: str, records: list):
    records.to_excel(file_name)

def from_excel(file_name='tel.xlsx') -> list: 
    return pandas.read_excel(file_name)    
    

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