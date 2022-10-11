from django.shortcuts import render
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser,FileUploadParser,BaseParser
from rest_framework.response import Response
from .serialization import *
import random,json
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# def register_id(Master_model,sub_master,user,custmer):
#         master_count=str(Master_model.objects.all().count())
#         sub_master_count=str(sub_master.objects.all().count())
#         user_count=str(user.objects.all().count())
#         custmer_count=str(custmer.objects.all().count())
#         value=master_count+sub_master_count+user_count+custmer_count
#         return value
class country(APIView):
    # parser_classes=[JSONParser]
    # def get(self, request, format=None):
    #     user_count = User.objects.filter(is_active=True)
    #     content = {'user_count': json.dumps(user_count)}
    #     return JSONRenderer(JSONRenderer().render(user_count))
    
    # def post(self,request,format=None):
    
        
    #     return Response({"data":""})
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None,id=None):
        # country_data=Country.objects.filter(id=id)
        # data=CountrySerialization(country_data,many=True)
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
    

    # def put(self,request,format=None):
    #     return Response({"data":request.data})
    # parser_classes = [FileUploadParser]

    # def put(self, request, filename, format=None):
    #     file_obj = request.data['file']
    #     # ...
    #     # do some stuff with uploaded file
    #     # ...
    #     return Response(status=204)
class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)

# class Test_api(APIView):
#     parser_classes=[JSONParser]
#     if Test.objects.get(id=id)!=None:
#         def get(self,request,id,format=None):
#             test_data=Test.objects.get(id=id)
#             test_data=TestSelialiaztion(test_data)
#             return Response({" data":test_data.data})

#         # def post(self,request,format=None):
#         #     data=TestSelialiaztion(data=request.data)
#         #     if data.is_valid():
#         #         data.save()
#         #         return Response({"data":"Succes full"})

#         def put(self,request,id,formate=None):
            
#             testdata=Test.objects.get(id=id)
#             test=TestSelialiaztion(testdata,data=request.data)
#             if test.is_valid():
#                 test.save()
#                 test.save()
#                 return Response(test.data)
#             return Response({"data":test.data})
#         def delete(self, request, id, format=None):
#             snippet = Test.objects.get(id=id)
#             snippet.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         def get(request,self,format=None):
#             Response({"MSG":"Data Deleted "})