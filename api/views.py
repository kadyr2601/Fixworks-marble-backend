from rest_framework import views, response
from .models import (Services, About, Activity, Projects, WhatOurClientsSay,
                     GetInContactSection, ClientsReviews, ClientsEmail, Partners)
from .serializers import (ServicesSerializer, AboutSerializer, ActivitySerializer,
                          ProjectsSerializer, ProjectsNameSerializer, WhatOurClientSaySerializer,
                          GetInContactSerializer, ReviewsSerializer, PartnersSerializer, ClientsEmailSerializer)


class ServicesView(views.APIView):
    def get(self, request):
        services = Services.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return response.Response(serializer.data)


class AboutUsView(views.APIView):
    def get(self, request):
        about = About.objects.first()
        serializer = AboutSerializer(about)
        return response.Response(serializer.data)


class ActivitiesView(views.APIView):
    def get(self, request):
        activities = Activity.objects.first()
        serializer = ActivitySerializer(activities)
        return response.Response(serializer.data)


class ProjectsGalleryView(views.APIView):
    def get(self, request):
        projects = Projects.objects.all().order_by('number')
        serializer = ProjectsSerializer(projects, many=True)
        return response.Response(serializer.data)


class ProjectsNameView(views.APIView):
    def get(self, request):
        project = Projects.objects.all().values('name', "number").order_by('number')
        serializer = ProjectsNameSerializer(project, many=True)
        return response.Response(serializer.data)


class WhatOurClientsSayView(views.APIView):
    def get(self, request):
        clients = WhatOurClientsSay.objects.first()
        serializer = WhatOurClientSaySerializer(clients)
        return response.Response(serializer.data)


class GetInContactView(views.APIView):
    def get(self, request):
        data = GetInContactSection.objects.first()
        serializer = GetInContactSerializer(data)
        return response.Response(serializer.data)


class ReviewsView(views.APIView):
    def get(self, request):
        reviews = ClientsReviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return response.Response(serializer.data)


class PartnersView(views.APIView):
    def get(self, request):
        partners = Partners.objects.all()
        serializer = PartnersSerializer(partners, many=True)
        return response.Response(serializer.data)


class ClientsEmailView(views.APIView):
    def post(self, request):
        serializer = ClientsEmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=201)
        return response.Response(serializer.errors, status=400)
