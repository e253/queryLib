from mongo import _mongo_get_meals 
from neo4j import _neo4j_get_meals 


def get_meals(ingr_list, db='MongoDB'):
    '''Takes a list of ingredients and a database, returns a list of compatible meals.
    ingr_list: list of ingredients which meals are wanted
    ingr_listType: list
    db: Default 'MongoDB'
        Options:
            - mongodb
            - neo4j
    return: list of recipe's contained the given ingredient list
    rType: list
    '''
    if db.lower().strip() == 'mongodb':
        print('Processing Query with MongoDB!')
        return _mongo_get_meals(ingr_list)
    if db.lower().strip() == 'neo4j':
        print('Processing Query with Neo4j!')
        return _neo4j_get_meals(ingr_list)
    else:
        return '{} is an invalid input database. Try...\n- MongoDB\n- Neo4j'.format(db)



if __name__ == "main":
    print('Welcome to LB food queryLib')
    ingr_list = input('Enter ingredients comma separated without spaces')
    print(get_meals(ingr_list.split(',')))