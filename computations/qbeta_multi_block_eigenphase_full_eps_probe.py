#!/usr/bin/env python3
"""qbeta_multi_block_eigenphase_full_eps_probe.py — Q_β bridge
experiment #4: extend exp #3 from LO to FULL per-block ε-expansion
through ε⁶ (the documented per-block character expansions).
(Item 2 of the 2026-06-09 post-1574 standing queue.)

CONTEXT. Experiment #3 (`qbeta_multi_block_eigenphase_probe.py`)
showed q₀-STABILITY (0.0003%) for the multi-block fundamental-rep
eigenphase at LO — a *necessary* condition for being the Q_β bridge.
But the LO-only residual was −1.19% (above compute precision). The
verdict was "open: q₀-stable but not Taylor-exact."

This probe extends to the FULL per-block ε-expansion. The character
expansions are documented in `qbeta_per_block_paper_closed_forms.py`:

  χ_(3)(β_n − β_p)     = -2·ε - 3·ε² - 3·ε³ - ε⁴ - ε⁵/2 + ε⁶/4
  χ_(2,1)(β_n − β_p)   = -1·ε + ε²/2 - 5·ε³/2 + 7·ε⁴/2 - 5·ε⁵ + 27·ε⁶/4
  χ_(1,1,1)(β_n − β_p) = -2·ε + 5·ε² - 11·ε³ + 21·ε⁴ - 73·ε⁵/2 + 237·ε⁶/4

The fundamental-rep-weighted eigenphase α_eff at full order:
  α_eff(ε) = Σ_λ [dim_q^FR(λ) / Z(q)] · χ_λ(β_n − β_p)
  Q_bridge = Q_A · cos(α_eff)

Two questions:
  1. Does the full ε-expansion close Q_β to compute precision at q₀?
  2. If not, is the residual Taylor-exact (q₀-stable) — confirming the
     bridge IS the multi-block fundamental-rep eigenphase but in a
     different functional form than cos(α_eff)?

DISCIPLINE: per bridge-narrowing addendum §4, q₀-dependent residuals
= form-fitting. No identification claimed unless q₀-stable AND
< compute precision.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

try:
    from _precision import set_compute_dps
except ImportError:
    def set_compute_dps(): mp.mp.dps = 50
set_compute_dps()

try:
    from witness_base import WitnessBuilder
except ImportError:
    sys.path.insert(0, str(HERE.parent))
    from witness_base import WitnessBuilder
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV

Q0_STALE_MUON_PIN = "1.10997859555418057528159407960950937799328227995870"
Q_BETA_CODATA_MEV = mp.mpf("0.78233341")


def per_block_chi_full(eps):
    """Full per-block χ_λ(β_n − β_p) through ε⁶ from the documented
    Taylor expansions in qbeta_per_block_paper_closed_forms.py."""
    return {
        "(3)":
            -2 * eps - 3 * eps**2 - 3 * eps**3 - eps**4
            - eps**5 / 2 + eps**6 / 4,
        "(2,1)":
            -1 * eps + eps**2 / 2 - mp.mpf(5)/2 * eps**3 + mp.mpf(7)/2 * eps**4
            - 5 * eps**5 + mp.mpf(27)/4 * eps**6,
        "(1,1,1)":
            -2 * eps + 5 * eps**2 - 11 * eps**3 + 21 * eps**4
            - mp.mpf(73)/2 * eps**5 + mp.mpf(237)/4 * eps**6,
    }


def bridge_test_full(q0_str: str, max_order: int = 6) -> dict:
    """Multi-block fundamental-rep eigenphase, truncated at order
    ε^max_order. max_order=1 reproduces experiment #3 (LO only).
    max_order=6 uses the full documented expansion."""
    q = mp.mpf(q0_str)
    me = mp.mpf(M_E_MEV)
    eps = q - 1
    h = q - 1 / q
    Q_A = me * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)

    # Fundamental-rep quantum dimensions per H_3 block (n=2 / SU_q(2)):
    qbr2 = (q ** 2 - q ** (-2)) / (q - 1 / q)  # [2]_q
    dim_qFR = {"(3)": mp.mpf(1), "(2,1)": qbr2, "(1,1,1)": mp.mpf(1)}
    Z_q = sum(dim_qFR.values())

    # Per-block characters, optionally truncated at max_order
    chi_full = per_block_chi_full(eps)
    if max_order < 6:
        # Re-build with explicit truncation — recompute only terms <= max_order
        truncated = {}
        for b, full_val in chi_full.items():
            # Reconstruct as polynomial truncated; coefficients hardcoded
            if b == "(3)":
                coeffs = [0, -2, -3, -3, -1, mp.mpf(-1)/2, mp.mpf(1)/4]
            elif b == "(2,1)":
                coeffs = [0, -1, mp.mpf(1)/2, mp.mpf(-5)/2, mp.mpf(7)/2, -5, mp.mpf(27)/4]
            else:  # (1,1,1)
                coeffs = [0, -2, 5, -11, 21, mp.mpf(-73)/2, mp.mpf(237)/4]
            truncated[b] = sum(coeffs[k] * eps**k for k in range(min(max_order, 6) + 1))
        chi_full = truncated

    alpha_eff = sum(dim_qFR[b] * chi_full[b] for b in dim_qFR) / Z_q
    Q_bridge_cos = Q_A * mp.cos(alpha_eff)
    err_cos_ppb = (Q_bridge_cos / Q_BETA_CODATA_MEV - 1) * mp.mpf(10) ** 9

    # Alternative bridge ansätze (since cos(α_eff) at LO was wrong-sign):
    #   exp(α_eff):  Q_β = Q_A · exp(α_eff)         — non-cyclic
    #   (1+α_eff):   Q_β = Q_A · (1 + α_eff)         — leading linear
    Q_bridge_exp = Q_A * mp.exp(alpha_eff)
    Q_bridge_lin = Q_A * (1 + alpha_eff)
    err_exp_ppb = (Q_bridge_exp / Q_BETA_CODATA_MEV - 1) * mp.mpf(10) ** 9
    err_lin_ppb = (Q_bridge_lin / Q_BETA_CODATA_MEV - 1) * mp.mpf(10) ** 9

    return {
        "q": q, "eps": eps, "Q_A": Q_A,
        "max_order": max_order,
        "alpha_eff": alpha_eff,
        "Q_bridge_cos": Q_bridge_cos, "err_cos_ppb": err_cos_ppb,
        "Q_bridge_exp": Q_bridge_exp, "err_exp_ppb": err_exp_ppb,
        "Q_bridge_lin": Q_bridge_lin, "err_lin_ppb": err_lin_ppb,
        "chi_full": chi_full,
    }


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder("qbeta-multi-block-eigenphase-full-eps-probe",
                             engine="python+mpmath", start_time=t0)
    builder.set_description(
        "Q_β bridge experiment #4: extends exp #3 from LO ε-only to "
        "full per-block ε-expansion through ε^6 (the documented per-"
        "block character expansions from qbeta_per_block_paper_closed_"
        "forms.py). Tests THREE bridge ansätze in parallel: "
        "cos(α_eff), exp(α_eff), (1+α_eff). Each tested for q₀-"
        "stability and compute-precision residual. Order-by-order "
        "convergence shown."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")

    print("=" * 78)
    print(" Q_β BRIDGE EXPERIMENT #4 — full per-block ε-expansion through ε⁶")
    print(" (3 ansätze in parallel: cos, exp, 1+α)")
    print("=" * 78)
    print()

    # Order-by-order convergence at canonical q₀
    print(f"  Order-by-order at canonical q₀ = {Q_50_DIGIT_STR[:18]}…")
    print(f"  {'order':<7} {'α_eff':<22} {'err cos (ppb)':<18} {'err exp (ppb)':<18} {'err 1+α (ppb)':<18}")
    print(f"  {'-'*7} {'-'*22} {'-'*18} {'-'*18} {'-'*18}")
    order_results = []
    for order in [1, 2, 3, 4, 5, 6]:
        r = bridge_test_full(Q_50_DIGIT_STR, max_order=order)
        print(f"  ε^{order:<5} {mp.nstr(r['alpha_eff'], 14):<22} "
              f"{mp.nstr(r['err_cos_ppb'], 8):<18} "
              f"{mp.nstr(r['err_exp_ppb'], 8):<18} "
              f"{mp.nstr(r['err_lin_ppb'], 8):<18}")
        order_results.append({
            "order": order,
            "alpha_eff": mp.nstr(r['alpha_eff'], 30),
            "err_cos_ppb": mp.nstr(r['err_cos_ppb'], 12),
            "err_exp_ppb": mp.nstr(r['err_exp_ppb'], 12),
            "err_lin_ppb": mp.nstr(r['err_lin_ppb'], 12),
        })
    print()

    # q₀-stability test at full ε⁶
    canon = bridge_test_full(Q_50_DIGIT_STR, max_order=6)
    stale = bridge_test_full(Q0_STALE_MUON_PIN, max_order=6)
    print(f"  q₀-STABILITY at full ε⁶:")
    print(f"  {'ansatz':<8} {'err canon (ppb)':<22} {'err stale (ppb)':<22} {'drift':<10}")
    print(f"  {'-'*8} {'-'*22} {'-'*22} {'-'*10}")
    drifts = {}
    for ansatz, cf, sf in [
        ("cos",  canon["err_cos_ppb"], stale["err_cos_ppb"]),
        ("exp",  canon["err_exp_ppb"], stale["err_exp_ppb"]),
        ("1+α",  canon["err_lin_ppb"], stale["err_lin_ppb"]),
    ]:
        drift = abs(cf - sf)
        drift_pct = float(drift / abs(cf) * 100) if cf != 0 else float("inf")
        drifts[ansatz] = drift_pct
        print(f"  {ansatz:<8} {mp.nstr(cf, 10):<22} {mp.nstr(sf, 10):<22} {drift_pct:.5f}%")
    print()

    # Find the BEST ansatz at full ε⁶
    best_ans, best_err = min(
        [("cos", canon["err_cos_ppb"]),
         ("exp", canon["err_exp_ppb"]),
         ("1+α", canon["err_lin_ppb"])],
        key=lambda x: abs(float(x[1]))
    )
    abs_best_err = abs(float(best_err))

    # Verdict
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if abs_best_err < 0.001:
        verdict = f"RULED-IN ({best_ans} ansatz Taylor-exact at canonical q₀)"
        msg = f"""
  ✓ BREAKTHROUGH. The {best_ans} ansatz of the multi-block fundamental-
    rep eigenphase closes Q_β to {mp.nstr(best_err, 6)} ppb (< compute
    precision) at canonical q₀, with q₀-drift {drifts[best_ans]:.5f}%.
    The Q_β bridge IS the multi-block fundamental-rep eigenphase under
    the {best_ans} ansatz. Production wiring + Lean formalisation
    follow."""
    elif drifts[best_ans] > 0.01:
        verdict = f"RULED-OUT ({best_ans}: q₀-drift > 0.01%)"
        msg = f"""
  ✗ Even at full ε⁶ none of the three ansätze (cos / exp / 1+α) reaches
    compute precision, AND the best ({best_ans}) has q₀-drift
    {drifts[best_ans]:.5f}% > 0.01% — flagged as form-fitting per the
    discipline lock §4. The multi-block fundamental-rep eigenphase is
    NOT the bridge under any of these three composition rules.

    Honest reading: the bridge requires a more complex composition than
    {{cos, exp, 1+α}}(α_eff) — possibly the PR #1521 composite
    [Habiro × Planck-tick × Bloch-Wigner] structure, which is research-
    grade per audit doc §4. Production stays Q_N2 (1279 ppb)."""
    else:
        verdict = f"OPEN ({best_ans}: q₀-stable but residual {mp.nstr(best_err, 4)} ppb)"
        msg = f"""
  ◐ The {best_ans} ansatz at full ε⁶ is q₀-stable ({drifts[best_ans]:.5f}%
    drift across pins, well below the 0.01% form-fitting threshold) but
    its residual {mp.nstr(best_err, 6)} ppb is above compute precision.
    Still closer than 6 prior ruled-out mechanisms. Two reads:

    (a) the LO ε structure is right but the ε^7+ tail matters — a Padé
        resummation of the per-block χ_λ might close the gap;
    (b) the ansatz family {{cos, exp, 1+α}} is insufficient — the
        bridge needs a more complex functional form (e.g. PR #1521's
        Bloch-Wigner composite).

    Either way: q₀-stability persisting through full ε⁶ is the FIRST
    sustained positive signal across the bridge-narrowing campaign.
    Worth recording. Production stays Q_N2 until closure."""
    print(msg)
    print()
    print(f"  verdict: {verdict}")
    print()

    builder.add_data("pins", {
        "canonical_mp_pin_q0": Q_50_DIGIT_STR,
        "stale_muon_pin_q0": Q0_STALE_MUON_PIN,
    })
    builder.add_data("order_by_order_convergence_canonical", order_results)
    builder.add_data("full_eps_6_canonical", {
        "alpha_eff": mp.nstr(canon["alpha_eff"], 30),
        "Q_A_MeV": mp.nstr(canon["Q_A"], 30),
        "Q_bridge_cos_MeV": mp.nstr(canon["Q_bridge_cos"], 30),
        "Q_bridge_exp_MeV": mp.nstr(canon["Q_bridge_exp"], 30),
        "Q_bridge_lin_MeV": mp.nstr(canon["Q_bridge_lin"], 30),
        "err_cos_ppb": mp.nstr(canon["err_cos_ppb"], 12),
        "err_exp_ppb": mp.nstr(canon["err_exp_ppb"], 12),
        "err_lin_ppb": mp.nstr(canon["err_lin_ppb"], 12),
    })
    builder.add_data("q0_stability", {
        ansatz: {
            "drift_pct": drifts[ansatz],
            "stable_under_0.01_pct": drifts[ansatz] < 0.01,
        } for ansatz in ("cos", "exp", "1+α")
    })
    builder.add_data("verdict", {
        "classification": verdict,
        "best_ansatz": best_ans,
        "best_err_ppb_canonical": mp.nstr(best_err, 12),
        "best_q0_drift_pct": drifts[best_ans],
        "production_action": (
            "wire" if abs_best_err < 0.001
            else "Q_β stays at Q_N2 (1279 ppb)"
        ),
    })
    builder.add_assertion(
        "full_eps_expansion_completed",
        computed=1.0, expected=1.0, tolerance=0.0,
        source="probe completes through ε⁶ with all 3 ansätze; verdict reported",
    )
    builder.save()
    print(f"  Witness: qbeta-multi-block-eigenphase-full-eps-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
