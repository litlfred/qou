#!/usr/bin/env python3
"""Clean volume-weighted SDP-cost plot: 2-quark vs 3-quark, linear y-scale."""

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).parent


def delta_n(n):
    return (n + math.sqrt(n * n + 4)) / 2


PHI = delta_n(1)
DELTA_SILVER = delta_n(2)
DELTA_BRONZE = delta_n(3)
Q0 = 1.1099785955541805


def q_int(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def q_factorial(n, q):
    out = 1.0
    for k in range(1, n + 1):
        out *= q_int(k, q)
    return out


def y_2_sym(q):
    return q_int(2, q)


def y_2_anti(q):
    return 1 / q_int(2, q)


def tr_M_n2_sigma1_k(k, q):
    return y_2_sym(q) * q ** k + y_2_anti(q) * ((-1 / q) ** k)


def y_3_sym(q):
    d = q_int(3, q) * q_int(2, q)
    return d * d / q_factorial(3, q)


def y_3_mixed(q):
    d = q_int(3, q) * 1
    return d * d / q_factorial(3, q)


def tr_M_borromean(q):
    s = q - 1 / q
    chi_3 = -1
    chi_111 = -1
    chi_21 = s ** 6 - 6 * s ** 4 + 9 * s ** 2 - 2
    return y_3_sym(q) * chi_3 + y_3_mixed(q) * chi_21 + y_3_sym(q) * chi_111


def main():
    qs = [Q0 + i * (DELTA_BRONZE - Q0) / 300 for i in range(301)]

    # Hyperbolic volumes (from SnapPy canonical values)
    V_HOPF = 0.0
    V_TREFOIL = 0.0
    V_FIG8 = 2.0298832128193072
    V_5_1 = 0.0
    V_BORROMEAN = 7.327724753417960

    # Costs |tr_M(β)| × V_hyp(β) per state
    cost_hopf = [abs(tr_M_n2_sigma1_k(2, q)) * V_HOPF for q in qs]
    cost_trefoil = [abs(tr_M_n2_sigma1_k(3, q)) * V_TREFOIL for q in qs]
    cost_fig8 = [abs(tr_M_n2_sigma1_k(4, q)) * V_FIG8 for q in qs]
    cost_5_1 = [abs(tr_M_n2_sigma1_k(5, q)) * V_5_1 for q in qs]
    cost_borr = [abs(tr_M_borromean(q)) * V_BORROMEAN for q in qs]

    fig, ax = plt.subplots(figsize=(11, 6.5))

    # Free states at zero cost (horizontal line at y=0)
    ax.axhline(0, color="tab:green", lw=2.5, ls="-",
               label=r"Hopf, trefoil, 5_1 (torus, $V_{\rm hyp}=0$) — FREE")

    # Hyperbolic 2-quark
    ax.plot(qs, cost_fig8, "tab:orange", lw=2,
            label=r"figure-8 / 4_1 ($V_{\rm hyp} \approx 2.03$)")

    # Borromean
    ax.plot(qs, cost_borr, "k-", lw=2.5,
            label=r"Borromean L_6a4 ($V_{\rm hyp} = 8G \approx 7.33$) — BARYON FLOOR")

    # Metallic anchors
    for q_special, name, color in [
        (Q0, r"$q_0$", "tab:red"),
        (PHI, r"$\varphi$", "goldenrod"),
        (DELTA_SILVER, r"$\delta_2$ silver", "silver"),
        (DELTA_BRONZE, r"$\delta_3$ bronze", "peru"),
    ]:
        ax.axvline(q_special, color=color, lw=1.2, ls=":", alpha=0.8)
        ax.text(q_special, ax.get_ylim()[1] * 0.95 if ax.get_ylim()[1] > 0 else 200,
                " " + name, color=color, fontsize=10, va="top")

    ax.set_xlabel(r"$q$ (real, $\mathrm{Im}(q) = 0$)")
    ax.set_ylabel(r"$|\mathrm{tr}_M(\beta)| \times V_{\rm hyp}(\beta)$  (SDP cost proxy)")
    ax.set_title(r"Volume-weighted SDP cost — why 2-quark $<$ 3-quark across all metallic intervals")
    ax.grid(alpha=0.3)
    ax.legend(loc="upper left", fontsize=10)
    ax.set_xlim(1.0, float(DELTA_BRONZE) + 0.05)
    ax.set_ylim(-50, max(cost_borr) * 1.1)

    plt.tight_layout()
    out = HERE / "two-quark-volume-weighted-clean.png"
    fig.savefig(out, dpi=140, bbox_inches="tight")
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
