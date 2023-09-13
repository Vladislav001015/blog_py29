from rest_framework import serializers

from applications.post.models import Post, Comment, Rating


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        # return Post.objects.create(**validated_data) # title=Post3, image='', owner=''
        return super().create(validated_data)
    
    def to_representation(self, instance):
        # print(instance)
        rep =  super().to_representation(instance)
        # print(rep)
        # rep['name'] = 'John'
        rep['like_count'] = instance.likes.filter(is_like=True).count()
        return rep


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Rating
        fields = ('rating',)
