from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', BookingViewSet)

urlpatterns = [
    path('', index, name='home'),
    path('bookings/', include(router.urls)),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth', obtain_auth_token)
]