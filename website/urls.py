from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.base, name='base'),
    path('', views.login, name='login'),
    path('register/',views.register, name='register'),
    path('todo/',include('ToDo_app.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL ,document_root = settings.STATICFILES_DIRS[0])