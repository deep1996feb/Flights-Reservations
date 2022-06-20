from django.urls import path
from flight_service.views import FlightAPIView, FlightDetailAPIView,PassengerAPIView,PassengerDetailAPIView,ReservationAPIView, ReservationDetailAPIView,FindingFlight,SaveReservation
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('flights/',view=FlightAPIView.as_view()),
    path('flight/<int:id>/', view=FlightDetailAPIView.as_view()),
    path('passengers/', view=PassengerAPIView.as_view()),
    path('passenger/<int:id>/', view=PassengerDetailAPIView.as_view()),
    path('reservations/', ReservationAPIView.as_view()),
    path('reservation/<int:id>/', view=ReservationDetailAPIView.as_view()),
    path('find/', view=FindingFlight.as_view()),
    path('savereservation/', view=SaveReservation.as_view()),
    path('apiauthtoken/', view=obtain_auth_token,name='api_token_auth'),
]
