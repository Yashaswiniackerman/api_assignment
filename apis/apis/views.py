from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AboutSerializer, MyserviceSerializer

@api_view(['POST'])
def update_about_details(request):
    serializer = AboutSerializer(data=request.data)
    if serializer.is_valid():
        # Save/update About details
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_myservice_details(request):
    serializer = MyserviceSerializer(data=request.data)
    if serializer.is_valid():
        # Save/update Myservice details
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_about_details(request):
    # Fetch and return About details
    about_data = { 'name': 'Your Name', 'description': 'Your Description' }
    return Response(about_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_readme_details(request):
    # Fetch and return ReadMe details
    readme_data = { 'content': 'Your ReadMe content' }
    return Response(readme_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_myservice_details(request):
    email = request.query_params.get('email')
    if not email:
        return Response({'error': 'Email parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)
    # Fetch and return Myservice details for the given email
    myservice_data = { 'email': email, 'data': 'Your Myservice data' }
    return Response(myservice_data, status=status.HTTP_200_OK)
