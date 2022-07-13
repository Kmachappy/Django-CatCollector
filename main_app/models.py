from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.
print("testing!#@#123")
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()


    def __str__(self):
        return f"name:{self.name} - breed:{self.breed}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id':self.id})
    
    def fed_today(self):
        print(self.feeding_set.all())
        print(len(MEALS))
        print(self.feeding_set.filter(date=date.today()).count())
        # return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
        return self.feeding_set.filter(date=date.today()).count() >= 3
MEALS =(
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        #  only takes one of the choices
        max_length=1, 
        # choices is a tuple
        choices=MEALS,
        # default is the first choice
        default=MEALS[0][0])
    
    # cat is the foreign key
    # on_delete=models.CASCADE means if the cat is deleted, all the feedings will be deleted
    # on_delete=models.SET_NULL means if the cat is deleted, the feeding will be set to null
    # on_delete=models.SET_DEFAULT means if the cat is deleted, the feeding will be set to the default value
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    
    def __str__(self):
        # self.meal is the value of the choice
        # self.get_meal_display() is the display value
        # self.date is the date of the feeding
        return f"{self.get_meal_display()} on {self.date}"
    
    # sort the feedings by date
    # reverse=True means newest first
    # reverse=False means oldest first
    # default_ordering = ['date']
    # default_ordering = ['-date']
    # default_ordering = ['meal']
    # default_ordering = ['-meal']
    # default_ordering = ['cat'] 
    class Meta:
        #  sort the feedings by date

        ordering = ['-date' , '-meal']
        # ordering = ['meal']
        
        verbose_name_plural = "feedings"

    
