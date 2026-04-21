from django.contrib import admin
from .models import Post

# Registering the post model so I can manage security logs
admin.site.register(Post)
