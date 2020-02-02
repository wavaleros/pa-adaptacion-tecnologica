from django.contrib import admin
from .models import *

admin.site.register(Athlete, SportAdmin)
admin.site.register(Sport, AthleteAdmin)
admin.site.register(Coach)
admin.site.register(Event, EventAdmin)
admin.site.register(AthleteEvent, HiddenModelAdmin)
admin.site.register(EventVideoComments)
admin.site.register(SportModality)
admin.site.register(Student, StudentAdmin)
admin.site.register(AthleteSport, HiddenModelAdmin)

# Register your models here.
