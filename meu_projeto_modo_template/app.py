import datetime

from flask import Flask, render_template

app = Flask("meu_projeto")

@app.route("/data_atual")
def data_atual():
    return render_template("data_atual.html", data_atual=datetime.date.today().strftime('%A'))


app.run(debug=True)