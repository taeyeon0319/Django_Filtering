from django.shortcuts import render
from .models import Person
from .filters import PersonFilter

from django.core.paginator import Paginator

# Create your views here.

def show_all_persons_page(request):
    context = {}

    filtered_persons = PersonFilter(
        request.GET, 
        queryset=Person.objects.all()
    )

    context['filtered_persons'] = filtered_persons

    paginated_filtered_persons = Paginator(filtered_persons.qs, 2)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_persons.get_page(page_number)

    context['person_page_obj'] = person_page_obj

    return render(request, 'myapp/show_all_persons_page.html', context=context)