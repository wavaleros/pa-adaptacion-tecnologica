from django import forms
from django.contrib import admin

from django.db import models

# Create your models here.
from django.forms import PasswordInput
from django.utils import timezone


class Student(models.Model):
    username = models.CharField(max_length=60, db_column='username')
    password = models.CharField(max_length=60, db_column='password')
    firstName = models.CharField(max_length=100, db_column='first_name')
    lastName = models.CharField(max_length=100, db_column='last_name')
    email = models.CharField(max_length=100, db_column='email')

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Sport(models.Model):
    name = models.CharField(max_length=60, db_column='name', null=True)
    photo = models.CharField(max_length=300, db_column='photo', null=True)

    def __str__(self):
        return self.name


class SportModality(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, db_column='id_sport', null=True)
    name = models.CharField(max_length=60, db_column='name', null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    sport = models.ForeignKey(Sport, models.CASCADE, db_column='id_sport', null=True)
    sportModality = models.ForeignKey(SportModality, models.CASCADE, db_column='id_sport_modality', null=True)
    videoLink = models.CharField(max_length=100, db_column='video_link')
    eventDate = models.DateField(db_column='event_date', default=timezone.now)
    eventTime = models.TimeField(db_column='event_time', default=timezone.now)

    def __str__(self):
        return self.sport.__str__() + ' ' + self.sportModality.__str__() + ' ' + self.eventDate.__str__() + ' ' + self.eventTime.__str__()


class EventVideoComments(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='id_event', null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='id_student', null=True)
    creationDate = models.DateField(db_column='creation_date', default=timezone.now)
    comment = models.CharField(max_length=500, db_column='comment', null=True)

    def __str__(self):
        return self.event.__str__() + ' ' + self.student.__str__() + ' ' + self.creationDate.__str__()


class Coach(models.Model):
    firstName = models.CharField(max_length=100, db_column='first_name')
    lastName = models.CharField(max_length=100, db_column='last_name')

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Athlete(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, db_column='id_coach', null=True)
    names = models.CharField(max_length=100, db_column='names')
    lastName = models.CharField(max_length=100, db_column='last_name')
    birthDate = models.DateField(db_column='birth_date')
    birthPlace = models.CharField(max_length=100, db_column='birth_place')
    weight = models.FloatField(db_column='weight')
    height = models.FloatField(db_column='height')
    photo = models.CharField(max_length=300, db_column='photo')
    sport = models.ManyToManyField(Sport, through='AthleteSport', through_fields=('athlete', 'sport'))

    def __str__(self):
        return self.names + ' ' + self.lastName


class AthleteSport(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, db_column='id_athlete', null=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, db_column='id_sport', null=True)


class AthleteEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='id_event', null=True)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, db_column='id_athlete', null=True)
    result = models.CharField(max_length=20, db_column='result')

    def __str__(self):
        return self.event.__str__() + ' ' + self.athlete.__str__()


class AthleteEventInline(admin.TabularInline):
    model = AthleteEvent
    extra = 1


class AthleteSportInline(admin.TabularInline):
    model = AthleteSport
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = (AthleteEventInline,)


class AthleteAdmin(admin.ModelAdmin):
    inlines = (AthleteSportInline,)


class SportAdmin(admin.ModelAdmin):
    inlines = (AthleteSportInline,)


class StudentForm(forms.ModelForm):
    widgets = {
        'password': PasswordInput,
    }


class StudentAdmin(admin.ModelAdmin):
    form = StudentForm


class HiddenModelAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False
