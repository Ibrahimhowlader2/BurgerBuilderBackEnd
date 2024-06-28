from rest_framework.serializers import ModelSerializer
from BurgerApi.models import UserProfile, Order, Ingredient, CustomarDetails


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        # fields = "__all__"
        exclude = ['id']


class CustomarDetailSerializer(ModelSerializer):

    class Meta:
        model = CustomarDetails
        # fields = "__all__"
        exclude = ['id']
   
        
class OrderSerializer(ModelSerializer):
    ingredient = IngredientSerializer()
    customar = CustomarDetailSerializer()

    class Meta:
        model = Order
        fields = "__all__"
        
    def create(self,validated_data):
        ingredient_data = validated_data.pop("ingredient")
        customar_data = validated_data.pop("customar")
        ingredient = IngredientSerializer.create(IngredientSerializer(),validated_data=ingredient_data)
        customar = CustomarDetailSerializer.create(CustomarDetailSerializer(),validated_data=customar_data)
        order,created = Order.objects.update_or_create(
            ingredient=ingredient,
            customar=customar,
            price = validated_data.pop("price"),
            orderTime = validated_data.pop("orderTime"),
            user = validated_data.pop("user"),
            )
        return order
        
