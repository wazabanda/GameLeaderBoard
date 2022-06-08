
from django.urls import path,include
from . import views as v

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Leader Board API",
#         default_version='v1',
#         description="A Leader Board API By WAZA_DEV for making leader Boards in games easily",
#         terms_of_service="non",
#         contact=openapi.Contact(email="1wazabanda@gmail.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
urlpatterns = [

    path("getBoardData/<token>/",v.getBoardData),
    path("addBoardItem/<token>/",v.addBoardItem),
    #path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]