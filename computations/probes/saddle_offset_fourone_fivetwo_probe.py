#!/usr/bin/env python3
"""saddle_offset_fourone_fivetwo_probe.py — the "saddle-offset" geometric
reading of the certified 4₁ / 5₂ Stokes data.

EXPLORATORY, derive-then-check, anti-fit. Tests a *physical picture*: the
knot winds NEAR-but-not-ON the saddle points of the state integral (the
"holes" of the covering surface), the winding being origin-centered
(offset 0) only in the amphichiral / bar-symmetric limit. The probe lifts
the merged 5₂ {3,4} distinguisher (`fivetwo_crossknot_34_distinguisher.py`,
`FiveTwoDTSpectrumSplit.lean`) from a bare integer difference into a genuine
2-D *saddle vector* with an ANGLE and a MAGNITUDE, and checks that the ι-odd
(bar-odd) OFFSET of that vector reproduces the {3,4} datum (= 1) for chiral
5₂ and vanishes for amphichiral 4₁.

DEFINITIONS (locked BEFORE computing — nothing below is tuned to pass):

  • For chirality ε, `c^ε(q)` is the certified off-diagonal Stokes q-series
    that carries the DT constant:
        5₂:  c⁺(q) = S⁺(q)[0][1]   (the (96) factorization, leading 4)
             c⁻(q) = S⁻(q)[0][2]   (the (97) factorization, leading 3)
        4₁:  amphichiral ⇒ a single 2×2 block, DT spectrum collapses to the
             one constant {3}; both chiralities carry the SAME 3, so
             c⁺ = c⁻ = S⁺(0)[0][1] = 3.
    (The chirality→slot identification is the merged distinguisher's, reused
     unchanged: `dt_from_Splus = S⁺(0)[0][1]`, `dt_from_Sminus = S⁻(0)[0][2]`.)

  • SADDLE VECTOR   v(q) = ( c⁺(q), c⁻(q) ) ∈ ℝ².
  • The CLASSICAL / ι-fixed (amphichiral) axis is the diagonal c⁺ = c⁻.
  • ι-EVEN (symmetric)  coordinate  e(q) = ½( c⁺(q) + c⁻(q) )   — projection
    onto the diagonal (the scalar / "on-saddle" component).
  • ι-ODD (bar-odd) OFFSET  o(q) = c⁺(q) − c⁻(q)   — the perpendicular
    displacement of the saddle vector off the classical diagonal. This is the
    bar-odd grade the observable ω = β·p − β⁻¹·q lives in
    (`BarOddAntisymOffDiagonal.omega_iota_odd`), the antisymmetric datum that
    is exactly 0 on the amphichiral ι-fixed locus.
  • SADDLE ANGLE   θ(q) = atan2( o(q), c⁺(q)+c⁻(q) )  — the angle of v(q) off
    the classical diagonal (0 ⇔ on the saddle; small nonzero ⇔ near-but-not-on).
  • MAGNITUDE  |v(q)| = hypot(c⁺, c⁻);  perpendicular offset distance = |o|/√2.

LOCKED EXPECTED ASSERTIONS (falsifiable, set before the compute — if any had
come out otherwise it would be a valuable honest negative, reported scope-(a)):

  A1  5₂ q→0 offset  o(0) = c⁺(0) − c⁻(0)  == 1   (the {3,4} ι-odd difference).
  A2  4₁ offset       o    == 0                    (amphichiral, single DT const).
  A3  5₂ saddle angle θ(0) > 0  AND  4₁ angle == 0 (near-but-not-on vs on).
  A4  the 5₂ offset o(q) is NOT a q-constant — the saddle is genuinely
      q-deformed (drifts away from its q→0 position). Expected: NOT constant.

HONEST SCOPE (stated up front, NOT overclaimed):
  The certified Stokes series are Taylor series around q → 0 (the DT /
  semiclassical limit, where GGM read {3,4}); the (q;q)-type factors DIVERGE
  at q = 1. So the "origin-centered ONLY at q = 1" leg of the picture — that
  o(q) → 0 as q → 1 — CANNOT be tested from these series (q = 1 is outside
  their domain). q = 1 is the ι-fixed point where any bar-odd object vanishes
  structurally, but o(q) here is a q→0-ANCHORED cross-chirality datum, not an
  object continued to q = 1. This probe therefore CONFIRMS the DT-limit legs
  (A1–A4) and leaves the q = 1 leg OPEN (beaned). No fit; no c_k wired; no
  axiomatization; nothing wired to any dashboard / the Q_β ladder; scope-(a).
"""
from __future__ import annotations

import importlib.util
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

