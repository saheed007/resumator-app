from flask import *

expr = Blueprint("exp", __name__, static_folder="static", template_folder = "templates")

@expr.route("/exp", methods=["POST", "GET"])
def exp():
	if "company1" in session:
		if request.method == "POST":
			company1 = request.form["company1"]
			role1 = request.form["role1"]
			location1 = request.form["location1"]
			from1 = request.form["from1"]
			to1 = request.form["to1"]
			desc1 = request.form["desc1"]

			company2 = request.form["company2"]
			role2 = request.form["role2"]
			location2 = request.form["location2"]
			from2 = request.form["from2"]
			to2 = request.form["to2"]
			desc2 = request.form["desc2"]

			session["company1"] = company1
			session["role1"] = role1
			session["location1"] = location1
			session["from1"] = from1
			session["to1"] = to1
			session["desc1"] = desc1

			session["company2"] = company2
			session["role2"] = role2
			session["location2"] = location2
			session["from2"] = from2
			session["to2"] = to2
			session["desc2"] = desc2


			company1 = session["company1"] 
			role1 = session["role1"] 
			location1 = session["location1"] 
			from1 = session["from1"] 
			to1 = session["to1"] 
			desc1 = session["desc1"] 

			company2 = session["company2"] 
			role2 = session["role2"] 
			location2 = session["location2"] 
			from2 = session["from2"] 
			to2 = session["to2"] 
			desc2 = session["desc2"]
			return redirect(url_for("projects.projects"))
		else:
			company1 = session["company1"] 
			role1 = session["role1"] 
			location1 = session["location1"] 
			from1 = session["from1"] 
			to1 = session["to1"] 
			desc1 = session["desc1"] 

			company2 = session["company2"] 
			role2 = session["role2"] 
			location2 = session["location2"] 
			from2 = session["from2"] 
			to2 = session["to2"] 
			desc2 = session["desc2"]
			return render_template('experience.html',\
		 company1 = company1, role1=role1, location1 = location1, from1 = from1, to1 = to1, desc1=desc1,\
		 company2 = company2, role2=role2, location2 = location2, from2 = from2, to2 = to2, desc2=desc2)
	else:
		if request.method == "POST":
			company1 = request.form["company1"]
			role1 = request.form["role1"]
			location1 = request.form["location1"]
			from1 = request.form["from1"]
			to1 = request.form["to1"]
			desc1 = request.form["desc1"]

			company2 = request.form["company2"]
			role2 = request.form["role2"]
			location2 = request.form["location2"]
			from2 = request.form["from2"]
			to2 = request.form["to2"]
			desc2 = request.form["desc2"]

			session["company1"] = company1
			session["role1"] = role1
			session["location1"] = location1
			session["from1"] = from1
			session["to1"] = to1
			session["desc1"] = desc1

			session["company2"] = company2
			session["role2"] = role2
			session["location2"] = location2
			session["from2"] = from2
			session["to2"] = to2
			session["desc2"] = desc2


			company1 = session["company1"] 
			role1 = session["role1"] 
			location1 = session["location1"] 
			from1 = session["from1"] 
			to1 = session["to1"] 
			desc1 = session["desc1"] 

			company2 = session["company2"] 
			role2 = session["role2"] 
			location2 = session["location2"] 
			from2 = session["from2"] 
			to2 = session["to2"] 
			desc2 = session["desc2"]

			return redirect(url_for("projects.projects"))
		else:
			return render_template('experience.html')

@expr.route("/clear3")
def clear3():
	if "company1" in session:
		session.pop("company1")
		session.pop("company2")
		session.pop("role1")
		session.pop("role2")
		session.pop("location1")
		session.pop("location2")
		session.pop("from1")
		session.pop("from2")
		session.pop("to1")
		session.pop("to2")
		session.pop("desc1")
		session.pop("desc2")
	else:
		pass 
	return redirect(url_for("exp.exp"))