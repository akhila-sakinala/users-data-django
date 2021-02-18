import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')


import django
django.setup()

## Fake POP script
import random
from app_1.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['search','social']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t 

def populate(N=5):
    for entry in range(N):

        # get topic for entry
        top = add_topic()

        # fake data for web
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_data = fakegen.date()

        # create new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        accrec = AccessRecord.objects.get_or_create(name=webpg,date=fake_data)


print("Populating script")
populate(10)
print("Done")

