from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import*
from rest_framework.response import Response
from rest_framework import status

class WorkShifCreateView(APIView):
    def post(self, request):
        serilizer= Work_ShiftSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"status":"success","data":serilizer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serilizer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, id=None):
        if not id:
            return Response({"msg": "Please provide a valid id."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = Work_Shift.objects.get(id=id)
            serializer = Work_ShiftSerializer(data)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Work_Shift.DoesNotExist:
            return Response({"msg": "Work Shift with the provided id does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        
    def patch(self, request, id=None):
        try:
            data = Work_Shift.objects.get(id=id)
            serializer = Work_ShiftSerializer(data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "update success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors})
        except:
            return Response({"msg":"id is not valid !! you can take some valid id"})

    def delete(self,request, id=None):
        try:
            data = Work_Shift.objects.get(id=id)
            data.delete()
            return Response({"status":"success","data":"delete successfully"})
        except:
            return Response({"msg":"id is not valid !! you can take some valid id"})
        

class Alldataget(APIView): 
    def get(self, request):
        data= Work_Shift.objects.all() 
        serializer= Work_ShiftSerializer(data, many=True)
        return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)



