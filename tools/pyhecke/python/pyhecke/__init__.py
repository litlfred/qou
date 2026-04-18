"""pyhecke — Hecke algebra + Gram matrix + tower binding infrastructure.

M1 carve-out of folio-assistant/computations/hecke_core.py. This module
exposes a stable import surface while delegating the heavy lifting to
the legacy file so downstream scripts continue to work unchanged.

Stable re-exports (stability contract for M1):
  Constants:  G, G_INV, Q, Q_INV, HA, TR_M, NF_BASIS, NF_NAMES, z,
              alpha_em, W_SYM, W_STD, W_ALT
  Functions:  hm, hm_exact, nf_tr, nf_net, check_frobenius,
              build_atom_nf, build_atom_nf_exact, knot_factor,
              partitions_of, partition_dimension, partition_conjugate,
              partition_is_self_conjugate, q_dimension, wedderburn_weight,
              q_factorial, q_hook_product

Submodules are the canonical import path for M2+:
  pyhecke.gram, pyhecke.wedderburn, pyhecke.partition, pyhecke.trace,
  pyhecke.tower, pyhecke.certificate, pyhecke.bridge, pyhecke.schema,
  pyhecke.crt
"""

from __future__ import annotations

__version__ = "0.1.0"

# Submodules are always importable; top-level symbol re-exports are
# best-effort (they require the legacy hecke_core path to be on sys.path).

from . import schema  # always importable — pure stdlib + jsonschema
from . import certificate  # uses schema
from . import bridge  # uses subprocess only
from . import crt  # pure numpy + mpmath
from . import undo  # Track B shortcut undo dispatcher

try:
    from . import gram  # re-exports from hecke_core
    from . import wedderburn
    from . import partition
    from . import trace
    from . import tower
    _legacy_available = True
except Exception:  # hecke_core imports fail (q_parameter etc. not on path)
    _legacy_available = False

__all__ = [
    "__version__",
    "schema",
    "certificate",
    "bridge",
    "crt",
    "undo",
]

if _legacy_available:
    __all__ += ["gram", "wedderburn", "partition", "trace", "tower"]

    # Flatten the most common symbols to package level for legacy callers.
    from .gram import (  # noqa: E402,F401
        G, G_INV, TR_M, NF_BASIS, NF_NAMES, hm, hm_exact, nf_tr, nf_net,
    )
    from .wedderburn import (  # noqa: E402,F401
        partitions_of, partition_dimension, partition_conjugate,
        partition_is_self_conjugate, q_dimension, wedderburn_weight,
    )
    __all__ += [
        "G", "G_INV", "TR_M", "NF_BASIS", "NF_NAMES",
        "hm", "hm_exact", "nf_tr", "nf_net",
        "partitions_of", "partition_dimension", "partition_conjugate",
        "partition_is_self_conjugate", "q_dimension", "wedderburn_weight",
    ]
