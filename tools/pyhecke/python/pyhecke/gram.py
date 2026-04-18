"""Gram matrix G on the H_3(q) NF basis, NF multiplication, and exact
(Fraction) variants.

M1: re-exports from folio-assistant/computations/hecke_core.py. M2 will
extract the definitions outright (lines 797-965 of that file).
"""

from __future__ import annotations

from . import _legacy  # noqa: F401  — adjusts sys.path

from hecke_core import (  # type: ignore[import-not-found]
    NF_BASIS,
    NF_NAMES,
    TR_M,
    G,
    G_INV,
    hm,
    hm_exact,
    nf_tr,
    nf_net,
    z,
)

# q-parameter constants that callers routinely also need
from hecke_core import (  # type: ignore[import-not-found]
    W_SYM,
    W_STD,
    W_ALT,
    alpha_em,
)

__all__ = [
    "NF_BASIS", "NF_NAMES", "TR_M", "G", "G_INV",
    "hm", "hm_exact", "nf_tr", "nf_net", "z",
    "W_SYM", "W_STD", "W_ALT", "alpha_em",
]


def gram_matrix():
    """Return the 6x6 Gram matrix on the NF basis of H_3(q) at q_0.

    Equivalent to the module-level `G`; provided as a function for
    call-site clarity and forward-compatibility with M3 Rust routing.
    """
    return G


def gram_inverse():
    """Return G^{-1}."""
    return G_INV
