from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('people/<str:username>/', views.people, name="people"),
    path('update', views.update, name="update"),
    path('delete', views.delete, name='delete'),
    path('password', views.password, name="password"),
    path('profile_update', views.profile_update, name="profile_update"),
    path('<int:user_id>/follow/', views.follow, name="follow"),
]