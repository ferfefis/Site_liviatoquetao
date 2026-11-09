from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def inicio():
    return render_template("site_base.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/buque")
def buque():
    return render_template("buque.html")


@app.route("/cerimonias")
def cerimonias():
    return render_template("cerimonias.html")


@app.route("/mesa-doces")
def mesa_doces():
    return render_template("mesa_doces.html")


@app.route("/mesa-convidados")
def mesa_convidados():
    return render_template("mesa_convidados.html")


@app.route("/backdroop")
def backdroop():
    return render_template("backdroop.html")


if __name__ == "__main__":
    app.run(debug=True)