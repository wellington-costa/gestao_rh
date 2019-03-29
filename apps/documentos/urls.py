from django.urls import path
from .views import CreateDocumento

urlpatterns = (

    path('novo', CreateDocumento.as_view(), name = 'create_documento'),

)