from django.contrib import admin
from .models import Academic, Skill, User, Cv, Profile, Referee

model_list = [Academic, Skill, User, Cv, Profile, Referee]
admin.site.register(model_list)
