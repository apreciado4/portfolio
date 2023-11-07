from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.http import HttpResponse


# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = ContactForm()
    context = {
            'form': form
    }
    return render(request, 'contact/contact.html', context)


def success(request):
    return HttpResponse('Success!')
