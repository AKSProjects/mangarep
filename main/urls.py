from django.urls import path
from . import views
from django.urls import path, include
from .views import access_table
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('manga/<int:manga_id>/', views.manga_template, name='manga_detail'),
    path('', views.home, name='home'),
    path('access-table/<int:manga_id>/', access_table, name='access_table'),
    path('access-top-100/', views.access_top_100, name='access_top_100'),
    path('access-top-seinen/', views.access_top_seinen, name='access_top_seinen'),
    path('access-top-shounen/', views.access_top_shounen, name="access_top_shounen"),
    path('access-top-manhua/', views.access_top_manhua, name="access_top_manhua"),
    path('access-top-shoujo/', views.access_top_shoujo, name="access_top_shoujo"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


