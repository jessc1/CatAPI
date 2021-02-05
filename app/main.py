from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()


cat_db = [
    {
        "name":"c2",
        "breed": "Angora",
        "location_of_origin": "Thailand",
        "coat_length": "short",
        "body_type": "fat",
        "pattern": "blue eyes",
        }
    ]
        
 
class Cat(BaseModel):
    name:str
    breed: str
    location_of_origin:str
    coat_length: str
    body_type:str
    pattern:str

  

@app.get('/', response_model=List[Cat])
async def index():
    """ Retorna dados sobre o gato. """
    return cat_db


@app.post('/', status_code=201)
async def add_cat(catload: Cat):
    """Cria dados sobre um gato e retorna o id. """
    cat = catload.dict()
    cat_db.append(cat)
    return {'id': len(cat_db) - 1}




@app.put('/id')
async def update_cat(id: int, catload: Cat):
    """ Atualiza dados sobre o gato a partir do id digitado. """
    cat = catload.dict()
    cats_length = len(cat_db)
    if 0 <= id <= cats_length:
        cat_db[id] = cat
        return None
    raise HTTPException(status_code=404, detail="Cat with given id not found")


@app.patch("/{id}")
async def patch(id:int, cat: Cat):
    if cat.breed == cat_db[id]:
        return{"cat": cat.breed}
    raise HTTPException(status_code=400, detail="Breed already exist")

@app.delete("/id")
async def delete_cat(id: int):
    """ Deleta um gato da API a partir do id digitado """
    cats_length = len(cat_db)
    if 0 <= id <= cats_length:
        del cat_db[id]
        return None
    raise HTTPException(status_code=404, detail="Cat with given id not found")
