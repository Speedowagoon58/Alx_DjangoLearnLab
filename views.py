from rest_framework.permissions import IsAuthenticated

["generics.ListAPIView"]


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    ["viewsets.ModelViewSet"]
