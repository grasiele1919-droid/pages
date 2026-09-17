from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api")

VISITAS = [
    {
        "id": 1,
        "nome": "João Silva",
        "empresa": "SENAC",
        "bloco": "A",
        "apartamento": "302",
        "data": "2026-09-16",
        "horario": "09:30",
        "status": "confirmada",
    },
    {
        "id": 2,
        "nome": "Maria Oliveira",
        "empresa": "Portaria Registro",
        "bloco": "B",
        "apartamento": "118",
        "data": "2026-09-16",
        "horario": "11:00",
        "status": "pendente",
    },
    {
        "id": 3,
        "nome": "Carlos Mendes",
        "empresa": "Condomínio Central",
        "bloco": "C",
        "apartamento": "540",
        "data": "2026-09-17",
        "horario": "14:15",
        "status": "confirmada",
    },
]


@router.get("/visitas")
def listar_visitas():
    return {"total": len(VISITAS), "dados": VISITAS}


@router.get("/visitas/{visita_id}")
def obter_visita(visita_id: int):
    for visita in VISITAS:
        if visita["id"] == visita_id:
            return visita

    raise HTTPException(status_code=404, detail=f"Visita {visita_id} não encontrada")
