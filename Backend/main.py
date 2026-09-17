from fastapi import FastAPI

from rotas.dashboard import router as dashboard_router
from rotas.visitas import router as visitas_router

app = FastAPI(title="Portaria API")

app.include_router(visitas_router)
app.include_router(dashboard_router)


@app.get("/health")
def health():
    return {"status": "ok", "message": "API is running successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
