# -*- coding: utf-8 -*-

"""Constants for Bio2BEL ExCAPE-DB."""

import os

from bio2bel import get_data_dir

MODULE = 'excape'
DATA_DIR = get_data_dir(MODULE)

URL = 'https://zenodo.org/record/173258/files/pubchem.chembl.dataset4publication_inchi_smiles.tsv.xz?download=1'
PATH = os.path.join(DATA_DIR, 'pubchem.chembl.dataset4publication_inchi_smiles.tsv.xz')
HEADER = [
    'Ambit_InchiKey',
    'Original_Entry_ID',
    'Entrez_ID',
    'Activity_Flag',
    'pXC50',
    'DB	Original_Assay_ID',
    'Tax_ID',
    'Gene_Symbol',
    'Ortholog_Group',
    'InChI',
    'SMILES',
]
