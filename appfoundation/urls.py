from django.urls import path
from . import views

urlpatterns = [
    path('',views.renderTest, name='hello'),
    path('contact/',views.Person_detail, name='contact'),
    path('subscribe/',views.Subscribe, name='subscribe'),
    #Comment: Do you know 'Path converters' in django
    path('<int:year>/<str:month>',views.renderTest)
]