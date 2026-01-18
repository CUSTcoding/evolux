from django.shortcuts import render
from .models import Goal
from .serializers import GoalSerializer
from rest_framework.viewsets import ModelViewSet


class GoalViewSet(ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer