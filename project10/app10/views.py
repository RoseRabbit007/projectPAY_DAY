from django.shortcuts import render
from rest_framework.response  import Response
from rest_framework.views import APIView 
from rest_framework import status
from .models import Bank,Address_detail
from .serializer import bankserializer,addresserializer
# from rest_framework.request import Request
# from django.http import HttpRequest
# bank crud operations
class BankDetail(APIView):
    def get(self,request):
        obj=Bank.objects.all()
        serializer=bankserializer(obj, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        # import pdb
        # pdb.set_trace()
        serializer =bankserializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        # else:   

        #     msg={"msg":"already exists"}
        #     return Response(msg,status=status.HTTP_208_ALREADY_REPORTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class bankinfo(APIView):
    def get(self,request,id):
        try:
            obj=Bank.objects.get(id=id)
        except Bank.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
            
        serializer=bankserializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def put(self,request,id):
        try:
            obj=Bank.objects.get(id=id)
        except Bank.DoesNotExist:
            msg={"msg":"not found  error"}

            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        serializer=bankserializer(obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


    def patch(self,request,id):
        try:
            obj=Bank.objects.get(id=id)
        except Bank.DoesNotExist:
            msg={"msg":"not found  error"}

            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        serializer=bankserializer(obj,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def  delete(self,request,id):
        try:
            obj=Bank.objects.get(id=id)
        except Bank.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
    
# address_detail crud operations
class AddressDetail(APIView):
    def get(self,request):
        obj=Address_detail.objects.all()
        serializer=addresserializer(obj, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        # try:
            serializer=addresserializer(data=request.data)

            if serializer.is_valid():
                if Address_detail.objects.filter(phone_number=self.request.data['phone_number']).exists():
                    return Response({"error": "This phone number already exists."})
                serializer.save()
                return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

                 


            
            
        

    
class addressinfo(APIView):
    def get(self,request,id):
        try:
            obj=Address_detail.objects.get(id=id)
        except Address_detail.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
            
        serializer=addresserializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def put(self,request,id):
        try:
            obj=Address_detail.objects.get(id=id)
        except Address_detail.DoesNotExist:
            msg={"msg":"not found  error"}

            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        serializer=addresserializer(obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


    def patch(self,request,id):
        try:
            obj=Address_detail.objects.get(id=id)
        except Address_detail.DoesNotExist:
            msg={"msg":"not found  error"}

            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        serializer=addresserializer(obj,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def  delete(self,request,id):
        try:
            obj=Address_detail.objects.get(id=id)
        except Address_detail.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
    
# marge api

# class MergedAPIView(APIView):
#     def get(self, request):
#         # Fetch data from API1
#         api1_data =BankDetail.as_view()(request).data
#         bank_details = BankDetail.objects.all()  # Replace this with your API1 data retrieval logic
#         bank_serializer = bankserializer(bank_details, many=True)
#         api1_data = bank_serializer.data


#         # Fetch data from API2
#         # api2_data = AddressDetail.as_view()(request).data

#         # Merge data from both APIs
#         merged_data = {}
#         merged_data['api1_data'] = api1_data
#         # merged_data['api2_data'] = api2_data

#         return Response(merged_data)

