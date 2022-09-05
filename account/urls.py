from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout_view,name='logout'),
    path('register',views.register,name='register'),
    path('update',views.account_view,name='update'),
    
    # Copy
    # path('', home_screen_view, name="home"),
    # path('account/', account_view, name="account"),
    # path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls', 'blog')),
    # path('login/', login_view, name="login"),
    # path('logout/', logout_view, name="logout"),
	# path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
    # path('register/', registration_view, name="register"),

    # # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='my_tmp/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='my_tmp/password_change.html'), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    #  name='password_reset_complete'),    
]