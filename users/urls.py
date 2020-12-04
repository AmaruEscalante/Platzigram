"""Users URLs."""

# Django
from django.urls import path

# View
from users import views

urlpatterns = [

    # Posts
    path(
        route='<str:username>',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # Management
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('me/profile/', views.update_profile, name='update'),
]
