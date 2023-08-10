import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Details


class DetailsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'location', 'email', 'phone_number')
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="details.csv"'

        writer = csv.writer(response)
        writer.writerow(['Full Name', 'Location', 'Email', 'Phone Number'])

        for obj in queryset:
            writer.writerow([obj.full_name, obj.location, obj.email, obj.phone_number])

        return response

    export_as_csv.short_description = "Export selected details as CSV"

admin.site.register(Details, DetailsAdmin)
