from django.urls import path
from . import views

urlpatterns = [
    path('',views.renderTest, name='hello'),
    path('contact/',views.get_name, name='contact'),
    path('<int:year>/<str:month>',views.renderTest)
]