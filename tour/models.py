
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, default='Горный')

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=100)
    leader = models.CharField(max_length=100, default='Сергей Дмитриевич')
    register_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f'{self.title}-{self.register_date}'


class Person(models.Model):
    choice_tour = models.OneToOneField(Tour, on_delete=models.CASCADE)
    person = models.CharField(max_length=100, default='Сергей Дмитриевич')
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_tour}-{self.person}'


class Comment(models.Model):
    choice_tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.TextField(default='GOOD TOUR')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_tour}-{self.created_at}'
