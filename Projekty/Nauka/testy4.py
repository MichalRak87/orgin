import pytest


def sort_by(names,first_letter=False,last_letter=False,length=False):
    if first_letter:
        names.sort()
    elif last_letter:
        names.sort(key=lambda name: name[::-1])
    elif length:
        names.sort(key=len,reverse=False)
    return names


class TestSort:
    @pytest.fixture
    def names(self):
        return ['Alina','Ewa','Paulina','Maciej']

    def test_sort(self,names):
        # when
        sorted_names = sort_by(names, first_letter=True)

        # then

        assert sorted_names == ['Alina','Ewa','Maciej','Paulina']

    def test_reverse_sort(self,names):
        sorted_names = sort_by(names, last_letter=True)
        assert sorted_names == ['Alina','Paulina','Ewa','Maciej']

    def test_sort_by_length(self,names):
        sorted_names = sort_by(names,length=True)
        assert sorted_names == ['Ewa','Alina','Maciej','Paulina']