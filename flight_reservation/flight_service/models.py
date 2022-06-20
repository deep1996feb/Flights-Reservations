from django.db import models

# Create your models here.

class Flight(models.Model):
    Flight_Number = models.CharField(max_length=30)
    Operating_Airlines = models.CharField(max_length=30)
    Departure_City = models.CharField(max_length=30) #Blank=True is used when we want to skip the field.
    Arrival_City = models.CharField(max_length=30) #null=True is used when we want to field for a null
    Date_of_Departure = models.DateField()
    Time_of_Onboard = models.TimeField()
    Time_of_Offboard = models.TimeField()
    
    def __str__(self):
        return self.Flight_Number
            
        
    
class Passenger(models.Model):
    Passenger_First_name = models.CharField(max_length=30)
    Passenger_Last_name = models.CharField(max_length=20)
    Passenger_Email_Id = models.CharField(max_length=30)
    Passenger_Mobile_Number = models.CharField(max_length=10)
    Passenger_Health_Status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Passenger_First_name
    
    
class Reservation(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.passenger.Passenger_First_name

    