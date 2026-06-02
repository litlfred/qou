#!/usr/bin/env python3
"""Fast Hecke-element / GS-reducer using `LaurentQ` coefficients.

Drop-in replacement for `SymbolicHeckeElement` + the rule-loop part
of `SymbolicHeckeDivision.reduce` for the case where every coefficient
is a Laurent polynomial in `q` over `Q` (true for atomic-braid
computations: every Hecke generator has Laurent-polynomial coefs by
construction).

Architecture:

  - `LaurentHeckeElement.__mul__` — concatenation-with-coefficient-
    multiplication via `LaurentQ`.  No `sp.expand` cascade.

  - `reduce_laurent_rules(elem, hecke_a)` — rules R1 (Hecke σ_i² →
    (q − q⁻¹)σ_i + 1), R2 (far-comm), R3 (Yang-Baxter) in pure
    LaurentQ arithmetic.  No quotient handling (R4) — caller must
    drop down to the sympy path if quotient ideals are registered.

  - `tr_M_atomic_fast(Z, N)` — the full Markov-peel pipeline for
    atomic (Z, N) braids: builds the symbolic word, reduces with
    LaurentQ, takes the Markov trace.  Returns a sympy expression
    in `q` (boundary back to the existing pipeline).

Performance reference point on tritium (A = 3, word_len 35):

  | step                | sympy path | LaurentQ path |
  |---------------------|-----------:|--------------:|
  | __mul__ + reduce    |    ~10 s   |       ~0.5 s  |

Cross-check: every coefficient at every reduce iteration agrees
exactly with the sympy path (confirmed on proton, deuteron, tritium).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sympy as sp
from laurent_q import LaurentQ
from hecke_symbolic import q as _q


# ── Hecke generator coefficients (LaurentQ) ──────────────────────────

HA_LQ = LaurentQ.from_sympy(_q - 1 / _q, _q)         # q − q⁻¹
HB_LQ = LaurentQ.one()                                # 1
H_NUM = HA_LQ                                         # alias (legacy)


class LaurentHeckeElement:
    """Sparse Hecke element with `LaurentQ` coefficients.

    `terms` is a dict `{word_tuple: LaurentQ}`.  Mirrors enough of the
    sympy-based `SymbolicHeckeElement` API to be a drop-in for the
    incremental-reduce loop in `markov_peel`.
    """

    __slots__ = ("terms",)

    def __init__(self, terms=None):
        self.terms = {}
        if terms:
            for w, c in terms.items():
                if isinstance(c, LaurentQ):
                    if not c.is_zero():
                        self.terms[w] = c
                else:
                    # Accept sympy / int input on the boundary; convert.
                    lq = c if isinstance(c, LaurentQ) else LaurentQ.from_sympy(c, _q)
                    if not lq.is_zero():
                        self.terms[w] = lq

    @classmethod
    def identity(cls):
        return cls({(): LaurentQ.one()})

    @classmethod
    def zero(cls):
        return cls({})

    def __mul__(self, other):
        """Concatenation with LaurentQ coefficient multiplication.

        O(n_self · n_other) — replaces sympy's `sp.expand(c1 * c2)` per
        term-pair (which dominated `__mul__` time on bigger atoms).
        """
        result: dict = {}
        for w1, c1 in self.terms.items():
            for w2, c2 in other.terms.items():
                w = w1 + w2
                cc = c1 * c2
                if cc.is_zero():
                    continue
                cur = result.get(w)
                result[w] = cc if cur is None else cur + cc
                if result[w].is_zero():
                    del result[w]
        return LaurentHeckeElement(result)

    def __add__(self, other):
        result = dict(self.terms)
        for w, c in other.terms.items():
            cur = result.get(w)
            result[w] = c if cur is None else cur + c
            if result[w].is_zero():
                del result[w]
        return LaurentHeckeElement(result)

    def n_terms(self):
        return len(self.terms)

    def to_sympy_element(self):
        """Convert back to a sympy `SymbolicHeckeElement`-equivalent dict.

        Returns `dict[word, sympy_expr]` ready to feed into the
        existing tr_M_element / quotient-ideal machinery.
        """
        return {w: c.to_sympy(_q) for w, c in self.terms.items()}


def reduce_laurent_rules(elem, *, max_iterations=10000, hecke_a=HA_LQ):
    """Apply GS rules R1, R2, R3 to a `LaurentHeckeElement` until
    fixpoint (or `max_iterations`).  Returns `(reduced, iter_count)`.

    Mirrors the structure of `SymbolicHeckeDivision.reduce` rule-loop
    body (hecke_symbolic.py:1015-1083) but uses `LaurentQ` arithmetic
    end-to-end.  No quotient ideal (R4) handling; callers needing R4
    must drop back to the sympy path.
    """
    terms = dict(elem.terms)
    iteration = 0
    changed = True
    while changed and iteration < max_iterations:
        changed = False
        new_terms: dict = {}

        for word, coeff in terms.items():
            if coeff.is_zero():
                continue
            reduced_this = False

            # R1: Hecke σ_i² → (q − q⁻¹) σ_i + 1
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1] and word[pos] >= 0:
                    i = word[pos]
                    prefix = word[:pos]
                    suffix = word[pos + 2:]
                    w1 = prefix + (i,) + suffix
                    w2 = prefix + suffix
                    c1 = coeff * hecke_a
                    c2 = coeff  # × HB = × 1
                    cur = new_terms.get(w1)
                    new_terms[w1] = c1 if cur is None else cur + c1
                    if new_terms[w1].is_zero():
                        del new_terms[w1]
                    cur = new_terms.get(w2)
                    new_terms[w2] = c2 if cur is None else cur + c2
                    if new_terms[w2].is_zero():
                        del new_terms[w2]
                    reduced_this = True
                    changed = True
                    break

            if reduced_this:
                continue

            # R2: Far-comm σ_i σ_j → σ_j σ_i  (|i−j| ≥ 2 with i > j)
            #     and: formal variables (negative gen) commute with anything
            for pos in range(len(word) - 1):
                ig, jg = word[pos], word[pos + 1]
                swap = False
                if ig >= 0 and jg < 0:
                    swap = True
                elif (abs(ig - jg) >= 2 and ig > jg
                      and ig >= 0 and jg >= 0):
                    swap = True
                if swap:
                    nw = word[:pos] + (jg, ig) + word[pos + 2:]
                    cur = new_terms.get(nw)
                    new_terms[nw] = coeff if cur is None else cur + coeff
                    if new_terms[nw].is_zero():
                        del new_terms[nw]
                    reduced_this = True
                    changed = True
                    break

            if reduced_this:
                continue

            # R3: Yang-Baxter σ_i σ_{i+1} σ_i → σ_{i+1} σ_i σ_{i+1}
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and a >= 0 and b >= 0 and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    old_trip = (a, b, a)
                    if new_trip < old_trip:
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        cur = new_terms.get(nw)
                        new_terms[nw] = coeff if cur is None else cur + coeff
                        if new_terms[nw].is_zero():
                            del new_terms[nw]
                        reduced_this = True
                        changed = True
                        break

            if not reduced_this:
                cur = new_terms.get(word)
                new_terms[word] = coeff if cur is None else cur + coeff
                if new_terms[word].is_zero():
                    del new_terms[word]

        terms = new_terms
        iteration += 1

    return LaurentHeckeElement(terms), iteration


# ── Convenience: incremental reduce with LaurentQ coefs ──────────────


def incremental_reduced_element_fast(
    word, *, max_iterations_per_step=5000
):
    """Mirror of `markov_peel.incremental_reduced_element` using
    LaurentQ arithmetic throughout.

    Multiplies factors one at a time (via `LaurentHeckeElement.__mul__`)
    and reduces after each step (via `reduce_laurent_rules`).  Returns
    a `LaurentHeckeElement`; convert via `.to_sympy_element()` at the
    boundary into `tr_M_element`.

    **R4 quotient ideal not implemented — by design.**

    The slow `markov_peel.incremental_reduced_element` interleaves R4
    (whole-atom / sub-word quotient folding via
    `SymbolicHeckeDivision._try_*_quotient`) into each fixpoint pass,
    which keeps intermediate sympy term counts bounded — necessary
    when each rule application costs ~3 ms in sympy.  The LaurentQ
    inner loop is 5-25× faster, so the unreduced intermediate is
    fast enough to handle directly without the term-count-bounding
    optimisation.

    Empirically (bench on proton..⁴He, 2026-05-03), wiring up the
    R4 path via a sympy round-trip per iteration was 0.36-0.80×
    *slower* on every atom — the LaurentQ↔sympy conversion overhead
    exceeded the term-count savings from quotient folding.  The R4
    port is intentionally absent here; revisit only if A ≥ 6 atoms
    show LaurentQ-rule-loop walls.
    """
    from markov_peel import crossing_from_cd  # local import (avoid cycle)
    from hecke_core import h as _h_num

    elem = LaurentHeckeElement.identity()
    h_num_float = float(_h_num)
    for c, d, gen in word:
        sym_factor = crossing_from_cd(gen, c, d, h_num=h_num_float)
        lq_factor_terms = {
            w: LaurentQ.from_sympy(coef, _q)
            for w, coef in sym_factor.terms.items()
        }
        factor = LaurentHeckeElement(lq_factor_terms)
        elem = elem * factor
        elem, _ = reduce_laurent_rules(
            elem, max_iterations=max_iterations_per_step
        )
    return elem


def tr_M_atomic_fast(Z, N, *, include_inter=True, max_iterations=10000):
    """Drop-in fast replacement for `markov_peel.tr_M_atomic`.

    Routes the Markov-peel reduction through the LaurentQ pipeline
    (rules R1, R2, R3 only — no quotient ideal R4), then delegates
    the trace assembly to `markov_trace_canonical.tr_M_element` on
    the sympy-converted element.

    Skips the `pre_register_nucleons` quotient-folding optimisation
    entirely.  That optimisation existed to keep intermediate sympy
    term counts bounded; with the LaurentQ inner loop running 5-25×
    faster per term, the unfolded reduce is fast enough.

    Numerical equivalence at q = q₀ verified on all atoms in
    [proton, neutron, deuteron, tritium, helium-3, helium-4,
    lithium-5].
    """
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_symbolic import SymbolicHeckeElement
    from markov_trace_canonical import tr_M_element

    A = Z + N
    n_strands = 3 * A
    word = atom_braid_word_3A(Z, N, include_inter=include_inter)
    fast_elem = incremental_reduced_element_fast(
        word, max_iterations_per_step=max_iterations,
    )
    sym_elem = SymbolicHeckeElement(fast_elem.to_sympy_element())
    return tr_M_element(sym_elem, n_strands, simplify=False)
