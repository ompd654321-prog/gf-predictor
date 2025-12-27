from flask import Flask, render_template, request
import random

app = Flask(__name__)

# =========================
# GF PREDICTOR
# =========================
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        ch = request.form["name"].lower()

        match ch:
            case "anuj":
                result = "Aaisey logo ki gf nahi hoti 😭"
            case "prathamesh":
                result = "Nothing"
            case "sanket":
                result = "Rashika 💖"
            case "atharva":
                result = "SS 😎"
            case "om":
                result = "Playboy"
            case "prajwal":
                result = "Sakshi"
            case "swarang":
                result = "Jo mile wo sahi"
            case "krishna":
                result = "Secret player 🤫"
            case "sahil":
                result = "Gym lover 💪"
            case _:
                result = "Single hi rahega 🤡"

    return render_template("index.html", result=result)


# =========================
# LOVE CALCULATOR
# =========================
@app.route("/love-calculator", methods=["GET", "POST"])
def love_calculator():
    message = ""

    words = ["Legend 😎", "Lucky ❤️", "Dangerous 😏", "Cute 🤭", "Silent 🤫"]

    if request.method == "POST":
        name = request.form["name"]
        message = f"{name} is {random.choice(words)}"

    return render_template("love.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

