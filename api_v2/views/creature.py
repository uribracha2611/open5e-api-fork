from rest_framework import viewsets

from django_filters import FilterSet

from api_v2 import models
from api_v2 import serializers


class CreatureFilterSet(FilterSet):

    class Meta:
        model = models.Creature
        fields = {
            'key': ['in', 'iexact', 'exact' ],
            'name': ['iexact', 'exact'],
            'document__key': ['in','iexact','exact'],
             'size': ['exact'],
            'armor_class': ['exact','lt','lte','gt','gte'],
            'ability_score_strength': ['exact','lt','lte','gt','gte'],
            'ability_score_dexterity': ['exact','lt','lte','gt','gte'],
            'ability_score_constitution': ['exact','lt','lte','gt','gte'],
            'ability_score_intelligence': ['exact','lt','lte','gt','gte'],
            'ability_score_wisdom': ['exact','lt','lte','gt','gte'],
            'ability_score_charisma': ['exact','lt','lte','gt','gte'],
            'saving_throw_charisma': ['isnull'],
            'saving_throw_strength': ['isnull'],
            'saving_throw_dexterity': ['isnull'],
            'saving_throw_constitution': ['isnull'],
            'saving_throw_intelligence': ['isnull'],
            'saving_throw_wisdom': ['isnull'],
            'saving_throw_charisma': ['isnull'],
            'skill_bonus_acrobatics': ['isnull'],
            'skill_bonus_animal_handling': ['isnull'],
            'skill_bonus_arcana': ['isnull'],
            'skill_bonus_athletics': ['isnull'],
            'skill_bonus_deception': ['isnull'],
            'skill_bonus_history': ['isnull'],
            'skill_bonus_insight': ['isnull'],
            'skill_bonus_intimidation': ['isnull'],
            'skill_bonus_investigation': ['isnull'],
            'skill_bonus_medicine': ['isnull'],
            'skill_bonus_nature': ['isnull'],
            'skill_bonus_perception': ['isnull'],
            'skill_bonus_performance': ['isnull'],
            'skill_bonus_persuasion': ['isnull'],
            'skill_bonus_religion': ['isnull'],
            'skill_bonus_sleight_of_hand': ['isnull'],
            'skill_bonus_stealth': ['isnull'],
            'skill_bonus_survival': ['isnull'],
            'passive_perception': ['exact','lt','lte','gt','gte'],
        }

class CreatureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list: API endpoint for returning a list of creatures.
    retrieve: API endpoint for returning a particular creature.
    """
    queryset = models.Creature.objects.all().order_by('pk')
    serializer_class = serializers.CreatureSerializer
    filterset_class = CreatureFilterSet


class CreatureTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CreatureType.objects.all().order_by('pk')
    serializer_class = serializers.CreatureTypeSerializer