from rest_framework import serializers
from .models import (Services, About, Activity, SubActivity, Projects, WhatOurClientsSay,
                     GetInContactSection, ClientsReviews, ClientsEmail, Partners)


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class SubActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubActivity
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    sub_activities = SubActivitySerializer(many=True)

    class Meta:
        model = Activity
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ProjectsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['name', 'number']


class WhatOurClientSaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatOurClientsSay
        fields = '__all__'


class GetInContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetInContactSection
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsReviews
        fields = '__all__'


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'


class ClientsEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsEmail
        fields = '__all__'