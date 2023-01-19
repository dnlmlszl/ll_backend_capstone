from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
#from rest_framework.generics import ListCreateView, RetrieveUpdateView, DestroyAPIView
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer

# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request): 
    return Response({"message":"This view is protected"})

def home(request):
    return render(request, "index.html", {})

def about(request):
    pass

class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]
        


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

    # def post(self, request):
    #     serializer = MenuSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({ "status": "success", "data": serializer.data })

class MenuItemsCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes=[IsAdminUser]