from django.urls import path
from . import views
from .views import LayoutDataView, FeedbackPostCreateView, ProductGet

urlpatterns = [
    # Другие URL-маршруты
    path('all-slides/', views.AllSlides.as_view(), name='all-slides'),
    path('layoutdata/', LayoutDataView.as_view(), name='layout-data'),
    path('feedback/', FeedbackPostCreateView.as_view(), name='feedback-create'),
    path('product/', ProductGet.as_view(), name='product-all'),
]
