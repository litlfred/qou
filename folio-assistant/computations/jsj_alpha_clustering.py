#!/usr/bin/env python3
"""
α-cluster unfolding of doubly-magic atoms.

User's insight: magic / doubly-magic atoms need to be unfolded 1 or 2
levels in the jet tower.  Concretely, ⁴He is one "closed α-shell" unit
at level 0.  Heavier doubly-magic atoms are aggregates of α-clusters
at level 1 with inter-α couplings:

    ⁴He      = 1 α   = base unit (Vol = 4·8G, ρ = 2m_e)
    ⁸Be      = 2 α   + 1 α-α coupling
    ¹²C      = 3 α   + 3 α-α couplings    (Z=N=6, doubly magic)
    ¹⁶O      = 4 α   + 6 α-α couplings    (Z=N=8, doubly magic)
    ²⁰Ne     = 5 α   + 10 α-α couplings
    ...

Each α contributes B(⁴He) ≈ 28.30 MeV.  Each α-α coupling contributes
an additional coupling constant c.  Fit c from ¹²C, predict ¹⁶O, ²⁰Ne.

If the unfolded model is correct, c should be a simple knot volume
(dimensionally = m_e · Vol or 2m_e · Vol for some specific knot).
"""
from __future__ import annotations

import sys
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0

CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN = 8.0 * CATALAN_G
M_E_MEV = 0.51099895
B_4HE_AME_MEV = 28.295674

# Doubly-magic atoms (Z = N = magic number)
DOUBLY_MAGIC = [
    ("4He",  2,  2,  28.295674,  1),   # 1 α
    ("16O",  8,  8, 127.619,     4),   # 4 α
    ("40Ca", 20, 20, 342.052,   10),   # 10 α (ish)
]

# Other magic/near-magic atoms for testing
OTHER_MAGIC = [
    ("12C",  6,  6,  92.1617,  3),     # 3 α (Hoyle state)
    ("8Be",  4,  4,  56.4995,  2),     # 2 α, unstable (lifetime ~10⁻¹⁶ s)
    ("20Ne", 10, 10, 160.645,  5),     # 5 α
    ("24Mg", 12, 12, 198.257,  6),     # 6 α
]


def n_alpha_pairs(n_alpha: int) -> int:
    """Number of α-α couplings = C(n_α, 2)."""
    return n_alpha * (n_alpha - 1) // 2


def fit_coupling_from(atoms: list) -> float:
    """Fit α-α coupling constant c from: B = n_α·B(⁴He) + n_pairs·c.

    Uses weighted LSQ over the given atoms (excluding ⁴He to have a
    nontrivial equation).
    """
    eqs = []  # (n_pairs, B - n_α·B₄He)
    for name, Z, N, B, n_alpha in atoms:
        n_pairs = n_alpha_pairs(n_alpha)
        if n_pairs > 0:
            residual = B - n_alpha * B_4HE_AME_MEV
            eqs.append((n_pairs, residual))
    if not eqs:
        return 0.0
    # LSQ: minimize Σ (n_pairs·c - residual)²
    sum_n2 = sum(e[0] ** 2 for e in eqs)
    sum_nr = sum(e[0] * e[1] for e in eqs)
    return sum_nr / sum_n2 if sum_n2 else 0.0


