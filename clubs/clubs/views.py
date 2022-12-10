from .serializers import clubSerializer
from .models import Club
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def clubs(request):
    all_clubs = Club.objects.all()
    serializer = clubSerializer(all_clubs, many=True)
    return JsonResponse({"clubs": serializer.data})

@api_view(['POST'])
def create_club(request):
    serializer = clubSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def club_detail(request, id):
    club = Club.objects.get(pk=id)

    if request.method == 'GET':
        serializer = clubSerializer(club)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = clubSerializer(club, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        club.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



