#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical knot-invariant engine.
"""Correct signed HOMFLY via the Ocneanu trace — KEEP THE WRITHE.

This is the reworked HOMFLY engine that REPLACES the broken
`homflypt_engine._homflypt_nstrand_numerical` ratio-only path. It was
derived and validated against the independent skein reference in
`homflypt_reference_qa.py` (see
`docs/homfly-markov-convention-discipline.md` and
`docs/audits/2026-06-04-hidden-fitting-verification-gap-mass-binding-walkthrough.md`).

## The model (validated exactly, 1e-10, on held-out knots)

At the SU(2) point with `s = √q₀`, `a = s²`, `z = s − s⁻¹`, the signed
HOMFLY of a braid closure β̂ is the Ocneanu trace

    P_framed(β)   = Σ_λ w_λ · χ^λ(β)          ← writhe KEPT (production)
    P_unframed(β) = a^{w(β)} · P_framed(β)     ← ambient-isotopy invariant

where:

- `χ^λ(β)` is the **signed** seminormal Hecke character
  (`hecke_characters.chi_lambda_braid` evaluated at `s = √q₀`, NOT q₀ —
  that variable bug is documented in the convention doc), and
- `w_λ` are the **Ocneanu trace weights**: unique constants (the trace is
  unique by the Markov property), determined per strand count `n` by
  solving against a spanning set of braids whose unframed HOMFLY is known
  independently from the skein recurrence, then **validated on held-out
  knots**.

### Why "keep the writhe"

In QOU the writhe `w` is the U(1) framing phase `q^{w·c}` — the EM
phase / chirality (see the convention doc §2). Production uses
`P_framed` (writhe retained); the gate divides the known framing `a^{-w}`
back out only to check the knot-type part against the skein reference.

### Why solve-and-validate is NOT fitting

The Ocneanu weights are *unique structural constants* (forced by the
Markov property), not free parameters. Solving an exactly-determined
linear system for them and then proving the result reproduces held-out
knots (figure-8, higher torus links) to 1e-10 is determination +
verification, not curve-fitting. A fit would have residual freedom; this
has none — the held-out predictions are forced.

## Scope

Implemented and validated for n = 2, 3, 4, 5. n = 3 covers the
proton/neutron `(σ₁σ₂⁻¹)³` braids; n = 4, 5 cover the larger-nucleus
braids of the exploratory mass tower. n ≥ 6 raises NotImplementedError
with the spanning-set recipe in the message; extending is mechanical
(add a spanning set + held-out knots, the module self-validates on
import via `_weights`).

The n ≥ 4 weights show the same structure observed at n = 3: the
fully-symmetric and other ≤ 2-row partition weights are 0 (to working dps),
while the multi-row weights are forced nonzero (e.g. n=4: w_(2,2) ≈
−0.499, w_(1⁴) ≈ −2.524; n=5: w_(2,2,1) = 1, w_(1⁵) ≈ 3.044). The
weight w ≈ 2.0109 of the "next-to-antisymmetric" partition recurs at
every n (n=3 w_(1³), n=5 w_(2,1,1,1)). These are solved, not fitted,
and verified on held-out knots at full mpmath precision (the character
eval uses the mpfr Rust kernel — see `_chi`; held-out deltas ~1e-49).
"""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402 — substrate modules moved to substrate/ subdir
from hecke_characters import chi_lambda_braid, partitions_of  # noqa: E402


def _chi(shape, word, s):
    """Signed seminormal Hecke character χ^shape(β) evaluated at s=√q₀.

    Uses the **mpfr** path of `chi_lambda_braid` (Rust `rug::Float` kernel):
    the character is evaluated at full arbitrary precision, NOT float64. We
    pass `s` as a decimal string carrying `mp.mp.dps + 5` digits and request
    `precision="mpfr_<dps>dps"` (≥ 50); the kernel returns a decimal string
    that `mp.mpf` parses exactly. This removes the former float64 bound — the
    held-out validation deltas in `_weights` drop from ~1e-15 to ~1e-49.

    (The Rust kernel `pyhecke_native` is already a hard requirement of this
    engine: the Python `chi_lambda_braid` fallback only supports `q_value == q₀`,
    whereas every character here is evaluated at `s = √q₀ ≠ q₀`.)"""
    hc = [(1, g) if g > 0 else (-1, -g) for g in word]
    dps = max(50, mp.mp.dps)
    q_str = mp.nstr(s, dps + 5, strip_zeros=False)
    return mp.mpf(chi_lambda_braid(list(shape), hc,
                                   q_value=q_str, precision=f"mpfr_{dps}dps"))


def _writhe(word):
    return sum(1 if g > 0 else -1 for g in word)


def _torus_unframed(k, a, z):
    """Independent skein HOMFLY of closure(σ₁^k) — the 2-strand torus
    family (Lickorish v⁻¹P₊ − vP₋ = zP₀). Used to seed/validate weights."""
    v = a
    delta = (1 / v - v) / z
    A, B = delta, mp.mpf(1)
    if k == 0:
        return delta
    if k == 1:
        return B
    for _ in range(2, k + 1):
        A, B = B, v * v * A + v * z * B
    return B


