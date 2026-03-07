from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserLoginApiView, UserRegistrationApiview,UserLogout

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('patient', views.PatientViewset)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    path("register/",UserRegistrationApiview.as_view(),name='register'),
    path("login/",UserLoginApiView.as_view(),name='login'),
    path("logout/", UserLogout.as_view(),name='logout'),
    path("active/<uid64>/<token>/",views.activate,name='active')
]
