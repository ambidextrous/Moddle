import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moddle_project.settings')

import django
django.setup()
from moddle.models import User, Bike

def populate():

	Scarlet_bikes = [{"name": "A cool bike", "boys_bike": False, "adults_bike": True, "description": "This is a cool bike." },]

	Steves_bikes = [{"name": "A normal city bike", "boys_bike": True, "adults_bike": True, "description": "Boring bike but helps you get anywhere." },]


	users = {"sarahGLA": {"full_name": "Sarah Johnson", "email": "sarahGLA@gmail.com", "phone_number":"07443048651", "gender": False, "post_code":"G3 5PE", "bikes": []},
	"biancaBikeLover": {"full_name":"Bianca Dolson", "email":"therealBianca@gmail.com", "phone_number":"074453325650", "gender": False, "post_code":"E2 1DD", "bikes": []},
	"therealScarlett": {"full_name":"Scarlett Johnasson", "email":"therealScarlett@gmail.com", "phone_number":"03476573", "gender": False, "post_code":"AB CD", "bikes": Scarlet_bikes},
	"boringSteve": {"full_name":"Normal Steve", "email":"normal_steve@gmail.com", "phone_number":"1234567", "gender": True, "post_code":"EE EEE", "bikes": Steves_bikes},
	}

	for user, user_data in users.items():
		u = add_user(user, user_data["full_name"], user_data["email"], user_data["phone_number"], user_data["gender"], user_data["post_code"])
		for b in user_data["bikes"]:
			add_bike(b["name"], u, b["boys_bike"], b["adults_bike"], b["description"])

		# Print out the categories we have added.
		for u in User.objects.all():
			for b in Bike.objects.filter(owner=u):
				print("- {0} - {1}".format(str(u), str(b)))

def add_bike(name, user, boys_bike, adults_bike, description):
	b = Bike.objects.get_or_create(name=name, owner=user, boys_bike=boys_bike, adults_bike=adults_bike, description=description)[0]
	b.owner = user
	b.save()
	return b

def add_user(username, full_name, email, phone_number, gender, post_code):
	u = User.objects.get_or_create(username=username, full_name=full_name, email=email, phone_number=phone_number, gender_male=gender, post_code=post_code)[0]
	u.save()
	return u

if __name__ == '__main__':
	print "Starting Rango population script..."
	populate()

