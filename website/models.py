from django.db import models
from django.contrib.auth.models import User

from social.apps.django_app.default.models import UserSocialAuth
from scipy2017 import settings
import os

def get_document_dir(instance, filename):
    # ename, eext = instance.user.email.split("@")
    fname, fext = os.path.splitext(filename)
    print "----------------->",instance.user
    return '%s/attachment/%s/%s.%s' % (instance.user, instance.proposal_type, fname+'_'+str(instance.user), fext)

class Proposal(models.Model):
    user = models.ForeignKey(User)
    about_me = models.TextField(max_length=500)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length = 20)
    title = models.CharField(max_length=250)
    abstract = models.TextField(max_length=700)
    prerequisite = models.CharField(max_length=750)
    duration = models.CharField(max_length = 100)
    attachment = models.FileField(upload_to=get_document_dir)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 100, default='Pending', editable=True)
    proposal_type = models.CharField(max_length = 100)
    tags = models.CharField(max_length = 250)

class Ratings(models.Model):
    proposal = models.ForeignKey(Proposal)
    user = models.ForeignKey(User)
    rating = models.CharField(max_length=700)
    
class Comments(models.Model):
    proposal = models.ForeignKey(Proposal)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=700)
    # rate = models.CharField(max_length =100)
