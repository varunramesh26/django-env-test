from django.urls import path, include
from . import views

urlpatterns = [
    #path('comm/', views.farmerinfo_list),
    #path('comm/<int:pk>', views.farmerinfo_detail),
    path('comm/', views.FarmerInfoList.as_view(), name='farmers_list')
]