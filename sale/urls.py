from django.urls import path

from sale import views

urlpatterns = [
    path('sale/', views.SaleView.as_view(), name='products'),
    path('sale/<int:id>', views.SaleDetailView.as_view(), name='products'),

]