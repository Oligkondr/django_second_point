"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from books import views
from books.views import BooksView

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', BooksView.as_view(), name='book_list'),
    # path('<int:book_id>/', BooksView.as_view(), name='book_list'),
    path('new/', views.create, name='create'),
]
