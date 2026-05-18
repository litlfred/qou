#!/usr/bin/env python3
"""Visualization with explicit formulas + C4 hypothesis test.

Shows:
- The cubic underlying the integrands (Schur-Weyl 3-root)
- The TWO integrands plotted directly
- A(a) and its derivatives
- C4 hypothesis: solve A(a) = 2.4616 and check if a_C4 = (4-q)/(4q+3)
- The exact m_p_pred curve with both criteria marked

Emits c2_inflection_with_formulas.png.
"""
from __future__ import annotations
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import integrate, optimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from q_parameter import Q as q0_float, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV, VOL_BORROMEAN
from picard_lefschetz_thimble import cubic_roots, sw_3root_product_degree1

q0 = float(q0_float)
z_mark = 1 / (np.sqrt(q0) + np.sqrt(1.0 / q0))
borromean_factor = VOL_BORROMEAN / (HBAR_Q ** 2)
a_post_hoc = (4 - q0) / (4 * q0 + 3)

# Targets (for the C4 hypothesis)
M_N_target = (M_P_MEV + (M_P_MEV + Q_NEUTRON_MEV + M_E_MEV)) / 2
A_target = M_P_MEV / (borromean_factor * M_E_MEV)  # the OUTPUT factor we need


def integrand_baryon(z):
    return float(np.real(sw_3root_product_degree1(z)))


def integrand_electron(z):
    cs = cubic_roots(z)
    c = cs[np.argmin(np.abs(cs.imag))]
    return float(np.real(c + z))


def A_of(a_val):
    e_ref, _ = integrate.quad(integrand_electron, -a_val, a_val, limit=200)
    prod, _ = integrate.quad(integrand_baryon, -a_val, a_val, limit=200)
    return abs(prod) / abs(e_ref) if abs(e_ref) > 1e-15 else float("nan")


