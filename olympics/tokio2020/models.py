from django import forms
from django.contrib import admin

from django.db import models

# Create your models here.
from django.forms import PasswordInput


class Student(models.Model):
    username = models.CharField(max_length=60, db_column='username')
    password = models.CharField(max_length=60, db_column='password')
    firstName = models.CharField(max_length=100, db_column='first_name')
    lastName = models.CharField(max_length=100, db_column='last_name')
    email = models.CharField(max_length=100, db_column='email')

    def __str__(self):
        return self.firstName + ' ' + self.lastName

    class Meta:
        managed = False
        db_table = u'"Student\'sTables\".\"students"'


class Sport(models.Model):
    name = models.CharField(max_length=60, db_column='name')
    photo = models.CharField(max_length=300, db_column='photo')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = u'"Athlete\'sTables\".\"sports"'


class SportModality(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, db_column='id_sport')
    name = models.CharField(max_length=60, db_column='name')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = u'"Athlete\'sTables\".\"sport_modalities"'


class Event(models.Model):
    sport = models.ForeignKey(Sport, models.CASCADE, db_column='id_sport')
    sportModality = models.ForeignKey(SportModality, models.CASCADE, db_column='id_sport_modality')
    videoLink = models.CharField(max_length=100, db_column='video_link')
    eventDate = models.DateField(db_column='event_date')
    eventTime = models.TimeField(db_column='event_time')

    def __str__(self):
        return self.sport.__str__() + ' ' + self.sportModality.__str__() + ' ' + self.eventDate.__str__() + ' ' + self.eventTime.__str__()

    class Meta:
        managed = False
        db_table = u'"Event\'sTables\".\"events"'


class EventVideoComments(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='id_event')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='id_student')
    creationDate = models.DateField(db_column='creation_date')
    comment = models.CharField(max_length=500, db_column='comment')

    def __str__(self):
        return self.event.__str__() + ' ' + self.student.__str__() + ' ' + self.creationDate.__str__()

    class Meta:
        managed = False
        db_table = u'"Student\'sTables\".\"event_video_comments"'


class Coach(models.Model):
    firstName = models.CharField(max_length=100, db_column='first_name')
    lastName = models.CharField(max_length=100, db_column='last_name')

    def __str__(self):
        return self.firstName + ' ' + self.lastName

    class Meta:
        managed = False
        db_table = u'"Athlete\'sTables\".\"coaches"'


class Athlete(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, db_column='id_coach')
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

    class Meta:
        managed = False
        db_table = u'"Athlete\'sTables\".\"athletes"'


class AthleteSport(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, db_column='id_athlete')
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, db_column='id_sport')

    class Meta:
        managed = False
        db_table = u'"Athlete\'sTables\".\"athletes_sports"'


class AthleteEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='id_event')
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, db_column='id_athlete')
    result = models.CharField(max_length=20, db_column='result')

    def __str__(self):
        return self.event.__str__() + ' ' + self.athlete.__str__()

    class Meta:
        managed = False
        db_table = u'"Event\'sTables\".\"athlete_event"'


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
    class Meta:
        widgets = {
            'password': PasswordInput,
        }


class StudentAdmin(admin.ModelAdmin):
    form = StudentForm


class HiddenModelAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False
