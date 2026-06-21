from django import forms
from .models import  Customer, Note

# این فرم مستقیماً به دیتابیس متصل است
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer  # متصل به مدل دیتابیس Customer
        fields = ['name', 'company_name', 'phone_number', 'status'] # ستون‌هایی که کاربر باید پر کند


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note  # متصل به مدل دیتابیس Note
        fields = ['tag', 'content', 'is_pinned']