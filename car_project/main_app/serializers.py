from rest_framework import serializers

from .models import Country, Manufacturer, Car, Comments
from django.contrib.auth import get_user_model

User = get_user_model()


class AddCountrySerializer(serializers.ModelSerializer):

    name = serializers.CharField(min_length=3, max_length=100)

    def validate(self, validated_data):
        name = ["name"]
        if Country.objects.filter(uname=name).exists():
            raise serializers.ValidationError(f"Страна {name} уже существует")
        return validated_data

    class Meta:
        model = Country
        fields = ["name"]

    def create(self, validated_data):
        country = Country.objects.create(**validated_data)
        return country


class AddManufacturerSerializer(serializers.ModelSerializer):

    name = serializers.CharField(min_length=3, max_length=100)
    country = AddCountrySerializer()

    def velidate(self, validated_data):
        name = ["name"]
        if Manufacturer.objects.filter(uname=name).exists():
            raise serializers.ValidationError(f"Производитель {name} уже существует")
        return validated_data

    class Meta:
        model = Manufacturer
        fields = "__all__"

    def create(self, validated_data):
        manufacturer = Manufacturer.objects.create(**validated_data)
        return manufacturer


class AddCarSerializer(serializers.ModelSerializer):

    name = serializers.CharField(min_length=3, max_length=100)
    year_of_release = serializers.DateField()
    year_of_graduation = serializers.DateField()
    manufacturer = AddManufacturerSerializer()

    def validate(self, validated_data):
        name = ["name"]
        if Car.objects.filter(uname=name).exists():
            raise serializers.ValidationError(f"Aвтомобиль {name} уже существует")
        return validated_data

    class Meta:
        model = Car
        fields = "__all__"

    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        return car


class AddCommentSerializer(serializers.ModelSerializer):

    author_email = serializers.EmailField()
    created_at = serializers.DateTimeField()
    text_comment = serializers.CharField()
    car = AddCarSerializer()

    class Meta:
        model = Comments
        fields = "__all__"

    def create(self, validated_data):
        comment = Comments.objects.create(**validated_data)
        return comment


class UpdateCountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class UpdateManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.country = validated_data.get("country", instance.country)
        instance.save()
        return instance


class UpdateCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.year_of_release = validated_data.get(
            "year_of_release ", instance.year_of_release
        )
        instance.year_of_graduation = validated_data.get(
            "year_of_graduation", instance.year_of_graduation
        )
        instance.manufacturer = validated_data.get(
            "manufacturer", instance.manufacturer
        )
        instance.save()
        return instance


class UpdateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.author_email = validated_data.get(
            "author_email", instance.author_email
        )
        instance.created_at = validated_data.get("created_at", instance.created_at)
        instance.text_comment = validated_data.get(
            "text_comment", instance.text_comment
        )
        instance.car = validated_data.get("car", instance.car)
        instance.save()
        return instance


class GetCountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3, max_length=100)

    class Meta:
        model = Country
        fields = "__all__"


class GetManufacturerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3, max_length=100)
    country = GetCountrySerializer()

    class Meta:
        model = Manufacturer
        fields = "__all__"


class GetCarSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3, max_length=100)
    year_of_release = serializers.DateField()
    year_of_graduation = serializers.DateField()
    manufacturer = GetManufacturerSerializer()

    class Meta:
        model = Car
        fields = "__all__"


class GetCommentSerializer(serializers.ModelSerializer):
    author_email = serializers.EmailField()
    created_at = serializers.DateTimeField()
    text_comment = serializers.CharField()
    car = GetCarSerializer()

    class Meta:
        model = Comments
        fields = "__all__"
