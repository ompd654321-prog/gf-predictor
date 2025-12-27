from flask import Flask, render_template, request
import random as r

app = Flask(__name__)

# =========================
# GF PREDICTOR (EXISTING)
# =========================
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        ch = request.form["name"].lower()

        match ch:
            case "anuj":
                result = "Aaisey logo ki gf nahi hoti, follow back bhi nahi milta 😭"
            case "prathamesh":
                result = "Nothing"
            case "sanket":
                result = "Rashika 💖"
            case "atharva":
                result = "SS 😎"
            case "om":
                result = "Playboy"
            
            case "prajwal":
                result = "sakshi"
            case "swarang":
                result = "jo mile wo sahi sari duniya apni hey"
            case "krishna":
                result = "ye bade chupe rustom hey, inka kisiko pata nahi"
            case "sahil":
                result = "isko gym jana pasand hey ladkikyo me intrest nahi hey"
            case _:
                result = "Ye chakke hey 🤡"

    return render_template("index.html", result=result)


# =========================
# LOVE CALCULATOR (NEW)
# =========================
@app.route("/love-calculator", methods=["GET", "POST"])
def love_calculator():
   arr=["Lund","bsdk","Bhadwa","Randwa","BKL","Chhakka","Bhadkhau"];
   n=str(input("Enter Your Name : "))
   print(n," ",r.choice(arr));
love_calculator()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

