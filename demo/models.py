from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField('标题',max_length=50)
    content = RichTextField('内容',blank=True,null=True)
    publish_date = models.DateField()

    def __unicode__(self):
        return self.name