from django.contrib import admin

from main import models

admin.site.register([
    models.Author,
    models.Article,
    
    
])