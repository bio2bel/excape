# -*- coding: utf-8 -*-

"""Tests for population of the database."""

from bio2bel_excape import Manager
from tests.cases import TemporaryCacheClassMixin


class TestPopulate(TemporaryCacheClassMixin):
    """Test population of the database."""

    manager: Manager

    def test_count_chemicals(self):
        """Test counting the chemicals in the database."""
        self.assertEqual(2, self.manager.count_chemicals())

    def test_count_proteins(self):
        """Test counting the proteins in the database."""
        self.assertEqual(9, self.manager.count_proteins())

    def test_get_missing_chemical_by_inchi_key(self):
        """Test getting a chemical by InChI key that does not exist."""
        missing_chemical = self.manager.get_chemical_by_inchi_key('aslagljkadgljsadgl')
        self.assertIsNone(missing_chemical)

    def test_get_chemical_by_inchi_key(self):
        """Test getting a chemical by InChI key."""
        chemical = self.manager.get_chemical_by_inchi_key('AAABHMIRDIOYOK-NPVYFSBINA-N')
        self.assertIsNotNone(chemical)
        self.assertEqual('AAABHMIRDIOYOK-NPVYFSBINA-N', chemical.inchi_key)
        self.assertEqual(
            'InChI=1/C18H14N6O3/c1-23-10-15(24(26)27)16(22-23)18(25)19-12-7-8-13-14(9-12)21-17(20-13)11-5-3-2-4-6-11/'
            'h2-10H,1H3,(H,19,25)(H,20,21)/f/h19-20H',
            chemical.inchi
        )
        self.assertEqual('O=C(NC=1C=C2N=C(NC2=CC1)C=3C=CC=CC3)C4=NN(C=C4N(=O)=O)C', chemical.smiles)

    def test_get_missing_protein_by_entrez_id(self):
        """Test getting a protein by Entrez identifier that does not exist."""
        missing_protein = self.manager.get_protein_by_entrez_id('sakgjladlkjghalk')
        self.assertIsNone(missing_protein)

    def test_get_protein_by_entrez_id(self):
        """Test getting a protein by Entrez identifier that exists."""
        protein = self.manager.get_protein_by_entrez_id("19885")
        self.assertIsNotNone(protein)
        self.assertEqual("19885", protein.entrez_id)
        self.assertEqual("10090", protein.tax_id)
        self.assertEqual("RORC", protein.gene_symbol)
        self.assertEqual("3770", protein.ortholog_group)


    # TODO @miguel add a test for getting a protein. Needs to have fields for species, gene symbol, ortholog group, etc
