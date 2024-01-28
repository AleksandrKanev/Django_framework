from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import update_product, img

urlpatterns = [
    path('products_update/', update_product, name='products_update'),
    path('img/<int:id_>', img, name='img'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
