# -*- coding: utf-8 -*-

"""Manager for Bio2BEL ExCAPE-DB."""

from typing import Mapping, Optional

from tqdm import tqdm

from bio2bel import AbstractManager
from bio2bel.manager.flask_manager import FlaskMixin
from .constants import MODULE
from .models import Base, Chemical, Interaction, Protein
from .parser import get_chunks


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
        chunks = get_chunks(url=url)

        for chunk in tqdm(chunks):
            for row in tqdm(chunk.iterrows(), leave=False):
                raise NotImplementedError

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

    def get_chemical_by_inchi_key(self, inchi_key: str) -> Optional[Chemical]:
        """Get a chemical by its InChI key, if it exists."""
        # TODO consider validating against regex ^[A-Z]{14}\-[A-Z]{10}(\-[A-Z])?
        raise NotImplementedError

    def get_protein_by_entrez_id(self, entrez_id: str) -> Optional[Protein]:
        """Get a protein by its Entrez identifier, if it exists."""
        raise NotImplementedError
