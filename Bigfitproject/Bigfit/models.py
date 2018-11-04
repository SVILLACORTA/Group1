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

    def __str__(self):
        return str(self.weight)

    class Meta:
        ordering = ['user', 'record_date']
