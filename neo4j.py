from py2neo import Graph
from decouple import config

def connect_to_neo():
    '''Attempts to establish connect to Neo4j in EC2 

    return: Graph Object 
    rtype: py2neo.database.Graph '''
    try: 
        return Graph("bolt://{}:7687".format(config('IP')), auth = (config('NEO_USERNAME'), config("NEO_PASSWORD")))
    except:
        print('Connection to Neo4j failed, check connection information and try again')

def _neo4j_get_meals(ingr1, ingr2):
    graph = connect_to_neo()
    return list(graph.run("MATCH (one:INGREDIENT)-[:USES]-(ee:RECIPE)-[:USES]-(two:INGREDIENT)WHERE one.name <> '{0}' AND two.name <> '{1}' RETURN ee.name".format(ingr1, ingr2)))
