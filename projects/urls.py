from rest_framework import routers
from .apiViewSets import ProjectViewSet

# Este router.defaultrouter me crea un crud con la ruta (GET, POST, PUT, DELETE)
router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls