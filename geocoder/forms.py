from django import forms

from .models import AddressBook

class AddressBookForm(forms.ModelForm):
    class Meta:
        model = AddressBook
        fields = ('file_name', 'excel_file')
        widgets = {
            'file_name': forms.TextInput(attrs={
                'id': 'file-name', 
                'class': 'file-name form-control form-control-lg"', 
                'required': True, 
                'placeholder': 'File name...'
            }),
            'excel_file': forms.FileInput(attrs={
                'id': 'excel-file', 
                'class': 'excel-file form-control form-control-lg"', 
                'required': True, 
            }),
        }