from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=100)
    first_dish = models.IntegerField()
    second_dish = models.IntegerField()
    third_dish = models.IntegerField()
    fourth_dish = models.IntegerField()
    fifth_dish = models.IntegerField()
    food_list = [{'rating':first_dish, 'foods':['mexican','taco','bean','chile','burrito','asada','pastor']},
                 {'rating':second_dish, 'foods':['italian','pasta','pizza']},
                 {'rating':third_dish, 'foods':['american','burger','hot dog','steak','beer','wine']},
                 {'rating':fourth_dish, 'foods':['japanese','sushi','ramen','teriyaki']},
                 {'rating':fifth_dish, 'foods':['chinese','chowmein','dumplings','fried rice','noodles','duck']},]
    def __str__(self):
        return self.firs_name + self.last_name


class Restaurant(models.Model):
    google_id = models.CharField(max_length=100)
    user_rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_rating
