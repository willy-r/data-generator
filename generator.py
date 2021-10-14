import os
import sys

import requests

import queries as q


def generate_data(quantity: int) -> str:
    params = {'results': quantity, 'nat': 'br', 'inc': 'name,email,login,dob,phone'}
    r = requests.get('https://randomuser.me/api/', params=params)
    data = r.json()

    tuples_lines = ''

    for i, user_data in enumerate(data['results']):
        name = user_data['name']['first'] + ' ' + user_data['name']['last']
        email = user_data['email']
        username = user_data['login']['username']
        password = user_data['login']['password']
        birth_date = user_data['dob']['date'][:10] # Gets only the date.
        age = user_data['dob']['age']
        phone = user_data['phone']

        insert_comma = '' if (data['info']['results'] - 1) == i else ','
        
        tuples_lines += f"  ('{name}', '{email}', '{username}', '{password}', '{birth_date}', {age}, '{phone}'){insert_comma}\n"
    
    return tuples_lines


def create_files(tuples_str: str) -> None:
    # Creates directoy to save .sql file in the same directory.
    try:
        os.makedirs('db', exist_ok=True)

        with open('db/db-schema.sql', 'w') as writer:
            writer.write(q.CREATE_DATABASE_SQL + '\n')
            writer.write(q.CREATE_TABLE_SQL)

        with open('db/db-data.sql', 'w') as writer:
            writer.write(q.INSERT_DATA_SQL)
            writer.write(tuples_str + ';\n')
    except OSError:
        print('A pasta não pôde ser criada.')
    else:
        print('Arquivos .sql gerados com sucesso, aproveite as consultas!')


if __name__ == '__main__':
    USAGE = 'usage: python3 generator.py quantity'
    
    try:
        quantity = int(sys.argv[1])

        if quantity > 5000:
            quantity = 5000
    except IndexError:
        # Default.
        quantity = 5000
    except ValueError:
        print('error: quantity param must be a valid integer')
        sys.exit()

    tuples = generate_data(quantity)
    create_files(tuples)
