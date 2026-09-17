from pydantic import BaseModel


class VisitaCriar(BaseModel):
    nome: str
    empresa: str
    bloco: str
    apartamento: str
    data: str
    horario: str
    status: str


class VisitaSaida(BaseModel):
    id: int
    nome: str
    empresa: str
    bloco: str
    apartamento: str
    data: str
    horario: str
    status: str
