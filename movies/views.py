from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from movies.models import Movies
from movies.serializer import MovieModelSerializer
from app.permissions import GlobalDefaultPermission
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()


    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_starts = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(data={

            'total_moviea': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_starts': round(average_starts, 1) if average_starts else 0,
            },
          status=status.HTTP_200_OK,
        )

