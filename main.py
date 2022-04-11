from query import Query

while True:
    print('_'*50)
    print('\n 1 - consult database\n 2 - choose a specific spirit\n')
    print('_'*50)

    option = input('Choose a number from the list: ')
    if option == '1':
        print('hey')
    elif option == '2':
        Query().search()

    elif option == '3':
        option = input('What is that you want to add? ')
