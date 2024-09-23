from django.contrib import admin
from django.urls import path,include

from .import views

urlpatterns = [
    path('', views.home),
    path('client/<int:id>',views.clientdetails),
    path('createclient',views.client_create),
    path('Project/<int:id>',views.projectdetails),
    path('createproject',views.project_create),
    path('client_list', views.client_list),
    path('project_details', views.project_details),
    path('deleteclient/<int:id>', views.deleteclient),
    path('deleteProject/<int:id>', views.deleteProject),
    # path('upadateclient/<int:id>', views.updateclientdata),
    path('update/<int:id>/', views.updateclient),

]