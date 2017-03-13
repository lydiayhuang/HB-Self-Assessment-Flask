from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route('/')
def start_here():

	return render_template('index.html')

@app.route('/application-form')
def app_form():
	# used werd job to test the drop down was correct
	jobs = ['software engineer','QA engineer','Product Manager','werd job']
	#pass in the jobs variable at the end here
	return render_template("app-form.html",jobs=jobs)

#kept on messing up here until I read the lecture that the correct syntax for POST method in a decorator is methods=['POST']. Also, I decided to be uninventive and passed in application-response instead of application-success.
@app.route('/application-response', methods=['POST'])
def app_sucess():

	# request.args.get('name') is for get method
	firstname = request.form.get('firstname')
	lastname = request.form.get('lastname')
	salary = request.form.get('quantity')
	job = request.form.get('jobjob')
	# print job
	#took this from madlibs lab to pass in these variables into application-response.html.
	return render_template("application-response.html", firstname=firstname, lastname=lastname, salary=salary, job=job)





if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
