import json

def create_db():
    register = {}
    register ['spirits'] = {
        'Vodka':
        {
            'process':'',
            'brand':'',
            'description':'',
            'types':''
        },
        'Gin':
        {
            'process':'',
            'brand':'',
            'description':'',
            'types':''
        },
        'Rum':
        {
            'process':'',
            'brand':'',
            'description':'',
            'types':'',
            'vintage':''
        },
        'Tequila':
        {
            'process':'',
            'brand':'',
            'description':'',
            'types':'',
            'vintage':''
        },
        'Whiskey':
        {
            'process':'',
            'brand':'',
            'description':'',
            'types':'',
            'vintage':''
        }           
    }
    register ['liquor'] = {
        'Vermouth':
        {
            'process':'',
            'brand':'',
            'description':'',
            'types':''
        },
        'Port wine':
        {
            'process':'',
            'brand':'',
            'description':'',
            'types':''
        },
        'Rum':
        {
            'process':'',
            'brand':'',
            'description':'',
            'types':'',
            'vintage':''
        },
        'Tequila':
        {
            'process':'',
            'brand':'',
            'description':'',
            'types':'',
            'vintage':''
        },
        'Whiskey':
        {
            'process':'',
            'brand':'',
            'description':'',
            'types':'',
            'vintage':''
        }           
    } 
    register ['non-alcoholic'] = {}
    #print(register)

    with open('bar.json', 'w') as bd:
        json.dump(register, bd, indent=4)