from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import serializers

from api.models import Product, Category, Storage, Store


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'email', 'first_name', 'last_name']


class StoreSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = ['name', 'id', 'products']

    def get_products(self, obj):
        products = Product.objects.filter(store=obj)
        s = ProductSerializer(products, many=True, context=self.context)
        return s.data


class StorageSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Storage
        fields = ['name', 'id', 'products']

    def get_products(self, obj):
        products = Product.objects.filter(storage=obj)
        s = ProductSerializer(products, many=True, context=self.context)
        return s.data


class ProductSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'id','link', 'category', 'storage', 'store',
                  'sales_product_count', 'product_in_store',
                  'product_in_storage']

    def get_link(self, obj):
        uri = reverse("products-detail", kwargs={"pk": obj.pk})
        return self.context["request"].build_absolute_uri(uri)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'id']


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    password2 = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

    def create(self, validated_data):
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if password == password2:
            user = User.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"]
            )
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError(
                {"password": "Password are not the same"})
