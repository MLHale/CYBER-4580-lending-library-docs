# @Author: Matthew Hale <matthale>
# @Date:   2018-02-28T00:25:25-06:00
# @Email:  mlhale@unomaha.edu
# @Filename: models.py
# @Last modified by:   matthale
# @Last modified time: 2018-03-05T14:15:06-06:00
# @Copyright: Copyright (C) 2018 Matthew L. Hale



from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from rest_framework_json_api import serializers
from django.core.validators import *

# Note: the OneToOneField here ‘inherits’ the User model from django.contrib.auth
# 	the django.contrib.auth.models.User can handel roles with its is_staff, is_admin, user_permissions fields
#	user_permissions is a ManyToMany relationship with django.contrib.auth.models.Permission 
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	org = models.ForeignKey(Organization, blank=False)

class Organization(models.Model):
	name = models.CharField(max_length=1000, blank=False)
	address1 = models.CharField(max_length=1000, blank=False)
	address2 = models.CharField(max_length=1000, blank=False)
	city = models.CharField(max_length=100, blank=False)
	state = models.CharField(max_length=2, blank=False)
	zip = models.CharField(max_length=20, blank=False)
	
class Order(models.Model):
	user = models.ForeignKey(User, blank=False)
	ORDER_STATUS_CHOICES = (
		(CART, 'In Cart'),
		(ORDERED,'Ordered'),
		(INFUL, 'In Fulfillment'),
		(FUL, 'Fulfilled'),
		(SHIPPED, 'Shipped'),
		(RECIEVED, 'Return Recieved'),
		(RETURNED, 'Returned'),
	)
	status = models.CharField(max_length=100, blank=False) choices=ORDER_STATUS_CHOICES
	createdon = models.DateTimeField(null = True, blank = True)
	fulfilledon = models.DateField(null = True, blank = True)
	returnedon = models.DateField(null = True, blank = True)
	missingparts = models.TextField(max_length=1000, blank=True)

	
	
# class OrderItemsRel(models.Model):
#	order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False)
#	item = models.ForeignKey(Item, related_names='items', blank=False)


class Item(models.Model):
	type = models.ForeignKey(ItemType, blank=False)
	barcode = models.CharField(max_length=100, blank=True)
	ITEM_STATUS_CHOICES = (
		(AVAIL, 'Available'),
		(CO,'Checked Out'),
		(BROKE, 'Broken'),
		(MISSING, 'MISSING'),
		(NOTRET, 'Not Returned'),
	)
	status = models.CharField(max_length=100, blank=False) choices=ITEM_STATUS_CHOICES
	owner = models.ForeignKey(User, blank=False)
	order = models.ManyToManyField(Order)
	checkedoutto = models.ForeignKey(User)
	
class ItemType(models.Model):
	name = models.CharField(max_length=200, blank=False)
	description = models.TextField(max_length=1000, blank=False)

class Package(models.Model):
	name = models.CharField(max_length=200, blank=False)
	description = models.TextField(max_length=1000, blank=False)
	items = models.ManyToManyField( 
		ItemType,
		through='PackageItemRel',
		through_fields=('package', 'itemtype'),
	)
	
	
class PackageItemRel(models.Model):
	package = models.ForeignKey(Package, blank=False)
	itemtype = models.ForeignKey(Item, blank=False)
	quantity = models.IntegerField(blank=False)



class Source(models.Model):
    # Award Source choices
    # FED = 'federal'
    # LOCAL = 'local'
    # STATE = 'state'
    # PRIV = 'private_industry'
    # INT = 'internal'
    # SOURCE_OTHER = 'other'
    # AWARD_SOURCE_CHOICES = (
    #     (FED, 'Federal Government'),
    #     (STATE,'State Government'),
    #     (LOCAL, 'Local Government'),
    #     (INT, 'Internal'),
    #     (PRIV, 'Private Industry'),
    #     (SOURCE_OTHER, 'Other')
    # )
    name = models.CharField(max_length=100, blank=False, unique=True) #choices=AWARD_SOURCE_CHOICES, default=SOURCE_OTHER,

    def __str__(self):
        return str(self.name)

    class JSONAPIMeta:
        resource_name = "sources"

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id','name')


