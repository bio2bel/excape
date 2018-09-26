# -*- coding: utf-8 -*-

"""Manager for Bio2BEL ExCAPE-DB."""

from typing import Mapping, Optional

from tqdm import tqdm

from bio2bel import AbstractManager
from bio2bel.manager.flask_manager import FlaskMixin
from .constants import MODULE
from .models import Base, Chemical, Interaction, Protein
from .parser import get_df


class Manager(AbstractManager, FlaskMixin):
    """Manager for Bio2BEL ExCAPE-DB."""

    module_name = MODULE
    _base = Base
    flask_admin_models = [Chemical, Protein, Interaction]

    def is_populated(self) -> bool:
        """Check if the database is populated."""
        return 0 < self.count_chemicals()

    def populate(self, url: Optional[str] = None) -> None:
        """Populate the database."""
        df = get_df(url=url)

        for row in tqdm(df.iterrows()):
            pass

    def count_chemicals(self) -> int:
        """Count the chemicals in the database."""
        return self._count_model(Chemical)

    def count_proteins(self) -> int:
        """Count the proteins in the database."""
        return self._count_model(Protein)

    def summarize(self) -> Mapping[str, int]:
        """Summarize the database."""
        return dict(
            chemicals=self.count_chemicals(),
            proteins=self.count_proteins(),
        )
