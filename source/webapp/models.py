from django.db import models

status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Note(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    text = models.TextField(max_length=3000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=status_choices, null=False, blank=False, default='active')

    class Meta:
        db_table = 'notes'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.id}. {self.name}: {self.status}'

# Create your models here.
