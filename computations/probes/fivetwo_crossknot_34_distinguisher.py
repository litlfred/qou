#!/usr/bin/env python3
"""fivetwo_crossknot_34_distinguisher.py — the 5₂ cross-knot {3,4} structural
distinguisher for the scalar-symmetry-constant vs DT-spectrum fork.

STRUCTURAL probe (dodges the σ_A ≈ 40 % precision ceiling of the 4₁ numerics).
The c₃-odd chain hinges on: does the bar-odd observable S carry the *scalar*
GGM symmetry constant (`A_ω = 3` for 4₁, from `S₁₂+S₂₁ = 3·S₁₁`), or something
reflecting the full **DT spectrum {3,4}**? For 4₁ the 2×2 block makes the two
readings hard to separate; 5₂'s 3×3 block has its OWN Stokes structure and DT
data, so the 5₂ analogue is a q₀-independent distinguisher.

REUSE (not recompute): the certified 5₂ Stokes pair `S±(q)` is assembled by
`qbeta_g3_5two_stokes_sandwich.py` (K1/K2/K3 passing, unflipped convention),
whose q→0 targets are the glyph-decoded (96/97) factorizations carrying the
constants {3,4}. This probe imports that machinery unchanged and computes:

  1. The 5₂ analogue of the 4₁ symmetry constant `(S₁₂+S₂₁)/S₁₁ = 3`, for the
     3×3 blocks S⁺(q) and S⁻(q) — is any clean-integer, q-exact combination
     present, per matrix?
  2. The 5₂ DT spectrum (the eq-98 analogue) — the off-diagonal integers the
     leading Stokes factorization carries.
  3. THE DISTINGUISHER: whether the ι-even (symmetric SUM) reading yields a
     single scalar constant, and whether the ι-ODD (antisymmetric DIFFERENCE)
     reading — the grade the bar-odd observable `ω = βp − β⁻¹q` actually lives
     in (`BarOddAntisymOffDiagonal.lean`, `omega_iota_odd`) — instead reflects
     the chirality split {S⁺ ↔ 4, S⁻ ↔ 3}.

No fit, no c_k wired, no axiomatization, no answer picked to match 4₁; exact
Fraction arithmetic (mpmath only for a numeric echo); scope-(a).
"""
from __future__ import annotations

import importlib.util
import sys
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

# import the certified sandwich machinery unchanged
_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_stokes_sandwich",
    _HERE / "qbeta_g3_5two_stokes_sandwich.py")
_sw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sw)
_tw = _sw._tw

ORD = 12  # series order to test q-exactness of candidate constants


def _coeff(series, k):
    return series[k] if k < len(series) else Fr(0)


def series_is_const(series, order=ORD):
    """True iff a q-series is a q-independent constant to `order` (all higher
    coefficients zero). Returns (is_const, value_or_None)."""
    c0 = _coeff(series, 0)
    for k in range(1, order + 1):
        if _coeff(series, k) != 0:
            return False, None
    return True, c0


def ratio_const(num_series, den_series, order=ORD):
    """Test whether num/den is a q-independent constant, by long division of
    q-series. Returns (is_const, value_or_None). den[0] must be nonzero."""
    d0 = _coeff(den_series, 0)
    if d0 == 0:
        return False, None
    # compute quotient q-series Q with num = den * Q, to `order`
    Q = []
    for k in range(order + 1):
        acc = _coeff(num_series, k)
        for j in range(1, k + 1):
            acc -= _coeff(den_series, j) * Q[k - j]
        Q.append(acc / d0)
    # constant iff Q[k]=0 for k>=1
    for k in range(1, order + 1):
        if Q[k] != 0:
            return False, None
    return True, Q[0]


def build_S():
    """Assemble the certified S±(q) 3×3 series (unflipped convention)."""
    Wq_raw = _sw.series_mat_raw()
    Wqi_raw = _sw.series_mat_ext()
    Sp = _sw.sandwich(Wq_raw, Wqi_raw, _sw.L_P, _sw.R_P, first_is_qi=True)
    Sm = _sw.sandwich(Wq_raw, Wqi_raw, _sw.L_M, _sw.R_M, first_is_qi=False)
    return Sp, Sm


def add_series(a, b):
    return _tw._add(a, b)


def leading(S):
    return [[_coeff(S[i][j], 0) for j in range(3)] for i in range(3)]


