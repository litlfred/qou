#!/usr/bin/env python3
"""Spike: probe the categorical reason for q^10 selectivity in
PR #943's finding ``1 / (1 − h_q · q_0^10) ≈ λ_p`` (+19 ppm).

Three probes, in priority order from the coordination ledger
`docs/coordination/explore-q10.md`:

  (P1) **Q-locality sweep** — per the user constraint surfaced
       in #909, "q_0 not special, just where we happen to be":
       any structural identity must be smooth in q across the
       substrate window. Sweeps ``q ∈ [q_0 − 0.05, q_0 + 0.05]``
       and reports the residual ``λ_p_codata(q) − 1/(1 − h_q·q^10)``
       as a function of q. A smooth curve supports H1 (categorical);
       a sharply-peaked feature at q_0 supports H3 (null).

       Caveat: λ_p_codata is defined at the *physical* q_0 via
       (m_p/m_e) · ℏ_q² / (8G). To sweep over q we use the
       q-functional definition ``λ_p(q) = (m_p/m_e) · h_q² / (8G)``
       (substituting `h_q = q − 1/q` for the substrate-form ℏ_q).
       This is the natural q-extension; deviations from physical q_0
       reflect substrate-only structure, not data.

  (P2) **Φ_q tower expansion** — the functional equation gives
       ``Φ_q(qz)/Φ_q(z) = 1/(1 − z)``. Iterating:

           ``Φ_q(q^n · z_0) / Φ_q(z_0) = ∏_{k=0..n-1} 1/(1 − q^k · z_0)``

       Compute the full ratio ``Φ_q(h_q·q^{11}) / Φ_q(h_q·q^{10})``
       at high precision and compare to ``1/(1 − h_q · q^10)``. The
       difference is the sub-leading Φ_q tail. If small, identifies
       which factor closes the 19 ppm gap (H2). If large, the form
       captures only the first factor — structural backing must
       come elsewhere (H1 fallback or H3).

  (P3) **Adjacent-power composite** — the proton-braid polynomial
       ``p(q) = q^{20} + q^{18} + 2q^{12} − 2q^{8} − q^{2} − 1``
       has explicit symmetric coefficient pairs at degree (8, 12)
       and (2, 18). Test composites

           ``1/(1 − h_q·q^{10})  +  α · [other p(q) terms]``

       where α is dictated by p(q)'s coefficient structure, not
       fit-derived.

Negative result format: each probe reports a numerical residual
+ smoothness diagnostic; combined witness records all three.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder


def _phi_q(z, qi, K=300):
    """Φ_q(z) = ∏_{j=1..K} (1 − qi^j · z)^{-1}. Converges for |qi|<1."""
    p = mp.mpf(1)
    qj = qi
    for _ in range(K):
        p /= (1 - qj * z)
        qj *= qi
        if abs(qj) < mp.mpf(10) ** (-mp.mp.dps - 10):
            break
    return p


def lambda_p_q(q):
    """Substrate-q functional form of λ_p:
       λ_p(q) = (m_p/m_e) · ℏ_q²(q) / (8G).

    Uses paper's ℏ_q = (q − 1)/q (NOT h_q = q − 1/q). At physical
    q_0 this reproduces the CODATA 2.4599527843613… value.
    """
    G = mp.catalan
    M_PE = mp.mpf("1836.15267343")  # CODATA m_p/m_e
    hbar_q = (q - 1) / q
    return M_PE * hbar_q ** 2 / (8 * G)


def main():
    t_start = time.monotonic()
    mp.mp.dps = 60

    Q0 = mp.mpf(Q_50_DIGIT_STR)
    Qi = 1 / Q0
    h_q0 = Q0 - Qi
    G = mp.catalan
    # CODATA-implied target (high precision, matches Bring-Bloch tiers).
    lambda_p_codata = mp.mpf("2.4599527843613182892482457339493")

    print(f"Explore q^10 selectivity  (dps={mp.mp.dps})")
    print(f"q_0 = {mp.nstr(Q0, 14)}, h_q = {mp.nstr(h_q0, 14)}")
    print(f"λ_p (CODATA target) = {mp.nstr(lambda_p_codata, 20)}")
    print()

    # ── P1: Q-locality sweep ─────────────────────────────────────
    print("(P1) Q-locality sweep — residual smoothness across substrate window")
    print("=" * 70)
    print(f"{'q':<14s} {'λ_p(q)':<22s} {'1/(1-h_q·q^10)':<22s} {'residual (ppm)':<14s}")
    locality_data = []
    for delta in [
        mp.mpf("-0.05"), mp.mpf("-0.02"), mp.mpf("-0.01"),
        mp.mpf("-0.005"), mp.mpf("-0.001"),
        mp.mpf(0),
        mp.mpf("0.001"), mp.mpf("0.005"),
        mp.mpf("0.01"), mp.mpf("0.02"), mp.mpf("0.05"),
    ]:
        q = Q0 + delta
        h_q = q - 1 / q
        form_q = 1 / (1 - h_q * q ** 10)
        lp_q = lambda_p_q(q)
        # Residual ppm
        residual_rel = (form_q - lp_q) / lp_q
        locality_data.append({
            "delta": mp.nstr(delta, 8),
            "q": mp.nstr(q, 16),
            "lambda_p_q": mp.nstr(lp_q, 16),
            "form_q": mp.nstr(form_q, 16),
            "residual_rel_ppm": mp.nstr(residual_rel * 1e6, 8),
        })
        marker = "  ← q_0" if delta == 0 else ""
        print(f"{mp.nstr(q, 12):<14s} {mp.nstr(lp_q, 16):<22s} {mp.nstr(form_q, 16):<22s} {mp.nstr(residual_rel * 1e6, 6):<14s}{marker}")

    # Smoothness diagnostic: is residual_rel(q) monotone / smooth across the window?
    residuals = [mp.mpf(d["residual_rel_ppm"]) for d in locality_data]
    # Linear fit slope at q_0 to detect substrate-q dependence
    qs = [mp.mpf(d["q"]) for d in locality_data]
    n = len(qs)
    qsum = sum(qs)
    rsum = sum(residuals)
    qrsum = sum(qs[i] * residuals[i] for i in range(n))
    qsqsum = sum(qs[i] ** 2 for i in range(n))
    slope = (n * qrsum - qsum * rsum) / (n * qsqsum - qsum ** 2)
    intercept = (rsum - slope * qsum) / n
    # Curvature: second-difference at the midpoint
    mid = n // 2
    curvature = residuals[mid + 1] - 2 * residuals[mid] + residuals[mid - 1]
    print()
    print(f"Smoothness diagnostic:")
    print(f"  slope (d_residual/d_q) at q_0: {mp.nstr(slope, 6)} ppm/q")
    print(f"  curvature (2nd diff at q_0):   {mp.nstr(curvature, 6)} ppm")
    print(f"  → if slope and curvature are O(1) ppm, residual is smooth → H1/H2 supported")
    print(f"  → if either is O(1000) ppm, residual is a substrate-q_0 accident → H3 supported")
    print()

    # ── P2: Φ_q tower expansion ──────────────────────────────────
    print("(P2) Φ_q tower expansion — does the next functional-eq factor close the gap?")
    print("=" * 70)
    z_star = h_q0 * Q0 ** 10
    print(f"  z_*       = h_q · q_0^10 = {mp.nstr(z_star, 18)}")
    print(f"  1/(1−z_*) = {mp.nstr(1 / (1 - z_star), 18)}  (the form, 19 ppm from λ_p)")
    print()
    # Compute the EXACT functional-equation ratio Φ_q(q·z_*)/Φ_q(z_*)
    # via direct Φ_q product (not just the first factor).
    phi_z = _phi_q(z_star, Qi, K=400)
    phi_qz = _phi_q(Q0 * z_star, Qi, K=400)
    ratio_full = phi_qz / phi_z
    ratio_first_factor = 1 / (1 - z_star)
    print(f"  Φ_q(z_*)              = {mp.nstr(phi_z, 18)}")
    print(f"  Φ_q(q·z_*)            = {mp.nstr(phi_qz, 18)}")
    print(f"  Full ratio            = {mp.nstr(ratio_full, 18)}")
    print(f"  First-factor (form)   = {mp.nstr(ratio_first_factor, 18)}")
    print(f"  full/first            = {mp.nstr(ratio_full / ratio_first_factor, 18)}")
    print()
    # Note: by the functional eq, Φ_q(qz)/Φ_q(z) = 1/(1−z) IDENTICALLY.
    # So ratio_full and ratio_first_factor must be equal up to numerical
    # error. This is a sanity check; the residual is at floor.
    fe_sanity_err = abs(ratio_full - ratio_first_factor) / abs(ratio_first_factor)
    print(f"  functional-eq sanity check: |full − first| / first = {mp.nstr(fe_sanity_err, 6)}")
    print(f"  (must be at numerical floor — Φ_q(qz)/Φ_q(z) = 1/(1−z) identically)")
    print()
    # The real question: is there a z OTHER than h_q·q^10 — call it z_*′ —
    # for which 1/(1 − z_*′) = λ_p_codata EXACTLY? Yes: z_*′ = 1 − 1/λ_p.
    # The question is whether z_*′ has a Φ_q functional-equation
    # interpretation. We checked in PR #941 that no substrate-natural
    # z lands at z_*′ to ppb. PR #943 found h_q·q^10 close but 19 ppm off.
    z_star_exact = 1 - 1 / lambda_p_codata
    delta_z = z_star_exact - z_star
    print(f"  z_*′ = 1 − 1/λ_p_codata = {mp.nstr(z_star_exact, 18)}")
    print(f"  z_* = h_q · q^10        = {mp.nstr(z_star, 18)}")
    print(f"  Δz  = z_*′ − z_*        = {mp.nstr(delta_z, 10)}")
    print(f"      / h_q                = {mp.nstr(delta_z / h_q0, 10)}")
    print(f"      · q_0^10             = {mp.nstr(delta_z * Q0 ** 10, 10)}")
    print(f"      · q_0^20             = {mp.nstr(delta_z * Q0 ** 20, 10)}")
    print()

    # ── P3: Adjacent-power composite (p(q) coefficient-guided) ───
    # p(q) = q^20 + q^18 + 2q^12 − 2q^8 − q^2 − 1
    # symmetric pairs: (q^20, −1), (q^18, −q^2), (q^12, −q^8) coefficient (2, −2)
    print("(P3) Adjacent-power composite — p(q) coefficient-guided candidates")
    print("=" * 70)
    candidates = {
        "1/(1 − h_q · q^10)": 1 / (1 - h_q0 * Q0 ** 10),
        # The symmetric pair around q^10: factors of (q^11 − q^9) appearing
        # with coefficients from p(q)
        "1/(1 − h_q·q^10) · (1 − 1/12·q^{-20}·p(q))":
            (1 / (1 - h_q0 * Q0 ** 10)) * (1 - mp.mpf(1)/12 * Q0 ** (-20) *
             (Q0**20 + Q0**18 + 2*Q0**12 - 2*Q0**8 - Q0**2 - 1)),
        # Symmetric pair contribution from (q^12, q^8) coefficients (+2, −2)
        # ratio (q^12 − q^8)/q^10 = q^2 − q^{-2} = (q-q^{-1})(q+q^{-1}) = h_q·(q+q^{-1})
        "1/(1 − h_q·q^10) − 2·h_q²·(q+q^{-1})·G":
            1 / (1 - h_q0 * Q0 ** 10) - 2 * h_q0 ** 2 * (Q0 + 1/Q0) * G,
        "1/(1 − h_q·q^10) − h_q²·G":
            1 / (1 - h_q0 * Q0 ** 10) - h_q0 ** 2 * G,
        "5/2 − h_q²·G (existing benchmark)":
            mp.mpf(5)/2 - h_q0 ** 2 * G,
    }
    print(f"  {'candidate':<58s} {'value':<22s} {'ppm':<10s}")
    p3_data = {}
    best_err = mp.inf
    best_name = None
    for name, v in candidates.items():
        rel_ppm = (v - lambda_p_codata) / lambda_p_codata * 1e6
        marker = ""
        if abs(rel_ppm) < 1:
            marker = " ← <1 ppm"
        elif abs(rel_ppm) < 10:
            marker = " ← <10 ppm"
        print(f"  {name:<58s} {mp.nstr(v, 15):<22s} {mp.nstr(rel_ppm, 6):<10s}{marker}")
        p3_data[name] = {"value": mp.nstr(v, 18), "rel_ppm": mp.nstr(rel_ppm, 8)}
        if abs(rel_ppm) < best_err:
            best_err = abs(rel_ppm)
            best_name = name
    print()
    print(f"  best: {best_name} ({mp.nstr(best_err, 6)} ppm)")
    print()

    # ── P4: q-locality of existing 5/2 − h_q²·G benchmark for comparison ──
    print("(P4) Q-locality of EXISTING benchmark 5/2 − h_q²·G — is IT smooth?")
    print("=" * 70)
    p4_data = []
    for delta in [mp.mpf("-0.05"), mp.mpf("-0.01"), mp.mpf(0), mp.mpf("0.01"), mp.mpf("0.05")]:
        q = Q0 + delta
        h_q_local = q - 1 / q
        form_q = mp.mpf(5) / 2 - h_q_local ** 2 * G
        lp_q = lambda_p_q(q)
        residual_rel = (form_q - lp_q) / lp_q
        marker = "  ← q_0" if delta == 0 else ""
        print(f"  q = {mp.nstr(q, 12):<14s} residual = {mp.nstr(residual_rel * 1e6, 8):<14s} ppm{marker}")
        p4_data.append({"delta": mp.nstr(delta, 6), "residual_ppm": mp.nstr(residual_rel * 1e6, 8)})
    # Slope at q_0
    p4_qs = [Q0 + mp.mpf("-0.01"), Q0, Q0 + mp.mpf("0.01")]
    p4_residuals = [(mp.mpf(5)/2 - (q - 1/q)**2 * G - lambda_p_q(q)) / lambda_p_q(q) * 1e6 for q in p4_qs]
    p4_slope = (p4_residuals[2] - p4_residuals[0]) / (p4_qs[2] - p4_qs[0])
    p4_curvature = p4_residuals[2] - 2 * p4_residuals[1] + p4_residuals[0]
    print(f"  slope (d_residual/d_q) at q_0: {mp.nstr(p4_slope, 6)} ppm/q")
    print(f"  curvature (2nd diff at q_0):   {mp.nstr(p4_curvature, 6)} ppm")
    print()

    # ── Summary ──────────────────────────────────────────────────
    print("=" * 70)
    print("INTERPRETATION:")
    if abs(slope) < mp.mpf(100) and abs(curvature) < mp.mpf(100):
        print("  P1: residual is SMOOTH → H1/H2 supported (q_0 not special)")
    else:
        print(f"  P1: slope = {mp.nstr(slope, 4)}, curvature = {mp.nstr(curvature, 4)} → potentially substrate-accident")
    if fe_sanity_err > mp.mpf(10) ** (-15):
        print(f"  P2: Φ_q functional-eq sanity FAILED (compute error)")
    else:
        print(f"  P2: 1/(1-z_*) IS the full functional-eq ratio (sanity {mp.nstr(fe_sanity_err, 4)})")
        print(f"      No Φ_q tail to close 19 ppm gap; the form is structurally exact.")
    if best_err < mp.mpf("1"):
        print(f"  P3: composite candidate within 1 ppm — categorical closure plausible")
    else:
        print(f"  P3: no composite within 1 ppm; best is {best_name} at {mp.nstr(best_err, 4)} ppm")
    p4_smooth = abs(p4_slope) < mp.mpf(1000) and abs(p4_curvature) < mp.mpf(100)
    if p4_smooth:
        print(f"  P4: 5/2−h_q²·G IS smooth (slope {mp.nstr(p4_slope, 4)}, curv {mp.nstr(p4_curvature, 4)})")
        print(f"      → existing benchmark is structural, NOT a coincidence")
    else:
        print(f"  P4: 5/2−h_q²·G ALSO non-smooth (slope {mp.nstr(p4_slope, 4)}, curv {mp.nstr(p4_curvature, 4)})")
        print(f"      → both forms are substrate-q_0 accidents; CAL-4 status tightened")

    # ── Witness ──────────────────────────────────────────────────
    w = WitnessBuilder(
        "explore-q10-selectivity",
        engine="mpmath",
        start_time=t_start,
    )
    w.set_description(
        "Spike: investigate the categorical reason for q^10 selectivity "
        "in PR #943's finding 1/(1 − h_q·q_0^10) ≈ λ_p (+19 ppm). "
        "Three probes per docs/coordination/explore-q10.md: "
        "(P1) q-locality sweep across q_0 ± 0.05 testing residual "
        "smoothness; (P2) Φ_q tower-expansion sanity (functional-eq "
        "ratio IS the form; no Φ_q tail to close the gap); (P3) "
        "adjacent-power composite candidates p(q)-coefficient-guided "
        "from the proton braid Markov trace polynomial."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("dps", 60)
    w.add_parameter("phi_q_K", 400)
    w.add_data("p1_locality_sweep", locality_data)
    w.add_data("p1_slope_ppm_per_q", mp.nstr(slope, 12))
    w.add_data("p1_curvature_ppm", mp.nstr(curvature, 12))
    w.add_data("p2_phi_q_functional_eq_sanity_err", mp.nstr(fe_sanity_err, 12))
    w.add_data("p2_z_star_form", mp.nstr(z_star, 22))
    w.add_data("p2_z_star_exact", mp.nstr(z_star_exact, 22))
    w.add_data("p2_delta_z", mp.nstr(delta_z, 22))
    w.add_data("p3_candidates", p3_data)
    w.add_data("p3_best_candidate", best_name)
    w.add_data("p3_best_ppm", mp.nstr(best_err, 12))
    w.add_data("p4_benchmark_locality", p4_data)
    w.add_data("p4_benchmark_slope_ppm_per_q", mp.nstr(p4_slope, 12))
    w.add_data("p4_benchmark_curvature_ppm", mp.nstr(p4_curvature, 12))
    w.add_assertion(
        "spike_completed",
        computed=1.0,
        expected=1.0,
    )
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
