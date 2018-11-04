from django.db import models
from django.core.validators import MaxValueValidator


class Account(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email', 'id']


class User(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    target_weight = models.PositiveSmallIntegerField(validators=[MaxValueValidator(999)])
    feet = models.PositiveSmallIntegerField(validators=[MaxValueValidator(9)])
    inches = models.PositiveSmallIntegerField(validators=[MaxValueValidator(11)])
    date_of_birth = models.DateField()
    gender = models.CharField(choices=SEX_CHOICES, max_length=1)
    zip_code = models.CharField(max_length=5)
    insert_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

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
        ordering = ['user', 'user_id', 'record_date']
