from django.shortcuts import render

from authweb.globals import get_year
from authweb.main.helpers import never_ever_cache
from authweb.realestate.models import Entry


@never_ever_cache
def real_estate_admin(request):
    from authweb.realestate.forms import EntryForm
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry, created = Entry.objects.get_or_create(
                bedrooms=form.cleaned_data['bedrooms'],
                bathrooms=form.cleaned_data['bathrooms'],
                square_feet=form.cleaned_data['square_feet'],
                address=str(form.cleaned_data['address']),
                city=str(form.cleaned_data['city']),
                country=str(form.cleaned_data['country']),
                agency=str(form.cleaned_data['agency']),
                price=str(form.cleaned_data['price']),
            )
            if created:
                entry.image = form.cleaned_data['image']
                entry.save()

            return render(request, 'realestate/home.html', {
                'ver': '1.1.1',
                'current_year': get_year(),
                'entries': Entry.get_entries(),
            })

    else:
        form = EntryForm()

    return render(request, 'realestate/admin.html', {
        'form': form,
        'ver': '1.1.1',
        'current_year': get_year(),
    })


@never_ever_cache
def real_estate_home(request):
    return render(request, 'realestate/home.html', {
        'ver': '1.1.1',
        'current_year': get_year(),
        'entries': Entry.get_entries(),
    })
