from django.db import models

# Create your models here.

class Module(models.Model):
    
    title = models.CharField(max_length=200)
    module_number = models.IntegerField(default=0)
    
    
class Lesson(models.Model):
    
    
    lesson_code_text = models.TextField()
    lesson_psudo_code = models.TextField()
    lesson_plain_text = models.TextField()
    lesson_text = models.TextField(default="no lesson text")
    
    needs_psudo = models.BooleanField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)