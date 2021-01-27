from django.db import models


class Institution(models.Model):
    name = models.CharField(max_length=900)

    def __str__(self):
        return self.name


class News(models.Model):
    link = models.CharField(max_length=2000)
    content = models.CharField(max_length=3000)
    agency = models.ForeignKey('Institution', on_delete=models.PROTECT)
    type = models.CharField(max_length=400, null=True)
    date_added = models.DateField('data dodania')

    def __str__(self):
        return self.link


class User(models.Model):
    mail = models.CharField(max_length=300)
    date_since = models.DateField('początek subskrypcji')
    interest1 = models.ForeignKey('Institution', on_delete=models.PROTECT,
        related_name='+', null=True)
    interest2 = models.ForeignKey('Institution', on_delete=models.PROTECT,
        related_name='+', null=True)
    interest3 = models.ForeignKey('Institution', on_delete=models.PROTECT,
        related_name='+', null=True)

    def __str__(self):
        return self.mail
