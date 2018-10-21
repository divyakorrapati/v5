from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import logout, password_change as pwd_change, password_change_done as pwd_change_done, password_reset as reset, password_reset_done as reset_done, password_reset_confirm as reset_confirm, password_reset_complete as reset_complete
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    #path('', views.home, name='home'),
    #url(r'^home/$', views.home, name='home'),

    # change password urls
    #url(r'^password-change/$', pwd_change, name='password_change'),
    url(r'^password-change/done/$', pwd_change_done, name='password_change_done'),
    url(r'^password-change/$', pwd_change, {'post_change_redirect': '/password-change/done/'}, name='password_change'),


# restore password urls
    url(r'^password-reset/complete/$', reset_complete, name='password_reset_complete'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', reset_confirm, {'post_reset_redirect': '/password-reset/complete/'}, name='password_reset_confirm'),
    url(r'^password-reset/done/$', reset_done, name='password_reset_done'),
    url(r'^password-reset/$', reset, {'post_reset_redirect': '/password-reset/done/', 'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),


    url(r'^register/$', views.register, name='register'),
    path('', views.product_list, name='product_list'),
    #path('login/', views.user_login(), name='login'),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]