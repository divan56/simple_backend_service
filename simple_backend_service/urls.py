# from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('students/', include('students.urls')),
    path('api-auth/', include('rest_framework.urls'))
    #    path('admin/', admin.site.urls),
]
