from django.urls import include, path

urlpatterns = [
    path('users/', include('user.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]