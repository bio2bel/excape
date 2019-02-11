# -*- coding: utf-8 -*-

"""Constants for Bio2BEL ExCAPE-DB."""

import os

from bio2bel import get_data_dir

MODULE = 'excape'
DATA_DIR = get_data_dir(MODULE)

URL = 'https://zenodo.org/record/173258/files/pubchem.chembl.dataset4publication_inchi_smiles.tsv.xz?download=1'
PATH = os.path.join(DATA_DIR, 'pubchem.chembl.dataset4publication_inchi_smiles.tsv.xz')
HEADER = [
    'Ambit_InchiKey',               #hashkey
    'Original_Entry_ID',            #source database id
    'pXC50',                        #measurement value (float)
    'DB',                           #source database + version
    'InChI',                        #Structual information
    'SMILES',                       #Same thing
    'Entrez_ID',                    #Identifer from the entrez database for the target
    'Tax_ID',                       #Species
    'Gene_Symbol',                  #pretty name for gene
    'Ortholog_Group',               #Gene group classifier
    'Activity_Flag',                #active / not active
    'Original_Assay_ID'             #Identifier of original assay
]
