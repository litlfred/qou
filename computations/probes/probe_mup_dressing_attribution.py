#!/usr/bin/env python3
"""
probe_mup_dressing_attribution.py — attribution test for the μ–p
dressing: if the missing higher-order correction multiplies the MUON
identity (the sign-favored reading from
probe_mup_dressing_vs_even_kernel), the two-observable system DECOUPLES
and yields a third, independent q₀ pin.

Structure (exact, no fit). Hypothesis H_μ: the exact mass functor gives
m_μ = A(q)·(1+δ) with A = m_e·Vol(4₁)/ℏ_q², δ the (unknown, small)
dressing; the proton identity m_p = 2(m_μ·F_Bor − 6m_e) is exact in
terms of the PHYSICAL m_μ. Then:

  * eq-p:  m_p^obs = 2(m_μ^obs·F_Bor(q) − 6m_e)   — contains NO δ:
    q₀ is pinned by the pure dimensionless Hecke factor
      F_Bor(q₀^F) = (m_p^obs + 12m_e)/(2·m_μ^obs)          (the F-pin)
  * eq-μ:  δ* = m_μ^obs/A(q₀^F) − 1                — the dressing,
    measured exactly under H_μ.

Deliverables:
  1. q₀^F (the F-pin) and its distance to the muon and proton pins —
     is the attribution self-consistent (q₀^F between/near them)?
  2. δ* exact, with the sensitivity d ln F_Bor/d ln q (how sharply the
     mass ratio pins q).
  3. Ratios of δ* to the pre-existing sharpener candidates (the k=5
     rung / k≥5 tail of the ORD-17 bar-even kernel) — no new candidate
     scan (formalize-first; the C1–C12 refuted-class precedent).
  4. Alternative attribution H_F (dressing on F_Bor): ε* = δ_p at the
     muon pin (degenerate — reproduces the known 242 ppb; recorded for
     completeness).
  5. Kashaev-subleading naturality check: the N that would make the
     (3/2)·log N·(2π/N)/Vol(4₁) volume-conjecture subleading term equal
     |δ*| — natural (≈ a corpus scale like 1/ℏ_q², 1/u) or not?

Output: probe-mup-dressing-attribution.witness.json
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from knot_volumes import VOL_4_1_MPF  # noqa: E402
from m_p_substrate_identity_50dps import F_Bor  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

M_P = mp.mpf("938.27208816")
M_MU = mp.mpf("105.6583755")
ORD17_WITNESS = HERE.parent / "qbeta" / "qbeta-bar-split-ord17.witness.json"


def A_muon(q, m_e):
    return m_e * VOL_4_1_MPF / (((q - 1) / q) ** 2)


def m_p_pure(q, m_e):
    return 2 * (A_muon(q, m_e) * F_Bor(q) - 6 * m_e)


def main() -> int:
    # PROVENANCE (verified): Q_50_DIGIT_STR is produced by the package
    # q_at() PROTON solve WITH the fitted Habiro tower
    # (1+46u^4)(1+4u^5)(1-29u^6) inside — the tower the 2026-05-28
    # floor audit rejected as a fit. Because the tower was fitted to
    # close the mu-p gap, the towered proton pin lands on the MUON
    # value to sub-ppb (m_mu fingerprint 1.36 ppb). Numerically this
    # constant IS the muon-pin value; its provenance is
    # proton-data + fitted tower.
    q0_mu = mp.mpf(Q_50_DIGIT_STR)                     # muon-valued pin
    m_e = mp.mpf(M_E_MEV)
    q0_p = mp.findroot(lambda q: m_p_pure(q, m_e) - M_P, q0_mu)  # proton pin

    # --- 1. the F-pin: F_Bor(q) = (m_p + 12 m_e) / (2 m_mu) ---
    target_F = (M_P + 12 * m_e) / (2 * M_MU)
    q0_F = mp.findroot(lambda q: F_Bor(q) - target_F, q0_mu)

    ppb = lambda a, b: (a / b - 1) * mp.mpf(10) ** 9
    d_mu_ppb = ppb(q0_F, q0_mu)
    d_p_ppb = ppb(q0_F, q0_p)
    between = (q0_F - q0_mu) * (q0_F - q0_p) < 0

    # --- 2. delta* and the F_Bor sensitivity ---
    delta_star = M_MU / A_muon(q0_F, m_e) - 1
    eps = mp.mpf(10) ** -20
    dlnF = (mp.log(F_Bor(q0_F * (1 + eps))) - mp.log(F_Bor(q0_F))) / eps
    dlnA = (mp.log(A_muon(q0_F * (1 + eps), m_e))
            - mp.log(A_muon(q0_F, m_e))) / eps

    # --- 3. ratios to the pre-existing sharpener candidates ---
    wb_upstream_path = ORD17_WITNESS
    with open(ORD17_WITNESS, "r", encoding="utf-8") as f:
        w = json.load(f)
    rungs = {int(k): mp.mpf(str(sp.N(sp.sympify(v), mp.mp.dps)))
             for k, v in w["data"]["E_rungs_exact"].items()}
    hbar2 = ((q0_F - 1) / q0_F) ** 2
    b = mp.sqrt(q0_F**4 + q0_F**2 + 1) / (q0_F**2 + 1)
    ut = q0_F * b * hbar2
    rung5 = rungs[5] * ut**5
    tail5 = mp.fsum(rungs[k] * ut**k for k in rungs if k >= 5)

    # --- 4. H_F attribution (degenerate; recorded) ---
    eps_F = M_P / m_p_pure(q0_mu, m_e) - 1   # = the known +242 ppb-ish

    # --- 4b. eps* vs the production solver's fitted Habiro tower ---
    # constants.py::q_at() multiplies the proton identity by
    # (1+46u^4)(1+4u^5)(1-29u^6), u = b*hbar_q^2 (legacy normalization).
    # If eps* equals (tower - 1), the "economical F_Bor-leg dressing"
    # measured here IS what the rejected fit supplies — pinning the
    # derivation target to the u^4 rung with coefficient ~46.
    hbar2_mu = ((q0_mu - 1) / q0_mu) ** 2
    b_mu = mp.sqrt(q0_mu**4 + q0_mu**2 + 1) / (q0_mu**2 + 1)
    u_leg = b_mu * hbar2_mu
    habiro_m1 = (1 + 46*u_leg**4) * (1 + 4*u_leg**5) * (1 - 29*u_leg**6) - 1
    ratio_tower = eps_F / habiro_m1

    # --- 5. Kashaev-subleading naturality ---
    # (3/2)·log N·(2π/N) / Vol(4_1) = |delta*|  → solve for N
    target = abs(delta_star) * VOL_4_1_MPF / (2 * mp.pi) / mp.mpf("1.5")
    N_k = mp.findroot(lambda N: mp.log(N) / N - target, mp.mpf(10) ** 8)
    scales = {"1/hbar_q^2": 1 / hbar2, "1/u~": 1 / ut,
              "1/u~^2": 1 / ut**2, "1/hbar_q^4": 1 / hbar2**2}

    print(f"muon pin   q0 = {mp.nstr(q0_mu, 20)}")
    print(f"proton pin q0 = {mp.nstr(q0_p, 20)}")
    print(f"F-pin      q0 = {mp.nstr(q0_F, 20)}")
    print(f"  F-pin vs muon: {mp.nstr(d_mu_ppb, 6)} ppb   vs proton: "
          f"{mp.nstr(d_p_ppb, 6)} ppb   between pins: {between}")
    print(f"  sensitivity d ln F_Bor/d ln q = {mp.nstr(dlnF, 6)} "
          f"(vs d ln A/d ln q = {mp.nstr(dlnA, 6)})")
    print(f"delta* (muon-leg dressing, measured) = {mp.nstr(delta_star, 8)}")
    print(f"  ratio to k=5 rung  e5*u~^5 = {mp.nstr(rung5 / delta_star, 6)}")
    print(f"  ratio to k>=5 tail        = {mp.nstr(tail5 / delta_star, 6)}")
    print(f"eps* (F_Bor-leg attribution, degenerate) = {mp.nstr(eps_F, 8)}")
    print(f"fitted Habiro tower - 1 at same q0       = {mp.nstr(habiro_m1, 8)}")
    print(f"  eps*/(tower-1) = {mp.nstr(ratio_tower, 8)}  (1.0 = the fit IS this dressing)")
    print(f"Kashaev-subleading N for |delta*|: N = {mp.nstr(N_k, 8)}")
    for nm, sc in scales.items():
        print(f"  vs {nm} = {mp.nstr(sc, 8)}  (ratio {mp.nstr(N_k / sc, 5)})")

    wb = WitnessBuilder("probe-mup-dressing-attribution",
                        engine="mpmath+sympy", output_dir=HERE)
    wb.add_upstream(ORD17_WITNESS)
    wb.set_description(
        "Attribution test for the mu-p dressing under hypothesis H_mu "
        "(dressing multiplies the muon identity): the system decouples, "
        "q0 is pinned by the pure Hecke factor F_Bor from the mass ratio "
        "(the F-pin), and delta* is measured exactly. Reports where the "
        "F-pin lands relative to the muon/proton pins, the F_Bor "
        "sensitivity, delta* vs the ORD-17 kernel sharpener candidates, "
        "and the Kashaev-subleading naturality check. No fit; no wiring.")
    wb.add_data("q0_muon_pin", mp.nstr(q0_mu, 50))
    wb.add_data("q0_proton_pin", mp.nstr(q0_p, 50))
    wb.add_data("q0_F_pin", mp.nstr(q0_F, 50))
    wb.add_data("F_pin_vs_muon_ppb", mp.nstr(d_mu_ppb, 12))
    wb.add_data("F_pin_vs_proton_ppb", mp.nstr(d_p_ppb, 12))
    wb.add_data("F_pin_between_pins", str(bool(between)))
    wb.add_data("dlnFBor_dlnq_at_Fpin", mp.nstr(dlnF, 12))
    wb.add_data("dlnA_dlnq_at_Fpin", mp.nstr(dlnA, 12))
    wb.add_data("delta_star_muon_leg", mp.nstr(delta_star, 15))
    wb.add_data("delta_star_ratio_rung5", mp.nstr(rung5 / delta_star, 10))
    wb.add_data("delta_star_ratio_tail5", mp.nstr(tail5 / delta_star, 10))
    wb.add_data("eps_star_FBor_leg", mp.nstr(eps_F, 15))
    wb.add_data("fitted_habiro_tower_minus_1", mp.nstr(habiro_m1, 15))
    wb.add_data("eps_star_over_tower_minus_1", mp.nstr(ratio_tower, 12))
    wb.add_data("kashaev_subleading_N", mp.nstr(N_k, 12))
    wb.add_data("kashaev_N_vs_corpus_scales",
                {nm: mp.nstr(N_k / sc, 8) for nm, sc in scales.items()})
    wb.add_assertion(
        "fpin_consistency_with_amplification",
        float(abs(dlnA / dlnF)) > 1.0, True,
        source="the muon identity must be MORE q-sensitive than F_Bor "
               "for the attribution geometry to make sense (record)")
    path = wb.save()
    print(f"witness: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
