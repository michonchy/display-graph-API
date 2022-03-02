import json

import pytest

from display_graph import app


def test_number_display_graph():
    assert app.number_display_graph([5,6]) == ["5  :*****","6  :***** *"]


    