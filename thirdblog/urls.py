from django.contrib import admin
from django.urls import path
from home.views import index,contact,about,detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('<int:id>/' , detail , name='detail')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
