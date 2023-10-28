import datetime

from flask import Flask

app = Flask("meu_projeto")

@app.route("/data_atual")
def data_atual():
    return f"hoje é {datetime.date.today().strftime('%A')}<button>clique-me</button>"


app.run(debug=True)