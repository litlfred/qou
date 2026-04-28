"""Young partitions and partition-valued functionals.

Re-exports the partition-specific functionals from hecke_core: spectral
rates, LP shadow prices, Laplacian eigenvalues, resolvent weights.
"""

from __future__ import annotations

from . import _legacy  # noqa: F401

from hecke_core import (  # type: ignore[import-not-found]
    lp_shadow_price,
    q_laplacian_eigenvalue,
    q_resolvent_weight,
    partition_character_sigma1,
    partition_spectral_log_rate,
)

__all__ = [
    "lp_shadow_price",
    "q_laplacian_eigenvalue",
    "q_resolvent_weight",
    "partition_character_sigma1",
    "partition_spectral_log_rate",
]
