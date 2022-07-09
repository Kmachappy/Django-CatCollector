# NOTHING IN HERE
# all routes go in here not in the cat collector urls
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/',views.about, name='about'),
  path('cats/', views.cats_index, name='cats'),
  path('cats/<int:cat_id>', views.cats_detail, name='detail'),
  path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
  path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
  path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
]
