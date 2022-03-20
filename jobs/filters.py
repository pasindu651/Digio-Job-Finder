import django_filters
from .models import *

class JobFilter(django_filters.FilterSet):
    #start_date = DateFilter(filter_name="time", lookup_expr="gte")
    #end_date = DateFilter(filter_name="time", lookup_expr="lte")
    class Meta:
        model = Job
        exclude = ['slug', 'manager_email', 'description', 'applicants', 'time']
