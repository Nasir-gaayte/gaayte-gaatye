from django.urls import path
from core import views
from core.views import AddPost,PostDetail,HomeView


urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.about,name='about'),
    path('team/',views.team,name='team'),
    # path('add_post/',views.add_post,name='add_post'),
    path('add_post/',views.AddPost.as_view(),name='add_post'),
    # path('details/<int:pk>/',views.details,name='details'),
    path('details/<int:pk>/',views.PostDetail.as_view(),name='details'),
]
