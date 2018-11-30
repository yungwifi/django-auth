import rest_framework
         
from . import models
                                                     
class UserSerializer(rest_framework.serializers.ModelSerializer):
    id = rest_framework.serializers.CharField(source='hash_id', read_only=True)
                             
    class Meta:
        model = models.User
        fields = ('id','username')