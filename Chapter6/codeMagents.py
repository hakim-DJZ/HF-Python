sara = get_coach_data('sara2.txt')
(sarah_name,sarah_dob) = sarah.pop(0),sarah.pop(0)

print(sarah_name + "'s fastest times are: " +  str(sorted(set([sanitize(t) for t in sarah]))[0:3]))