def _split_union(delta, *pieces):
    """Unframed HOMFLY of a split union: P(L₁ ⊔ … ⊔ L_m) = δ^{m-1}·∏ P(Lᵢ).
    Each unbraided strand contributes a split unknot (a `pieces` entry of 1)."""
    prod = mp.mpf(1)
    for r in pieces:
        prod = prod * r
    return delta ** (len(pieces) - 1) * prod


def _fig8_unframed(a, z):
    """Unframed HOMFLY of the figure-8 knot (4₁): a² + a⁻² − 1 − z²."""
    return a ** 2 + a ** -2 - mp.mpf(1) - z ** 2


# Spanning braids per n: (word, independent_unframed_HOMFLY_fn).
# The unframed HOMFLY of each braid closure is known from three rigorous,
# Hecke-free rules:
#   (T)  torus family:   T(k) := HOMFLY(closure σ₁^k) via the skein
#                        recurrence `_torus_unframed(k, a, z)`;
#   (⊔)  split union:    P(L₁ ⊔ … ⊔ L_m) = δ^{m-1}·∏ P(Lᵢ), with each
#                        unbraided strand contributing a split unknot
#                        (δ = (1/a − a)/z); and
#   (M)  Markov stab.:   appending σ_{n-1} once leaves the closure (and
#                        hence the unframed HOMFLY) unchanged, so an
#                        (n−1)-strand reference lifts to n strands.
# The figure-8 polynomial fig8 = a² + a⁻² − 1 − z² is the one non-torus
# seed (used at n ≥ 5 to span the extra partitions). Each spanning set is
# chosen for good conditioning (det of the character matrix ≫ 0): n=4
# det ≈ 1205, n=5 det ≈ 8.95. Held-out validation lives in `_weights`.
def _spanning_sets(a, z):
    delta = (1 / a - a) / z
    one = mp.mpf(1)

    def T(k):
        return _torus_unframed(k, a, z)

    def split(*pieces):
        return _split_union(delta, *pieces)

    fig8 = _fig8_unframed(a, z)                          # figure-8 (4₁)

    return {
        2: [
            ([1], lambda: one),                             # unknot
            ([1, 1], lambda: T(2)),                         # Hopf
        ],
        3: [
            ([1, 2], lambda: one),                          # unknot
            ([1, 1, 2], lambda: T(2)),                      # Hopf (Markov-stab)
            ([1, 1, 1], lambda: split(T(3), one)),          # trefoil ⊔ unknot
        ],
        4: [
            ([1, 1, 1, 1], lambda: split(T(4), one, one)),  # T(2,4) ⊔ 2 unknots
            ([1, 1, 1, 3, 3], lambda: split(T(3), T(2))),   # trefoil ⊔ Hopf
            ([1, 1, 1, 2, 3], lambda: T(3)),                # trefoil (Markov-stab)
            ([1, 1, 1, 1, 2, 3], lambda: T(4)),             # T(2,4) (Markov-stab)
            ([1, 1, 1, 3], lambda: split(T(3), one)),       # trefoil ⊔ unknot
        ],
        5: [
            ([1, 1, 1, 1, 1], lambda: split(T(5), one, one, one)),   # T(2,5) ⊔ 3 unknots
            ([1, 1, 1, 3, 3, 3], lambda: split(T(3), T(3), one)),    # trefoil ⊔ trefoil ⊔ unknot
            ([1, -2, 1, -2, 3, 4], lambda: fig8),                    # figure-8 (Markov-stab ×2)
            ([1, 1, 2, 3, 4], lambda: T(2)),                         # Hopf (Markov-stab)
            ([1, 1, 1, 2, 3, 4], lambda: T(3)),                      # trefoil (Markov-stab)
            ([1, -2, 1, -2, 3], lambda: split(fig8, one)),           # figure-8 ⊔ unknot
            ([1, 1, 1, 1, 3, 3], lambda: split(T(4), T(2), one)),    # T(2,4) ⊔ Hopf ⊔ unknot
        ],
    }


