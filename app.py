from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        ch = request.form["name"].lower()

        match ch:
            case "anuj":
                result = "Aaisey logo ki gf nahi hoti, follow back bhi nahi milta 😭"
            case "prathamesh":
                result = "Laddu 🍩"
            case "sanket":
                result = "Rashika 💖"
            case "atharva":
                result = "SS 😎"
            case "om":
                result = "Ha sabhaya sushil mulga aahe 🫡"
            case "hod":
                result = "Sanket yacha tondat ghete ani ha takla aahe 😈"
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
