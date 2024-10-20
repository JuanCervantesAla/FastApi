import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Ciudadano(BaseModel):
    Nombre: str
    Apellido: str
    Curp: str
    Estado: int


ciudadanos = [
    Ciudadano(Nombre="Juan", Apellido="Pérez", Curp="CURP123456", Estado=1),
    Ciudadano(Nombre="María", Apellido="García", Curp="CURP654321", Estado=2),
    Ciudadano(Nombre="Pedro", Apellido="López", Curp="CURP789456", Estado=3)
]

@app.get("/")
def index():
    return {"message": "Bienvenido a la API de Ciudadanos"}


@app.get("/ciudadanos", response_model=List[Ciudadano])
def mostrar_ciudadanos():
    return ciudadanos

@app.post("/ciudadanos")
def insertar_ciudadano(ciudadano: Ciudadano):
    ciudadanos.append(ciudadano)  
    return {"message": f"Ciudadano {ciudadano.Nombre} insertado con éxito"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000)) 
    uvicorn.run(app, host="0.0.0.0", port=port)
