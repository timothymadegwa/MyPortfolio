from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('project', views.project, name='project'),
    path('blog', views.blog, name='blog'),
    path('cv', views.cv, name='cv'),
    path('contact', views.contact, name='contact'),
]