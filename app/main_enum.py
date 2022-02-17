from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class Nomes(str, Enum):
    nome = "gustavo"
    sobrenome = "garcia"
    segundo = "pereira"

@app.get('/nomes/{nomes}')
async def nome(nomes:Nomes):
    print("<>",nomes)
    print("<>",Nomes.nome)
    print("<>",Nomes.sobrenome)
    print("<>",Nomes.nome.value)
    if nomes == Nomes.nome:

        return {Nomes.nome}
    if nomes == Nomes.sobrenome:

        return {"nome":Nomes.sobrenome}
    return {"nome":""}
