from rest_framework import serializers

from applications.book_store.models import CustomUser


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = CustomUser
        fields ='__all__'

    def create(self, validated_data):
        print(validated_data)
        return CustomUser.objects.create(**validated_data)
