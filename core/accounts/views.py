from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": f"Hello {request.user.username}",
            "role": request.user.role
        })


from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminRole
from rest_framework.views import APIView
from rest_framework.response import Response


class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get(self, request):
        return Response({
            "message": "Welcome Admin",
            "user": request.user.username
        })
