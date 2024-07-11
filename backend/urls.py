from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from backend import views


urlpatterns = [
    path('crear/users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('token/', obtain_tokens, name='token_obtain'),
    path('diarios-de-pesca/', DiarioDePescaListView.as_view(), name='diario_de_pesca_list'),
    path('diarios-de-pesca/<int:pk>/', DiarioDePescaDetailView.as_view(), name='diario_de_pesca_detail'),
    path('diarios-de-pesca/<int:pk>/delete/', DiarioDePescaDeleteView.as_view(), name='diario_de_pesca_delete'),
    path('embarcaciones/', EmbarcacionesListCreateView.as_view(), name='embarcaciones-list-create'),
    path('especies/', EspeciesListCreateView.as_view(), name='especies-list-create'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)