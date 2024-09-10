
from django.urls import path,include
from app import views


urlpatterns = [
    path('firstRender/',views.firstRender,name="firstRender"),
    path('firstRender1/',views.firstRender1,name="firstRender1"),
    path('firstRender2/',views.firstRender2,name="firstRender2"),
    path('firstRender3/',views.firstRender3,name="firstRender3")
]