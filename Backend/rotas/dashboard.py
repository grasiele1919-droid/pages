from fastapi import APIRouter

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


@router.get("/resumo")
def resumo_visitas():
    return {
        "total_visitas": len(VISITAS),
        "visitantes_confirmados": sum(
            1 for visita in VISITAS if visita["status"] == "confirmada"
        ),
        "proximas_visitas": VISITAS[:2],
    }
