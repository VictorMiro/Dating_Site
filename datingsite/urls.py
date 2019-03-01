"""datingsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib import admin

from datingcore import views
from datingcore.views import HomePageView, Register, ThankYouView, ProfileView, SearchFormView, \
    EditUserProfileView, SuccessfulEditView, FriendsRelationView, change_friends

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='homepage'),
    path('registration/', Register.as_view(), name='registration'),
    path('registration/registration_successfully/', ThankYouView.as_view(), name='thank_you'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', ProfileView.as_view(), name='profile_view'),
    path('profile/edit/', EditUserProfileView.as_view(), name='profile_edit_view'),
    path('search/', SearchFormView.as_view(), name='search_view'),
    path('profile/edit/success/', SuccessfulEditView.as_view(), name='success_update'),
    path('friend_list/', FriendsRelationView.as_view(), name='change_friends'),
    re_path(r'^friend_list/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends_change')



]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

