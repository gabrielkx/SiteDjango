from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('inscricao/', include('subscriptions.urls')),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),

]
