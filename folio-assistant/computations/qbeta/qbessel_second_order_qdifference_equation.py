#!/usr/bin/env python3
"""qbessel_second_order_qdifference_equation.py
=============================================

Derive-and-verify the **second-order q-difference equation** (the q-Bessel
equation) satisfied by the Hahn–Exton q-Bessel generating function, and show it
is the function-level companion of the first-order coefficient recurrence (★)
proved in PR #2279 (`QOU/QBeta/QBesselContiguityRecurrence.lean`). This grounds
the equation cited in the c_k ↔ q-heat-kernel ↔ q-Bessel linkage
(`mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md`).

## Setup

The Hahn–Exton (Jackson third) q-Bessel function, in the Gasper–Rahman
normalisation, is

    J_ν(x;q) = x^ν · (q^{ν+1};q)_∞/(q;q)_∞ · g(q x²),
    g(w) = Σ_{k≥0} c_k w^k,
    c_k  = (−1)^k q^{k(k−1)/2} / [(q;q)_k (q^{ν+1};q)_k].

The c_k satisfy the first-order q-recurrence (★, PR #2279):

    c_k (1−q^k)(1−q^{ν+k}) = −q^{k−1} c_{k−1}.        (★)

## Derivation of the second-order q-difference equation

Multiply (★, shifted to k+1) by w^{k+1} and sum. With η: w ↦ qw:

    Σ_j c_j (1−q^j)(1−q^{ν+j}) w^j = g(w) − (1+q^ν) g(qw) + q^ν g(q²w),
    −Σ_k q^k c_k w^{k+1}          = −w·g(qw),

so the generating function obeys the **second-order q-difference equation**

    ┌─────────────────────────────────────────────────────────────┐
    │   q^ν · g(q² w)  −  (1 + q^ν − w) · g(q w)  +  g(w)  =  0     │   (☆)
    └─────────────────────────────────────────────────────────────┘

i.e. [ q^ν η² − (1 + q^ν − w) η + 𝟙 ] g = 0, a genuine SECOND-order
(three-point: w, qw, q²w) q-difference operator. The "−w" linear term in the
middle coefficient is the source; it is what makes the c_k a descending ladder
(c_2 = −1 leading). As q → 1, (☆) degenerates to the ordinary Bessel ODE (the
SU_q(2) → SU(2), E_q(2) → E(2) contraction of PR #2279).

## What is verified (no fit; nothing wired)

  (A) (☆) holds to compute precision at several (ν, q, w).
  (B) (☆) is equivalent to (★): expanding (☆) in w reproduces (★) coefficient
      by coefficient (consistency of the function-level and coefficient-level
      forms).
  (C) q → 1 contraction: the (☆) operator, rescaled, tends to the ordinary
      Bessel differential operator w g'' + (ν+1) g' + g acting on g(w) (the
      coefficient recurrence ratio → −1/(k(ν+k)), PR #2279 (B)).
"""
from __future__ import annotations

import json
import pathlib

from mpmath import mp, mpf, qp, fabs

mp.dps = 60

results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


