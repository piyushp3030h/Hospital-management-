from django.urls import path
from . import views

urlpatterns = [

    # API Routes
    path('', views.get_routes),

    # Department APIs
    path('departments/', views.get_departments),
    path('departments/<int:pk>/', views.get_department),

    # Patient APIs
    path('patients/', views.get_patients),
    path('patients/<int:pk>/', views.get_patient),

    # Record APIs
    path('records/', views.get_records),
    path('records/<int:pk>/', views.get_record),
]