from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Slide, FeedbackPost, Product
from .serializers import SlideSerializer, LayoutDataSerializer, FeedbackPostSerializer, ProductSerializer


class LayoutDataView(APIView):
    def get(self, request):
        serializer = LayoutDataSerializer(context={'request': request})
        header_data = serializer.get_header()  # Вызываем метод get_header без аргументов
        footer_data = serializer.get_footer()
        data = {
            'header': header_data,
            'footer': footer_data,
        }
        return Response(data, status=status.HTTP_200_OK)


class AllSlides(APIView):
    def get(self, request, format=None):
        slides = Slide.objects.all()
        serializer = SlideSerializer(slides, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FeedbackPostCreateView(generics.CreateAPIView):
    queryset = FeedbackPost.objects.all()
    serializer_class = FeedbackPostSerializer


class ProductGet(APIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get(self, request):
        products = self.get_queryset()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)