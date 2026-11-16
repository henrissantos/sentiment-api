from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Sentiment API está funcionando!"

@app.route("/analisar", methods=["POST"])
def analisar():
    dados = request.get_json()

    texto = dados.get("texto")

    if texto is None:
        return {"erro": "O campo 'texto' é obrigatório"}, 400

    return {"mensagem": f"Texto recebido: {texto}"}

@app.route("/status", methods=["GET"])
def status():
    return "API online!"

if __name__ == "__main__":
    app.run(debug=True)

