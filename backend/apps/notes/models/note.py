from django.db import models
from django.core.validators import MaxLengthValidator


class Note(models.Model):

    title = models.CharField(max_length=200, help_text='Enter the note title')

    content = models.TextField(max_length=600, validators=[MaxLengthValidator(1500)], help_text='Enter the content of the note.') 

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Create date')

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update date')

    class Meta:

        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created_at']

    
    def __str__(self):
        return self.title[:40]