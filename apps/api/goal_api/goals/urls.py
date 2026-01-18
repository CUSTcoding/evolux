from .views import GoalViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'goals', GoalViewSet)

urlpatterns = router.urls
