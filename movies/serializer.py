from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movies
from genres.models import Genre
from actors.serializer import ActorSerializer
from genres.serializer import GenereSerializer


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        return value

    def validate_resumo(self, value):
        if len(value) > 250:
            raise serializers.ValidationError('O campo de resumo do filme não pode ter mais de 250 caracteres.')
        return value

class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenereSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resumo']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
          return round(rate, 1)
        return None





