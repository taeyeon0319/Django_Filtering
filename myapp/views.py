from django.shortcuts import render
from .models import Person
from .filters import PersonFilter

# Create your views here.

def show_all_persons_page(request):
    context = {}

    filtered_persons = PersonFilter(
        request.GET, 
        queryset=Person.objects.all()
    )

    context['filtered_persons'] = filtered_persons

    return render(request, 'myapp/show_all_persons_page.html', context=context)