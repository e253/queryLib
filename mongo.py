from pymongo import MongoClient 
from pymongo.errors import ConnectionFailure
from decouple import config

def connect_to_mongo():
    '''Attempts to establish connect to mongo in EC2 
    throws ConnectException if something goes wrong

    return: mongo client
    rtype: MongoClient '''
    try: 
        return MongoClient(config('IP'), 27017)
    except ConnectionError:
        print('Connection to MongoDB failed, check connection information and try again') 


def _mongo_get_meals(ingr_list):
    client = connect_to_mongo()
    collection = client.project2.food
    # QUERY GOES HERE
    # return answer