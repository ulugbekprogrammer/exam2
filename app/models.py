from django.db import models
from django.conf import settings
from django.core.mail import send_mail


# Create your models here.
class EmailMessage(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.EmailField()

    def __str__(self):
        return self.subject
    
    def save(self, *args, **kwargs):
        send_mail(self.subject, self.body,  settings.EMAIL_HOST_USER, [self.sent_at])
        super(EmailMessage, self).save(*args, **kwargs)