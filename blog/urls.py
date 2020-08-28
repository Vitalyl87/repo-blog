from django.urls import path
from .views import  *
from .import views
urlpatterns=[
    path('blog/', Blog.as_view(), name="blog"),
    path('new/', New.as_view(), name="add_article"),
    #path('blog/<int:pk>/', ArticleDetailView.as_view(), name='get_detail')
    path('blog/<slug:pk>/', ArticleDetailView.as_view(), name='get_detail')
]