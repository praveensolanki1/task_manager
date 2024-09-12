from django.urls import path
from .views import task_list, task_create, task_update, task_delete, task_toggle_complete, signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('update/<int:task_id>/', task_update, name='task_update'),
    path('delete/<int:task_id>/', task_delete, name='task_delete'),
    path('toggle/<int:task_id>/', task_toggle_complete, name='task_toggle_complete'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='task/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
