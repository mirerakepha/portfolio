from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='HOME'),
    path('ABOUT/', views.about_view, name='ABOUT'),
    path('PORTFOLIO/', views.portfolio_view, name='PORTFOLIO'),
    path('SKILLS/', views.skills_view, name='SKILLS'),
    path('RESUME/', views.resume_view, name='RESUME'),
]
