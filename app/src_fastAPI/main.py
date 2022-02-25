# projeto usando o neo4j e fastAPI


from neo4j import GraphDatabase

from fastapi import FastAPI

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, name: str, name2: str):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, name, name2)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, name: str, name2: str):
        query = (
            "CREATE (p1:Person { name: $person1_name }) "
            "CREATE (p2:Person { name: $person2_name }) "
            "CREATE (p1)-[:relacao]->(p2) "
            "RETURN p1, p2"
        )
        result = tx.run(query, person1_name=name, person2_name=name2)
        return 'ok'



app = FastAPI()

@app.get('/{name}/{name2}')
async def main(name:str, name2: str):
    """
        Creta um novo no
        - **name**: nome do no
        - **name2**: nome do no
    """
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "gugu")
    greeter.print_greeting(name, name2)
    greeter.close()
    return {"status": "cadastrado"}

