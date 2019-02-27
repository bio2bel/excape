# -*- coding: utf-8 -*-

"""Manager for Bio2BEL ExCAPE-DB."""

from typing import Mapping, Optional

from bio2bel import AbstractManager
from bio2bel.manager.flask_manager import FlaskMixin
from tqdm import tqdm

from .constants import MODULE
from .models import Base, Chemical, Interaction, Target
from .parser import get_chunks


class Manager(AbstractManager, FlaskMixin):
    """Manager for Bio2BEL ExCAPE-DB."""

    module_name = MODULE
    _base = Base
    flask_admin_models = [Chemical, Target, Interaction]

    def count_chemicals(self) -> int:
        """Count the chemicals in the database."""
        return self._count_model(Chemical)

    def is_populated(self) -> bool:
        """Check if the database is populated."""
        return 0 < self.count_chemicals()

    def populate(self, url: Optional[str] = None, compression='xz') -> None:
        """Populate the database."""
        chunksize = 100_000
        chunks = get_chunks(url=url, compression=compression, chunksize=chunksize)

        inchi_to_chemical = {}
        entrez_gene_id_to_target = {}

        for df in tqdm(chunks):
            for i, row in tqdm(df.iterrows(), leave=False, total=chunksize):
                chemical = inchi_to_chemical.get(row.InChI)
                if chemical is None:
                    inchi_to_chemical[row.InChI] = chemical = Chemical(
                        inchikey=row.Ambit_InchiKey,
                        entry_id=row.Original_Entry_ID,
                        db=row.DB,
                        inchi=row.InChI,
                        smiles=row.SMILES,
                    )
                    self.session.add(chemical)

                target = entrez_gene_id_to_target.get(row.Entrez_ID)
                if target is None:
                    entrez_gene_id_to_target[row.Entrez_ID] = target = Target(
                        entrez_id=row.Entrez_ID,
                        tax_id=row.Tax_ID,
                        gene_symbol=row.Gene_Symbol,
                        ortholog_group=row.Ortholog_Group,
                    )
                    self.session.add(target)

                interaction = Interaction(
                    activity_flag=row.Activity_Flag,
                    assay_id=row.Original_Assay_ID,
                    db=row.DB,
                    pxc50=row.pXC50,
                    chemical=chemical,
                    target=target,
                )
                self.session.add(interaction)
            self.session.commit()

    def count_targets(self) -> int:
        """Count the proteins in the database."""
        return self._count_model(Target)

    def summarize(self) -> Mapping[str, int]:
        """Summarize the database."""
        return dict(
            chemicals=self.count_chemicals(),
            interaction=self.count_interactions(),
            proteins=self.count_targets(),
        )

    def get_chemical_by_inchi_key(self, inchi_key: str) -> Optional[Chemical]:
        """Get a chemical by its InChI key, if it exists."""
        chemical: Chemical = self.session.query(Chemical).filter_by(inchikey=inchi_key).first()
        return chemical

    def get_protein_by_entrez_id(self, entrez_id: str) -> Optional[Target]:
        """Get a protein by its Entrez identifier, if it exists."""
        target: Target = self.session.query(Target).filter_by(entrez_id=entrez_id).first()
        return target

    def count_interactions(self) -> int:
        """Count the interactions in the database."""
        return self._count_model(Interaction)