def scan_symmetry_constants(S, label):
    """For a 3×3 series matrix, scan candidate q-exact 'symmetry constant'
    combinations analogous to 4₁'s (S₁₂+S₂₁)/S₁₁ = 3.

    Candidates (all ι-even / symmetric SUM forms unless noted):
      P(i,j) = (S_ij + S_ji)/S_kk   for each unordered pair {i,j}, each diag k.
    Report which are q-exact constants and their values.
    """
    out = {}
    pairs = [(0, 1), (0, 2), (1, 2)]
    for (i, j) in pairs:
        num = add_series(S[i][j], S[j][i])
        for k in range(3):
            ok, val = ratio_const(num, S[k][k])
            if ok:
                out[f"(S{i+1}{j+1}+S{j+1}{i+1})/S{k+1}{k+1}"] = str(val)
    # also: is the raw off-diagonal SUM itself a constant series?
    for (i, j) in pairs:
        num = add_series(S[i][j], S[j][i])
        ok, val = series_is_const(num)
        if ok:
            out[f"S{i+1}{j+1}+S{j+1}{i+1} (raw const)"] = str(val)
    # trace
    tr = _tw._add(_tw._add(S[0][0], S[1][1]), S[2][2])
    okt, vt = series_is_const(tr)
    out["trace"] = str(vt) if okt else "q-dependent"
    return out


