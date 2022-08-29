

from email.mime import image
from rest_framework import serializers




from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    email = serializers.StringRelatedField(source='user.email')
    class Meta:
        model = Post 
        fields = ['email', 'title', 'discription', 'post_date']
       
class CommentSerilizer(serializers.ModelSerializer):
    email = serializers.StringRelatedField(source='user.email')
    class Meta:
        model = Comment
        fields = ['email', 'comment', 'comment_date']   


class ShowOwnPostSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()
    # def get_image(self, obj):
    #         return self.context['request'].build_absolute_uri( obj.image.url)
    email = serializers.StringRelatedField(source='user.email')

    class Meta:
        model = Post 
        fields = ['email', 'title',  'discription', 'post_date']
    


        
