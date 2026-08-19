"""Closed form of the meson EM correction: (1+ℏ_q−ℏ_q²/2) = (3q²−1)/(2q²).

The merged #1442 showed the meson m_K²/m_π² closes to 0.056 ppm via:

  m_K²/m_π² = [3]_q·[4]_q + (α_em/π)·(1 + ℏ_q − ℏ_q²/2)

with (1 + ℏ_q − ℏ_q²/2) the leading two terms of `1 + log(1+ℏ_q)`.
This probe identifies the CLOSED-FORM identity behind that truncation:

  1 + ℏ_q − ℏ_q²/2  =  1 + (1 − q⁻²)/2  =  (3 − q⁻²)/2  =  (3q² − 1)/(2q²).

The form `(3q² − 1)/(2q²)` is a rational polynomial in q⁻² with
coefficients (3, −1) — not a series truncation. The "3" is the
number of quark/lepton generations (T(2,3), T(2,5), T(2,7) — three
saturating torus knots on Bring's surface, per em-coupling-projection
Diophantine uniqueness). The 1/q² is the substrate's squared inverse
Planck.

This brings the meson sector to a single closed-form derived expression:

  m_K²/m_π² = [3]_q · [4]_q  +  (α_em / π) · (3q² − 1)/(2q²)
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_K_PM_MEV_VALIDATION, M_PI_PM_MEV_VALIDATION  # noqa: E402 (codata sweep)
import sys
import time
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def q_int(k, q):
    return (q**k - q**(-k)) / (q - 1/q)


def _alpha_em_inv_derived(q, order=None):
    """Framework-derived α_em⁻¹ — the bare force-carrier coupling dressed by
    the Chern–Simons tower, computed at full working precision.

    Mirrors `pyhecke.constants.ALPHA_EM_INV_DERIVED` (which evaluates in
    float64) but keeps everything in mpmath so the meson closure is not
    silently capped at double precision.

    `order` is the truncation order of the CS tower:
      order 0 → bare
      order 1 → bare·(1 + c₁)
      order 2 → bare·(1 + c₁ + c₁²·κ_gram)          [canonical / shipped]
      order n → adds c₁ⁿ·κ_gram^{n−1}                (geometric continuation)
      order None → EXACT resummation 1 + c₁/(1 − c₁κ)  [default]

    The tower is geometric with ratio c₁·κ, so it sums in closed form and
    needs no truncation at all. `order` is retained only so the sweep below
    can show that the truncated values converge onto the exact one.
    """
    pi = mp.pi
    qi = 1 / q
    bare = q * q_int(9, q) * q_int(10, q)

    # CS invariants of the two genus-4 force-carrier torus knots.
    # CS(T_{m,n}) = π²(m²−1)(n²−1)/(12mn)
    cs_29 = pi**2 * mp.mpf(10) / 9
    cs_35 = pi**2 * mp.mpf(16) / 15
    n2 = q_int(2, q)
    c1 = (cs_29 + cs_35) * (n2 / 2) * (1 - qi)**2 / bare

    # Gram matrix of the CS pairing — classical vs q-deformed.
    sl, linking = 8, 17          # self-linking (m−1)(n−1); |2·5 − 3·9|
    g_cl_11 = cs_29 + pi**2 * sl**2 / mp.mpf(2 * 9)**2
    g_cl_22 = cs_35 + pi**2 * sl**2 / mp.mpf(3 * 5)**2
    g_cl_12 = pi**2 * linking**2 / (mp.mpf(2 * 9) * (3 * 5))
    det_cl = g_cl_11 * g_cl_22 - g_cl_12**2

    lk_q = abs(n2 * q_int(5, q) - q_int(3, q) * q_int(9, q))
    cs_q_29 = pi**2 * (n2**2 - 1) * (q_int(9, q)**2 - 1) / (12 * n2 * q_int(9, q))
    cs_q_35 = (pi**2 * (q_int(3, q)**2 - 1) * (q_int(5, q)**2 - 1)
               / (12 * q_int(3, q) * q_int(5, q)))
    sl_q_29 = (n2 - 1) * (q_int(9, q) - 1)
    sl_q_35 = (q_int(3, q) - 1) * (q_int(5, q) - 1)
    g_q_11 = cs_q_29 + pi**2 * sl_q_29**2 / (n2 * q_int(9, q))**2
    g_q_22 = cs_q_35 + pi**2 * sl_q_35**2 / (q_int(3, q) * q_int(5, q))**2
    g_q_12 = pi**2 * lk_q**2 / (n2 * q_int(9, q) * q_int(3, q) * q_int(5, q))
    det_q = g_q_11 * g_q_22 - g_q_12**2

    kappa_gram = det_cl / det_q

    if order is None:
        tower = 1 + c1 / (1 - c1 * kappa_gram)      # exact, all orders
    else:
        tower = mp.mpf(1)
        for k in range(1, order + 1):
            tower += c1**k * kappa_gram**(k - 1)
    return bare * tower



def alpha_em_inv_derived(q, order=None):
    """Public entry point for the framework-derived alpha_em^-1.

    Same computation as `_alpha_em_inv_derived`, exported so other producers
    import the derivation instead of copying its VALUE. Two of them were
    carrying the literal `mp.mpf("137.035944")` -- the MUON-anchor evaluation
    from before the 2026-05-28 proton re-pin, 65.0 ppb from what this returns
    at the current pin. A value copied across module boundaries cannot follow
    a re-pin; a call can.
    """
    return _alpha_em_inv_derived(q, order=order)

def main():
    _t0 = time.perf_counter()
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    hbar_q = (q - 1)/q
    qi2 = 1/q**2

    # Closed-form candidates — verify they ALL equal the same value.
    series_form     = 1 + hbar_q - hbar_q**2/2
    closed_form_1   = 1 + (1 - qi2)/2
    closed_form_2   = (3 - qi2)/2
    closed_form_3   = (3*q**2 - 1)/(2*q**2)

    print("=" * 70)
    print("  Closed form of (1 + ℏ_q − ℏ_q²/2)")
    print("=" * 70)
    print()
    print("  Verifying the chain of equalities at q₀:")
    print(f"    1 + ℏ_q − ℏ_q²/2     = {mp.nstr(series_form, 20)}")
    print(f"    1 + (1 − q⁻²)/2      = {mp.nstr(closed_form_1, 20)}")
    print(f"    (3 − q⁻²)/2          = {mp.nstr(closed_form_2, 20)}")
    print(f"    (3q² − 1)/(2q²)      = {mp.nstr(closed_form_3, 20)}")
    print()
    # All differences must be zero (modulo numerical precision):
    diff_1 = abs(series_form - closed_form_1)
    diff_2 = abs(closed_form_1 - closed_form_2)
    diff_3 = abs(closed_form_2 - closed_form_3)
    print(f"  |series_form − closed_form_1|    = {float(diff_1):.2e}")
    print(f"  |closed_form_1 − closed_form_2|  = {float(diff_2):.2e}")
    print(f"  |closed_form_2 − closed_form_3|  = {float(diff_3):.2e}")
    print(f"  (all should be 0 at machine precision — ring identity)")
    print()

    # ---------------------------------------------------------------
    # Use the closed form to close m_K²/m_π² at sub-ppm
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  Full meson closure form (single closed-form derived expression)")
    print("-" * 70)
    print()
    # α_em is DERIVED, never imported. Previously this line hardcoded the
    # literal mp.mpf("137.035944") — the CS-corrected value copied in as a
    # constant. A hardcoded literal sitting a few hundred ppb from CODATA is
    # exactly the pattern the canonical-watcher flags, and it made the meson
    # closure depend on a number the script did not compute.
    #
    # We now build the same quantity from the framework's own objects:
    #   bare      = q·[9]_q·[10]_q                      (force-carrier crossings)
    #   c₁        = (CS(T₂,₉)+CS(T₃,₅))·([2]_q/2)·ℏ_q²/bare
    #   κ_gram    = det G_classical / det G_q-deformed
    #   α_em⁻¹    = bare·(1 + c₁/(1 − c₁·κ_gram))      EXACT, all orders
    #
    # NOTE ON ORDER: the correction tower Σ_{j≥1} c₁ʲκ^{j−1} is geometric with
    # ratio c₁·κ ≈ 2.7e-3, so it sums in closed form — there is no truncation
    # and no order parameter to get wrong. `pyhecke` historically shipped the
    # order-2 Taylor polynomial `1 + c₁ + c₁²κ`; that cost 11.06 ppb and is
    # now fixed there too.
    #
    # The residual that survives exact resummation is ≈ −467.6 ppb against
    # CODATA 137.035999177. That is STRUCTURAL — no further orders exist to
    # add. The order sweep below exhibits the convergence onto the exact value.
    alpha_em_inv = _alpha_em_inv_derived(q)          # exact resummation
    alpha_em = 1 / alpha_em_inv
    m_pi = mp.mpf(M_PI_PM_MEV_VALIDATION)
    m_K  = mp.mpf(M_K_PM_MEV_VALIDATION)
    prod_34 = q_int(3, q) * q_int(4, q)
    em_factor = closed_form_3  # (3q² − 1)/(2q²)
    prediction = prod_34 + alpha_em/mp.pi * em_factor
    measured = (m_K / m_pi)**2
    miss_ppm = float((prediction - measured)/measured) * 1e6

    print(f"  m_K²/m_π² = [3]_q · [4]_q  +  (α_em / π) · (3q² − 1)/(2q²)")
    print()
    print(f"    α_em⁻¹ (DERIVED, exact resummation) = {mp.nstr(alpha_em_inv, 15)}")
    print(f"    [3]_q · [4]_q         = {float(prod_34):.6f}")
    print(f"    (α_em / π) · em_factor = {float(alpha_em/mp.pi * em_factor):.6f}")
    print(f"    prediction             = {float(prediction):.6f}")
    print(f"    measured  (PDG)        = {float(measured):.6f}")
    print(f"    full miss              = {miss_ppm:+.3f} ppm  ({miss_ppm*1e3:+.1f} ppb)")
    print()

    # ---------------------------------------------------------------
    # Order sensitivity of the CS tower — is the residual a truncation
    # artifact, or structural?
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  CS-tower order sensitivity (is the residual a truncation?)")
    print("-" * 70)
    print()
    order_rows = []
    for k in (0, 1, 2, 3, 6, 12, None):
        a_inv_k = _alpha_em_inv_derived(q, order=k)
        pred_k = prod_34 + (1 / a_inv_k) / mp.pi * em_factor
        ppb_k = float((pred_k - measured) / measured) * 1e9
        order_rows.append((k, float(a_inv_k), ppb_k))
        tag = ("  <-- EXACT (canonical)" if k is None
               else "  <-- old truncation" if k == 2 else "")
        label = "exact" if k is None else f"{k:5d}"
        print(f"    order {label:>5s}:  α_em⁻¹ = {float(a_inv_k):.9f}   "
              f"m_K²/m_π² miss = {ppb_k:+10.1f} ppb{tag}")
    print()
    print("    The tower is geometric with ratio c₁·κ_gram ≈ 2.7e-3, so it")
    print("    CONVERGES — but not onto the measurement. The residual that")
    print("    survives resummation is structural, not a truncation artifact.")
    print()

    # ---------------------------------------------------------------
    # Structural reading: 3 generations + substrate inverse Planck²
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  Structural reading of (3q² − 1)/(2q²)")
    print("-" * 70)
    print()
    print("  Numerator 3q² − 1:")
    print("    • 3 is the number of saturating-genus generation torus knots")
    print("      on Bring's surface (T(2,3), T(2,5), T(2,7) — gen 1/2/3).")
    print("    • q² is the substrate's squared coupling parameter.")
    print("    • −1 is the unit subtraction (= q²·q⁻² when normalising the")
    print("      LO Planck-quantum-squared correction).")
    print("  Denominator 2q²:")
    print("    • 2 is the standard EM-self-energy halving (Casimir factor).")
    print("    • q² puts everything on the substrate-natural scale.")
    print()
    print("  ⟹ structural form: (3 generations · substrate − unit) / (2 ·")
    print("    substrate²). Consistent with the EM channel being the sinh/")
    print("    Coulomb part of #1417's [n]_q = sinh(nλ)/sinh(λ) decomposition")
    print("    (sinh = Coulomb), and with the framework's three-generation")
    print("    saturation on Bring's surface.")
    print()

    w = WitnessBuilder("meson-em-sinh-closed-form", engine="mpmath",
                       start_time=_t0)
    w.set_description(
        f"Closed-form identity (1 + ℏ_q − ℏ_q²/2) = (3q² − 1)/(2q²), "
        f"verified at q₀ to machine precision. Full meson m_K²/m_π² "
        f"closure form: [3]_q[4]_q + (α_em/π)·(3q² − 1)/(2q²). "
        f"At q₀: {miss_ppm:+.3f} ppm. The numerator 3q²−1 reflects 3 "
        f"generations + substrate; denominator 2q² is the standard "
        f"EM-self-energy halving on the substrate-natural scale."
    )
    w.set_audit_only("docs/audits/2026-05-28-meson-mass-ratio-derived-vs-fitted.md")
    w.add_data("series_form_at_q0", str(mp.nstr(series_form, 20)))
    w.add_data("closed_form_at_q0", str(mp.nstr(closed_form_3, 20)))
    w.add_data("ring_identity_residual", float(diff_3))
    w.add_data("full_meson_miss_ppm", miss_ppm)
    w.add_data("alpha_em_inv_derived_exact", str(mp.nstr(alpha_em_inv, 15)))
    w.add_data("alpha_em_source", "derived (q·[9]_q·[10]_q dressed by the CS "
                                  "tower); NOT the experimental value")
    w.add_data("cs_tower_order_sweep",
               [{"order": ("exact" if k is None else k),
                 "alpha_em_inv": a, "meson_miss_ppb": p}
                for k, a, p in order_rows])
    w.add_data("cs_tower_converges_but_not_to_measurement", True)
    w.add_assertion("closed_form_ring_identity",
                    computed=1 if float(diff_3) < 1e-30 else 0,
                    expected=1, tolerance=0,
                    source="(1+ℏ_q−ℏ_q²/2) = (3q²−1)/(2q²) at machine precision")
    w.add_assertion("meson_sub_ppm",
                    computed=1 if abs(miss_ppm) < 1 else 0,
                    expected=1, tolerance=0,
                    source="full m_K²/m_π² closure < 1 ppm with closed form")
    print(f"  Witness: {w.save()}")


if __name__ == "__main__":
    main()
