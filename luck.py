import random as r
luck=str(input("Enter Your Name : "));
n=["Lund","BSDK","BKL","Bhadwa","Bhosri Wala"]

print(r.choice(n), " ",luck);
return render_template("index.html", result=result)
