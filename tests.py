import pandas


def from_csv(file_name='tel.csv') -> list:    
    try:
        with open(file_name,'r', encoding='utf-8') as f:
            text = f.read()
        lst_str = text.split('\n')
        return [tuple(elem_str.split(',')) for elem_str in lst_str]
    except:
        return []
    
ds = pandas.ExcelFile('tel.xlsx').parse('Sheet1')  

print(ds)    

