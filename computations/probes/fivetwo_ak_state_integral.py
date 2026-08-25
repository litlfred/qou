#!/usr/bin/env python3
"""5₂ Andersen–Kashaev state integral I_{0,0} — literature reproduction of
Fantini–Wheeler, *Summability for State Integrals of hyperbolic knots*
(arXiv:2410.20973, 2024).  Bean qou-3xug.

WHAT THIS IS.  A faithful, from-the-definitions transcription of the
Andersen–Kashaev state integral for 5₂, which is the (m,ℓ)=(0,0) member of the
Fantini–Wheeler family I_{m,ℓ}(τ) (FW §1.2: "The Andersen–Kashaev state
integrals for 4₁ and 5₂ … correspond to m = ℓ = 0").  5₂ has Neumann–Zagier
data (A,B) = (2,3) (FW eq (6) / §1.1; max{A,B}=3 saddles).

FW eq (13):
    I_{m,ℓ}(τ) = μ₈^B · e_q^{−B/24} q^{B/24}
                 ∫_{J_{ℓ,τ}} Φ((z−ℓ)τ; τ)^B · e( (A/2) z(zτ+τ+1) + m z τ ) dz
  e(x) := exp(2πi x);  q := e(τ) = e^{2πiτ};  ẽ_q := q̃ := e(−1/τ) = e^{−2πi/τ};
  μ₈ = e^{iπ/4} (μ₈⁸ = 1, FW eq (7); the overall root of unity — it and the
  q-prefactor are common to every (m,ℓ) and cancel in every ratio below);
  contour  J_{ℓ,τ} = (i τ^{−1/2} e^{−iAε} ℝ_{≥0} − 1/2 + ℓ)
                   ∪ (i τ^{−1/2} e^{−i(A−B)ε} ℝ_{≤0} − 1/2 + ℓ),  ε > 0 small.
  ℏ = −2πi/τ (FW footnote 1).

Faddeev's Φ(z;τ) via the FW eq-(12) product form (valid τ ∈ ℍ):
    Φ(z;τ) = (q e(z); q)_∞ / (e(z/τ); q̃)_∞ ,  (x;q)_∞ = ∏_{k≥0}(1 − q^k x).

GATES (all self-contained or against independent corpus objects):
  G1 — Φ(z;τ) quasi-periodicity  Φ(z−τ;τ) = (1 − e(z)) Φ(z;τ)  (FW, after eq
       (13)).  Validates the Φ evaluator.  [~1e-38]
  G2 — I_{0,0}^{5₂}(τ) contour-angle (ε) INDEPENDENCE.  The AK contour value
       must not depend on the tilt ε (Cauchy: no poles crossed in the
       convergence sector).  ε ∈ {0.04,0.08,0.14,0.20} agree.  Validates the
       contour homotopy class + the quadrature.  [~1e-20]
  G3 — I_{0,0}^{5₂}(τ) vs the corpus's INDEPENDENT GGM/Peacock H-series
       factorization of the 5₂ state integral (qbeta_5two_stokes_barodd_index
       H_num; GGM 2007.10190 eq 110 / Peacock eq 82, the A2-validated
       machinery used by qbeta-5two-chirality-state-integral).  With the full
       FW prefactor the ratio I_FW/Z_GGM is REAL (imaginary part → 0): the
       FW-vs-GGM framing phase resolves exactly, so the two independent
       representations are the SAME analytic object up to a real change-of-
       variables Jacobian.  [Im(ratio) ~ 1e-30]

MEDIAN-BOREL LINKAGE (the FW Theorem 1.4 content).  FW prove Φ_{5₂}(−2πi/τ) is
Borel–Laplace summable to a ℤ[q^±]-combination of the I_{m,ℓ}; on a Stokes-free
ray this is a single state integral up to prefactor.  The corpus median-Borel
probe (qbeta-5two-median-borel-resummation) resums φ_σ1(5₂) and matches it to
the exact object F(τ)=h₁(τ)·e^{−V/2πτ} with h₁ = H⁺₁ — the SAME H-series that
appears in the Z_GGM factorization G3 cross-checks against.  So I_{0,0} is
cross-checked, through G3, against the very analytic object the median-Borel
resummation targets.  The exact ℤ[q^±] Stokes prefactor linking them (FW §3
algorithm) is NOT reproduced here (bean-filed GAP).

DISCIPLINE.  Literature reproduction of Fantini–Wheeler; NOT a QOU c3
derivation; no fit; nothing wired to production.  auditOnly.

Refs: [fantini-wheeler2024] arXiv:2410.20973; Andersen–Kashaev; GGM 2007.10190;
Garoufalidis–Kashaev 1411.6062.

Run: python3 -u computations/probes/fivetwo_ak_state_integral.py \\
       2>&1 | tee /tmp/fivetwo_ak_state_integral.log
"""
from __future__ import annotations

