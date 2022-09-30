from django.contrib import admin
from .models import PostModel, Category

# Register your models here.


admin.site.register(PostModel)
admin.site.register(Category)