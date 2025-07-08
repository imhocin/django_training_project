from django.shortcuts import render
from django_training_project.forms import ContactForm


def contact_us_view(request):
    contact_form = ContactForm()

    context = {
        'message2': 'this is contact us page',
        'contact_form': contact_form,
    }
    return render(request, 'contact_us.html', context)
