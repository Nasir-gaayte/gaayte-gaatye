from gc import get_objects
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import PostForm
from .models import PostModel
from django.views import generic 
from django.views.generic import DetailView, ListView, TemplateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import  reverse_lazy 


# Create your views here.

# class beast views to show all in home is ===========

class HomeView(generic.TemplateView):
    model = PostModel
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = PostModel.objects.order_by('-id')
        return context
      


#========================================================

# functions pased view for home page 


# def home (request):
#     posts = PostModel.objects.all()

#     return render(request,'core/home.html',{'posts':posts})

#=============================================================



def about(request):
    return render(request,'core/about.html')    


def team(request):
    return render(request,'core/team.html')    


#========================= Add Post =======================
# def add_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect ('home')
#         else:
#             messages.error(request,'wrong')
#             return redirect('home')
#     form = PostForm()
#     return render(request,'core/add_post.html',{'form':form}) 

# @login_required
class AddPost(generic.CreateView):
    model: PostModel
    form_class= PostForm
    template_name= 'core/add_post.html'
    reverse_lazy= 'home/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
#=================================================================


#======================== Detail of the post =====================

# def details(request, pk):
#     post= PostModel.objects.filter(id=pk)
    
#     return render(request,'core/details.html',{'post':post})


class PostDetail(generic.DetailView):
    model = PostModel
    template_name = 'core/details.html'
    context_object_name= 'post'

    

class UpdatePost(generic.UpdateView):
    model = PostModel
    form_class = PostForm 

    template_name= 'core/update_post.html'    



class DeletePost(generic.DeleteView):
    model = PostModel
    # form_class = PostForm 

    template_name= 'core/delete_post.html'
    success_url= reverse_lazy('home')
   