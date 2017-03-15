import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moddle_project.settings')

import django
django.setup()
from moddle.models import User, UserProfile, Bike

def populate():

    sarahGLAs_bikes = [{"name": "Ladies Country Bike", "category":"Cross Country", "bike_gender": "Womens", "bike_age": "Adults", "description": "This rustic old bike will make a cycle through the countryside that much better. Comes with a padded seat and a front basket.", "bike_picture":"bikes/sarahGLA/bike-190483_1280.jpg"},]
    biancaBikeLovers_bikes = [{"name": "Stylish City Bike", "category":"City Bike", "bike_gender": "Mens", "bike_age": "Adults", "description": "My trusty city bike. It has a bell, front basket, front light, and a rear carrier. It's quite a big bike so suitable for a tall person. Ignore the flat tire, that has since been fixed!!", "bike_picture":"bikes/biancaBikeLover/amsterdam-1788167_1280.jpg"},
                                {"name": "Medium Sized City Bike", "category":"City Bike", "bike_gender": "Mens", "bike_age": "Adults", "description": "This simple city bike is slightly smalelr than my other one. Comes with front and rear lights.", "bike_picture":"bikes/biancaBikeLover/bike-1637234_1280.jpg"},]
    scarlets_bikes = [{"name": "Hardtail Cross Country Bike", "category":"Cross Country", "bike_gender": "Womens", "bike_age": "Adults", "description": "My brand new cross country bike. It comes with front suspension and a handy front basket!", "bike_picture":"bikes/therealScarlett/bicycle-788733_1280.jpg"},]
    steves_bikes = [{"name": "Bulls Mountainbike", "category":"Mountainbike", "bike_gender": "Mens", "bike_age": "Adults", "description": "Excellent bike for getting round the countryside. Comes with front suspension, a padlock and a stand. Watch out for the disk brakes as they are very strong.", "bike_picture":"bikes/boringSteve/bicycle-1834265_1280.jpg"},]

    users = {"sarahGLA": {"price_per_day":5.0, "about_me":"My friend told me about this website, if you want to know more about my bike just contact me.", "first_name": "Sarah", "last_name": "Johnson", "email": "sarahGLA@gmail.com", "phone_number":"07443048651", "gender": "Female", "post_code":"G3 5PE", "longitude":-4.327204, "latitude":55.883214, "profile_picture":"profile_pictures/sarahGLA/sarah-15723_1280.jpg", "bikes": sarahGLAs_bikes},
    "biancaBikeLover": {"price_per_day":100.0, "about_me":"City cycling is the best kind of cycling.", "first_name":"Bianca", "last_name": "Dolson", "email":"therealBianca@gmail.com", "phone_number":"074453325650", "gender": "Female", "post_code":"E2 1DD", "longitude":-3.950891, "latitude":56.118095, "profile_picture":"profile_pictures/biancaBikeLover/portrait-1243972_1280.jpg", "bikes": biancaBikeLovers_bikes},
    "therealScarlett": {"price_per_day":12.0, "about_me":"I cycle to the farmers market every Sunday.", "first_name":"Scarlett", "last_name": "Johnasson", "email":"therealScarlett@gmail.com", "phone_number":"03476573", "gender": "Female", "post_code":"AB CD", "longitude":-4.200372, "latitude":57.476331, "profile_picture":"profile_pictures/therealScarlett/scarlett-1280445_1280.jpg", "bikes": scarlets_bikes},
    "boringSteve": {"price_per_day":10.0, "about_me":"I like to mountainbike a lot and enjoy sunsets.", "first_name":"Steve", "last_name": "Normal", "email":"normal_steve@gmail.com", "phone_number":"1234567", "gender": "Male", "post_code":"EE EEE", "longitude":-0.106288, "latitude":51.522884, "profile_picture":"profile_pictures/boringSteve/man-103041_1280.jpg", "bikes": steves_bikes},
    }

    for username, user_data in users.items():
        profile = add_user(username, user_data["about_me"], user_data["first_name"], user_data["last_name"], user_data["email"], user_data["phone_number"], user_data["gender"], user_data["post_code"], user_data["longitude"], user_data["latitude"], user_data["profile_picture"])
        for bike in user_data["bikes"]:
            add_bike(bike["name"], profile, bike["category"], bike["bike_gender"], bike["bike_age"], bike["description"], bike["bike_picture"])

        # Print out the users and bikes we have added.
        for user in User.objects.all():
            for bike in Bike.objects.filter(owner=profile):
                print("- {0} - {1}".format(str(profile), str(bike)))

def add_bike(name, profile, category, bike_gender, bike_age, description, bike_picture):
    bike = Bike.objects.get_or_create(name=name, owner=profile, category=category, bike_gender=bike_gender, bike_age=bike_age, description=description, bike_picture=bike_picture)[0]
    bike.owner = profile
    bike.save()
    return bike

def add_user(username, about_me, first_name, last_name, email, phone_number, gender, post_code, longitude, latitude, profile_picture):
    user = User.objects.get_or_create(username=username, first_name=first_name, last_name=last_name, email=email)[0]
    user.set_password("moddle123")
    user.save()
    profile = UserProfile.objects.get_or_create(about_me=about_me, user=user, phone_number=phone_number, gender=gender, post_code=post_code, longitude=longitude, latitude=latitude, profile_picture=profile_picture)[0]
    profile.save()
    return profile

if __name__ == '__main__':
    print "Starting Moddle population script..."
    populate()
