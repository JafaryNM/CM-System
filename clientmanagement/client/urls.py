
from unicodedata import name
from django.urls import path
from .views import * 

urlpatterns = [
    
    
  ######### INDUSTRY CRUD  URLS ########################
    
    path('industies/',DisplayIndustry.as_view(), name='industries'),
    path('industry/create/',CreateIndustry.as_view(), name='createindustry' ),
    path("industry/<int:pk>/update/", UpdateIndustry.as_view(), name='industryupdate'),
    path("Industry/<int:pk>/delete/",DeleteIndustry.as_view(), name='industrydelete'),
    
   ########### SERVICE CRUD URLS ########################
   path('services/',DisplayServicesCategories.as_view(), name='services' ),
   path('services/create',CreateServicesCategories.as_view(), name='createservices'),
   path('services/<int:pk>/update/',UpdateServicesCategories.as_view(), name='serviceupdate'),
   path('services/<int:pk>/delete', DeleteServicesCategories.as_view(), name='servicedelete'),
   
   ########## CLIENT CRUD URLS ###################
   path('clients/',DisplayAllClient.as_view(), name='clients'),
   path('client/create',CreateClient.as_view(), name='createclient'),
   path('client/<int:pk>/update/>',UpdateClient.as_view(), name='clientupdate'),
   path('client/<int:pk>/delete/>',DeleteClient.as_view(), name='clientdelete'),
   
   ########### PROJECTCRUD URLS ###################

    path ('',DisplayProjects.as_view(), name='projects' ),
    path ('project/create',CreateProjects.as_view(), name='createproject'),
    path ('project/<int:pk>/update', UpdateProject.as_view(), name='projectupdate'),
    path('project/<int:pk>/delete',DeleteProject.as_view(), name='projectdelete'),
    path('projectall/',AllProjects.as_view(), name='project_all')
   
   
   
    
    
    
    
    
    
]