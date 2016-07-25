from flask import Flask, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # # Alternately, we could make this a Jinja template in `templates/`
    # # and return that result of rendering this, like:
    # #
    return render_template("index.html")

@app.route("/application")
def application_form():
    """Shows applicant data to submit for job opening."""

    return render_template("application-form.html")

@app.route("/application-response", methods=["POST"])
def acknowledge_response():
    """Shows a confirmation page with applicant information"""

    applicant_firstname = request.form.get("firstname")
    applicant_lastname = request.form.get("lastname")
    min_salary_requirement = request.form.get("salaryrequirement")
    desired_position = request.form.get("jobposition")

    print ("this is on the response page", applicant_firstname, 
            applicant_lastname, min_salary_requirement, desired_position)

    return render_template("application-response.html", 
                            applicant_firstname=applicant_firstname,
                            applicant_lastname=applicant_lastname,
                            min_salary_requirement=min_salary_requirement,
                            desired_position=desired_position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(debug=True, host="0.0.0.0")

