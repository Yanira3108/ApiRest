
from .models import Tarea
from .serializer import TareaSerializer

# Create your views here.

from rest_framework.viewsets import ModelViewSet 
class TareaViewSet(ModelViewSet):
    queryset= Tarea.objects.all()
    serializer_class= TareaSerializer
      
    
    
