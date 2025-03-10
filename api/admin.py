from django.contrib import admin
from .models import (Services, About, Activity, SubActivity, Projects, WhatOurClientsSay,
                     GetInContactSection, ClientsReviews, ClientsEmail, Partners)

admin.site.site_header = 'Welcome to FIXWORKS Admin Panel'
admin.site.site_title = 'FIXWORKS Admin Panel'
admin.site.index_title = 'Sections'

admin.site.register(Services)
admin.site.register(About)

class SubActivityInline(admin.StackedInline):
    model = SubActivity
    extra = 2

class ActivityAdmin(admin.ModelAdmin):
    inlines = [SubActivityInline,]

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Projects)
admin.site.register(WhatOurClientsSay)
admin.site.register(GetInContactSection)
admin.site.register(ClientsReviews)
admin.site.register(ClientsEmail)
admin.site.register(Partners)