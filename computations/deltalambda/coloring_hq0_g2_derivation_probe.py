#!/usr/bin/env python3
"""The H(q₀) coloring-map derivation (owner "go"): pin the meridian-holonomy map by μ₀-consistency
and read off the bar-even coefficient g₂ — forward, parameter-free, **no fit to g₂**.

RESULT (scope-(a) prune, formalize-first): the flat trefoil shape z=1/2 is an INFLECTION point of the
Rogers dilogarithm (L''(1/2)=0, proved in RogersDilogInflection.lean), so the single-tetrahedron
bar-even (2nd-order) shape correction VANISHES. Hence g₂ (order h²) cannot come from the single shape
modulus; it must be the pairwise e₂ coupling of the 4 octahedral tetrahedra (FourDilogFirstOrder.e2).

CHAIN (read first):
  * PR #4301: deuteron σ₁³ = trefoil T(2,3), torus knot, flat shape z=1/2, exact reciprocal partner
    z₁=1/z₀; frame = single modulus z₀ via meridian map z₀=H/(H-1) (flat H=-1 ⟹ z₀=1/2).
  * The single-tetrahedron binding amplitude is the Rogers dilog L(z)=Li₂(z)+½ ln z ln(1-z) (the real
    phase of the octahedral state integral; the volume/Im side vanishes on the flat shape).
  * μ₀ = m_e/(3(q-q⁻¹)/2) (derived, in the paper). The octahedral first-order (bar-odd) amplitude
    A₁·δ must match this weight ⇒ pins κ=δ/(q-q⁻¹)=1/2 — PARAMETER-FREE, not a fit.

WHAT THIS PROBE ESTABLISHES (all forward; no number fitted to g₂):
  A. L''(1/2)=0 EXACTLY (high-precision + the analytic bracket B(z)=ln z/(1-z)² - ln(1-z)/z²
     antisymmetric under z↦1-z; B(1/2)=0). The flat shape is a Rogers-dilog inflection.
  B. Consistency pin: A₁ = L'(z)-shape-slope gives κ=1/2 (matches μ₀'s 3(q-q⁻¹)/2 "3-crossing" weight).
  C. The g₂ BRACKET TABLE: Rogers (single tet) → g₂=0 (inflection); naive symmetric s(z₀)=z₀+1/z₀
     → g₂=2 (factor-2 overshoot, not the physical dilog); target 1.0087. Neither single-coordinate
     amplitude hits it — g₂ is a genuine 4-tetrahedron (e₂) quantity.
  D. The single-modulus's LEADING bar-even term is 4th-order (L''''≠0) ⇒ ∝ h⁴, negligible at h².

ANTI-FIT (STRICT): κ=1/2 is pinned by μ₀ (independently derived), not tuned to g₂. The g₂ values
0 and 2 are parameter-free CONSEQUENCES; the target 1.0087 is reproduced by NEITHER — reported as a
prune, not a match. The §2e entropy bound forbids scanning amplitude-forms for g₂. Nothing wired.

EXPLORATORY — audit + witness only.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q0_STR = "1.10997859555733471"   # muon-canonical (computations/ layer)


def rogers_L(z):
    """Real Rogers dilogarithm L(z)=Li₂(z)+½ ln z ln(1-z) (0<z<1)."""
    return mp.polylog(2, z) + mp.mpf("0.5") * mp.log(z) * mp.log(1 - z)


def L2_bracket(z):
    """The analytic bracket B(z)=ln z/(1-z)² - ln(1-z)/z²  (L''(z) = -½ B(z))."""
    return mp.log(z) / (1 - z) ** 2 - mp.log(1 - z) / z ** 2


def deriv(f, z, n):
    return mp.diff(f, z, n)


def main() -> int:
    q = mp.mpf(Q0_STR)
    h = q - 1 / q                     # counit weight (q-q⁻¹)
    z0 = mp.mpf("0.5")

    # --- A. inflection: L''(1/2)=0, analytic bracket antisymmetric under z↦1-z ---
    L2_via_bracket = -mp.mpf("0.5") * L2_bracket(z0)
    L2_via_diff = deriv(rogers_L, z0, 2)
    bracket_half = L2_bracket(z0)
    bracket_reflect_ok = abs(L2_bracket(1 - mp.mpf("0.3")) + L2_bracket(mp.mpf("0.3"))) < mp.mpf("1e-40")
    inflection = abs(L2_via_bracket) < mp.mpf("1e-40") and abs(L2_via_diff) < mp.mpf("1e-30")

    # --- B. consistency pin κ=1/2 via the shape slope A₁ (naive symmetric s carries the -3 slope) ---
    def s(z):
        return z + 1 / z
    A1_s = deriv(s, z0, 1)            # = 1 - 1/z0² = -3
    kappa = mp.mpf(-3) / (2 * A1_s)   # from A1_s·δ = -3(q-q⁻¹)/2, δ=κ(q-q⁻¹) ⇒ κ=-3/(2 A1_s)=1/2

    # --- C. g₂ bracket table: single-coordinate amplitudes, consistency-pinned ---
    def g2_for(amp, name):
        A1 = deriv(amp, z0, 1)
        A2 = deriv(amp, z0, 2) / 2      # 2nd Taylor coeff
        kap = mp.mpf(-3) / (2 * A1)     # each amplitude pinned to the same μ₀ first-order weight
        g2 = A2 * kap ** 2              # bar-even 2nd-order coeff, in units of h²
        return name, mp.nstr(A1, 6), mp.nstr(A2, 6), mp.nstr(kap, 6), mp.nstr(g2, 6)

    table = [g2_for(rogers_L, "Rogers L(z) single tet"), g2_for(s, "naive symmetric z+1/z")]

    # --- D. single-modulus amplitude is PURELY BAR-ODD about z=1/2 (all even derivs vanish) ---
    #   Euler reflection L(z)+L(1-z)=π²/6 ⇒ L(1/2+δ)+L(1/2-δ)=const ⇒ even part constant.
    L4 = deriv(rogers_L, z0, 4)
    L3 = deriv(rogers_L, z0, 3)
    reflection_const = rogers_L(mp.mpf("0.3")) + rogers_L(1 - mp.mpf("0.3"))   # = π²/6
    reflection_ok = abs(reflection_const - mp.pi ** 2 / 6) < mp.mpf("1e-30")
    all_even_vanish = abs(L2_via_diff) < mp.mpf("1e-30") and abs(L4) < mp.mpf("1e-20")
    leading_bar_even_order = None  # single modulus: NO bar-even at any order

    target_g2 = mp.mpf("1.00865")

    result = {
        "A_inflection": {
            "L2_half_via_bracket": mp.nstr(L2_via_bracket, 6),
            "L2_half_via_numeric_diff": mp.nstr(L2_via_diff, 6),
            "bracket_half_B(1/2)": mp.nstr(bracket_half, 6),
            "bracket_antisymmetric_under_reflect": bool(bracket_reflect_ok),
            "inflection_confirmed": bool(inflection),
            "meaning": "z=1/2 (flat trefoil shape) is an inflection of the Rogers dilog; single-"
                       "tetrahedron bar-even 2nd-order correction vanishes. (Lean: rogersL2_half_eq_zero.)",
        },
        "B_consistency_pin": {
            "shape_slope_A1_of_s": mp.nstr(A1_s, 6),
            "kappa": mp.nstr(kappa, 6),
            "pin": "A₁·δ = -3(q-q⁻¹)/2 (μ₀'s derived 3-crossing weight) ⇒ κ=1/2. Parameter-free.",
            "suggestive_not_claimed": "1/z0²-1 = 3 = trefoil crossing number at z0=1/2 (flagged; not a claim).",
        },
        "C_g2_bracket_table": {
            "columns": ["amplitude", "A1", "A2", "kappa", "g2 = A2*kappa^2 (units h^2)"],
            "rows": table,
            "target_g2": mp.nstr(target_g2, 6),
            "verdict": "single-coordinate amplitudes give g₂ ∈ {0 (Rogers, inflection), 2 (naive sym, "
                       "factor-2 overshoot)}; target 1.0087 reproduced by NEITHER. g₂ is a genuine "
                       "4-tetrahedron (octahedral e₂) quantity, not a single-modulus one.",
            "no_fit": True,
        },
        "D_single_modulus_purely_bar_odd": {
            "L'''(1/2)_bar_odd_3rd": mp.nstr(L3, 6),
            "L''(1/2)_bar_even_2nd": mp.nstr(L2_via_diff, 6),
            "L''''(1/2)_bar_even_4th": mp.nstr(L4, 6),
            "euler_reflection_L(z)+L(1-z)": mp.nstr(reflection_const, 8),
            "euler_reflection_eq_pi2_over_6": bool(reflection_ok),
            "all_even_derivs_vanish": bool(all_even_vanish),
            "meaning": "L(z)+L(1-z)=π²/6 (Euler reflection) ⇒ the single-tetrahedron amplitude is "
                       "PURELY BAR-ODD about z=1/2: ALL even-order (bar-even) terms vanish, not just "
                       "the 2nd. So the single modulus supplies ZERO bar-even at every order ⇒ g₂ is "
                       "entirely the octahedral e₂ (multi-tetrahedron) coupling.",
        },
        "scope": {
            "classification": "scope-(a): PRUNES the single-modulus route (proved bar-even 2nd order "
                              "=0 at the flat shape); does NOT derive g₂, does NOT exclude the "
                              "octahedral e₂ route. Next target = the 4-tetrahedron e₂ coupling.",
            "anti_laundering": "the Lean proves the inflection, not g₂. No axiom/class carries g₂.",
        },
    }

    payload = {
        "computation": "coloring-hq0-g2-derivation",
        "description": ("H(q₀) coloring-map derivation: the flat trefoil shape z=1/2 is an INFLECTION "
                        "point of the Rogers dilogarithm (L''(1/2)=0; bracket antisymmetric under Abel "
                        "reflection z↦1-z), so the single-tetrahedron bar-even 2nd-order correction "
                        "vanishes. Consistency-pinned (κ=1/2 from μ₀'s 3-crossing weight, parameter-"
                        "free) single-coordinate amplitudes give g₂∈{0 (Rogers), 2 (naive symmetric)}; "
                        "the target 1.0087 is reproduced by NEITHER. Hence g₂ is a 4-tetrahedron "
                        "octahedral e₂ quantity, not a single-modulus one — scope-(a) prune, redirects "
                        "to FourDilogFirstOrder.e2. No fit to g₂; nothing wired."),
        "audit_only": True,
        "tier": "derivation attempt → scope-(a) prune (analytic inflection + parameter-free g₂ table)",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, the H(q₀) coloring-map / g₂ bar-even coefficient",
            "lean_brick": "QOU/MassTheory/RogersDilogInflection.lean (rogersL2_half_eq_zero, "
                          "rogersL2Bracket_reflect)",
            "builds_on": "PR #4301 (deuteron=trefoil frame), #4127 (FourDilogFirstOrder.e2)",
            "sibling_magnus": "#4158 W2b (cosh→9/8, Magnus→0 — same factor-2/9-8 family, now explained)",
            "q0_convention": "muon-canonical (computations/ layer)",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "coloring-hq0-g2-derivation", payload,
        script_path=__file__, engine="mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("rogers_inflection_L2_half_zero", computed=str(bool(inflection)), expected="True")
    wb.add_assertion("bracket_antisymmetric", computed=str(bool(bracket_reflect_ok)), expected="True")
    wb.add_assertion("kappa_is_half", computed=mp.nstr(kappa, 4), expected="0.5")
    out = wb.save(extra={"auditOnly": True})

    print("=== H(q₀) coloring map → g₂: Rogers-dilog inflection prune ===")
    print(f"A. L''(1/2) = {mp.nstr(L2_via_bracket,4)} (bracket) / {mp.nstr(L2_via_diff,4)} (numeric) "
          f"⇒ INFLECTION: {inflection}   [bracket antisym under z↦1-z: {bracket_reflect_ok}]")
    print(f"B. consistency pin: A1(s)={mp.nstr(A1_s,4)} ⇒ κ={mp.nstr(kappa,4)} (=1/2, from μ₀'s 3-crossing weight)")
    print("C. g₂ bracket table (amplitude | A1 | A2 | κ | g₂=A2·κ²):")
    for r in table:
        print("     ", " | ".join(r))
    print(f"     target g₂ = {mp.nstr(target_g2,6)}  — reproduced by NEITHER (0 Rogers, 2 naive-sym)")
    print(f"D. Euler reflection L(z)+L(1-z)={mp.nstr(reflection_const,8)} (=π²/6: {reflection_ok}) ⇒ "
          f"amplitude PURELY BAR-ODD about z=1/2")
    print(f"   L''={mp.nstr(L2_via_diff,3)}, L''''={mp.nstr(L4,3)} (all even vanish: {all_even_vanish}); "
          f"L'''={mp.nstr(L3,4)} (bar-odd survives) ⇒ single modulus supplies ZERO bar-even at EVERY order")
    print("VERDICT: scope-(a) prune — the single modulus contributes NO bar-even (purely bar-odd by "
          "Euler reflection); g₂ is ENTIRELY the octahedral e₂ 4-tetrahedron coupling. No fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
