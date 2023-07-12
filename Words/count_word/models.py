from django.db import models


class FileRequest(models.Model):
    file = models.FileField(upload_to="uploads")
    word_to_find = models.CharField(max_length=64)
