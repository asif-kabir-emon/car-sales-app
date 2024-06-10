from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("brand/<slug:brand_slug>", home, name="brand_wise_cars"),
    path("user/", include("users.urls")),
    path("car/", include("cars.urls")),
    path("brand/", include("brands.urls")),
    path("order/", include("orders.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
