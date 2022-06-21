from flask import *

proj = Blueprint("projects", __name__, static_folder="static", template_folder = "templates")

@proj.route("/projects", methods=["POST", "GET"])
def projects():
	if "projtit1" in session:
		if request.method == "POST":
			projtit1 = request.form["projtit1"]
			projdate1 = request.form["projdate1"]
			projdesc1 = request.form["projdesc1"]

			projtit2 = request.form["projtit2"]
			projdate2 = request.form["projdate2"]
			projdesc2 = request.form["projdesc2"]

			session["projtit1"] = projtit1
			session["projdate1"] = projdate1
			session["projdesc1"] = projdesc1

			session["projtit2"] = projtit2
			session["projdate2"] = projdate2
			session["projdesc2"] = projdesc2

			projtit1 = session["projtit1"] 
			projdate1 = session["projdate1"] 
			projdesc1 = session["projdesc1"]

			projtit2 = session["projtit2"] 
			projdate2 = session["projdate2"] 
			projdesc2 = session["projdesc2"]
			return redirect(url_for("skills.skills_interest"))
		else:
			projtit1 = session["projtit1"] 
			projdate1 = session["projdate1"] 
			projdesc1 = session["projdesc1"]

			projtit2 = session["projtit2"] 
			projdate2 = session["projdate2"] 
			projdesc2 = session["projdesc2"]
			return render_template('projects.html',\
		 projtit1 = projtit1, projdate1 =projdate1, projdesc1 = projdesc1,\
		 projtit2 = projtit2, projdate2 =projdate2, projdesc2 = projdesc2)

	else:
		if request.method == "POST":
			projtit1 = request.form["projtit1"]
			projdate1 = request.form["projdate1"]
			projdesc1 = request.form["projdesc1"]

			projtit2 = request.form["projtit2"]
			projdate2 = request.form["projdate2"]
			projdesc2 = request.form["projdesc2"]

			session["projtit1"] = projtit1
			session["projdate1"] = projdate1
			session["projdesc1"] = projdesc1

			session["projtit2"] = projtit2
			session["projdate2"] = projdate2
			session["projdesc2"] = projdesc2


			projtit1 = session["projtit1"] 
			projdate1 = session["projdate1"] 
			projdesc1 = session["projdesc1"]

			projtit2 = session["projtit2"] 
			projdate2 = session["projdate2"] 
			projdesc2 = session["projdesc2"]

			return redirect(url_for("skills.skills_interest"))
		else:
			return render_template('projects.html')

@proj.route("/clear4")
def clear4():
	if "projtit1" in session:
		session.pop("projtit1")
		session.pop("projtit2")
		session.pop("projdate1")
		session.pop("projdate2")
		session.pop("projdesc1")
		session.pop("projdesc2")
		pass
	return redirect(url_for("projects.projects")) 