class Applicanttype(models.Model):
    name = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.name)

	class JSONAPIMeta:
		resource_name = "applicanttypes"

class ApplicanttypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicanttype
        fields = ('id','name')


class Stemfield(models.Model):
    name = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.name)

	class JSONAPIMeta:
		resource_name = "stemfields"

class StemfieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stemfield
        fields = ('id','name')


class Awardpurpose(models.Model):
    name = models.CharField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return str(self.name)

	class JSONAPIMeta:
		resource_name = "awardpurposes"

class AwardpurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awardpurpose
        fields = ('id','name')


class Areaofinterest(models.Model):
    name = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.name)

	class JSONAPIMeta:
		resource_name = "areaofinterests"

class AreaofinterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areaofinterest
        fields = ('id','name')


class UserSerializer(serializers.ModelSerializer):
    lastname = serializers.CharField(source='last_name')
    firstname = serializers.CharField(source='first_name')
    issuperuser = serializers.CharField(source='is_superuser')
    class Meta:
		resource_name = 'users'
		model = User
		fields = ('id', 'username', 'lastname', 'firstname', 'email', 'issuperuser')

class InternalItemSerializer(serializers.ModelSerializer):
    #owner = UserSerializer(read_only = True)
    #checkedoutto = CheckoutSerializer(read_only = True)
    included_serializers = {'owner': UserSerializer,}

    class Meta:
        model = Item
        fields = ('id', 'partname', 'owner', 'description')

    class JSONAPIMeta:
        included_resources = ['owner']


class CheckoutSerializer(serializers.ModelSerializer):
    items = InternalItemSerializer(read_only = True, many = True)
    #included_serializers = {'items', InternalItemSerializer}

    class Meta:
        model = Checkout
        fields = ('id', 'items', 'firstname', 'lastname', 'address', 'phonenumber', 'numberofstudents', 'createdon', 'fulfilledon', 'returnedon', 'missingparts' )

    class JSONAPIMeta:
        included_resources = ['items']

class ItemSerializer(serializers.ModelSerializer):
    #owner = UserSerializer(read_only = True)
    #checkedoutto = CheckoutSerializer(read_only = True)
    included_serializers = {'owner': UserSerializer, 'checkedoutto': CheckoutSerializer,}

    class Meta:
        model = Item
        #fields = ('id', 'partname', 'owner', 'description', 'checkedoutto')
        fields = '__all__'

    class JSONAPIMeta:
        included_resources = ['owner', 'checkedoutto']

class ProfileSerializer(serializers.ModelSerializer):
    included_serializers = {
        'user': UserSerializer,
        'areasofinterest': AreaofinterestSerializer
    }

    class Meta:
        model = Profile
        fields = ('id', 'org', 'college', 'dept', 'otherdetails','user', 'areasofinterest')


    class JSONAPIMeta:
		included_resources = ['user']

class AwardSerializer(serializers.ModelSerializer):
    included_serializers = {
        'createdby': ProfileSerializer,
        'applicanttypes': ApplicanttypeSerializer,
        'awardpurposes': AwardpurposeSerializer,
        'stemfields': StemfieldSerializer,
        'source': SourceSerializer
    }

    class Meta:
        model = Award
        fields = ('id', 'title', 'description', 'awardlink','sponsororg', 'recurring','nomreq','recurinterval','opendate','nomdeadline','submdeadline','additionalinfo','source','previousapplicants','createdon','createdby','applicanttypes','awardpurposes','stemfields')


    class JSONAPIMeta:
		included_resources = ['createdby','applicanttypes', 'awardpurposes','stemfields','source']

