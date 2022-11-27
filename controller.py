import model
import view
import consts
import io_
import os

class Controller:
    actions = ['0 - Загрузить', '1 - Сохранить', '2 - Просмотреть', '3 - Добавить', '4 - Настройки','5 - Выход']

    def __init__(self, file_name = 'tel', mode = 0):

        self.view = view.View(self.actions)
        self.model = model.Phone_booK()
        self.data = consts.DataClass(mode = mode, file_name = file_name)
        self.menu = {0: self.load, 1: self.save, 2: self.show, 3: self.add, 4: self.settings, 5: self.exit}
        pass
    
    def settings(self):
        self.data.mode = int(self.view.get_answer('Выберите способ хранения данных: csv[0]/excel[1] --> '))
        name = self.view.get_answer('Введите имя файла без расширения, Enter - оставить предыдущее значение --> ')
        if name:
            self.data.file_name = name

    def load(self):
        self.data.records = io_.load_data(self.data)

    def save(self):
        io_.save_data(self.data)
    
    def show(self):
        self.view.show_records(self.data.records)
        self.view.get_answer('press enter to continue')

    def add(self):
        self.data.records.append(self.view.get_record(self.data.structure))

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
            
