from django.urls import path
from rest_framework import routers
# from . import views
from .api import ItemViewSet

router = routers.DefaultRouter()

router.register('api/items', ItemViewSet, 'items')

urlpatterns = router.urls

# urlpatterns = [
#     path('items', views.getItems),
#     path('item/<int:id>', views.getItem),
#     path('addItem', views.addItem),
#     path('deleteItem/<int:id>', views.deleteItem)
# ]
