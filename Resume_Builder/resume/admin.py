from django.contrib import admin
from resume.models import Profile,Skill,Education,Project
# Register your models here.

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Project)