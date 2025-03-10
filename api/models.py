from django.db import models

class Services(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.number} - {self.name}'

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class About(models.Model):
    image_big = models.ImageField(upload_to='about/')
    image_small = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=512)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class Activity(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'


class SubActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='sub_activities')
    subTitle = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.subTitle


class Projects(models.Model):
    number = models.IntegerField()
    image = models.ImageField(upload_to='projects/')
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class WhatOurClientsSay(models.Model):
    review = models.TextField()
    fullname = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    image = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'What Our Clients Say'
        verbose_name_plural = 'What Our Clients Say'


class GetInContactSection(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Get In Contact Section'
        verbose_name_plural = 'Get In Contact Section'


class ClientsReviews(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    fullname = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    image = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Clients Review'
        verbose_name_plural = 'Clients Reviews'


class ClientsEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Clients Email'
        verbose_name_plural = 'Clients Emails'


class Partners(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'


