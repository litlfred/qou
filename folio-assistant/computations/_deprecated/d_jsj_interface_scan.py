#!/usr/bin/env python3
"""
D's JSJ interface: scan braid patterns for the inter-nucleon piece.

Per the JSJ decomposition picture:
  atomic link(D) = [proton Borromean] U [neutron Borromean] U [interface piece]

with proton/neutron each = (σ_0 σ_1⁻¹)^3 on their own 3 strands (Vol 8G).
The inter-piece Vol is what should equal B_AME(D)/m_e = 4.3533 if
rho_F = m_e.

This probe sweeps inter-nucleon braid-word patterns and computes the
closure's total Vol, reporting excess over 2·8G = 14.655 as the
"interface Vol".
"""
from __future__ import annotations

import sys
import json
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

import snappy

B_D_AME = 2.22456612
M_E = 0.51099895
TARGET = B_D_AME / M_E   # 4.3533...
TWO_BORROMEAN = 14.65545  # 2 * 8G

PROTON = [1, -2, 1, -2, 1, -2]   # (σ_0 σ_1⁻¹)^3 on strands [1-3]
NEUTRON = [4, -5, 4, -5, 4, -5]  # (σ_3 σ_4⁻¹)^3 on strands [4-6]


INTER_PATTERNS = [
    ("sigma_3",                      [3]),
    ("sigma_3 * 2",                  [3, 3]),
    ("sigma_3 * 3",                  [3, 3, 3]),
    ("sigma_2 sigma_3 sigma_4",      [2, 3, 4]),
    ("sigma_4 sigma_3 sigma_2",      [4, 3, 2]),
    ("sigma_3 sigma_2 sigma_3 sigma_4 sigma_3", [3, 2, 3, 4, 3]),
    ("sigma_3 sigma_2^-1 sigma_3 sigma_4^-1 sigma_3", [3, -2, 3, -4, 3]),
    ("sigma_2 sigma_3 sigma_3 sigma_2", [2, 3, 3, 2]),
    ("sigma_2 sigma_3^-1 sigma_2",   [2, -3, 2]),
    ("sigma_2 sigma_3^-1",           [2, -3]),
    ("sigma_3 sigma_4^-1 sigma_3",   [3, -4, 3]),
    ("sigma_3 sigma_2 sigma_3^-1 sigma_4 sigma_3", [3, 2, -3, 4, 3]),
    ("sigma_2 sigma_3^-1 sigma_2 sigma_4^-1 sigma_3", [2, -3, 2, -4, 3]),
    ("sigma_2 sigma_3^-1 sigma_4^-1 sigma_2 sigma_3", [2, -3, -4, 2, 3]),
    ("sigma_2 sigma_4 (disjoint)",   [2, 4]),
    ("sigma_3 sigma_3^-1 sigma_3",   [3, -3, 3]),
]


def main() -> int:
    print(f"  target (B_AME/m_e) = {TARGET:.6f}")
    print(f"  2*Borromean base   = {TWO_BORROMEAN:.6f}")
    print()
    print(f"  {'pattern':<48} {'|K|':>4} {'comps':>5} "
          f"{'Vol':>12} {'excess':>10} {'err %':>10}")
    print("  " + "-" * 96)

    results = []
    for name, inter in INTER_PATTERNS:
        word = PROTON + inter + NEUTRON
        try:
            L = snappy.Link(braid_closure=word)
            E = L.exterior()
            v = float(E.volume())
        except Exception as e:
            print(f"  {name:<48} error: {str(e)[:50]}")
            continue
        excess = v - TWO_BORROMEAN
        err = (excess - TARGET) / TARGET * 100 if excess > 0.01 else None
        comps = len(L.link_components)
        err_str = f"{err:>+9.3f}%" if err is not None else "     —    "
        print(f"  {name:<48} {len(word):>4} {comps:>5} "
              f"{v:>12.6f} {excess:>+10.6f} {err_str}")
        results.append({
            "inter_pattern": name,
            "inter_word": inter,
            "full_braid": word,
            "n_components": comps,
            "vol_total": v,
            "vol_excess": excess,
            "err_pct": err,
        })

    # Find best
    best = min((r for r in results if r["vol_excess"] > 0),
                 key=lambda r: abs(r["err_pct"]) if r["err_pct"] is not None
                 else float("inf"))
    print(f"\n  Best: '{best['inter_pattern']}' with excess "
          f"{best['vol_excess']:.6f}, err {best['err_pct']:+.3f}%")
    print(f"  B_pred = m_e · {best['vol_excess']:.6f} = "
          f"{M_E * best['vol_excess']:.6f} MeV  (AME: {B_D_AME})")

    witness = {
        "computation": "d-jsj-interface-scan",
        "description": (
            "Scan inter-nucleon braid-word patterns for D's JSJ "
            "interface piece.  Target Vol = B_AME/m_e = 4.3533.  "
            "Excess over 2*Borromean is the interface contribution."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "target_vol": TARGET,
        "two_borromean": TWO_BORROMEAN,
        "B_AME_D": B_D_AME,
        "patterns": results,
        "best": best,
    }
    out = Path(__file__).parent / "d-jsj-interface-scan.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
