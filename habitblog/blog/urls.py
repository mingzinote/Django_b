
from django.urls import path
from .views import HabitListView, HabitDetailView, HabitCreateView,
HabitUpdateView, HabitDeleteView
from django.contrib.auth import views as auth_views
from .views import SignUpView           # views에서 SignUpView를 임포트




urlpatterns = [
    path('', HabitListView.as_view
(), name='habit_list'),
    path('habit/<int:pk>/',
HabitDetailView.as_view(), name='
habit_detail'),
    path('habit/new/',
HabitCreateView.as_view(), name='
habit_create'),
    path('habit/<int:pk>/delete/',
HabitDeleteView.as_view(), name='
habit_delete'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'), 
]
    