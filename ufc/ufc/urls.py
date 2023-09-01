from django.contrib import admin
from django.urls import path

from my_site.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', FightersList.as_view(), name='home'),
    path('', index, name='home'),
    path('about/', about, name='about'),
]
