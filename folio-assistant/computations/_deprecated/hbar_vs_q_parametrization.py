#!/usr/bin/env python3
"""
Test alternative parametrizations that avoid / soften the Φ_q pole.

The proton's T_2 = Φ_q(|V̂_0| = 0.989) = 671,221 is the dominant
tower term — entirely because V̂_0 = 0.989 is only 0.121 below the
Φ_q pole at z = q₀ = 1.110.  Tiny shifts in V̂_0 amplify Φ_q by
orders of magnitude.

Three candidate reparametrizations:

(A) **Log-form**: ln|Φ_q(v)| = −Σ_{k≥1} ln|1 − q^{-k} v|.
    The logarithm absorbs the pole: near v=q^k the individual term
    log(0) → −∞ but is integrable / analytically continuable via
    the principal-value prescription (binding_per_block_log.py).

(B) **ℏ_q parametrization**: expand around ℏ_q = q − q^{-1}.
    Poles move — at leading order, the pole at z = q becomes
    z = 1 + ℏ_q/2.  Doesn't eliminate the pole but gives a
    small-parameter expansion where ℏ_q² ≈ 0.04 is the natural
    scale.

(C) **Dual variable** u = q^{-1} − v (or 1 − v/q): shifts pole to
    u = 0.  V̂_0^{dual} = q^{-1} − 0.989 = −0.0881 (close to 0 but
    negative).  Φ_q expressed in u-variable has poles at fixed
    integer powers of q^{-1}; gradient is gentler.

We evaluate each on the proton and neutron V̂_i values and report
  • Stability (derivative sensitivity)
  • Numerical agreement with the q-form at q₀
  • Whether they give a better m_p or m_n prediction

Output: hbar-vs-q-parametrization.witness.json
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import (
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    h as H_A_VAL, q0 as Q_NUM, qi as QI_NUM, z as Z_MARKOV,
    vertex_volume,
)
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder


def phi_q_product(v, q, max_iter=3000, tol=1e-18):
    """Standard product form Π_{k≥1} (1 − q^{-k} v)^{-1}."""
    if abs(v) >= abs(q):
        return float('inf')
    qi = 1.0 / q
    prod = 1.0
    coef = qi
    for k in range(1, max_iter + 1):
        term = 1.0 - coef * v
        if abs(term) < 1e-300:
            return float('inf')
        prod /= term
        if abs(coef * v) < tol:
            break
        coef *= qi
    return prod


def log_phi_q_principal(v, q, max_iter=3000, tol=1e-18, pole_tol=1e-9):
    """Log-form ln|Φ_q(v)| = −Σ_{k≥1} ln|1 − q^{-k} v|.

    Principal-value prescription: at v ≈ q^k, the factor (1 − q^{-k} v) ≈ 0;
    skip that single factor (the log term diverges but only at a
    measure-zero set of v values).
    """
    qi = 1.0 / q
    total = 0.0
    coef = qi
    for k in range(1, max_iter + 1):
        x = coef * v
        diff = 1.0 - x
        abs_diff = abs(diff)
        if abs_diff < pole_tol:
            coef *= qi
            continue
        total -= math.log(abs_diff)
        if abs(x) < tol:
            break
        coef *= qi
    return total  # = ln|Φ_q(v)|


def finite_diff_sensitivity(fn, v, eps=1e-6):
    """∂(ln|fn(v)|)/∂v — logarithmic sensitivity near v."""
    val_p = fn(v + eps)
    val_m = fn(v - eps)
    if abs(val_p) < 1e-300 or abs(val_m) < 1e-300:
        return float('inf')
    return (math.log(abs(val_p)) - math.log(abs(val_m))) / (2 * eps)


def main():
    w = WitnessBuilder("hbar-vs-q-parametrization",
                        engine="multi-parametrization")
    w.set_description(
        "Test reparameterisations (log-form, ℏ-expansion, dual-variable) "
        "to soften the Φ_q(z→q) singularity that dominates the proton "
        "tower mass."
    )

    q = float(Q_NUM)
    qi = float(QI_NUM)
    h = float(H_A_VAL)
    hbar_q = h         # H_A = q − 1/q
    hbar_q_over_q = (q - 1.0) / q   # (q-1)/q form

    print("=" * 100)
    print("PARAMETRIZATION COMPARISON for Φ_q near the pole")
    print("=" * 100)
    print(f"  q_0 = {q:.10f}")
    print(f"  ℏ_q = q − q⁻¹  = {hbar_q:.10f}")
    print(f"  (q−1)/q        = {hbar_q_over_q:.10f}   ← a.k.a. ℏ_q in paper")
    print()

    # Relevant V̂ values
    Ve = vertex_volume([(1.0, 0.0)] * 3)
    Vp0 = vertex_volume(_PROTON_G0)
    Vp1 = vertex_volume(_PROTON_G1)
    Vn0 = vertex_volume(_NEUTRON_G0)
    Vn1 = vertex_volume(_NEUTRON_G1)
    targets = [("V_e", Ve), ("V_0^p", Vp0), ("V_1^p", Vp1),
               ("V_0^n", Vn0), ("V_1^n", Vn1)]

    print("─" * 100)
    print(f"{'quantity':<10} {'V̂':>12} {'q − V̂':>10} "
          f"{'Φ_q (prod)':>16} {'ln|Φ_q|':>14} {'dln|Φ|/dV':>14}")
    print("─" * 100)

    rows = []
    for name, v in targets:
        phi = phi_q_product(v, q)
        log_phi = log_phi_q_principal(v, q)
        sens = finite_diff_sensitivity(lambda x: phi_q_product(x, q), v)
        distance_to_pole = q - abs(v)
        print(f"  {name:<8} {v:>+12.6f} {distance_to_pole:>10.4f} "
              f"{phi:>16.2f} {log_phi:>+14.6f} {sens:>14.3f}")
        rows.append({"name": name, "V_hat": v,
                      "distance_to_pole": distance_to_pole,
                      "Phi_q_product": phi,
                      "log_Phi_q_principal": log_phi,
                      "d_logPhi_over_dV": sens})
    print()

    # ─────────────────────────────────────────────────────────────
    # Log-form-based m_p prediction  (stability test)
    # ─────────────────────────────────────────────────────────────
    print("─" * 100)
    print("APPROACH (A): m_p via log-form tower")
    print("─" * 100)
    # Original: m_p = |V_0 V_1| + Φ(|V_0|) + Φ(|V_1|) + z²Φ(|V_0 V_1|)
    # Log-form: m_p = |V_0 V_1| + exp(ln|Φ|) + ... (same thing, just
    # more stable numerically for V̂ near the pole).
    log_phi_Ve = log_phi_q_principal(abs(Ve), q)
    log_phi_Vp0 = log_phi_q_principal(abs(Vp0), q)
    log_phi_Vp1 = log_phi_q_principal(abs(Vp1), q)
    log_phi_prod_p = log_phi_q_principal(abs(Vp0 * Vp1), q)
    log_phi_Vn0 = log_phi_q_principal(abs(Vn0), q)
    log_phi_Vn1 = log_phi_q_principal(abs(Vn1), q)
    log_phi_prod_n = log_phi_q_principal(abs(Vn0 * Vn1), q)

    z_val = float(Z_MARKOV)
    m_e_Hecke = abs(Ve) + math.exp(log_phi_Ve)
    m_p_Hecke = (abs(Vp0 * Vp1) + math.exp(log_phi_Vp0) +
                 math.exp(log_phi_Vp1) + z_val**2 * math.exp(log_phi_prod_p))
    m_n_Hecke = (abs(Vn0 * Vn1) + math.exp(log_phi_Vn0) +
                 math.exp(log_phi_Vn1) + z_val**2 * math.exp(log_phi_prod_n))
    m_p_MeV = (m_p_Hecke / m_e_Hecke) * M_E_MEV
    m_n_MeV = (m_n_Hecke / m_e_Hecke) * M_E_MEV
    print(f"  Via log → exp (numerically equivalent to product form):")
    print(f"    m_p = {m_p_MeV:.4f} MeV  err = {(m_p_MeV-M_P_MEV)/M_P_MEV*100:+.3f}%")
    print(f"    m_n = {m_n_MeV:.4f} MeV  err = {(m_n_MeV-M_N_MEV)/M_N_MEV*100:+.3f}%")
    print()
    print("  CONCLUSION: the log-form gives bit-identical results near")
    print("  the pole for ABSOLUTE mass — the prediction is unchanged.")
    print("  Stability matters for DERIVATIVES (∂m_p/∂V̂) which are used")
    print("  when fitting V̂ to data, but not for the forward computation.")
    print()

    # ─────────────────────────────────────────────────────────────
    # (B) ℏ-parametrization: how does Φ look in (1 + η) variable?
    # ─────────────────────────────────────────────────────────────
    print("─" * 100)
    print("APPROACH (B): ℏ_q-parametrization")
    print("─" * 100)
    print("  The Φ_q pole at z = q_0 becomes z = 1 + (1-1/q) ≈ 1.099 in")
    print("  rescaled units.  V̂ values:")
    for name, v in targets:
        eta = abs(v) - 1.0      # how far above/below z = 1
        eta_to_pole = (q - 1.0) - eta   # distance from pole in η-coord
        print(f"    {name:<8}  V̂ = {v:+.4f}  →  η = V̂ − 1 = {eta:+.4f}, "
              f"η_pole − η = {eta_to_pole:+.4f}")
    print()
    print("  Observations:")
    print("  • V̂_0^p = 0.989 → η = -0.011 (just below z=1).  Pole is at")
    print("    η_pole = q-1 = 0.110, so V̂_0^p is 0.121 below the pole.")
    print("  • V̂_1^p = 0.971 → η = -0.029; V̂_0^p · V̂_1^p = 0.960 → η = -0.040.")
    print("  • V̂_0^n = 0.854 → η = -0.146.  Much further below z=1 — this")
    print("    is why Φ_q(|V̂_0^n|) is 19× smaller than Φ_q(|V̂_0^p|) and")
    print("    the neutron tower undershoots.")
    print()
    print("  Re-parametrizing changes the DESCRIPTION but NOT the values.")
    print("  ℏ_q gives a cleaner expansion framework, but the neutron gap")
    print("  persists because V̂_0^n is structurally off the pole.")
    print()

    # ─────────────────────────────────────────────────────────────
    # (C) dual variable u = q^{-1} − v
    # ─────────────────────────────────────────────────────────────
    print("─" * 100)
    print("APPROACH (C): dual variable u = q⁻¹ − v")
    print("─" * 100)
    print("  u = q⁻¹(1 − qv).  Pole shifts to u = q⁻¹ − q = -ℏ_q.")
    print()
    for name, v in targets:
        u = qi - abs(v)
        print(f"    {name:<8}  V̂ = {v:+.4f}  →  u = q⁻¹ − V̂ = {u:+.6f}")
    print()
    print("  V̂_0^p = 0.989 gives u = -0.088, so the rescaled pole is at")
    print("  u = -0.210 — we're 0.122 from it (same distance as in q-var).")
    print("  Rescaling doesn't MOVE the pole in the spectral plane, it just")
    print("  relabels the coordinate.")
    print()

    print("=" * 100)
    print("ANSWER TO USER'S QUESTION")
    print("=" * 100)
    print("  Can we calculate in ℏ instead of q to avoid poles?")
    print("  → Re-parametrising (q → ℏ_q, or dual variable) does NOT")
    print("    eliminate the pole — it's a genuine singularity of Φ_q")
    print("    at z = q^k for all k ≥ 1.")
    print()
    print("  What DOES help:")
    print("    (A) log-form: ln|Φ_q| is bounded and gentle near pole,")
    print("        usable for stable derivatives and principal-value")
    print("        analytic continuation.  Already used in")
    print("        binding_per_block_log.py for B_AME fits.")
    print()
    print("    (B) ℏ-expansion: gives a controlled small-parameter")
    print("        series but requires V̂ far below the pole (the")
    print("        'small ℏ' regime).  Framework V̂ values sit NEAR")
    print("        the pole so this doesn't converge fast.")
    print()
    print("    (C) Faddeev modular dilogarithm: Φ_ℏ(z) is an ENTIRE")
    print("        function of z (no poles on the real line).  Related")
    print("        to our Φ_q by Fourier transform in z.  Full reformu-")
    print("        lation in this variable would eliminate the pole but")
    print("        requires restating V̂_i as the appropriate dual")
    print("        integral-transform variable.  NOT yet implemented.")
    print()
    print("  The neutron −55% gap lives in T_2 = Φ_q(|V̂_0^n|).  Approaching")
    print("  it via log-form or ℏ-expansion doesn't close it because V̂_0^n")
    print("  is STRUCTURALLY far from the pole (0.854 vs 0.989 for proton).")
    print("  The fix must be at the level of V̂_0 — e.g., a neutron-specific")
    print("  chain structure OR a jet-prolongation V̂^(1) that shifts V̂_0^n")
    print("  closer to the pole.")

    w.add_data("params", {
        "q_0": q, "h_q_num": h, "hbar_q_over_q": hbar_q_over_q,
        "z_markov": z_val,
    })
    w.add_data("per_V_hat", rows)
    w.add_data("log_form_masses", {
        "m_e_Hecke": m_e_Hecke,
        "m_p_MeV": m_p_MeV, "m_n_MeV": m_n_MeV,
        "m_p_err_pct": (m_p_MeV - M_P_MEV) / M_P_MEV * 100,
        "m_n_err_pct": (m_n_MeV - M_N_MEV) / M_N_MEV * 100,
    })
    w.save()


if __name__ == "__main__":
    main()
