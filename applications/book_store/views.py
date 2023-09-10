from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from applications.book_store.models import CustomUser
from applications.book_store.permissions import IsOwnerOrAdminReadOnly
from applications.book_store.serializers import PostSerializer


# Create your views here.
class ListPostView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreatePostView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class RetrievePostView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrAdminReadOnly]


class UpdatePostView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrAdminReadOnly]

class DeletePostView(generics.DestroyAPIView):
        queryset = CustomUser.objects.all()
        serializer_class = PostSerializer
        permission_classes = [IsOwnerOrAdminReadOnly]
