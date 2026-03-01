from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/form")
def form():
	return render_template("form.html")

@app.route("/result")
def result():
	if request.method == "POST":
		return render_template("result.html", placeholder=request.args.get("whatUserTyped"))
	if request.method == "GET":
		return render_template("result.html", placeholder=request.args.get("whatUserTyped"))

if __name__ == '__main__':
	app.run(debug=True)