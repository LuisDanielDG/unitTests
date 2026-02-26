from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    data = {"message":"Pruebas unitarias"}
    return JSONResponse(content=data, status_code=202)

@app.get("/sumas")
def sumas(numero1: int, numero2: int):
    suma = numero1 + numero2
    data = {
        "numero1": numero1,
        "numero2": numero2,
        "suma": suma
    }
    return JSONResponse(content=data, status_code=202)

@app.get("/restas")
def restas(numero1: int, numero2: int):
    resta = numero1 - numero2
    data = {
        "numero1": numero1,
        "numero2": numero2,
        "resta": resta
    }
    return JSONResponse(content=data, status_code=202)

@app.get("/multiplicaciones")
def multiplicaciones(numero1: int, numero2: int):
    multiplicacion = numero1 * numero2
    data = {
        "numero1": numero1,
        "numero2": numero2,
        "multiplicacion": multiplicacion
    }
    return JSONResponse(content=data, status_code=202)

@app.get("/divisiones")
def divisiones(numero1: int, numero2: int):
    division = numero1 / numero2
    data = {
        "numero1": numero1,
        "numero2": numero2,
        "division": division
    }
    return JSONResponse(content=data, status_code=202)

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    C0RSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)