from rest_framework import serializers
from main.models import Post

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model=Post
    fields=('id','title','slug','content','date','approved','user_id','closed','state')