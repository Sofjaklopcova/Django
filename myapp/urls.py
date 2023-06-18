from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('treneri/', views.TreneriListView.as_view(), name='treneri_list'),
path('treneri/<int:pk>', views.TrenerDetailView.as_view(), name='trener_detail'),
path('hraci/', views.HraciListView.as_view(), name='hraci_list'),
path('hraci/<int:pk>', views.HracDetailView.as_view(), name='hrac_detail'),
]