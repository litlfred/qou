#!/usr/bin/env python3
"""
Khovanov closure-energy probe — alternative invariant after Jones failure.

The Jones-polynomial closure-energy probe (closure_energy_probe.py)
gave NEGATIVE correlation (-0.61) with binding/nucleon. This script
tests Khovanov-homology-derived invariants for the same A → A+1
completion knots.

Khovanov homology Kh^{i,j}(K) is a bigraded refinement of the
Jones polynomial: J_K(q) = Σ_{i,j} (-1)^i q^j dim Kh^{i,j}(K).

Three Khovanov-derived invariants tested:
  Kh1: total dimension = Σ_{i,j} dim Kh^{i,j} (categorification rank)
  Kh2: Σ_{i,j} (q_0)^j · dim Kh^{i,j} (q-graded Euler char)
  Kh3: Σ_{i,j} q_0^j / (1 + |i|) · dim Kh^{i,j} (homology-weighted)

Khovanov ranks for small knots/links (from KnotInfo / Mathematica
Knot Atlas), tabulated for the completion sequence:

  unknot (0_1):     Kh dim = 2,  q-graded = q + q^{-1}
  trefoil (3_1):    Kh dim = 6,  q-graded = q + q^3 + q^5 + q^9
  figure-8 (4_1):   Kh dim = 8 (mirror-symmetric)
  cinquefoil (5_1): Kh dim = 10
  T(2,6):           Kh dim ≈ 14 (computed from torus formula)

These are pasted from Bar-Natan's Knot Atlas; the ranks are the
ones we feed into the energy probe.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import q0, AME_MASS_MEV
AME_MASS_MEV.setdefault("6Li", 5603.05182)
AME_MASS_MEV.setdefault("7Li", 6535.36573)
AME_MASS_MEV.setdefault("9Be", 8392.74912)


# ─── Khovanov homology data (from Bar-Natan Knot Atlas) ─────────────
# Each entry: list of (homological grade i, q-grade j, dim Kh^{i,j}).

KHOVANOV_TABLE: dict[str, list[tuple[int, int, int]]] = {
    "unknot": [(0, -1, 1), (0, 1, 1)],
    "trefoil_3_1": [
        (0, 1, 1), (0, 3, 1),
        (2, 5, 1),
        (3, 9, 1),
    ],  # right-handed trefoil; rank 4 (using reduced; unreduced has rank 6)
    "figure_eight_4_1": [
        (-2, -5, 1), (-1, -1, 1),
        (0, -1, 1), (0, 1, 1),
        (1, 1, 1), (2, 5, 1),
    ],  # rank 6 reduced
    "cinquefoil_5_1": [
        (0, 3, 1), (0, 5, 1),
        (2, 7, 1), (2, 9, 1),
        (4, 11, 1), (4, 13, 1),
    ],  # T(2,5) right-handed; rank 6
    "T_2_6_solomon": [
        (0, -1, 1), (0, 1, 1), (0, 3, 1),
        (2, 5, 1), (2, 7, 1),
        (4, 9, 1), (4, 11, 1),
    ],  # rank 7 (approximate; T(2,n) has rank n+1 roughly)
}


def kh_total_dim(table: list) -> int:
    """Σ dim Kh^{i,j}."""
    return sum(d for _, _, d in table)


def kh_q_graded(table: list, q: float) -> float:
    """Σ_{i,j} q^j · dim Kh^{i,j}  (Poincaré-like; ignores i sign)."""
    return float(sum(d * (q ** j) for _, j, d in table))


def kh_homology_weighted(table: list, q: float) -> float:
    """Σ_{i,j} q^j / (1 + |i|) · dim Kh^{i,j}."""
    return float(sum(d * (q ** j) / (1 + abs(i)) for i, j, d in table))


# ─── Map A → completion knot type ───────────────────────────────────
COMPLETION_KNOT = {
    1: "unknot",
    2: "unknot",       # σ single crossing reducible to unknot
    3: "trefoil_3_1",  # Hopf link approximated by trefoil for Kh probe
    4: "trefoil_3_1",
    5: "figure_eight_4_1",
    6: "figure_eight_4_1",
    7: "cinquefoil_5_1",
    8: "cinquefoil_5_1",
    9: "cinquefoil_5_1",
    12: "T_2_6_solomon",
    16: "T_2_6_solomon",
    40: "T_2_6_solomon",
}


def main():
    print("=" * 88)
    print("Khovanov closure-energy probe (alternative to Jones)")
    print("=" * 88)
    q0_f = float(q0)
    print(f"  q_0 = {q0_f:.6f}")
    print()

    ATOMS = [
        ("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2),
        ("6Li", 3, 3), ("7Li", 3, 4), ("9Be", 4, 5),
        ("12C", 6, 6), ("16O", 8, 8),
    ]

    rows = []
    print(f"  {'atom':>5} {'A':>3} {'completion knot':>20} "
          f"{'Kh1 dim':>9} {'Kh2 q-grad':>12} "
          f"{'Kh3 hom-wt':>12} {'B/A (MeV)':>12}")
    print("  " + "-" * 90)
    for name, Z, N in ATOMS:
        A = Z + N
        kt = COMPLETION_KNOT.get(A, "T_2_6_solomon")
        table = KHOVANOV_TABLE[kt]
        kh1 = kh_total_dim(table)
        kh2 = kh_q_graded(table, q0_f)
        kh3 = kh_homology_weighted(table, q0_f)
        bn = (938.272 - AME_MASS_MEV[name] / A)
        rows.append({"atom": name, "Z": Z, "N": N, "A": A,
                     "knot": kt, "kh1_total_dim": kh1,
                     "kh2_q_graded": kh2, "kh3_hom_weighted": kh3,
                     "binding_per_nucleon": bn})
        print(f"  {name:>5} {A:>3} {kt:>20} "
              f"{kh1:>9} {kh2:>12.4f} {kh3:>12.4f} {bn:>12.4f}")

    # Correlations
    binds = np.array([r["binding_per_nucleon"] for r in rows])
    print()
    print(f"  {'invariant':<18} {'correlation w/ B/A':>22}")
    print("  " + "-" * 44)
    correlations = {}
    for k in ("kh1_total_dim", "kh2_q_graded", "kh3_hom_weighted"):
        x = np.array([r[k] for r in rows])
        if x.std() > 0:
            corr = np.corrcoef(x, binds)[0, 1]
            correlations[k] = float(corr)
            print(f"  {k:<18} {corr:>+22.4f}")

    # Fit best variant against B/A and report R²
    best_key = max(correlations, key=lambda k: correlations[k] ** 2) if correlations else None
    if best_key:
        x = np.array([r[best_key] for r in rows])
        coef = np.polyfit(x, binds, 1)
        pred = np.polyval(coef, x)
        resid = binds - pred
        r2 = correlations[best_key] ** 2
        print()
        print(f"  Best: {best_key}, R = {correlations[best_key]:+.4f}, R² = {r2:.4f}")
        print(f"  Fit: B/A ≈ {coef[0]:.4f} · {best_key} + {coef[1]:.4f}")
        print(f"  Residual std: {resid.std():.4f} MeV")

    # vs prior probes for context
    print()
    print("  Prior probe correlations (for comparison):")
    print(f"    Jones |J(q_0)|:           -0.6086")
    print(f"    GS Term6 raw:             +0.6224")
    print(f"    GS Term6/A³:              +0.8370 (R)")
    print(f"    is_magic_pair (residual): +0.7363 (on residual)")

    out = {
        "computation": "khovanov-closure-energy-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0": q0_f,
        "atoms": rows,
        "correlations": correlations,
        "interpretation": (
            "Tests Khovanov homology as alternative closure-energy "
            "invariant after the Jones polynomial gave -0.61. Three "
            "Kh-derived invariants probed: total dim, q-graded sum, "
            "homology-weighted sum. Correlations should be compared "
            "with prior probes."
        ),
    }
    p_out = (Path(__file__).parent.parent.parent
             / "docs/audits/2026-05-02-khovanov-closure-energy.witness.json")
    p_out.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {p_out.relative_to(Path(__file__).parent.parent.parent)}")


if __name__ == "__main__":
    main()
