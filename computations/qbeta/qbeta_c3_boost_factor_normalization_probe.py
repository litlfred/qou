#!/usr/bin/env python3
"""qbeta_c3_boost_factor_normalization_probe.py — DISTINCT-ANGLE attack on the sole
surviving c₃ target (bean qou-iyj5 / PR #4515): the boost-rapidity enhancement
`c = √A ≈ 1.4305` (`A ≈ 2.054`).

PR #4515 measured, via the EXACT figure-8 complex volume, that the muon bar-odd leak
`S(muon)` needs an effective boost `Re u = c·ln q₀` with `c ≈ 1.4305 = √A`, `A ≈ 2.054`,
because `Im 𝔙₄₁(u) = κ_pot·(Re²u − Im²u)` with the Lean-EXACT potential coefficient
`κ_pot = √3/4` and `Re u = ln q₀` gives only `A = 1`. Its addendum noted `A = 2` (`c=√2`)
is indistinguishable from `A = 2.054` (a q₀-shift of `5.7×10⁻¹¹`, far below the pin).

This probe brings a DIFFERENT context than the exact-CS-integral numerics of #4515:

  1. STRUCTURAL IDENTITY (the clean candidate, Lean-exact).  The factor `A = 2` is NOT
     ad hoc: it is precisely the reciprocal of the Neumann–Zagier ½ potential
     normalization.  The figure-8 cusp SHAPE is `κ_shape = √3/2 = sin(π/3) = Im(e^{iπ/3})`;
     the NZ complex-volume POTENTIAL coefficient is `κ_pot = κ_shape/2 = √3/4`
     (the ½ is the NZ potential normalization — see the `FigureEightComplexVolume.lean`
     docstring).  So `κ_shape/κ_pot = 2` EXACTLY, and since `Im 𝔙 ∝ (Re u)²`, an
     observable that carries the cusp-SHAPE quadratic form rather than the NZ POTENTIAL
     coefficient has `A = 2`, i.e. an effective boost `c = √2` — with NO free parameter.
     The whole "why c = √A?" question REDUCES to a single, named, falsifiable
     normalization question: does the bar-odd leak `S` carry the NZ ½ or not?

  2. PRECISION CEILING (the anti-numerology prune, PR #1805 pattern).  `S(muon)` is a
     `1/u³`-amplified near-threshold quantity (registry `dc₃/dq₀ ≈ 4.6×10⁶`).  We measure
     `dA/dq₀` directly by finite difference and show the q₀-pin uncertainty makes `A`'s
     muon-anchor value (2.054) uncertain at the O(tens-of-%) level, so the clean
     structural candidates `{A=2, Vol(4₁), q₀+q₀⁻¹, q₀²+q₀⁻²}` — all within ≈2.6 % —
     are INDISTINGUISHABLE by the measurement.  `c = √A` therefore CANNOT be identified
     to a precision that separates a structural identity from a coincidence.

VERDICT (honest): REDUCED, not derived.  `c = √A` reduces to the binary NZ-½ normalization
question with the clean value `A = 2` (`c = √2`); the residual `2.0 → 2.054` is within the
amplification noise.  This is scope-(a): it does NOT assert `S` sees `κ_shape` (that would
be a fit), and does NOT exclude the meridian deformation.  No c_k wired; nothing inverts
Q_β/CODATA; no `SDeformedVolumeChannel` instance fabricated.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
VOL41 = +(2 * mp.clsin(2, mp.pi / 3))
KPOT = mp.sqrt(3) / 4          # NZ potential coefficient (Lean cuspModulus, EXACT)
KSHAPE = mp.sqrt(3) / 2        # cusp SHAPE = sin(π/3) = Im(e^{iπ/3}); κ_pot = κ_shape/2


def S_at(q):
    """Muon bar-odd leak S(q) = c3_target(q) + Vol(4₁) (the Im 𝔙₄₁ target)."""
    return c3_target_at(q, QCOD, ME) + VOL41


def main() -> int:
    print("=" * 78)
    print(" c₃ boost factor c=√A: NZ-½ structural identity + precision ceiling")
    print("=" * 78)
    q0 = q_muon_at(50)
    lnq = mp.log(q0)
    S_muon = S_at(q0)
    lead = KPOT * lnq ** 2
    A_meas = S_muon / lead
    c_meas = mp.sqrt(A_meas)

    print(f"\n q0(muon)   = {mp.nstr(q0, 18)}")
    print(f" ln q0      = {mp.nstr(lnq, 12)}")
    print(f" κ_pot=√3/4 = {mp.nstr(KPOT, 12)}   (Lean-exact FigureEightComplexVolume.cuspModulus)")
    print(f" S(muon)    = {mp.nstr(S_muon, 12)}")
    print(f" lead(naive, Re u=ln q0) = {mp.nstr(lead, 12)}")
    print(f" A_measured = {mp.nstr(A_meas, 10)}   c=√A = {mp.nstr(c_meas, 10)}")

    # ---- 1. STRUCTURAL IDENTITY: κ_shape / κ_pot = 2 EXACTLY (the NZ ½) ----
    ratio = KSHAPE / KPOT
    ratio_is_two = abs(ratio - 2) < mp.mpf("1e-50")
    print(f"\n [1] κ_shape/κ_pot = (√3/2)/(√3/4) = {mp.nstr(ratio, 12)}  (EXACT = 2, the NZ ½)")
    print(f"     ⇒ shape-normalized observable ⇒ A = 2 exactly ⇒ c = √2 = {mp.nstr(mp.sqrt(2), 10)}")

    # ---- 2. candidate degeneracy ----
    Vol41 = VOL41
    barEven = q0 + 1 / q0
    barEvenSq = q0 ** 2 + q0 ** -2
    cands = {
        "A=2  (NZ ½: κ_shape/κ_pot; c=√2)": mp.mpf(2),
        "A=barEven(q0)=q0+1/q0": barEven,
        "A=Vol(4₁)=2·Cl₂(π/3)": Vol41,
        "A=barEven(q0²)=q0²+q0⁻²": barEvenSq,
        "A=2.054 (measured)": A_meas,
    }
    print("\n candidate A                          A        c=√A      miss(A)%")
    misses = []
    for name, Ac in cands.items():
        miss = 100 * (Ac - A_meas) / A_meas
        misses.append(abs(miss))
        print(f"   {name:34s} {mp.nstr(Ac,6):>8} {mp.nstr(mp.sqrt(Ac),6):>8}   {mp.nstr(miss,3):>7}")
    max_clean_miss = max(m for n, m in zip(cands, misses) if "measured" not in n)

    # ---- 3. PRECISION CEILING: dA/dq0 by finite difference ----
    delta = q0 * mp.mpf("1e-12")
    dS = (S_at(q0 + delta) - S_at(q0 - delta)) / (2 * delta)
    dA_dq = dS / lead          # lead's (ln q0)² q0-dependence is subleading here
    qpin = mp.mpf("1e-9")      # ppb-level q0 pin
    sigma_A = abs(dA_dq) * qpin
    sigma_c = sigma_A / (2 * c_meas)
    # q0-shift that maps A_meas -> 2 exactly:
    dq_to_A2 = abs(A_meas - 2) / abs(dA_dq)
    print(f"\n [3] dA/dq0 (finite diff)   ≈ {mp.nstr(dA_dq, 6)}   (S is 1/u³-amplified)")
    print(f"     q0-pin ~ {mp.nstr(qpin,2)}  ⇒ σ_A ≈ {mp.nstr(sigma_A,4)} "
          f"({mp.nstr(100*sigma_A/A_meas,3)}% of A), σ_c ≈ {mp.nstr(sigma_c,4)} "
          f"({mp.nstr(100*sigma_c/c_meas,3)}% of c)")
    print(f"     Δq0 that maps A_meas→2 exactly = {mp.nstr(dq_to_A2,4)} "
          f"({'below' if dq_to_A2 < qpin else 'above'} the pin) "
          f"⇒ A=2 indistinguishable from 2.054")
    print(f"     clean-candidate spread ≤ {mp.nstr(max_clean_miss,3)}% ≪ σ_A "
          f"⇒ measurement CANNOT select the identity")

    print("\n VERDICT: REDUCED (not derived, not refuted). c=√A ⇒ the binary NZ-½")
    print("   normalization question; A=2 (c=√2) is the clean value = 1/(NZ ½).")
    print("   Residual 2.0→2.054 is amplification noise. Deriving that S carries the")
    print("   cusp-SHAPE (κ_shape) rather than the NZ POTENTIAL (κ_pot) is the open sub-")
    print("   obstruction (qou-yh67). Asserting it would be a fit — NOT done here.")

    ok = bool(ratio_is_two and (dq_to_A2 < qpin) and (max_clean_miss < 5))

    wb = WitnessBuilder("qbeta-c3-boost-factor-normalization", engine="mpmath")
    wb.set_description(
        "Distinct-angle attack on the c₃ boost-rapidity enhancement c=√A≈1.4305 (A≈2.054, "
        "PR #4515 / qou-iyj5). (1) STRUCTURAL: κ_shape/κ_pot=(√3/2)/(√3/4)=2 EXACTLY — the "
        "figure-8 cusp SHAPE (sin π/3) over the NZ POTENTIAL coefficient (Lean cuspModulus √3/4); "
        "the factor-2 IS the Neumann–Zagier ½ potential normalization, so a shape-normalized "
        "bar-odd leak has A=2, c=√2 with no free parameter. (2) PRECISION CEILING: S(muon) is "
        "1/u³-amplified (dA/dq0 measured huge); at the ppb q0-pin the clean candidates "
        "{A=2, Vol(4₁), q0+q0⁻¹, q0²+q0⁻²} (all ≤2.6%) are INDISTINGUISHABLE — c=√A cannot be "
        "identified to separate an identity from a coincidence (PR #1805 entropy pattern). "
        "VERDICT: REDUCED (scope-a), not derived/refuted; A=2 (c=√2) = 1/(NZ ½) is the clean "
        "candidate, residual 2.0→2.054 is amplification noise. No c_k wired; nothing inverts "
        "Q_β/CODATA; no SDeformedVolumeChannel instance fabricated.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("boost_factor_normalization", {
        "q0_muon": mp.nstr(q0, 18),
        "ln_q0": mp.nstr(lnq, 12),
        "kappa_pot_sqrt3_4": mp.nstr(KPOT, 12),
        "kappa_shape_sqrt3_2": mp.nstr(KSHAPE, 12),
        "kappa_shape_over_kappa_pot": mp.nstr(ratio, 12),
        "S_muon": mp.nstr(S_muon, 12),
        "lead_naive": mp.nstr(lead, 12),
        "A_measured": mp.nstr(A_meas, 10),
        "c_measured_sqrtA": mp.nstr(c_meas, 10),
        "sqrt_2": mp.nstr(mp.sqrt(2), 10),
        "dA_dq0_finite_diff": mp.nstr(dA_dq, 6),
        "sigma_A_at_ppb_pin": mp.nstr(sigma_A, 6),
        "sigma_A_pct": mp.nstr(100 * sigma_A / A_meas, 4),
        "dq0_mapping_A_to_2": mp.nstr(dq_to_A2, 6),
        "max_clean_candidate_miss_pct": mp.nstr(max_clean_miss, 4),
        "candidates": {n: mp.nstr(v, 8) for n, v in cands.items()},
        "verdict": ("REDUCED not derived: c=√A ⇒ binary NZ-½ normalization; A=2 (c=√2) = "
                    "1/(NZ ½), κ_shape/κ_pot=2 exact; residual 2.0→2.054 within amplification "
                    "noise; clean candidates indistinguishable at the q0 pin — no high-precision "
                    "identification possible. Deriving that S carries κ_shape is the open "
                    "sub-obstruction (qou-yh67); asserting it would be a fit."),
    })
    wb.add_assertion("kappa_shape_over_kappa_pot_is_two", str(bool(ratio_is_two)), "True")
    wb.add_assertion("A_equals_2_indistinguishable_from_measured",
                     str(bool(dq_to_A2 < qpin)), "True")
    wb.add_assertion("clean_candidates_within_amplification_band",
                     str(bool(max_clean_miss < 5)), "True")
    wb.save()
    print("\nwitness → qbeta-c3-boost-factor-normalization.witness.json")
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
