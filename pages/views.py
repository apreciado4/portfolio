from django.shortcuts import render, redirect
from contact.forms import ContactForm
from projects.models import Project
from experience.models import Position
from skills.models import Skills, Langauges
from django.http import HttpResponse, FileResponse, Http404


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = ContactForm()

    projects = Project.objects.all()
    positions = Position.objects.all()
    skills = Skills.objects.all()
    languages = Langauges.objects.all()
    context = {
        'form': form,
        'projects': projects,
        'positions': positions,
        'skills': skills,
        'languages': languages,
    }
    return render(request, 'pages/home.html', context)


def resume(request):
    try:
        return FileResponse(open('static/pdf/TestPDF.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


def success(request):
    return HttpResponse('Success!')
