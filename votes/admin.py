from django.contrib import admin
from .models import Candidate, Votes

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Votes)
