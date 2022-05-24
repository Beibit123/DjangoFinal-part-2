from django.contrib import admin
from django.urls import path, include

from onlinestore.views import *
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', obtain_jwt_token),
    path('books/', BookListAPIView.as_view(), name = 'book'),
    path('journals/', JournalListAPIView.as_view(), name = 'journal'),
    path('books/<int:pk>/', BookViewSet.as_view(), name = 'singlebook'),
    path('journals/<int:pk>/', JournalViewSet.as_view(), name = 'singlejournal')
]