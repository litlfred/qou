#!/usr/bin/env python3
# polynomial_q_not_applicable: finite icosahedral character/rotation data + map
# tests; exact arithmetic in Q(sqrt5). No q-deformation here.
"""
Keystone geometric fibre map — step 1: is there a DERIVED, injective
irrepToRotation : {A,T₁,T₂,G,H} → icosahedral rotation, or are the Bring
H⁰(Ω¹) automorphism matrices genuinely needed?

Per docs/workplans/2026-06-20-keystone-bring-quintic-fiber-map-first-step.md.
This probe does NOT build the Bring map; it tests the two *elementary* derived
candidates the workplan ranks and reports which (if any) is injective — the
honest gate before the harder H⁰(Ω¹) computation.

DISCIPLINE: a map is admissible only if DERIVED by a uniform rule (no hand
assignment of angles to irreps). Injectivity = `five_distinct_classes`.

Candidates:
  (a) SO(3)↓I first-appearance ℓ (canonical; already in Lean icosBranchingMult)
      A@0, T₁@1, H@2, T₂@3, G@3   — T₂,G COLLIDE at ℓ=3.
  (b) argmax character over NON-identity classes, trivial↦identity (uniform rule)

Self-check: the A₅ character table is verified by row orthogonality
(Σ |class|·χ_i·χ_j = 60·δ_ij) before any map is read off it.

Exploratory; no fit, nothing wired.  Run:
  python3 -u computations/keystone_icosahedral_irrep_rotation_step1.py 2>&1 | tee /tmp/icos.log
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# --- A₅ ≅ I conjugacy classes: (label, size, rotation angle) ---------------
# angle fixed by T₁ (standard rotation rep): χ_{T₁}(θ) = 1 + 2cos θ.
CLASSES = [("1A", 1, mp.mpf(0)),                 # identity
           ("2A", 15, mp.pi),                    # order 2  -> π
           ("3A", 20, 2 * mp.pi / 3),            # order 3  -> 120°
           ("5A", 12, 2 * mp.pi / 5),            # order 5  -> 72°
           ("5B", 12, 4 * mp.pi / 5)]            # order 5  -> 144°
IRREPS = ["A", "T1", "T2", "G", "H"]


def char_table():
    """A₅ character table (rows A,T₁,T₂,G,H; cols 1A,2A,3A,5A,5B)."""
    phi = (1 + mp.sqrt(5)) / 2
    psi = (1 - mp.sqrt(5)) / 2          # = 1 - φ = -1/φ
    return {
        "A":  [mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1), mp.mpf(1)],
        "T1": [mp.mpf(3), mp.mpf(-1), mp.mpf(0), phi, psi],
        "T2": [mp.mpf(3), mp.mpf(-1), mp.mpf(0), psi, phi],
        "G":  [mp.mpf(4), mp.mpf(0), mp.mpf(1), mp.mpf(-1), mp.mpf(-1)],
        "H":  [mp.mpf(5), mp.mpf(1), mp.mpf(-1), mp.mpf(0), mp.mpf(0)],
    }


def verify_orthogonality(ct):
    sizes = [c[1] for c in CLASSES]
    ok = True
    for i in IRREPS:
        for j in IRREPS:
            s = sum(sizes[k] * ct[i][k] * ct[j][k] for k in range(5))
            expect = 60 if i == j else 0
            if abs(s - expect) > mp.mpf(10) ** -30:
                ok = False
    return ok


# SO(3)↓I first-appearance ℓ (from the in-Lean icosBranchingMult table)
FIRST_ELL = {"A": 0, "T1": 1, "H": 2, "T2": 3, "G": 3}


def main() -> int:
    set_compute_dps()
    ct = char_table()
    deg = lambda a: float(a * 180 / mp.pi)

    print("\n  KEYSTONE FIBRE MAP — STEP 1: derived irrepToRotation candidates")
    print(f"  A₅ character table orthogonality self-check: "
          f"{'PASS' if verify_orthogonality(ct) else 'FAIL'}\n")
    print("  classes (label, size, angle°):",
          ", ".join(f"{l}:{deg(a):.0f}°" for l, _, a in CLASSES), "\n")

    # --- candidate (a): first-appearance ℓ -------------------------------
    ells = {r: FIRST_ELL[r] for r in IRREPS}
    inj_a = len(set(ells.values())) == len(ells)
    print("  CANDIDATE (a) — SO(3)↓I first-appearance ℓ (canonical, in Lean):")
    print("    " + "  ".join(f"{r}→ℓ{ells[r]}" for r in IRREPS))
    print(f"    injective? {inj_a}  ({'T2,G collide at ℓ=3' if not inj_a else 'ok'})\n")

    # --- candidate (b): argmax character over non-identity classes -------
    #     uniform rule; trivial irrep (constant χ) ↦ identity (angle 0).
    mapb = {}
    for r in IRREPS:
        chi = ct[r]
        nonid = list(range(1, 5))               # exclude identity class
        if len(set(float(chi[k]) for k in nonid)) == 1:   # constant => trivial
            mapb[r] = (CLASSES[0][0], CLASSES[0][2])       # identity
        else:
            kbest = max(nonid, key=lambda k: float(chi[k]))
            mapb[r] = (CLASSES[kbest][0], CLASSES[kbest][2])
    angles_b = [mapb[r][1] for r in IRREPS]
    inj_b = len(set(round(deg(a), 6) for a in angles_b)) == len(angles_b)
    print("  CANDIDATE (b) — argmax χ over non-identity classes (trivial↦identity):")
    for r in IRREPS:
        cl, ang = mapb[r]
        print(f"    {r:2} → {cl} ({deg(ang):.0f}°)   [maxχ rule]")
    print(f"    angles = {sorted(round(deg(a)) for a in angles_b)}   injective? {inj_b}\n")

    # --- verdict ---------------------------------------------------------
    print("  ---------------------------------------------------------------")
    print("  VERDICT (step-1 gate)")
    print(f"   * (a) first-ℓ: injective={inj_a} — FAILS (T₂,G both first appear at ℓ=3);")
    print("     the SO(3)-tower level alone cannot separate the chirality-partner T₂")
    print("     from G.  A tie-break from the curve is required.")
    print(f"   * (b) argmax-χ: injective={inj_b} — a DERIVED, uniform rule yields five")
    print("     DISTINCT angles {0,72,120,144,180}°.  It separates T₁(72°)/T₂(144°)")
    print("     exactly by the φ↔1-φ Galois swap (the chirality pair), which (a) could not.")
    print("   * BUT (b) is a candidate, NOT confirmed as the Bring map: 'argmax χ' is a")
    print("     uniform rule, not yet shown to equal the H⁰(Ω¹) automorphism action.")
    print("     => Do NOT wire a BringFiberAction instance from (b) (would be the")
    print("        'arbitrary instance' the workplan guard forbids).  Next sub-step:")
    print("        compute the Σ₄ S₅-automorphism matrices on H⁰(Ω¹)≅V_(4,1), restrict")
    print("        to A₅→G, and CHECK whether the induced map equals (b).  Refute-or-confirm.\n")

    w = WitnessBuilder("keystone-icosahedral-irrep-rotation-step1", engine="python")
    w.set_description(
        "Step 1 of the keystone geometric fibre map. A₅ character table "
        "(orthogonality-verified) + the two elementary derived candidates for "
        "irrepToRotation. (a) SO(3)↓I first-ℓ FAILS injectivity (T₂,G collide at "
        "ℓ=3); (b) argmax-χ over non-identity classes gives a DERIVED injective map "
        "{0,72,120,144,180}° separating T₁/T₂ by the Galois swap. (b) is a candidate "
        "pending confirmation against the Σ₄ H⁰(Ω¹) automorphism action — not wired.")
    w.add_data("char_table_orthogonality_ok", bool(verify_orthogonality(ct)))
    w.add_data("candidate_a_first_ell", ells)
    w.add_data("candidate_a_injective", bool(inj_a))
    w.add_data("candidate_b_argmax_chi_map",
               {r: [mapb[r][0], round(deg(mapb[r][1]))] for r in IRREPS})
    w.add_data("candidate_b_injective", bool(inj_b))
    w.add_data("verdict", "first-ℓ fails (T2/G collide); argmax-χ injective but "
                          "unconfirmed vs Bring H⁰(Ω¹) — next sub-step. Not wired.")
    w.add_assertion("char_table_orthogonal", float(verify_orthogonality(ct)), 1.0,
                    source="Σ|class|χ_i χ_j = 60 δ_ij")
    w.add_assertion("first_ell_not_injective", float(not inj_a), 1.0,
                    source="T₂,G both first appear at ℓ=3")
    w.add_assertion("argmax_chi_injective", float(inj_b), 1.0,
                    source="5 distinct angles {0,72,120,144,180}°")
    w.add_caveat(
        "argmax-χ is a candidate uniform rule, NOT confirmed as the Bring-induced "
        "map. Wiring a BringFiberAction instance from it would be the 'arbitrary "
        "instance' the workplan discipline guard forbids. Confirmation requires the "
        "Σ₄ S₅-automorphism matrices on H⁰(Ω¹) (next sub-step).")
    path = w.save()
    print(f"  witness -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
