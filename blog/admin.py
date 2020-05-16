from django.contrib import admin
from .models import Post

# Register your models here.
# This makes our model visible on the admin page.
# See https://docs.djangoproject.com/en/2.2/ref/contrib/admin/

admin.site.register(Post)
