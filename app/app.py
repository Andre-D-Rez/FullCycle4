from flask import Flask, request
from markupsafe import escape # <--- Importamos a proteção contra XSS

app = Flask(__name__)

@app.route('/health-check')
def health_check():
    return "<h1>Hello, I'm Alive!</h1>"

@app.route('/hello')
def hello():
    name = request.args.get("name")

    if not name:
        return "Nome não informado", 400
    else:
        # Usamos o escape() aqui para blindar a variável "name"
        return f"Hello, {escape(name)}!" # nosemgrep

if __name__ == "__main__": # pragma: no cover
    # Deixamos apenas o app.run() padrão, sem o modo debug
    app.run() # nosemgrep