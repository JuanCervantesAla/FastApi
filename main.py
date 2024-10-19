import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Curso(BaseModel):
    titulo: str
    descripcion: str
    dificultad: str
    tiempoMeses: int

@app.get("/")
def index():
    return {"message": "Bienvenido al curso de FastAPI"}

@app.get("/cursos")
def mostrar_curso(tituloCurso: str):
    return {"message": f"curso: {tituloCurso}"}

@app.post("/cursos")
def insertar_curso(curso: Curso):
    return {"message": f"curso {curso.titulo} insertado"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # Usa el puerto de Render o 8000 por defecto
    uvicorn.run(app, host="0.0.0.0", port=port)
