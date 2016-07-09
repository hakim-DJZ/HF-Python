import cgi
import cgitb
import athletemodel
import yate

cgitb.enable()

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.header("Athlete:" +
                          athletes[athlete_name].name +
                          ", DOB:" +
                          athletes[athlete_name].dob + "."))
print(yate.para("The top times for this athlete are:"))

top3 = athletes[athlete_name].top3
print(yate.u_list(top3))


print(yate.include_footer({"Home": "/index.html",
                           "Select another athlete.": "generate_list.py"}))



