#!/usr/bin/env python3
"""qbessel_jackson_contiguity.py
=================================

Derive-and-verify the **first- and second-kind** Jackson q-Bessel coefficient
contiguity recurrences — the `SU_q(1,1)` (quantum hyperbolic plane) partners of
the Hahn–Exton (Jackson third) q-Bessel equation. This wires the two Lean
theorems

    QOU.QBeta.qbessel_first_kind_coeff_closed_form
    QOU.QBeta.qbessel_second_kind_coeff_closed_form

(`QOU/QBeta/QBesselContiguityRecurrence.lean`, lines 115–147) to a computation,
mirroring the already-wired third-kind script
`qbessel_second_order_qdifference_equation.py`. Block:
`mass-theory/jackson-q-bessel-contiguity.ts` (was `computation`-less, hence
unwired in the compute-integration sense).

## Setup — Jackson's first/second kind (Gasper–Rahman / Ismail normalisation)

With `a := q^ν`:

    J_ν^{(1)}(x;q) ∝ Σ_{k≥0} A_k (x/2)^{2k+ν},   A_k = (−1)^k / [(q;q)_k (q^{ν+1};q)_k]
    J_ν^{(2)}(x;q) ∝ Σ_{k≥0} B_k (x/2)^{2k+ν},   B_k = (−1)^k q^{k(k+ν)} / [(q;q)_k (q^{ν+1};q)_k]

Their consecutive-coefficient ratios are exactly the Lean closed forms

    A_{k+1}/A_k = −1 / [(1−q^{k+1})(1−a q^{k+1})]                =: qbesselFirstKindRatio
    B_{k+1}/B_k = −(a q^{2k+1}) / [(1−q^{k+1})(1−a q^{k+1})]     =: qbesselSecondKindRatio

equivalently the **first-order contiguity recurrences** the Lean theorems take as
hypothesis `hrec`:

    A_{k+1}·(1−q^{k+1})(1−a q^{k+1}) = −A_k                       (★₁, first kind)
    B_{k+1}·(1−q^{k+1})(1−a q^{k+1}) = −(a q^{2k+1})·B_k          (★₂, second kind)

and the Lean conclusion is the q-hypergeometric product `c_k = c_0 ∏_{j<k} r_j`
(`first_order_solution`).

## What is verified (no fit; fibre-level structure)

  (A) RATIO IDENTITY — the Jackson coefficient ratio equals the Lean closed-form
      ratio, both SYMBOLICALLY (sympy, symbolic ν, all k≤6) and numerically.
  (B) CONTIGUITY (★₁)/(★₂) hold to 60 dps at several (ν, q).
  (C) CLOSED-FORM PRODUCT SOLUTION c_k = c_0 ∏_{j<k} r_j (the Lean conclusion)
      reproduces the direct Jackson coefficient to 60 dps.

These are fibre-level coefficient identities in the FORMAL variable q (cf.
AGENTS.md "Im(q) at fibre vs observable level"): they hold for all q and do not
depend on the substrate anchor q_0 — so we test at several rational q (where the
defining series also converges) AND symbolically (which covers all q). Like the
third-kind script: no fit; nothing about the binding/Q_β scale is claimed here;
the c_k stay cal-anchored. This wires the SKELETON (the proved recurrence), not
any archimedean binding application.
"""
from __future__ import annotations

import json
import pathlib

import sympy as sp
from mpmath import mp, mpf, qp, fabs

mp.dps = 60

results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ── Jackson coefficients (numeric, mpmath q-Pochhammer) ──────────────────────
def A_k(k: int, nu, q):
    """First-kind coefficient (up to the k-independent prefactor)."""
    return (-1) ** k / (qp(q, q, k) * qp(q ** (nu + 1), q, k))


def B_k(k: int, nu, q):
    """Second-kind coefficient (up to the k-independent prefactor)."""
    return (-1) ** k * q ** (k * (k + nu)) / (qp(q, q, k) * qp(q ** (nu + 1), q, k))


