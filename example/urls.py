from example.views import BookViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls