#!/usr/bin/env python3
# polynomial_q_not_applicable: structural braid-word API, not a q-series compute.
"""Tier 1.B — nucleon-orbit reduction API (S_Z × S_N orbit of an atomic braid).

**CORRECTED identity** (proven 2026-05-30 —
``docs/audits/2026-05-30-orbit-trace-identity-proof.md``):

    tr_M(β_{Z,N}) = tr_M(representative)        ← NO |orbit| multiplier

The optimisation roadmap
(``docs/audits/2026-05-20-compute-optimization-roadmap.md`` §1.B) drafted
``tr_M(β_{Z,N}) = |orbit| · tr_M(rep)`` with ``|orbit| = Z!·N!``. **That
formula is wrong** and this module exists partly to guard against it:
multiplying the trace by ``|orbit|`` would make ``m(⁴He)`` 4× too large,
``m(⁸Be)`` 576× too large. The correct statement has **no multiplier**,
because the canonical word ``atom_braid_word_3A(Z, N)`` is *already* the
orbit representative:

* **Lemma 1 (word invariance).** A same-species permutation
  ``σ ∈ S_Z × S_N`` fixes the ordering string ``p…pn…n`` and preserves
  every adjacency type (pp / pn / nn), so it leaves the word — hence its
  trace — unchanged. The whole orbit maps to one word.
* **Lemma 2 (Markov M1).** ``tr_M`` is conjugation-invariant; the
  cyclic-rotation test on the real ⁴He braid agrees to 3.7e-51 @50dps.

Consequently ``orbit_size = Z!·N!`` is **audit metadata** (it records the
combinatorial multiplicity of the orbit for provenance), *not* a factor
applied to any observable.

**On the "36× / 576× speedup".** The roadmap's wall-reduction table
assumed the current reduce walks ``|orbit|`` permuted words and the
orbit-quotient walks one. It does not: ``atom_braid_word_3A`` already
emits the single canonical ``p…pn…n`` word, so there is no
``|orbit|``-fold enumeration to collapse. The headline reduce-speedup is
therefore **illusory as framed**. The *real* benefit the identity
licenses is correctness + ordering choice: the canonical ``p…pn…n``
ordering is **interface-minimal** (exactly one pn crossing; every other
ordering of the same multiset has ≥ 1 and generically more), and the
identity guarantees the trace is independent of which same-species
representative you pick — so the cheapest (canonical) one is always
valid. See the audit doc for the measured wall comparison.

Public API:

* ``atom_braid_orbit_representative(Z, N, ...)`` → ``OrbitRepresentative``
* ``tr_M_via_orbit_representative(Z, N, ...)`` → the trace on the rep
  (canonical Tier-1.B entry point; **no** ``|orbit|`` factor)
* ``atom_braid_word_ordered(ordering, ...)`` → generalized word builder
  for arbitrary species orderings (used by the cross-check to exhibit
  interface-minimality; the canonical path delegates to the unchanged
  ``atom_braid_word_3A``).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


def _interface_type(a: str, b: str) -> str:
    if a == "p" and b == "p":
        return "pp"
    if a == "n" and b == "n":
        return "nn"
    return "pn"


def atom_braid_word_ordered(ordering, *, m_pp: int = 1, m_pn: int = 1,
                            m_nn: int = 1, include_inter: bool = True):
    """``atom_braid_word_3A`` generalized to an explicit species ordering.

    ``ordering`` is a sequence over ``{'p', 'n'}``. Emits, per nucleon ``k``,
    the species intra-crossings (gens ``3k``, ``3k+1``) then the
    adjacency-typed inter-crossing (gen ``3k+2``). Matches
    ``atom_braid_word_3A`` exactly on the canonical ``'p'*Z + 'n'*N``.
    """
    from hecke_core import (_PROTON_G0, _PROTON_G1, _NEUTRON_G0,
                            _NEUTRON_G1, h)
    A = len(ordering)
    h_num = float(h)
    word: list[tuple[float, float, int]] = []
    for k, nuc in enumerate(ordering):
        g0 = _PROTON_G0 if nuc == "p" else _NEUTRON_G0
        g1 = _PROTON_G1 if nuc == "p" else _NEUTRON_G1
        for c, d in g0:
            word.append((float(c), float(d), 3 * k))
        for c, d in g1:
            word.append((float(c), float(d), 3 * k + 1))
        if include_inter and k < A - 1:
            t = _interface_type(nuc, ordering[k + 1])
            if t == "pp":
                cd, m = (1.0, 0.0), m_pp
            elif t == "nn":
                cd, m = (1.0, -h_num), m_nn
            else:
                cd, m = (1.0, -h_num / 2), m_pn
            for _ in range(m):
                word.append((cd[0], cd[1], 3 * k + 2))
    return word


def interface_multiset(ordering) -> dict[str, int]:
    """Multiset of adjacency interface types for a species ordering."""
    return dict(Counter(_interface_type(a, b)
                        for a, b in zip(ordering, ordering[1:])))


@dataclass(frozen=True)
class OrbitRepresentative:
    """Canonical S_Z × S_N orbit representative of an atomic braid.

    ``orbit_size`` is **audit metadata** (``Z!·N!``), NOT a trace
    multiplier — ``tr_M(β) = tr_M(rep)`` exactly (see module docstring).
    """
    Z: int
    N: int
    ordering: str
    word: list = field(repr=False)
    orbit_size: int
    interfaces: dict

    @property
    def n_pn(self) -> int:
        return self.interfaces.get("pn", 0)


def atom_braid_orbit_representative(Z: int, N: int, *, m_pp: int = 1,
                                    m_pn: int = 1, m_nn: int = 1,
                                    include_inter: bool = True
                                    ) -> OrbitRepresentative:
    """Canonical ``p…pn…n`` orbit representative of ``β_{Z,N}``.

    Delegates the word to the unchanged production ``atom_braid_word_3A``
    so the canonical compute path is byte-identical to today's. Returns
    the word plus orbit metadata (``orbit_size = Z!·N!`` — *metadata*).
    """
    from mass_at_3A_proper import atom_braid_word_3A
    ordering = "p" * Z + "n" * N
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                              include_inter=include_inter)
    return OrbitRepresentative(
        Z=Z, N=N, ordering=ordering, word=word,
        orbit_size=math.factorial(Z) * math.factorial(N),
        interfaces=interface_multiset(ordering),
    )


def tr_M_via_orbit_representative(Z: int, N: int, *, include_inter: bool = True,
                                  max_iterations: int = 10000):
    """``tr_M(β_{Z,N})`` via the orbit representative — **no |orbit| factor**.

    Canonical Tier-1.B entry point. Equal to ``tr_M_atomic_fast(Z, N)``
    (same canonical word); the orbit framing adds the metadata + the
    guarantee that the trace is representative-independent, NOT a speedup
    or a multiplier. The ``orbit_size`` is deliberately *not* used in the
    return value.
    """
    rep = atom_braid_orbit_representative(Z, N, include_inter=include_inter)
    from hecke_laurent_fast import incremental_reduced_element_fast
    from hecke_symbolic import SymbolicHeckeElement
    from markov_trace_canonical import tr_M_element
    fe = incremental_reduced_element_fast(
        rep.word, max_iterations_per_step=max_iterations)
    se = SymbolicHeckeElement(fe.to_sympy_element())
    return tr_M_element(se, 3 * (Z + N), simplify=False)
