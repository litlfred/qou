#!/usr/bin/env python3
"""The geometric quantum-dilog amplitude on the pinned octahedral shape z'=−h²: the semiclassical
dilog confirms g₂~1's SCALE (order-1) but the exact r needs the geometric regular part + the full
4-shape octahedron. The honest research frontier. ONE principled evaluation; NO dilog-variant scan.

CHAIN: #4345 got the octahedral tetrahedron shape from the pinned rep: z'=−(m−1/m)²=−h² exactly.
#4339: g₂=1+r, leading 1 exact (real coloring), r = the shapes→e₂ nonlinearity. This probe evaluates
the principled semiclassical amplitude on that shape and reports the honest state.

THE ONE PRINCIPLED EVALUATION (no scan): the semiclassical amplitude of a tetrahedron of shape z in
the octahedral state integral is the dilogarithm Li₂(z) (the saddle of the geometric quantum dilog).
Evaluate ONCE on z'=−h²:
  Li₂(z')/z' = 0.9893  (order-1 — confirms g₂~1's SCALE)
  leading nonlinearity Li₂(z)/z ≈ 1 + z/4 = 1 − h²/4 = 0.9891  (dilog gives −1.07%)
But g₂ − 1 = r = +0.87% (opposite sign, different magnitude). So the naive semiclassical Li₂ is NOT r.

WHY (honest wall): the exact r needs
  (i) the GEOMETRIC quantum-dilog regular part (2509.02354 §5.2, the pinched limit — NOT the naive
      Li₂ saddle; the pinched regularization has its own finite part), and
  (ii) ALL FOUR octahedral tetrahedron shapes (z_r,z_t,z_l,z_b) — this probe has ONE (z'); the other
      three need the octahedron's apex data (P±), i.e. the per-crossing octahedral developing map.
Trying different dilog forms (Li₂ vs Rogers vs Bloch–Wigner) or shapes to hit 1.00865 is the §2e
FORBIDDEN SCAN — explicitly NOT done. This probe reports the honest frontier, not a fit.

NET (whole g₂ chain, honest): g₂ = 1 + r. DERIVED: g₂_leading = 1 (exact); the octahedral shape
carrying the bar-even structure = −h² (from the rep); the amplitude is dilog(shape), order-1
(g₂~1 scale confirmed). NOT derived: the exact r = +0.87% — needs the geometric §5.2 regular part +
the 4-shape octahedron. A single, well-posed, non-fishing research object. scope-(a), audit-only,
nothing wired.
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
Q0_STR = "1.10997859555733471"


def main() -> int:
    q0 = mp.mpf(Q0_STR)
    h2 = (q0 - 1 / q0) ** 2
    zp = -h2                                # pinned octahedral shape z' = -h^2 (#4345)

    Li2 = mp.polylog(2, zp)                 # THE one principled evaluation (no scan)
    ratio = Li2 / zp                        # semiclassical amplitude / shape (order-1)
    lead_nonlin = 1 + zp / 4                # Li2(z)/z ~ 1 + z/4 = 1 - h^2/4
    r_target = mp.mpf("1.00865") - 1        # +0.00865
    dilog_nonlin = ratio - 1                # ~ -0.0107 (wrong sign vs r)

    result = {
        "pinned_shape": {"z_prime": mp.nstr(zp, 8), "equals": "-(m-1/m)^2 = -h^2 (from the rep, #4345)"},
        "one_principled_evaluation": {
            "amplitude": "Li₂(z) — the octahedral state-integral saddle (semiclassical)",
            "Li2_zprime": mp.nstr(Li2, 10),
            "Li2_over_zprime": mp.nstr(ratio, 8) + " (ORDER 1 — confirms g₂~1's SCALE)",
            "leading_nonlinearity": mp.nstr(lead_nonlin, 8) + " (= 1 - h²/4)",
            "no_scan": "ONE evaluation of the principled amplitude; dilog variants NOT scanned (§2e).",
        },
        "honest_comparison": {
            "g2_minus_1_r": mp.nstr(r_target, 4) + " (+0.87%)",
            "dilog_nonlinearity": mp.nstr(dilog_nonlin, 4) + " (~ -1.07%)",
            "verdict": "the naive semiclassical Li₂ nonlinearity is NOT r — opposite sign, different "
                       "magnitude. g₂~1's SCALE is confirmed (order-1); the exact r is not the naive dilog.",
        },
        "the_wall": {
            "needs_i": "the GEOMETRIC quantum-dilog regular part (2509.02354 §5.2 pinched limit) — its "
                       "finite part, not the naive Li₂ saddle.",
            "needs_ii": "ALL FOUR octahedral shapes (z_r,z_t,z_l,z_b); this probe has ONE (z'); the "
                        "other three need the octahedron apex data (P±) / per-crossing developing map.",
            "forbidden": "scanning dilog forms or shapes to hit 1.00865 is the §2e forbidden fit — NOT done.",
        },
        "net": {
            "derived": "g₂_leading=1 (exact); octahedral shape = −h² (from rep); amplitude=dilog(shape), "
                       "order-1 (g₂~1 scale confirmed).",
            "not_derived": "exact r=+0.87% (geometric §5.2 regular part + 4-shape octahedron).",
            "status": "a single, well-posed, non-fishing research object — the honest frontier.",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "geometric-qdilog-amplitude-r-frontier",
        "description": ("The geometric quantum-dilog amplitude on the pinned octahedral shape z'=−h² "
                        "(#4345): ONE principled evaluation Li₂(z')/z'=0.989 is ORDER-1, confirming "
                        "g₂~1's SCALE, but the naive dilog nonlinearity (−1.07%) is NOT r (+0.87%; "
                        "opposite sign). The exact r needs (i) the GEOMETRIC quantum-dilog regular part "
                        "(2509.02354 §5.2 pinched finite part, not the naive Li₂ saddle) and (ii) all 4 "
                        "octahedral shapes (apex data; this has 1). Scanning dilog forms/shapes to hit "
                        "1.00865 is the forbidden §2e fit — NOT done. DERIVED: g₂_leading=1, shape=−h², "
                        "amplitude order-1. NOT derived: exact r. The honest research frontier. "
                        "scope-(a), audit-only, nothing wired."),
        "audit_only": True,
        "tier": "one principled semiclassical evaluation + honest frontier (no scan, no fit)",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, the exact r (geometric quantum-dilog amplitude)",
            "builds_on": "#4345 (shape=−h² from rep), #4339 (g₂_leading=1), #4315 (octahedral e₂)",
            "the_open_object": "geometric quantum-dilog regular part (2509.02354 §5.2) on the 4-shape octahedron",
            "q0_convention": "muon-canonical (computations/ layer)",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "geometric-qdilog-amplitude-r-frontier", payload,
        script_path=__file__, engine="mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("Li2_amplitude_order_1", computed=str(bool(abs(ratio - 1) < mp.mpf("0.05"))), expected="True")
    wb.add_assertion("dilog_nonlin_is_not_r",
                     computed=str(bool(abs(dilog_nonlin - r_target) > mp.mpf("0.01"))), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Geometric quantum-dilog amplitude on z'=−h² — the honest frontier ===")
    print(f"pinned shape z' = −h² = {mp.nstr(zp,8)}")
    print(f"ONE principled evaluation: Li₂(z')/z' = {mp.nstr(ratio,6)} (ORDER-1 ⇒ g₂~1 SCALE confirmed)")
    print(f"dilog nonlinearity = {mp.nstr(dilog_nonlin,4)} (~-1.07%)  vs  r = g₂−1 = {mp.nstr(r_target,4)} (+0.87%)")
    print("⇒ the naive semiclassical Li₂ is NOT r (opposite sign). Exact r needs the GEOMETRIC §5.2 "
          "regular part + all 4 octahedral shapes (apex data; have 1). NO dilog-variant scan (forbidden).")
    print("NET: g₂=1+r; DERIVED g₂_leading=1, shape=−h², amplitude order-1; NOT derived exact r. Frontier.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
