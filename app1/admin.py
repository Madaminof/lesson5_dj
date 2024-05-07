from django.contrib import admin
from .models import Books,Books_Category,Author,Review
# Register your models here.
admin.site.register(Books)
admin.site.register(Books_Category)
admin.site.register(Author)
admin.site.register(Review)
