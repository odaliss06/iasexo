from flask import Flask, render_template, request

app = Flask(__name__)

def ia_responder(pregunta):
    pregunta = pregunta.lower()
    if "hola" in pregunta:
        return "¡Hola! ¿En qué puedo ayudarte?"
    elif "adiós" in pregunta:
        return "¡Hasta luego! 😊"
    elif "nombre" in pregunta:
        return "Soy una IA creada por ti. 😄"
    else:
        return "Lo siento, no entendí tu pregunta."

@app.route("/", methods=["GET", "POST"])
def index():
    respuesta = ""
    if request.method == "POST":
        pregunta = request.form["pregunta"]
        respuesta = ia_responder(pregunta)
    return render_template("index.html", respuesta=respuesta)

if __name__ == "__main__":
    app.run(debug=True)
