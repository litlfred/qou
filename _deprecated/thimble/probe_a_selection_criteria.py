"""
probe_a_selection_criteria.py — test 6 candidate categorical
criteria for selecting `a ∈ (0, z_markov)`.

Per owner: "probe criterion...."

After the higher-derivative + GB-grade probe ruled out
"missing sub-leading h^k" as the source of the +0.42% gap,
the question sharpens to:

  What categorical principle SELECTS a inside (0, z_markov)?

This probe tests 6 candidate selection criteria empirically.
Each is a substrate-clean (no CODATA m_p input) criterion that
COULD determine `a` uniquely.  We find the `a` each criterion
picks and compare to the post-hoc 0.388 and to z_markov ≈ 0.499.

Criteria tested:
  C1. min |dA/da|  — slowest growth point
  C2. d²A/da² = 0  — inflection point
  C3. d³A/da³ = 0  — higher-order critical point
  C4. A(a) = |tr_M(β_p)|_paper = 1.0653  — substrate identity
  C5. Where the integrand ∏ dc_k/dz hits a real-axis structural
      feature (sign change, zero crossing, extremum)
  C6. ν_SDP · |tr_M| · a = ν_SDP_target  — operator-selection
      identity (per prop:operator-selection-lp)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
import numpy as np
from scipy import integrate, optimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from picard_lefschetz_thimble import (
    cubic_roots, sw_3root_product_degree1,
)
from q_parameter import Q as q0, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, VOL_BORROMEAN

z_mark = 1 / (np.sqrt(q0) + np.sqrt(1.0 / q0))
borromean = VOL_BORROMEAN / (HBAR_Q ** 2)
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


def m_p_of(a_val):
    return borromean * A_of(a_val) * M_E_MEV


def main() -> int:
    print("=" * 78)
    print("  Probe: categorical selection criteria for `a` in (0, z_markov)")
    print("=" * 78)
    print(f"  q_0 = {q0:.10f}")
    print(f"  z_markov = {z_mark:.10f}")
    print(f"  a_post_hoc (4-q)/(4q+3) = {a_post_hoc:.10f}  ← TARGET")
    print(f"  CODATA m_p = {M_P_MEV:.4f} MeV")
    print()

    # Fine grid over physical interval
    a_grid = np.linspace(0.05, z_mark * 1.05, 500)
    A_grid = np.array([A_of(a) for a in a_grid])
    m_p_grid = borromean * A_grid * M_E_MEV
    dA = np.gradient(A_grid, a_grid)
    d2A = np.gradient(dA, a_grid)
    d3A = np.gradient(d2A, a_grid)

    results = []

    # ── C1: min dA/da ─────────────────────────────────────────────
    idx_min_dA = np.argmin(dA)
    a_C1 = a_grid[idx_min_dA]
    print(f"  C1. min dA/da (slowest growth):")
    print(f"      a = {a_C1:.10f}, dA/da = {dA[idx_min_dA]:.6f}")
    print(f"      A = {A_grid[idx_min_dA]:.6f}, m_p = {m_p_grid[idx_min_dA]:.4f} MeV")
    print(f"      vs target {a_post_hoc:.4f}: ratio = {a_C1 / a_post_hoc:.4f}")
    print()
    results.append({"criterion": "C1 min dA/da", "a": float(a_C1),
                    "m_p_pred": float(m_p_grid[idx_min_dA]),
                    "ratio_to_post_hoc": float(a_C1 / a_post_hoc)})

    # ── C2: d²A/da² = 0 (inflection) ─────────────────────────────
    sign_changes_d2A = []
    for i in range(1, len(d2A) - 1):
        if d2A[i] * d2A[i+1] < 0:
            sign_changes_d2A.append(i)
    print(f"  C2. d²A/da² = 0 (inflection points):")
    if sign_changes_d2A:
        for idx in sign_changes_d2A[:3]:
            a_C2 = a_grid[idx]
            print(f"      a = {a_C2:.10f}, m_p = {m_p_grid[idx]:.4f} MeV")
            print(f"      vs target: ratio = {a_C2 / a_post_hoc:.4f}")
            results.append({"criterion": f"C2 d2A/da2=0 at idx {idx}",
                           "a": float(a_C2),
                           "m_p_pred": float(m_p_grid[idx]),
                           "ratio_to_post_hoc": float(a_C2 / a_post_hoc)})
    else:
        print(f"      NONE found in the physical interval")
    print()

    # ── C3: d³A/da³ = 0 ──────────────────────────────────────────
    sign_changes_d3A = []
    for i in range(1, len(d3A) - 1):
        if d3A[i] * d3A[i+1] < 0:
            sign_changes_d3A.append(i)
    print(f"  C3. d³A/da³ = 0 (higher-order critical):")
    if sign_changes_d3A:
        for idx in sign_changes_d3A[:3]:
            a_C3 = a_grid[idx]
            print(f"      a = {a_C3:.10f}, m_p = {m_p_grid[idx]:.4f} MeV")
            print(f"      vs target: ratio = {a_C3 / a_post_hoc:.4f}")
            results.append({"criterion": f"C3 d3A/da3=0 at idx {idx}",
                           "a": float(a_C3),
                           "m_p_pred": float(m_p_grid[idx]),
                           "ratio_to_post_hoc": float(a_C3 / a_post_hoc)})
    print()

    # ── C4: A(a) = |tr_M(β_p)| = 1.0653 (paper substrate) ─────────
    tr_M_p_paper = 1.0653
    print(f"  C4. A(a) = |tr_M(β_p)|_paper = {tr_M_p_paper}:")
    sign_C4 = np.sign(A_grid - tr_M_p_paper)
    for i in range(len(a_grid) - 1):
        if sign_C4[i] * sign_C4[i+1] < 0:
            try:
                a_C4 = optimize.brentq(lambda a: A_of(a) - tr_M_p_paper,
                                        a_grid[i], a_grid[i+1])
                A_C4 = A_of(a_C4)
                m_p_C4 = borromean * A_C4 * M_E_MEV
                print(f"      a = {a_C4:.10f}, A = {A_C4:.6f}")
                print(f"      m_p = {m_p_C4:.4f} MeV, residual = "
                      f"{(m_p_C4 - M_P_MEV)/M_P_MEV*100:+.4f}%")
                print(f"      vs target {a_post_hoc:.4f}: ratio = {a_C4 / a_post_hoc:.4f}")
                results.append({"criterion": "C4 A(a) = tr_M(p)_paper",
                               "a": float(a_C4),
                               "m_p_pred": float(m_p_C4),
                               "ratio_to_post_hoc": float(a_C4 / a_post_hoc)})
            except Exception as exc:
                print(f"      bracket error: {exc}")
            break
    else:
        print(f"      NO crossing in [{a_grid[0]:.3f}, {a_grid[-1]:.3f}]")
    print()

    # ── C5: ∏ dc_k/dz structural features on real axis ───────────
    print(f"  C5. Integrand ∏ dc_k/dz structural features:")
    z_grid = np.linspace(0.05, z_mark + 0.05, 500)
    integrand_vals = np.array([integrand_baryon(z) for z in z_grid])
    d_integrand = np.gradient(integrand_vals, z_grid)
    # Find zeros (sign changes)
    zeros = [i for i in range(len(integrand_vals)-1)
             if integrand_vals[i] * integrand_vals[i+1] < 0]
    print(f"      Real-axis zeros of ∏ dc_k/dz (in physical interval):")
    if zeros:
        for idx in zeros[:5]:
            print(f"        z_zero ≈ {z_grid[idx]:.6f}, integrand = {integrand_vals[idx]:.4f}")
            a_C5 = z_grid[idx]
            m_p_C5 = m_p_of(a_C5)
            results.append({"criterion": f"C5 integrand_zero at z = {z_grid[idx]:.4f}",
                           "a": float(a_C5),
                           "m_p_pred": float(m_p_C5),
                           "ratio_to_post_hoc": float(a_C5 / a_post_hoc)})
    else:
        print(f"        NONE — integrand doesn't change sign in (0.05, z_markov]")
    # Extrema of the integrand
    extrema_int = [i for i in range(1, len(d_integrand)-1)
                   if d_integrand[i] * d_integrand[i+1] < 0]
    print(f"      Real-axis extrema of ∏ dc_k/dz:")
    if extrema_int:
        for idx in extrema_int[:5]:
            print(f"        z_ext ≈ {z_grid[idx]:.6f}, value = {integrand_vals[idx]:.4f}")
    print()

    # ── C6: ν_SDP · A · |tr_M| = some target ─────────────────────
    # Per prop:operator-selection-lp: x_star · t = primal_obj
    # In our context: A · |tr_M| · m_e (in some normalization)
    # could equal a specific substrate value.
    # Specifically: per ρ_K · m_e · |tr_M| = m_p, and A enters as
    # A · m_e · borromean ≈ m_p.  Look for a where:
    #   A(a) = (m_p_CODATA / m_e / borromean) — but this is CODATA-anchored, circular
    # OR: A(a) · ν_SDP = some clean categorical ratio
    # Test: A(a) = 8G / ℏ_q² = Vol(Borromean)/ℏ_q² · (some factor)
    # That gives back borromean factor itself: ~747 — way too big
    # Try: A(a) = q_int(2) = [2]_q = 2.011
    target_C6 = 2.011  # [2]_q
    print(f"  C6. A(a) = [2]_q = {target_C6:.4f} (Wenzl-bridge identity):")
    sign_C6 = np.sign(A_grid - target_C6)
    for i in range(len(a_grid) - 1):
        if sign_C6[i] * sign_C6[i+1] < 0:
            try:
                a_C6 = optimize.brentq(lambda a: A_of(a) - target_C6, a_grid[i], a_grid[i+1])
                A_C6 = A_of(a_C6)
                m_p_C6 = borromean * A_C6 * M_E_MEV
                print(f"      a = {a_C6:.10f}")
                print(f"      m_p = {m_p_C6:.4f} MeV")
                results.append({"criterion": "C6 A(a) = [2]_q",
                               "a": float(a_C6),
                               "m_p_pred": float(m_p_C6),
                               "ratio_to_post_hoc": float(a_C6 / a_post_hoc)})
            except Exception as exc:
                print(f"      bracket error: {exc}")
            break

    # Other candidate targets for A:
    print()
    print(f"  C6b. Various A-target candidates:")
    for label, target in [
        ("[2]_q", 2.011),
        ("[3]_q / b", 3.044 / 0.868),
        ("[2]_q · cos(π/3)", 2.011 * 0.5),
        ("q + 1/q", q0 + 1/q0),
        ("Vol_4_1 (figure-8 vol)", 2.030),
        ("Vol_4_1 · 1.2", 2.030 * 1.2),
        ("c_q · ℏ_q", 1/(q0-1) * (q0-1)/q0),  # = 1/q
        ("3 · b", 3 * 0.868),
    ]:
        sign_arr = np.sign(A_grid - target)
        for i in range(len(a_grid) - 1):
            if sign_arr[i] * sign_arr[i+1] < 0:
                try:
                    a_target = optimize.brentq(lambda a: A_of(a) - target, a_grid[i], a_grid[i+1])
                    m_p_target = m_p_of(a_target)
                    err_pct = (m_p_target - M_P_MEV) / M_P_MEV * 100
                    marker = " ← MATCH" if abs(a_target - a_post_hoc) / a_post_hoc < 0.01 else ""
                    print(f"      A = {label:25s} (={target:.4f})  →  a = {a_target:.6f}  "
                          f"m_p = {m_p_target:.3f} MeV, res = {err_pct:+.4f}%{marker}")
                    break
                except Exception:
                    pass

    # Final summary
    print()
    print("  Summary table:")
    print(f"  {'criterion':50s} {'a':>12s} {'m_p (MeV)':>12s} {'ratio':>8s}")
    print("  " + "-" * 86)
    for r in results:
        print(f"  {r['criterion']:50s} {r['a']:>12.6f} "
              f"{r['m_p_pred']:>12.4f} {r['ratio_to_post_hoc']:>8.4f}")
    print()

    # Find best match to a_post_hoc
    if results:
        best = min(results, key=lambda r: abs(r["a"] - a_post_hoc))
        print(f"  Closest criterion to post-hoc a = {a_post_hoc:.6f}:")
        print(f"    {best['criterion']}")
        print(f"    a = {best['a']:.6f}, residual = "
              f"{(best['a'] - a_post_hoc)/a_post_hoc*100:+.4f}%")

    # Witness
    w = (WitnessBuilder("probe-a-selection-criteria",
                         engine="scipy+numpy")
         .set_description("Test categorical selection criteria for `a` in (0, z_markov)"))
    w.add_data("q_0", q0)
    w.add_data("z_markov", z_mark)
    w.add_data("a_post_hoc", a_post_hoc)
    w.add_data("criteria_tested", results)
    if results:
        best = min(results, key=lambda r: abs(r["a"] - a_post_hoc))
        w.add_data("closest_to_post_hoc", best)
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
