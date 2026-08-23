#!/usr/bin/env python3
"""The deuteron trefoil boundary-parabolic coloring: one-parameter, fully substrate-pinned, and its
deviation from flat is an EXACT bar-even square. Forward, no fit to g₂.

CHAIN (read first):
  * #4315 (merged): g₂ = the octahedral e₂ finite part in the PINCHED limit; the wall was "solve the
    trefoil coloring + pin all DOF (no fit)."
  * THIS probe removes the anti-fishing branch of that wall: the trefoil coloring is ONE-parameter
    (meridian eigenvalue m), fully pinned by the substrate m↔q₀ — no residual freedom.

WHAT THIS ESTABLISHES (all forward; the identity is exact, no observable fitted):
  A. Trefoil rep <u,v|uvu=vuv>, ρ(u)=[[m,1],[0,1/m]], ρ(v)=[[m,0],[c,1/m]]. The braid relation forces
     c(m) = -(m⁴-m²+1)/m². CROSS-CHECK: reducible c=0 ⟺ m⁴-m²+1=0 ⟺ Alexander Δ(t)=t²-t+1 roots
     m²=e^{±iπ/3}; parabolic m=1 ⟹ c=-1 (flat). One parameter m; substrate pins m↔q₀ ⇒ NO freedom.
  B. EXACT identity c(m)+1 = -(m-1/m)² — a perfect BAR-EVEN square (m-1/m bar-odd). (Lean:
     trefoilColoring_add_one.)
  C. Substrate pins (parameter-free evaluations): m=q₀ ⇒ c+1 = -(q₀-q₀⁻¹)² = -h² EXACTLY (the #4158
     bar-even gap); m=√q₀ ⇒ -(v-v⁻¹)² = -h²/[2]_v². Identifies the bar-even SCALE as h².

ANTI-FISHING (STRICT): (i) c+1=-(m-1/m)² is an EXACT identity, not a fit. (ii) The bar-even scale is
h² — but the COEFFICIENT g₂ is NOT derived here (it is the e₂ finite part, #4315). (iii) The pin's
POWER (m=q₀ vs √q₀) must be justified by the quantum-group meridian convention INDEPENDENTLY;
choosing m=q₀ *because* it gives h² would be fishing and is explicitly flagged OPEN, not claimed.
Nothing wired; anti-laundering stands.

EXPLORATORY — audit + witness only.
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
Q0_STR = "1.10997859555733471"   # muon-canonical (computations/ layer)


def main() -> int:
    # --- A. solve the rep symbolically ---
    m, c = sp.symbols("m c")
    U = sp.Matrix([[m, 1], [0, 1 / m]])
    V = sp.Matrix([[m, 0], [c, 1 / m]])
    D = (U * V * U - V * U * V).applyfunc(sp.expand)
    nz = [sp.simplify(D[i, j]) for i in range(2) for j in range(2)]
    nz = [e for e in nz if e != 0]
    c_sol = sp.solve(nz, c, dict=True)[0][c]
    c_of_m = sp.simplify(c_sol)                        # -(m⁴-m²+1)/m²
    # Alexander cross-check: reducible c=0 ⟺ m⁴-m²+1=0 ⟺ m²=e^{±iπ/3}
    red_m = sp.solve(sp.Eq(m ** 4 - m ** 2 + 1, 0), m)
    red_m2 = sorted({sp.simplify(r ** 2) for r in red_m}, key=str)
    parabolic_c = sp.simplify(c_of_m.subs(m, 1))       # -1

    # --- B. exact identity c+1 = -(m-1/m)² ---
    identity_ok = sp.simplify((c_of_m + 1) - (-(m - 1 / m) ** 2)) == 0

    # --- C. substrate pins (parameter-free) ---
    q0 = mp.mpf(Q0_STR)
    v = mp.sqrt(q0)
    h = q0 - 1 / q0
    f = sp.lambdify(m, c_of_m, "mpmath")
    dev = lambda mm: f(mm) + 1                          # = -(mm-1/mm)²
    pins = {
        "m=q0": {
            "c_plus_1": mp.nstr(dev(q0), 10),
            "equals_-h^2": bool(abs(dev(q0) - (-(h ** 2))) < mp.mpf("1e-35")),
            "note": "-(q0-q0⁻¹)² = -h² EXACTLY (the #4158 bar-even gap)",
        },
        "m=sqrt(q0)": {
            "c_plus_1": mp.nstr(dev(v), 10),
            "equals_-(v-1/v)^2": bool(abs(dev(v) - (-((v - 1 / v) ** 2))) < mp.mpf("1e-35")),
            "note": "-(v-v⁻¹)² = -h²/[2]_v²",
        },
        "m=1 (flat)": {"c_plus_1": mp.nstr(dev(mp.mpf(1)), 6), "note": "flat/parabolic rep, c=-1"},
    }

    result = {
        "A_rep": {
            "coloring_c_of_m": str(c_of_m),
            "alexander_reducible_m2": [str(x) for x in red_m2],
            "alexander_crosscheck": "reducible c=0 ⟺ m⁴-m²+1=0 ⟺ Δ(t)=t²-t+1 roots m²=e^{±iπ/3} ✓",
            "parabolic_m1_c": str(parabolic_c),
            "dof": "ONE parameter (meridian eigenvalue m); substrate pins m↔q₀ ⇒ NO residual freedom "
                   "⇒ e₂/g₂ is a FORWARD number, not a scan (resolves #4315 anti-fishing branch).",
        },
        "B_exact_bar_even_identity": {
            "identity": "c(m)+1 = -(m-1/m)²",
            "verified": bool(identity_ok),
            "parity": "(m-1/m) bar-ODD ⇒ (m-1/m)² bar-EVEN — the g₂ correction parity. Lean: "
                      "trefoilColoring_add_one.",
        },
        "C_substrate_pins": pins,
        "scope": {
            "what_is_derived": "the coloring's bar-even SCALE = h² = barOdd(q₀)² (exact identity at m=q₀).",
            "what_is_NOT": "the coefficient g₂ (=e₂ finite part, #4315) — NOT derived here.",
            "pin_power_RESOLVED": "m=q₀ is corpus-authoritative: meridian holonomy = multiplication by "
                                  "q (meridian-holonomy-boost.md; holonomy_hyperbola), trace q+q⁻¹ ⇒ "
                                  "eigenvalue m=q₀ (not √q₀). Sibling PR #4288 uses the same barOdd(q)="
                                  "q−q⁻¹ deformation for c₃. Pin fixed INDEPENDENTLY of the h² match.",
            "piece2_reduction": "g₂ = the barEven (squared-CS) face of the deformed trefoil cusp shape "
                                "(cusp-shape-bar-parity: 4₁ has barOdd(ω)²=−3; trefoil deformation has "
                                "barOdd(q₀)²=h²). Converges with sibling c₃ (barOdd/CS face) on ONE "
                                "Neumann-Zagier object. Coloring coefficient is exactly 1 (c+1=−1·h²); "
                                "g₂≈1.0087=1+r suggests leading coeff 1 + residual r (lead, not claim).",
            "anti_laundering": "the Lean proves the algebraic identity, not g₂. Nothing wired.",
        },
    }

    payload = {
        "computation": "trefoil-coloring-pinned-bareven",
        "description": ("The deuteron trefoil <u,v|uvu=vuv> boundary-parabolic coloring is ONE-"
                        "parameter (meridian eigenvalue m): the braid relation forces "
                        "c(m)=-(m⁴-m²+1)/m² (Alexander cross-check ✓; parabolic m=1⟹c=-1). Substrate "
                        "pins m↔q₀ ⇒ NO residual freedom (resolves the #4315 anti-fishing branch). "
                        "EXACT identity c(m)+1=-(m-1/m)² is a perfect BAR-EVEN square; at m=q₀ it is "
                        "-(q₀-q₀⁻¹)²=-h² EXACTLY (the #4158 bar-even gap), at m=√q₀ it is -(v-v⁻¹)². "
                        "Identifies the bar-even SCALE as h² (exact, not a fit). Does NOT derive g₂ "
                        "(=e₂ finite part); the pin's power is flagged open (not fished). scope-(a), "
                        "audit-only, nothing wired."),
        "audit_only": True,
        "tier": "rep solve + Alexander cross-check + exact bar-even identity + substrate pins; no fit",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, the trefoil coloring feeding e₂/g₂",
            "lean": "QOU/MassTheory/TrefoilColoringBarEven.lean (trefoilColoring_add_one)",
            "builds_on": "#4315 (e₂ pinched-limit wall), #4309, #4301, #4127",
            "sibling_magnus": "#4158 (h² = the bar-even gap)",
            "q0_convention": "muon-canonical (computations/ layer)",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "trefoil-coloring-pinned-bareven", payload,
        script_path=__file__, engine="sympy+mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("exact_identity_c_plus_1", computed=str(bool(identity_ok)), expected="True")
    wb.add_assertion("m_q0_gives_minus_h2", computed=str(pins["m=q0"]["equals_-h^2"]), expected="True")
    wb.add_assertion("parabolic_c_is_minus_1", computed=str(parabolic_c), expected="-1")
    out = wb.save(extra={"auditOnly": True})

    print("=== Trefoil coloring: one-parameter, substrate-pinned, exact bar-even ===")
    print(f"A. c(m) = {c_of_m}   (Alexander reducible m²={[str(x) for x in red_m2]}; parabolic m=1 ⟹ c={parabolic_c})")
    print(f"   DOF: ONE parameter m, substrate-pinned m↔q₀ ⇒ no residual freedom (forward, not a scan)")
    print(f"B. EXACT identity  c(m)+1 = -(m-1/m)²  verified: {identity_ok}   (bar-EVEN)")
    print(f"C. substrate pins (c+1 = -(m-1/m)²):")
    print(f"     m=q₀      : {pins['m=q0']['c_plus_1']}  = -h² exactly ({pins['m=q0']['equals_-h^2']})")
    print(f"     m=√q₀     : {pins['m=sqrt(q0)']['c_plus_1']}  = -(v-v⁻¹)²")
    print("VERDICT: bar-even SCALE = h² = barOdd(q₀)² (exact); pin m=q₀ corpus-RESOLVED (meridian "
          "holonomy = mult by q, #4288-consistent). g₂ COEFFICIENT open = barEven cusp-shape face / "
          "e₂ finite part (#4315), converges with sibling c₃ bar-odd face. scope-(a), no fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
