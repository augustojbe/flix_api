from django.contrib import admin
from movies.models import Movies

@admin.register(Movies)
class MovieAdm(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'resumo',)

    def ready(self):
        import movies.signals
