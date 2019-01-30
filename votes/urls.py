from django.urls import path
from . import views

app_name = 'candidate'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:candidate_id>/', views.detail, name='detail'),
    path('<int:candidate_id>/update', views.update, name='update'),
    path('<int:candidate_id>/comment', views.comment, name='comment'),
    path('create/', views.create, name='create'),
]
