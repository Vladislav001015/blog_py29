from rest_framework import serializers

from applications.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        # return Post.objects.create(**validated_data) # title=Post3, image='', owner=''
        return super().create(validated_data)
    
    