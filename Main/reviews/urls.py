from django.urls import path
from .views import review_list_view, ReviewListCreate, ReviewReply

urlpatterns = [
    path('reviews/', review_list_view, name='review_list_view'),
    path('api/reviews/', ReviewListCreate.as_view(), name='list_create_reviews'),
    path('api/reviews/<int:id>/reply/', ReviewReply.as_view(), name='reply_review'),
]