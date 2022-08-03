
from django.db import models
from colorful.fields import RGBColorField

class city(models.Model):
    city_name=models.CharField(max_length=30)
    city_image=models.ImageField(upload_to='city_images')
    city_summary=models.CharField(max_length=200)
    city_color= RGBColorField(colors=['#FF0000', '#00FF00', '#0000FF'],default=0)
    updated_date=models.DateTimeField(auto_now=True)
    price=models.IntegerField(default=None)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.city_name

    class Meta:
        ordering = ['city_name',]

class place(models.Model):
    place_name = models.CharField(max_length=40)
    place_intro=models.TextField(default=None)
    place_images=models.ImageField(upload_to='place_images')
    city= models.ForeignKey(city, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' %(self.city,self.place_name)

    class Meta:
        ordering = ['city',]


class car(models.Model):
    car_name=models.CharField(max_length=30)
    car_image=models.ImageField(upload_to='car_images')
    car_rent=models.IntegerField(default=None)

    def __str__(self):
        return self.car_name

    class Meta:
        ordering = ['car_name',]





from django.db import models
from colorful.fields import RGBColorField

class city(models.Model):
    city_name=models.CharField(max_length=30)
    city_image=models.ImageField(upload_to='city_images')
    city_summary=models.CharField(max_length=200)
    city_color= RGBColorField(colors=['#FF0000', '#00FF00', '#0000FF'],default=0)
    updated_date=models.DateTimeField(auto_now=True)
    price=models.IntegerField(default=None)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.city_name

    class Meta:
        ordering = ['city_name',]

class place(models.Model):
    place_name = models.CharField(max_length=40)
    place_intro=models.TextField(default=None)
    place_images=models.ImageField(upload_to='place_images')
    city= models.ForeignKey(city, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' %(self.city,self.place_name)

    class Meta:
        ordering = ['city',]


class car(models.Model):
    car_name=models.CharField(max_length=30)
    car_image=models.ImageField(upload_to='car_images')
    car_rent=models.IntegerField(default=None)

    def __str__(self):
        return self.car_name

    class Meta:
        ordering = ['car_name',]




