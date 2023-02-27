from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import TeamFilter
from .models import Team
from .permissions import ObjectPermission
from .serializers import TeamDetailsSerializer
from .serializers import TeamSerializer


@extend_schema_view(
    create=extend_schema(description="API endpoint to create a team"),
    list=extend_schema(
        description="API endpoint to get a list of teams, with filtering options"
    ),
    retrieve=extend_schema(
        description="API endpoint to retrieve a specific team, which gives on him detailed informations"
    ),
    update=extend_schema(description="API endpoint to modify a specific team"),
    partial_update=extend_schema(
        description="API endpoint to partially modify a specific team\n\nAll fields are optionnal"
    ),
    destroy=extend_schema(
        description="API endpoint to delete a specific team. It's horrible"
    ),
)
class TeamViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        ObjectPermission,
    )
    filterset_class = TeamFilter

    def get_queryset(self):
        if self.action == "list":
            user = self.request.user
            return Team.objects.filter(trainer=user).order_by("name")
        return Team.objects.all().order_by("name")

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TeamDetailsSerializer
        return TeamSerializer
