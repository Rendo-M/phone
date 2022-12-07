class View:

    
    def __init__(self, actions, promo='ТЕЛЕФОННЫЙ СПРАВОЧНИК'):
        self.actions = actions
        self.promo = promo

    def main_menu(self, actions = None):
        if actions is None:
            actions =self.actions
        print(self.promo)
        for action in actions:
            print(action)

    def get_answer(self, ask='--> '):
        return input(ask)

            
    # def show_records(self, records):
    #     for record in records:
    #         for value in record:
    #             print(f'{value}', end=' \t')
    #         print()

    def out(self, value):
        print(value)

def main():
    pass                