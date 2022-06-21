from flask import *

skills = Blueprint("skills", __name__, static_folder="static", template_folder = "templates")

@skills.route("/skills_interest", methods=["POST", "GET"])
def skills_interest():
	if "skill1" in session:
		if request.method == "POST":
			skill1 = request.form["skill1"]
			skill2 = request.form["skill2"]
			skill3 = request.form["skill3"]
			skill4 = request.form["skill4"]

			interest1 = request.form["interest1"]
			interest2 = request.form["interest2"]
			interest3 = request.form["interest3"]


			session["skill1"] = skill1
			session["skill2"] = skill2
			session["skill3"] = skill3
			session["skill4"] = skill4

			session["interest1"] = interest1
			session["interest2"] = interest2
			session["interest3"] = interest3


			skill1 = session["skill1"] 
			skill2 = session["skill2"] 
			skill3 = session["skill3"] 
			skill4 = session["skill4"]

			interest1 = session["interest1"] 
			interest2 = session["interest2"] 
			interest3 = session["interest3"] 
			return redirect(url_for("resume"))
		else:
			skill1 = session["skill1"] 
			skill2 = session["skill2"] 
			skill3 = session["skill3"] 
			skill4 = session["skill4"]

			interest1 = session["interest1"] 
			interest2 = session["interest2"] 
			interest3 = session["interest3"]
			return render_template('skills_interest.html',\
		 skill1 = skill1, skill2 =skill2, skill3 =skill3, skill4 = skill4,\
		 interest1 = interest1, interest2 = interest2, interest3 = interest3)

	else:
		if request.method == "POST":
			skill1 = request.form["skill1"]
			skill2 = request.form["skill2"]
			skill3 = request.form["skill3"]
			skill4 = request.form["skill4"]

			interest1 = request.form["interest1"]
			interest2 = request.form["interest2"]
			interest3 = request.form["interest3"]


			session["skill1"] = skill1
			session["skill2"] = skill2
			session["skill3"] = skill3
			session["skill4"] = skill4

			session["interest1"] = interest1
			session["interest2"] = interest2
			session["interest3"] = interest3



			skill1 = session["skill1"] 
			skill2 = session["skill2"] 
			skill3 = session["skill3"] 
			skill4 = session["skill4"]

			interest1 = session["interest1"] 
			interest2 = session["interest2"] 
			interest3 = session["interest3"]

			return redirect(url_for("resume"))
		else:
			return render_template('skills_interest.html')

@skills.route("/clear5")
def clear5():
	if "skill1" in session:
		session.pop("skill1")
		session.pop("skill2")
		session.pop("skill3")
		session.pop("skill4")
		session.pop("interest1")
		session.pop("interest2")
		session.pop("interest3")
		pass
	return redirect(url_for("skills.skills_interest"))