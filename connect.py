import pycps, time

def connect_db():
	try:
		return pycps.Connection('tcp://cloud-us-0.clusterpoint.com:9007', 'skylld', 'kristian.guevara@live.com', '8ZBLaFFZig', '101023')
	except pycps.ConnectionError:
		return "Can't reach the server!"


#LOAD ALL ENTITIES HERE FIRST

def insert_user(username, password, firstname, lastname, middlename="a", typeid = "1", birthday="", \
	telephonenumber = "0", cellphone = "0", nationality = "none", datejoined="0", totaljobsdone=0, \
	picture="/", isactivated=1):
	return '<document><id>'+ str(int(round(time.time()))) +'</id>' \
		'<users>'\
		'<id>' + str(int(round(time.time()))) + '</id>'\
		'<username>'+ str(username) +'</username>' \
		'<password>'+ str(password) +'</password>' \
		'<firstname>'+ str(firstname) +'</firstname>' \
		'<middlename>'+ str(middlename) +'</middlename>' \
		'<lastname>'+ str(lastname) +'</lastname>'\
		'<typeid>'+ str(typeid) +'</typeid>' \
		'<birthday>'+ str(birthday) +'</birthday>' \
		'<telephonenumber>'+ str(telephonenumber) +'</telephonenumber>' \
		'<cellphone>'+ str(cellphone) +'</cellphone>' \
		'<nationality>'+ str(nationality) +'</nationality>' \
		'<datejoined>'+ str(datejoined) +'</datejoined>' \
		'<totaljobsdone>'+ str(totaljobsdone) +'</totaljobsdone>' \
		'<picture>'+ str(picture) +'</picture>' \
		'<isactivated>'+ str(isactivated) +'</isactivated>' \
		'</users></document>'

def insert_user_description():
	return '<document><id>'+ str(int(round(time.time()))) +'</id>' \
	'<userdesc>'\
	'<id>' + str(int(round(time.time()))) + '</id>'\
	'<userid></userid>' \
	'<jobtitle></jobtitle>' \
	'<durationstart></durationstart>' \
	'<city></city>' \
	'<country></country>' \
	'<subdivision></subdivision>' \
	'<aboutme></aboutme>' \
	'<educlevel></educlevel>' \
	'<points></points>' \
	'<ratingave></ratingave>' \
	'</userdesc></document>'

def insert_usert_skills():
	return '<document><id>'+ str(int(round(time.time()))) +'</id>' \
	'<userskills>'\
	'<id>' + str(int(round(time.time()))) + '</id>'\
	'<userid></userid>' \
	'<skills></skills>' \
	'<userskills></document>'

def insert_user_type():
	return '<document><id>'+ str(int(round(time.time()))) +'</id>' \
	'<usertype>'\
	'<id>' + str(int(round(time.time()))) + '</id>'\
	'<type></type>' \
	'<usertype></document>'

def insert_testimonty():
	return '<document><id>'+ str(int(round(time.time()))) +'</id>' \
	'<testimony>'\
	'<id>' + str(int(round(time.time()))) + '</id>'\
	'<rating></rating>' \
	'<comment></comment>' \
	'<ratedby></ratedby>' \
	'<testimony></document>' 

def register_user(username, password):
	message=""
	user = insert_user(username, password, "Juan", "Dela Cruz")
	try:
		connect_db().insert(user, fully_formed=True)
		return "User Successfully Registered!"
	except pycps.APIError as e:
		return e


