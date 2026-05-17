"""
probe_a_interval_transitions.py — sweep `a` over (0, z_markov] to find:
  - transition points (Stokes lines crossing real axis)
  - stable/extremum points in m_p_pred(a)
  - LP vs SDP comparison (is full SDP overkill?)

Per owner: "on (0, z_markov] there must be a transition point. is
there a stable or maximal point in that interval. give more math
and physics context for a. are we making more complicated... LP or
shadow prices?"

This probe sweeps the integration limit `a` and analyses:

  1. m_p_pred(a) — first and second derivative; any interior
     stable points?

  2. A(q₀, a) — the amplification factor; where does it extremize?

  3. Stokes-line intersections — the discriminant roots z_c⁻,
     z_c⁺ are at 0.106 ± 0.937i.  The Stokes lines (curves of
     constant Im(S)) cross the real axis at specific points;
     these are the natural transitions.

  4. LP-only version (no PSD constraint on the std block,
     instead use eigenvalue inequalities directly).  Does LP
     give the same a_optimum = z_markov?
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
import numpy as np
from scipy import integrate
import cvxpy as cp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from picard_lefschetz_thimble import (
    cubic_roots, dF_dc, dF_dz, sw_3root_product_degree1, find_discriminant_roots,
)
from joint_tower_sdp_solver_v2 import (
    trivial_rep_of_braid, sign_rep_of_braid, represent_braid_in_h3_standard,
)
from q_parameter import Q as q0, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, VOL_BORROMEAN

borromean = VOL_BORROMEAN / (HBAR_Q ** 2)
z_mark = 1 / (np.sqrt(q0) + np.sqrt(1.0 / q0))
z_0 = np.sqrt(q0) - np.sqrt(1.0 / q0)
hbar_q = (q0 - 1) / q0
proton_word = [1, -2, 1, -2, 1, -2]


def m_p_at(a_val):
    """m_p_pred(a) and A(q₀, a) for given integration limit a."""
    e_ref, _ = integrate.quad(
        lambda z: float(np.real(cubic_roots(z)[np.argmin(np.abs(cubic_roots(z).imag))] + z)),
        -a_val, a_val, limit=200)
    prod_re, _ = integrate.quad(
        lambda z: float(np.real(sw_3root_product_degree1(z))),
        -a_val, a_val, limit=200)
    A = abs(prod_re) / abs(e_ref) if abs(e_ref) > 1e-15 else float("nan")
    mp_pred = borromean * A * M_E_MEV
    return mp_pred, A


def main() -> int:
    print("=" * 78)
    print("  a-interval sweep: transitions, stable points, LP vs SDP")
    print("=" * 78)
    print(f"  q_0 = {q0:.10f}, z_markov = {z_mark:.6f}, z_0 = {z_0:.6f}")
    print()

    # ── Step 1: sweep m_p_pred(a) over (0, z_markov + ε] ──────────
    print("  Step 1: Sweep m_p_pred(a) — find extrema, transitions")
    print("  " + "-" * 66)
    a_values = np.linspace(0.01, z_mark + 0.01, 60)
    m_p_values = []
    A_values = []
    for a_val in a_values:
        mp_pred, A = m_p_at(a_val)
        m_p_values.append(mp_pred)
        A_values.append(A)
    m_p_arr = np.array(m_p_values)
    A_arr = np.array(A_values)
    a_arr = np.array(a_values)
    # First derivative dm_p/da
    dm_p_da = np.gradient(m_p_arr, a_arr)
    # Second derivative d²m_p/da²
    d2m_p_da2 = np.gradient(dm_p_da, a_arr)

    # Find sign changes in second derivative (inflection points)
    inflection_idx = [i for i in range(1, len(d2m_p_da2)-1)
                      if d2m_p_da2[i-1] * d2m_p_da2[i+1] < 0]
    print(f"    Sweep range: a ∈ [{a_arr[0]:.4f}, {a_arr[-1]:.4f}], {len(a_arr)} points")
    print(f"    m_p range:   [{m_p_arr.min():.3f}, {m_p_arr.max():.3f}] MeV")
    print(f"    A range:     [{A_arr.min():.6f}, {A_arr.max():.6f}]")
    print(f"    d²m_p/da² inflection points (where curvature flips sign):")
    if inflection_idx:
        for idx in inflection_idx:
            print(f"      a = {a_arr[idx]:.6f}, m_p = {m_p_arr[idx]:.4f} MeV, "
                  f"d²/da² ≈ {d2m_p_da2[idx]:.2e}")
    else:
        print(f"      NONE in the sweep — m_p_pred(a) is convex/concave throughout")
    print()
    print(f"    m_p = CODATA crossings:")
    for i in range(len(a_arr)-1):
        if (m_p_arr[i] - M_P_MEV) * (m_p_arr[i+1] - M_P_MEV) < 0:
            # Linear interpolation
            alpha = (M_P_MEV - m_p_arr[i]) / (m_p_arr[i+1] - m_p_arr[i])
            a_cross = a_arr[i] + alpha * (a_arr[i+1] - a_arr[i])
            print(f"      m_p_pred(a={a_cross:.6f}) ≈ CODATA")
    print()

    # ── Step 2: Find Stokes-line real-axis crossings ──────────────
    print("  Step 2: Stokes-line analysis")
    print("  " + "-" * 66)
    print("    Discriminant roots z_c (complex saddles of S):")
    z_cs_raw = find_discriminant_roots()
    z_cs = []
    for item in (z_cs_raw if hasattr(z_cs_raw, '__iter__') else [z_cs_raw]):
        if hasattr(item, '__len__') and not isinstance(item, complex):
            for sub in item:
                z_cs.append(complex(sub))
        else:
            z_cs.append(complex(item))
    z_cs = [z for z in z_cs if abs(z.imag) > 1e-6][:6]  # complex pairs
    print(f"      Found {len(z_cs)} complex saddles")
    for zc in z_cs:
        print(f"      {zc.real:+.6f}{zc.imag:+.6f}i")
    print()
    # Compute action S at each saddle (real and imag parts)
    # S(z_c) is the value of the action at the saddle.
    # For SW action S = ∫^z λ_SW(z') dz', we need to numerically
    # integrate from 0 to z_c.
    def S_at(z_target):
        try:
            def integrand_real(t):
                z = t * z_target  # parametrise 0 → z_target
                cs = cubic_roots(z)
                c = cs[np.argmin(np.abs(cs.imag))]
                denom = dF_dc(z, c)
                if abs(denom) < 1e-15:
                    return 0.0
                return float(np.real(-dF_dz(z, c) / denom * z_target))
            def integrand_imag(t):
                z = t * z_target
                cs = cubic_roots(z)
                c = cs[np.argmin(np.abs(cs.imag))]
                denom = dF_dc(z, c)
                if abs(denom) < 1e-15:
                    return 0.0
                return float(np.imag(-dF_dz(z, c) / denom * z_target))
            real_part, _ = integrate.quad(integrand_real, 0, 1, limit=100)
            imag_part, _ = integrate.quad(integrand_imag, 0, 1, limit=100)
            return complex(real_part, imag_part)
        except Exception:
            return complex("nan", "nan")

    print("    Action S(z_c) per saddle:")
    Ss = []
    for zc in z_cs[:4]:
        S_val = S_at(zc)
        Ss.append(S_val)
        print(f"      z_c = {zc.real:+.4f}{zc.imag:+.4f}i  →  Re(S) = {S_val.real:+.6f}, "
              f"Im(S) = {S_val.imag:+.6f}")
    print()
    print("    Stokes lines: curves of constant Im(S).  Two saddles z_c1,")
    print("    z_c2 are on the SAME Stokes line iff Im(S(z_c1)) = Im(S(z_c2)).")
    if len(Ss) >= 2:
        for i in range(len(Ss)):
            for j in range(i+1, len(Ss)):
                diff = abs(Ss[i].imag - Ss[j].imag)
                if diff < 0.1:  # rough tolerance
                    print(f"      Saddles {i}, {j}: |ΔIm(S)| = {diff:.4f} — close (Stokes-related)")
    print()

    # ── Step 3: LP-only version (no PSD constraint) ───────────────
    print("  Step 3: LP-only version (replace PSD(P_21) with eigenvalue ≥ 0)")
    print("  " + "-" * 66)

    # Compute eigenvalues of sym(ρ_(2,1)(β_p)) numerically
    M = represent_braid_in_h3_standard(proton_word, q0)
    M_sym = (M + M.T) / 2
    eigs = np.linalg.eigvalsh(M_sym)
    chi_3 = trivial_rep_of_braid(proton_word, q0)
    chi_111 = sign_rep_of_braid(proton_word, q0)
    chi_21 = float(np.trace(M))

    qfact_3 = 1
    for k in range(1, 4):
        qfact_3 *= (q0**k - q0**(-k)) / (q0 - 1/q0)
    y_3 = 1/qfact_3
    y_21 = ((q0**2 - q0**(-2))/(q0 - 1/q0))**2 / qfact_3
    y_111 = 1/qfact_3

    alpha_3 = cp.Variable(nonneg=True, name="alpha_3")
    alpha_21 = cp.Variable(nonneg=True, name="alpha_21")
    alpha_111 = cp.Variable(nonneg=True, name="alpha_111")
    a_var = cp.Variable(nonneg=True, name="a")

    # LP-only constraints (no matrix variable)
    constraints_lp = [
        alpha_3 + alpha_21 + alpha_111 == 1,
        alpha_3 == alpha_111,
        # Eigenvalue-positivity replacement for PSD: both eigenvalues ≥ 0
        # (automatic since they're 0.973, 1.021 — both positive)
        alpha_21 * eigs[0] >= 0,  # trivial since eigs[0] > 0
        alpha_21 * eigs[1] >= 0,
        # Markov pair-trace constraint
        alpha_3 * y_3 * chi_3 + alpha_21 * y_21 * chi_21 + alpha_111 * y_111 * chi_111
        >= z_mark**2 * (alpha_3 + alpha_21 + alpha_111),
        # Integration-limit consistency
        a_var * 4 <= alpha_21 * (eigs[0] + eigs[1]) + alpha_3 + alpha_111,
    ]
    prob_lp = cp.Problem(cp.Maximize(a_var), constraints_lp)
    prob_lp.solve(solver=cp.HIGHS, verbose=False)

    print(f"    LP status:   {prob_lp.status}")
    print(f"    LP optimal a: {a_var.value:.10f}")
    print(f"    LP α_3:       {alpha_3.value:.10f}")
    print(f"    LP α_(2,1):   {alpha_21.value:.10f}")
    print(f"    LP α_(1,1,1): {alpha_111.value:.10f}")
    print()
    print(f"    Compare:")
    print(f"      SDP a:     ≈ 0.4985 (z_markov)")
    print(f"      LP a:      {a_var.value:.4f}")
    print(f"      Same? {abs(a_var.value - z_mark) < 0.01}")
    print()

    # Shadow prices (dual variables)
    print("    LP shadow prices (dual variables):")
    for c in constraints_lp:
        if hasattr(c, 'dual_value') and c.dual_value is not None:
            dv = c.dual_value
            try:
                print(f"      {str(c)[:60]:60s} → y = {float(dv):+.6f}")
            except (TypeError, ValueError):
                print(f"      {str(c)[:60]:60s} → y = {dv}")
    print()

    # ── Step 4: Physics interpretation ────────────────────────────
    print("  Step 4: Physics / math context for `a`")
    print("  " + "-" * 66)
    print("""    `a` is the real-axis cutoff for the prolonged SW differential
    λ_SW^(1) = dc/dz on the color-tube cubic.  Physically:

      - z is the spacetime affine coordinate on Bring's curve
      - c(z) is the color-tube root at coordinate z (the proton's
        chiral fibre at that point)
      - λ_SW^(1) = dc/dz is the rate-of-change of color along z
      - The action S = ∫^z λ_SW dz is the "Hecke energy" of a
        configuration extending in spacetime

    The integration over z ∈ [-a, +a] computes the proton's mass
    contribution from the spacetime PATCH of half-extent a.

    BOUNDS on a:
      - LOWER: a should be ≥ Re(z_c) ≈ 0.106 (the nearest saddle's
        real part).  Below this, the integration misses the
        dominant saddle's contribution.
      - UPPER: a is bounded by where the integrand picks up
        contributions from OTHER saddles via Stokes phenomena.
        For the QOU cubic, this is approximately z_markov ≈ 0.499.

    So `a` ∈ [0.106, 0.499] is the PHYSICAL range.  Within this:
      - a = 0.388 (post-hoc fit) is at 65% of the interval
      - a = 0.450 (1/(2q)) is at 87%
      - a = 0.499 (z_markov, SDP max) is at 100%

    No simple structural value gives EXACTLY 0.388.  The integration
    must be determined by ADDITIONAL physics:
      - WHERE the chiral-fibre's contribution to mass STABILIZES
        (a STABLE point in some functional)
      - OR where a Stokes line crosses the real axis
      - OR where the SDP gap closes uniquely (with more constraints)
