from django.urls import path, include
from . import views, api_views, auth_views
from .auth_views import MyTokenObtainPairView
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)




urlpatterns = [
  path('', views.welcome,name = 'test'),
  path('items/<project>/<id>', views.welcome2,name = 'test2'),


  ## Authentication apis
  path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

  path('api/users', api_views.UserList.as_view()),
  path('api/projects', api_views.ProjectList.as_view()),
  path('api/suppliers', api_views.SupplierList.as_view()),
  path('api/items', api_views.ItemList.as_view()),

  path('api/item/project/<project>', api_views.ItemsByProjectList.as_view()),
  path('api/item/project/<project>/id/<id>', api_views.ItemsByProjectAndId.as_view()),

  path('api/item/project/<project>/date/<date>', api_views.ItemsByDateList.as_view()),
  path('api/item/project/<project>/supplier/<supplier>', api_views.ItemsBySupplierList.as_view()),
  path('api/item/<id>', api_views.ItemsById.as_view()),

  ## Calculation apis

  path('api/total_price_by_project/<project>', api_views.TotalPrice.as_view()),
  path('api/total_item_price_by_project/<project>', api_views.PriceByItem.as_view()),
  path('api/avg_price_by_item/<project>', api_views.AvgByItem.as_view()),
  path('api/qty_by_item/<project>', api_views.QtyByItem.as_view()),
  path('api/price_by_item_supplier/<project>', api_views.PriceByItemSupplier.as_view()),
  path('api/avg_price_by_item_supplier/<project>', api_views.AvgPriceByItemSupplier.as_view()),
  path('api/total_price_by_supplier/<project>', api_views.PriceBySupplier.as_view()),
  path('api/total_price_by_date/<project>', api_views.PriceByDate.as_view()),
  path('api/total_price_by_month/<project>', api_views.PriceByMonth.as_view()),
  path('api/total_price_by_year/<project>', api_views.PriceByYear.as_view()),
  path('api/total_amount_by_date_range/<project>/<date>/<date2>', api_views.TotalPriceByDateRange.as_view()),


]
