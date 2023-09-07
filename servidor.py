from flask import Flask, render_template, jsonify, request
import numpy as np
from joblib import load
import os

# Cargar el modelo
dt = load("dt1.joblib")

# Servidor (backend)
# Generar el servidor (Back-end)
servidorWeb = Flask(__name__)

@servidorWeb.route("/holamundo", methods=['GET'])
# def formulario() # No es necesario que corresponda el nombre de la función con la ruta
def holamundo():
    return render_template('pagina1.html')

# Envío de datos a través de JSON
@servidorWeb.route("/modelo", methods=['POST'])
def modeloPrediccion():
    # Procesar los datos de entrada
    contenido = request.json
    print(contenido)
    datosEntrada = np.array([
        # Se mandan los datos reales de una observación para no tener que mandar todo
            # Solamente para fines demostrativos
        # Los nombres de las columnas en el JSON no necesariamente tienen que corresponer con las columnas del dataframe
            # Siempre y cuando correspondan para que se puedan reconocer en este archivo
        0.88, 0, 2.6, 0.098, 25, 67, 0.9968,
        contenido["pH"],
        contenido["sulphates"],
        contenido["alcohol"]
    ])

    # Utilizar el modelo
    resultado = dt.predict(datosEntrada.reshape(1, -1))

    # return jsonify({"resultado": "Hola"})
    return jsonify({"resultado": str(resultado[0])})

if __name__ == '__main__':
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')