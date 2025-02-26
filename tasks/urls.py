from django.urls import path
from tasks.views import manager_dashboard, user_dashboard,test,dashboard
# from .views import home   # This is the same as the line above

urlpatterns = [
    path('dashboard/', dashboard),
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/', user_dashboard),
    path('test/', test),
]