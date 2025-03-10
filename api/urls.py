from django.urls import path
from .views import (ServicesView, AboutUsView, ActivitiesView, ProjectsGalleryView,
                    ProjectsNameView, WhatOurClientsSayView, GetInContactView, ReviewsView,
                    PartnersView, ClientsEmailView)

urlpatterns = [
    path('services/', ServicesView.as_view()),
    path('about-us/', AboutUsView.as_view()),
    path('activities/', ActivitiesView.as_view()),
    path('projects/', ProjectsGalleryView.as_view()),
    path('projects-name/', ProjectsNameView.as_view()),
    path('what-our-clients-say/', WhatOurClientsSayView.as_view()),
    path('get-in-contact/', GetInContactView.as_view()),
    path('reviews/', ReviewsView.as_view()),
    path('partners/', PartnersView.as_view()),
    path("send-email", ClientsEmailView.as_view())
]