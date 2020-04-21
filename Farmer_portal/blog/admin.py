from django.contrib import admin
from .models import Post
from .models import Like
from .models import Query
from .models import Query_Answer

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Query)
admin.site.register(Query_Answer)