def main() -> int:
    print("=" * 78)
    print(" 5₂ cross-knot {3,4} distinguisher — scalar symmetry constant vs "
          "DT spectrum")
    print("=" * 78)

    Sp, Sm = build_S()
    Lp, Lm = leading(Sp), leading(Sm)
    print("\n[data] certified leading Stokes matrices (unflipped, K1/K2/K3 ✓):")
    print("  S⁺(0) =", Lp, "  (carries the (96) constant 4 at (1,2))")
    print("  S⁻(0) =", Lm, "  (carries the (97) constant 3 at (1,3))")

    # ---- 1. symmetry-constant scan, per 3×3 block --------------------------
    scan_p = scan_symmetry_constants(Sp, "S+")
    scan_m = scan_symmetry_constants(Sm, "S-")
    print("\n[1] q-exact symmetry-constant combinations found:")
    print("    S⁺:", scan_p)
    print("    S⁻:", scan_m)

    # 4₁ reference: (S12+S21)/S11 = 3 exactly. Test the DIRECT (1,2) analogue
    # per matrix (the closest structural clone of the 4₁ relation).
    ok_p12, val_p12 = ratio_const(add_series(Sp[0][1], Sp[1][0]), Sp[0][0])
    ok_m12, val_m12 = ratio_const(add_series(Sm[0][1], Sm[1][0]), Sm[0][0])
    print("\n[1b] direct 4₁-clone (S12+S21)/S11, per matrix:")
    print(f"     S⁺: q-exact const? {ok_p12}  value={val_p12 if ok_p12 else '—'}")
    print(f"     S⁻: q-exact const? {ok_m12}  value={val_m12 if ok_m12 else '—'}")

    # ---- 2. DT spectrum (eq-98 analogue) -----------------------------------
    # The 5₂ leading factorization constants: the off-diagonal integers the
    # (96)/(97) unipotent factorizations carry. S⁺(0) upper (1,2)=4; S⁻(0)
    # upper (1,3)=3. The DT spectrum is the multiset of these constants.
    dt_from_Splus = Lp[0][1]      # (96) constant
    dt_from_Sminus = Lm[0][2]     # (97) constant
    dt_spectrum = sorted({dt_from_Splus, dt_from_Sminus})
    print("\n[2] 5₂ DT spectrum (eq-98 analogue):")
    print(f"     from S⁺(0) (96) constant : {dt_from_Splus}")
    print(f"     from S⁻(0) (97) constant : {dt_from_Sminus}")
    print(f"     spectrum = {dt_spectrum}")

    # ---- 3. the distinguisher ---------------------------------------------
    # ι-even (SUM): symmetric across chirality — for 4₁ (amphichiral) S⁺≅S⁻ so
    # a single scalar (3). For 5₂ (chiral), do S⁺ and S⁻ give the SAME scalar?
    even_scalar_matches = (ok_p12 and ok_m12 and val_p12 == val_m12)
    # ι-odd (DIFFERENCE): the grade the bar-odd observable ω lives in. The
    # chirality split is 4 (S⁺) vs 3 (S⁻); their antisymmetric datum is 4−3.
    chirality_split = (dt_from_Splus, dt_from_Sminus)
    odd_difference = dt_from_Splus - dt_from_Sminus

    print("\n[3] DISTINGUISHER:")
    print(f"     ι-EVEN scalar reading — do S⁺ and S⁻ share ONE (S12+S21)/S11 "
          f"constant? {even_scalar_matches}")
    print(f"        (S⁺→{val_p12 if ok_p12 else '—'}, "
          f"S⁻→{val_m12 if ok_m12 else '—'})")
    print(f"     ι-ODD chirality split — S⁺ carries {chirality_split[0]}, "
          f"S⁻ carries {chirality_split[1]}; the bar-odd (ι-odd) datum is the "
          f"difference {odd_difference}.")

    # Adjudication (honest, scope-labelled).
    if not even_scalar_matches:
        verdict_key = "refutes-scalar-universality"
        verdict = (
            "5₂ REFUTES the single-scalar-symmetry-constant reading "
            "[scope-(a), structural]. Unlike amphichiral 4₁ — where S⁺≅S⁻ under "
            "ι and one scalar (S12+S21)/S11 = 3 serves both — chiral 5₂ splits "
            f"the DT spectrum {dt_spectrum} across the two Stokes matrices "
            f"(S⁺ carries {dt_from_Splus}, S⁻ carries {dt_from_Sminus}). The "
            "bar-odd observable ω = βp − β⁻¹q is ι-ODD "
            "(BarOddAntisymOffDiagonal.omega_iota_odd) and vanishes on the "
            "amphichiral (ι-fixed) locus, so it cannot be carried by the "
            "ι-EVEN symmetric-sum constant that gives the scalar 3. The 5₂ "
            "data are therefore consistent with a SPECTRUM-reflecting / "
            "chirality-split reading, NOT the universal scalar A_ω=3. This "
            "neither confirms A=2 (κ_shape) nor A=3 (A_ω·κ_pot) as a universal "
            "scalar: the correct object is per-chirality (the {3,4} split), "
            "which at 4₁ degenerates to the single 3 because the two "
            "chiralities coincide. Whether the OBSERVABLE inherits the sum "
            "(3+4)/… , the S⁺ member (4), or the S⁻ member (3) is the residual "
            "normalization fork (qou-yh67); 5₂ shows it is a CHOICE AMONG "
            "SPECTRUM MEMBERS, not a knot-independent constant.")
    else:
        verdict_key = "scalar-universal"
        verdict = (
            f"5₂ supports a knot-independent scalar symmetry constant "
            f"{val_p12}: both chiral Stokes matrices share (S12+S21)/S11 = "
            f"{val_p12} q-exactly [scope-(a)]. This is consistent with the "
            f"scalar A_ω reading.")

    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("fivetwo-crossknot-34-distinguisher",
                        engine="fractions-exact")
    wb.set_description(
        "5₂ cross-knot {3,4} structural distinguisher for the scalar-"
        "symmetry-constant vs DT-spectrum fork (scalar A_ω=3 / A=3 vs "
        "spectrum-reflecting). Reuses the certified 5₂ Stokes pair; tests "
        "whether the two chiral Stokes matrices S± share one q-exact "
        "(S12+S21)/S11 constant (ι-even) or split the DT spectrum {3,4} "
        "across chirality (ι-odd, the grade the bar-odd observable lives in). "
        "q₀-independent — dodges the σ_A≈40% 4₁ precision ceiling.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("certified_leading_matrices", {
        "S_plus_0": [[str(x) for x in r] for r in Lp],
        "S_minus_0": [[str(x) for x in r] for r in Lm],
        "provenance": "qbeta_g3_5two_stokes_sandwich.py K1/K2/K3 ✓, unflipped"})
    wb.add_data("symmetry_constant_scan", {
        "S_plus": scan_p, "S_minus": scan_m,
        "direct_4one_clone_S12plusS21_over_S11": {
            "S_plus": {"q_exact_const": ok_p12,
                       "value": str(val_p12) if ok_p12 else None},
            "S_minus": {"q_exact_const": ok_m12,
                        "value": str(val_m12) if ok_m12 else None}}})
    wb.add_data("dt_spectrum", {
        "from_S_plus_96_constant": dt_from_Splus,
        "from_S_minus_97_constant": dt_from_Sminus,
        "spectrum": dt_spectrum,
        "eq98_analogue": "5₂ carries both {3,4}; 4₁'s single S⁺(0)=[[1,3],[0,1]] "
                         "carries only 3 (amphichiral degeneracy)"})
    wb.add_data("distinguisher", {
        "iota_even_scalar_universal": even_scalar_matches,
        "iota_odd_chirality_split": list(chirality_split),
        "iota_odd_difference": odd_difference,
        "verdict_key": verdict_key,
        "bar_odd_grade_ref": "BarOddAntisymOffDiagonal.omega_iota_odd (ι-odd; "
                             "vanishes on amphichiral ι-fixed locus)"})
    wb.add_data("verdict", verdict)
    wb.add_data("discipline",
                "structural; exact Fraction q-series; no fit; no c_k wired; "
                "no axiomatization; scope-(a); q₀-independent (dodges σ_A≈40% "
                "ceiling); answer NOT picked to match 4₁")
    wb.add_assertion("scalar_universality_across_chirality",
                     computed=1.0 if even_scalar_matches else 0.0,
                     expected=0.0, tolerance=0.5,
                     source="whether chiral 5₂'s S± share one q-exact "
                            "(S12+S21)/S11 — expected FALSE (spectrum splits "
                            "across chirality)")
    wb.add_assertion("dt_spectrum_is_3_4",
                     computed=1.0 if dt_spectrum == [3, 4] else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="5₂ leading Stokes factorization carries {3,4}")
    wb.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
