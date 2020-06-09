from django.urls import path
from django.conf.urls import url
from . import views # current directory

urlpatterns = [
    #path('',views.article_list),
    url('',views.article_list),
]
