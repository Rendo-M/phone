class DataClass:
    def __init__(self, *args, **kwargs):
        self.setter(*args, **kwargs)
    
    def setter(self, file_name = 'empl', records=[], mode = 0):
        self.file_name = file_name        
        self.records = records
        self.mode = mode
        self.structure = ['Имя','Должность','Телефон','Зарплата']