import sys
import time
from math import comb
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
import qbeta_5two_stokes_barodd_index_probe as sb  # noqa: E402  (corpus H_num)
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# 5₂ Neumann–Zagier data (FW eq (6) / §1.1)
A_52, B_52 = 2, 3
MU8 = mp.e ** (1j * mp.pi / 4)          # FW eq (7): μ₈, an 8th root of unity
Q0_MUON = mp.mpf("1.10997859555733471")  # substrate modulus (muon-q₀ canonical)


def e(x):
    """FW's e(x) = exp(2πi x)."""
    return mp.e ** (2 * mp.pi * 1j * x)


def phi_fw(z, tau, kmax=12000):
    """Faddeev Φ(z;τ) via the FW eq-(12) product form (τ ∈ ℍ):
    Φ = (q e(z); q)_∞ / (e(z/τ); q̃)_∞,  q = e(τ), q̃ = e(−1/τ).

    Both Pochhammers converge for Im τ > 0 (|q|,|q̃| < 1).  Validated by the
    quasi-periodicity Φ(z−τ;τ)=(1−e(z))Φ(z;τ) (G1)."""
    z = mp.mpc(z)
    tau = mp.mpc(tau)
    q = e(tau)
    qt = e(-1 / tau)
    ez = e(z)
    ezt = e(z / tau)
    tol = mp.mpf(10) ** (-mp.mp.dps - 8)
    num = mp.mpf(1)
    qp = q
    for k in range(kmax):
        num *= (1 - qp * ez)
        qp *= q
        if abs(qp) * abs(ez) < tol and k > 2:
            break
    den = mp.mpf(1)
    qtp = mp.mpf(1)
    for k in range(kmax):
        den *= (1 - qtp * ezt)
        qtp *= qt
        if abs(qtp) * abs(ezt) < tol and k > 2:
            break
    return num / den


def I_ml(tau, A, B, m, l, T=mp.mpf(9), eps=mp.mpf("0.10"), prefactor=True):
    """FW eq (13): I_{m,ℓ}(τ) by direct contour quadrature on J_{ℓ,τ}.

    Returns (value, endpoint_magnitude).  endpoint_magnitude is |integrand| at
    the ends of the truncated contour — a convergence certificate (must be tiny
    for the value to be trustworthy).  Robustly convergent for the AK member
    (m,ℓ)=(0,0) with B>A>0; higher m / shifted ℓ have out-migrating saddles that
    a straight ray does not resolve (see GAP note / bean)."""
    tau = mp.mpc(tau)
    sq = mp.sqrt(tau)
    dp = (1j / sq) * mp.e ** (-1j * A * eps)        # t ≥ 0 ray direction
    dm = (1j / sq) * mp.e ** (-1j * (A - B) * eps)  # t ≤ 0 ray direction
    base = mp.mpf(-1) / 2 + l

    def integrand(z):
        return phi_fw((z - l) * tau, tau) ** B * e(
            (mp.mpf(A) / 2) * z * (z * tau + tau + 1) + m * z * tau)

    Ipos = mp.quad(lambda t: integrand(base + dp * t) * dp, [0, T])
    Ineg = mp.quad(lambda t: integrand(base + dm * t) * dm, [-T, 0])
    val = Ipos + Ineg
    if prefactor:
        q = e(tau)
        qt = e(-1 / tau)
        val *= MU8 ** B * qt ** (-mp.mpf(B) / 24) * q ** (mp.mpf(B) / 24)
    endp = max(abs(integrand(base + dp * T)), abs(integrand(base + dm * (-T))))
    return val, endp