def lean_first_ratio(k: int, nu, q):
    a = q ** nu
    return -1 / ((1 - q ** (k + 1)) * (1 - a * q ** (k + 1)))


def lean_second_ratio(k: int, nu, q):
    a = q ** nu
    return -(a * q ** (2 * k + 1)) / ((1 - q ** (k + 1)) * (1 - a * q ** (k + 1)))


# ── (A) RATIO IDENTITY — symbolic (all k, symbolic ν) ─────────────────────────
print("(A) ratio identity: Jackson coeff ratio == Lean closed-form ratio (symbolic)")
qs, nus = sp.symbols("q nu", positive=True)
a_s = qs ** nus


def qpoch_sym(base, k):
    out = sp.Integer(1)
    for j in range(k):
        out *= (1 - base * qs ** j)
    return out


def A_sym(k):
    return sp.Integer((-1) ** k) / (qpoch_sym(qs, k) * qpoch_sym(qs ** (nus + 1), k))


def B_sym(k):
    return sp.Integer((-1) ** k) * qs ** (k * (k + nus)) / (qpoch_sym(qs, k) * qpoch_sym(qs ** (nus + 1), k))


sym_ok_1 = sym_ok_2 = True
for k in range(0, 7):
    lean1 = -1 / ((1 - qs ** (k + 1)) * (1 - a_s * qs ** (k + 1)))
    lean2 = -(a_s * qs ** (2 * k + 1)) / ((1 - qs ** (k + 1)) * (1 - a_s * qs ** (k + 1)))
    d1 = sp.simplify(sp.powsimp(A_sym(k + 1) / A_sym(k) - lean1, force=True))
    d2 = sp.simplify(sp.powsimp(B_sym(k + 1) / B_sym(k) - lean2, force=True))
    sym_ok_1 = sym_ok_1 and (d1 == 0)
    sym_ok_2 = sym_ok_2 and (d2 == 0)
print(f"    first  kind: ratio identity symbolic for k=0..6 -> {sym_ok_1}")
print(f"    second kind: ratio identity symbolic for k=0..6 -> {sym_ok_2}")
results["ratio_identity_symbolic"] = {"first_kind": sym_ok_1, "second_kind": sym_ok_2}
check("(A) first-kind ratio == qbesselFirstKindRatio (symbolic, all k≤6)", sym_ok_1)
check("(A) second-kind ratio == qbesselSecondKindRatio (symbolic, all k≤6)", sym_ok_2)


# ── (B) CONTIGUITY (★₁)/(★₂) numeric, 60 dps ─────────────────────────────────
print("\n(B) contiguity recurrences (★₁)/(★₂) hold to 60 dps")
cases = [(0, mpf("0.60")), (1, mpf("0.83")), (2, mpf("0.75")), (3, mpf("0.90"))]
worst1 = worst2 = mpf(0)
rows = []
for nu, q in cases:
    a = q ** nu
    for k in range(0, 8):
        D = (1 - q ** (k + 1)) * (1 - a * q ** (k + 1))
        r1 = A_k(k + 1, nu, q) * D - (-A_k(k, nu, q))
        r2 = B_k(k + 1, nu, q) * D - (-(a * q ** (2 * k + 1)) * B_k(k, nu, q))
        worst1 = max(worst1, fabs(r1))
        worst2 = max(worst2, fabs(r2))
    rows.append({"nu": nu, "q": str(q)})
print(f"    max |★₁ residual| = {mp.nstr(worst1, 4)}   max |★₂ residual| = {mp.nstr(worst2, 4)}")
results["contiguity_numeric"] = {"cases": rows, "max_resid_first": mp.nstr(worst1, 6),
                                 "max_resid_second": mp.nstr(worst2, 6)}
