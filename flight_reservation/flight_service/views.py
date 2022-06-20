from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from flight_service.models import Flight, Passenger, Reservation
from flight_service.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class FlightAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        flight = Flight.objects.all()
        serializer = FlightSerializer(flight, many=True)
        return Response(serializer.data)
            
    def post(self,request):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
 
class FlightDetailAPIView(APIView):

    def get(self, request, id):
         flight = Flight.objects.get(id=id)
         serializer = FlightSerializer(flight)
         return Response(serializer.data)
     
    def put(self,request,id):
         flight = Flight.objects.get(id=id)
         serializer = FlightSerializer(flight,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        flight = Flight.objects.get(id=id)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
     
     
class PassengerAPIView(APIView):
    def get(self,request):
        passenger = Passenger.objects.all()
        serializer = PassengerSerializer(passenger, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class PassengerDetailAPIView(APIView):
    
    def get(self, request, id):
         passenger = Passenger.objects.get(id=id)
         serializer = PassengerSerializer(passenger)
         return Response(serializer.data)
    
    def put(self,request,id):
        passenger = Passenger.objects.get(id=id)
        serializer = PassengerSerializer(passenger,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        passenger = Passenger.objects.get(id=id)
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ReservationAPIView(APIView):
    def get(self,request):
        reservation = Reservation.objects.all()
        serializer = ReservationSerializer(reservation, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ReservationSerializer(unique=False,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ReservationDetailAPIView(APIView):

    def get(self,request,id):
        reservation = Reservation.objects.get(id=id)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)
    
    def put(self,request,id):
        reservation = Reservation.objects.get(id=id)
        serializer = ReservationSerializer(reservation,serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FindingFlight(APIView):    
    def post(self,request):
        flights = Flight.objects.filter(Departure_City=request.data['Departure_City'],Arrival_City=request.data['Arrival_City'],Date_of_Departure=request.data['Date_of_Departure'])
        serializer = FlightSerializer(flights,many=True)
        return Response(serializer.data)
    
class SaveReservation(APIView):
    def post(self,request):
        flight = Flight.objects.get(id=request.data['flightid'])
        
        passenger = Passenger()
        passenger.Passenger_First_name = request.data['First_name']
        passenger.Passenger_Last_name = request.data['Last_name']
        passenger.Passenger_Email_Id = request.data['Email_Id']
        passenger.Passenger_Mobile_Number = request.data['Mobile_Number']
        passenger.Passenger_Health_Status = request.data['Health_Status']
        passenger.save()
        
        reservation = Reservation()
        reservation.flight = flight
        reservation.passenger = passenger
        reservation.save()
        return Response(status=status.HTTP_201_CREATED)
        
    
#Adminpanel = flightapp
#User = Soni, 123@soni
          
         
        
