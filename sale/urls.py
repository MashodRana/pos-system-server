from django.urls import path

from sale import views

urlpatterns = [
    path('sale/', views.Sale.as_view(), name='products'),

]