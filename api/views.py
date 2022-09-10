from urllib import response
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from testapp.models import SampleUser
from testapp.serializers import TestSerializer


class TestCreateAPIView(generics.CreateAPIView):
    serializer_class = TestSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TestSerializer
    
    queryset = SampleUser.objects.all()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class TestRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TestSerializer
    
    queryset = SampleUser.objects.all()

    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        user = SampleUser.objects.get(id=response.data['id'])

        ##### DIFFERENCE
        rem_time = user.business_plan.remaining_time(user.subscription_date)
        response.data["end_date"] = rem_time
        ##### END
        
        return response 
        