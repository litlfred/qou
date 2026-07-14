#!/usr/bin/env python3
"""qbeta_dladder_log_q_holonomic_probe.py — is log D(ũ) (q-)holonomic?

Owner suggestion (2026-07-14): the #3716/#3737 negatives tested D(ũ) = Σ d_k ũ^k
itself. But (q-)holonomicity is NOT closed under log/exp — if D = exp(G) with G
(q-)holonomic, D itself is generically not. So the LOG of the ladder is a
genuinely distinct, untested class, and a positive here would be an exact
structural characterization the direct tests could not see.

Objects (exact, ℚ(√3), from the same merged build path as #3737):
    D(ũ) = d₁·ũ·(1 + E(ũ)),   ℓ(ũ) = log(1 + E) = Σ_{k≥1} ℓ_k ũ^k
    (power-series log recursion ℓ_k = e_k − (1/k)·Σ_{j<k} j·ℓ_j·e_{k−j};
     e_k = d_{k+1}/d₁ ∈ ℚ(√3), so every ℓ_k ∈ ℚ(√3) exactly).
    Also tested: the log-derivative coefficients k·ℓ_k (= coefficients of
    ũ·D′/D − 1) — equivalent to ℓ_k for polynomial-in-k recurrences but NOT
    for q-holonomic (base-Xᵏ) ones, so both sequences get both kernels.

Kernels (reused verbatim from the merged probes):
    * coupled ℚ(√3) P-recurrence (qbeta_dladder_coupled_qsqrt3_recurrence_probe
      .coupled_recurrence_kernel) — exact rational null space;
    * q-holonomic base X ∈ {3, 1/3} + classical-k control
      (qbeta_dladder_q_holonomic_base3_probe.q_holonomic_kernel) — negative
      certified by full column rank mod large primes.

Same finite-window honesty as #3737: negatives close the LOW-ORDER windows
(coupled r≤2/D≤4, r=3/D≤3, r=4/D≤2; q-holonomic r≤3/E≤3) — not all orders.
A nontrivial null vector at any cell is an exact closed-form recurrence for
log D (decisive positive). auditOnly; no c_k; no fit; no wiring.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent          # computations/qbeta
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "substrate"))

from qbeta_dladder_coupled_qsqrt3_recurrence_probe import (  # noqa: E402
    exact_dk, coupled_recurrence_kernel,
)
from qbeta_dladder_q_holonomic_base3_probe import (  # noqa: E402
    q_holonomic_kernel,
)

COUPLED_WINDOWS = [(1, 4), (2, 4), (3, 3), (4, 2)]     # (r, D)
QHOLO_WINDOWS = [(r, E) for r in (1, 2, 3) for E in (1, 2, 3)]
QHOLO_BASES = [("base3", sp.Integer(3)), ("base1/3", sp.Rational(1, 3)),
               ("classical_k", None)]


def log_coeffs(ab, KMAX):
    """Exact ℓ_k ∈ ℚ(√3) of log(D/(d₁ũ)), as (rational, √3-part) pairs."""
    s3 = sp.sqrt(3)
    d = {k: ab[k][0] + ab[k][1] * s3 for k in range(1, KMAX + 1)}
    d1 = d[1]
    assert sp.simplify(d1) != 0, "d_1 vanishes — normalization invalid"
    # e_k = d_{k+1}/d_1, k = 1..KMAX-1  (rationalize the ℚ(√3) division)
    e = {}
    for k in range(1, KMAX):
        e[k] = sp.expand(sp.radsimp(d[k + 1] / d1))
    L = {}
    for k in range(1, KMAX):
        acc = e[k]
        for j in range(1, k):
            acc -= sp.Rational(j, k) * L[j] * e[k - j]
        L[k] = sp.expand(acc)
    # split into exact ℚ pairs
    ab_l = {}
    for k, v in L.items():
        b = sp.nsimplify(sp.expand(v).coeff(s3, 1))
        a = sp.nsimplify(sp.expand(v - b * s3))
        assert a.is_rational and b.is_rational, (k, a, b)
        ab_l[k] = (sp.Rational(a), sp.Rational(b))
    return ab_l, KMAX - 1, d1


def run_kernels(name, ab_seq, kmax, results):
    print(f"\n  [{name}] coupled ℚ(√3) P-recurrence windows:")
    for r, D in COUPLED_WINDOWS:
        ns, n, nrows = coupled_recurrence_kernel(ab_seq, kmax, r, D)
        verdict = "NONTRIVIAL NULLSPACE (recurrence!)" if ns else "none"
        results[f"{name}/coupled r={r} D={D}"] = {
            "unknowns": n, "rows": nrows, "nullspace_dim": len(ns), "verdict": verdict}
        print(f"    r={r} D={D}: unknowns {n}, rows {nrows} -> {verdict}")
        if ns:
            results[f"{name}/coupled r={r} D={D}"]["null_vector"] = [str(x) for x in ns[0]]
    print(f"  [{name}] q-holonomic windows:")
    for bname, base in QHOLO_BASES:
        for r, E in QHOLO_WINDOWS:
            has_ns, n, nrow = q_holonomic_kernel(ab_seq, kmax, r, E, base)
            verdict = ("NONTRIVIAL NULLSPACE (recurrence!)" if has_ns
                       else "full rank (no recurrence)")
            results[f"{name}/qholo {bname} r={r} E={E}"] = {
                "unknowns": n, "rows": nrow, "has_nullspace": bool(has_ns), "verdict": verdict}
            if has_ns:
                print(f"    {bname} r={r} E={E}: {verdict}")
    print(f"    (q-holonomic: all cells full-rank unless printed above)")


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" log D(ũ) (q-)holonomy — the log-closure class the C-negatives did not test")
    print("=" * 78)

    ab, KMAX = exact_dk()
    ab_l, LMAX, d1 = log_coeffs(ab, KMAX)
    print(f"\n  exact d_k rebuilt k=1..{KMAX}; exact ℓ_k of log(D/(d₁ũ)) k=1..{LMAX}; d₁ = {d1}")

    # k·ℓ_k (the ũ·D′/D − 1 coefficients)
    ab_kl = {k: (k * a, k * b) for k, (a, b) in ab_l.items()}

    results = {}
    run_kernels("logD", ab_l, LMAX, results)
    run_kernels("k_logD_prime", ab_kl, LMAX, results)

    positives = [k for k, v in results.items()
                 if v.get("nullspace_dim", 0) > 0 or v.get("has_nullspace")]
    verdict = ("POSITIVE — exact recurrence found for log D (cells: %s)" % positives
               if positives else
               "NEGATIVE — log D is not low-order coupled-ℚ(√3) P-finite nor "
               "q-holonomic in base 3 / 1/3 / classical k (same windows as #3737); "
               "the log-closure loophole is CLOSED at accessible order")
    print(f"\n  VERDICT: {verdict}")

    witness = {
        "computation": "qbeta-dladder-log-q-holonomic",
        "description": (
            "Owner-suggested log-closure test: (q-)holonomicity is not closed "
            "under log/exp, so the #3716/#3737 negatives on D(u) do not cover "
            "log D. Exact l_k in Q(sqrt3) of log(D/(d1*u)) via the power-series "
            "log recursion (and k*l_k = the u*D'/D coefficients, distinct under "
            "base-X^k recurrences); both sequences run through the SAME two "
            "merged kernels: coupled Q(sqrt3) P-recurrence (exact nullspace; "
            "windows r<=2/D<=4, r=3/D<=3, r=4/D<=2) and q-holonomic base 3, 1/3, "
            "classical-k control (prime-certified full rank; r<=3, E<=3). "
            "Finite-window honesty as in #3737. " + verdict + ". auditOnly; "
            "no c_k; no fit; no wiring."
        ),
        "audit_only": True,
        "parameters": {"KMAX_d": KMAX, "LMAX": LMAX, "d1": str(d1),
                       "coupled_windows": COUPLED_WINDOWS,
                       "qholo_windows": QHOLO_WINDOWS,
                       "qholo_bases": [b[0] for b in QHOLO_BASES]},
        "l_k_a_b": {str(k): [str(a), str(b)] for k, (a, b) in ab_l.items()},
        "cells": results,
        "verdict": verdict,
        "assertions": [
            {"label": "exact l_k computed in Q(sqrt3) for k=1..%d" % LMAX, "passed": True},
            {"label": "all cells executed (2 sequences x %d coupled + %d qholo)" % (
                len(COUPLED_WINDOWS), len(QHOLO_BASES) * len(QHOLO_WINDOWS)),
             "passed": len(results) == 2 * (len(COUPLED_WINDOWS) + len(QHOLO_BASES) * len(QHOLO_WINDOWS))},
        ],
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    import os
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-dladder-log-q-holonomic.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  Witness: {out.name}   ({time.monotonic() - t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
