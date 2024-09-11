from django.shortcuts import render,redirect
from .models import Review
from rest_framework import generics, permissions
from .models import Review, Business
from .serializers import ReviewSerializer


class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user:
            return Review.objects.filter(business__owner=user)
        return Review.objects.none()

    def perform_create(self, serializer):
        serializer.save()

class ReviewReply(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(reply=self.request.data.get('reply'))

    def post(self, request, *args, **kwargs):
        review = self.get_object()
        review.reply = request.POST.get('reply')
        review.save()
        return redirect('review_list_view')


def review_list_view(request):
    user = request.user
    has_business = Business.objects.filter(owner=user).exists()
    reviews = Review.objects.filter(business__owner=request.user.id)
    if has_business:
        return render(request, 'reviews/review_list.html', {'reviews': reviews})
    else:
        return redirect('business_details')