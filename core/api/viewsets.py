from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # def list(self, request, *args, **kwargs):
    #     return Response({'teste': 123}) - exemplo de get All sendo sobrescrito

    # @action(methods=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     return Response({'teste': 123})