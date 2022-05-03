from django.db import models
from django.db.models.deletion import CASCADE

class NewsTag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "news_tag"


class News(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=5000)
    tag = models.ForeignKey(NewsTag, on_delete=CASCADE)
    pub_date = models.DateField()
    class Meta:
        db_table = 'news'
