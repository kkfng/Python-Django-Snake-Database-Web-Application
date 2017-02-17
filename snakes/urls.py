from django.conf.urls import url

from snakes import views

urlpatterns = [
    url(r'^$', views.index, name='snakes'),
    url(r'^add/', views.add, name='add_snakes'),
    url(r'^edit/(?P<snake_id>\d+)', views.edit, name='edit_snake'),
    url(r'^delete/(?P<snake_id>\d+)', views.delete),
    url(r'^snake/(?P<snake_id>\d+)', views.view, name='view_snake'),
]