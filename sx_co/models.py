from django.db import models

class Customer(models.Model):
    # گزینه‌های وضعیت مشتری
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('lost', 'Lost'),
    ]

    # ستون‌های جدول مشتری
    name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True) # ثبت خودکار تاریخ عضویت

    def __str__(self):
        return self.name

    def get_avatar_initials(self):
        names = self.name.split()
        if len(names) >= 2:
            return f"{names[0][0]}{names[1][0]}".upper()
        return self.name[0:2].upper()


class Note(models.Model):
    # ستون‌های جدول یادداشت
    tag = models.CharField(max_length=50, default='General')
    content = models.TextField()
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tag} - {self.created_at.strftime('%H:%M')}"