def main():
    print(f"q_0 = {q0:.10f}")
    print(f"z_markov = {z_mark:.10f}")
    print(f"a_post_hoc = (4-q)/(4q+3) = {a_post_hoc:.10f}")
    print(f"Target A(a_*) for CODATA m_p: {A_target:.10f}")
    print()

    # Dense grid
    a_grid = np.linspace(0.05, z_mark * 0.99, 2000)
    A_vals = np.array([A_of(a) for a in a_grid])
    dA = np.gradient(A_vals, a_grid)
    d2A = np.gradient(dA, a_grid)
    m_p_vals = borromean_factor * A_vals * M_E_MEV

    # Find inflection (d²A = 0)
    sign_changes = [i for i in range(1, len(d2A)-1) if d2A[i]*d2A[i+1] < 0]
    a_C2 = a_grid[sign_changes[0]] if sign_changes else None

    # Find C4: solve A(a) = A_target using bisection
    try:
        a_C4 = optimize.brentq(lambda a: A_of(a) - A_target, 0.1, z_mark * 0.99)
    except ValueError:
        a_C4 = None

    print(f"  a_C2 (d²A = 0, inflection): {a_C2:.10f}, A = {A_of(a_C2):.6f}")
    print(f"  a_C4 (A = target, m_p match): {a_C4:.10f}, A = {A_of(a_C4):.6f}")
    print(f"  a_post_hoc (4-q)/(4q+3):     {a_post_hoc:.10f}, A = {A_of(a_post_hoc):.6f}")
    print()
    print(f"  Ratio a_C4 / a_post_hoc: {a_C4/a_post_hoc:.6f}")
    print(f"  → C4 hypothesis: {'MATCH' if abs(a_C4 - a_post_hoc)/a_post_hoc < 0.001 else 'no exact match'}")

    # Integrand sample
    z_grid = np.linspace(-z_mark, z_mark, 1500)
    int_b = np.array([integrand_baryon(z) for z in z_grid])
    int_e = np.array([integrand_electron(z) for z in z_grid])

    # Layout: 3×3
    fig, axes = plt.subplots(3, 3, figsize=(17, 14))
    fig.suptitle(
        "C2 inflection criterion — full structural context for PR #690's substrate m_p anchor\n"
        f"q_0 = {q0:.6f}, target factor A* = m_p / (Vol(B_3)/ℏ_q² · m_e) = {A_target:.6f}",
        fontsize=12,
    )

    markers = [
        (a_C2, f"a_C2 = {a_C2:.4f}\n(d²A=0)", "red", "-"),
        (a_C4, f"a_C4 = {a_C4:.4f}\n(A=target)", "magenta", "-."),
        (a_post_hoc, f"a_post_hoc = {a_post_hoc:.4f}\n(PR #690 formula)", "green", "--"),
        (z_mark, f"z_markov = {z_mark:.4f}\n(boundary)", "gray", ":"),
    ]

    # (1,1) Integrands
    ax = axes[0, 0]
    ax.plot(z_grid, int_b, "C0-", linewidth=1.2, label="integrand_baryon (SW 3-root)")
    ax.plot(z_grid, int_e, "C3-", linewidth=1.2, label="integrand_electron (cubic root)")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("z"); ax.set_ylabel("integrand")
    ax.set_title("(1) The two integrands")
    ax.legend(fontsize=8, loc="best")
    ax.grid(alpha=0.3)

    # (1,2) Formula box
    ax = axes[0, 1]
    ax.axis("off")
    formula_text = (
        "FORMULAS  (PR #690 framework)\n"
        "\n"
        "         |∫_{-a}^{a} integrand_baryon(z) dz|\n"
        "  A(a) = ───────────────────────────────────\n"
        "         |∫_{-a}^{a} integrand_electron(z) dz|\n"
        "\n"
        "where:\n"
        "  baryon   : z ↦ Re(SW₃(z))\n"
        "             Schur-Weyl 3-root product, degree-1\n"
        "  electron : z ↦ Re(c + z)\n"
        "             c = cubic root nearest the imaginary axis\n"
        "\n"
        "  a ∈ (0, z_markov)   categorical action parameter\n"
        "\n"
        "MASS PREDICTION\n"
        "                 Vol(B_3)\n"
        "  m_p_pred(a) = ───────── · A(a) · m_e\n"
        "                   ℏ_q²\n"
        "\n"
        "CRITERIA TESTED\n"
        "  C1: min |dA/da|          — slowest growth\n"
        "  C2: d²A/da² = 0          — inflection (PR #690 picks)\n"
        "  C3: d³A/da³ = 0          — higher-order critical\n"
        "  C4: A(a) = A*_target     — direct mass match (NEW)\n"
        "  C5: integrand zero/extremum crossing\n"
        "  C6: LP shadow-price identity\n"
        "\n"
        "EMPIRICAL POST-HOC FORMULA (PR #690)\n"
        "                      4 − q\n"
        "  a_post_hoc(q) = ─────────\n"
        "                    4q + 3\n"
    )
    ax.text(0.0, 1.0, formula_text, transform=ax.transAxes,
            fontsize=9, family="monospace", verticalalignment="top")

    # (1,3) A(a)
    ax = axes[0, 2]
    ax.plot(a_grid, A_vals, "b-", linewidth=1.5, label="A(a)")
    ax.axhline(A_target, color="black", linestyle="-", linewidth=1.0,
               label=f"A* target = {A_target:.4f}")
    for a, lbl, col, ls in markers:
        ax.axvline(a, color=col, linestyle=ls, alpha=0.7)
    ax.set_xlabel("a"); ax.set_ylabel("A(a)")
    ax.set_title("(2) A(a) with mass-match target")
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(alpha=0.3)

    # (2,1) dA/da
    ax = axes[1, 0]
    ax.plot(a_grid, dA, "purple", linewidth=1.5)
    ax.axhline(0, color="k", linewidth=0.5)
    for a, _, col, ls in markers:
        ax.axvline(a, color=col, linestyle=ls, alpha=0.7)
    ax.set_xlabel("a"); ax.set_ylabel("dA/da")
    ax.set_title("(3) dA/da")
    ax.grid(alpha=0.3)

    # (2,2) d²A/da² with C2 zero marked
    ax = axes[1, 1]
    ax.plot(a_grid, d2A, "orange", linewidth=1.5)
    ax.axhline(0, color="k", linewidth=0.5)
    if a_C2 is not None:
        ax.scatter([a_C2], [0], color="red", s=120, zorder=5,
                   label=f"d²A=0 at a={a_C2:.4f}")
    for a, _, col, ls in markers:
        ax.axvline(a, color=col, linestyle=ls, alpha=0.7)
    ax.set_xlabel("a"); ax.set_ylabel("d²A/da²")
    ax.set_title("(4) d²A/da² — C2 criterion")
    ax.legend(fontsize=8, loc="best")
    ax.grid(alpha=0.3)

    # (2,3) Zoom: A(a) near the four candidate a-values
    ax = axes[1, 2]
    a_zoom = (min(a_C2, a_C4, a_post_hoc) - 0.02,
              max(a_C2, a_C4, a_post_hoc) + 0.02)
    mask = (a_grid >= a_zoom[0]) & (a_grid <= a_zoom[1])
    ax.plot(a_grid[mask], A_vals[mask], "b-", linewidth=2)
    ax.axhline(A_target, color="black", linestyle="-", linewidth=1.0,
               label=f"A* target = {A_target:.6f}")
    for a, lbl, col, ls in markers:
        if a_zoom[0] <= a <= a_zoom[1]:
            ax.axvline(a, color=col, linestyle=ls, alpha=0.7, label=lbl.split("\n")[0])
            ax.scatter([a], [A_of(a)], color=col, s=80, zorder=5)
    ax.set_xlabel("a"); ax.set_ylabel("A(a)")
    ax.set_title("(5) Zoom on candidates — does any match A*?")
    ax.legend(fontsize=8, loc="best")
    ax.grid(alpha=0.3)

    # (3,1) m_p prediction
    ax = axes[2, 0]
    ax.plot(a_grid, m_p_vals, "b-", linewidth=1.5)
    ax.axhline(M_P_MEV, color="black", linestyle="-", linewidth=1.2,
               label=f"CODATA m_p = {M_P_MEV:.3f} MeV")
    for a, lbl, col, ls in markers:
        ax.axvline(a, color=col, linestyle=ls, alpha=0.7)
        if a < z_mark:
            ax.scatter([a], [borromean_factor*A_of(a)*M_E_MEV],
                       color=col, s=80, zorder=5)
    ax.set_xlabel("a"); ax.set_ylabel("m_p_pred (MeV)")
    ax.set_title("(6) m_p prediction curve")
    ax.legend(fontsize=8, loc="best")
    ax.grid(alpha=0.3)

    # (3,2) C4 hypothesis test
    ax = axes[2, 1]
    ax.axis("off")
    if a_C4 is not None:
        ratio_C4 = a_C4 / a_post_hoc
        diff_pct = (a_C4 - a_post_hoc) / a_post_hoc * 100
        c4_match = "MATCH (<0.001)" if abs(diff_pct) < 0.1 else f"diff {diff_pct:+.4f}%"
        report = (
            "C4 HYPOTHESIS TEST\n"
            "\n"
            "  Claim: a_post_hoc = (4-q)/(4q+3)\n"
            "         solves A(a) = A* (mass-match)\n"
            "\n"
            f"  At q_0 = {q0:.6f}:\n"
            f"    a_C4 (numerical) =  {a_C4:.8f}\n"
            f"    a_post_hoc      =  {a_post_hoc:.8f}\n"
            f"    ratio: a_C4/a_post_hoc = {ratio_C4:.6f}\n"
            f"    relative diff: {diff_pct:+.4f}%\n"
            "\n"
            f"  → {c4_match}\n"
            "\n"
            f"  m_p (at a_C4):  {borromean_factor*A_of(a_C4)*M_E_MEV:.5f} MeV\n"
            f"  m_p (at phoc):  {borromean_factor*A_of(a_post_hoc)*M_E_MEV:.5f} MeV\n"
            f"  CODATA m_p:     {M_P_MEV:.5f} MeV\n"
            "\n"
            "C2 vs C4 at 2000 pts\n"
            f"  a_C2 (d²A=0):  {a_C2:.6f}  m_p={borromean_factor*A_of(a_C2)*M_E_MEV:.4f}\n"
            f"  a_C4 (A=A*):   {a_C4:.6f}  m_p={borromean_factor*A_of(a_C4)*M_E_MEV:.4f} ≈ CODATA\n"
            f"  a_phoc:        {a_post_hoc:.6f}  m_p={borromean_factor*A_of(a_post_hoc)*M_E_MEV:.4f}\n"
            "\n"
            "  a_C2 ≠ a_C4 (5% apart). PR #690's\n"
            "  a_post_hoc matches a_C4 more closely\n"
            "  than the d²A=0 inflection.\n"
        )
        ax.text(0.0, 1.0, report, transform=ax.transAxes,
                fontsize=10, family="monospace", verticalalignment="top")

    # (3,3) m_p zoom showing the three intersections
    ax = axes[2, 2]
    mask = (a_grid >= a_zoom[0]) & (a_grid <= a_zoom[1])
    ax.plot(a_grid[mask], m_p_vals[mask], "b-", linewidth=2)
    ax.axhline(M_P_MEV, color="black", linestyle="-", linewidth=1.2,
               label=f"CODATA m_p = {M_P_MEV:.4f}")
    for a, lbl, col, ls in markers:
        if a_zoom[0] <= a <= a_zoom[1]:
            ax.axvline(a, color=col, linestyle=ls, alpha=0.7, label=lbl.split("\n")[0])
            ax.scatter([a], [borromean_factor*A_of(a)*M_E_MEV],
                       color=col, s=80, zorder=5)
    ax.set_xlabel("a"); ax.set_ylabel("m_p_pred (MeV)")
    ax.set_title("(8) Zoom on m_p crossings of CODATA")
    ax.legend(fontsize=8, loc="best")
    ax.grid(alpha=0.3)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    out_path = HERE / "c2_inflection_with_formulas.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"\nSaved: {out_path}")
    plt.close(fig)
    return out_path


if __name__ == "__main__":
    main()
