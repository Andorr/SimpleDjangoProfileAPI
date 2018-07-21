from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ A serializer for the ProfileFeedItem."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

class ProfileMessageSerializer(serializers.ModelSerializer):
    """ A serializer for the ProfileMessage"""

    class Meta:
        model = models.ProfileMessage
        fields = ('id', 'user_profile', 'to_profile', 'message', 'time')
        extra_kwargs = {'user_profile': {'read_only': True}}

class PostSerializer(serializers.ModelSerializer):
    """ A serializer for the posts"""
    poster = UserProfileSerializer(read_only=True)
    likes = serializers.IntegerField()
    
    class Meta:
        model = models.Post
        fields = ('id', 'text', 'time', 'poster', 'likes')


class PostLikeSerializer(serializers.ModelSerializer):
    """ A serializer for liking of posts"""

    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = models.PostLike
        fields = ('id', 'post', 'user',)
        unique_together = ('post', 'user')
       

