from django.db import models

class Goal(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('in_progress', 'Em progresso'),
        ('done', 'Concluída'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    progress = models.PositiveIntegerField(default=0)  # 0 a 100
    created_at = models.DateTimeField(auto_now_add=True)

    def is_late(self):
        from django.utils.timezone import now
        return self.deadline < now().date() and self.status != 'done'

    def __str__(self):
        return self.title
