from django.urls import path

from . import views

urlpatterns = [
    path('container_yard_status', views.containerYardStatus),
    path('import', views.imp),
    path('export', views.exp),
    path('unpack', views.unpack),

    path('import_search', views.import_search_m),
    path('export_search', views.export_search),
]