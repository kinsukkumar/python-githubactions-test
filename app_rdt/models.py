from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

RDT_CONFIG_DB_SCHEMA = ''
if settings.RDT_CONFIG_DB_SCHEMA and len(settings.RDT_CONFIG_DB_SCHEMA) > 0:
    RDT_CONFIG_DB_SCHEMA = settings.RDT_CONFIG_DB_SCHEMA
    print('RDT_CONFIG_DB_SCHEMA:', RDT_CONFIG_DB_SCHEMA)

########## General Model ##########
#class Post(models.Model):
#    title = models.CharField(max_length=100)
#    content = models.TextField()
#    date_posted = models.DateTimeField(default=timezone.now)
#    author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#    def get_absolute_url(self):
#        return reverse('post-detail', kwargs={'pk': self.pk})
#    class Meta:
#        managed = False
#        app_label = 'app360'
#        db_table = AIMS_CONFIG_DB_SCHEMA + '].[app360_post'  

########## Custom Permission Model ##########
class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    # content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        app_label = 'app360'
        db_table = RDT_CONFIG_DB_SCHEMA + '].[auth_permission'
        unique_together = (('codename'),)

class RdtLog(models.Model):
    transaction_datetime = models.DateTimeField()
    log_type = models.CharField(max_length=100, blank=True, null=True)
    application_name = models.CharField(max_length=100, blank=True, null=True)
    event_type = models.CharField(max_length=200, blank=True, null=True)
    source_address = models.CharField(max_length=200, blank=True, null=True)
    source_hostname = models.CharField(max_length=200, blank=True, null=True)
    source_user = models.CharField(max_length=200, blank=True, null=True)
    source_object = models.CharField(max_length=500, blank=True, null=True)
    destination_address = models.CharField(max_length=500, blank=True, null=True)
    destination_hostname = models.CharField(max_length=200, blank=True, null=True)
    destination_user = models.CharField(max_length=200, blank=True, null=True)
    destination_object = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    message = models.CharField(max_length=2000, blank=True, null=True)
    other = models.CharField(max_length=1024, blank=True, null=True)
    remark = models.CharField(max_length=4000, blank=True, null=True)
    last_upd_date = models.DateTimeField(blank=True, null=True)
    last_upd_by_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'app_rdt'
        db_table = RDT_CONFIG_DB_SCHEMA + '].[rdt_log'
        
########## Home Page Model ##########    
class RdtAnnouncement(models.Model):
    subject = models.CharField(max_length=1024, blank=True, null=True)
    content = models.CharField(max_length=2048, blank=True, null=True)
    last_upd_date = models.DateTimeField(blank=True, null=True)
    last_upd_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        app_label = 'app_rdt'
        db_table = RDT_CONFIG_DB_SCHEMA + '].[rdt_announcement'



########## databrick Model ########## 
class DataReadiness(models.Model):
    area = models.CharField(max_length=255, blank=True, null=True, primary_key=True)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    data_date = models.CharField(max_length=255, blank=True, null=True)
    data_volumn = models.CharField(max_length=255, blank=True, null=True)
    last_upd_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False        
        app_label = 'databrick'
        db_table = 'data_readiness'