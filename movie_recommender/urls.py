from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',include('web_app.urls')),
    path('admin/',admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('allauth.urls')),

  ]
