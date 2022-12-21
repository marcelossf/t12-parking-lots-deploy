from django.urls import path
from . import views
from floors import views as floor_views
from vehicles import views as vehicles_views

urlpatterns = [
    path('parking-lots/', views.ParkingLotView.as_view()),
    path('parking-lots/<int:parking_lot_id>', views.ParkingLotDetailView.as_view()),
    path('parking-lots/<int:parking_lot_id>/floors/', floor_views.FloorView.as_view()),
    path('parking-lots/<int:parking_lot_id>/vehicles/', vehicles_views.VechicleView.as_view()),

]
