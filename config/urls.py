from django.contrib import admin
from django.urls import path
from frontend import views  # 👈 import from frontend now

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
