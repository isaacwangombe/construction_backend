from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Item,Supplier
from .serializer import ItemSerializer, SupplierSerializer, ProjectSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password




# @permission_classes([IsAuthenticated])		
# def ProjectList(request):
#   user = request.user					
#   notes = user.project_set.all()				
#   serializer = ProjectSerializer(notes, many=True)
#   return Response(serializer.data)


# @permission_classes([IsAuthenticated])		
# def UserList(request):
#   # user = request.user					
#   notes = User.objects.all()				
#   serializer = UserSerializer(notes, many=True)
#   return Response(serializer.data)

class UserList(APIView):
  def get(self, request, format=None):
    notes = User.objects.all()				
    serializer = UserSerializer(notes, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializers = UserSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save(password=make_password("2385791"))
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])		
class ProjectList(APIView):
  def get(self, request, format=None):
    user = request.user
    all_projects = user.project_set.all()	
    serializers = ProjectSerializer(all_projects, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = SupplierSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplierList(APIView):
  def get(self, request, format=None):
    all_supplier = Supplier.get_all()
    serializers = SupplierSerializer(all_supplier, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = SupplierSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#### Items Serialisers ----------------------------------------------------------------


# ## General--------------------------------------------------------------------------------
class ItemList(APIView):
  def get(self, request, format=None):
    all_item = Item.get_all()
    serializers = ItemSerializer(all_item, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = ItemSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemsByProjectList(APIView):
  def get(self, request,project, format=None):
    items = Item.filter_by_project(project)
    serializers = ItemSerializer(items, many=True)
    return Response(serializers.data)

class ItemsBySupplierList(APIView):
  def get(self, request,project,supplier, format=None):
    items = Item.filter_by_supplier(supplier, project)
    serializers = ItemSerializer(items, many=True)
    return Response(serializers.data)

class ItemsByDateList(APIView):
  def get(self, request,project, date, format=None):
    items = Item.filter_by_date(date, project)
    serializers = ItemSerializer(items, many=True)
    return Response(serializers.data)


class ItemsById(APIView):
  def get(self, request,id, format=None):
    item = Item.get_by_id(id)
    serializers = ItemSerializer(item, many=False)
    return Response(serializers.data)

  def delete(self, request,id, format=None):
    item = Item.get_by_id(id)
    item.delete()    
    return Response({'message': 'item was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

  def patch(self, request,id, format=None):
    item = Item.get_by_id(id)
    serializers = ItemSerializer(item, data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


### By Item and Project ------------------------------------------------------------------------------------------------


class ItemsByProjectAndId(APIView):
  def get(self, request,project, id, format=None):
    items = Item.get_by_project_and_id(project, id)
    serializers = ItemSerializer(items, many=True)
    return Response(serializers.data)


### Calculation results -------------------------------------------------------------


class TotalPrice(APIView):
		def get(self, request,project):
			total_price = Item.total_price_by_project(project)
			return Response({"total_price":total_price})



class PriceByItem(APIView):
		def get(self, request,project):
			price_by_item = Item.total_price_by_items_project(project)
			return Response(price_by_item)

class AvgByItem(APIView):
		def get(self, request,project):
			price_by_item = Item.avg_price_by_items(project)
			return Response({"price_by_item":price_by_item})

class QtyByItem(APIView):
		def get(self, request,project):
			qty_by_item = Item.total_quantity_by_item(project)
			return Response({"qty_by_item":qty_by_item})

class PriceByItemSupplier(APIView):
		def get(self, request,project):
			price_by_item = Item.total_price_by_items_supplier(project)
			return Response({"price_by_item":price_by_item})

class AvgPriceByItemSupplier(APIView):
		def get(self, request,project):
			price_by_item = Item.average_price_by_items_supplier(project)
			return Response({"price_by_item":price_by_item})

class PriceBySupplier(APIView):
		def get(self, request,project):
			price_by_supplier = Item.total_price_by_supplier(project)
			return Response({"price_by_supplier": price_by_supplier})

class PriceByDate(APIView):
		def get(self, request,project):
			price_by_date = Item.total_price_by_date(project)
			return Response({"price_by_date":price_by_date})

class PriceByMonth(APIView):
		def get(self, request,project):
			price_by_month = Item.total_price_by_month(project)
			return Response({"price_by_month":price_by_month})

class PriceByYear(APIView):
		def get(self, request,project):
			price_by_year = Item.total_price_by_year(project)
			return Response({"price_by_year":price_by_year})



class TotalPriceByDateRange(APIView):
		def get(self, request,project,date, date2):
			total_amount_by_date_range = Item.total_amount_by_date_range(project,date, date2)
			return Response({"total_amount_by_date_range":total_amount_by_date_range})


