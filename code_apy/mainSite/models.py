from django.db import models

# Create your models here.

class Module(models.Model):
    
    title = models.CharField(max_length=200)
    module_number = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    
class Lesson(models.Model):
    
    lesson_title = models.CharField(max_length=200)
    lesson_code_text = models.TextField()
    lesson_psudo_code = models.TextField()
    lesson_plain_text = models.TextField()
    needs_psudo = models.BooleanField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    def __str__(self):
        return self.lesson_title