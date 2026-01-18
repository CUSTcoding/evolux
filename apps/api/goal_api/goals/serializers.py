from rest_framework import serializers
from .models import Goal


class GoalSerializer(serializers.ModelSerializer):
    is_late =serializers.SerializerMethodField()

    class Meta:
        model = Goal
        fields = '__all__'

    def get_is_late(self, obj):
        return obj.is_late()
    
    def update(self, instance, validated_data):
        progress = validated_data.get('progress', instance.progress)

        if progress == 100:
            validated_data['status'] = 'done'
        elif progress > 0:
            validated_data['status'] = 'in_progress'

        return super().update(instance, validated_data)
