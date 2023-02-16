from rest_framework.routers import DefaultRouter

from apps.products.api.views.product_views import ProductViewset

router = DefaultRouter()

router.register(r'product', ProductViewset, basename='products')

urlpatterns = router.urls