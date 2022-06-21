from flask import *

education = Blueprint("education", __name__, static_folder="static", template_folder = "templates")

@education.route("/edu", methods=["POST", "GET"])
def edu():
	if "school1" in session:
		if request.method == "POST":
			school1 = request.form["school1"]
			course1 = request.form["course1"]
			cert1 = request.form["cert1"]
			sch_loc1 = request.form["sch_loc1"]
			sch_from1 = request.form["sch_from1"]
			sch_to1 = request.form["sch_to1"]
			sch_desc1 = request.form["sch_desc1"]

			school2 = request.form["school2"]
			course2 = request.form["course2"]
			cert2 = request.form["cert2"]
			sch_loc2 = request.form["sch_loc2"]
			sch_from2 = request.form["sch_from2"]
			sch_to2 = request.form["sch_to2"]
			sch_desc2 = request.form["sch_desc2"]

			session["school1"] = school1
			session["course1"] = course1
			session["cert1"] = cert1
			session["sch_loc1"] = sch_loc1
			session["sch_from1"] = sch_from1
			session["sch_to1"] = sch_to1
			session["sch_desc1"] = sch_desc1

			session["school2"] = school2
			session["course2"] = course2
			session["cert2"] = cert2
			session["sch_loc2"] = sch_loc2
			session["sch_from2"] = sch_from2
			session["sch_to2"] = sch_to2
			session["sch_desc2"] = sch_desc2


			school1 = session["school1"]
			course1 = session["course1"]  
			cert1 = session["cert1"] 
			sch_loc1 = session["sch_loc1"] 
			sch_from1 = session["sch_from1"] 
			sch_to1 = session["sch_to1"] 
			sch_desc1 = session["sch_desc1"]

			school2 = session["school2"]
			course2 = session["course2"] 
			cert2 = session["cert2"] 
			sch_loc2 = session["sch_loc2"] 
			sch_from2 = session["sch_from2"] 
			sch_to2 = session["sch_to2"] 
			sch_desc2 = session["sch_desc2"]
			return redirect(url_for("exp.exp"))
		else:
			school1 = session["school1"]
			course1 = session["course1"] 
			cert1 = session["cert1"] 
			sch_loc1 = session["sch_loc1"] 
			sch_from1 = session["sch_from1"] 
			sch_to1 = session["sch_to1"] 
			sch_desc1 = session["sch_desc1"]

			school2 = session["school2"]
			course2 = session["course2"] 
			cert2 = session["cert2"] 
			sch_loc2 = session["sch_loc2"] 
			sch_from2 = session["sch_from2"] 
			sch_to2 = session["sch_to2"] 
			sch_desc2 = session["sch_desc2"]
			return render_template('education.html',\
			school1 = school1, course1=course1, cert1=cert1, sch_loc1 = sch_loc1,\
			 sch_from1 = sch_from1, sch_to1 = sch_to1, sch_desc1=sch_desc1,\
			 school2 = school2, course2=course2, cert2=cert2, sch_loc2 = sch_loc2,\
			 sch_from2 = sch_from2, sch_to2 = sch_to2, sch_desc2=sch_desc2)

	else:
		if request.method == "POST":
			school1 = request.form["school1"]
			course1 = request.form["course1"]
			cert1 = request.form["cert1"]
			sch_loc1 = request.form["sch_loc1"]
			sch_from1 = request.form["sch_from1"]
			sch_to1 = request.form["sch_to1"]
			sch_desc1 = request.form["sch_desc1"]

			school2 = request.form["school2"]
			course2 = request.form["course2"]
			cert2 = request.form["cert2"]
			sch_loc2 = request.form["sch_loc2"]
			sch_from2 = request.form["sch_from2"]
			sch_to2 = request.form["sch_to2"]
			sch_desc2 = request.form["sch_desc2"]

			session["school1"] = school1
			session["course1"] = course1
			session["cert1"] = cert1
			session["sch_loc1"] = sch_loc1
			session["sch_from1"] = sch_from1
			session["sch_to1"] = sch_to1
			session["sch_desc1"] = sch_desc1

			session["school2"] = school2
			session["course2"] = course2
			session["cert2"] = cert2
			session["sch_loc2"] = sch_loc2
			session["sch_from2"] = sch_from2
			session["sch_to2"] = sch_to2
			session["sch_desc2"] = sch_desc2


			school1 = session["school1"]
			course1 = session["course1"] 
			cert1 = session["cert1"] 
			sch_loc1 = session["sch_loc1"] 
			sch_from1 = session["sch_from1"] 
			sch_to1 = session["sch_to1"] 
			sch_desc1 = session["sch_desc1"]

			school2 = session["school2"]
			course2 = session["course2"] 
			cert2 = session["cert2"] 
			sch_loc2 = session["sch_loc2"] 
			sch_from2 = session["sch_from2"] 
			sch_to2 = session["sch_to2"] 
			sch_desc2 = session["sch_desc2"]

			return redirect(url_for("exp.exp"))
		else:
			return render_template('education.html')

@education.route("/clear2")
def clear2():
	if "school1" in session:
		session.pop("school1")
		session.pop("school2")
		session.pop("course1")
		session.pop("course2")
		session.pop("cert1")
		session.pop("cert2")
		session.pop("sch_loc1")
		session.pop("sch_loc2")
		session.pop("sch_from1")
		session.pop("sch_from2")
		session.pop("sch_to1")
		session.pop("sch_to2")
		session.pop("sch_desc1")
		session.pop("sch_desc2")
	else:
		pass
	return redirect(url_for("education.edu"))