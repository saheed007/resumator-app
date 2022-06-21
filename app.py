from flask import *
from info import info
from education import education
from exp import expr
from projects import proj
from skills import skills


app = Flask(__name__)
app.register_blueprint(info, url_prefix="")
app.register_blueprint(education, url_prefix="")
app.register_blueprint(expr, url_prefix="")
app.register_blueprint(proj, url_prefix="")
app.register_blueprint(skills, url_prefix="")

app.secret_key = "awsthgnbdfjfdhkujsdgfl2324ks_dfjhgiu345dgfu9r4kjgdfsa3_asdfh"

@app.route("/")
def home():
	return render_template('home.html')

# @app.route("/view")
# def resume():
# 	res = [ f'{x} -->  {y}' for x,y in session.items()] 
# 	# res = [x for x in res1 if len(x) != 0]
# 	return render_template('resume.html', res= res)

@app.route("/view")
def resume():
	res = [ f'{x} -->  {y}' for x,y in session.items()] 
	if "name" in session:
		name = session["name"]
		email = session["email_"]
		address = session["address"]
		phone = session["phone"]
		city = session["city"]
		occup = session["occup"]
		about = session["about"]
		_zip = session["_zip"]
		twitter = session["twitter"]
		linkedin = session["linkedin"]
		other = session["other"]

		if "company1" in session:
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
		else:
			company1 = ''
			role1 = ''
			location1 = '' 
			from1 = '' 
			to1 = '' 
			desc1 = '' 

			company2 = '' 
			role2 = '' 
			location2 = '' 
			from2 = '' 
			to2 = '' 
			desc2 = ''

		if "school1" in session:
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
		else:
			school1 = ''
			course1 = '' 
			cert1 = '' 
			sch_loc1 = '' 
			sch_from1 = '' 
			sch_to1 = '' 
			sch_desc1 = ''

			school2 = ''
			course2 = '' 
			cert2 = '' 
			sch_loc2 = '' 
			sch_from2 = '' 
			sch_to2 = '' 
			sch_desc2 = ''

		if "projtit1" in session:
			projtit1 = session["projtit1"] 
			projdate1 = session["projdate1"] 
			projdesc1 = session["projdesc1"]

			projtit2 = session["projtit2"] 
			projdate2 = session["projdate2"] 
			projdesc2 = session["projdesc2"]
		else:
			projtit1 = '' 
			projdate1 = '' 
			projdesc1 = ''

			projtit2 = '' 
			projdate2 = '' 
			projdesc2 = ''

		if "skill1" in session:
			skill1 = session["skill1"] 
			skill2 = session["skill2"] 
			skill3 = session["skill3"] 
			skill4 = session["skill4"]

			interest1 = session["interest1"] 
			interest2 = session["interest2"] 
			interest3 = session["interest3"]
		else:
			skill1 = '' 
			skill2 = '' 
			skill3 = '' 
			skill4 = ''

			interest1 = '' 
			interest2 = '' 
			interest3 = ''

		flash("Resume successfully generated!", "info")
		flash("You can download your resume using the download button at the end of this page!", "info")
		flash("Or you can go back to edit your resume details!", "info")
		return render_template("resume.html", res= res,\
		 _name = name , _email=email, cty=city, addr = address, occup=occup, _zip= _zip, about = about,\
		 phone = phone, twitter = twitter, linkedin = linkedin, other = other,\
		 company1 = company1, role1=role1, location1 = location1, from1 = from1, to1 = to1, desc1=desc1,\
		 company2 = company2, role2=role2, location2 = location2, from2 = from2, to2 = to2, desc2=desc2,\
		 school1 = school1, course1=course1, cert1=cert1, sch_loc1 = sch_loc1, sch_from1 = sch_from1, sch_to1 = sch_to1, sch_desc1=sch_desc1,\
		 school2 = school2, course2=course2, cert2=cert2, sch_loc2 = sch_loc2, sch_from2 = sch_from2, sch_to2 = sch_to2, sch_desc2=sch_desc2,\
		 projtit1 = projtit1, projdate1 =projdate1, projdesc1 = projdesc1,\
		 projtit2 = projtit2, projdate2 =projdate2, projdesc2 = projdesc2,\
		 skill1 = skill1, skill2 =skill2, skill3 =skill3, skill4 = skill4,\
		 interest1 = interest1, interest2 = interest2, interest3 = interest3)

	else:
		return render_template("resume.html", res= res)

@app.route("/clear6")
def clear6():
	session.clear()
	return redirect(url_for("info.p_info"))

if __name__ == "__main__":
	app.run( debug = True)