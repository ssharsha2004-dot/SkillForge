from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from students.views import home, add_student, profile, edit_profile, resources
from accounts.views import register, user_login, user_logout

urlpatterns = [

path(
    "profile/",
    profile,
    name="profile"
),

path(
    "edit-profile/",
    edit_profile,
    name="edit_profile"
),

path(
    "resources/",
    resources,
    name="resources"
),

path(
'',
home
),

path(
'add/',
add_student
),

path(
'register/',
register
),

path(
'login/',
user_login
),

path(
'logout/',
user_logout
),

path(
'admin/',
admin.site.urls
),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )