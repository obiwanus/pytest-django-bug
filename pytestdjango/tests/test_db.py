import pytest
from first.models import Model1
from second.models import Model2

pytestmark = pytest.mark.django_db


def test1():
    Model1.objects.create(name='blah1')
    Model2.objects.create(name='blah2')

def test2():
    assert len(Model1.objects.all()) == 0
    assert len(Model2.objects.all()) == 0

