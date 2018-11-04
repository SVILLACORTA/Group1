from django.db import models


class User(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    target_weight = models.PositiveSmallIntegerField()
    feet = models.PositiveSmallIntegerField()
    inches = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(choices=SEX_CHOICES, max_length=1)
    zip_code = models.CharField(max_length=5)
    email = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name', 'first_name', 'id']


class WeightTracker(models.Model):
    user = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE)
    record_date = models.DateField(auto_now_add=True)
    weight = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.weight)

    class Meta:
        ordering = ['user', 'user_id', 'record_date']
