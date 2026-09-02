#!/usr/bin/env python3
"""ursell_alternation_order_four_probe.py
==========================================

**Does the Ursell sign alternation `(−1)^{n−1} φᵀ_n ≥ 0` continue at n = 4?**

[#6152](https://github.com/litlfred/qou/pull/6152) established, in exact rational
arithmetic, that the Mayer/Ursell sign law is `(−1)^{n−1}` (0/200 for the OCR's
`(−1)^n`, 200/200 for `(−1)^{n−1}`), that the corpus carries a **uniform** minus
instead, and that `MayerThreeBodySign`'s forced `b₃ < 0` is that missing
alternation rather than a physical obstruction. It also reported that the
low-order identity `b₃ = −φᵀ₃(f−1)` does **not** extend to `n = 4`: `b₄` matched
neither `+φᵀ₄` nor `−φᵀ₄`, 200/200 mismatches each.

That left the question this probe answers. Two things were conflated in "does it
extend to n=4", and they have different answers:

  (Q1) does the SIGN LAW `(−1)^{n−1} φᵀ_n ≥ 0` hold at n = 4 (and 5)?
  (Q2) does the corpus's `b₄` equal `−φᵀ₄`, as `b₃ = −φᵀ₃` does at n = 3?

Q1 is a statement about Mayer/Ursell functions alone. Q2 is a statement about
whether the corpus's 4-body cumulant is built the same way as its 3-body one.
A negative on Q2 says nothing about Q1.

WHAT IS COMPUTED
----------------
For n = 2…5, over the complete graph K_n with a bond variable per edge:

  φᵀ_n(g)  = Σ_{G connected spanning subgraph of K_n} ∏_{e ∈ E(G)} g_e
             — the Ursell function, by direct enumeration of edge subsets with
               a connectivity test. No formula is assumed.

  κ_n(f)   = Σ_{π ⊢ [n]} (|π|−1)! (−1)^{|π|−1} ∏_{B ∈ π} F(B),
             F(B) = ∏_{pairs ⊆ B} f  — the cumulant by Möbius inversion over
             set partitions.

  b_n^corpus = −κ_n  — the corpus's convention, read off `MayerThreeBodySign`
             (`b3 f P3 = (1−P3) − 3·b2 f`, `b2 f = 1−f`, giving `3f−2−f³`,
             which is exactly `−κ₃`).

Then: (i) `φᵀ_n(f−1) = κ_n(f)` as an identity; (ii) the sign of
`(−1)^{n−1} φᵀ_n` on the repulsive class `f ∈ (0,1)`; (iii) whether
`b_n^corpus = −φᵀ_n` at each n.

PRECISION
---------
`fractions.Fraction` end to end — **exact**, no tolerance and no float anywhere,
so every verdict is a decision rather than a measurement. `float()` appears only
in display f-strings.

SCOPE
-----
(a). This measures the sign law and the identity. It does not claim the corpus's
4-body assembly is right or wrong, does not identify any physical binding term,
and does not establish `f_corpus = e^{−v}` — the load-bearing gap #6152 names
and which this probe inherits untouched.
"""
from __future__ import annotations

# Bootstrap BEFORE importing the bridge (bean `qou-0e1t`).
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import itertools
import random
import time
from fractions import Fraction

from qou_substrate.witness import WitnessBuilder  # noqa: E402


def edges(n):
    return list(itertools.combinations(range(n), 2))


def connected(n, edge_subset):
    """Is the spanning subgraph with these edges connected on all n vertices?"""
    if n == 1:
        return True
    adj = {v: set() for v in range(n)}
    for a, b in edge_subset:
        adj[a].add(b)
        adj[b].add(a)
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == n


def phi_T(n, g):
    """Ursell φᵀ_n by direct enumeration of connected spanning subgraphs.

    `g` maps an edge (i,j) -> Fraction. No closed form assumed.
    """
    E = edges(n)
    total = Fraction(0)
    for r in range(len(E) + 1):
        for sub in itertools.combinations(E, r):
            if connected(n, sub):
                term = Fraction(1)
                for e in sub:
                    term *= g[e]
                total += term
    return total


def _partitions(collection):
    collection = list(collection)
    if len(collection) == 1:
        yield [collection]
        return
    first = collection[0]
    for smaller in _partitions(collection[1:]):
        for k, subset in enumerate(smaller):
            yield smaller[:k] + [[first] + subset] + smaller[k + 1:]
        yield [[first]] + smaller


def _factorial(k):
    out = 1
    for i in range(2, k + 1):
        out *= i
    return out


