# -*- coding: utf-8 -*-

"""Manager for Bio2BEL ExCAPE-DB."""

from typing import Mapping, Optional

from bio2bel import AbstractManager
from .models import Base


class Manager(AbstractManager):
    """Manager for Bio2BEL ExCAPE-DB."""

    module_name = 'excape'
    _base = Base

    def is_populated(self) -> bool:
        """Check if the database is populated"""
        raise NotImplementedError

    def populate(self, url: Optional[str] = None) -> None:
        """Populate the database."""
        raise NotImplementedError

    def summarize(self) -> Mapping[str, int]:
        """Summarize the database"""
        raise NotImplementedError
