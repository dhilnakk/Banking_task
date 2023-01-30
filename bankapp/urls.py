from django.urls import path

from  .import views
app_name="bankapp"
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('account/',views.account,name='account'),
    path('update/',views.update,name='update'),
    path('logout/',views.logout,name='logout'),
    path('branches/',views.branches,name='branches'),
]
