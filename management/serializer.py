from rest_framework import serializers
from .models import Item,Supplier, Project
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('__all__')

class SupplierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Supplier
    fields = ('id', 'supplier', 'phone')


class ItemSerializer(serializers.ModelSerializer):

  class Meta:
    model = Item
    fields = ('__all__' )

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ('__all__' )