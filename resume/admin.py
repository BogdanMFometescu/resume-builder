from django.contrib import admin
from .models import Resume,Experience,Skills,Projects,Education

# Register your models here.

admin.site.register(Resume)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Projects)
admin.site.register(Education)

