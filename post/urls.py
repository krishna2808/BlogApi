

from argparse import Namespace
from django.urls import path, include
from post.views import PostModelViewSet, ShowOwnPostApiView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

# for ViewSet class 
# router.register('studentapi', views.StudentViewSet, basename='student')

# for ModelViewSet class 
router.register('post', PostModelViewSet, basename='post')
# router.register('show_own_post', ShowOwnPostApiView, basename='show_own_post')

# ReadOnlyModelViewSet class 
# router.register('studentapi', views.StuentReadOnlyModelViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('show_own_post/', ShowOwnPostApiView.as_view(), name='show_own_post'),
    path('show_own_post/<int:pk>/', ShowOwnPostApiView.as_view(), name='show_own_post'),

   

  

] 