if __name__ == "__main__":
    print("=" * 100)
    print("α-CLUSTER UNFOLDING OF DOUBLY-MAGIC ATOMS")
    print(f"  B(⁴He) = {B_4HE_AME_MEV} MeV (baseline α-cluster binding)")
    print(f"  Unfold: B(atom) = n_α · B(⁴He) + n_pairs · c_αα")
    print("=" * 100)

    # Fit c from 12C only (single equation)
    print(f"\n{'=' * 80}")
    print("FIT 1: α-α coupling c from ¹²C alone")
    print("=" * 80)
    c_from_12C = (92.1617 - 3 * B_4HE_AME_MEV) / n_alpha_pairs(3)
    print(f"  ¹²C: B = {92.1617}, n_α = 3, n_pairs = 3")
    print(f"  c_αα = (B - n_α·B₄He) / n_pairs = "
          f"({92.1617:.4f} - {3*B_4HE_AME_MEV:.4f}) / 3 = {c_from_12C:.6f} MeV")
    print(f"  In m_e units: c_αα / m_e = {c_from_12C/M_E_MEV:.4f}")
    print(f"  In 2m_e units: c_αα / 2m_e = {c_from_12C/(2*M_E_MEV):.4f}")
    print(f"  Comparison: 8G/3 = {VOL_BORROMEAN/3:.4f},  "
          f"2·8G/6 = 8G/3 = {VOL_BORROMEAN/3:.4f}")
    print(f"  Comparison: Vol(7_3 knot) ≈ 4.5921 → m_e·Vol = "
          f"{M_E_MEV*4.5921:.4f} MeV")

    print(f"\n{'=' * 80}")
    print("PREDICTIONS on other magic atoms using c_αα from ¹²C")
    print("=" * 80)
    print(f"  {'atom':>6} {'Z':>2} {'N':>2} {'n_α':>4} {'n_pairs':>8} "
          f"{'B_AME':>10} {'B_pred':>10} {'err_%':>10}")
    results = []
    all_atoms = DOUBLY_MAGIC + OTHER_MAGIC
    for name, Z, N, B_ame, n_alpha in all_atoms:
        n_pairs = n_alpha_pairs(n_alpha)
        B_pred = n_alpha * B_4HE_AME_MEV + n_pairs * c_from_12C
        err = (B_pred - B_ame) / B_ame * 100 if B_ame else float("nan")
        print(f"  {name:>6} {Z:>2} {N:>2} {n_alpha:>4} {n_pairs:>8} "
              f"{B_ame:>10.4f} {B_pred:>+10.4f} {err:>+9.3f}%")
        results.append({"atom": name, "Z": Z, "N": N, "A": Z + N,
                          "B_AME": B_ame, "n_alpha": n_alpha,
                          "n_pairs": n_pairs, "B_pred_MeV": B_pred,
                          "err_pct": err})

    # Alternative: fit c from ALL magic atoms via LSQ
    print(f"\n{'=' * 80}")
    print("FIT 2: α-α coupling c by LSQ over all magic atoms (A ≥ 8)")
    print("=" * 80)
    fit_set = OTHER_MAGIC + DOUBLY_MAGIC[1:]    # skip 4He (n_pairs=0)
    c_lsq = fit_coupling_from(fit_set)
    print(f"  c_αα (LSQ) = {c_lsq:.6f} MeV")
    print(f"  In m_e units: c_αα / m_e = {c_lsq/M_E_MEV:.4f}")

    print(f"\n  Residuals with LSQ c:")
    print(f"  {'atom':>6} {'B_AME':>10} {'B_pred':>10} {'err_%':>10}")
    for name, Z, N, B_ame, n_alpha in all_atoms:
        n_pairs = n_alpha_pairs(n_alpha)
        B_pred = n_alpha * B_4HE_AME_MEV + n_pairs * c_lsq
        err = (B_pred - B_ame) / B_ame * 100 if B_ame else float("nan")
        print(f"  {name:>6} {B_ame:>10.4f} {B_pred:>+10.4f} {err:>+9.3f}%")

    # Interpretation: is c_αα a recognizable knot volume?
    print(f"\n{'=' * 80}")
    print("INTERPRETATION: what specific knot has Vol = c_αα / ρ?")
    print("=" * 80)
    for rho_label, rho in [("m_e", M_E_MEV), ("2m_e", 2 * M_E_MEV)]:
        V_target = c_from_12C / rho
        print(f"  ρ = {rho_label} → target Vol = {V_target:.4f}")
        # Find closest census knot
        try:
            import snappy
            closest = []
            for cross_cnt in [4, 5, 6, 7]:
                for M in snappy.LinkExteriors(crossings=cross_cnt):
                    try:
                        v_raw = M.volume()
                        v = float(v_raw.real) if hasattr(v_raw, "real") else float(v_raw)
                        if abs(v - V_target) < 1.0:
                            closest.append((M.name(), v,
                                              (v - V_target) / V_target * 100))
                    except Exception:
                        pass
            closest.sort(key=lambda x: abs(x[1] - V_target))
            for n, v, e in closest[:5]:
                print(f"    {n:>12}  Vol = {v:.4f}  err {e:+.2f}%")
        except ImportError:
            pass

    witness = {
        "computation": "jsj-alpha-clustering",
        "description": (
            "Unfold doubly-magic atoms as α-cluster aggregates: "
            "B(atom) = n_α·B(⁴He) + n_pairs·c_αα.  Fit c_αα from "
            "¹²C (3 α + 3 couplings) and predict other magic atoms.  "
            "If unfolding is correct, c_αα should correspond to a "
            "specific hyperbolic knot volume, completing the picture "
            "that each binding interaction = one JSJ piece."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "B_4HE_AME_MeV": B_4HE_AME_MEV,
            "m_e_MeV": M_E_MEV,
            "Vol_Borromean_8G": VOL_BORROMEAN,
        },
        "fit_c_from_12C": {
            "c_alpha_alpha_MeV": c_from_12C,
            "c_over_m_e": c_from_12C / M_E_MEV,
            "c_over_2m_e": c_from_12C / (2 * M_E_MEV),
        },
        "predictions_from_12C_fit": results,
        "c_lsq_from_all_magic": c_lsq,
    }
    out = Path(__file__).parent / "jsj-alpha-clustering.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
