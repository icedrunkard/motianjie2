from django.shortcuts import render_to_response
from .models import School, Department,Tutor
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def schools(request):
    schools = School.objects.all()
    return render_to_response('schools/schools.html', locals())


@login_required
def dpts(request, id):
    id = int(id)
    school = School.objects.get(id=id)
    dpts = school.dpts.all()
    return render_to_response('schools/dpts.html', locals())

@login_required
def tutors(request,school_id,dpt_id):
    tutors=Tutor.objects.filter(school_id=school_id,dpt_id=dpt_id)
    return render_to_response('schools/tutors.html', locals())
