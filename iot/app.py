from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://iot1234567890-default-rtdb.firebaseio.com/sensores/sucursal1.json"

@app.route("/")
def index():
    response = requests.get(url)
    data = response.json()

    temperatura = data.get("temperatura", "--")
    distancia = data.get("humedad", "--")

    return render_template(
        "index.html",
        temperatura=temperatura,
        distancia=distancia
    )

if __name__ == "__main__":
    app.run(debug=True)