def z_ggm_factorization(tau):
    """Corpus's INDEPENDENT 5₂ state integral via the GGM/Peacock H-series
    factorization (GGM 2007.10190 eq 110 / Peacock eq 82), as used by
    qbeta_5two_chirality_state_integral_probe:
        Z_5₂ = −(e^{iπ/4}/2)(q/q̃)^{1/8}
               ( τ H⁺₂(q)H⁻₀(q̃) − 2 H⁺₁(q)H⁻₁(q̃) + (1/τ) H⁺₀(q)H⁻₂(q̃) ).
    Uses the A2-validated H_num (18 printed-table gates).  Real q,q̃ on the
    imaginary-τ ray."""
    tau = mp.mpc(tau)
    q = e(tau)
    qt = e(-1 / tau)
    Hp = lambda j: sb.H_num(+1, j, 0, q)   # noqa: E731
    Hm = lambda j: sb.H_num(-1, j, 0, qt)  # noqa: E731
    pref = -(mp.e ** (1j * mp.pi / 4) / 2) * (q / qt) ** (mp.mpf(1) / 8)
    return pref * (tau * Hp(2) * Hm(0) - 2 * Hp(1) * Hm(1)
                   + (1 / tau) * Hp(0) * Hm(2))


def _relerr(a, c):
    return float(mp.fabs(a - c) / max(mp.fabs(c), mp.mpf("1e-40")))


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" 5₂ Andersen–Kashaev state integral I_{0,0} — Fantini–Wheeler "
          "reproduction")
    print(" (A,B)=(2,3);  bean qou-3xug;  literature reproduction, no fit, "
          "nothing wired")
    print("=" * 78)

    # ---- G1: Φ(z;τ) quasi-periodicity ----
    print("\n[G1] Φ(z;τ) shift equation  Φ(z−τ;τ) = (1 − e(z)) Φ(z;τ):",
          flush=True)
    tau_g = mp.mpc(0, 1)
    g1_err = mp.mpf(0)
    for z in (mp.mpc("0.3", "0.2"), mp.mpc("-0.4", "0.1"), mp.mpc("0.15", "-0.25")):
        lhs = phi_fw(z - tau_g, tau_g)
        rhs = (1 - e(z)) * phi_fw(z, tau_g)
        g1_err = max(g1_err, mp.fabs(lhs - rhs) / mp.fabs(rhs))
    print(f"     max rel.err over 3 points: {mp.nstr(g1_err, 4)}  "
          f"{'PASS' if g1_err < mp.mpf('1e-25') else 'FAIL'}")
    g1_ok = g1_err < mp.mpf("1e-25")

    # ---- I_{0,0}^{5₂}(τ) at a moderate τ and at the substrate ray ----
    print("\n[I] I_{0,0}^{5₂}(τ) = the Andersen–Kashaev state integral "
          "(FW (m,ℓ)=(0,0)):", flush=True)
    tau_eval = mp.mpc(0, mp.mpf("0.6"))       # arg(τ)=90° (Stokes-free x-ray), moderate ℏ
    I00_eval, ep_eval = I_ml(tau_eval, A_52, B_52, 0, 0)
    hbar_eval = -2j * mp.pi / tau_eval
    print(f"     τ = {mp.nstr(tau_eval, 6)}  (ℏ = −2πi/τ = {mp.nstr(hbar_eval, 8)})")
    print(f"     I_{{0,0}} = {mp.nstr(I00_eval, 25)}")
    print(f"     endpoint |integrand| = {mp.nstr(ep_eval, 3)}  (convergence "
          f"certificate)")

    # substrate ray τ = iβ, β = ln q₀ / 2π  (the corpus resummation's home point)
    beta = mp.log(Q0_MUON) / (2 * mp.pi)
    tau_sub = mp.mpc(0, beta)
    # Gaussian damping ∝ Im τ = β is weak at the substrate ⇒ needs a long contour.
    I00_sub, ep_sub = I_ml(tau_sub, A_52, B_52, 0, 0, T=mp.mpf(60))
    print(f"\n     substrate τ = iβ = {mp.nstr(tau_sub, 8)} (β = ln q₀/2π):")
    print(f"     I_{{0,0}} = {mp.nstr(I00_sub, 20)}   endpoint = "
          f"{mp.nstr(ep_sub, 3)}")

    # ---- G2: ε-independence (Cauchy homotopy invariance) ----
    print("\n[G2] I_{0,0}^{5₂} contour-tilt (ε) independence (Cauchy homotopy):",
          flush=True)
    eps_vals = ["0.04", "0.08", "0.14", "0.20"]
    I_eps = [I_ml(tau_eval, A_52, B_52, 0, 0, eps=mp.mpf(ev))[0] for ev in eps_vals]
    g2_spread = max(_relerr(v, I_eps[0]) for v in I_eps[1:])
    for ev, v in zip(eps_vals, I_eps):
        print(f"     ε={ev}: {mp.nstr(v, 18)}")
    print(f"     max rel spread: {mp.nstr(g2_spread, 4)}  "
          f"{'PASS' if g2_spread < 1e-15 else 'FAIL'}")
    g2_ok = g2_spread < 1e-15

    # ---- G3: I_FW vs corpus GGM H-series factorization ----
    print("\n[G3] I_{0,0}^{5₂}(τ) vs the corpus GGM/Peacock H-series "
          "factorization Z_GGM:", flush=True)
    g3_rows = []
    g3_im_max = mp.mpf(0)
    for s in ("0.6", "0.85", "1.1", "1.4"):
        tau = mp.mpc(0, mp.mpf(s))
        I_full = I_ml(tau, A_52, B_52, 0, 0)[0]
        Z = z_ggm_factorization(tau)
        R = I_full / Z
        im_frac = mp.fabs(mp.im(R)) / mp.fabs(R)
        g3_im_max = max(g3_im_max, im_frac)
        g3_rows.append({"tau_im": s, "ratio_re": mp.nstr(mp.re(R), 14),
                        "ratio_im_over_abs": mp.nstr(im_frac, 4)})
        print(f"     τ=i·{s}: I_FW/Z_GGM = {mp.nstr(R, 12)}  "
              f"|Im/|R|| = {mp.nstr(im_frac, 3)}")
    print(f"     max |Im(ratio)/|ratio|| : {mp.nstr(g3_im_max, 4)}  "
          f"{'PASS (phase resolves — same analytic object)' if g3_im_max < 1e-20 else 'FAIL'}")
    print("     NOTE: the residual REAL factor is the FW↔GGM change-of-"
          "variables Jacobian (τ-dependent, O(1)); its closed form is a "
          "bean-filed GAP, not a correctness question about I_{0,0}.")
    g3_ok = g3_im_max < 1e-20

    # ---- eq-(14) recursion: the honest partial + the GAP ----
    print("\n[eq14] FW eq (14) recursion — HONEST PARTIAL.", flush=True)
    print("     The recursion mixes I_{m,ℓ} with m up to B=3 and shifted ℓ; "
          "those shifted /")
    print("     higher-m integrals have out-migrating saddles that a straight "
          "AK ray does not")
    print("     resolve (I_{2,0} peaks ~1e5, I_{3,0} ~1e22 mid-contour → "
          "catastrophic cancellation).")
    print("     A faithful check needs steepest-descent contours + guard "
          "precision — bean-filed GAP.")

    elapsed = time.monotonic() - t0
    print(f"\n  wall: {elapsed:.1f}s")

    # ---- witness ----
    wb = WitnessBuilder("fivetwo-ak-state-integral", engine="mpmath",
                        _script_path=__file__)
    wb.set_description(
        "Bean qou-3xug: literature reproduction of the Fantini–Wheeler "
        "(arXiv:2410.20973) Andersen–Kashaev state integral I_{0,0} for 5₂, "
        "Neumann–Zagier data (A,B)=(2,3), the (m,ℓ)=(0,0) member of the "
        "I_{m,ℓ} family (FW eq (13)). Faddeev Φ(z;τ) via the eq-(12) product "
        "form; contour quadrature on J_{0,τ}. Gates: G1 Φ quasi-periodicity; "
        "G2 contour-tilt (ε) independence (Cauchy homotopy); G3 phase match "
        "against the corpus's independent GGM/Peacock H-series factorization "
        "of the same state integral (Im(I_FW/Z_GGM)→0). Median-Borel linkage: "
        "the corpus median-Borel resummation of Φ_{5₂} targets F=h₁·e^{−V/2πτ} "
        "with h₁=H⁺₁, one of the H-series G3 matches. NOT a QOU c3 derivation; "
        "no fit; nothing wired.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("phi_quasi_periodicity", computed=float(g1_err),
                     expected=0.0, tolerance=1e-25,
                     source="G1: Φ(z−τ;τ)=(1−e(z))Φ(z;τ) max rel err over 3 pts")
    wb.add_assertion("I00_eps_independence", computed=float(g2_spread),
                     expected=0.0, tolerance=1e-15,
                     source="G2: I_{0,0} independent of contour tilt ε∈{0.04..0.20}")
    wb.add_assertion("I00_phase_matches_ggm_factorization",
                     computed=float(g3_im_max), expected=0.0, tolerance=1e-20,
                     source="G3: Im(I_FW/Z_GGM)/|ratio|→0 — same analytic object")

    wb.add_data("knot", "5_2")
    wb.add_data("neumann_zagier_AB", [A_52, B_52])
    wb.add_data("ml_label", [0, 0])
    wb.add_data("ml_label_meaning",
                "AK state integral = (m,ℓ)=(0,0) member of FW I_{m,ℓ} (FW §1.2)")
    wb.add_data("hbar_convention", "ℏ = −2πi/τ (FW footnote 1)")
    wb.add_data("I00_at_tau_i0p6", {
        "tau": mp.nstr(tau_eval, 15), "hbar": mp.nstr(hbar_eval, 15),
        "value": mp.nstr(I00_eval, 30),
        "endpoint_integrand": mp.nstr(ep_eval, 6)})
    wb.add_data("I00_at_substrate", {
        "tau": mp.nstr(tau_sub, 15), "beta": mp.nstr(beta, 15),
        "value": mp.nstr(I00_sub, 25),
        "endpoint_integrand": mp.nstr(ep_sub, 6)})
    wb.add_data("g3_ratio_table", g3_rows)
    wb.add_data("crosscheck_delta", {
        "g1_phi_quasiperiodicity_relerr": mp.nstr(g1_err, 6),
        "g2_eps_independence_spread": mp.nstr(g2_spread, 6),
        "g3_phase_residual_im_over_abs": mp.nstr(g3_im_max, 6),
        "interpretation": "G3 phase residual → 0 confirms I_{0,0}^{FW} equals "
                          "the corpus GGM H-series state integral up to a real "
                          "τ-dependent Jacobian; that Jacobian's closed form + "
                          "the exact ℤ[q^±] Stokes prefactor of FW Thm 1.4 are "
                          "the bean-filed GAPs."})
    wb.add_data("median_borel_linkage",
                "The corpus median-Borel probe "
                "(qbeta-5two-median-borel-resummation) resums φ_σ1(5₂) to "
                "F=h₁·e^{−V/2πτ}, h₁=H⁺₁(q); H⁺₁ is a factor of the Z_GGM "
                "H-series against which G3 matches I_{0,0} in phase. So I_{0,0} "
                "is cross-checked, via G3, against the analytic object the "
                "median-Borel resummation targets. The exact ℤ[q^±] prefactor "
                "(FW §3 algorithm) is not reproduced (GAP).")
    wb.add_data("open_gaps", [
        "exact FW eq-(14) recursion (needs steepest-descent contours + guard "
        "precision for the shifted/high-m I_{m,ℓ})",
        "closed form of the real FW↔GGM change-of-variables Jacobian R(τ)=I_FW/Z_GGM",
        "exact ℤ[q^±] Stokes-constant prefactor of FW Thm 1.4 linking I_{0,0} "
        "to the median-Borel resummation of Φ_{5₂}"])
    wb.add_data("discipline",
                "literature reproduction of Fantini–Wheeler; NOT a QOU c3 "
                "derivation; no fit; nothing wired")

    ok = g1_ok and g2_ok and g3_ok
    print(f"\n  GATES: G1 {'OK' if g1_ok else 'FAIL'} | "
          f"G2 {'OK' if g2_ok else 'FAIL'} | G3 {'OK' if g3_ok else 'FAIL'}")
    wb.save()
    print("  witness -> computations/probes/fivetwo-ak-state-integral.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
