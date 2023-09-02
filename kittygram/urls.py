from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet

router = SimpleRouter()

router.register('cats', CatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', ..., name='api-root'),
]







'''
# Обновлённый urls.py - дженерики
from django.urls import path

from cats.views import CatList, CatDetail

urlpatterns = [
    path('cats/', CatList.as_view()),
    path('cats/<int:pk>/', CatDetail.as_view()),
]





# Прошлая версия с вью-функциями
from django.urls import path

from cats.views import APICat

urlpatterns = [
   path('cats/', APICat.as_view()),
]
'''