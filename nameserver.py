import json
from flask import Flask

app = Flask(__name__)


@app.route('/info', methods=['GET'])
def home():
    componente = "nameserver"
    desc = "prove aos clientes, nomes simplificados para os servers"
    ver = "0.1"
    out = {
        "componente": componente,
        "descricao": desc,
        "versao": ver
    }
    return json.dumps(out)


def main():
    app.run(host='0.0.0.0', port=3001)


if __name__ == "__main__":
    main()