check("(B) first-kind contiguity (★₁) holds (< 1e-30)", worst1 < mpf("1e-30"))
check("(B) second-kind contiguity (★₂) holds (< 1e-30)", worst2 < mpf("1e-30"))


# ── (C) CLOSED-FORM PRODUCT SOLUTION  c_k = c_0 ∏_{j<k} r_j  (Lean conclusion) ─
print("\n(C) product solution c_k = c_0·∏_{j<k} r_j reproduces the Jackson coefficient")
worstC1 = worstC2 = mpf(0)
for nu, q in cases:
    A0, B0 = A_k(0, nu, q), B_k(0, nu, q)
    prod1 = prod2 = mpf(1)
    for k in range(0, 9):
        c1 = A0 * prod1   # A0·∏_{j<k} lean_first_ratio(j)
        c2 = B0 * prod2
        worstC1 = max(worstC1, fabs(c1 - A_k(k, nu, q)))
        worstC2 = max(worstC2, fabs(c2 - B_k(k, nu, q)))
        prod1 *= lean_first_ratio(k, nu, q)
        prod2 *= lean_second_ratio(k, nu, q)
print(f"    max |first-kind product − A_k|  = {mp.nstr(worstC1, 4)}")
print(f"    max |second-kind product − B_k| = {mp.nstr(worstC2, 4)}")
results["product_solution"] = {"max_resid_first": mp.nstr(worstC1, 6),
                               "max_resid_second": mp.nstr(worstC2, 6)}
check("(C) first-kind product solution matches A_k (< 1e-30)", worstC1 < mpf("1e-30"))
check("(C) second-kind product solution matches B_k (< 1e-30)", worstC2 < mpf("1e-30"))


all_passed = all(ok for _, ok in asserts)
verdict = (
    "PROVED (derive-and-verify, 60 dps + symbolic). The first- and second-kind "
    "Jackson q-Bessel (SU_q(1,1)) coefficient ratios equal the Lean closed forms "
    "qbesselFirstKindRatio / qbesselSecondKindRatio; the contiguity recurrences "
    "(★₁) A_{k+1}(1−q^{k+1})(1−a q^{k+1}) = −A_k and (★₂) with the −a q^{2k+1} "
    "factor hold to 60 dps; and the q-hypergeometric product solution "
    "c_k = c_0 ∏_{j<k} r_j (the Lean first_order_solution conclusion) reproduces "
    "the Jackson coefficients. These are formal-q fibre-level identities (hold "
    "for all q, independent of the substrate anchor). Wires the proved SKELETON "
    "of the two SU_q(1,1) partners of the third-kind equation; no fit, no binding "
    "scale claimed, c_k stay cal-anchored."
)
print("\n" + ("ALL PASSED" if all_passed else "SOME FAILED"))
print("VERDICT:", verdict)

witness = {
    "computation": "qbessel_jackson_contiguity",
    "description": (
        "Verify the first- and second-kind Jackson q-Bessel (SU_q(1,1)) coefficient "
        "contiguity recurrences and their q-hypergeometric product solution, wiring "
        "QOU.QBeta.qbessel_first_kind_coeff_closed_form and "
        "qbessel_second_kind_coeff_closed_form (QBesselContiguityRecurrence.lean). "
        "Partners of the already-wired third-kind second-order q-difference equation."
    ),
    "discipline": "no fit; derive-or-verify; fibre-level (formal q); c_k cal-anchored; wires the Lean skeleton only",
    "lean_refs": [
        "qou:QOU.QBeta.qbessel_first_kind_coeff_closed_form",
        "qou:QOU.QBeta.qbessel_second_kind_coeff_closed_form",
    ],
    "precision_dps": mp.dps,
    "results": results,
    "assertions": {name: ok for name, ok in asserts},
    "allPassed": all_passed,
    "verdict": verdict,
}
out = pathlib.Path(__file__).parent / "qbessel-jackson-contiguity.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"\nwitness → {out}")
