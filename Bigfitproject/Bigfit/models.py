from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    target_weight = models.PositiveSmallIntegerField(validators=[MaxValueValidator(999)], null=True)
    feet = models.PositiveSmallIntegerField(validators=[MaxValueValidator(9)], null=True)
    inches = models.PositiveSmallIntegerField(validators=[MaxValueValidator(11)], null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(choices=SEX_CHOICES, max_length=1, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    phone = models.CharField(max_length=10, null=True)

    @property
    def totalInches(self):
        totalInches = self.feet*12 + self.inches
        return totalInches

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name', 'first_name', 'id']


class WeightTracker(models.Model):

    user = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now_add=True)
    weight = models.PositiveSmallIntegerField(validators=[MaxValueValidator(999)])
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    @property
    def bmi(self):
        inches = self.user.totalInches
        weight = self.weight
        bmi = round((weight / (inches * inches)) * 703.0, 1)
        return bmi

    @property
    def weightStatus(self):
        status = None
        if self.bmi <= 18.5:
            status = "Underweight"
        elif 18.5 <= self.bmi <= 24.9:
            status = "Normal weight"
        elif 25 <= self.bmi <= 29.9:
            status = "Overweight"
        elif self.bmi >= 30:
            status = "Obese"
        return status

    def __str__(self):
        return str(self.weight)

    class Meta:
        ordering = ['user', 'record_date']


class CalorieTracker(models.Model):
    user = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now_add=True)
    calories = models.PositiveSmallIntegerField(validators=[MaxValueValidator(99999)])
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.calories)

    class Meta:
        ordering = ['user', 'record_date']
