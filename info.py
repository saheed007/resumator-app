from flask import *

info = Blueprint("info", __name__, static_folder="static", template_folder = "templates")

@info.route("/p_info", methods = ["POST", "GET"])
def p_info():
	if "name" in session:
		if request.method == "POST":
			name = request.form["name"]
			email_ = request.form["email_"]
			phone = request.form["phone"]
			address = request.form["address"]
			city = request.form["city"]
			occup = request.form["occup"]
			_zip = request.form["zip"]
			about = request.form["about"]
			twitter = request.form["twitter"]
			linkedin = request.form["linkedin"]
			other = request.form["other"]

			session["name"] = name
			session["email_"] = email_
			session["phone"] = phone
			session["address"] = address
			session["city"] = city
			session["occup"] = occup
			session["_zip"] = _zip
			session["about"] = about
			session["twitter"] = twitter
			session["linkedin"] = linkedin
			session["other"] = other


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
			return redirect(url_for("education.edu"))
		else:
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
			return render_template('personal_info.html', name = name, email=email, city=city,\
			 address = address, occup=occup, _zip= _zip, abt = about, phone = phone, \
		 twitter = twitter, linkedin = linkedin, other = other)

	else:
		if request.method == "POST":
			name = request.form["name"]
			email_ = request.form["email_"]
			phone = request.form["phone"]
			address = request.form["address"]
			city = request.form["city"]
			occup = request.form["occup"]
			_zip = request.form["zip"]
			about = request.form["about"]
			twitter = request.form["twitter"]
			linkedin = request.form["linkedin"]
			other = request.form["other"]

			session["name"] = name
			session["email_"] = email_
			session["phone"] = phone
			session["address"] = address
			session["city"] = city
			session["occup"] = occup
			session["_zip"] = _zip
			session["about"] = about
			session["twitter"] = twitter
			session["linkedin"] = linkedin
			session["other"] = other


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

			return redirect(url_for("education.edu"))
		else:
			return render_template('personal_info.html')

@info.route("/clear")
def clear():
	if "name" in session:
		session.pop("name")
		session.pop("email_")
		session.pop("address")
		session.pop("phone")
		session.pop("city")
		session.pop("occup")
		session.pop("about")
		session.pop("_zip")
		session.pop("twitter")
		session.pop("linkedin")
		session.pop("other")
	else:
		pass
	return redirect(url_for("info.p_info"))