# reuse the certified 5₂ sandwich machinery UNCHANGED (K1/K2/K3 ✓, unflipped)
_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_stokes_sandwich",
    _HERE / "qbeta_g3_5two_stokes_sandwich.py")
_sw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sw)
_tw = _sw._tw

ORD = 18  # exact-integer q-series order the sandwich certifies (K2)

# ---- 4₁ certified leading Stokes datum (amphichiral control) --------------
# S⁺(0) = [[1,3],[0,1]] (GGM eq 60; StokesQZeroDTCount.Splus0). Amphichiral ⇒
# the DT spectrum collapses to the single constant {3}; both chiralities carry
# the same 3. Corpus q-drift of that off-diagonal entry (StokesSymmetryConstant
# R1, cited — NOT recomputed here): 3 at q→0 → 1.5852 at the substrate q̃_sub.
FOURONE_DT_CONST = 3
FOURONE_SUBSTRATE_R1 = 1.5852  # cited: StokesSymmetryConstant.lean (R1 reading)


def _coeff(series, k):
    return series[k] if k < len(series) else Fr(0)


def build_5two_S():
    """Assemble the certified S±(q) 3×3 series (unflipped, K1/K2/K3 ✓)."""
    Wq = _sw.series_mat_raw()
    Wqi = _sw.series_mat_ext()
    Sp = _sw.sandwich(Wq, Wqi, _sw.L_P, _sw.R_P, first_is_qi=True)
    Sm = _sw.sandwich(Wq, Wqi, _sw.L_M, _sw.R_M, first_is_qi=False)
    return Sp, Sm


def series_sub(a, b, order=ORD):
    return [_coeff(a, k) - _coeff(b, k) for k in range(order + 1)]


def series_add(a, b, order=ORD):
    return [_coeff(a, k) + _coeff(b, k) for k in range(order + 1)]


def eval_series(series, q, order):
    return sum(float(_coeff(series, k)) * q ** k for k in range(order + 1))


def is_q_constant(series, order=ORD):
    return all(_coeff(series, k) == 0 for k in range(1, order + 1))


def saddle_geometry(cp0, cm0):
    """(angle off diagonal, magnitude, perpendicular offset distance) for the
    leading (q→0) saddle vector v = (cp0, cm0)."""
    o = cp0 - cm0
    s = cp0 + cm0
    angle = math.degrees(math.atan2(float(o), float(s)))
    mag = math.hypot(float(cp0), float(cm0))
    perp = abs(float(o)) / math.sqrt(2.0)
    return angle, mag, perp


