import json
from barback import create_db

class Query():
    def __init__(self):
        try:
            with open ('bar.json', 'r') as db_json:
                self.db = json.load(db_json)
        except FileNotFoundError:
            create_db()
    
    def search(self):
        print(f"{'-'*50} \ncategories:\n{'-'*50}")
        i = 1
        #visualizacao de categorias
        for category in self.db:
            print(f"{i} - {category}")   
            i += 1
    
        option = input('\nChoose a category: ')
        if option == '1':
            print(f"{'-'*50} \ncategories:\n{'-'*50}")
            for category in self.db['spirits']:
                print(category)
            option = input('\nChoose your poison:')
            if option == '1':
                print(self.db['spirits']['Vodka'])
            elif option == '2':
                print(self.db['spirits']['Gin'])
            elif option == '3':
                print(self.db['spirits']['Rum'])
            elif option == '4':
                print(self.db['spirits']['Tequila'])
            elif option == '5':
                print(self.db['spirits']['Whiskey'])
        elif option == '2':
            print(f"{'-'*50} \ncategories:\n{'-'*50}")
            for category in self.db['liquor']:
                print(category)
            option = input('\nChoose your poison:')
            if option == '1':
                print(self.db['liquor']['Vermouth'])
            elif option == '2':
                print(self.db['liquor']['Port wine'])
            elif option == '3':
                print(self.db['liquor']['Rum'])
            elif option == '4':
                print(self.db['liquor']['Tequila'])
            elif option == '5':
                print(self.db['liquor']['Whiskey'])
        elif option == '3':
            print(f"{'-'*50} \ncategories:\n{'-'*50}")
            for category in self.db['non-alcoholic']:
                print(category)
            option = input('\nChoose your poison:')
            if option == '1':
                print(self.db['spirits']['vodka'])
            elif option == '2':
                print(self.db)