# -*- coding: utf-8 -*-

"""Tests for population of the database."""
from pybel import BELGraph
from pybel.constants import PROTEIN, FUNCTION, NAMESPACE, NAME
from pybel.dsl import Protein, Abundance

from bio2bel_excape import Manager
from tests.cases import TemporaryCacheClassMixin


graph: BELGraph = BELGraph()
test_chem: Abundance = Abundance('INCHIKEY', 'AAAAZQPHATYWOK-YRBRRWAQNA-N')
test_chem2: Abundance = Abundance('INCHIKEY', 'AAABHMIRDIOYOK-NPVYFSBINA-N')
graph.add_node_from_data(test_chem)
graph.add_node_from_data(test_chem2)
test_target: Protein = Protein('EGID', '2740')
test_target2: Protein = Protein('EGID', '2778')
graph.add_node_from_data(test_target)
graph.add_node_from_data(test_target2)

class TestEnrich(TemporaryCacheClassMixin):
    """Test population of the database."""

    manager: Manager

    def test_enrich_chemicals(self):
        """Test enriching a BEL graph with additional info from the database"""
        num_edges: int = graph.number_of_edges()
        enriched_graph = self.manager.enrich_chemicals(graph)
        print(f"Num nodes: {enriched_graph.number_of_nodes()}, Num edges: {enriched_graph.number_of_edges()}")
        self.assertGreater(enriched_graph.number_of_edges(), num_edges)

    def test_enrich_targets(self):
        num_edges: int = graph.number_of_edges()
        enriched_graph = self.manager.enrich_targets(graph)
        print(f"Num nodes: {enriched_graph.number_of_nodes()}, Num edges: {enriched_graph.number_of_edges()}")
        self.assertGreater(enriched_graph.number_of_edges(), num_edges)