from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.detail import DetailView


from .forms import SignUpForm, EditProfileForm, LoginForm
from .models import User


# used in 'profile/' url to redirect user
def redirect_to_user_details(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to=f"{request.user.pk}/")
    return HttpResponseRedirect(redirect_to="/")


class UserEdit(UpdateView):
    """
    User can edit his/her details
    """
    model = User
    template_name = 'user-edit.html'
    context_object_name = 'user'
    form_class = EditProfileForm
    success_url = '/accounts/profile/'


class UserDetails(DetailView):
    """
    User can see his/her details
    """
    model = User
    template_name = 'user-details.html'
    context_object_name = 'user'


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/'
    template_name = 'signup.html'


class LogIn(LoginView):
    model = User
    form_class = LoginForm
    success_url = '/'
    template_name = 'login.html'
