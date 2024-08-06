from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def batata_frita():
    return render_template("index.html")

@app.route("/contato")
def batata_assada():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)