from flask import Flask, render_template, request
import random as r

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        ch = request.form["name"].lower()

        match ch:
            case "anuj":
                result = "Pehle follow Back mang "
            case "prathamesh":
                result = "Virat Kohli & Jhat farakj nahi Padta Ladkiyo ke baare me"
            case "sanket":
                result = "Rashika 💖 & ",ch
            case "atharva":
                result = "SS 😎 & ",AK
            case "om":
                result = "Laddu Paglu  or Playboy & Iski GF bolti he ye 10 sec se jyada nahi tikta peech pe"
            
            case "prajwal":
                result = "sakshi"
            case "swarang":
                result = "jo mile wo sahi sari duniya apni hey"
            case "krishna":
                result = "ye bade chupe rustom hey, inka kisiko pata nahi"
            case "sahil":
                result = "isko gym jana pasand hey ladkikyo me intrest nahi hey"
            case _:
                result = "Chutiya he kya saale,Jake Mia Khalifa dekh Wahi tera sabkuchh he🤡"

    luck=str(input("Enter Your Name : "));
n=["Lund","BSDK","BKL","Bhadwa","Bhosri Wala"]

print(r.choice(n), " ",luck);
    
            

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
