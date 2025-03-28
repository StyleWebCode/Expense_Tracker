from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),

    path('delete-transaction<id>/', views.delete_transaction, name='delete_transaction'),

]