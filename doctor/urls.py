from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('Doctor', views.DoctorViewset)
router.register('Review', views.ReviewViewset)
router.register('Designation', views.DesignationViewset)
router.register('Specialization', views.SpecializationViewset)
router.register('Available_time', views.AvailableTimeViewset)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    
]