def kappa(n, f):
    """Cumulant κ_n by Möbius inversion over set partitions.

    `f` maps an edge (i,j) -> Fraction; F(block) = ∏ f over pairs inside it.
    """
    total = Fraction(0)
    for pi in _partitions(range(n)):
        prod = Fraction(1)
        for block in pi:
            for a, b in itertools.combinations(sorted(block), 2):
                prod *= f[(a, b)]
        k = len(pi)
        total += Fraction((-1) ** (k - 1) * _factorial(k - 1)) * prod
    return total


def main() -> int:
    t0 = time.monotonic()
    rng = random.Random(20260830)
    N_SAMPLES = 200
    results = {}
    assertions = []

    for n in (2, 3, 4, 5):
        E = edges(n)
        ident_ok = 0
        sign_ok = 0
        worst_sign_value = None
        for _ in range(N_SAMPLES):
            # repulsive class: f ∈ (0,1) strictly, so g = f-1 ∈ (-1,0)
            f = {e: Fraction(rng.randint(1, 9999), 10000) for e in E}
            g = {e: f[e] - 1 for e in E}
            pt = phi_T(n, g)
            kp = kappa(n, f)
            if pt == kp:
                ident_ok += 1
            # the alternation claim
            alt = pt if (n - 1) % 2 == 0 else -pt
            if alt >= 0:
                sign_ok += 1
            if worst_sign_value is None or alt < worst_sign_value:
                worst_sign_value = alt
        results[f"n={n}"] = {
            "n_edges": len(E),
            "samples": N_SAMPLES,
            "phiT_equals_kappa": f"{ident_ok}/{N_SAMPLES}",
            "alternation_(-1)^(n-1)*phiT_ge_0": f"{sign_ok}/{N_SAMPLES}",
            "worst_(-1)^(n-1)*phiT_exact": str(worst_sign_value),
        }
        assertions.append((n, ident_ok, sign_ok))
        print(f"n={n}  edges={len(E):>2}  "
              f"phiT==kappa {ident_ok}/{N_SAMPLES}  "
              f"(-1)^(n-1)*phiT>=0 {sign_ok}/{N_SAMPLES}  "
              f"worst={float(worst_sign_value):+.6g}")

    # uniform-bond closed forms, for the record
    print()
    uniform = {}
    for n in (2, 3, 4, 5):
        E = edges(n)
        # evaluate at the chi typing f = z_D(q0) used by #6152
        fv = Fraction(6126880371, 10000000000)
        f = {e: fv for e in E}
        g = {e: fv - 1 for e in E}
        pt = phi_T(n, g)
        uniform[f"n={n}"] = {
            "f_uniform": str(fv), "phiT_exact": str(pt),
            "minus_phiT_exact": str(-pt),
            "alternation_sign_expected": (-1) ** (n - 1),
        }
        print(f"  uniform f={float(fv):.10f}  n={n}:  phiT={float(pt):+.10f}   "
              f"corpus b_n = -phiT = {float(-pt):+.10f}")

    w = WitnessBuilder("ursell-alternation-order-four", start_time=t0)
    w.set_description(
        "Does the Ursell sign alternation (-1)^(n-1)*phi^T_n >= 0 continue at "
        "n=4? Separates the SIGN LAW (Q1) from whether the corpus's b_4 equals "
        "-phi^T_4 (Q2) — #6152 reported a negative on the n=4 identity, which "
        "does not by itself settle the sign law. Exact Fraction arithmetic; "
        "phi^T by direct connected-subgraph enumeration, kappa by Moebius "
        "inversion over set partitions, neither assuming a closed form.")
    w.add_data("method", {
        "phiT": "direct enumeration of connected spanning subgraphs of K_n",
        "kappa": "Moebius inversion over set partitions of [n]",
        "corpus_convention": ("b_n = -kappa_n, read off MayerThreeBodySign: "
                              "b3 f P3 = (1-P3) - 3*b2 f with b2 f = 1-f, "
                              "i.e. 3f-2-f^3 = -kappa_3"),
        "arithmetic": "fractions.Fraction, exact, no tolerance, no float",
        "repulsive_class": "f in (0,1) strictly, sampled as Fraction(k,10000)",
    })
    w.add_data("by_order", results)
    w.add_data("uniform_chi_typing", uniform)
    for n, ident_ok, sign_ok in assertions:
        w.add_assertion(f"phiT_equals_kappa_n{n}", ident_ok, N_SAMPLES)
        w.add_assertion(f"alternation_holds_n{n}", sign_ok, N_SAMPLES)
    w.save()
    print(f"\nwall {time.monotonic()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
