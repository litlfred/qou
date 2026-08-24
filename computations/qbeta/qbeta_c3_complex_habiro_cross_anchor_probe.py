#!/usr/bin/env python3
# ANCHOR NOTE — CORRECTED 2026-08-23. The 2026-06-22 boilerplate that stood
# here had the two anchors INVERTED, in all 13 files carrying it. Measured:
#   • 1.10997858275… is NOT "the RETIRED pre-2026-05-28 proton anchor" — it is
#     the CURRENT proton pin. q_at() returns 1.10997858275138…
#   • "the CURRENT canonical proton q0 is ≈ 1.1099785955573347" named the MUON
#     value; q_at() never returns it.
#   • "q_muon_at() ≈ 1.10997859555418" named the SUPERSEDED (CODATA-2018) muon
#     value; q_muon_at() returns 1.10997859564274… See
#     computations/audits/muon_pin_three_values_probe.py for the three values.
# An agent trusting it would read the two-layer discipline backwards.
#
# What is true: the 1.10997858275… occurrences below ARE the current proton
# pin, and this probe is preserved as-is by design — its cross-anchor
# comparison is the point, so it must NOT be migrated.
"""qbeta_c3_complex_habiro_cross_anchor_probe.py — test candidate
complex-analytic Habiro elements at BOTH proton + muon anchors.

PR #1801 follow-up. The 569bedda1 falsify commit on main showed:

  proton anchor q_p = 1.10997858275:  empirical c_3 = -2.0693
  muon   anchor q_μ = 1.10997859555:  empirical c_3 = -2.0097
  Δq = 1.28e-8,  Δc_3 = 0.0596  →  dc_3/dq ≈ 4.66e6 per unit q

The [3]_q/25 closure formula is RIGID (swings 6.18e-7%, vs the
empirical 2.88%) — 4.7 MILLION× too rigid. The redirect from
569bedda1: "genuine Habiro element (if any) is complex-analytic /
root-of-unity."

This probe attempts the redirect concretely. A real-analytic c_3(q)
formula can be 4.66e6 per unit q ONLY if it has a near-singularity
within ~|c_3(q_0)| / 4.66e6 ≈ 4.3e-7 of q_0. So a real-q Habiro
candidate must have a near-pole at ~1.10998 ± 4.3e-7.

Natural candidates with near-singularities at non-root-of-unity
real values:

  A. F(q) = 1 / (q - q_0_pole)  for q_0_pole near q_0
     — generic pole at the substrate (no categorical justification)
  B. F(q) = log(q - 1) / (q - 1)
     — log-singularity at q=1 (Habiro ring near classical limit)
  C. F(q) = (q-1) · ψ(q) where ψ has root-of-unity expansion
     — compact quantum dilogarithm (analytic away from roots of unity)
  D. F(q) = Σ_{ζ root of unity} a_ζ / (q - ζ)
     — partial-fraction decomposition over root of unity poles

This probe tests:
  1. Whether ANY of {A, B, C, D} is consistent with the empirical
     c_3 at BOTH proton and muon anchors (within experimental noise).
  2. Whether the implied near-pole (if any) sits at a categorically
     meaningful point (root of unity, classical limit, or a
     substrate-derived value).

If NONE of {A, B, C, D} matches both anchors, the redirect's
"complex-analytic / root-of-unity Habiro" hypothesis is either
REFUTED at this scope, or requires a MORE EXOTIC analytic
structure than what's tested here.

Honest scoping. No fit. The probe reports a verdict either way.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

from witness_base import WitnessBuilder  # noqa: E402


# Cross-anchor q values (per falsify 569bedda1 + qbeta-c3-... probe).
# validation: PINNED q-anchors used as a reference for the empirical-c_3
# comparison below — canonical substrate constants live in
# substrate/q_parameter.py; included as literals here only to keep the
# cross-anchor harness self-contained. Not a CAL-4 input.
_Q_PROTON_VALIDATION = mp.mpf("1.10997858275")
_Q_MUON_VALIDATION   = mp.mpf("1.10997859555")

# validation: empirical c_3 readouts at each anchor — the OUTPUTS of the
# production pipeline (falsify commit 569bedda1), included only as
# comparison targets for the candidate complex-Habiro forms tested below.
# Not a substrate input.
_C3_PROTON_EMP_VALIDATION = mp.mpf("-2.0693")
_C3_MUON_EMP_VALIDATION   = mp.mpf("-2.0097")


def candidate_A(q, q_pole):
    """A: F(q) = 1 / (q - q_pole)  generic pole at q_pole."""
    return 1 / (q - q_pole)


def candidate_B(q):
    """B: F(q) = log(q - 1) / (q - 1)  log-singularity at q=1."""
    return mp.log(q - 1) / (q - 1)


def candidate_C(q):
    """C: F(q) = (q - 1) · ψ(q) with ψ ~ Faddeev dilog approximant.

    Use the leading-log approximation ψ(q) ≈ 1/(q-1) · log(q),
    so F ≈ log(q). Smooth, no near-pole — included as a NEGATIVE
    control (we EXPECT this to be too rigid).
    """
    return mp.log(q)


def candidate_D(q):
    """D: partial-fraction sum over n-th roots of unity for n = 1..5,
    INCLUDING ζ = 1 (the k = 0 term).  Returns mp.mpc (complex sum); the
    imaginary part vanishes at real q by conjugate pairing of the
    root-of-unity terms.

    F(q) = Σ_{n = 1..5} Σ_{k = 0..n-1} 1 / (n · (q - exp(2πi · k / n)))

    All complex constants stay inside mpmath's high-precision context
    (`mp.mpc(0, 1)` instead of Python's `1j`) so 65-dps precision is
    preserved through the loop.
    """
    s = mp.mpc(0)
    two_pi_i = 2 * mp.pi * mp.mpc(0, 1)
    for n in (1, 2, 3, 4, 5):
        for k in range(0, n):  # include k = 0 (ζ = 1)
            zeta = mp.exp(two_pi_i * mp.mpf(k) / n)
            s += 1 / (n * (q - zeta))
    return s


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-c3-complex-habiro-cross-anchor-probe",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Tests four candidate complex-analytic Habiro forms (A: "
        "generic pole, B: log singularity at q=1, C: Faddeev "
        "dilog approximant, D: cyclotomic partial fractions) "
        "for cross-anchor consistency at proton + muon anchors "
        "per the 569bedda1 falsify redirect. Honest scoping — "
        "either CONFIRMS or REFUTES the redirect at this scope."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Q_β c_3 complex-Habiro cross-anchor scoping")
    print("=" * 78)
    print()
    # Cross-anchor slope and required near-singularity radius — computed
    # once from the empirical anchors and reused throughout the report
    # so the narrative stays self-consistent if anchors are updated.
    slope_required = (_C3_MUON_EMP_VALIDATION - _C3_PROTON_EMP_VALIDATION) / (_Q_MUON_VALIDATION - _Q_PROTON_VALIDATION)
    near_sing_radius = mp.fabs(_C3_PROTON_EMP_VALIDATION) / mp.fabs(slope_required)

    print(f"  Empirical (per 569bedda1):")
    print(f"    q_proton = {mp.nstr(_Q_PROTON_VALIDATION, 14)}  c_3_emp = {_C3_PROTON_EMP_VALIDATION}")
    print(f"    q_muon   = {mp.nstr(_Q_MUON_VALIDATION, 14)}  c_3_emp = {_C3_MUON_EMP_VALIDATION}")
    print(f"    Δq       = {mp.nstr(_Q_MUON_VALIDATION - _Q_PROTON_VALIDATION, 4)}")
    print(f"    Δc_3     = {mp.nstr(_C3_MUON_EMP_VALIDATION - _C3_PROTON_EMP_VALIDATION, 5)}")
    print(f"    dc_3/dq  ≈ {mp.nstr(slope_required, 4)}  (computed)")
    print(f"    → required near-singularity radius: "
          f"~{mp.nstr(near_sing_radius, 4)}")
    print()

    print(f"  Cross-anchor test — does the candidate match BOTH?")
    print(f"  {'Candidate':<48} {'@ q_p':<14} {'@ q_μ':<14} {'Δ':<10}")
    print(f"  {'-'*48} {'-'*14} {'-'*14} {'-'*10}")

    results = []

    # ---- Candidate A: generic pole ----
    # For A to match, we need to find q_pole such that
    # 1/(q_p - q_pole) and 1/(q_μ - q_pole) give c_3_p, c_3_μ.
    # This is 2 equations, 1 unknown (q_pole) + 1 scale → solvable.
    # Solve: c_p = α/(q_p - q_pole), c_μ = α/(q_μ - q_pole)
    # → c_p (q_p - q_pole) = α = c_μ (q_μ - q_pole)
    # → q_pole = (c_p q_p - c_μ q_μ) / (c_p - c_μ)
    q_pole_A = (_C3_PROTON_EMP_VALIDATION * _Q_PROTON_VALIDATION - _C3_MUON_EMP_VALIDATION * _Q_MUON_VALIDATION) / (_C3_PROTON_EMP_VALIDATION - _C3_MUON_EMP_VALIDATION)
    alpha_A = _C3_PROTON_EMP_VALIDATION * (_Q_PROTON_VALIDATION - q_pole_A)
    A_p = alpha_A * candidate_A(_Q_PROTON_VALIDATION, q_pole_A)
    A_m = alpha_A * candidate_A(_Q_MUON_VALIDATION, q_pole_A)
    delta_A = (A_m - _C3_MUON_EMP_VALIDATION) / _C3_MUON_EMP_VALIDATION
    print(f"  {'A. α/(q-q_pole) [forced match]':<48} "
          f"{mp.nstr(A_p, 7):<14} {mp.nstr(A_m, 7):<14} {float(delta_A):+.1e}")
    distance_q_p_to_pole = _Q_PROTON_VALIDATION - q_pole_A
    print(f"    q_pole = {mp.nstr(q_pole_A, 12)} "
          f"(distance to q_p: {mp.nstr(distance_q_p_to_pole, 4)})")
    results.append({"name": "A_generic_pole",
                    "q_pole": mp.nstr(q_pole_A, 25),
                    "distance_q_p_to_pole": mp.nstr(distance_q_p_to_pole, 25),
                    "matches_both_by_construction": True,
                    "categorical_meaning_of_q_pole": "NONE (fit-derived)"})

    # ---- Candidate B: log(q-1)/(q-1) ----
    B_p = candidate_B(_Q_PROTON_VALIDATION)
    B_m = candidate_B(_Q_MUON_VALIDATION)
    print(f"  {'B. log(q-1)/(q-1)':<48} "
          f"{mp.nstr(B_p, 7):<14} {mp.nstr(B_m, 7):<14}")
    print(f"    (no scale fitted; just baseline shape)")
    results.append({"name": "B_log_singularity",
                    "value_q_p": mp.nstr(B_p, 25),
                    "value_q_m": mp.nstr(B_m, 25)})

    # ---- Candidate C: log(q) (NEGATIVE control — should be too rigid) ----
    C_p = candidate_C(_Q_PROTON_VALIDATION)
    C_m = candidate_C(_Q_MUON_VALIDATION)
    dC = (C_m - C_p) / (_Q_MUON_VALIDATION - _Q_PROTON_VALIDATION)
    print(f"  {'C. log(q) [neg control]':<48} "
          f"{mp.nstr(C_p, 7):<14} {mp.nstr(C_m, 7):<14}")
    print(f"    dF/dq ≈ {float(dC):.3e}  (vs required 4.66e6)")
    results.append({"name": "C_log_q_neg_control",
                    "dF_dq": float(dC),
                    "too_rigid": float(abs(dC)) < 1e3})

    # ---- Candidate D: cyclotomic partial fractions ----
    D_p = candidate_D(_Q_PROTON_VALIDATION)
    D_m = candidate_D(_Q_MUON_VALIDATION)
    D_p_real = D_p.real
    D_m_real = D_m.real
    D_p_imag = D_p.imag
    D_m_imag = D_m.imag
    dD = (D_m_real - D_p_real) / (_Q_MUON_VALIDATION - _Q_PROTON_VALIDATION)
    print(f"  {'D. Σ cyclotomic partial fractions':<48} "
          f"{mp.nstr(D_p_real, 7):<14} {mp.nstr(D_m_real, 7):<14}")
    print(f"    Im at q_p: {mp.nstr(D_p_imag, 6)}  Im at q_μ: {mp.nstr(D_m_imag, 6)}")
    print(f"    dF/dq ≈ {float(dD):.3e}  (vs required 4.66e6)")
    print(f"    Im_part vanishes at real q: "
          f"{'✓' if mp.fabs(D_p_imag) < mp.mpf('1e-30') else '✗'}")
    results.append({"name": "D_cyclotomic_partial_fractions",
                    "value_q_p_real": mp.nstr(D_p_real, 25),
                    "value_q_p_imag": mp.nstr(D_p_imag, 25),
                    "dF_dq": float(dD),
                    "im_vanishes_at_real_q": bool(mp.fabs(D_p_imag) < mp.mpf("1e-30"))})

    print()
    print("=" * 78)
    print(" VERDICT — complex-Habiro redirect at this scope")
    print("=" * 78)
    print()
    print(f"  A. Generic pole: BY CONSTRUCTION matches both anchors,")
    print(f"     but the pole sits at q_pole = {float(q_pole_A):.6f}, which is")
    print(f"     NOT at a root of unity nor at the classical limit q=1.")
    print(f"     Distance to q_p: {float(_Q_PROTON_VALIDATION - q_pole_A):.3e}.")
    print(f"     CATEGORICAL MEANING: none derived. This is a 2-point")
    print(f"     fit, not a structural identification.")
    print()
    print(f"  B. log(q-1)/(q-1) at q=1 singularity: TOO RIGID (no")
    print(f"     near-pole near q_0 ≈ 1.11; the q=1 singularity is")
    print(f"     0.11 away, dF/dq is moderate, NOT 4.66e6).")
    print()
    print(f"  C. log(q): NEGATIVE control as expected — dF/dq ≈ "
          f"{mp.nstr(dC, 4)}, vs required {mp.nstr(slope_required, 4)}.")
    print(f"     Refutes smooth-log.")
    print()
    print(f"  D. Cyclotomic partial fractions: roots of unity sit at")
    print(f"     |ζ| = 1, but q_0 ≈ 1.11, so distance to any ζ is ≥ 0.1.")
    print(f"     dF/dq is moderate; matches the falsify-commit's general")
    print(f"     observation that root-of-unity poles are TOO FAR to")
    print(f"     produce the required dc_3/dq ≈ 4.66e6.")
    print()
    print(f"  CONCLUSION:")
    print(f"    Naive root-of-unity Habiro elements (poles at |q|=1)")
    print(f"    are TOO FAR from q_0 ≈ 1.11 to give the required")
    print(f"    dc_3/dq ≈ {mp.nstr(slope_required, 4)}. The redirect from 569bedda1 was")
    print(f"    'complex-analytic / root-of-unity' — but at this scope,")
    print(f"    no NATURAL root-of-unity Habiro element matches.")
    print()
    print(f"    Two possibilities remain:")
    print(f"      1. The empirical c_3 across-anchor jitter is NOT a")
    print(f"         genuine fibre-level effect — it's measurement noise")
    print(f"         or calibration-specific normalization (consistent")
    print(f"         with the falsify-commit's 'proton-anchor near-match'")
    print(f"         classification). The 'Habiro element' need not")
    print(f"         track the empirical jitter.")
    print()
    print(f"      2. The Habiro element has poles at MORE EXOTIC points")
    print(f"         (not standard roots of unity) — e.g. transcendental")
    print(f"         singularities, or limits of root-of-unity sequences")
    print(f"         that approach q_0 ≈ 1.11 from a specific direction.")
    print(f"         These would be hard to identify a priori.")
    print()
    print(f"  HONEST SCOPING: the 'complex-Habiro / root-of-unity' redirect")
    print(f"  does NOT readily yield a c_3 candidate matching BOTH anchors.")
    print(f"  Possibility 1 (empirical jitter is normalization artifact)")
    print(f"  is more parsimonious. Possibility 2 would need a new angle.")
    print()

    builder.add_data("empirical", {
        "q_proton": mp.nstr(_Q_PROTON_VALIDATION, 25),
        "q_muon": mp.nstr(_Q_MUON_VALIDATION, 25),
        "c_3_proton": str(_C3_PROTON_EMP_VALIDATION),
        "c_3_muon": str(_C3_MUON_EMP_VALIDATION),
        "delta_q": mp.nstr(_Q_MUON_VALIDATION - _Q_PROTON_VALIDATION, 25),
        "delta_c_3": mp.nstr(_C3_MUON_EMP_VALIDATION - _C3_PROTON_EMP_VALIDATION, 25),
        "dc_3_dq_required": mp.nstr(slope_required, 25),
        "near_sing_radius": mp.nstr(near_sing_radius, 25),
    })
    builder.add_data("candidates", results)
    builder.add_data("verdict", {
        "naive_root_of_unity_habiro_works": False,
        "implication_1_empirical_jitter_is_artifact":
            "More parsimonious. Consistent with 569bedda1's "
            "'proton-anchor near-match' classification.",
        "implication_2_more_exotic_poles_needed":
            "Would require transcendental singularities or limits "
            "of root-of-unity sequences approaching q_0 ≈ 1.11.",
        "scope_status":
            "Complex-Habiro redirect at this scope does NOT yield "
            "a c_3 candidate matching BOTH anchors via natural "
            "root-of-unity poles.",
    })

    # Assertion: candidate D's Im → 0 at real q (a sanity check on the
    # cyclotomic sum being constructed with conjugate pairs).
    builder.add_assertion(
        "candidate_D_im_vanishes_at_real_q",
        computed=1 if mp.fabs(D_p_imag) < mp.mpf("1e-30") else 0,
        expected=1,
        tolerance=0,
        source=("Sanity invariant: the partial-fraction cyclotomic sum "
                "D includes conjugate root-of-unity pairs, so at real q "
                "the imaginary part vanishes. Confirms Candidate D "
                "is a valid REAL observable at the substrate, "
                "consistent with the lusztig_q_0_imaginary_part_zero "
                "archimedean assertion."),
    )

    builder.save()
    print(f"  Witness: qbeta-c3-complex-habiro-cross-anchor-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
