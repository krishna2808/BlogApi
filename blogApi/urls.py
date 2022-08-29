
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from api import views 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView



# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('blogapi', views.PostModelViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('api.urls')),
    path('postapi/', include('post.urls')),

   


    # path('', include(router.urls)),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    
]  +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 