from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Contact)
admin.site.register(Blogs)



class InternshipAdmin(admin.ModelAdmin):
    list_display=('fullname',
    'usn',
    'email',
    'collegename',
    'offer_status',
    'start_date',
    'end_date',
    'proj_report'
                  )
    search_fields=('fullname','usn','email')
admin.site.register(Internship,InternshipAdmin)

