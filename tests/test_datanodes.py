"""
DataNodes creation tests.

"""
from smart_choice.decisiontree import DecisionTree
from smart_choice.examples import (
    stguide,
    stguide_dependent_outcomes,
    stguide_dependent_probabilities,
)

from tests.capsys import check_capsys


def test_stguide_fig_5_4a(capsys):
    """Table of variables"""

    nodes = stguide()
    print(nodes)
    check_capsys("./tests/files/stguide_fig_5_4a.txt", capsys)


def test_stguide_fig_7_3a(capsys):
    """Change probabilities"""

    nodes = stguide_dependent_probabilities()
    print(nodes)
    check_capsys("./tests/files/stguide_fig_7_3a.txt", capsys)
