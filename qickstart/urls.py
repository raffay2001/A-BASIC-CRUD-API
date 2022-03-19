from django.contrib import admin
from django.urls import path,include
from app.views import employeeListView, userListView, employeeDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees/', employeeListView),
    path('api/employees/<int:pk>', employeeDetailView),
    path('api/users/', userListView)
]
