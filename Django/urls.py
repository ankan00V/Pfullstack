from project.urls import path
from .views import LPU, about

urlpatterns = [
    path('',LPU,name="land"),
    path('about',about,name="about")
]