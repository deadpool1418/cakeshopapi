from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authtoken.models import Token

class seriToken(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
        
class seriUser(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    def create(self,validate_data):
        user = User.objects.create_user(validate_data['username'],validate_data['email'],validate_data['password'])
        return user
    class Meta:
        model = User
        fields = ['id','email','username','password']

class seriImage(serializers.ModelSerializer):
    class Meta:
        model = Imagemodel
        fields = '__all__'

class seriCake(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()
    # def get_image(self,obj):
    #     request = self.context.get('request')
    #     image_path = obj.image.image.url
    #     return request.build_absolute_uri(image_path)
    class Meta:
        model = cake
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        data['image'] = request.build_absolute_uri(seriImage(Imagemodel.objects.get(pk=data['image'])).data['image'])
        data['owner'] = seriUser(User.objects.get(pk=data['owner'])).data
        del data['owner']['password']
        return data

class seriCart(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = '__all__'

class seriOrder(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['cakes']=seriCart(cart.objects.filter(id__in = data['cakes']),many=True).data
        return data

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         try:
#             data = super().validate(attrs)
#             refresh = self.get_token(self.user)
#             data['refresh'] = str(refresh)
#             data['access'] = str(refresh.access_token)
#             data['email']= str(self.user.username)
#             data['username']=data['email']
#             data['id']=self.user.id
#             print(self.user.id,"idd...............")
#             return data
#         except:
#             print("Unathorized acces!!!!")
#             data ={}
#             data['message']='Invalid User Credentials'
#             return data