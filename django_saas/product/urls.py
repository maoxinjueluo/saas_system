from django.conf.urls import url
from product.unit.add_unit import AddUnit

urlpatterns = [
    url(r'^add_unit$', AddUnit.as_view()),  # add unit
]
