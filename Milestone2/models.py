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

class Checkout(models.Model):
    #REGEX for phone number validation
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    firstname = models.CharField(max_length=1000, blank=False)
    lastname = models.CharField(max_length=1000, blank=False)
    address = models.CharField(max_length=254, blank = False)
    phonenumber = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    numberofstudents = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=False)
    createdon = models.DateTimeField(null = True, blank = True)
    fulfilledon = models.DateField(null = True, blank = True)
    returnedon = models.DateField(null = True, blank = True)
    missingparts = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return str(self.lastname) + ', ' + str(self.firstname)

    class JSONAPIMeta:
        resource_name = "checkouts"


class Item(models.Model):
    partname = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items', blank=False)
    description = models.TextField(max_length=1000, blank=False)
    checkedoutto = models.ForeignKey(Checkout, on_delete=models.CASCADE, related_name='items', null = True, blank=True)

    def __str__(self):
        return str(self.partname)

    class JSONAPIMeta:
        resource_name = "items"

class Category(models.Model):
    categoryname = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.categoryname)

    class JSONAPIMeta:
        resource_name = "categories"

class Profile(models.Model):
    UNL = 'unl'
    UNO = 'uno'
    UNMC = 'unmc'
    UNK = 'unk'
    ORG_OTHER = 'other'
    ORG_CHOICES = (
        (UNL, 'University of Nebraska - Lincoln'),
        (UNO, 'University of Nebraska - Omaha'),
        (UNMC, 'University of Nebraska Medical Center'),
        (UNK, 'University of Nebraska - Kearney'),
        (ORG_OTHER, 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org = models.CharField(max_length=30, choices=ORG_CHOICES, default=UNO)
    college = models.CharField(max_length=1000, blank=True)
    dept = models.CharField(max_length=1000, blank=True)
    otherdetails = models.CharField(max_length=1000, blank=True)
    areasofinterest = models.ManyToManyField('Areaofinterest', related_name='profiles', blank=True)

    def __str__(self):
        return str(self.user.username)


class Award(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    description = models.TextField(blank=True)
    awardlink = models.URLField(max_length=1000, blank=False)
    sponsororg = models.CharField(max_length=1000, blank=True)

    recurring = models.BooleanField(default=False)
    nomreq = models.BooleanField(default=False)
    recurinterval = models.CharField(max_length=1000, blank=True)
    opendate = models.DateTimeField()
    nomdeadline = models.DateTimeField()
    submdeadline = models.DateTimeField()

    additionalinfo = models.TextField(blank=True)

    previousapplicants = models.IntegerField(default=0, blank=False)
    createdon = models.DateTimeField(auto_now_add=True)

    # Relationships
    source = models.ForeignKey('Source', related_name='awards', on_delete=models.PROTECT, blank=True)
    stemfields = models.ManyToManyField('Stemfield', related_name='awards', blank=True)
    applicanttypes = models.ManyToManyField('Applicanttype', related_name='awards', blank=True)
    awardpurposes = models.ManyToManyField('Awardpurpose', related_name='awards', blank=True)
    createdby = models.ForeignKey('Profile', related_name='awards', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.title)

    class JSONAPIMeta:
        resource_name = "awards"

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
