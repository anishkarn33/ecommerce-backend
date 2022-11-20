from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets 

# Serializers define the API representation.
class CatalogSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name','last_name','email',]

# ViewSets define the view behavior.
class Index(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CatalogSerializers

class Login(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CatalogSerializers
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', Index)
router.register(r'users', Login)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]