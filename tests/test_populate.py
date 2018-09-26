# -*- coding: utf-8 -*-

"""Tests for population of the database."""

from tests.cases import TemporaryCacheClassMixin


class TestPopulate(TemporaryCacheClassMixin):
    """Test population of the database."""

    def test_count(self):
        """Test counting the contents of the database."""
        self.assertEqual(2, self.manager.count_chemicals())
