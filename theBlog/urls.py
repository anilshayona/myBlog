from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, \
    UpdateCategoryView, DeleteCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    path('category/edit/<int:pk>', UpdateCategoryView.as_view(), name="update_category"),
    path('category/<int:pk>/delete', DeleteCategoryView.as_view(), name="delete_category"),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
]
