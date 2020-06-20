def do_real_estate_demo_reset():
    from django.db import transaction

    try:
        with transaction.atomic():
            from authweb.realestate.models import Entry
            entries = Entry.objects.all()
            if len(entries) > 5:
                from authweb.realestate.models import Entry
                import os
                import shutil

                entries.delete()

                from authweb.config.settings.base import SITE_ROOT
                for root, dirs, files in os.walk(SITE_ROOT + '/authweb/media/images/real-estate'):
                    for f in files:
                        if not f == 'temp_do_not_remove.jpg':
                            print(f)
                            os.unlink(os.path.join(root, f))

                entry = Entry()
                entry.bedrooms = 3
                entry.bathrooms = 2
                entry.square_feet = 200
                entry.address = '9 Hogan St, Green Hill'
                entry.city = 'Canberra'
                entry.country = 'Australia'
                entry.agency = 'Best Rentals'
                entry.price = 500
                entry.image = "static/real-estate/house2.jpg"
                entry.save()
                print(entry)

                entry = Entry()
                entry.bedrooms = 3
                entry.bathrooms = 2
                entry.square_feet = 225
                entry.address = '24 Whitlam St, Blue Hill'
                entry.city = 'Canberra'
                entry.country = 'Australia'
                entry.agency = 'Best Rentals'
                entry.price = 550
                entry.image = "static/real-estate/house3.jpg"
                entry.save()
                print(entry)

                entry = Entry()
                entry.bedrooms = 4
                entry.bathrooms = 3
                entry.square_feet = 250
                entry.address = '199 Fraser St, Red Hill'
                entry.city = 'Canberra'
                entry.country = 'Australia'
                entry.agency = 'Best Rentals'
                entry.price = 600
                entry.image = "static/real-estate/house4.jpg"
                entry.save()
                print(entry)

                entry = Entry()
                entry.bedrooms = 4
                entry.bathrooms = 3
                entry.square_feet = 275
                entry.address = '100 Keating St, Black Hill'
                entry.city = 'Canberra'
                entry.country = 'Australia'
                entry.agency = 'Best Rentals'
                entry.price = 650
                entry.image = "static/real-estate/house5.jpg"
                entry.save()
                print(entry)

                entry = Entry()
                entry.bedrooms = 5
                entry.bathrooms = 3
                entry.square_feet = 300
                entry.address = '51 Blake St, Upper Hill'
                entry.city = 'Canberra'
                entry.country = 'Australia'
                entry.agency = 'Best Rentals'
                entry.price = 700
                entry.image = "static/real-estate/house6.jpg"
                entry.save()
                print(entry)

                from django.core.mail import send_mail
                from authweb.config.settings.base import EMAIL_HOST_USER
                send_mail(
                    'Real estate demo was used and entries reset',
                    'All good',
                    EMAIL_HOST_USER,
                    ['adee.macdowell@gmail.com'],
                    fail_silently=False,
                )
                print('email sent')

    except Exception as e:
        print(999999999)