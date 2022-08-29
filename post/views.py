
from functools import partial
from api.models import User
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.parsers import MultiPartParser, FormParser


from .serializers import PostSerializer, ShowOwnPostSerializer
from .models import Post, Comment

# Create your views here.


class PostModelViewSet(viewsets.ReadOnlyModelViewSet):
  
   authentication_classes = [SessionAuthentication]
   permission_classes = [IsAuthenticated]
   queryset = Post.objects.all() 
   serializer_class = PostSerializer
  


# class ShowOwnPostApiView(viewsets.ModelViewSet):
#    authentication_classes = [SessionAuthentication]
#    permission_classes = [IsAuthenticated]
#    queryset = Post.objects.all() 
#    serializer_class = ShowOwnPostSerializer
   




class ShowOwnPostApiView(APIView):
   authentication_classes = [SessionAuthentication]
   permission_classes = [IsAuthenticated]
   # parser_classes = (MultiPartParser, FormParser)
   


   def get(self, request,pk=None, format=None):
      # print('************** ', type(request.user), request.data, request.user)
      post_query_set = Post.objects.filter(user=request.user)     
      serializer = ShowOwnPostSerializer(post_query_set, many=True, context={'request': request})
      # print('************', serializer.data)
      # print('*******************', request.body)
      return Response(serializer.data)   


   def post(self, request, pk=None, format=None):
      serializer =serializer = ShowOwnPostSerializer(data=request.data, context={'request': request})
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

   def patch(self, request, pk = None, format=None):
      id = pk 
      post_query_set = Post.objects.filter(user=request.user, id =id)    

      serializer = ShowOwnPostSerializer(post_query_set, data=request.data, context={'request': request}, partial=True)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def put(self, request, pk=None, format=None):
      id =pk 
      post_query_set = Post.objects.filter(user=request.user, id=id)     
      serializer = ShowOwnPostSerializer(post_query_set, data=request.data, many=True, context={'request': request})
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self, request, pk = None, format=None):
      id = pk 
      try:
         post = Post.objects.get(user=request.user, id=id)
         post.delete()
         return Response({'msg': 'Post Delete Successfully '})

      except: 
         return Response({'msg': 'Invalid id number  '})
            


          
      

