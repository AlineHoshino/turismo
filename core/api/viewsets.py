from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    search_fields = ('nome', 'descricao', 'endereco__linha1')

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     return Response({'teste': 123}) - exemplo de get All sendo sobrescrito

    # @action(methods=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     return Response({'teste': 123})

    # @action(methods=['post'], detail=True)
    # def associa_atracoes(self, request, id):
    #     atracoes = request.data['ids']
    #     ponto = PontoTuristico.objects.get(id=id)
    #
    #     ponto.atracoes.set(atracoes)
    #
    #     ponto.save()
    #     return HttpResponse("ok")
