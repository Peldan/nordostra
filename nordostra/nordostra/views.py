from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from narvaro.models import Person, Session
import datetime
# Create your views here.
def percent(request, session):
    session = Session.objects.get(id = session)
    s = Session.objects.all()
    s_id = []
    persons = Person.objects.all().count()
    s_date = []
    session_attendees = session.persons.count()
    antalfk = Person.objects.filter(kurs = 'FK').count()
    antalgk = Person.objects.filter(kurs = 'GK').count()
    antallk = Person.objects.filter(kurs = 'LK').count()
    for i in s:
        s_id.append(i.id)
        s_date.append(i)
    return render_to_response('narvaro/ost.html',{'session':session.date, 'percent':session_attendees * 100 / persons, 'fk':antalfk, 'gk': antalgk, 'lk': antallk, 'sesdir': s_id, 'ses': s_date})


def home(request):
    s = list(Session.objects.all())
    persons = Person.objects.all().count()
    antalfk = Person.objects.filter(kurs = 'FK').count()
    antalgk = Person.objects.filter(kurs = 'GK').count()
    antallk = Person.objects.filter(kurs = 'LK').count()
    s_id = map(lambda session: session.id, s)
    s_date = [session.date for session in s]
    for i in s:
        s_id.append(i.id)
        s_date.append(i.date)

    return render_to_response('narvaro/ostbackup.html',{'gk': antalgk, 'fk': antalfk, 'lk': antallk, 'sesdir': s_id, 'ses': s_date, 's': s, 'indien': i.id, 'i': i})
        


