from django.urls import path
from . import views


urlpatterns = [

    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),  # 수정페이지 Path 지정
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/new_comment/', views.new_comment),  # urls.py 경로추가
    path('<int:pk>/', views.PostDetail.as_view()),  # p번째 페이지로 이동
    path('', views.PostList.as_view()),
    # path('<int:pk>/', views.single_post_page),  # p번째 페이지로 이동
    # path('', views.index),
    # path('', views.index)
]
