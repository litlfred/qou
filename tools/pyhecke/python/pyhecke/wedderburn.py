"""Wedderburn-Artin weights, q-dimensions, partition utilities.

Re-exports from hecke_core. See `partition.py` for Young-tableau specific
helpers.
"""

from __future__ import annotations

from . import _legacy  # noqa: F401

from hecke_core import (  # type: ignore[import-not-found]
    partitions_of,
    partition_dimension,
    partition_conjugate,
    partition_is_self_conjugate,
    partition_jet_depth,
    q_dimension,
    wedderburn_weight,
    q_factorial,
    q_hook_product,
)

__all__ = [
    "partitions_of",
    "partition_dimension",
    "partition_conjugate",
    "partition_is_self_conjugate",
    "partition_jet_depth",
    "q_dimension",
    "wedderburn_weight",
    "q_factorial",
    "q_hook_product",
]
