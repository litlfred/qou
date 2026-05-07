#!/usr/bin/env python3
"""
A.3 v2 — shell-aware level-1 jet correction.

Builds on `per_braid_tower_hybrid.py` (level-0 hybrid: q-Hecke
descended + q=1 MN tower). Per the cal/m_e structure audit
([2026-05-02-cal-spread-structure.md](../../docs/audits/2026-05-02-cal-spread-structure.md)):

- The level-0 cal/m_e follows a clean log(A) trend
  ($\\approx 0.993 - 0.0033 \\cdot \\log A$).
- 4He is a -3458 ppm outlier (doubly-magic).
- The structural distinguishing feature is **shell-pair distance**
  to the magic ladder Z, N $\\in$ {2, 8, 20, 28, 50, 82, 126}
  (per PR #500's `optimised_magic_verifier.py`).

This script implements a shell-aware level-1 correction that
subtracts mass proportionally to (Z, N)'s proximity to a magic
shell pair. NOT a 4He-special-case: the same formula gives big
corrections at every doubly-magic atom and small corrections
elsewhere — driven by *shell-pair distance*, not by atom-specific
flags.

## Mechanism

1. Define `shell_factor(Z, N) = exp(-d(Z, N) / scale)` where
   d(Z, N) is the shell-distance to the closest magic shell-pair
   (manhattan-style |Z - Z*| + |N - N*| over magic numbers).
2. Level-1 contribution: `m^{(1)} = -ε · shell_factor(Z, N) · m^{(0)}`.
3. Fit ε on one anchor atom (e.g. 4He cal/m_e → 1.0 minus a small
   residual). Test universality on the other 9 atoms.

The α here is **not a free parameter beyond the three-calibration
discipline** — it is structurally determined as the leading
shell-correction coefficient and should equal $h \\cdot z^2 / [n]_q$
or similar at the algebraic level. In v2 we fit it once on 4He
and check whether the same α improves the spread on the other 9
(test of universality).
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import per_braid_mass_hybrid
from q_parameter import Q as Q0_FLOAT

mpmath.mp.dps = 50
q0 = mpmath.mpf(str(Q0_FLOAT))
qi0 = 1 / q0
hbar_q = (q0 - 1) / q0
hbar_q_sq = hbar_q ** 2

M_E_MEV = 0.51099895000

AME_MASS_MEV = {
    "D":    1875.61294257,
    "3He":  2808.39148127,
    "3H":   2808.92113298,
    "4He":  3727.37909409,
    "6Li":  5603.05182,
    "7Li":  6535.36573,
    "9Be":  8392.74912,
    "12C": 11177.9292,
    "16O": 14899.16828,
    "40Ca": 37224.9202,
}

# Magic ladder per PR #500's MAGIC_LADDER (also rem:magic-numbers-from-q).
MAGIC = (2, 8, 20, 28, 50, 82, 126)


def shell_distance(Z: int, N: int) -> int:
    """Manhattan distance to closest magic shell-pair (Z*, N*)."""
    return min(abs(Z - mz) + abs(N - mn) for mz in MAGIC for mn in MAGIC)


def shell_factor(Z: int, N: int, *, scale: float = 4.0) -> mpmath.mpf:
    """Shell-saturation enrichment: 1 at magic, decays with distance."""
    d = shell_distance(Z, N)
    return mpmath.exp(-mpmath.mpf(d) / mpmath.mpf(scale))


def per_braid_mass_shell_aware(Z: int, N: int, *,
                                 epsilon: mpmath.mpf = None,
                                 scale: float = 4.0) -> dict:
    """Level-0 hybrid + shell-aware level-1 correction.

    m_total = m^{(0)} · (1 - ε · shell_factor(Z, N))

    where ε is fit on 4He (returns 0.0 if epsilon unset → reduces
    to level-0 hybrid).
    """
    level0 = per_braid_mass_hybrid(Z, N)
    m0 = level0["total"]
    sf = shell_factor(Z, N, scale=scale)
    if epsilon is None:
        epsilon = mpmath.mpf(0)
    correction = epsilon * sf
    m_total = m0 * (1 - correction)
    return {
        "Z": Z, "N": N, "A": Z + N,
        "shell_distance": shell_distance(Z, N),
        "shell_factor": float(sf),
        "epsilon": float(epsilon),
        "level_0_total": float(m0),
        "correction_fraction": float(correction),
        "total_with_shell": float(m_total),
    }


def fit_epsilon_on_4He(scale: float = 4.0) -> mpmath.mpf:
    """Fit ε so cal/m_e_4He = exact AME/pred match.

    cal_target = AME / [m^{(0)} · (1 - ε · shell_factor(2,2))]
    m_e_norm = cal_target / m_e
    Want m_e_norm = 1.0 exactly:
      → m^{(0)} · (1 - ε) = AME / m_e
      → ε = 1 - (AME / m_e) / m^{(0)}
    (since shell_factor(2,2) = exp(0) = 1)
    """
    he4 = per_braid_mass_hybrid(2, 2)
    m0 = he4["total"]
    target = AME_MASS_MEV["4He"] / M_E_MEV
    epsilon = 1 - target / m0
    return epsilon


if __name__ == "__main__":
    print("=" * 100)
    print("A.3 v2 — Shell-aware level-1 jet correction (per cal-spread audit)")
    print("=" * 100)
    print(f"q_0   = {q0}")
    print(f"m_e   = {M_E_MEV} MeV")
    print(f"magic = {MAGIC}")
    print()

    # Step 1: fit ε on 4He
    epsilon_4He = fit_epsilon_on_4He()
    print(f"ε fitted on 4He: {float(epsilon_4He):.6e}")
    print()

    ATOMS = [
        ("D", 1, 1),
        ("3He", 2, 1),
        ("3H", 1, 2),
        ("4He", 2, 2),
        ("6Li", 3, 3),
        ("7Li", 3, 4),
        ("9Be", 4, 5),
        ("12C", 6, 6),
        ("16O", 8, 8),
        ("40Ca", 20, 20),
    ]

    rows = []
    print(f"  {'atom':>5} {'Z':>3} {'N':>3} {'A':>3} {'d':>3} "
          f"{'sh_factor':>10} {'level0':>14} {'correction':>11} "
          f"{'total':>14} {'AME':>12} {'cal/m_e':>10}")
    print("  " + "-" * 110)
    ratios = []
    for name, Z, N in ATOMS:
        out = per_braid_mass_shell_aware(Z, N, epsilon=epsilon_4He)
        ame = AME_MASS_MEV[name]
        total = out["total_with_shell"]
        cal_over_me = (ame / total) / M_E_MEV
        ratios.append(cal_over_me)
        print(f"  {name:>5} {Z:>3} {N:>3} {Z+N:>3} {out['shell_distance']:>3} "
              f"{out['shell_factor']:>10.6f} {out['level_0_total']:>14.4e} "
              f"{out['correction_fraction']:>11.6e} "
              f"{total:>14.4e} {ame:>12.4f} {cal_over_me:>10.6f}")
        rows.append({
            "atom": name, "Z": Z, "N": N,
            "shell_distance": out["shell_distance"],
            "shell_factor": out["shell_factor"],
            "level_0_total": out["level_0_total"],
            "correction_fraction": out["correction_fraction"],
            "total_with_shell": total,
            "ame_mass_mev": ame,
            "cal_over_me": cal_over_me,
        })

    mean_ratio = sum(ratios) / len(ratios)
    spread = (max(ratios) - min(ratios)) / mean_ratio * 100
    print()
    print(f"  Mean cal/m_e = {mean_ratio:.6f}, spread = {spread:.4f}%")
    print()

    # Compare with level-0-only baseline (epsilon = 0)
    print("--- Comparison: level-0 baseline vs shell-aware ---")
    level0_ratios = []
    for name, Z, N in ATOMS:
        out0 = per_braid_mass_shell_aware(Z, N, epsilon=mpmath.mpf(0))
        ame = AME_MASS_MEV[name]
        cal_over_me = (ame / out0["total_with_shell"]) / M_E_MEV
        level0_ratios.append(cal_over_me)
    l0_mean = sum(level0_ratios) / len(level0_ratios)
    l0_spread = (max(level0_ratios) - min(level0_ratios)) / l0_mean * 100
    print(f"  Level-0 only:  mean = {l0_mean:.6f}, spread = {l0_spread:.4f}%")
    print(f"  Shell-aware:   mean = {mean_ratio:.6f}, spread = {spread:.4f}%")
    print(f"  Spread change: {(spread - l0_spread):+.4f}%")
    print()

    # Witness output
    out_path = (Path(__file__).parent.parent.parent
                / "docs/audits/2026-05-02-shell-aware-level-1.witness.json")
    out_path.write_text(json.dumps({
        "audit": "A.3 v2 — shell-aware level-1 jet correction",
        "generated": datetime.now(timezone.utc).isoformat(),
        "q_0": str(q0),
        "m_e_mev": M_E_MEV,
        "magic_ladder": list(MAGIC),
        "epsilon_fit_atom": "4He",
        "epsilon_value": str(epsilon_4He),
        "scale": 4.0,
        "level_0_baseline_spread_pct": l0_spread,
        "shell_aware_spread_pct": spread,
        "spread_change_pct": spread - l0_spread,
        "atoms": rows,
        "interpretation": (
            "Shell-aware level-1 correction: m^(0) · (1 - ε · "
            "exp(-d(Z,N)/scale)) where d is manhattan distance to "
            "closest magic shell-pair. ε fit on 4He, scale = 4. "
            "Test of universality: same ε applied to all atoms — "
            "does it close the spread?"
        ),
    }, indent=2, default=str))
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
