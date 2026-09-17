from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rotas.dashboards import router as dashboards_router
from rotas.visitas import router as visitas_router

app = FastAPI(title="Portaria API")

# Registrar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(visitas_router, prefix="/api/visitas", tags=["Visitas"])
app.include_router(dashboards_router, prefix="/api/dashboards", tags=["Dashboards"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
