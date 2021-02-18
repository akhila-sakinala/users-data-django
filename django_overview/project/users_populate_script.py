import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
django.setup()

from faker import Faker
from users_app.models import Users

f = Faker()
def populate(N=5):
    

    for eachuser in range(N):

        fake_fname = f.name()
        fake_lname = f.name()
        fake_email = f.email()

        usr_obj = Users.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,email=fake_email)[0]
        usr_obj.save()

print("script started")
populate(10)
print("Done")
