import graphene
from graphene_django import DjangoObjectType
from .models import ShiftType, Warehouse, ItemPattern, ShiftLog, Items

class ShiftTypeType(DjangoObjectType):
    class Meta:
        model = ShiftType

class WarehouseType(DjangoObjectType):
    class Meta:
        model = Warehouse

class ItemPatternType(DjangoObjectType):
    class Meta:
        model = ItemPattern

class ShiftLogType(DjangoObjectType):
    class Meta:
        model = ShiftLog

class ItemsType(DjangoObjectType):
    class Meta:
        model = Items

class Query(graphene.ObjectType):
    all_shift_types = graphene.List(ShiftTypeType)
    all_warehouse = graphene.List(WarehouseType)
    all_item_pattern = graphene.List(ItemPatternType)
    all_shift_log = graphene.List(ShiftLogType)
    all_items_type = graphene.List(ItemsType)