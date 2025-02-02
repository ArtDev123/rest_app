from django.db import models

class Man(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    categoty = models.ForeignKey('Category', on_delete=models.PROTECT, null = True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields = ['-time_create'])
        ]
    
    
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name