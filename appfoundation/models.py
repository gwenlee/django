from django.db import models

#comment: run 'python manage.py makemigrations' whenever we make a change to a model
#run 'python manage.py migrate' after 'makemigrations' to apply updates in the current instance
# https://sixfeetup.com/blog/django-migrate-or-makemigrations 
#commnet: Always run 'python manage.py makemgirations' and 'python manage.py migrate' togeter, it compensates each other

class Person(models.Model):
    subscription_channel =[
        ('OR', 'Orange'),
        ('AP', 'Apple'),
        ('BA', 'Banana')
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    #Question: modelChoiceField vs forms.ChoiceField
    subscription = models.CharField(max_length=2, choices=subscription_channel, default=subscription_channel[0][0])
    
    #Question: Do you know how to set up many-to-many relationship in Models?
    #comment: Django has __str__ implementations everywhere to print a default string representation of its objects.
    #However, this default is usually not very helpful - hence why we may want to return with __str__ so that it gives a more human friendly name of the object
    def __str__(self):
        #Question: What if the value of first name is None?
        return self.first_name