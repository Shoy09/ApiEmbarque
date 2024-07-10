from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

from backend import views

urlpatterns = [
    path('crear/users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('token/', obtain_tokens, name='token_obtain'),
    
     ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)