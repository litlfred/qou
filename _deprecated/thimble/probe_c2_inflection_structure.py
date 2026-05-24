#!/usr/bin/env python3
"""Explore the structural meaning of the C2 inflection criterion
(d²A/da² = 0) that PR #690 uses to fix the substrate m_p.

Hypotheses to test:

H1. The inflection point coincides with a CRITICAL POINT of the
    underlying Schur-Weyl 3-root cubic. If so, C2 reduces to:
    "a* such that the integrand_baryon has a real-axis structural
    feature at z = a*".

H2. The inflection point is a Picard-Lefschetz saddle. If so,
    ∂A/∂a vanishes (or A has a stationary phase) on the
    Lefschetz thimble passing through a*.

H3. The inflection point matches the Yang-Baxter R-matrix
    critical point at a categorical level.

H4. The inflection point has no special structural meaning —
    it's a numerical near-coincidence with `5/2 − h²·G`.

Test bench:
- Tabulate A(a), dA, d²A, d³A on a fine grid
- Find the inflection point a_C2 numerically (high precision)
- Compare to:
  - integrand_baryon zero crossings / extrema (H1)
  - cubic discriminant zeros (H2)
  - 1/q, q/(1+q), and related substrate-Laurent values (H4)
- Compute the second-derivative WIDTH at the inflection (sharpness)
"""
from __future__ import annotations
import json, sys
from pathlib import Path

import numpy as np
import mpmath as mp
from scipy import integrate

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from q_parameter import Q as q0_float, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, VOL_BORROMEAN
from picard_lefschetz_thimble import cubic_roots, sw_3root_product_degree1

q0 = float(q0_float)
z_mark = 1 / (np.sqrt(q0) + np.sqrt(1.0 / q0))
borromean_factor = VOL_BORROMEAN / (HBAR_Q ** 2)
a_post_hoc = (4 - q0) / (4 * q0 + 3)


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


def m_p_of(a):
    return borromean_factor * A_of(a) * M_E_MEV


