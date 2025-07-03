from pydantic import BaseModel, RootModel
from typing import List

class RegistroIn(BaseModel):
    nome: str
    titulo: str
    data_lancamento: int
    description: str

class RegistroOut(RegistroIn):
    registro_id: str

class ListaRegistros(RootModel[List[RegistroOut]]):
    pass
