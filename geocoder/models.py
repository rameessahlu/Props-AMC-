from django.db import models
import uuid

class AddressBook(models.Model):
    ab_id = models.CharField(primary_key=True, unique=True, editable=False, max_length=5)
    #models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.CharField(max_length=100)
    excel_file = models.FileField(upload_to="uploaded_add_books/excel/")
    geocode_generated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ab_id)

    def save(self, **kwargs):
        if not self.ab_id:
            self.ab_id = 'ABM{}'.format(AddressBook.objects.count()+1)
        super().save(*kwargs)