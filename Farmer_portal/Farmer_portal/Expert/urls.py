from django.urls import path
from Expert.views import login, auth_view, logout,loggedin, invalidlogin,varify,userdoesnotexist,updatedans,register,submitanswer,allansQuery,updateQueryans,expertverify
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
url(r'^login/$', login),
url(r'^auth/$', auth_view),
url(r'^logout/$', logout),
url(r'^loggedin/$', loggedin),
url(r'^invalidlogin/$', invalidlogin),
url(r'^register/$', register),
url(r'^varify/$', varify),
url(r'^updatedans/$', updatedans),
url(r'^expertverify/$', expertverify),
url(r'^updateQueryans/$', updateQueryans),
url(r'^allansQuery/$', allansQuery),
url(r'^submitanswer/$', submitanswer),
url(r'^userdoesnotexist/$', userdoesnotexist),
]