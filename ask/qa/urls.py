from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^popular/.*$', views.popular, name='popular'),
    re_path(r'^ask/.*$', views.ask, name='ask'),
    re_path(r'^answer/.*$', views.answer, name='answer'),
    re_path(r'^signup/.*$', views.user_signup, name='signup'),
    re_path(r'^login/.*$', views.user_login, name='login'),
    re_path(r'^logout/.*$', views.user_logout, name='logout'),
    re_path(r'^new/.*$', views.test),
    re_path(r'^question/(?P<question_id>[0-9]+)/$', views.question, name='question'),
]