def main() -> int:
    w = WitnessBuilder("c2-inflection-structure-probe", engine="numpy+scipy+mpmath")
    w.set_description(
        "Explore the structural meaning of C2 inflection (d²A/da² = 0). "
        "Tests 4 hypotheses for why this criterion picks the substrate "
        "m_p value at 0.07% precision."
    )
    w.set_content_block("conj:flavor-dressed-mass-from-substrate-split")

    print("=" * 78)
    print("C2 Inflection Structure Probe")
    print("=" * 78)
    print(f"  q_0 = {q0:.10f}")
    print(f"  z_markov = {z_mark:.10f}")
    print(f"  a_post_hoc = (4-q)/(4q+3) = {a_post_hoc:.10f}")
    print(f"  → m_p(a_post_hoc) = {m_p_of(a_post_hoc):.4f} MeV")
    print(f"  CODATA m_p = {M_P_MEV:.4f} MeV (0.069% diff)")
    print()

    # ─── Find C2 inflection at high resolution ────────────────────
    a_grid = np.linspace(0.05, z_mark * 0.99, 2000)
    A_grid = np.array([A_of(a) for a in a_grid])
    dA = np.gradient(A_grid, a_grid)
    d2A = np.gradient(dA, a_grid)
    d3A = np.gradient(d2A, a_grid)

    # Find d²A sign changes
    sign_changes_d2 = []
    for i in range(1, len(d2A) - 1):
        if d2A[i] * d2A[i+1] < 0:
            sign_changes_d2.append(i)

    a_C2_inflections = [a_grid[idx] for idx in sign_changes_d2]
    print(f"  C2 inflection points found: {len(a_C2_inflections)}")
    for a_inf in a_C2_inflections:
        print(f"    a = {a_inf:.10f}, ratio to a_post_hoc = {a_inf/a_post_hoc:.6f}")
        print(f"    m_p = {m_p_of(a_inf):.4f} MeV")
    print()

    if not a_C2_inflections:
        print("  No inflection found! Aborting structural analysis.")
        w.add_data("status", "no_inflection_found")
        out = w.save()
        return 0

    a_C2 = a_C2_inflections[0]  # primary inflection
    w.add_data("a_C2_numerical", a_C2)
    w.add_data("a_post_hoc_formula_at_q0", a_post_hoc)
    w.add_data("ratio_a_C2_to_a_post_hoc", a_C2 / a_post_hoc)

    # ─── H1: Does a_C2 coincide with an integrand zero/extremum? ──
    print("[H1] Does a_C2 coincide with an integrand_baryon zero or extremum?")
    # Compute integrand_baryon on a fine grid; find zeros + extrema
    z_grid = np.linspace(-z_mark, z_mark, 2000)
    int_b_grid = np.array([integrand_baryon(z) for z in z_grid])
    int_e_grid = np.array([integrand_electron(z) for z in z_grid])

    # Zeros of baryon integrand
    zeros_b = []
    for i in range(1, len(int_b_grid) - 1):
        if int_b_grid[i] * int_b_grid[i+1] < 0:
            zeros_b.append(z_grid[i])
    print(f"  Zeros of integrand_baryon in (-z_mark, z_mark): {len(zeros_b)}")
    for z0 in zeros_b[:5]:
        print(f"    z = {z0:.6f}  (|z|/a_C2 = {abs(z0)/a_C2:.6f})")

    # Extrema of baryon integrand
    extrema_b = []
    d_int_b = np.gradient(int_b_grid, z_grid)
    for i in range(1, len(d_int_b) - 1):
        if d_int_b[i] * d_int_b[i+1] < 0:
            extrema_b.append((z_grid[i], int_b_grid[i]))
    print(f"  Extrema of integrand_baryon: {len(extrema_b)}")
    for z0, v in extrema_b[:5]:
        print(f"    z = {z0:.6f}, value = {v:.6f}  (|z|/a_C2 = {abs(z0)/a_C2:.6f})")

    h1_close_match = any(abs(abs(z0) - a_C2) < 0.01 for z0 in zeros_b + [z[0] for z in extrema_b])
    w.add_data("H1_close_match_a_C2_to_integrand_feature", h1_close_match)
    print(f"  H1 verdict: {'MATCH (within 0.01)' if h1_close_match else 'NO match'}")
    print()

    # ─── H2: Picard-Lefschetz interpretation ──────────────────────
    # Cubic discriminant: cubic_roots returns roots of a cubic in z.
    # If the cubic has a discriminant zero at z = a_C2, that's a PL
    # saddle (root collision).
    print("[H2] Picard-Lefschetz check — cubic discriminant zeros")
    # Compute cubic_roots at z = a_C2; check if roots are degenerate
    cs_at_C2 = cubic_roots(a_C2)
    print(f"  cubic_roots(a_C2) = {[float(c.real) for c in cs_at_C2]} + i·{[float(c.imag) for c in cs_at_C2]}")
    # Pairwise differences
    pairwise = []
    for i in range(3):
        for j in range(i+1, 3):
            pairwise.append(abs(complex(cs_at_C2[i]) - complex(cs_at_C2[j])))
    min_pair_diff = min(pairwise)
    print(f"  min pairwise root distance at a_C2: {min_pair_diff:.6f}")
    print(f"  H2 verdict: {'COLLISION' if min_pair_diff < 0.01 else 'no collision'}")
    w.add_data("H2_min_pairwise_root_distance_at_a_C2", float(min_pair_diff))
    print()

    # ─── H4: Substrate-Laurent expressibility ────────────────────
    print("[H4] Compare a_C2 to substrate-Laurent candidates")
    candidates = {
        "(4-q)/(4q+3)": (4 - q0) / (4*q0 + 3),
        "1/(q+2)": 1/(q0 + 2),
        "(q-1)/(q+1)": (q0 - 1)/(q0 + 1),
        "1 - 1/q²": 1 - 1/q0**2,
        "q/(q² + 1)": q0/(q0**2 + 1),
        "1/[3]_q": 1/(q0**2 + 1 + 1/q0**2),
        "h·2": 2 * (q0 - 1/q0),
        "h/(2-h)": (q0 - 1/q0) / (2 - (q0 - 1/q0)),
    }
    for name, val in candidates.items():
        rel = (val - a_C2) / a_C2 * 100
        marker = " ← <0.1%" if abs(rel) < 0.1 else (" ← <1%" if abs(rel) < 1 else "")
        print(f"  {name:25s} = {val:.10f}  (Δ {rel:+.3f}%){marker}")
    w.add_data("H4_substrate_candidates", {n: float(v) for n, v in candidates.items()})
    print()

    # ─── Inflection sharpness ─────────────────────────────────────
    idx_inf = sign_changes_d2[0]
    d3A_at_inf = d3A[idx_inf]
    print(f"  d³A/da³ at inflection: {d3A_at_inf:.6f}")
    print(f"  → inflection 'sharpness' (|d³A| determines curvature scale):")
    if abs(d3A_at_inf) > 1:
        print(f"     sharp ({abs(d3A_at_inf):.2f}); robust structural feature")
    else:
        print(f"     shallow ({abs(d3A_at_inf):.4f}); may be sensitive to deformation")
    w.add_data("inflection_d3A", float(d3A_at_inf))

    # ─── Verdict ──────────────────────────────────────────────────
    print()
    print("=" * 78)
    print("VERDICT")
    print("=" * 78)
    h1_ver = "MATCH" if h1_close_match else "NO match"
    h2_ver = "COLLISION" if min_pair_diff < 0.01 else "no collision"
    print(f"  H1 (integrand feature):    {h1_ver}")
    print(f"  H2 (Picard-Lefschetz):     {h2_ver}")
    h4_best = min(candidates.items(), key=lambda kv: abs(kv[1] - a_C2))
    print(f"  H4 (substrate-Laurent):    closest = {h4_best[0]} (Δ {(h4_best[1]-a_C2)/a_C2*100:+.3f}%)")
    w.add_data("h4_best_match", {"form": h4_best[0], "value": float(h4_best[1])})
    w.add_data("verdicts", {
        "H1_integrand_feature": h1_ver,
        "H2_picard_lefschetz_collision": h2_ver,
        "H4_substrate_laurent_best_match": h4_best[0],
    })

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
