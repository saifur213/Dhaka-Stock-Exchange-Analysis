from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from webScraping.models import *
#from .serializers import *
# Create your views here.
class CompanyApiView(APIView):
    #serializer_class = BookSerializer
    def get(self,request):
        allCompany = company_details.objects.all().values()
        return Response({"Message":"List of Company","Company List":allCompany})
    
    # def post(self,request):
    #     Book.objects.create(id=request.data["id"],
    #                         title=request.data["title"],
    #                         author=request.data["author"])
    #     book = Book.objects.all().filter(id=request.data["id"]).values()
    #     return Response({"Message":"New Book added","Book":book})


    # def post(self,request):
    #     print("Request data is: ",request.data)
    #     serializer_obj = BookSerializer(data=request.data)
    #     if(serializer_obj.is_valid()):
    #         Book.objects.create(id=serializer_obj.data.get("id"),
    #                             title=serializer_obj.data.get("title"),
    #                             author=serializer_obj.data.get("author"))
            
    #     book = Book.objects.all().filter(id=request.data["id"]).values()
    #     return Response({"Message":"New Book added","Book":book})
        
