#!/usr/bin/env python3
"""R&D 4 Exploration: find a specific knot/link K_p with
  Vol(K_p) ≈ 1836.15 · ℏ_q² ≈ 18.03

so that `m_p/m_e = Vol(K_p)/ℏ_q²` directly (no λ_scale, no Skein).

Strategy:

1. Tabulate hyperbolic volumes of standard small-volume building
   blocks (ideal tetrahedron, octahedron, figure-8, Whitehead,
   Borromean, etc.) and their linear combinations.

2. Identify what additive/multiplicative combinations of standard
   volumes can produce 18.03.

3. Check whether any natural categorical-braid construction
   (e.g., 9-strand canonical proton braid, dressed Borromean)
   has a known volume in this range.

4. Test the SAME approach for neutron (m_n/m_e · ℏ_q² ≈ 18.07)
   and for second-generation baryons (Σ, Λ).

Key constraint: Vol must be a topological invariant of the
COMPLEMENT of a hyperbolic 3-manifold; not all 3-manifolds are
hyperbolic.

Cross-check: at q=1 (classical limit), the formula reduces to
m_p/m_e = Vol(K_p) / ℏ_q²|_{q=1} but ℏ_q² → 0 as q → 1, making
the limit singular. This SUGGESTS the formula needs a
q-deformation of Vol or a different normalisation entirely.
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json, sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, M_P_MEV

mp.mp.dps = 80
Q = mp.mpf(Q_50_DIGIT_STR)
HBAR = (Q - 1) / Q
G = mp.catalan

# Standard hyperbolic 3-manifold volumes
V_TET = 2 * mp.im(mp.polylog(2, mp.exp(mp.mpc(0, mp.pi/3))))  # = 2·Cl_2(π/3) ≈ 1.0149
V_OCT = 4 * G  # = 8·Λ(π/4) ≈ 3.6639 (octahedral)
VOL_4_1 = V_OCT / 2 * (2)  # figure-8 = 2·V_tet ≈ 2.0299
# Better: VOL_4_1 = 2.029883...
VOL_4_1 = 2 * V_TET
VOL_B3 = 2 * V_OCT  # Borromean = 2 ideal octahedra ≈ 7.3277
VOL_5_2 = mp.mpf("2.82812208833")
VOL_6_1 = mp.mpf("3.16396322648")
VOL_6_2 = mp.mpf("4.40083251217")
VOL_6_3 = mp.mpf("5.69302109614")
VOL_7_4 = mp.mpf("5.13794120982")
VOL_8_1 = mp.mpf("3.42720252426")  # Whitehead link
VOL_BRINGS = mp.mpf("28.5783194")  # Bring's surface volume (approx, 5-cusped)

# m_p / m_e target
M_E_VAL = mp.mpf(repr(M_E_MEV))
M_P_VAL = mp.mpf(repr(M_P_MEV))
M_P_OVER_ME = M_P_VAL / M_E_VAL
VOL_K_P_TARGET = M_P_OVER_ME * HBAR**2


def main() -> int:
    w = WitnessBuilder("lambda-scale-rd4-k-p-search", engine="mpmath")
    w.set_description(
        "R&D 4 exploration: search for a specific knot/link K_p with "
        "Vol(K_p) = m_p/m_e · ℏ_q² ≈ 18.03, eliminating the λ_scale "
        "fudge factor from the Borromean baryon mass formula."
    )
    w.set_content_block("conj:borromean-baryon-mass-formula")
    w.add_parameter("dps", 80)

    print(f"Target Vol(K_p) = m_p/m_e · ℏ_q² = {mp.nstr(VOL_K_P_TARGET, 15)}")
    print(f"  m_p/m_e (CODATA): {float(M_P_OVER_ME):.6f}")
    print(f"  ℏ_q² at q_0:      {float(HBAR**2):.10f}")
    print()

    # Standard building blocks
    blocks = {
        "V_tetrahedron":     V_TET,
        "V_octahedron":      V_OCT,
        "Vol(4_1)":          VOL_4_1,
        "Vol(5_2)":          VOL_5_2,
        "Vol(6_1)":          VOL_6_1,
        "Vol(6_2)":          VOL_6_2,
        "Vol(6_3)":          VOL_6_3,
        "Vol(7_4)":          VOL_7_4,
        "Vol(L_Whitehead)":  VOL_8_1,
        "Vol(B_3)":          VOL_B3,
    }
    print("Standard hyperbolic volumes:")
    for name, v in blocks.items():
        print(f"  {name:25s} = {float(v):.6f}")
    print()

    # Integer combinations
    print("Integer combinations matching 18.03:")
    print(f"  {'combination':30s}  {'value':>10s}  {'rel err':>10s}")
    for name, v in blocks.items():
        for k in range(1, 30):
            test = k * v
            if abs(test - VOL_K_P_TARGET) < 0.5:
                rel = float((test - VOL_K_P_TARGET) / VOL_K_P_TARGET)
                print(f"  {k} · {name:25s}  {float(test):>10.4f}  {rel:>+10.4f}")
    print()

    # Pair sums
    print("Pair sums:")
    names = list(blocks.keys())
    pair_matches = []
    for i, n1 in enumerate(names):
        for j, n2 in enumerate(names):
            if j < i: continue
            v1 = blocks[n1]
            v2 = blocks[n2]
            for a in range(0, 6):
                for b in range(0, 6):
                    if a == 0 and b == 0: continue
                    test = a*v1 + b*v2
                    if abs(test - VOL_K_P_TARGET) < 0.1:
                        rel = float((test - VOL_K_P_TARGET) / VOL_K_P_TARGET)
                        pair_matches.append((f"{a}·{n1} + {b}·{n2}", float(test), rel))
    pair_matches.sort(key=lambda x: abs(x[2]))
    for desc, val, rel in pair_matches[:8]:
        print(f"  {desc:50s} = {val:.4f}  (rel {rel:+.4e})")
    print()

    # Check q-deformed Vol candidates
    print("q-deformed Vol candidates (Vol · f(q)):")
    candidates_qdef = {
        "Vol(B_3) · 5/2": VOL_B3 * mp.mpf(5)/2,
        "Vol(B_3) · [2]_q^2/2": VOL_B3 * (Q + 1/Q)**2 / 2,
        "Vol(4_1) · 9": VOL_4_1 * 9,
        "Vol(4_1) · [3]_q²": VOL_4_1 * (Q**2 + 1 + 1/Q**2)**2,
        "Vol(B_3) · (5/2 + 3h²/4)": VOL_B3 * (mp.mpf(5)/2 + 3*(Q-1/Q)**2/4),
        "Vol(B_3) · (1/4) Σ dim_q V_λ at H_4": VOL_B3 * (3*Q**2 + 4 + 3/Q**2)/4,
        "Vol(L6a4)·[2]_q^2": VOL_B3 * (Q + 1/Q)**2,
    }
    for name, val in candidates_qdef.items():
        rel = float((val - VOL_K_P_TARGET) / VOL_K_P_TARGET)
        marker = " *MATCH*" if abs(rel) < 1e-3 else ""
        print(f"  {name:45s} = {float(val):>10.4f}  (rel {rel:+.4e}){marker}")
    print()

    # The decisive structural test: if any combination gives Vol_K_p to
    # within 1 ppm structurally, that's the answer.
    print("Looking for structural matches at 1 ppm precision:")
    matches_strict = []
    for name, val in {**blocks, **candidates_qdef}.items():
        rel = float(abs(val - VOL_K_P_TARGET) / VOL_K_P_TARGET)
        if rel < 1e-5:
            matches_strict.append((name, val, rel))
    if matches_strict:
        for n, v, r in matches_strict:
            print(f"  {n}: rel err {r:.2e}")
    else:
        print("  None within 1 ppm. The empirical Vol(K_p)=18.03 is not")
        print("  reproduced by simple combinations of standard small-volume blocks.")
    print()

    # Conclusion
    w.add_data("Vol_K_p_target", float(VOL_K_P_TARGET))
    w.add_data("standard_blocks", {k: float(v) for k, v in blocks.items()})
    w.add_data("best_pair_matches", [
        {"combo": d, "val": v, "rel_err": r} for d, v, r in pair_matches[:5]
    ])
    w.add_data("conclusion", (
        "No integer combination of standard small-volume hyperbolic "
        "3-manifolds matches Vol(K_p) = 18.03 to 1 ppm. The closest "
        "candidates (9·Vol(4_1) = 18.27, 5·V_oct = 18.32) are off by "
        "~1%. q-deformed Vol candidates including the Family A factor "
        "Vol(B_3)·(5/2 + 3h²/4) match λ_p's q-rational form but not "
        "the CODATA target exactly. The Borromean baryon mass formula's "
        "structural status remains conjectural; foundational paper-"
        "level work needed."
    ))

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
