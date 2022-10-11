from atexit import register
from re import M
from django.urls import path
from .Api_views import *
from .views import *
# from .state import *
# from .country import *
# from .distric import *
urlpatterns = [
    # path("country_data",country_data),
    # path("state_data",state_data),
    # path("distric_data",distric_data),
    # path("register",Master.register),
    # path("country/<int:id>",country.as_view())
    # path('test',Test_api.as_view()),
    # path('test/<int:id>',Test_api.as_view())
    # path("person",Master.persson)
    # Web_pages
    path("user_register",Master.user_register,name="master_register"),
    path("login",Master.login,name="login"),
    path("home",Master.home,name="home"),
    path("view",Master.view,name="view"),
]