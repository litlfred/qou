#!/usr/bin/env python3
"""GAP-A-3 deuteron mixed-plethystic content channel probe.

Tests the refined `P_λ_mixed(K) = m_{1/2}(λ)^{4N} · m_1(λ)^{2(Z-1)}`
candidate from
`docs/audits/2026-06-05-gap-a3-refined-mixed-plethystic-scope.md`
on the deuteron sub-case (Z=1, N=1).

For the deuteron, the m_1 exponent is 2·(Z-1) = 0, so the candidate
reduces to:

    P_λ_mixed(D) = m_{1/2}(λ)^4

where m_{1/2}(λ) is the SU(2) Schur-Weyl multiplicity of V_{1/2} in
V_{1/2}^⊗6 — equal to the Specht dimension f^λ for ≤2-row partitions
of 6, zero otherwise.

This is PR #1870's C1 channel RAISED TO THE 4TH POWER — a NEW
projection NOT in the 5 channels already refuted by PR #1870. The
4th-power exponent is read DIRECTLY off the Phase-4 carrier
`(q^{1/2}+q^{-1/2})^{4N}` exponent, not fitted.

Closure target (per audit §3): `A(D) · Σ_λ y_λ · χ^λ · P_λ_mixed(D)
= −B(D) / m_e ≈ −4.353`.

Per audit §4: 5% threshold. If lands within 5%, this is the FIRST
positive partition projection in 14 prior attempts. If refutes, the
refuted-class map gains a new row C13: "mixed plethystic deuteron
sub-case, m_{1/2}^4".

EXPLORATORY — emits `gap-a3-deuteron-mixed-plethystic-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import json
import math
from pathlib import Path

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic  # noqa: E402
from codata_constants import M_E_MEV as M_E_MEV_RAW  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

# Canonical anchors per the existing GAP-A-3 channels probe.
# CODATA constants imported from the central registry per Gemini
# review on PR #1899; M_E_MEV is re-cast to mp.mpf for precision.
Q_0_50DPS = "1.1099785827513808075916690956107688798744991218736"
VOL_HYP_D = mp.mpf("12.776")   # Phase-4 deuteron hyperbolic volume
M_E_MEV = mp.mpf(str(M_E_MEV_RAW))
B_D_MEV = mp.mpf("2.2245")
CHI_WITNESS = COMPUTE_DIR / "chi-deuteron-h6-at-q0-50dps.witness.json"


def hook_lengths(lam):
    hooks = []
    L = len(lam)
    for i in range(L):
        for j in range(lam[i]):
            arm = lam[i] - 1 - j
            leg = sum(1 for k in range(i + 1, L) if lam[k] > j)
            hooks.append(arm + leg + 1)
    return hooks


def specht_dim(lam):
    """f^λ = n! / Π hook lengths."""
    n = sum(lam)
    prod = 1
    for h in hook_lengths(lam):
        prod *= h
    return math.factorial(n) // prod


def m_half_su2(lam):
    """SU(2) Schur-Weyl multiplicity of V_{1/2} in V_{1/2}^⊗n.
    Equal to f^λ for ≤2-row partitions, 0 otherwise."""
    if len(lam) > 2:
        return 0
    return specht_dim(lam)


def main() -> int:
    builder = WitnessBuilder(
        "gap-a3-deuteron-mixed-plethystic-probe",
        engine="python+sympy+mpmath",
    )
    builder.set_description(
        "Refined GAP-A-3 deuteron sub-case: tests "
        "P_λ_mixed(D) = m_{1/2}(λ)^4 (PR #1870's C1 raised to 4th "
        "power via the Phase-4 (q^{1/2}+q^{-1/2})^{4N} exponent) against "
        "the closure target −B(D)/m_e. Per "
        "docs/audits/2026-06-05-gap-a3-refined-mixed-plethystic-scope.md."
    )
    builder.set_content_block("def:delta-lambda")

    print("=" * 78)
    print(" GAP-A-3 deuteron mixed plethystic probe — P_λ = m_{1/2}^4")
    print("=" * 78)
    print()

    q0 = mp.mpf(Q_0_50DPS)

    # Phase-4 amplitude A(D)
    def q_num(k, q):
        return (q ** k - q ** (-k)) / (q - q ** (-1))

    eight_q = q_num(8, q0)
    two_q = q_num(2, q0)   # for ([2]_q)^4 carrier
    A_D = VOL_HYP_D / eight_q * two_q ** 4   # Z=1 ⇒ [3]_q^0 = 1

    # BUG FIX (per Copilot review on PR #1899): the audit's closure
    # form is A(K)·Σ y_λ·χ^λ·P_λ(K) = −B(K)/m_e. The earlier code had
    # target = -B/(m_e·A_D) which factored A_D into the wrong side;
    # compared with closure_with_A = A_D·Σ, this introduced an extra
    # A_D factor. Correct: compare closure_with_A to -B/m_e DIRECTLY.
    target = -B_D_MEV / M_E_MEV
    print(f"  Vol_hyp(D) = {VOL_HYP_D}")
    print(f"  A(D) = Vol/[8]_q · ([2]_q)^4 = {mp.nstr(A_D, 12)}")
    print(f"  Target = −B(D)/m_e = {mp.nstr(target, 12)}")
    print(f"    (compared to A(D)·Σ y_λ·χ^λ·P_λ, NOT to Σ alone)")
    print()

    # Load χ^λ + compute y_λ
    with CHI_WITNESS.open() as fh:
        chi_data = json.load(fh)
    chi_by_part = {tuple(e["partition"]): mp.mpf(e["chi_lambda"])
                   for e in chi_data["by_partition"]}

    q_sym = sp.Symbol("q", positive=True)
    q0_sp = sp.Float(Q_0_50DPS, 50)
    y_by_part = {}
    for p in chi_by_part.keys():
        y_sym = y_lambda_wenzl_bridge_symbolic(p)
        y_val = mp.mpf(str(sp.N(y_sym.subs(q_sym, q0_sp), 50)))
        y_by_part[p] = y_val

    # Compute m_{1/2}(λ)^4 per partition + closure sum
    print(f"  Partition projection P_λ_mixed = m_{{1/2}}(λ)^4:")
    print(f"  {'partition':<14} {'m_{1/2}':>8} {'m_{1/2}^4':>10} "
          f"{'y_λ·χ^λ·P_λ':>16}")
    print(f"  {'-'*14} {'-'*8} {'-'*10} {'-'*16}")
    closure = mp.mpf(0)
    per_lambda = []
    for p in chi_by_part.keys():
        m_half = m_half_su2(p)
        p_lam = m_half ** 4
        term = y_by_part[p] * chi_by_part[p] * p_lam
        closure += term
        per_lambda.append({
            "partition": list(p),
            "m_half_su2": m_half,
            "P_lambda_mixed": p_lam,
            "term": str(term),
        })
        print(f"  {str(p):<14} {m_half:>8} {p_lam:>10} "
              f"{mp.nstr(term, 10):>16}")
    print()

    closure_with_A = A_D * closure
    rel_err = mp.fabs(closure_with_A - target) / mp.fabs(target)

    print(f"  Σ y_λ · χ^λ · P_λ_mixed = {mp.nstr(closure, 12)}")
    print(f"  A(D) · Σ                = {mp.nstr(closure_with_A, 12)}")
    print(f"  Target = −B/m_e         = {mp.nstr(target, 12)}")
    # Format rel.err via mp.nstr to preserve precision per Copilot review
    print(f"  Rel. error              = {mp.nstr(rel_err, 6)} "
          f"({mp.nstr(rel_err * 100, 6)} %)")
    print()

    THRESHOLD = mp.mpf("0.05")
    passed = rel_err < THRESHOLD

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print()
    if passed:
        print(f"  ✓ PASSES — mixed plethystic m_{{1/2}}^4 lands within 5% on "
              f"deuteron.")
        print(f"    This is the FIRST positive partition projection in 14")
        print(f"    prior refutations. The mixed-channel framing from the")
        print(f"    refined GAP-A-3 scope (PR #1896) is supported on the")
        print(f"    deuteron sub-case. The genuine mixed case (⁴He, Z≥2)")
        print(f"    requires new Hecke compute at n=12 (owner-gated).")
    else:
        print(f"  ✗ REFUTED — mixed plethystic m_{{1/2}}^4 rel.err "
              f"{mp.nstr(rel_err * 100, 6)}% > 5% on deuteron.")
        print(f"    Adds row C13 to the refuted-class map: \"mixed")
        print(f"    plethystic deuteron sub-case, m_{{1/2}}^4 from Phase-4")
        print(f"    carrier exponent (4N)\".")
        print()
        print(f"    The refined GAP-A-3 framing's deuteron sub-case is now")
        print(f"    closed. The genuine mixed case (⁴He, Z≥2) remains")
        print(f"    untested — different per-partition distribution.")
        print(f"    Combined with 14 prior refutations, this confirms the")
        print(f"    structural pivot to GAP-A-4 (per-atom λ(K)) is the")
        print(f"    correct direction; partition-layer projection on the")
        print(f"    deuteron sub-case is exhausted.")
    print()

    builder.add_data("A_D", str(A_D))
    builder.add_data("target", str(target))
    builder.add_data("closure_with_A", str(closure_with_A))
    builder.add_data("rel_err", str(rel_err))
    builder.add_data("per_lambda", per_lambda)
    builder.add_data("verdict", "PASSED" if passed else "REFUTED")

    # Per Copilot review on PR #1899: avoid tautological assertion
    # (expected = computed always passes). The probe expects the mixed
    # plethystic candidate to be REFUTED on the deuteron (per refined
    # GAP-A-3 scope §3 / refuted-class precedent C1-C5 from PR #1870);
    # a positive result would be the first in 14 prior attempts and is
    # explicitly the surprise outcome. Encode this expectation:
    # expected=0 (refutation expected), computed=0 if refuted, 1 if passed.
    # Assertion passes when computed=expected; if it FAILS (passed=True
    # i.e. computed=1 ≠ expected=0), that's the genuine surprise.
    builder.add_assertion(
        "mixed_plethystic_m_half_fourth_power_refuted_as_expected",
        computed=0 if not passed else 1,
        expected=0,
        tolerance=0,
        source=("Refined GAP-A-3 deuteron sub-case: tests the "
                "P_λ_mixed(D) = m_{1/2}(λ)^4 channel (Phase-4 4N "
                "exponent applied to PR #1870's C1 projection). 5% "
                "threshold. Expected outcome: REFUTED (per the 14 "
                "prior partition-layer projection failures + the "
                "structural amplification by the 4th power). The "
                "assertion encodes this: pass = refuted as predicted, "
                "FAIL = a positive result (genuine surprise; the FIRST "
                "positive partition-layer projection). Witness data "
                "carries the precise rel.err for diagnostic depth."),
    )

    builder.save()
    print(f"  Witness: gap-a3-deuteron-mixed-plethystic-probe.witness.json")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
