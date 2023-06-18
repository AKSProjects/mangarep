from django.urls import path
from . import views
from django.urls import path, include
from .views import access_table
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('access-table/<int:manga_id>/', access_table, name='access_table'),
    path('access-top-100/', views.access_top_100, name='access_top_100'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


