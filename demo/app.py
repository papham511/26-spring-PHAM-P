from flask import Flask, render_template, request
import calc # Imports calculation from calc.py


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("form.html")

@app.route("/form")
def form():
	return render_template("form.html")

@app.route("/result")
def result():
	# Get user input from form.html 
	fname = request.args.get("fname")	# retrieve data from form.html
	username = request.args.get("username")
	description = request.args.get("description")
	results = calc.run_analysis(fname, username, description)

	# Route to error.html if no match found
	if results is None:
		return render_template("error.html")
	
	return render_template("result.html", matches=results)

if __name__ == '__main__':
	app.run(debug=True)