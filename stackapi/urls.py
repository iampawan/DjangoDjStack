from django.urls import path, include
from .views import index, QuestionAPI, latest
from rest_framework import routers


router = routers.DefaultRouter()
router.register("questions", QuestionAPI)

urlpatterns = [
    path('', index, name="index"),
    path('', include(router.urls)),
    path('latest', latest, name="latest"),
]
