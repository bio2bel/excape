# -*- coding: utf-8 -*-

"""Test cases for Bio2BEL ExCAPE."""

import os

from bio2bel.testing import AbstractTemporaryCacheClassMixin
from bio2bel_excape import Manager

HERE = os.path.dirname(os.path.realpath(__file__))
TEST_PATH = os.path.join(HERE, 'data.tsv')


class TemporaryCacheClassMixin(AbstractTemporaryCacheClassMixin):
    """A test case that has a populated database."""

    Manager = Manager
    manager: Manager

    @classmethod
    def populate(cls):
        """Populate the database with test data."""
        cls.manager.populate(url=TEST_PATH, compression=None)
