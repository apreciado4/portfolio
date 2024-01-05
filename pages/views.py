import django.http
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from contact.models import ContactModel
from contact.forms import ContactForm
from contact.utils import send_email
from projects.models import Project
from experience.models import Position
from skills.models import Skills, Langauges
from django.http import HttpResponse, FileResponse, Http404, HttpResponseServerError


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = ContactModel()
            new_contact.name = form.cleaned_data['name']
            new_contact.email = form.cleaned_data['email']
            new_contact.phone_number = form.cleaned_data['phone_number']
            new_contact.subject = form.cleaned_data['subject']
            new_contact.message = form.cleaned_data['message']

            new_contact.save()

            try:
                send_email(
                    reply_to=new_contact.email,
                    subject=f'Django Contact Me Subject: {new_contact.subject} from {new_contact.name}',
                    content=f'{new_contact.message} \n'
                            f'{new_contact.name} \n'
                            f'{new_contact.phone_number} \n'
                            f'{new_contact.email} \n'
                )
            except:
                raise Http404

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


def server_500(request):
    raise HttpResponseServerError


def server_404(request):
    raise Http404


def success(request):
    return HttpResponse('Success!')
