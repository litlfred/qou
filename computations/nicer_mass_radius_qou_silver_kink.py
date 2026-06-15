#!/usr/bin/env python3
"""NICER mass-radius data vs the QOU silver-kink prediction.

The QOU framework predicts that at the silver-density crossover
(`q = δ_silver` = 1+√2 ≈ 2.414), the EOS stiffens discontinuously from
Borromean-hadronic to CFL-superconducting.  This produces a **kink** in
the M-R relation at the corresponding density `ρ_c`.

This probe plots published NICER measurements alongside two model
families:
  - Pure hadronic EOS (no CFL transition): smooth M-R curve from soft
    nuclear EOS at low ρ asymptotically approaching a softer max-mass
    plateau.
  - QOU silver-kink EOS: hadronic up to `ρ_c`, then CFL-stiffened
    above, producing a kink in M(R) at the transition density.

Published NICER masses + radii (with 68% credible intervals):
  PSR J0030+0451 (Miller+ 2019, Riley+ 2019, Miller+ 2021)
  PSR J0740+6620 (Miller+ 2021, Riley+ 2021, Salmi+ 2024)
  PSR J0437-4715 (Choudhury+ 2024)

Plus the LIGO/Virgo GW170817 + GW190425 mass constraints
(low-mass tail of the population).

Output: PNG comparing data to two model families.  No fit is performed;
this is illustrative — to demonstrate the OBSERVABLE the QOU framework
predicts and where current data lies relative to it.

Limitations:
  - The q-ρ map is not pinned in the QOU framework yet, so the
    kink location in physical density is a free parameter.  We choose
    `ρ_c` to fall near the observed M ≈ 1.4 M☉ data so the kink is
    visible at relevant masses.
  - Model curves are schematic Newtonian polytropes, not full TOV
    integrations.  They illustrate the SHAPE of the prediction.

For a real falsification test, a TOV-integrated QOU EOS at the silver
crossover density should be compared to the joint NICER+LIGO+EOS
constraints (Hebeler+, Annala+, etc.).
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).parent


# ── Published NICER + GW measurements ───────────────────────────────────


NICER_DATA = {
    # (mass M☉, R km, err_M, err_R, label, color, ref)
    "J0030+0451 (Miller+ 2021)":
        (1.44, 13.02, 0.15, 1.06, "tab:blue", "Miller+ 2021"),
    "J0030+0451 (Riley+ 2019)":
        (1.34, 12.71, 0.16, 1.20, "tab:cyan", "Riley+ 2019"),
    "J0740+6620 (Miller+ 2021)":
        (2.072, 13.7, 0.07, 2.6, "tab:red", "Miller+ 2021"),
    "J0740+6620 (Riley+ 2021)":
        (2.072, 12.39, 0.07, 1.55, "tab:orange", "Riley+ 2021"),
    "J0740+6620 (Salmi+ 2024)":
        (2.072, 12.49, 0.07, 0.93, "tab:purple", "Salmi+ 2024"),
    "J0437-4715 (Choudhury+ 2024)":
        (1.418, 11.36, 0.037, 0.95, "tab:green", "Choudhury+ 2024"),
}

# GW170817-derived tidal deformability constraints on R(1.4 M☉)
# (Abbott+ 2018: R(1.4) = 11.9 +/- 1.4 km at 90% credibility)
GW170817_R_1p4 = (11.9, 1.4)

# Maximum-mass constraint from PSR J0952-0607: M = 2.35 M☉ (Romani+ 2022)
M_MAX_CONSTRAINT = 2.35


# ── Model curves ────────────────────────────────────────────────────────


def hadronic_only_curve(M_range: np.ndarray) -> np.ndarray:
    """Schematic hadronic-only EOS: soft nuclear matter (TM1-like).

    Smooth, monotonically rising R(M) curve, asymptotically constant
    around 11-12 km.  Captures the broad-stroke shape of typical
    'soft hadronic' models like SLy4, APR, DD2.
    """
    # Empirical fit to typical hadronic EOS M-R curves
    # R(M) = R_0 + (R_max - R_0) * (1 - exp(-M/M_scale))
    R_0 = 10.5  # km, low-mass radius
    R_max = 11.8  # km, max-mass asymptote
    M_scale = 0.6  # M☉
    return R_0 + (R_max - R_0) * (1 - np.exp(-M_range / M_scale))


def qou_silver_kink_curve(M_range: np.ndarray,
                          M_kink: float = 1.45) -> np.ndarray:
    """Schematic QOU-with-CFL-core EOS: kink at M_kink M☉.

    Below the kink: same as hadronic-only (R ≈ 11 km).
    Above the kink: CFL stiffening produces R ≈ 13 km plateau.

    The kink location M_kink is chosen so that the CFL transition
    density `ρ_c(δ_silver)` corresponds to neutron star mass
    ≈ 1.4-1.5 M☉ at the silver-density crossover.  The choice
    is illustrative; the framework would pin this once the q-ρ map
    is calibrated.
    """
    R_hadronic = hadronic_only_curve(M_range)
    R_cfl = 13.0  # km, CFL plateau (stiffer EOS)
    # Smooth tanh transition at M_kink with width 0.1 M☉
    transition = 0.5 * (1 + np.tanh((M_range - M_kink) / 0.05))
    return R_hadronic * (1 - transition) + R_cfl * transition


def main() -> None:
    M_range = np.linspace(0.8, 2.6, 200)
    R_hadronic = hadronic_only_curve(M_range)
    R_qou_low_kink = qou_silver_kink_curve(M_range, M_kink=1.35)
    R_qou_high_kink = qou_silver_kink_curve(M_range, M_kink=1.65)

    fig, ax = plt.subplots(figsize=(11, 7))

    # Hadronic-only band
    ax.plot(R_hadronic, M_range, "tab:gray", lw=2,
            label="Soft hadronic EOS (no CFL transition)", zorder=2)

    # QOU silver-kink predictions
    ax.plot(R_qou_low_kink, M_range, "tab:red", lw=2, ls="--",
            label=r"QOU silver kink @ $M_{\rm kink} = 1.35 M_\odot$",
            zorder=3)
    ax.plot(R_qou_high_kink, M_range, "tab:orange", lw=2, ls="--",
            label=r"QOU silver kink @ $M_{\rm kink} = 1.65 M_\odot$",
            zorder=3)

    # Mark the QOU kink locations
    ax.axhline(1.35, color="tab:red", lw=0.6, ls=":", alpha=0.5)
    ax.axhline(1.65, color="tab:orange", lw=0.6, ls=":", alpha=0.5)
    ax.text(8.6, 1.36, "QOU kink (low)", fontsize=8,
            color="tab:red", va="bottom")
    ax.text(8.6, 1.66, "QOU kink (high)", fontsize=8,
            color="tab:orange", va="bottom")

    # NICER data points with error bars
    for label, (M, R, eM, eR, color, ref) in NICER_DATA.items():
        ax.errorbar(R, M, xerr=eR, yerr=eM, fmt="o", color=color,
                    markersize=8, capsize=4, lw=1.5, alpha=0.85,
                    label=label, zorder=4)

    # GW170817 R(1.4) constraint band
    R_gw, R_gw_err = GW170817_R_1p4
    ax.axvspan(R_gw - R_gw_err, R_gw + R_gw_err, ymin=0.18, ymax=0.32,
               color="tab:purple", alpha=0.15, zorder=1)
    ax.text(R_gw, 1.45, r"GW170817 $\Lambda$",
            fontsize=8, color="purple", ha="center", va="bottom",
            rotation=90)

    # Max-mass constraint
    ax.axhline(M_MAX_CONSTRAINT, color="black", lw=0.6, ls=":")
    ax.text(8.6, M_MAX_CONSTRAINT + 0.03,
            r"$M_{\max}$ constraint (PSR J0952-0607)",
            fontsize=8, color="black")

    ax.set_xlabel("Radius (km)")
    ax.set_ylabel(r"Mass ($M_\odot$)")
    ax.set_title(
        "NICER + GW170817 NS mass-radius vs QOU silver-kink prediction\n"
        r"QOU: stiffening at $q = \delta_{\rm silver}$ produces a kink in $R(M)$"
    )
    ax.set_xlim(8.5, 16)
    ax.set_ylim(0.8, 2.6)
    ax.grid(alpha=0.3)
    ax.legend(loc="lower right", fontsize=8, framealpha=0.95)

    plt.tight_layout()
    out_png = HERE / "nicer-mass-radius-qou-silver-kink.png"
    fig.savefig(out_png, dpi=140, bbox_inches="tight")
    print(f"Saved: {out_png}")


if __name__ == "__main__":
    main()
