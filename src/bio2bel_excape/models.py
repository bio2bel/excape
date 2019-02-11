# -*- coding: utf-8 -*-

"""SQLAlchemy models for Bio2BEL ExCAPE-DB."""

from sqlalchemy import Column, Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

import pybel.dsl
from pybel import BELGraph
from .constants import MODULE

__all__ = [
    'Base',
    'Chemical',
    'Target',
    'Interaction',
]

CHEMICAL_TABLE_NAME = f'{MODULE}_chemical'
TARGET_TABLE_NAME = f'{MODULE}_target'
INTERACTION_TABLE_NAME = f'{MODULE}_interaction'

Base = declarative_base()


class Chemical(Base):
    """Represents a chemical."""

    __tablename__ = CHEMICAL_TABLE_NAME
    id = Column(Integer, primary_key=True)

    inchi = Column(String(4098), nullable=False, unique=True, doc="InChI for the chemical")
    inchikey = Column(String(27), nullable=False, doc="Hash of the InChI for the chemical")
    db = Column(String(32), nullable=False, doc="Name of the database from which the chemical was obtained")
    entry_id = Column(String(32), nullable=False, doc="Identifier of the chemical on the original database")
    smiles = Column(String(4098), nullable=False, doc="Canonical SMILES for the chemical (no stereochemistry)")

    __table_args__ = (
        UniqueConstraint(db, entry_id),
    )

    def as_pybel(self) -> pybel.dsl.Abundance:
        """Serialize as a PyBEL abundance."""
        return pybel.dsl.Abundance(namespace='inchi', identifier=self.inchi)


class Target(Base):
    """Represents a protein."""

    __tablename__ = TARGET_TABLE_NAME
    id = Column(Integer, primary_key=True)

    entrez_id = Column(String(64), nullable=False, unique=True, doc="entrez id for the target/protein")
    tax_id = Column(String(16), nullable=False, doc="tax id / specie of the protein")
    gene_symbol = Column(String(16), nullable=False, doc="name of the gene encoding such protein")
    ortholog_group = Column(String(16), nullable=False, doc="orthogonal group of the protein")

    def as_pybel(self) -> pybel.dsl.Protein:
        """Serialize as a PyBEL protein."""
        return pybel.dsl.Protein(namespace='ncbigene', identifier=self.entrez_id, name=self.gene_symbol)


class Interaction(Base):
    """Represents an interaction between a chemical and protein."""

    __tablename__ = INTERACTION_TABLE_NAME
    id = Column(Integer, primary_key=True)

    chemical_id = Column(Integer, ForeignKey(f'{Chemical.__tablename__}.id'), nullable=False)
    chemical = relationship(Chemical, backref=backref('interactions'))

    target_id = Column(Integer, ForeignKey(f'{Target.__tablename__}.id'), nullable=False)
    target = relationship(Target, backref=backref('interactions'))

    db = Column(String(32), nullable=False, doc="Name of the database from which the chemical was obtained")
    assay_id = Column(String(64), nullable=False)
    pxc50 = Column(Float, nullable=False, doc="pXC50/potency of the chemical")
    activity_flag = Column(String(255), nullable=False)

    __table_args__ = (
        UniqueConstraint(chemical_id, target_id, db, assay_id),
    )

    def add_to_bel_graph(self, graph: BELGraph) -> str:
        """Add this interaction to a BEL graph."""
        return graph.add_inhibits(
            self.chemical.as_pybel(),
            self.target.as_pybel(),
            citation='28316655',
            evidence='from ExCAPE-DB',
            annotations={
                'pXC50': self.pxc50,
                'activity_flag': self.activity_flag,
            }
        )

    @property
    def assay_url(self):
        if self.db == 'pubchem':
            return f"https://identifiers.org/pubchem.bioassay:{self.assay_id}"
        elif self.db == 'chembl20':
            return f"https://www.ebi.ac.uk/chembl/assay/inspect/CHEMBL{self.assay_id}"
