from django.db import models
from django.db.models import F, Q, Count, Avg
from datetime import timedelta
from datetime import datetime

class ArtistManager(models.Manager):
    def with_tracks_about_love(self):
        '''Returns Artists who have Albums which have tracks whose title
        contains the word "Love".

        Docs:
          topics/db/queries/#lookups-that-span-relationships
        '''
        return super().get_queryset().filter(album__track__title__contains="Love")



class AlbumManager(models.Manager):
    def earliest_released(self):
        '''Returns Album with earliest release_date.
        
        Docs:
          ref/models/querysets/#order-by
        '''
        return super().get_queryset().all().order_by('release_date')[0]


    def with_tracks_about_love(self):
        '''Returns Albums which have tracks whose title contains the word
        "Love".

        Docs:
          topics/db/queries/#lookups-that-span-relationships
        '''
        return super().get_queryset().filter(track__title__contains="Love")

    def released_in_month(self, month):
        '''Returns Albums whose release_date matches the given month.

        Docs:
          ref/models/querysets/#month
        '''
        return super().get_queryset().filter(month=2)


    def purchased_on_day_of_release(self):
        '''Returns Albums whose purchase_date is equal to the release_date.

        Docs:
          topics/db/queries/#filters-can-reference-fields-on-the-model
          ref/models/expressions/#f-expressions
        '''
        return super().get_queryset().filter(release_date__exact=F('purchase_date'))


    def purchased_after_day_of_release(self):
        '''Returns Albums whose purchase_date is after the release_date.

        Docs:
          ref/models/expressions/#f-expressions
        '''
        return super().get_queryset().filter(release_date=(F('purchase_date')-timedelta(days=1)))


    def with_more_than_one_artist(self):
        '''Returns Albums with more than one Artist.

        Docs:
          topics/db/aggregation/#generating-aggregates-for-each-item-in-a-queryset
        '''
        return super().get_queryset().all()

    def with_highest_rating(self):
        '''Returns Album with highest rating.

        Docs:
          ref/models/querysets/#order-by
        '''
        return super().order_by('-rating')[0:1]


    def with_highest_average_track_rating(self):
        '''Returns Album with highest average track rating.

        Docs:
          topics/db/aggregation/#generating-aggregates-for-each-item-in-a-queryset
        '''

        return super().annotate(sred=Avg('track__rating')).order_by('-sred')[0]


class TrackManager(models.Manager):
    def with_five_stars(self):
        '''Returns Tracks with rating of 5

        Docs:
          topics/db/queries/#retrieving-specific-objects-with-filters
        '''
        return super().get_queryset().filter(rating=5)


    def with_more_than_twenty_listens(self):
        '''Returns Tracks with more than 20 listens.

        Docs:
          topics/db/queries/#field-lookups
        '''

        return super().get_queryset().filter(listens__gt=20)


    def n_most_listened_to(self, n):
        '''Returns n Tracks with most listens.

        Docs:
          topics/db/queries/#limiting-querysets
        '''
        return super().get_queryset().all().order_by('-listens')[0:2]



    def about_love(self):
        '''Returns Tracks whose title contains the word "Love".

        Docs:
          topics/db/queries/#field-lookups
        '''
        return super().get_queryset().filter(title__contains='Love')

    def not_about_love(self):
        '''Returns Tracks whose title does not contain the word "Love".

        Docs:
          topics/db/queries/#retrieving-specific-objects-with-filters
        '''
        return super().get_queryset().exclude(title__contains="Love")

    def with_one_star_or_zero_listens(self):
        '''Returns Tracks which have either 0 listens or a rating of 1 (or
        both).

        Docs:
          topics/db/queries/#complex-lookups-with-q-objects
        '''
        return super().get_queryset().filter(Q(listens__exact=0)|Q(rating__exact=1))
