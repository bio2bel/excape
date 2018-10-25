# -*- coding: utf-8 -*-

"""SQLAlchemy models for Bio2BEL ExCAPE-DB."""

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import pybel.dsl
from pybel import BELGraph
from .constants import MODULE

__all__ = [
    'Base',
    'Chemical',
    'Protein',
    'Interaction',
]

CHEMICAL_TABLE_NAME = f'{MODULE}_chemical'
PROTEIN_TABLE_NAME = f'{MODULE}_protein'
INTERACTION_TABLE_NAME = f'{MODULE}_interaction'

Base = declarative_base()

class Chemical(Base):
    """Represents a chemical."""

    __tablename__ = CHEMICAL_TABLE_NAME
    id = Column(Integer, primary_key=True)

    ambit_inchikey = Column(String, nullable=False, doc="")
    original_entry_id = Column(String(255), nullable=False, doc="Name of the chemical on the original datbase")
    db = Column(String(255), nullable=False, doc="Name of the database from which the chemical was obtained")
    pxc50 = Column(Float, nullable=False, doc="pXC50/potency of the chemical")
    inchi = Column(String(255), nullable=False, doc="inchi key for the chemical")
    smiles = Column(String(255), nullable=False, doc="canonical smile for the chemical")

    def as_pybel(self) -> pybel.dsl.Abundance:
        """Serialize as a PyBEL abundance."""
        raise NotImplementedError


class Protein(Base):
    """Represents a protein."""

    __tablename__ = PROTEIN_TABLE_NAME
    id = Column(Integer, primary_key=True)

    entrez_id = Column(String(255), nullable=False, doc="entrez id for the target/protein")
    tax_id = Column(Integer, nullable=False, doc="tax id / specie of the protein")
    gene_symbol = Column(String(255), nullable=False, doc="name of the gene encoding such protein")
    ortholog_group = Column(String(255), nullable=False, doc="orthogonal group of the protein")


    def as_pybel(self) -> pybel.dsl.Protein:
        """Serialize as a PyBEL protein."""
        raise NotImplementedError


class Interaction(Base):
    """Represents an interaction between a chemical and protein."""

    __tablename__ = INTERACTION_TABLE_NAME
    id = Column(Integer, primary_key=True)

    chemical_id = Column(Integer, ForeignKey(f'{Chemical.__tablename__}.id'), nullable=False)
    chemical = relationship(Chemical)

    protein_id = Column(Integer, ForeignKey(f'{Protein.__tablename__}.id'), nullable=False)
    protein = relationship(Protein)

    activity_flag = Column(String(255), nullable=False)
    original_assay_id = Column(Integer, nullable=False)

    def add_to_bel_graph(self, graph: BELGraph) -> str:
        """Add this interaction to a BEL graph."""
        raise NotImplementedError
