from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

@api_view(['GET'])
def index(request):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = 'Clock time in live server is '
    return Response(data=message + date, status=status.HTTP_200_OK)