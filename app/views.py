from django.shortcuts import get_object_or_404
from app.serializers import*
from .models import*
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# start a file

class add_department(APIView):
    def post(self,request):
        serializer= AddDepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)



       
    def get(self, request, id=None): 
        if not id:
            return Response({"msg": "Please provide a valid id."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            data = AddDepartment.objects.get(id=id)
            serializer = AddDepartmentSerializer(data)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except AddDepartment.DoesNotExist:
            return Response({"msg": " id does not exist."}, status=status.HTTP_404_NOT_FOUND)


    
    def patch(self, request, id=None):
        try:
            data= AddDepartment.objects.get(id=id)
            serializer= AddDepartmentSerializer(data, data= request.data, partial= True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"data update","data":serializer.data})
            else:
                return Response({"status":"error please try again","data":serializer.errors})
        except:
            return Response({"msg":"id is not valid !! take some valid id"})
        
    def delete(self, request, id=None):
        try:
            data = AddDepartment.objects.get(id=id)
            data.delete()
            return Response({"status":"success","data":"delete successfully"})
        except:
            return Response({"msg":"id is not valid !! take some valid id"})
 
 
class DeleteAccountView(APIView):
    
      def delete(self, request, id):
        user = get_object_or_404(AddDepartment,id=id)
        user.deleted = True
        user.is_active = False
        user.save()
        return Response("User account deleted successfully.")        
    
class All_dataget(APIView):
    def get(self, request):
        data= AddDepartment.objects.all()
        serializer= AddDepartmentSerializer(data, many=True)
        return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)                
        
        
  
class Add_Designation(APIView):
    def post(self,request):
        serializer= AddDesignationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        
        if not id:
            return Response({"msg": "Please provide a valid id."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            data = AddDesignation.objects.get(id=id)
            serializer = AddDesignationSerializer(data)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except AddDesignation.DoesNotExist:
            return Response({"msg": "id does not exist."}, status=status.HTTP_404_NOT_FOUND)


    
    def patch(self, request, id=None):
        try:
            data= AddDesignation.objects.get(id=id)
            serializer= AddDesignationSerializer(data, data= request.data, partial= True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"data update","data":serializer.data})
            else:
                return Response({"status":"error please try again","data":serializer.errors}) 
        except:
            return Response({"msg":"id is not valid !! take some valid id"})    
        
    def delete(self, request, id=None):
        try:
            data = AddDesignation.objects.get(id=id)
            data.delete()
            return Response({"status":"success","data":"delete successfully"})    
        except:
            return Response({"msg":"id is not valid !! take some valid id"})
        
        
class Alldataget(APIView):
    def get(self, request):
        data= AddDesignation.objects.all()
        serializer= AddDesignationSerializer(data, many=True)
        return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)        
