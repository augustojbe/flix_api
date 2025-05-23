from django.db.models.signals import pre_save
from movies.models import Movies
from django.dispatch import receiver
from gemini_ai.cliente import get_movie_resumo

@receiver(pre_save, sender=Movies)
def movie_pre_save(sender, instance, **kwargs):
    if not instance.resumo:
        genero = instance.genre.name
        ai_resumo = get_movie_resumo(instance.title, genero)
        instance.resumo = ai_resumo



