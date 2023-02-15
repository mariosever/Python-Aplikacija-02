from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

    korisnik = "Ivo Ivić"

    return render_template("index.html", korisnik=korisnik)

@app.route("/proizvodi")
def proizvodi():

    proizvodi = ["grafička", "monitor", "tipkovnica"]

    return render_template("proizvodi.html", proizvodi=proizvodi)

@app.route("/kontakt", methods=["POST"])
def kontakt():

    name = request.form.get("contact-name")

    email = request.form.get("contact-email")

    return render_template("kontakt.html", name=name, email=email)



if __name__ == "__main__":
    app.run(use_reloader=True)