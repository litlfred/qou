#!/usr/bin/env python3
"""
Compound β-decay calibration for shell y_target values.

Principle (prop:compound-beta-shell-calibration):
  y_target(A_magic) is DERIVED, not calibrated, from β-decay Q-values
  across each magic shell boundary.

  y_target(A_magic) = Q_β(compound decay) / (E_0 · A_magic · m_p)

Where:
  - Q_β = Q-value of a β-decay that crosses the magic shell
  - E_0 = 0.782 MeV (free-neutron β-decay Q-value)
  - m_p = 938.272 MeV (proton mass)

Single archimedean input: E_0. All other values from AME (β-decay Q).
"""
import json
from pathlib import Path
from datetime import datetime, timezone


# β-decay Q-values (MeV) — AME 2020 / experimental
COMPOUND_BETA_DECAYS = [
    # (A_magic, parent → daughter, Q_MeV, description)
    (2,   "3H → 3He",    0.01859, "Tritium β⁻ (crosses N=2)"),
    (8,   "14C → 14N",   0.15648, "¹⁴C β⁻ (crosses N=8)"),
    (20,  "40K → 40Ca",  1.31100, "⁴⁰K β⁻ (crosses Z=20, N=20 double)"),
    (28,  "56Mn → 56Fe", 3.69500, "⁵⁶Mn β⁻ (near Z=N=28)"),
    (50,  "120Ag → 120Cd", 8.00000, "¹²⁰Ag β⁻ (crosses Z=50)"),
    (82,  "210Bi → 210Po", 1.16300, "²¹⁰Bi β⁻ (crosses Z=82)"),
    (126, "209Pb → 209Bi", 0.64400, "²⁰⁹Pb β⁻ (crosses N=126 anchor)"),
]

from experimental_constants import Q_NEUTRON_MEV, M_P_MEV
E_0_BETA_MeV = float(Q_NEUTRON_MEV)  # 0.78233341 MeV (CODATA-derived)
m_p_MeV = float(M_P_MEV)              # 938.27208816 MeV


def y_target(A_magic, Q_beta_MeV):
    """y_target(A_magic) from compound β-decay Q-value.

    y_target = Q_β / (E_0 · A_magic · m_p)
    """
    return Q_beta_MeV / (E_0_BETA_MeV * A_magic * m_p_MeV)


if __name__ == "__main__":
    print("COMPOUND β-DECAY → y_target(A_magic) derivation")
    print("=" * 88)
    print(f"E_0 (β, free neutron) = {E_0_BETA_MeV} MeV")
    print(f"m_p = {m_p_MeV} MeV")
    print()
    print(f"  {'A_magic':>8} {'β-decay':>16} {'Q (MeV)':>10} "
          f"{'y_target(A_m)':>15} {'B_AME/(A·m_p)':>16}")
    print("  " + "-" * 82)

    # Also compare to B_AME/(A·m_p) for the anchor atom
    ANCHOR_B_AME = {
        2: ("4He", 4, 28.30),         # A_m=2 → use 4He (N=2 magic)
        8: ("16O", 16, 127.62),       # A_m=8 → 16O (Z=N=8 double)
        20: ("40Ca", 40, 342.05),     # A_m=20 → 40Ca (Z=N=20 double)
        28: ("56Ni", 56, 483.99),     # A_m=28 → ⁵⁶Ni (Z=28)
        50: ("120Sn", 120, 1020.55),  # A_m=50 → ¹²⁰Sn (Z=50)
        82: ("208Pb", 208, 1636.45),  # A_m=82 → ²⁰⁸Pb (Z=82, N=126)
    }

    results = []
    for A_m, decay, Q_mev, desc in COMPOUND_BETA_DECAYS:
        y = y_target(A_m, Q_mev)
        anchor = ANCHOR_B_AME.get(A_m)
        if anchor:
            name, A_anchor, B_ame = anchor
            B_per_rest = B_ame / (A_anchor * m_p_MeV)
        else:
            name, A_anchor, B_ame, B_per_rest = None, None, None, None
        print(f"  {A_m:>8d} {decay:>16} {Q_mev:>10.5f} "
              f"{y:>15.6e} "
              f"{B_per_rest if B_per_rest else 'N/A':>16}")
        results.append({
            "A_magic": A_m,
            "beta_decay": decay,
            "Q_MeV": Q_mev,
            "description": desc,
            "y_target": y,
            "anchor_atom": name,
            "anchor_A": A_anchor,
            "anchor_B_AME": B_ame,
            "anchor_B_over_rest": B_per_rest,
            "ratio_y_to_B_over_rest": y / B_per_rest if B_per_rest else None,
        })

    # Key observation: how does y_target compare to B_AME/(A·m_p)?
    print()
    print("Ratio y_target / (B_AME/(A·m_p)) — closer to 1 is better:")
    print(f"  {'A_magic':>8} {'anchor':>6} {'y_target':>12} "
          f"{'B/M':>12} {'ratio':>8}")
    print("  " + "-" * 60)
    for r in results:
        if r["ratio_y_to_B_over_rest"] is not None:
            print(f"  {r['A_magic']:>8d} {r['anchor_atom']:>6} "
                  f"{r['y_target']:>12.6e} {r['anchor_B_over_rest']:>12.6e} "
                  f"{r['ratio_y_to_B_over_rest']:>8.4f}")

    witness = {
        "computation": "compound-beta-shell-calibration",
        "description": (
            "y_target(A_magic) derivation from compound β-decay Q-values. "
            "Single archimedean input: E_0 = 0.782 MeV (free-neutron "
            "β-decay). For each magic A, find a representative compound "
            "β-decay crossing that shell and compute y_target from Q/"
            "(E_0·A_magic·m_p)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"E_0_MeV": E_0_BETA_MeV, "m_p_MeV": m_p_MeV},
        "results": results,
    }
    out = Path(__file__).parent / "compound-beta-shell.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
