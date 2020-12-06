"""Users views."""
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import views as auth_views

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from posts.models import Post, Profile

# Forms
from users.forms import ProfileForm, SignupForm

# Create your views here.


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    # Login Required
    login_url = 'login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class LoginView(auth_views.LoginView):
    """Login View."""
    template_name = 'users/login.html'


class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html' # This view is never rendered bc it goes straight to the redirected url


class SignUpView(FormView):
    """Users sign up view."""
    model = Profile
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self, queryset=None):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


"""Logout Function View."""
# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('users:login')


"""Login Function View"""
# def login_view(request):
#     """Login view."""
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('posts:feed')
#         else:
#             return render(request, 'users/login.html', {'error': 'Invalid username and password'})
#     return render(request, 'users/login.html')

"""Signup Function View"""
# def signup(request):
#     """Signup view."""
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#
#     else:
#         form = SignupForm()
#
#     return render(request, 'users/signup.html', context={'form': form})

"""Update Profile Function View"""
# @login_required
# def update_profile(request):
#     """Update profile view."""
#     profile = request.user.profile
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#
#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             profile.picture = data['picture']
#             profile.save()
#
#             url = reverse('users:detail', kwargs={'username': request.user.username})
#             return redirect(url)
#     else:
#         form = ProfileForm()
#
#     return render(request, 'users/update_profile.html',
#                   context={
#                       'profile': profile,
#                       'user': request.user,
#                       'form': form,
#                   })
