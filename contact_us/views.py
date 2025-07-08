from django.shortcuts import render

def contact_us_view(request):
    context = {
        'message2': 'this is contact us page'
    }
    return render(request, 'contact_us.html', context)