from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name="southbike-home"),
    path('empresa/<str:company>/', views.Company, name="southbike-company"),
    path('galeria1/<str:gallery>/', views.Gallery, name="southbike-gallery"),
    path('galeria2/<str:galleryone>/', views.GalleryOne, name="southbike-gallery-one"),
    path('galeria3/<str:gallerytwo>/', views.GalleryTwo, name="southbike-gallery-two"),
    path('painel/<str:representative>/', views.Representative, name="southbike-representative"),
    path('registre/<str:record>/', views.Record, name="southbike-registre-sua-bicicleta"),
    path('urbans/<str:urbans>/', views.Urbans, name="southbike-urbans"),
    path('freeride/<str:freeride>/', views.Freeride, name="southbike-freeride"),
    path('infantil-1/<str:infantilone>/', views.InfantilOne, name="southbike-infantil-one"),
    path('infantil-2/<str:infantiltwo>/', views.InfantilTwo, name="southbike-infantil-two"),
    path('mountainbike-1/<str:mountainbikeone>/', views.MountainBikeOne, name="southbike-mtb-one"),
    path('mountainbike-2/<str:mountainbiketwo>/', views.MountainBikeTwo, name="southbike-mtb-two"),
    path('mountainbike-3/<str:mountainbikethree>/', views.MountainBikeThree, name="southbike-mtb-three"),
]
