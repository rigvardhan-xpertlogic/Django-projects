from django.contrib import admin
from student.models import module_1

class studentAdmin(admin.ModelAdmin):
    list_display=('roll_number','student_name','student_class','student_section','student_email','phone_number','subject')
# Register your models here.

admin.site.register(module_1,studentAdmin)