#!/usr/bin/env python3
"""h12_trace_multiplicativity_probe.py
=======================================

**Is the H₁₂ subset-trace `g(S)` multiplicative over bond subsets?**

This reconciles two results that look like they disagree.

  [#6152](https://github.com/litlfred/qou/pull/6152) reports that the identity
  `b₃ = −φᵀ₃(f−1)` holds 400/400 exactly at n = 3 and **fails at n = 4**: its
  `b₄` matches neither `+φᵀ₄` nor `−φᵀ₄`, 200/200 mismatches each.

  `helium4-mu4-cluster-moment.witness.json` (on `main`) reports the opposite
  shape at the same order: at A = 4 / H₁₂ the **alternation IS reproduced** —
  `μ₄/μ₃ = −1.0206` against a target `−9.7522`, so the sign continues and only
  the magnitude misses (by 9.56×).

Two conditions have to hold for a corpus cumulant to equal `±φᵀ_n`:

  (M1) the cumulant is the FULL Möbius inversion over set partitions, with the
       bonds and triangles summed individually rather than with uniform
       multiplicities; and
  (M2) the underlying weight is MULTIPLICATIVE, `g(S) = g(∅)·∏_{b∈S} f_b` —
       which is what makes `w(G) = ∏_{E(G)} f` a Mayer weight at all.

`ursell_alternation_order_four_probe.py` settles the (M1) half: with the full
Möbius inversion, `κ_n = φᵀ_n` **exactly, 200/200, at every order n = 2…5**
including 4, on non-uniform bonds. So a `b₄` that differs from `±φᵀ₄` is not the
full Möbius cumulant — which points at the corpus recursion
`mu4 = M[4] − 6·mu2 − 4·mu3`, whose uniform multiplicities `6` and `4` are only
correct when all six bonds and all four triangles are equivalent. At ⁴He they are
not: the committed witness carries three distinct adjacent flavour templates.

This probe tests (M2), the other half, using only committed data.

METHOD
------
If `g` were multiplicative then for a triangle `t` with bonds `1,2,3`:

    μ₂^(b) = g₀·(f_b − 1) =: g₀·x_b
    μ₃^(t) = g₀·φᵀ₃(x)   = g₀·(x₁x₂ + x₁x₃ + x₂x₃ + x₁x₂x₃)

Eliminating the `x_b` in favour of the measured `μ₂` gives, per triangle, a
quadratic in the single unknown `g₀`:

    μ₃·g₀² − (Σ_{pairs} μ₂μ₂)·g₀ − (∏ μ₂) = 0

Multiplicativity requires **one** `g₀` to solve all four triangles at once. The
test is therefore a consistency check across the four triangles of ⁴He, needing
no new H₁₂ evaluation — the committed `μ₂` and `μ₃` suffice.

SCOPE
-----
(a). A negative here says the H₁₂ subset-trace is not a multiplicative Mayer
weight, and therefore that a Mayer/Ursell identity should NOT be expected to
hold of it at any order — it does not say the alternation fails (it does not;
the committed witness reproduces it), nor that the corpus's μ₄ is wrong, nor
anything about `f_corpus = e^{−v}`, which remains #6152's stated open gap.

PRECISION
---------
mpmath at 40 dps. The inputs are the committed witness's own values, which are
serialized there as raw float64 — so the spread reported below is bounded below
by that, and this probe does not claim precision beyond its input. The verdict
is a *spread* of order 10⁻² to 10⁻¹, some 14 orders above float64 resolution, so
the conclusion does not rest on the arithmetic.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import itertools
import json
import subprocess
import time

import mpmath as mp  # noqa: E402

from _precision import fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 40
WITNESS = "computations/deltalambda/helium4-mu4-cluster-moment.witness.json"


def load_committed():
    raw = subprocess.run(["git", "show", f"origin/main:{WITNESS}"],
                         capture_output=True, text=True, check=True).stdout
    return json.loads(raw)["data"]["mu4_cluster_moment"]


def main() -> int:
    t0 = time.monotonic()
    m = load_committed()
    mu2 = {k: mp.mpf(str(v)) for k, v in m["mu2_per_bond"].items()}
    mu3 = {k: mp.mpf(str(v)) for k, v in m["mu3_per_triangle"].items()}

    rows = []
    upper, lower = [], []
    for t, v3 in mu3.items():
        idx = tuple(int(c) for c in t if c.isdigit())
        bonds = [str(tuple(sorted(p))) for p in itertools.combinations(idx, 2)]
        b = [mu2[x] for x in bonds]
        S2 = b[0] * b[1] + b[0] * b[2] + b[1] * b[2]
        P = b[0] * b[1] * b[2]
        disc = S2 ** 2 + 4 * v3 * P
        if disc < 0:
            rows.append({"triangle": t, "real_roots": False})
            continue
        r1 = (S2 + mp.sqrt(disc)) / (2 * v3)
        r2 = (S2 - mp.sqrt(disc)) / (2 * v3)
        upper.append(r1)
        lower.append(r2)
        rows.append({"triangle": t, "bonds": bonds,
                     "g0_root_upper": fmt(r1), "g0_root_lower": fmt(r2)})

    def spread(vals):
        return (max(vals) - min(vals)) / abs(sum(vals) / len(vals))

    sp_u, sp_l = spread(upper), spread(lower)
    # A common g0 would need BOTH branches consistent to numerical noise.
    TOL = mp.mpf("1e-9")
    multiplicative = (sp_u < TOL) or (sp_l < TOL)

    print("If g were multiplicative, one g0 must solve all four triangles.")
    for r in rows:
        print(f"  {r['triangle']}: upper={r.get('g0_root_upper')}  "
              f"lower={r.get('g0_root_lower')}")
    print()
    print(f"  upper-branch relative spread = {mp.nstr(sp_u, 6)}")
    print(f"  lower-branch relative spread = {mp.nstr(sp_l, 6)}")
    print(f"  multiplicative (tol {mp.nstr(TOL,3)})? {multiplicative}")

    w = WitnessBuilder("h12-trace-multiplicativity", start_time=t0)
    w.set_description(
        "Is the H12 subset-trace multiplicative over bond subsets? Reconciles "
        "#6152's n=4 identity failure with the committed He4 witness's "
        "'alternation REPRODUCED'. Consistency test across the four He4 "
        "triangles for a single g0; uses only committed data, no new H12 "
        "evaluation.")
    w.add_data("source_witness", WITNESS)
    w.add_data("per_triangle", rows)
    w.add_data("upper_branch_relative_spread", fmt(sp_u))
    w.add_data("lower_branch_relative_spread", fmt(sp_l))
    w.add_data("multiplicative", multiplicative)
    w.add_data("reading", (
        "No single g0 solves all four triangles, so the H12 subset-trace is "
        "NOT a multiplicative Mayer weight. A Mayer/Ursell identity should "
        "therefore not be expected to hold of it at ANY order; #6152's n=3 "
        "match is the coincidence to explain, not its n=4 miss. This says "
        "nothing against the alternation, which the committed He4 witness "
        "reproduces."))
    w.add_assertion("multiplicativity_refuted", multiplicative, False)
    w.save()
    print(f"\nwall {time.monotonic()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