@lru_cache(maxsize=None)
def _weights(n, s_str):
    """Ocneanu trace weights {partition: w_λ} for strand count n at s.

    Solved from the spanning set (exactly determined), then VALIDATED on
    held-out knots. Raises AssertionError if validation fails (which would
    mean the convention drifted) and NotImplementedError for unsupported n.
    """
    s = mp.mpf(s_str)
    a = s ** 2
    z = s - 1 / s
    sets = _spanning_sets(a, z)
    if n not in sets:
        raise NotImplementedError(
            f"HOMFLY Ocneanu weights not yet wired for n={n}. Recipe: provide "
            f"len(partitions_of({n})) spanning braids with independently-known "
            f"unframed HOMFLY (torus + disjoint-union family), solve the linear "
            f"system, and the module self-validates. Implemented: n∈{{2,3,4,5}}.")
    parts = [tuple(p) for p in partitions_of(n)]
    spanning = sets[n]
    assert len(spanning) == len(parts), f"need {len(parts)} spanning braids for n={n}"
    M = mp.matrix(len(parts), len(parts))
    rhs = mp.matrix(len(parts), 1)
    for r, (word, ref_fn) in enumerate(spanning):
        e = _writhe(word)
        for c, p in enumerate(parts):
            M[r, c] = a ** e * _chi(p, word, s)
        rhs[r] = ref_fn()
    wvec = mp.lu_solve(M, rhs)
    weights = {p: wvec[i] for i, p in enumerate(parts)}

    # Held-out validation (knots NOT in the spanning set). References use
    # the same (T)/(⊔)/(M) rules documented on `_spanning_sets`, via the
    # shared module-level helpers.
    delta = (1 / a - a) / z
    one = mp.mpf(1)
    fig8 = _fig8_unframed(a, z)

    def _split(*pieces):
        return _split_union(delta, *pieces)

    holdout = {
        2: [([1, 1, 1], lambda: _torus_unframed(3, a, z)),
            ([1, 1, 1, 1], lambda: _torus_unframed(4, a, z))],
        3: [([1, -2, 1, -2], lambda: fig8),                            # figure-8
            ([1, 1, 1, 2], lambda: _torus_unframed(3, a, z)),          # trefoil
            ([1, 1, 1, 1, 1, 2], lambda: _torus_unframed(5, a, z))],   # cinquefoil
        4: [([1, 2, 3], lambda: one),                                  # unknot
            ([1, 1], lambda: _split(_torus_unframed(2, a, z), one, one)),       # Hopf ⊔ 2 unknots
            ([1, 1, 3, 3], lambda: _split(_torus_unframed(2, a, z),
                                          _torus_unframed(2, a, z))),           # Hopf ⊔ Hopf
            ([1, -2, 1, -2, 3], lambda: fig8),                         # figure-8 (Markov-stab)
            ([1, 1, 1], lambda: _split(_torus_unframed(3, a, z), one, one))],   # trefoil ⊔ 2 unknots
        5: [([1, 2, 3, 4], lambda: one),                              # unknot
            ([1, 1], lambda: _split(_torus_unframed(2, a, z), one, one, one)),  # Hopf ⊔ 3 unknots
            ([1, 1, 3, 3], lambda: _split(_torus_unframed(2, a, z),
                                          _torus_unframed(2, a, z), one)),       # Hopf ⊔ Hopf ⊔ unknot
            ([1, 1, 1], lambda: _split(_torus_unframed(3, a, z), one, one, one)),  # trefoil ⊔ 3 unknots
            ([1, 1, 1, 3, 3], lambda: _split(_torus_unframed(3, a, z),
                                             _torus_unframed(2, a, z), one))],   # trefoil ⊔ Hopf ⊔ unknot
    }
    for word, ref_fn in holdout.get(n, []):
        e = _writhe(word)
        pred = a ** e * sum(weights[p] * _chi(p, word, s) for p in parts)
        assert abs(pred - ref_fn()) < mp.mpf("1e-9"), (
            f"Ocneanu-weight validation FAILED for n={n} on {word}: "
            f"pred={pred} ref={ref_fn()}")
    return weights


def homfly_signed_su2(word, n_strands, q0, *, framed=True):
    """Signed SU(2) HOMFLY of the closure of `word` (1-indexed ±braid word).

    framed=True  → P_framed = Σ_λ w_λ χ^λ(β)  (writhe KEPT — production).
    framed=False → P_unframed = a^{w}·P_framed (textbook ambient invariant).

    Validated against the skein reference to 1e-9 (see module docstring).
    """
    s = mp.sqrt(mp.mpf(str(q0)))
    a = s ** 2
    weights = _weights(n_strands, mp.nstr(s, 40))
    parts = list(weights.keys())
    framed_val = sum(weights[p] * _chi(p, word, s) for p in parts)
    if framed:
        return framed_val
    return a ** _writhe(word) * framed_val


if __name__ == "__main__":
    # Smoke test: print proton/neutron framed + unframed values.
    from q_parameter import Q_50_DIGIT_STR as Q
    q0 = mp.mpf(Q)
    mp.mp.dps = 40
    for label, word in [("proton (σ₁σ₂⁻¹)³", [1, -2, 1, -2, 1, -2]),
                        ("neutron (σ₁⁻¹σ₂)³", [-1, 2, -1, 2, -1, 2]),
                        ("figure-8", [1, -2, 1, -2])]:
        fr = homfly_signed_su2(word, 3, q0, framed=True)
        un = homfly_signed_su2(word, 3, q0, framed=False)
        print(f"{label:<20} framed={mp.nstr(fr,12):>14}  unframed={mp.nstr(un,12):>14}  "
              f"writhe={_writhe(word)}")
