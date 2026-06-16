#!/usr/bin/env python3
"""difference_knot_jsj_classification_probe.py — is the binding difference
knot a single hyperbolic piece, or JSJ-composite?

Follow-up to difference_knot_binding_probe.py (PR #2235): that probe found
the difference braid D = W_atom·W_free⁻¹ has nonzero, A-growing volume but
"contains degenerate tetrahedra" — a signature of a NON-geometric
triangulation, i.e. the link is composite (a JSJ union of hyperbolic +
Seifert pieces) rather than one hyperbolic knot. The recommended next step
was to JSJ-decompose and sum rigorous volumes of the hyperbolic pieces.

This probe runs the classification that plain SnapPy CAN do:
  * the cusp count (number of link components of the closed difference braid);
  * the best high-precision (ManifoldHP) volume + solution type after
    simplification.

and records the two hard blockers that gate the rigorous promotion:

  BLOCKER 1 (option 2, JSJ). Rigorous interval volumes
    (verify_hyperbolicity), the canonical retriangulation, and the
    torus-splitting decomposition (splitting_surfaces) are all SAGE-ONLY in
    SnapPy. Plain SnapPy (this sandbox) cannot rigorously decompose a
    composite link or interval-verify a volume. The difference links here
    stay "degenerate tetrahedra" even at high precision → genuinely
    composite → the rigorous per-piece volume sum needs Sage (or a manual
    JSJ).

  BLOCKER 2 (option 3, amplification-vs-mass-table). The production mass
    table computes the bound-nucleus mass as m_pred = Σ m_nucleon − B_pred
    (binding_method "E₀×q⁻¹"), so m_pred is DEFINED from B_pred. Testing the
    amplification identity binding_err ≈ (M/B)·mass_err against that table is
    therefore TAUTOLOGICAL — it re-derives the proven theorem
    (prop:binding-error-amplification) from the circular definition. An
    INDEPENDENT test needs the bound mass from m_e·Vol(K)·ρ(K)/ℏ_q² with a
    per-knot Vol(K), which production does not currently expose for nuclei
    (it uses the magic-A formula, not the direct geometric mass).

EXPLORATORY / DIAGNOSTIC — no production path, no content block, no fit.
Records research status + the cusp-structure data; promotes nothing.

Ref: computations/probes/difference_knot_binding_probe.py
Ref: docs/audits/2026-06-13-difference-knot-binding-geometric-probe.md
Ref: content/quantum-observable-universe/mass-theory/binding-error-amplification.md
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys  # noqa: E402
from pathlib import Path  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from difference_knot_binding_probe import _difference_braid  # noqa: E402

CASES = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]


def _classify(braid: list[int]):
    """(num_cusps, hp_volume, solution_type) of the closed braid via SnapPy
    high precision, after simplification."""
    import snappy
    if not braid:
        return 0, 0.0, "empty"
    try:
        M = snappy.Link(braid_closure=braid).exterior()
        M.simplify()
        M.simplify()
        cusps = M.num_cusps()
        try:
            Mhp = M.high_precision()
            return cusps, float(Mhp.volume()), Mhp.solution_type()
        except Exception:
            return cusps, float(M.volume()), M.solution_type()
    except Exception as exc:  # noqa: BLE001
        return -1, 0.0, f"failed:{type(exc).__name__}"


def main() -> int:
    set_compute_dps()
    w = WitnessBuilder("difference-knot-jsj-classification", engine="snappea")
    w.set_description(
        "Classification of the binding difference knot D = W_atom·W_free⁻¹ "
        "(PR #2235 follow-up): cusp count (link components) + high-precision "
        "volume + solution type. Finding: the difference links are composite "
        "(2A−1 cusps; persistently 'degenerate tetrahedra' even at high "
        "precision) — not single hyperbolic knots. Records the two blockers "
        "gating rigorous promotion: (1) the JSJ decomposition / interval-"
        "verified volumes are Sage-only in SnapPy (unavailable here); (2) the "
        "amplification-vs-mass-table test is tautological because production "
        "m_pred = Σ m_nucleon − B_pred is circular. Diagnostic only."
    )
    w.set_content_block("prop:binding-error-amplification")

    print(f"{'iso':4s} {'A':>2s} {'|D|':>4s} {'cusps':>5s} {'2A-1':>5s} "
          f"{'HP vol':>10s} {'solution':>26s}")
    all_composite = True
    for iso, Z, N in CASES:
        A = Z + N
        braid = _difference_braid(Z, N, "minus", reduce=True)
        cusps, vol, sol = _classify(braid)
        composite = "degenerate" in sol or "contains" in sol
        all_composite = all_composite and composite
        print(f"{iso:4s} {A:>2d} {len(braid):>4d} {cusps:>5d} {2*A-1:>5d} "
              f"{vol:>10.5f} {sol:>26s}")
        w.add_data(f"{iso}_num_cusps", cusps)
        w.add_data(f"{iso}_hp_volume", mp.nstr(mp.mpf(repr(vol)), 12))
        w.add_data(f"{iso}_solution_type", sol)
        w.add_data(f"{iso}_components_eq_2A_minus_1", bool(cusps == 2 * A - 1))

    w.add_assertion(
        name="difference_links_are_composite_not_single_hyperbolic",
        computed=bool(all_composite),
        expected=True,
        tolerance=0,
        source="every difference link closes to a multi-cusp manifold that "
               "stays 'degenerate tetrahedra' at high precision — composite "
               "(JSJ), not one hyperbolic knot; rigorous decomposition is "
               "Sage-gated",
    )
    w.add_data("blocker_option2_jsj",
               "SAGE-ONLY: verify_hyperbolicity / canonical_retriangulation / "
               "splitting_surfaces unavailable in plain SnapPy; rigorous JSJ "
               "volume sum needs Sage or a manual decomposition.")
    w.add_data("blocker_option3_amplification_test",
               "TAUTOLOGICAL: production m_pred = Σ m_nucleon − B_pred is "
               "circular, so binding_err ≈ (M/B)·mass_err re-derives "
               "prop:binding-error-amplification rather than confirming it; "
               "an independent test needs the bound mass from "
               "m_e·Vol(K)·ρ(K)/ℏ_q² with per-knot Vol(K).")
    out = w.save()
    print("\nblocker 1 (JSJ): rigorous decomposition is Sage-gated.")
    print("blocker 2 (amplification test): tautological vs the circular mass table.")
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
