from rest_framework import serializers

from tracker.models import Bug


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = '__all__'


class TrackerCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        bug = Bug.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            priority=validated_data['priority'],
            status=validated_data['status'],
            project=validated_data['project'],
            assigned_to=validated_data['assigned_to'],
            created_by=validated_data['created_by'],
            resolved_date=validated_data['resolved_date'],
        )
        return bug

    class Meta:
        model = Bug
        fields = ['name', 'description', 'priority', 'status', 'project', 'assigned_to', 'created_by', 'resolved_date']


class TrackerDeleteSerializer(serializers.ModelSerializer):
    def delete(self, validated_data):
        bug = Bug.objects.get(id=validated_data['id'])
        bug.delete()
        return validated_data
