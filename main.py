from sre_parse import CATEGORIES
from barback import create_db
import json

try:
    with open ('bar.json', 'r') as db_json:
        db = json.load(db_json)
except FileNotFoundError:
    create_db()

while True:
    print('_'*50)
    print('\n 1 - consult database\n 2 - choose a specific spirit\n')
    print('_'*50)

    option = input('Choose a number from the list: ')
    if option == '1':
        print(db)
    elif option == '2':
        print(f"{'-'*50} \ncategories:\n{'-'*50}")
        i = 1
        #visualizacao de categorias
        for category in db:
            print(f"{i} - {category}")   
            i += 1

        option = input('\nChoose a category: ')
        if option == '1':
            print(f"{'-'*50} \ncategories:\n{'-'*50}")
            for category in db['spirits']:
                print(category)
            option = input('\nChoose your poison:')
            if option == '1':
                print(db['spirits']['vodka'])
            elif option == '2':
                print(db['spirits']['gin'])
        elif option == '2':
            print(f"{'-'*50} \ncategories:\n{'-'*50}")
            for category in db['liquor']:
                print(category)
            option = input('\nChoose your poison:')
            if option == '1':
                print(db['spirits']['vodka'])
            elif option == '2':
                print(db)
        elif option == '3':
            print(f"{'-'*50} \ncategories:\n{'-'*50}")
            for category in db['non-alcoholic']:
                print(category)
            option = input('\nChoose your poison:')
            if option == '1':
                print(db['spirits']['vodka'])
            elif option == '2':
                print(db)
