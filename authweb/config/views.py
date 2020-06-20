from __future__ import unicode_literals


def view_page(request, url):

    if url == 'real-estate-home':
        from authweb.realestate.views import real_estate_home
        x = real_estate_home(request=request)
        if x:
            return x

    if url == 'real-estate-admin':
        from authweb.realestate.views import real_estate_admin
        x = real_estate_admin(request=request)
        if x:
            return x