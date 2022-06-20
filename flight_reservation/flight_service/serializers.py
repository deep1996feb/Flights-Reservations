from rest_framework import serializers
from flight_service.models import Passenger,Flight,Reservation
import re

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        
    def validate_Flight_Number(self, Flight_Number):#How to add a validation in a class 
        print("validate_Flight_Number")
        if(re.match("^[a-zA-Z0-9]*$",Flight_Number)==None):
            raise serializers.ValidationError("Invalid Flight Number. Make sure it is Alpha Numeric")
        return Flight_Number
    
    def validate(self,data):
        print("validate")    #Generic Valida data which is shown what the logic is invoked
        print(data["Flight_Number"])
        return data
        
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
        
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['flight', 'passenger']