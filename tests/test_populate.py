# -*- coding: utf-8 -*-

"""Tests for population of the database."""

import os

from bio2bel.testing import AbstractTemporaryCacheClassMixin
from bio2bel_excape import Manager

HERE = os.path.dirname(os.path.realpath(__file__))
TEST_PATH = os.path.join(HERE, 'data.tsv')


class TemporaryCacheClassMixin(AbstractTemporaryCacheClassMixin):
    """A test case that has a populated database."""
    Manager = Manager

    @classmethod
    def populate(cls):
        """Populate the database with test data."""
        cls.manager.populate(url=TEST_PATH)


class TestPopulate(TemporaryCacheClassMixin):
    """Test population of the database"""

    def test_count(self):
        """Test counting the contents of the database."""
        self.fail()
