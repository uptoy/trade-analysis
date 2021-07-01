from django.urls import path
from apps.accounts.views import UserProfile, Signup, PasswordChange, PasswordChangeDone, EditProfile, index

from django.contrib.auth import views as authViews
from .views import UserProfile



urlpatterns = [
    path('', index, name='index'),
    path('profile/<username>', UserProfile, name='profile'),
    path('profile/edit', EditProfile, name='edit-profile'),
    path('signup/', Signup, name='signup'),
    path('login/', authViews.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(), {'next_page': 'index'}, name='logout'),
    path('changepassword/', PasswordChange, name='change_password'),
    path('changepassword/done', PasswordChangeDone, name='change_password_done'),
    path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    path('passwordreset/done', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]