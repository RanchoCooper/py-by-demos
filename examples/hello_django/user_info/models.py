from django.db import models

class Dep(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    dep = models.ForeignKey(Dep, on_delete=models.CASCADE)

    def __str__(self):
        return self.name