from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    index = models.IntegerField()
    alt_text = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title