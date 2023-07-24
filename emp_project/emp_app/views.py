from django.shortcuts import render

from .models import personal_detail_model
from .models import Document_model
from .models import emergency_contact
from .models import salary
from .models import socialmedialink

from .serializers import persoal_detail_serializers
from .serializers import Document_serializers
from .serializers import emergencycontact_serializers
from .serializers import salaryserializers
from .serializers import socialmedialserializer

from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# ==========================================================================================
# -----------------------------[personal_details]-------------------------------------
class personal_detail_view(APIView):
    def get(self,request):
        obj=personal_detail_model.objects.all()
        serializer=persoal_detail_serializers(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=persoal_detail_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class Employeeinfo(APIView):
    def get(self,request,id):
        try:
            obj=personal_detail_model.objects.get(id=id)
        except personal_detail_model.DoesNotExist:
            msg={"msg":"not found get"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=persoal_detail_serializers(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            obj=personal_detail_model.objects.get(id=id)
        except personal_detail_model.DoesNotExist:
            msg={"msg":"Not Found Eroor put"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serilizer=persoal_detail_serializers(obj,data=request.data)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
# patch 
    def patch (self,request,id):
        try:  
            obj=personal_detail_model.objects.get(id=id)
        except personal_detail_model.DoesNotExist:
            msg={"msg":"Not Found Eroor patch"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serilizer=persoal_detail_serializers(obj,data=request.data,partial=True)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            obj=personal_detail_model.objects.get(id=id)
        except personal_detail_model.DoesNotExist:
            msg={"msg":"not found detelet"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
    
# ==============================================================================================================
# ---------------------[document]---------------------------------

class document_detail(APIView):
    def get(self,request):
        obj=Document_model.objects.all()
        serializer=Document_serializers(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=Document_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Document_info(APIView):

    def get(self,request,id):
        try:
            obj=Document_model.objects.get(id=id)
        except Document_model.DoesNotExist:
            msg={"msg":"not found get"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=Document_serializers(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            obj=Document_model.objects.get(id=id)
        except Document_model.DoesNotExist:
            msg={"msg":"Not Found Eroor put"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serilizer=Document_serializers(obj,data=request.data)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
# patch
    def patch (self,request,id):
        try:
            obj=Document_model.objects.get(id=id)
        except Document_model.DoesNotExist:
            msg={"msg":"Not Found Eroor patch"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serilizer=Document_serializers(obj,data=request.data,partial=True)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            obj=Document_model.objects.get(id=id)
        except Document_model.DoesNotExist:
            msg={"msg":"not found detelet"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)

# =============================================================================================
# -----------------------------[emergency contact]-----------------------------------------------------

class emergencycontact_view(APIView):
    def get(self,request):
        obj=emergency_contact.objects.all()
        serializer=emergencycontact_serializers(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=emergencycontact_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class emergencycontact_info(APIView):
    def get(self,request,id):
        try:
            obj=emergency_contact.objects.get(id=id)
        except emergency_contact.DoesNotExist:
            msg={"msg":"not found get"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=emergencycontact_serializers(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            obj=emergency_contact.objects.get(id=id)
        except emergency_contact.DoesNotExist:
            msg={"msg":"Not Found Eroor put"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        serilizer=emergencycontact_serializers(obj,data=request.data)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
# patch
    def patch (self,request,id):
        try:
            obj=emergency_contact.objects.get(id=id)
        except emergency_contact.DoesNotExist:
            msg={"msg":"Not Found Eroor patch"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serilizer=emergencycontact_serializers(obj,data=request.data,partial=True)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            obj=emergency_contact.objects.get(id=id)
        except emergency_contact.DoesNotExist:
            msg={"msg":"not found detelet"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)

# ============================================================================================
# ------------------------------------[salary]----------------------------------------------
class salary_view(APIView):
    def get(self,request):
        obj=salary.objects.all()
        serializer=salaryserializers(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=salaryserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class salary_info(APIView):
    def get(self,request,id):
        try:
            obj=salary.objects.get(id=id)
        except salary.DoesNotExist:
            msg={"msg":"not found get"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=salaryserializers(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            obj=salary.objects.get(id=id)
        except salary.DoesNotExist:
            msg={"msg":"Not Found Eroor put"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serilizer=salaryserializers(obj,data=request.data)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
# patch
    def patch (self,request,id):
        try:
            obj=salary.objects.get(id=id)
        except salary.DoesNotExist:
            msg={"msg":"Not Found Eroor patch"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serilizer=salaryserializers(obj,data=request.data,partial=True)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            obj=salary.objects.get(id=id)
        except salary.DoesNotExist:
            msg={"msg":"not found detelet"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)


# ============================================================================================
# -----------------------------------[social-meadia]--------------------------------------

class socialmeadia_view(APIView):

    def get(self,request):
        obj=socialmedialink.objects.all()
        serializer=socialmedialserializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=socialmedialserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class socialmeadia_info(APIView):

    def get(self,request,id):

        try:
            obj=socialmedialink.objects.get(id=id)
        except socialmedialink.DoesNotExist:
            msg={"msg":"not found get"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=socialmedialserializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            obj=socialmedialink.objects.get(id=id)
        except socialmedialink.DoesNotExist:
            msg={"msg":"Not Found Eroor put"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serilizer=socialmedialserializer(obj,data=request.data)
        
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
# patch
    def patch (self,request,id):
        try:
            obj=socialmedialink.objects.get(id=id)
        except socialmedialink.DoesNotExist: 
            msg={"msg":"Not Found Eroor patch"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serilizer=socialmedialserializer(obj,data=request.data,partial=True)

        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            obj=socialmedialink.objects.get(id=id)
        except socialmedialink.DoesNotExist:
            msg={"msg":"not found detelet"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
    
