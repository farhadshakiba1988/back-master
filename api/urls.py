from django.urls import path
from api.controllers import *

common = [
    path('auth_routes', ComController.auth_routes, name='authRoute'),
    path('fake_chart_data', ComController.fake_chart_data, name='fakeChartData'),
    path('project/notice', ComController.fake_chart_data, name='project/notice'),
    path('forms', ComController.forms, name='forms'),
    path('fake_list', ComController.fake_list, name='fake_list'),
    path('profile/basic', ComController.profile_basic, name='profile/basic'),
    path('profile/advanced', ComController.profile_advanced, name='profile/basic'),
    path('activities', ComController.activities, name='activities'),
    path('notices', ComController.notices, name='notices'),
]

user = [
    path('currentUser', UserController.index, name='currentUser'),
]

rule = [
    path('rule', RuleController.index, name='rule'),
    path('seed', RuleController.seed, name='seed'),
]

urlpatterns = user + rule + common
