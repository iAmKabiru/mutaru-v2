from .models import Project
import django_filters



class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Project
        fields = ['title', 'lga', 'ministry','date']