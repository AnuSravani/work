from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from .models import RobertCategorys,Roberts,Manufacturers
from .serializer import RobertCategorySerializer,RobertSerializer,ManufactureSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
# Create your views here.


class RobertView(ModelViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=RobertSerializer
    queryset=Roberts.objects.all()

    
    def list(self,request,*args,**kwargs):
        qs=Roberts.objects.all()
        serializer=RobertSerializer(qs,many=True)
        return Response(data=serializer.data)
       
    def create(self,request,*args,**kwargs):
        serializer=RobertSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

        
class ManufactureView(ModelViewSet):
    serializer_class=ManufactureSerializer
    queryset=Manufacturers.objects.all()


            
    

class RobertCategoryView(ModelViewSet):
    serializer_class=RobertCategorySerializer
    queryset=RobertCategorys.objects.all()

class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
           qs=User.objects.create_user(**serializer.validated_data)
           serializer=UserSerializer(qs,many=False)
           return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        


    
