from rest_framework import viewsets, mixins


class CreateReadModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass
