import model2
import view
import consts
import io_
import os

class Controller:
    actions = ['0 - Загрузить', '1 - Сохранить', '2 - Просмотреть', '3 - Добавить', 
        '4 - Настройки','5 - Поиск', '6 - Удалить', '7 - Выход']

    def __init__(self, file_name = 'tel', mode = 0):

        self.view = view.View(self.actions)
        self.model = model2.Phone_booK()
        self.data = consts.DataClass(mode = mode, file_name = file_name)
        self.menu = {0: self.load, 1: self.save, 2: self.show, 3: self.add, 
            4: self.settings, 5: self.find, 6: self.delete, 7: self.exit}
        self.load()
        
    
    def delete(self):
        os.system('cls')    
        self.view.out(self.model.records)
        index = int(self.view.get_answer('Индекс записи для удаления -> '))
        self.model.del_record(index)
        
    def find(self):
        os.system('cls')
        filter = self.view.get_answer('подстрока для поиска: ')     
        os.system('cls')   
        self.show(filter)

    def settings(self):
        self.data.mode = int(self.view.get_answer('Выберите способ хранения данных: csv[0]/excel[1] --> '))
        name = self.view.get_answer('Введите имя файла без расширения, Enter - оставить предыдущее значение --> ')
        if name:
            self.data.file_name = name

    def load(self):
        self.data.records = self.model.records
        self.model.records = io_.load_data(self.data)
        self.data.structure = self.model.records.columns


    def save(self):
        self.data.records = self.model.records
        io_.save_data(self.data)
    
    def show(self, filter=''):
        if not filter:
            self.view.out(self.model.records)
        else:
            self.view.out(self.model.filter_by_field(self.model.records, filter))    
        self.view.get_answer('press enter to continue')

    def add(self):
        record = list()
        for i in self.data.structure:
            record.append(self.view.get_answer(f'{i}--> '))
        self.model.add_record(record)

    def exit(self):
        pass
    
    def run(self):
        while True:
            self.view.main_menu()
            todo = int(self.view.get_answer())
            if 'Выход' in self.actions[todo]:
                break
            os.system('cls')
            self.menu[todo]()
            
