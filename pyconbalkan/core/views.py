import os

from django.db import models
from django.shortcuts import render

from pyconbalkan.conference.models import Conference, CountDown, MissionStatement
from pyconbalkan.speaker.models import Speaker
from pyconbalkan.sponsors.models import Sponsor, SponsorshipLevel
from .models import Person

def get_person():
    person = Person()
    person.full_name = "Ujjwal K Singh"
    person.email = "ujjwalks01@gmail.com"
    person.linkedin = "https://www.linkedin.com/in/ujjwal-singh-87617637"
    person.facebook = "https://medium.com/@ujjwal.singh"
    person.github = "https://github.com/ujjwalks"
    return person




def home(request):
    # conference = Conference.objects.filter(active=True)

    count_down = CountDown.objects.filter(active=True)
    keynotes = Speaker.objects.filter(active=True, keynote=True).order_by('full_name')

    keystone_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.keystone)
    platinum_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.platinum)
    gold_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.gold)
    silver_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.silver)
    partners = Sponsor.objects.filter(level=SponsorshipLevel.partner)

    mission_statement = MissionStatement.objects.filter(active=True)

    context = {
        'keynotes': keynotes,
        'keystone_sponsors': keystone_sponsors,
        'platinum_sponsors': platinum_sponsors,
        'gold_sponsors': gold_sponsors,
        'silver_sponsors': silver_sponsors,
        'partners': partners,
        'count_down': count_down.first() if count_down else None,
        'mission_statement': mission_statement.first() if mission_statement else None,
        'person': get_person(),
    }
    return render(request, 'home.html', context)




