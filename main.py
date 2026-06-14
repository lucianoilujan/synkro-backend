from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Synkro IoT Backend")

class Telemetria(BaseModel):
    dispositivo_id: str
    temperatura: float
    gas_ppm: int
    estado: str

@app.get("/")
def inicio():
    return {"status": "online", "mensaje": "Servidor Synkro corriendo desde GitHub en AWS"}

@app.post("/api/telemetria")
def recibir_datos(data: Telemetria):
    print(f"Datos recibidos de {data.dispositivo_id}: Gas {data.gas_ppm} PPM")
    return {
        "status": "success", 
        "mensaje": "Datos procesados correctamente",
        "recibido": data
    }