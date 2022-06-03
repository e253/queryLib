from pymongo import MongoClient 
from pymongo.errors import ConnectionFailure, OperationFailure
from decouple import config

def connect_to_mongo():
    '''Attempts to establish connect to mongo in EC2, 
    catches pymongo.errors.ConnectionFailure, pymongo.errors.OperationFailure error if something goes wrong with connection.

    return: mongo client
    rtype: pymong.MongoClient '''
    try: 
        return MongoClient('mongodb://{0}:{1}@{2}:27017/project2'.format(config('MONGO_USERNAME'), config('MONGO_PASSWORD'), config('IP')))
    except (ConnectionFailure, OperationFailure):
        print('Connection to MongoDB failed, check connection information and try again') 


def _mongo_get_meals(ingr1, ingr2):
    client = connect_to_mongo()
    collection = client.project2.food
    query = collection.find({'$or':[
        {'p_ingredient.ingredient_name': ingr1},
        {'p_ingredient.ingredient_name': ingr2},
        {'s_ingredient.ingredient_name': ingr1},
        {'s_ingredient.ingredient_name': ingr2},
    ]},
    {'recipe_name': 1})
    return [i['recipe_name'] for i in query]