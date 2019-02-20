from django.db.models import Manager


class PostManager(Manager):

    def sort_by_data(self):
        return self.get_queryset().filter("-date_of")
