from fastapi import APIRouter

from rotas.visitas import VISITAS

router = APIRouter()


@router.get("/resumo")
def resumo_visitas():
    return {
        "total_visitas": len(VISITAS),
        "visitantes_confirmados": sum(
            1 for visita in VISITAS if visita["status"] == "confirmada"
        ),
        "proximas_visitas": VISITAS[:2],
    }
