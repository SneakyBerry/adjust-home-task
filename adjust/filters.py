from django.db.models import Sum
from django_filters import rest_framework as filters

from adjust.models import Adjust


class AdjustFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()
    group = filters.MultipleChoiceFilter(
        choices=(
            ("date", "date"),
            ("channel", "channel"),
            ("country", "country"),
            ("os", "os"),
        ),
        method="group_by_filter",
    )
    order = filters.OrderingFilter(
        fields=(
            "date",
            "channel",
            "country",
            "os",
            "impressions",
            "clicks",
            "installs",
            "spend",
            "revenue",
            "cpi",
        )
    )

    def group_by_filter(self, queryset, name, value):
        return queryset.values(*value).annotate(
            clicks=Sum("clicks"),
            spend=Sum("spend"),
            impressions=Sum("impressions"),
            installs=Sum("installs"),
            revenue=Sum("revenue"),
            cpi=Sum("cpi"),
        )

    class Meta:
        model = Adjust
        fields = ["channel", "country", "os"]
