from django.db import models

class Diary(models.Model):
    first_text = models.CharField(max_length=25)
    second_text = models.CharField(max_length=25)
    third_text = models.CharField(max_length=25)
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '\n1: ' + self.first_text + '\n2: ' + self.second_text + '\n3: ' + self.third_text + '\n'
    
