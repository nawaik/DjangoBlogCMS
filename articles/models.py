from django.db import models
from django.shortcuts import reverse

from users.models import CustomUser

class Articles(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now=True)
    title = models.CharField(blank=False, max_length=80)
    text = models.TextField(blank=False, max_length=3000)
    meta_title = models.CharField(blank=True, max_length=150)
    meta_description = models.CharField(blank=True, max_length=300)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("artikeldetail", kwargs={"pk": self.pk})
    