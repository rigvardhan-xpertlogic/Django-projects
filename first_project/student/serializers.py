from rest_framework import serializers
from student.models import module_1

#creat serializers here
class Sutdent_Serializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=module_1
        fields="__all__"