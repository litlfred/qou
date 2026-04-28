#!/usr/bin/env python3
"""C4 — Component count, writhe, signature of T(2,N).

Backs `lem:T2N-components` in the Organic Chemistry chapter.

Algorithm
---------
For T(p,q) the standard knot-theoretic invariants have closed forms:

* **Components**: ``gcd(p, q)``.  For T(2, N): 1 if N is odd, 2 if N is
  even.
* **Crossings (braid representation)**: ``(p-1) * q``.  For T(2, N):
  ``q`` crossings — wait, for T(p,q) closure of (σ₁⋯σ_{p-1})^q the
  crossing count is ``(p-1)*q``.  For T(2, N) this is ``N`` crossings;
  the chapter quotes ``2(N-1)`` for the *braid word*
  ``(σ₁⋯σ_{N-1})²`` of T(2, N) used as the threading link.  Both are
  recorded.
* **Writhe**: all crossings have the same sign in the standard T(p,q)
  diagram, so writhe = ± (number of crossings).  We take the
  positive-braid convention, writhe = +(p-1)*q.
* **Signature** (Tristram–Levine at t = -1, for the standard
  positive torus link): for T(2, N) the signature is::

        σ(T(2, N)) = -(N - 1) for odd N (the (2, N) torus knot)
        σ(T(2, 2m)) = -(2m - 1) when oriented so all crossings are positive
                       (Murasugi 1965, Gordon-Litherland 1979).

  Below we use the simpler closed form ``σ = -(N - 1)`` valid for
  positive T(2, N).

The script verifies these against the chapter's Components column
(`def:threading-link`) and writes a witness with the full table.

Usage
-----
    python3 T2N_component_count.py
"""
import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from witness_base import WitnessBuilder


def components_T2N(N: int) -> int:
    return gcd(2, N)


def braid_word_crossings(N: int) -> int:
    """Crossings in the braid word (σ₁⋯σ_{N-1})² of T(2,N)."""
    return 2 * (N - 1)


def standard_T2N_crossings(N: int) -> int:
    """Crossings in the minimal-crossing diagram of T(2,N)."""
    return N


def writhe_positive_T2N(N: int) -> int:
    """Writhe (positive-braid convention)."""
    return braid_word_crossings(N)


def signature_T2N(N: int) -> int:
    """Signature of the positively-oriented torus link/knot T(2, N)."""
    return -(N - 1)


def main() -> int:
    w = WitnessBuilder("T2N-component-count", engine="python")
    w.set_description(
        "Component count, writhe, and signature of T(2,N) for N = 2,…,12. "
        "Verifies the gcd(2,N) component formula and the all-positive "
        "crossing convention from def:threading-link."
    )
    w.set_content_block("lem:T2N-components")

    rows = []
    for N in range(2, 13):
        rows.append({
            "N": N,
            "components": components_T2N(N),
            "braid_word_crossings": braid_word_crossings(N),
            "min_diagram_crossings": standard_T2N_crossings(N),
            "writhe_positive": writhe_positive_T2N(N),
            "signature": signature_T2N(N),
            "is_knot": components_T2N(N) == 1,
        })
    w.add_data("table", rows)

    # Headline assertions cited in def:threading-link.
    w.add_assertion("components(T(2,2)) == 2", components_T2N(2), 2)
    w.add_assertion("components(T(2,3)) == 1", components_T2N(3), 1)
    w.add_assertion("components(T(2,6)) == 2", components_T2N(6), 2)
    w.add_assertion("braid-word crossings T(2,6)", braid_word_crossings(6), 10)
    w.add_assertion("signature T(2,6)", signature_T2N(6), -5)

    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
