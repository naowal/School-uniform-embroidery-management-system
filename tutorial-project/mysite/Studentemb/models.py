from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import IntegerField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class StudentEmbInfo(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    firstname = models.CharField(max_length=100)
    lastname = models.TextField(max_length=100)
    schoolname = models.CharField(max_length=100)
    moreinfo = models.TextField(max_length=500)
    status = models.IntegerField(default = 0)
    color = models.CharField(max_length=30)
    create_by = models.CharField(max_length=30)
    price_baht = models.IntegerField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Studentemb_studentembinfo_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Studentemb_studentembinfo_update', args=(self.slug,))


class user(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('Studentemb_user_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('Studentemb_user_update', args=(self.slug,))


