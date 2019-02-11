# -*- coding: utf-8 -*-

"""Downloaders and parsers for Bio2BEL ExCAPE-DB."""

from typing import Optional

import pandas as pd

from bio2bel.downloading import make_downloader
from .constants import PATH, URL

#: Downloads the ExCAPE-DB data from Zenodo
downloader = make_downloader(URL, PATH)


def get_chunks(url: Optional[str] = None,
               cache: bool = True,
               force_download: bool = False,
               chunksize=100_000,
               compression: str = 'xz'):
    """Get the data from Zenodo as a data frame."""
    if url is None and cache:
        url = downloader(force_download=force_download)

    return pd.read_csv(
        url or URL,
        sep='\t',
        chunksize=chunksize,
        compression=compression,
    )
