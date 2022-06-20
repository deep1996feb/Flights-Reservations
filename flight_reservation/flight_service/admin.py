from django.contrib import admin
from flight_service.models import Flight,Passenger,Reservation
# Register your models here.

admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Reservation)
