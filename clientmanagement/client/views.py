
from pyexpat import model
from .models import *
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView,UpdateView,DeleteView

# Create your views here.


### INDUSTRY CRUD #############

#List All Industry
class DisplayIndustry(ListView):
    model=Industry
    template_name='industry/all_industry.html'
    
    def get_context_data(self, **kwargs):
        context = super(DisplayIndustry, self).get_context_data(**kwargs)
        context['industries']=Industry.objects.all()
        return context
    
# Add New Industry

class CreateIndustry(CreateView):
    model=Industry
    template_name='industry/form.html'
    fields='__all__'
    success_url=reverse_lazy('industries')
   
   
# Update Industry

class UpdateIndustry(UpdateView):
    model=Industry
    template_name='industry/updateform.html'
    fields='__all__'
    success_url=reverse_lazy('industries')

# Delete Industry
class DeleteIndustry(DeleteView):
     model=Industry
     success_url= reverse_lazy('industries')
     
     
     
############## SERVICE CATEGORY CRUD ##########

#list of all service categories

class DisplayServicesCategories(ListView):
    model=ServicesCategory
    template_name='services/all_services.html'
    
    def get_context_data(self, **kwargs):
        context = super(DisplayServicesCategories, self).get_context_data(**kwargs)
        context['services']=ServicesCategory.objects.all()
        return context


# Create New Categories
 
class CreateServicesCategories(CreateView):
    model=ServicesCategory
    template_name='services/form.html'
    fields='__all__'
    success_url=reverse_lazy('services')
    
    
# Update New Services Categories
 
class UpdateServicesCategories(UpdateView):
    model=ServicesCategory
    template_name='services/updateform.html'
    fields='__all__'
    success_url=reverse_lazy('services')

# Delete Services
class DeleteServicesCategories(DeleteView):
    model=ServicesCategory
    success_url=reverse_lazy('services')
    
########## CLIENT CRUD #############

#List Of All client

class DisplayAllClient(ListView):
    model=Client
    template_name='client/all_clients.html'
    
    def get_context_data(self, **kwargs):
        context = super(DisplayAllClient, self).get_context_data(**kwargs)
        context['clients']=Client.objects.all()
        return context

#Create New Clients
class CreateClient(CreateView):
    model=Client
    template_name='client/form.html'
    fields='__all__'
    success_url=reverse_lazy('clients')
    
#Update Client

class UpdateClient(UpdateView):
    model=Client
    template_name='client/updateform.html'
    fields='__all__'
    success_url=reverse_lazy('clients')
    
class DeleteClient(DeleteView):
    model=Client
    success_url=reverse_lazy('clients')
    

############ PROJECT URL ###############

#List Of All Projects

class DisplayProjects(ListView):
    model=Project
    template_name='project/all_projects.html'
    
    def get_context_data(self, **kwargs):
        context = super(DisplayProjects, self).get_context_data(**kwargs)
        context['projects']=Project.objects.all()
        return context
    

#Create New Project
    
class CreateProjects(CreateView):
    model=Project
    template_name='project/formcreate.html'
    fields='__all__'
    success_url=reverse_lazy('projects')
    
# Update Project

class UpdateProject(UpdateView):
    model=Project
    template_name='project/updateform.html'
    fields='__all__'
    success_url=reverse_lazy('projects')
    
# Delete Project
class DeleteProject(DeleteView):
    model=Project
    success_url=reverse_lazy('projects')
    
    
######### DISPLAY ALL PROJECTS ##############

class AllProjects(ListView):
    model=Project
    template_name='project/all_project.html'
    
    def get_context_data(self, **kwargs):
        context = super(AllProjects, self).get_context_data(**kwargs)
        context['projects']=Project.objects.all()
        return context