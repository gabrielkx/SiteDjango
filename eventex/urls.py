from django.contrib import admin
from django.urls import include, path
from subscriptions.views import subscribe
urlpatterns = [

    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('inscricao/', subscribe, name='subscribe'),

   # path('inscricao/',subscribe),


]
