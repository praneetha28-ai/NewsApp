from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.news_list,name='home'),
    path('scrape/', views.Scrape, name="Scrape"),
    path('detail',view = views.Detail,name='details')
]
