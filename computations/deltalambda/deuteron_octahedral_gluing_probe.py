#!/usr/bin/env python3
"""Deuteron octahedral gluing setup (owner task "1"): the concrete tool to attack the μ₀ −9%
residual `r` in its own frame — the ideal-triangulation shape modulus of the deuteron crossing.
Forward, SnapPy-backed, **no fit** (does NOT tune anything to r).

WHY (read first):
  * The deuteron braid word is σ₁³ (#4158). Its closure is the trefoil T(2,3) — a TORUS knot,
    NOT hyperbolic. SnapPy: Vol=0, solution_type="contains flat tetrahedra", shapes {1/2, 2},
    π₁=⟨a,b|a²b³⟩. So the crossing octahedra are DEGENERATE (real shapes) — mass Vol-side (Σ Im Φ_q)
    vanishes; binding μ₀ uses the surviving Re Φ_q phase. (audit 2026-07-25-octahedral-chi-coloring-frame-r.)
  * 2509.02354: crossing = ideal octahedron = 4 quantum dilogarithms (the 4 tetrahedra). μ₀ =
    single-tetrahedron first-order truncation (FourDilogFirstOrder.lean). Route B (#4127) ↔ Route A
    Magnus (#4158) converge on the bar-parity split −9.21% = bar-odd t ⊕ bar-even h²; the bar-even
    coefficient g₂≈1.00865 (residual r=0.87%) is the shared open.

WHAT THIS TOOL ESTABLISHES (all forward; the numbers are integer/algebraic topology, no observable
fit):
  A. Deuteron = trefoil facts (SnapPy): torus knot, Vol=0, flat, shapes {1/2,2}, group ⟨a,b|a²b³⟩.
  B. The single edge gluing equation ⟺ z₀·z₁ = 1 IDENTICALLY along the whole 1-parameter gluing
     variety. So the two flat tetrahedra are EXACT bar-reciprocals (z ↦ 1/z is the bar involution),
     and reciprocity is DEFORMATION-INVARIANT — it is never broken by the coloring. This REVISES the
     first-pass hypothesis "r = χ-coloring asymmetry across the reciprocal pair": there is no
     asymmetry to break. The frame is the single shape modulus z₀ (partner z₁=1/z₀).
  C. Meridian-holonomy map H(z₀)=z₀/(z₀−1), inverse z₀=H/(H−1); complete/flat H=−1 ⟹ z₀=1/2.
     So the deformation is one complex knob H (the substrate coloring's meridian holonomy). r is a
     BAR-EVEN function of the deformation of z₀ — the deviation of the symmetric combination
     s(z₀)=z₀+1/z₀ (bar-even) from its flat value 5/2 — NOT a reciprocal asymmetry (which is 0).

WHAT THIS TOOL DOES NOT DO (anti-fit, STRICT):
  It does NOT derive r. Producing r requires the substrate coloring's meridian-holonomy↔q map
  H(q₀) — an OPEN derivation. Illustrative parameter-free forward evaluations (H=−q₀ etc.) are
  printed ONLY to show the tool runs and the order of magnitude; they are explicitly NOT a claim
  that any equals r, and the §2e entropy bound forbids scanning H-conventions for a match. Nothing
  wired; anti-laundering stands.

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


def snappy_facts() -> dict:
    """Solid SnapPy facts about the deuteron = trefoil. Returns {} if SnapPy is absent."""
    try:
        import snappy  # noqa: F401
    except Exception:
        return {}
    import warnings
    warnings.filterwarnings("ignore")
    M = snappy.Link(braid_closure=[1, 1, 1]).exterior()   # σ₁³ closure
    shapes = [complex(z) for z in M.tetrahedra_shapes("rect")]
    G = M.fundamental_group()
    return {
        "manifold": "sigma_1^3 closure = trefoil T(2,3)",
        "volume": float(M.volume()),
        "solution_type": M.solution_type(),
        "num_tetrahedra": int(M.num_tetrahedra()),
        "shapes": [f"{z.real:.6f}{z.imag:+.6f}j" for z in shapes],
        "generators": list(G.generators()),
        "relators": list(G.relators()),
        "rect_gluing_equations": [str(r) for r in M.gluing_equations(form="rect")],
    }


def main() -> int:
    q = mp.mpf(Q0_STR)
    v = mp.sqrt(q)

    facts = snappy_facts()
    have_snappy = bool(facts)

    # --- B. edge eqn ⟺ z0·z1 = 1 exactly (verify at random z0; SnapPy-independent) ---
    #   edge0 (rect, SnapPy): z0^1 (1-z0)^-1 (1-z1)^1 = -1.  With z1 = 1/z0 this holds ∀ z0.
    recip_exact = True
    test_pts = [mp.mpc("0.31", "0.17"), mp.mpc("1.7", "-0.4"), mp.mpf("0.5"), mp.mpf("0.83")]
    for z0 in test_pts:
        z1 = 1 / z0
        lhs = z0 * (1 - z1) / (1 - z0)
        recip_exact = recip_exact and abs(lhs - (-1)) < mp.mpf("1e-30")

    # --- C. meridian holonomy map H(z0) = z0/(z0-1); z0 = H/(H-1); flat H=-1 -> z0=1/2 ---
    def z0_of_H(H):
        return H / (H - 1)

    def H_of_z0(z0):
        return z0 / (z0 - 1)

    z0_flat = mp.mpf("0.5")
    H_flat = H_of_z0(z0_flat)                       # = -1 (parabolic/complete)
    flat_bar_even = z0_flat + 1 / z0_flat           # = 5/2 (symmetric, bar-even)
    flat_bar_odd = z0_flat - 1 / z0_flat            # = -3/2 (antisymmetric, bar-odd)
    map_ok = abs(H_flat + 1) < mp.mpf("1e-30") and abs(z0_of_H(mp.mpf(-1)) - z0_flat) < mp.mpf("1e-30")

    # order parameter for r: BAR-EVEN deviation of s(z0)=z0+1/z0 from the flat 5/2.
    # (bar-odd reciprocal asymmetry log(z0 z1) ≡ 0 on the variety — nothing to break.)
    def bar_even_dev(H):
        z0 = z0_of_H(H)
        s = z0 + 1 / z0
        return (s - flat_bar_even) / flat_bar_even   # fractional bar-even deviation

    # ILLUSTRATIVE parameter-free forward evaluations (NOT a claim; NOT fitted). Two principled,
    # knob-free meridian-holonomy conventions off the complete value H=-1, deformed by the substrate.
    illustrative = {
        "H = -q0": mp.nstr(bar_even_dev(-q) * 100, 5) + " %",
        "H = -v (v=sqrt q0)": mp.nstr(bar_even_dev(-v) * 100, 5) + " %",
        "H = -q0^2": mp.nstr(bar_even_dev(-q * q) * 100, 5) + " %",
    }

    result = {
        "A_snappy_facts": facts if have_snappy else "snappy not installed; facts skipped",
        "B_reciprocal_pairing": {
            "edge_eqn_forces_z0z1_eq_1_identically": bool(recip_exact),
            "meaning": "the two flat tetrahedra are EXACT bar-reciprocals (z↦1/z is bar); "
                       "reciprocity is deformation-invariant — NEVER broken by the coloring.",
            "revises_hypothesis": "r is NOT a reciprocal-asymmetry (that is identically 0). The "
                                  "frame is the single shape modulus z0 (partner z1=1/z0).",
        },
        "C_deformation": {
            "meridian_holonomy_map": "H(z0)=z0/(z0-1); inverse z0=H/(H-1)",
            "complete_flat": "H=-1 (parabolic) -> z0=1/2 (the flat trefoil shape)",
            "map_verified": bool(map_ok),
            "flat_bar_even_s_z0": mp.nstr(flat_bar_even, 6),      # 5/2
            "flat_bar_odd": mp.nstr(flat_bar_odd, 6),            # -3/2
            "r_order_parameter": "BAR-EVEN fractional deviation of s(z0)=z0+1/z0 from 5/2 under the "
                                 "substrate deformation of the meridian holonomy H.",
        },
        "r_is_open": {
            "value_r": "0.008652 (g2-1) — OPEN, to DERIVE from the coloring H(q0) map, NEVER to fit",
            "the_missing_derivation": "the substrate coloring meridian-holonomy↔q map H(q0)",
            "illustrative_forward_bar_even_dev_NOT_a_claim": illustrative,
            "no_fit": True,
            "anti_laundering": "no axiom/class carrying r counts as a derivation.",
        },
    }

    payload = {
        "computation": "deuteron-octahedral-gluing",
        "description": ("Deuteron octahedral gluing setup (owner task): the deuteron σ₁³ closure is "
                        "the trefoil T(2,3) — a TORUS knot (SnapPy: Vol=0, flat tetrahedra, shapes "
                        "{1/2,2}, π₁=⟨a,b|a²b³⟩). The edge gluing equation forces z₀·z₁=1 IDENTICALLY "
                        "along the whole deformation, so the two flat tetrahedra are EXACT bar-"
                        "reciprocals (reciprocity never broken) — REVISING the 'r=χ-coloring "
                        "asymmetry' first pass. The frame is the single shape modulus z₀ via the "
                        "meridian-holonomy map H(z₀)=z₀/(z₀−1) (flat H=−1⟹z₀=1/2); r is a BAR-EVEN "
                        "function of the substrate deformation of z₀. The H(q₀) coloring map is the "
                        "OPEN derivation — r is never fitted. Forward, scope-(a), audit-only, nothing "
                        "wired."),
        "audit_only": True,
        "tier": "topological setup + structural narrowing (SnapPy facts + gluing algebra; no fit)",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, residual r in the octahedral χ-coloring frame",
            "sibling_magnus": "#4158 (Route A, 2026-07-24-eunit-magnus-order2.md)",
            "sibling_octahedral": "PR #4127 (Route B, FourDilogFirstOrder.lean)",
            "sibling_borromean_front": "beans qou-h8yc (W9) / qou-099h (B3) — Borromean (hyperbolic) "
                                       "angle-structure/normal-surface; distinct manifold, shared "
                                       "gluing machinery",
            "q0_convention": "muon-canonical (computations/ layer)",
            "snappy": "3.3.2" if have_snappy else "absent",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "deuteron-octahedral-gluing", payload,
        script_path=__file__, engine="snappy+mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("reciprocal_pairing_exact", computed=str(bool(recip_exact)), expected="True")
    wb.add_assertion("meridian_map_verified", computed=str(bool(map_ok)), expected="True")
    if have_snappy:
        wb.add_assertion("deuteron_is_torus_knot_vol_zero",
                         computed=str(abs(facts["volume"]) < 1e-9), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Deuteron octahedral gluing setup (trefoil T(2,3), σ₁³) ===")
    if have_snappy:
        print(f"SnapPy: Vol={facts['volume']}, sol='{facts['solution_type']}', "
              f"tet={facts['num_tetrahedra']}, shapes={facts['shapes']}, π₁ rel={facts['relators']}")
    else:
        print("SnapPy absent — structural (gluing-algebra) facts only.")
    print(f"B. edge eqn ⟺ z₀·z₁=1 identically:  {recip_exact}   (exact bar-reciprocity, "
          f"deformation-invariant — NOT broken)")
    print(f"C. meridian map H(z₀)=z₀/(z₀−1), flat H=−1⟹z₀=1/2 verified: {map_ok}")
    print(f"   flat bar-even s=z₀+1/z₀ = {mp.nstr(flat_bar_even,4)} (=5/2), "
          f"bar-odd z₀−1/z₀ = {mp.nstr(flat_bar_odd,4)} (=−3/2)")
    print("r-order-parameter = bar-even deviation of s(z₀) under the substrate H-deformation.")
    print(f"   illustrative (NOT a claim, no fit): {illustrative}")
    print("VERDICT: frame = single shape modulus z₀ (exact reciprocal partner). r is bar-even in the "
          "H(q₀) coloring deformation — the OPEN derivation. r never fitted.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