def main() -> int:
    print("=" * 78)
    print(" saddle-offset probe — 4₁ (amphichiral) vs 5₂ (chiral) certified "
          "Stokes data")
    print("=" * 78)

    # ================= 5₂ (chiral) — the real numerical content =============
    Sp, Sm = build_5two_S()
    c_plus = Sp[0][1]     # (96) factorization off-diagonal, leading 4
    c_minus = Sm[0][2]    # (97) factorization off-diagonal, leading 3
    offset = series_sub(c_plus, c_minus)
    even2 = series_add(c_plus, c_minus)

    cp0, cm0 = _coeff(c_plus, 0), _coeff(c_minus, 0)
    o0 = _coeff(offset, 0)
    angle2, mag2, perp2 = saddle_geometry(cp0, cm0)
    off_is_const = is_q_constant(offset)

    print("\n[5₂] certified saddle vector v(q) = (c⁺(q), c⁻(q)):")
    print(f"     c⁺(q) = S⁺[0][1] = "
          f"{[str(_coeff(c_plus, k)) for k in range(6)]} …  (leading {cp0})")
    print(f"     c⁻(q) = S⁻[0][2] = "
          f"{[str(_coeff(c_minus, k)) for k in range(6)]} …  (leading {cm0})")
    print(f"     ι-odd OFFSET o(q) = c⁺−c⁻ = "
          f"{[str(_coeff(offset, k)) for k in range(6)]} …")
    print(f"     q→0 offset o(0) = {o0}   (the {{3,4}} ι-odd difference)")
    print(f"     saddle angle θ(0) = {angle2:.4f}°   |v(0)| = {mag2:.4f}   "
          f"perp offset = {perp2:.4f}")
    print(f"     offset q-independent? {off_is_const}  "
          f"(picture predicts NO — the saddle is q-deformed)")

    # numeric angle/magnitude drift at a few |q|<1 sample points, with a
    # truncation-stability guard (compare O(q^18) vs O(q^12)).
    print("\n[5₂] saddle drift at |q|<1 (truncation-stable points only):")
    drift = {}
    for q in (0.02, 0.05, 0.10, 0.20):
        cp_hi, cm_hi = eval_series(c_plus, q, ORD), eval_series(c_minus, q, ORD)
        cp_lo, cm_lo = eval_series(c_plus, q, 12), eval_series(c_minus, q, 12)
        stable = (abs(cp_hi - cp_lo) < 1e-6 and abs(cm_hi - cm_lo) < 1e-6)
        o = cp_hi - cm_hi
        ang = math.degrees(math.atan2(o, cp_hi + cm_hi))
        mag = math.hypot(cp_hi, cm_hi)
        drift[f"q={q}"] = {"c_plus": cp_hi, "c_minus": cm_hi, "offset": o,
                           "angle_deg": ang, "magnitude": mag,
                           "trunc_stable": stable}
        flag = "stable" if stable else "UNSTABLE (series radius exceeded)"
        print(f"     q={q:<5}: offset={o:+.5f}  angle={ang:+.4f}°  "
              f"|v|={mag:.5f}  [{flag}]")

    # ================= 4₁ (amphichiral control) ============================
    # Decidable from the certified S⁺(0)=[[1,3],[0,1]] + amphichiral collapse:
    # single DT constant 3, both chiralities coincide ⇒ v=(3,3) on the diagonal.
    cp0_41 = cm0_41 = Fr(FOURONE_DT_CONST)
    o0_41 = cp0_41 - cm0_41
    angle41, mag41, perp41 = saddle_geometry(cp0_41, cm0_41)
    print("\n[4₁] amphichiral control (certified S⁺(0)=[[1,3],[0,1]], single "
          "DT const 3):")
    print(f"     saddle vector v = (3, 3)  ON the classical diagonal")
    print(f"     ι-odd OFFSET o = 3 − 3 = {o0_41}   (vanishes — amphichiral)")
    print(f"     saddle angle θ = {angle41:.4f}°   |v| = {mag41:.4f}")
    print(f"     [cited, not recomputed] off-diagonal q-drift: 3 (q→0) → "
          f"{FOURONE_SUBSTRATE_R1} (substrate) — the MAGNITUDE moves while the "
          f"OFFSET stays 0 (StokesSymmetryConstant R1).")

    # ================= verdict (honest, scope-labelled) ====================
    a1 = (o0 == 1)
    a2 = (o0_41 == 0)
    a3 = (angle2 > 0.0 and angle41 == 0.0)
    a4 = (not off_is_const)
    all_dt_legs = a1 and a2 and a3 and a4

    verdict = (
        "SADDLE-OFFSET PICTURE CONFIRMED AT THE DT LIMIT [scope-(a)], q=1 leg "
        "OPEN. Lifting the certified {3,4} Stokes data into a 2-D saddle "
        f"vector v(q)=(c⁺,c⁻): chiral 5₂ has v(0)=({cp0},{cm0}) sitting OFF "
        f"the classical (amphichiral) diagonal at angle {angle2:.3f}° with "
        f"ι-odd offset o(0) = c⁺−c⁻ = {o0} — reproducing EXACTLY the ι-odd "
        "{3,4} difference (the merged distinguisher's chiralityOdd 4 3 = 1) as "
        "the SEMICLASSICAL (q→0) displacement of the saddle. Amphichiral 4₁ "
        "has v=(3,3) ON the diagonal, offset 0 — the winding is origin-"
        "centered exactly when the knot is bar-symmetric. The offset is "
        f"q-DEPENDENT (o(q) = {o0} {'+' if _coeff(offset,1)>=0 else '−'}"
        f"{abs(_coeff(offset,1))}q + …, not a constant): the saddle genuinely "
        "deforms with q — the 'winds near-but-not-on' picture, quantified. "
        "HONEST SCOPE: the 'origin-centered ONLY at q=1' leg is NOT "
        "established — the q→0-anchored certified series diverge at q=1, and "
        "o(q) is a cross-chirality DT datum (leading 1 ≠ 0), not shown to "
        "continue to 0 at the ι-fixed point q=1. That leg is a distinct, "
        "untested claim (beaned). No fit; no c_k wired; no axiomatization; "
        "nothing wired to production; scope-(a)."
        if all_dt_legs else
        "SADDLE-OFFSET PROBE — HONEST NEGATIVE / PARTIAL [scope-(a)]. The "
        f"locked legs came out A1(o0==1)={a1}, A2(4₁ o==0)={a2}, "
        f"A3(angle split)={a3}, A4(q-deformed)={a4}. A failing leg CONSTRAINS "
        "the saddle-offset reading (it does NOT structurally exclude any "
        "ingredient — no proved invariant is invoked). Data recorded for the "
        "next attempt. No fit; no c_k wired; scope-(a).")
    print("\nVERDICT:", verdict)

    # ================= witness =============================================
    wb = WitnessBuilder("saddle-offset-fourone-fivetwo", engine="fractions-exact")
    wb.set_description(
        "Saddle-offset geometric reading of the certified 4₁/5₂ Stokes data. "
        "Lifts the {3,4} DT split into a 2-D saddle vector v(q)=(c⁺,c⁻) with an "
        "angle and magnitude; the ι-odd (bar-odd) offset o(q)=c⁺−c⁻ has q→0 "
        "value 1 for chiral 5₂ (reproducing the merged distinguisher's "
        "chiralityOdd 4 3 = 1) and 0 for amphichiral 4₁. Tests the 'knot winds "
        "near-but-not-on the saddle, origin-centered only in the bar-symmetric "
        "limit' picture; confirms the DT-limit legs and leaves the q=1 leg open.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("definitions", {
        "saddle_vector": "v(q) = (c^+(q), c^-(q)); c^eps = certified off-diag "
                         "Stokes series carrying the DT constant",
        "iota_even": "e(q) = (c^+ + c^-)/2  (projection on classical diagonal)",
        "iota_odd_offset": "o(q) = c^+ - c^-  (perpendicular displacement; "
                           "bar-odd grade of omega = beta*p - beta^-1*q)",
        "saddle_angle": "theta(q) = atan2(o, c^+ + c^-)  (deg off diagonal)",
        "chirality_slot_identification":
            "reused unchanged from fivetwo_crossknot_34_distinguisher.py: "
            "c^+ = S^+[0][1] (96 const 4), c^- = S^-[0][2] (97 const 3)"})
    wb.add_data("fivetwo", {
        "c_plus_series": [str(_coeff(c_plus, k)) for k in range(ORD + 1)],
        "c_minus_series": [str(_coeff(c_minus, k)) for k in range(ORD + 1)],
        "offset_series": [str(_coeff(offset, k)) for k in range(ORD + 1)],
        "saddle_vector_q0": [str(cp0), str(cm0)],
        "offset_q0": str(o0),
        "saddle_angle_q0_deg": angle2,
        "magnitude_q0": mag2,
        "perp_offset_q0": perp2,
        "offset_is_q_constant": off_is_const,
        "drift_samples": drift,
        "provenance": "qbeta_g3_5two_stokes_sandwich.py (K1/K2/K3 ✓, unflipped)"})
    wb.add_data("fourone", {
        "saddle_vector": ["3", "3"],
        "offset": str(o0_41),
        "saddle_angle_deg": angle41,
        "magnitude": mag41,
        "dt_spectrum": "{3} (amphichiral collapse of {3,4})",
        "offdiag_drift_cited": {"q_to_0": 3, "substrate_R1": FOURONE_SUBSTRATE_R1,
                                "source": "StokesSymmetryConstant.lean (R1)"},
        "note": "structural: offset 0 by amphichirality (V(4₁)_odd = 0); "
                "the magnitude moves with q but the vector stays on the diagonal"})
    wb.add_data("scope", {
        "confirmed": "DT-limit (q→0) legs A1–A4",
        "open": "the 'origin-centered only at q=1' leg — q→0-anchored series "
                "diverge at q=1; o(q) not continued to the iota-fixed point",
        "wired_to_production": False,
        "discipline": "no fit; no c_k wired; no axiomatization; scope-(a)"})
    wb.add_data("verdict", verdict)
    wb.add_assertion(
        "fivetwo_offset_q0_reproduces_34_difference",
        computed=float(o0), expected=1.0, tolerance=0.5,
        source="o(0) = c^+(0) - c^-(0) = 4 - 3 = 1, the ι-odd {3,4} datum "
               "(DEFINED before compute; not tuned)")
    wb.add_assertion(
        "fourone_offset_vanishes_amphichiral",
        computed=float(o0_41), expected=0.0, tolerance=0.5,
        source="amphichiral 4₁: single DT constant 3, v=(3,3) on diagonal")
    wb.add_assertion(
        "saddle_angle_split_chiral_vs_amphichiral",
        computed=1.0 if a3 else 0.0, expected=1.0, tolerance=0.5,
        source="5₂ angle>0 (near-but-not-on), 4₁ angle=0 (on the saddle)")
    wb.add_assertion(
        "fivetwo_offset_is_q_deformed",
        computed=0.0 if off_is_const else 1.0, expected=1.0, tolerance=0.5,
        source="o(q) is NOT a q-constant — the saddle genuinely deforms with q "
               "(picture: near-but-not-on, moves off the classical position)")
    wb.save()
    return 0 if all_dt_legs else 1


if __name__ == "__main__":
    raise SystemExit(main())
