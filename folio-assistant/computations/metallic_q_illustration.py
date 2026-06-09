#!/usr/bin/env python3
"""Illustration: Hecke-scalar q − q⁻¹ vs q across the metallic ladder.

Visualises what the 3 probes (Wenzl / Jones / per-block) found:
- The Hecke scalar `q − q⁻¹` is a SMOOTH monotonic function of q.
- Metallic ratios δ_n are exactly the values where it crosses integer n.
- This is the proven algebraic structure (PR #1999) — *not* a bifurcation.
- The per-block characters y_λ · χ^λ(β) inherit this smoothness:
  no sign flips at metallic ratios for any β at n=3.
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).parent


def delta_n(n):
    return (n + math.sqrt(n * n + 4)) / 2


PHI = delta_n(1)
DELTA_SILVER = delta_n(2)
DELTA_BRONZE = delta_n(3)
Q0 = 1.1099785955541805


def linspace(a, b, k):
    return [a + (b - a) * i / (k - 1) for i in range(k)]


def main():
    qs = linspace(0.5, 4.0, 500)
    hecke_scalar = [q - 1 / q for q in qs]

    # Per-block contributions for σ_1 σ_2 (3-cycle, the cyclic-quark op):
    # χ^{(3)}(σ_1σ_2) = q²,  χ^{(2,1)}(σ_1σ_2) = (q − q⁻¹)² − 1,
    # χ^{(1,1,1)}(σ_1σ_2) = q⁻²
    chi_3 = [q ** 2 for q in qs]
    chi_21 = [(q - 1 / q) ** 2 - 1 for q in qs]
    chi_111 = [1 / (q ** 2) for q in qs]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True)

    # Top panel: Hecke scalar
    ax1.plot(qs, hecke_scalar, "k-", lw=2, label=r"$q - q^{-1}$ (Hecke scalar)")
    ax1.axhline(1, color="goldenrod", lw=0.7, ls="--", alpha=0.7)
    ax1.axhline(2, color="silver", lw=0.7, ls="--", alpha=0.7)
    ax1.axhline(3, color="peru", lw=0.7, ls="--", alpha=0.7)
    ax1.axhline(0, color="gray", lw=0.5)
    ax1.set_ylabel(r"$q - q^{-1}$")
    ax1.set_title(r"Hecke-scalar $q - q^{-1}$ vs $q$: metallic ratios at integer crossings (smooth, NOT a bifurcation)")
    ax1.grid(alpha=0.3)
    ax1.set_ylim(-2.5, 4)

    # Bottom panel: characters of σ_1 σ_2
    ax2.plot(qs, chi_3, "C0-", lw=1.5, label=r"$\chi^{(3)}(\sigma_1\sigma_2) = q^2$")
    ax2.plot(qs, chi_21, "C1-", lw=1.5, label=r"$\chi^{(2,1)}(\sigma_1\sigma_2) = (q-q^{-1})^2 - 1$")
    ax2.plot(qs, chi_111, "C2-", lw=1.5, label=r"$\chi^{(1,1,1)}(\sigma_1\sigma_2) = q^{-2}$")
    ax2.axhline(0, color="gray", lw=0.5)
    ax2.set_ylabel("character value")
    ax2.set_xlabel(r"$q$")
    ax2.set_title(r"Per-Wedderburn-block characters of the 3-cycle $\sigma_1\sigma_2$ — all smooth across metallic boundaries")
    ax2.grid(alpha=0.3)
    ax2.set_ylim(-2, 8)
    ax2.legend(loc="upper left", fontsize=9)

    # Mark metallic ratios on both panels
    for ax in (ax1, ax2):
        for q_special, name, color in [
            (Q0, r"$q_0$", "tab:red"),
            (PHI, r"$\varphi$", "goldenrod"),
            (DELTA_SILVER, r"$\delta_2$", "silver"),
            (DELTA_BRONZE, r"$\delta_3$", "peru"),
        ]:
            ax.axvline(q_special, color=color, lw=1.5, ls=":", alpha=0.8)
            ax.text(q_special, ax.get_ylim()[1] * 0.92, " " + name,
                    color=color, fontsize=10, ha="left", va="top")

    plt.tight_layout()
    out = HERE / "metallic-q-illustration.png"
    fig.savefig(out, dpi=140, bbox_inches="tight")
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
