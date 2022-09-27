from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greet():
	a=flash("Hi " + str(request.form['name_input']) + ", great to see you " + chr(0x2665))
	return render_template("index.html",message=a)


if __name__ == "__main__":
    app.run()
