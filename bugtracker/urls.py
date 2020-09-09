"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from bug_app import views

urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('ticket/<int:ticket_id>/', views.ticket_view, name="ticket_detail"),
    path('addticket/', views.create_ticket_view, name="addticket"),
    path('assign/<int:ticket_id>', views.assign_view, name="assign"),
    path('completed/<int:ticket_id>', views.completed_view, name="completed"),
    path('invalid/<int:ticket_id>', views.invalid_view, name="invalid"),
    path('user/<str:username>', views.user_view, name="userdetail"),
    path('edit/<int:ticket_id>',views.edit_view,name="edit"),
    path('admin/', admin.site.urls),
]
