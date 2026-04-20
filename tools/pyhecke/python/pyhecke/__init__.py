"""pyhecke — Hecke algebra + Gram matrix + tower binding infrastructure.

M1 carve-out of folio-assistant/computations/hecke_core.py. This module
exposes a stable import surface while delegating the heavy lifting to
the legacy file so downstream scripts continue to work unchanged.

Stable re-exports:
  Constants:  G, G_INV, TR_M, NF_BASIS, NF_NAMES, z,
              W_SYM, W_STD, W_ALT, alpha_em
  Functions:  hm, hm_exact, nf_tr, nf_net,
              partitions_of, partition_dimension, partition_conjugate,
              partition_is_self_conjugate, q_dimension, wedderburn_weight,
              q_factorial, q_hook_product

Submodules (lazy-loaded via PEP-562 __getattr__):
  pyhecke.gram, pyhecke.wedderburn, pyhecke.partition, pyhecke.trace,
  pyhecke.tower, pyhecke.certificate, pyhecke.bridge, pyhecke.schema,
  pyhecke.crt, pyhecke.undo, pyhecke.sdp

Import `pyhecke.<submodule>` to pay only the cost of that submodule
plus its own deps. `import pyhecke` on its own loads none of them.
"""

from __future__ import annotations

import importlib as _importlib
from typing import Any

__version__ = "0.1.0"

_SUBMODULES = (
    # Stdlib-only or pure-numpy — cheap
    "schema", "certificate", "bridge", "crt", "undo", "sdp",
    # Depend on hecke_core and its siblings — expensive (42s today)
    "gram", "wedderburn", "partition", "trace", "tower",
)

# Flattened symbols exported at package level. The first time any of
# these is accessed, we load the owning submodule and cache the bind.
_FLATTENED = {
    # from pyhecke.gram
    "G": "gram", "G_INV": "gram", "TR_M": "gram",
    "NF_BASIS": "gram", "NF_NAMES": "gram",
    "hm": "gram", "hm_exact": "gram", "nf_tr": "gram", "nf_net": "gram",
    "z": "gram", "W_SYM": "gram", "W_STD": "gram", "W_ALT": "gram",
    "alpha_em": "gram",
    # from pyhecke.wedderburn
    "partitions_of": "wedderburn",
    "partition_dimension": "wedderburn",
    "partition_conjugate": "wedderburn",
    "partition_is_self_conjugate": "wedderburn",
    "q_dimension": "wedderburn",
    "wedderburn_weight": "wedderburn",
    "q_factorial": "wedderburn",
    "q_hook_product": "wedderburn",
}

__all__ = ["__version__", *sorted(_SUBMODULES), *sorted(_FLATTENED)]


def __getattr__(name: str) -> Any:
    """PEP-562 lazy loader.

    Two paths:
      1. `name` is a submodule (e.g. "gram", "schema"): import it, bind
         it on this package, return.
      2. `name` is a flattened symbol (e.g. "G", "hm"): import its
         owning submodule, pull the attribute, bind on this package.
    """
    if name in _SUBMODULES:
        module = _importlib.import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    if name in _FLATTENED:
        owner = _importlib.import_module(f"{__name__}.{_FLATTENED[name]}")
        try:
            value = getattr(owner, name)
        except AttributeError as e:
            raise AttributeError(
                f"pyhecke: submodule {_FLATTENED[name]!r} does not expose {name!r}. "
                f"This usually means hecke_core is not importable in this env."
            ) from e
        globals()[name] = value
        return value
    raise AttributeError(f"module 'pyhecke' has no attribute {name!r}")


def __dir__() -> list[str]:
    return list(__all__)
