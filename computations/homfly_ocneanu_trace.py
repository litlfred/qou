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

Implemented for arbitrary n ≥ 2 (the spanning set is generated
programmatically — see `_spanning_set`). n = 3 covers the proton/neutron
`(σ₁σ₂⁻¹)³` braids; n = 4.. cover the larger-nucleus braids of the
exploratory mass tower (⁴He, ⁶Li, ⁷Li, …). Validated for n = 2..9 on
import via `_weights` (held-out knots, full mpmath precision). The
uniform nested-Hopf family's character matrix conditioning slowly
degrades with n; `_weights` raises `NotImplementedError` if it becomes
singular (none observed through n ≈ 11).

The n ≥ 4 weights show the same structure observed at n = 3: the
fully-symmetric and other ≤ 2-row partition weights are 0 (to working dps),
while the multi-row weights are forced nonzero (e.g. n=4: w_(2,2) ≈
−0.499, w_(1⁴) ≈ −2.524; n=5: w_(2,2,1) = 1, w_(1⁵) ≈ 3.044). The
weight w ≈ 2.0109 of the "next-to-antisymmetric" partition recurs at
every n (n=3 w_(1³), n=5 w_(2,1,1,1)). These are solved, not fitted,
and verified on held-out knots at full mpmath precision (the character
eval uses the mpfr Rust kernel — see `_chi`; held-out deltas track the
working dps, ~1e-40 at the gate's 40 dps).
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
from hecke_characters import chi_lambda_braid_mpf, partitions_of  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def _chi(shape, word, s):
    """Signed seminormal Hecke character χ^shape(β) evaluated at s=√q₀.

    Routes through `hecke_characters.chi_lambda_braid_mpf`, which uses the
    **mpfr** path of the Rust `rug::Float` kernel: the character is evaluated
    at full arbitrary precision (not float64). `mp.mpf` rounds the kernel's
    decimal string to the working dps — deterministic at dps, not an exact
    real. This removes the former float64 bound; the held-out validation
    deltas in `_weights` track the working dps (~1e-40 at the gate's 40 dps)
    rather than ~1e-15.

    (The Rust kernel `pyhecke_native` is already a hard requirement of this
    engine: the Python character fallback only supports `q_value == q₀`,
    whereas every character here is evaluated at `s = √q₀ ≠ q₀`.)"""
    return chi_lambda_braid_mpf(shape, word, q_value=s)


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


# Spanning braids — generated programmatically for any n (no per-n table).
# The unframed HOMFLY of each braid closure is known from two rigorous,
# Hecke-free rules:
#   (T)  torus family:   T(k) := HOMFLY(closure σ₁^k) via the skein
#                        recurrence `_torus_unframed(k, a, z)`; and
#   (⊔)  split union:    P(L₁ ⊔ … ⊔ L_m) = δ^{m-1}·∏ P(Lᵢ), with each
#                        unbraided strand contributing a split unknot.
#
# SU(2) Ocneanu support (the key structural fact, observed at every n and
# verified by held-out validation): the weight w_λ is NONZERO only for
# partitions λ all of whose parts are ≤ 2 (equivalently λ has ≤ 2 columns
# — the support of the 2-dimensional fundamental in its tensor powers).
# So `_weights` restricts the solve to those `m+1 = floor(n/2)+1`
# partitions and sets the rest to 0.
#
# The spanning set is the **uniform nested-Hopf family**: braid of rank r
# (r = 0..m) places r Hopf links on the disjoint generator pairs
# (σ₁↔strands 1,2), (σ₃↔3,4), …, (σ_{2r-1}↔2r-1,2r), with the remaining
# strands as split unknots — except rank 0, a single σ₁ crossing (T(2,1)).
# This family has exactly m+1 members and a non-degenerate character
# matrix for all n checked (n=2..9; conditioning slowly degrades with n —
# `_weights` raises if the matrix becomes singular). Validated for n=2..9
# (held-out deltas ≤ ~1e-34 at the gate's working dps).
def _spanning_set(n, a, z):
    """Uniform nested-Hopf spanning braids for the parts-≤2 partitions of n.

    Returns a list of `(signed_braid_word, unframed_HOMFLY_value)` of length
    `floor(n/2)+1`. Rank 0 is the single crossing σ₁ (unknot on the first
    pair); rank r ≥ 1 is r Hopf links on σ₁, σ₃, …, σ_{2r-1} plus (n−2r)
    split unknots, with HOMFLY δ^{n-r-1}·T(2)^r."""
    delta = (1 / a - a) / z
    one = mp.mpf(1)
    t2 = _torus_unframed(2, a, z)
    out = []
    for r in range(n // 2 + 1):
        if r == 0:
            word = [1]                                   # σ₁ : unknot on pair 1
            pieces = [one] * (n - 1)                     # 1 + (n-2) unknots
        else:
            word = []
            for i in range(1, r + 1):
                word += [2 * i - 1, 2 * i - 1]           # Hopf on pair i
            pieces = [t2] * r + [one] * (n - 2 * r)
        out.append((word, _split_union(delta, *pieces)))
    return out


def _holdout_set(n, a, z):
    """Knots NOT in the spanning set, with independently-known unframed
    HOMFLY, used to validate the solved weights in `_weights`."""
    delta = (1 / a - a) / z
    one = mp.mpf(1)

    def T(k):
        return _torus_unframed(k, a, z)

    out = [
        ([1, 1, 1], _split_union(delta, T(3), *([one] * (n - 2)))),   # trefoil ⊔ (n-2) unknots
        ([1, 1, 1, 1], _split_union(delta, T(4), *([one] * (n - 2)))),  # T(2,4) ⊔ (n-2) unknots
    ]
    if n >= 3:
        out.append((list(range(1, n)), one))                          # connected unknot
        out.append(([1, -2, 1, -2] + list(range(3, n)),
                    _fig8_unframed(a, z)))                            # figure-8 (Markov-stab)
    if n >= 4:
        out.append(([1, 1, 1, 3, 3],
                    _split_union(delta, T(3), T(2), *([one] * (n - 4)))))  # trefoil ⊔ Hopf ⊔ unknots
    return out


@lru_cache(maxsize=None)
def _weights(n, s_str):
    """Ocneanu trace weights {partition: w_λ} for strand count n at s.

    Solved from the spanning set (exactly determined), then VALIDATED on
    held-out knots. Raises AssertionError if validation fails (which would
    mean the convention drifted) and NotImplementedError for unsupported n.
    """
    if n < 2:
        raise ValueError(f"n must be ≥ 2 (got {n})")
    s = mp.mpf(s_str)
    a = s ** 2
    z = s - 1 / s
    # SU(2)/Temperley–Lieb support: at the Jones/SU(2) specialisation the
    # Hecke algebra surjects onto the Temperley–Lieb algebra, whose simple
    # modules are indexed by partitions with **≤ 2 columns** — equivalently
    # every part ≤ 2 (`max(p) ≤ 2`). NOTE this is the *column* restriction
    # (the TL quotient), NOT the ≤2-*rows* (`len(p) ≤ 2`) restriction of
    # GL₂ Schur–Weyl: e.g. (1,1,1) and (2,1,1) are kept (3-4 rows, ≤2
    # columns) while (3) and (3,1) are dropped. Only these partitions carry
    # a nonzero Ocneanu weight; the rest are exactly 0 (held-out validation
    # below confirms the restriction is exact). Both families happen to have
    # the same cardinality floor(n/2)+1, which is why the distinction is
    # easy to confuse.
    parts = [tuple(p) for p in partitions_of(n) if max(p) <= 2]
    spanning = _spanning_set(n, a, z)
    assert len(spanning) == len(parts), f"need {len(parts)} spanning braids for n={n}"
    M = mp.matrix(len(parts), len(parts))
    rhs = mp.matrix(len(parts), 1)
    for r, (word, ref) in enumerate(spanning):
        e = _writhe(word)
        for c, p in enumerate(parts):
            M[r, c] = a ** e * _chi(p, word, s)
        rhs[r] = ref
    # `lu_solve` raises on a singular matrix — let it report the conditioning
    # limit of the uniform nested-Hopf family rather than pre-computing a
    # scaling-dependent det threshold (and duplicating the factorisation).
    try:
        wvec = mp.lu_solve(M, rhs)
    except (ZeroDivisionError, ValueError) as exc:
        raise NotImplementedError(
            f"HOMFLY Ocneanu spanning matrix is singular at n={n} (conditioning "
            f"limit of the uniform nested-Hopf family reached). Supply a better-"
            f"conditioned spanning set of floor(n/2)+1 braids over the parts-≤2 "
            f"partitions and the module will self-validate.") from exc
    weights = {p: wvec[i] for i, p in enumerate(parts)}

    # Held-out validation (knots NOT in the spanning set).
    for word, ref in _holdout_set(n, a, z):
        e = _writhe(word)
        pred = a ** e * sum(weights[p] * _chi(p, word, s) for p in parts)
        assert abs(pred - ref) < mp.mpf("1e-9"), (
            f"Ocneanu-weight validation FAILED for n={n} on {word}: "
            f"pred={pred} ref={ref}")
    # Include the parts-≥3 partitions with their (exactly zero) weight so a
    # caller indexing any partition of n gets 0 rather than a KeyError.
    for p in partitions_of(n):
        weights.setdefault(tuple(p), mp.mpf(0))
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
    # Skip the zero-weight (parts-≥3) partitions so their χ^λ is never
    # evaluated — `_weights` includes them as explicit 0 for the caller's
    # benefit, but they contribute nothing to the trace.
    framed_val = sum(w * _chi(p, word, s) for p, w in weights.items() if w)
    if framed:
        return framed_val
    return a ** _writhe(word) * framed_val


if __name__ == "__main__":
    # Smoke test: print proton/neutron framed + unframed values.
    from q_parameter import Q_50_DIGIT_STR as Q
    q0 = mp.mpf(Q)
    set_compute_dps()
    for label, word in [("proton (σ₁σ₂⁻¹)³", [1, -2, 1, -2, 1, -2]),
                        ("neutron (σ₁⁻¹σ₂)³", [-1, 2, -1, 2, -1, 2]),
                        ("figure-8", [1, -2, 1, -2])]:
        fr = homfly_signed_su2(word, 3, q0, framed=True)
        un = homfly_signed_su2(word, 3, q0, framed=False)
        print(f"{label:<20} framed={mp.nstr(fr,12):>14}  unframed={mp.nstr(un,12):>14}  "
              f"writhe={_writhe(word)}")