""")

    # Witness
    w = (WitnessBuilder("probe-a-interval-transitions",
                         engine="cvxpy+scipy+numpy")
         .set_description("Sweep `a` interval, find transitions, LP vs SDP comparison"))
    w.add_data("q_0", q0)
    w.add_data("a_interval", {"lower": float(a_arr[0]), "upper": float(a_arr[-1]),
                                "z_markov": float(z_mark),
                                "z_0": float(z_0), "hbar_q": float(hbar_q)})
    w.add_data("sweep_m_p", {"a": a_arr.tolist(), "m_p": m_p_arr.tolist(),
                              "A": A_arr.tolist()})
    w.add_data("m_p_arr_summary", {
        "min": float(m_p_arr.min()),
        "max": float(m_p_arr.max()),
        "monotonic_increasing": bool(np.all(np.diff(m_p_arr) > 0)),
        "interior_extrema": len(inflection_idx),
    })
    w.add_data("discriminant_roots_complex", [
        {"re": float(zc.real), "im": float(zc.imag)} for zc in z_cs[:4]
    ])
    w.add_data("actions_at_saddles", [
        {"saddle": i, "Re_S": float(s.real), "Im_S": float(s.imag)}
        for i, s in enumerate(Ss[:4]) if not np.isnan(s.real)
    ])
    w.add_data("lp_only_optimum", {
        "status": prob_lp.status,
        "a": float(a_var.value),
        "alpha_3": float(alpha_3.value) if alpha_3.value else None,
        "alpha_21": float(alpha_21.value) if alpha_21.value else None,
        "alpha_111": float(alpha_111.value) if alpha_111.value else None,
        "matches_sdp": bool(abs(a_var.value - z_mark) < 0.01) if a_var.value else False,
    })
    w.add_data("physics_interpretation",
               "a is the real-axis cutoff for the prolonged SW differential "
               "λ_SW = dc/dz on the color-tube cubic.  Physical range: "
               "[Re(z_c) ≈ 0.106, z_markov ≈ 0.499].  Post-hoc 0.388 sits "
               "at 65 % of this interval but has no obvious structural "
               "interpretation.")
    w.add_assertion("lp_matches_sdp_optimum",
                    computed=1.0 if abs(a_var.value - z_mark) < 0.01 else 0.0,
                    expected=1.0)
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
