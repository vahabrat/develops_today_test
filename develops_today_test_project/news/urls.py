from django.urls import path
from . import views
from .views import PostCreateView, PostRetrieveView, PostUpdateView, PostDeleteView

app_name = 'news'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create_post'),
    #path('retrieve/', PostRetrieveView.as_view(), name='retrieve_post'),
    path('detail/<int:id>/', PostRetrieveView.as_view(), name='detail_post'),
    path('update/<int:id>/', PostUpdateView.as_view(), name='update_post'),
    path('delete/', PostDeleteView.as_view(), name='delete_post'),
]