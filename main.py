from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import pandas as pd
from model.predictor import predecir_desde_datos
from data.mappings import CLASES_INTERES, CLASES_RANGO

app = FastAPI()

# Cargar modelo entrenado
modelo_interes = joblib.load("model/modelo_arbol_interes_inscribir_puntuacion.pkl")
modelo_rango = joblib.load("model/modelo_arbol_rango_pagar.pkl")

class EntradaModelo(BaseModel):
    sexo: str
    edad: str
    ocupacion: str
    campo: str
    competencias: str
    egresado_unillanos: str
    titulo: str
    universidad_titulo: str
    porcentaje_virtualidad: str

@app.post("/predecir-interes")
def predecir(data: EntradaModelo):
    try:
        entrada_df = pd.DataFrame([data.dict()])
        resultado = predecir_desde_datos(entrada_df, modelo_interes)
        resultado_int = int(resultado)
        resultado_texto = CLASES_INTERES.get(resultado_int, "Desconocido")
        return {"codigo": resultado_int, "descripcion": resultado_texto}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predecir-rango")
def predecir(data: EntradaModelo):
    try:
        entrada_df = pd.DataFrame([data.dict()])
        resultado = predecir_desde_datos(entrada_df, modelo_rango)
        resultado_int = int(resultado)
        resultado_texto = CLASES_RANGO.get(resultado_int, "Desconocido")
        return {"codigo": resultado_int, "descripcion": resultado_texto}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ui", response_class=HTMLResponse)
def get_ui():
    return HTMLResponse("""
<!DOCTYPE html>
<html lang=\"es\">
<head>
    <meta charset=\"UTF-8\">
    <title>Predicción de Interés y Rango</title>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6f8; padding: 2rem; }
        .container { max-width: 600px; background: white; padding: 2rem; margin: auto; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        h2 { text-align: center; color: #333; }
        label { display: block; margin-top: 1rem; font-weight: bold; }
        input, textarea, select { width: 100%; padding: 0.5rem; margin-top: 0.3rem; border: 1px solid #ccc; border-radius: 8px; }
        button { margin-top: 1.5rem; width: 100%; padding: 0.75rem; border: none; border-radius: 8px; font-size: 1rem; cursor: pointer; }
        .btn-interes { background-color: #4CAF50; color: white; }
        .btn-rango { background-color: #2196F3; color: white; }
        .resultado { margin-top: 1.5rem; padding: 1rem; background: #e3f2fd; border-radius: 8px; font-weight: bold; }
    </style>
</head>
<body>
<div class=\"container\">
    <h2>Predicción</h2>
    <label for=\"sexo\">Sexo</label>
    <select id=\"sexo\">
        <option value=\"masculino\">Masculino</option>
        <option value=\"femenino\">Femenino</option>
    </select>

    <label for=\"edad\">Edad</label>
    <input type=\"text\" id=\"edad\" placeholder=\"Ej: 26 a 30 años\">

    <label for=\"ocupacion\">Ocupación</label>
    <input type=\"text\" id=\"ocupacion\">

    <label for=\"campo\">Campo</label>
    <input type=\"text\" id=\"campo\">

    <label for=\"competencias\">Competencias</label>
    <textarea id=\"competencias\"></textarea>

    <label for=\"egresado\">¿Egresado Unillanos?</label>
    <select id=\"egresado\">
        <option value=\"Sí\">Sí</option>
        <option value=\"No\">No</option>
    </select>

    <label for=\"titulo\">Título</label>
    <input type=\"text\" id=\"titulo\">

    <label for=\"universidad_titulo\">Universidad del Título</label>
    <input type=\"text\" id=\"universidad_titulo\">

    <label for=\"virtualidad\">Porcentaje de virtualidad</label>
    <input type=\"number\" id=\"virtualidad\" min=\"0\" max=\"100\">

    <button class=\"btn-interes\" onclick=\"predecir('interes')\">Predecir Interés</button>
    <button class=\"btn-rango\" onclick=\"predecir('rango')\">Predecir Rango</button>

    <div id=\"resultado\" class=\"resultado\"></div>
</div>

<script>
    async function predecir(tipo) {
        const data = {
            sexo: document.getElementById('sexo').value,
            edad: document.getElementById('edad').value,
            ocupacion: document.getElementById('ocupacion').value,
            campo: document.getElementById('campo').value,
            competencias: document.getElementById('competencias').value,
            egresado_unillanos: document.getElementById('egresado').value,
            titulo: document.getElementById('titulo').value,
            universidad_titulo: document.getElementById('universidad_titulo').value,
            porcentaje_virtualidad: document.getElementById('virtualidad').value
        };

        const endpoint = tipo === 'interes' ? '/predecir-interes' : '/predecir-rango';

        try {
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            const result = await res.json();
            document.getElementById('resultado').innerText = `Resultado: ${result.descripcion}`;
        } catch (err) {
            document.getElementById('resultado').innerText = 'Error al procesar la solicitud';
        }
    }
</script>
</body>
</html>
""")
