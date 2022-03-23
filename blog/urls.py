from django.urls import path
from . import views


urlpatterns = [

    path('<int:pk>/', views.PostDetail.as_view()),  # p번째 페이지로 이동
    path('', views.PostList.as_view()),
    # path('<int:pk>/', views.single_post_page),  # p번째 페이지로 이동
    # path('', views.index),
    # path('', views.index)
]
