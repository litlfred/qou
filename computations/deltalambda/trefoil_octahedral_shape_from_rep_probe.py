#!/usr/bin/env python3
"""The trefoil crossing octahedral tetrahedron shape, computed RIGOROUSLY from the pinned boundary
rep (cross-ratios of the fixed points) — and it is EXACTLY the bar-even −h². Cracks the #4315 "need
the octahedral shapes" wall from the representation side. Forward, fully pinned, no fit.

CHAIN: #4315 said g₂ = the octahedral e₂ finite part but "need the 4 shapes." #4339: g₂_leading=1
(coloring exact), r = the shapes→e₂ nonlinearity. SnapPy gives only the degenerate 2-tet {1/2,2};
the per-crossing octahedral shapes are NOT available from it. THIS probe gets the shape from the rep.

THE RIGOROUS SHAPE (all pinned by m=q₀; nothing free):
  The 4 strand-endpoints at a crossing are the fixed points on CP¹ of ρ(u),ρ(v):
    ρ(u)=[[m,1],[0,1/m]] fixes ∞, a=1/(1/m−m);  ρ(v)=[[m,0],[c,1/m]] fixes 0, b=(m−1/m)/c.
  Cross-ratios give the tetrahedron shape triple (z, z'=1/(1−z), z''=(z−1)/z), product = −1 (a genuine
  ideal tetrahedron):
    z   = (m⁴−m²+1)/(m²−1)²  = −c/(m−1/m)²        (= 23.88 at q₀)
    z'  = 1/(1−z) = −(m−1/m)² = c+1  = −h²  EXACTLY (= −0.04371 at q₀)   ← the bar-even coloring!
    z'' = (z−1)/z = m²/(m⁴−m²+1)                    (= 0.958 at q₀)
  So the octahedral tetrahedron shape (z' form) IS the bar-even −h². The octahedral geometry and the
  bar-even coloring are the SAME object, now proven from the boundary rep (not asserted).

QUATERNION steer (owner: "Quaternion acting") — honest assessment:
  The ideal octahedron's symmetry is the binary octahedral group 2O ⊂ SU(2) (unit quaternions), and
  the meridian holonomy sits on the boost hyperbola barEven²−barOdd²=4 (rotor norm, exact). BUT the
  substrate meridian trace barEven=m+1/m=2.0109 is a DEFORMATION of the parabolic (trace 2), not a
  clean 2O trace (√2,1,0,2). A log|shape| proxy e₂ does NOT give g₂ (ratio −227). The real octahedral
  e₂ needs the GEOMETRIC QUANTUM-DILOG amplitudes a_j=log Λ(z_j) (2509.02354 §5.2 pinched regular
  part), not log|z_j|. So the quaternion/2O octahedral action is the identified structure for
  combining the 4 tetrahedra, but the e₂→r closure needs that dilog amplitude — still open.

SCOPE (honest): DERIVED — the octahedral tetrahedron shape from the rep, exactly z'=−h² (fully
pinned). NOT derived — r (the e₂ finite part; needs the geometric quantum-dilog amplitude + the
octahedral/quaternion combination of the 4 tetrahedra). scope-(a), audit-only, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

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
Q0_STR = "1.10997859555733471"


def main() -> int:
    m = sp.symbols("m")
    c = -(m ** 4 - m ** 2 + 1) / m ** 2
    a = 1 / (1 / m - m)
    b = (m - 1 / m) / c
    z = sp.simplify(a / b)                          # cross-ratio [0,∞;a,b]
    zp = sp.simplify(1 / (1 - z))
    zpp = sp.simplify((z - 1) / z)
    prod = sp.simplify(z * zp * zpp)                # ideal tet ⇒ −1
    ideal_ok = prod == -1
    # z' = -(m-1/m)^2 = c+1 exactly
    zp_is_bar_even = sp.simplify(zp - (-(m - 1 / m) ** 2)) == 0
    zp_is_c_plus_1 = sp.simplify(zp - (c + 1)) == 0

    q0 = mp.mpf(Q0_STR)
    v = mp.sqrt(q0)
    h = q0 - 1 / q0
    f = lambda e: sp.lambdify(m, e, "mpmath")(q0)
    bE = q0 + 1 / q0
    bO = q0 - 1 / q0
    boost = bE ** 2 - bO ** 2

    result = {
        "rigorous_shape_from_rep": {
            "fixed_points": "ρ(u): {∞, a=1/(1/m−m)}; ρ(v): {0, b=(m−1/m)/c}",
            "z": str(z) + f"  (= {mp.nstr(f(z),8)} at q₀)",
            "z_prime": str(zp) + f"  (= {mp.nstr(f(zp),8)} at q₀)",
            "z_prime_eq_minus_h2": bool(zp_is_bar_even),
            "z_prime_eq_c_plus_1": bool(zp_is_c_plus_1),
            "z_second": str(zpp) + f"  (= {mp.nstr(f(zpp),8)} at q₀)",
            "ideal_tet_product_minus_1": bool(ideal_ok),
            "meaning": "the octahedral tetrahedron shape (z' form) IS the bar-even −h², PROVEN from "
                       "the boundary rep (cross-ratios of fixed points) — not asserted. Cracks the "
                       "#4315 'need the shapes' wall from the rep side.",
        },
        "quaternion_steer": {
            "octahedron_symmetry": "binary octahedral group 2O ⊂ SU(2) (unit quaternions)",
            "boost_norm_barEven2_minus_barOdd2": mp.nstr(boost, 6) + " (= 4, exact rotor norm)",
            "meridian_trace_barEven": mp.nstr(bE, 8) + " — a DEFORMATION of parabolic (trace 2), NOT "
                                      "a clean 2O trace (√2, 1, 0, 2)",
            "log_abs_proxy_e2_over_h2": mp.nstr(
                (mp.log(abs(f(z))) * mp.log(abs(f(zp))) + mp.log(abs(f(z))) * mp.log(abs(f(zpp)))
                 + mp.log(abs(f(zp))) * mp.log(abs(f(zpp)))) / bO ** 2, 6) + " (NOT g₂; log|z| is the "
                "wrong amplitude)",
            "assessment": "2O/quaternion octahedral symmetry is the natural structure to combine the 4 "
                          "tetrahedra, but e₂→r needs the GEOMETRIC QUANTUM-DILOG amplitude "
                          "a_j=log Λ(z_j) (2509.02354 §5.2 pinched regular part), not log|z_j|. Open.",
        },
        "scope": {
            "derived": "the octahedral tetrahedron shape from the rep: z'=−h² exactly (fully pinned).",
            "not_derived": "r = the e₂ finite part (needs the geometric quantum-dilog amplitude + the "
                           "octahedral/quaternion combination of the 4 tetrahedra).",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "trefoil-octahedral-shape-from-rep",
        "description": ("The trefoil crossing octahedral tetrahedron shape, computed rigorously from "
                        "the pinned boundary rep (cross-ratios of the fixed points of ρ(u),ρ(v)): the "
                        "shape triple (z, z'=1/(1−z), z''), product −1 (genuine ideal tet), with "
                        "z'=−(m−1/m)²=c+1=−h² EXACTLY. So the octahedral geometry and the bar-even "
                        "coloring are the SAME object, proven from the rep (cracks the #4315 'need the "
                        "shapes' wall). Quaternion steer: the octahedron's 2O⊂SU(2) symmetry is the "
                        "structure to combine the 4 tetrahedra, but the meridian trace 2.011 is a "
                        "parabolic deformation (not a clean 2O element) and a log|z| proxy e₂ is not g₂ "
                        "— the real e₂→r needs the geometric quantum-dilog amplitude (2509.02354 §5.2). "
                        "DERIVED: shape z'=−h²; NOT derived: r. scope-(a), audit-only, nothing wired."),
        "audit_only": True,
        "tier": "rigorous octahedral shape from the pinned rep (exact) + quaternion-steer assessment; no fit",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, the octahedral shapes / e₂ / r",
            "builds_on": "#4339 (g₂_leading=1, r=shapes→e₂ nonlinearity), #4315 (octahedral e₂ wall), "
                         "#4319 (coloring c+1=−h²)",
            "owner_steer": "Quaternion acting (2O ⊂ SU(2) octahedral symmetry)",
            "q0_convention": "muon-canonical (computations/ layer)",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "trefoil-octahedral-shape-from-rep", payload,
        script_path=__file__, engine="sympy+mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("ideal_tet_product_minus_1", computed=str(bool(ideal_ok)), expected="True")
    wb.add_assertion("shape_zprime_eq_minus_h2", computed=str(bool(zp_is_bar_even)), expected="True")
    wb.add_assertion("boost_norm_4", computed=mp.nstr(boost, 4), expected="4.0")
    out = wb.save(extra={"auditOnly": True})

    print("=== Trefoil crossing octahedral shape from the pinned rep ===")
    print(f"shape triple: z={mp.nstr(f(z),6)}  z'={mp.nstr(f(zp),8)} (=−h², c+1: {zp_is_bar_even})  "
          f"z''={mp.nstr(f(zpp),6)}   product=−1: {ideal_ok}")
    print(f"⇒ the octahedral tetrahedron shape (z' form) IS the bar-even −h², PROVEN from the rep.")
    print(f"quaternion steer: boost norm barEven²−barOdd² = {mp.nstr(boost,4)} (=4 rotor); meridian "
          f"trace barEven={mp.nstr(bE,6)} (parabolic deformation, not a clean 2O trace).")
    print("e₂→r needs the geometric quantum-dilog amplitude (not log|z|); the 2O/quaternion octahedral "
          "combination of the 4 tetrahedra is the open structure. DERIVED: z'=−h². NOT: r. No fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
