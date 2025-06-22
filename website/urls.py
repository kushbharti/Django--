from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout_view, name='logout'),
    path('todo/',include('ToDo_app.urls')),
    path('weather/',include('WeatherApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL ,document_root = settings.STATICFILES_DIRS[0])