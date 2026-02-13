from django.contrib import admin
from django.urls import path, include
# from app.urls import

from app.views import LPU,about
# from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
    # path('',LPU,name="land"),
    # path('/about',about,name="about")
]