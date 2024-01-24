from django.urls import path
from . import views

urlpatterns = [
    path('welcome/',views.welcome,name="welcome"),
    path('login/',views.login,name="login"),
    path('input_login/',views.input_login,name="input_login"),
    path('openticket/',views.openticket,name="openticket"),
    path('open_ticket/',views.open_ticket,name="open_ticket"),
    path('active_ticket/',views.active_ticket,name="active_ticket"),
    path('closed_ticket/',views.closed_ticket,name="closed_ticket"),
    path('closeticket/',views.closeticket,name="closeticket"),
    path('close_ticket/',views.close_ticket,name="close_ticket"),
    path('responder/',views.responder,name="responder"),
    path('support/',views.support,name="support"),
    path('contact/',views.contact,name="contact"),
]