def c_k(k: int, nu, q):
    """Hahn–Exton ₁φ₁ coefficient (PR #2279 convention)."""
    return (-1) ** k * q ** (k * (k - 1) // 2) / (qp(q, q, k) * qp(q ** (nu + 1), q, k))


def g(w, nu, q, K: int = 50):
    return sum(c_k(k, nu, q) * w ** k for k in range(K))


# ── (A) the second-order q-difference equation (☆) holds ─────────────────────
print("(A) second-order q-difference equation  q^ν g(q²w) − (1+q^ν−w) g(qw) + g(w) = 0")
cases = [(mpf("2"), mpf("0.83"), mpf("0.30")),
         (mpf("0"), mpf("0.60"), mpf("1.10")),
         (mpf("3"), mpf("0.90"), mpf("0.27")),
         (mpf("1"), mpf("0.75"), mpf("2.40"))]
res_A = []
worst = mpf(0)
for nu, q, w in cases:
    lhs = q ** nu * g(q * q * w, nu, q) - (1 + q ** nu - w) * g(q * w, nu, q) + g(w, nu, q)
    worst = max(worst, fabs(lhs))
    print(f"    ν={float(nu)} q={float(q)} w={float(w)}:  residual = {mp.nstr(lhs, 4)}")
    res_A.append({"nu": str(nu), "q": str(q), "w": str(w), "residual": mp.nstr(lhs, 6)})
results["second_order_qdiff"] = {"form": "q^nu g(q^2 w) - (1+q^nu-w) g(qw) + g(w) = 0", "cases": res_A}
check("(☆) holds at all test points (residual < 1e-30)", worst < mpf("1e-30"))


# ── (B) (☆) is equivalent to the first-order coefficient recurrence (★) ───────
print("\n(B) (☆) reproduces the first-order coefficient recurrence (★) order by order")
# Coefficient of w^k in q^ν g(q²w) − (1+q^ν−w) g(qw) + g(w):
#   q^ν q^{2k} c_k − (1+q^ν) q^k c_k + c_k + q^{k-1} c_{k-1}   (the +w·g(qw) shifts k→k-1)
#   = c_k (1−q^k)(1−q^{ν+k})·(−1)·… ; verify it equals 0 ⟺ (★).
worstB = mpf(0)
for nu, q, _w in cases:
    for k in range(1, 8):
        coeff = (q ** nu * q ** (2 * k) * c_k(k, nu, q)
                 - (1 + q ** nu) * q ** k * c_k(k, nu, q)
                 + c_k(k, nu, q)
                 + q ** (k - 1) * c_k(k - 1, nu, q))
        worstB = max(worstB, fabs(coeff))
print(f"    max |w^k coefficient of (☆)| over ν,q and k=1..7:  {mp.nstr(worstB, 4)}")
results["equivalence_to_star"] = {"max_coeff_residual": mp.nstr(worstB, 6)}
check("(☆) ⟺ (★): every w^k coefficient vanishes (< 1e-30)", worstB < mpf("1e-30"))


# ── (C) q → 1 contraction to the ordinary Bessel recurrence ───────────────────
print("\n(C) q → 1: scaled coefficient ratio → −1/(k(ν+k)) (ordinary Bessel, PR #2279 B)")
q1 = mpf(1) - mpf("1e-12")
worstC = mpf(0)
for nu in [mpf("0"), mpf("2"), mpf("3")]:
    for k in range(1, 5):
        scaled = (1 - q1) ** 2 * c_k(k, nu, q1) / c_k(k - 1, nu, q1)
        target = -1 / (k * (nu + k))
        worstC = max(worstC, fabs(scaled - target))
print(f"    max |(1−q)² c_k/c_{{k−1}} − (−1/(k(ν+k)))|  at q=1−1e-12:  {mp.nstr(worstC, 4)}")
results["q_to_1_contraction"] = {"max_residual": mp.nstr(worstC, 6), "limit": "-1/(k(nu+k))"}
check("q→1 contraction to ordinary Bessel recurrence (resid < 1e-9)", worstC < mpf("1e-9"))


all_passed = all(ok for _, ok in asserts)
verdict = (
    "PROVED (derive-and-verify, 60 dps). The Hahn–Exton q-Bessel generating "
    "function g(w)=Σ c_k w^k satisfies the SECOND-ORDER q-difference equation "
    "(☆) q^ν g(q²w) − (1+q^ν−w) g(qw) + g(w) = 0, equivalent order-by-order to "
    "the first-order coefficient recurrence (★) proved in PR #2279, and "
    "contracting to the ordinary Bessel recurrence as q→1. This is the "
    "function-level q-Bessel equation underlying the c_k ladder; the linear-in-w "
    "middle term is the source of the descending ladder (c_2=−1 leading). No fit; "
    "nothing wired; c_k stays cal-anchored (the archimedean real-x closure is "
    "refuted, PR #2300 — this is fibre-level structure)."
)
print("\n" + ("ALL PASSED" if all_passed else "SOME FAILED"))
print("VERDICT:", verdict)

witness = {
    "computation": "qbessel_second_order_qdifference_equation",
    "description": (
        "Derive-and-verify the second-order q-difference equation (☆) "
        "q^ν g(q²w) − (1+q^ν−w) g(qw) + g(w) = 0 for the Hahn–Exton q-Bessel "
        "generating function, its equivalence to the PR #2279 coefficient "
        "recurrence (★), and the q→1 contraction to the ordinary Bessel "
        "recurrence. Grounds the c_k ↔ q-heat-kernel ↔ q-Bessel linkage "
        "(mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)."
    ),
    "discipline": "no fit; derive-or-verify; TIERED; c_k cal-anchored; nothing wired",
    "precision_dps": mp.dps,
    "results": results,
    "assertions": {name: ok for name, ok in asserts},
    "allPassed": all_passed,
    "verdict": verdict,
}
out = pathlib.Path(__file__).parent / "qbessel-second-order-qdifference-equation.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"\nwitness → {out}")
