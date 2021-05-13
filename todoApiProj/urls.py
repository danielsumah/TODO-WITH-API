from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todoapi.urls')),

    # rest framework url
    path('api-auth/', include('rest_framework.urls')),

    #frontend urls
    path('', include('frontend.urls')),

    #accounts url
    path('', include('accounts.urls')),
]
