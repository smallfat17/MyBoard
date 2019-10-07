from django.contrib import admin
from django.conf.urls import url, include
import django.contrib.auth.views as auth_views
from accounts import views as accounts_views

from boards import views as boards_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', boards_views.BoardListView.as_view(), name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # 带有表单的页面，哟个于启动重置过程；
    url(r'^reset/$', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'

    ), name='password_reset'),
    # ⼀个成功的页面，表示该过程已启动，指示用户检查其邮件⽂件夹等；
    url(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    # 检查通过电子邮件发送token的页面
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    # ⼀个告诉用户重置是否成功的页面
    url('^resest/complete/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),

    url(r'^boards/', include('boards.urls', namespace='boards')),
]
