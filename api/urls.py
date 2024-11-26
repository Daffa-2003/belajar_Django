from django.urls import path

from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostList.as_view(), name='blogpost-list'),
    path('blogposts/<int:id>/', view=views.BlogPostRetrieverUpdateDestroy.as_view(), name="update")
]