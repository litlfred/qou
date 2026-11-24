#!/usr/bin/env python3
"""qbeta_ck_basis_constrained_pslq.py — PROBE 4: basis-constrained PSLQ
per coefficient (docs/audits/2026-07-11-qbeta-ck-untested-avenues-and-literature.md §3.D).

TWO-STAGE, FORMALIZE-FIRST (compute-author.md §3.3; the PSLQ ENTROPY BOUND
of PR #1805: a PSLQ relation among n terms of integer height ≤ H is
meaningful ONLY if the target carries

        D_eff  >  n · log10(2·H)   (+ margin)

reliable digits; below that, ANY relation found is guaranteed-spurious
lattice noise).

STAGE 1 (entropy audit, mandatory, 80 dps, zero float64) — determine the
ACTUAL effective precision of the extracted c_3 / c_4 coefficients under the
canonical two-strand Markov trace z = q³/(q² + 1) (alongside the historical
z = √q/(1 + q) cache reference) by tracing the extraction chain:

    c_3_emp = (Q_β_CODATA / Q_N2 − 1) / u³ ,   u = b·ℏ_q² ≈ 0.008517
    c_4_emp = (Q_β_CODATA / Q_N3 − 1) / u⁴

The division by u³ ≈ 6.18e-7 (u⁴ ≈ 5.26e-9) AMPLIFIES the relative
experimental error of Q_β by ~1/(|c_k|·u^k). Error channels propagated:

  (a) experimental Q_β:  σ_rel ≈ 7.8e-7 (0.78 ppm; docs/precision-goals.md
      §L2 table — the "7.8 ppb" figure in circulation is the 100× TARGET
      σ_exp/100, not σ_exp). We audit BOTH readings — the kill must
      survive the most optimistic one.
  (b) q₀ pin:  cross-anchor dc_3/dq × pin precision (proton 0.06 ppb,
      muon 22 ppb).
  (c) observed inter-producer spread of historical c_3 readouts (~0.5%).

Note on the two-strand trace z = q³/(q² + 1) (bean qou-580o / qou-cds1):
substituting z = q³/(q² + 1) into the legacy eigenphase formula
α = (z − 1)h/2 yields c_3 ≈ −974.382 (muon pin) / −974.432 (proton pin),
a ~972.362 sensitivity shift relative to the retired z = √q/(1 + q) cache
(−2.020 / −2.069) because Q_N2 shifts by ~6×10⁻⁴ and is amplified by 1/u³.
Per QOU.QBeta.decayLadder_zC_threeRow_ne_zero and bean qou-cds1, −974.382
is a sensitivity readout, NOT a proposed c_3 coefficient, and is NOT wired
anywhere. Crucially, even at |c_3| ≈ 974.38 AND under the 100×-optimistic
σ(Q_β) = 7.8 ppb, D_eff(c_3) ≤ 4.89 < 9.20 digits (and ≤ 2.21 digits on the
historical cache), so Stage 1 is ENTROPY-BLOCKED in every frame and Stage 2
PSLQ is forbidden.

mpmath dps 80; zero float64.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys as _sys_qp
from datetime import datetime, timezone
from pathlib import Path as _Path_qp

import mpmath as mp

for _p_qp in (
    _Path_qp(__file__).resolve().parent.parent,
    _Path_qp(__file__).resolve().parent.parent / "substrate",
):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))

import _path_bridge  # noqa: F401, E402
from codata_constants import M_E_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_muon_at  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder, record_upstream  # noqa: E402

# Precision raised to 80 dps BEFORE module-scope constants.
mp.mp.dps = 80

_HERE = _Path_qp(__file__).resolve().parent
_COMP = _HERE.parent

# Both pins read BY NAME at 80 dps (manifest classifies this stem `ambiguous`).
Q0_CANONICAL = q_muon_at(80)
Q0_PROTON = q_at(80)
Q0_PROTON_50 = mp.mpf(Q_50_DIGIT_STR)

# Experimental relative uncertainty of Q_β (two readings audited)
SIGMA_Q_REL_ACTUAL = mp.mpf("7.8e-7")       # 0.78 ppm — precision-goals.md §L2
SIGMA_Q_REL_OPTIMISTIC = mp.mpf("7.8e-9")   # 7.8 ppb — 100× target read as σ

# q₀ pin precisions (relative) — AGENTS.md §q₀ anchor convention
PIN_REL_PROTON = mp.mpf("0.06e-9")   # 0.06 ppb
PIN_REL_MUON = mp.mpf("22e-9")       # 22 ppb

# Superseded pre-#1422 hopf-profile readout retained solely for spread audit
C3_EMP_MUON_HOPF = mp.mpf("-2.0097")

MARGIN_DIGITS = mp.mpf(3)  # confidence margin beyond the raw entropy floor


def ladder_chain(q: mp.mpf, q_beta_ref_mev: mp.mpf) -> dict[str, mp.mpf]:
    """Evaluate the c_3/c_4 extraction chain at anchor q under the canonical
    two-strand Markov trace weight z = q³ / (q² + 1)."""
    h = q - mp.mpf(1) / q
    z = q ** 3 / (q ** 2 + mp.mpf(1))
    alpha = (z - mp.mpf(1)) * h / mp.mpf(2)
    d1 = q ** 3 / (q ** 2 + mp.mpf(1))
    d2 = -mp.mpf(1) / (q * (q ** 2 + mp.mpf(1)))
    b = mp.sqrt(d1 * d2 + mp.mpf(1))
    hbar_q = (q - mp.mpf(1)) / q
    u = b * hbar_q ** 2
    Q_A = (
        M_E_MEV
        * (mp.mpf(2) * q + mp.mpf(1) - q ** 2)
        * (q + mp.mpf(1))
        / (mp.mpf(2) * q ** 3)
    )
    alpha_eff = alpha - b * hbar_q ** 2 / mp.mpf(2)
    Q_N1 = Q_A * mp.cos(alpha_eff)
    Q_N2 = Q_N1 * (mp.mpf(1) - u ** 2)  # c_2 = -1
    c3 = (q_beta_ref_mev / Q_N2 - mp.mpf(1)) / u ** 3
    Q_N3 = Q_N2 * (mp.mpf(1) + c3 * u ** 3)
    c4 = (q_beta_ref_mev / Q_N3 - mp.mpf(1)) / u ** 4
    return {"u": u, "Q_N2": Q_N2, "Q_N3": Q_N3, "c3": c3, "c4": c4}


def eff_digits_mpf(value: mp.mpf, err: mp.mpf) -> mp.mpf:
    """Effective significant digits log10(|value|/err) in mpmath (zero float64)."""
    if err <= 0:
        return mp.mpf("1e9")
    r = mp.fabs(value) / err
    return mp.log10(r) if r > mp.mpf(1) else mp.mpf(0)


def fmt_2dp(val: mp.mpf) -> str:
    """Deterministic 2-decimal-place string via mp.nint (zero float64)."""
    scaled = int(mp.nint(val * mp.mpf(100)))
    sign = "-" if scaled < 0 else ""
    a = abs(scaled)
    return f"{sign}{a // 100}.{a % 100:02d}"


def main():
    mp.mp.dps = 80
    upstream_records: list = []

    ck_cache_path = _COMP / "qbeta" / "qbeta-ck-cache.witness.json"
    sens_path = (
        _COMP
        / "qbeta"
        / "qbeta-c3-ladder-trace-convention-sensitivity.witness.json"
    )
    ck_cache_doc = record_upstream(ck_cache_path, upstream_records)
    sens_doc = record_upstream(sens_path, upstream_records)

    q_beta_codata_mev = mp.mpf(ck_cache_doc["data"]["Q_codata"])
    c3_hist_proton = mp.mpf(
        next(r["c_k"] for r in ck_cache_doc["data"]["rows"] if r["k"] == 3)
    )
    c3_hist_muon = mp.mpf(sens_doc["result"]["c3"]["C_muon"])
    c3_sens_d_muon = mp.mpf(sens_doc["result"]["c3"]["D_muon"])
    c3_sens_d_proton = mp.mpf(sens_doc["result"]["c3"]["D_proton"])

    print("=" * 78)
    print(" PROBE 4 — basis-constrained PSLQ: STAGE 1 entropy audit (80 dps)")
    print("=" * 78)

    # -----------------------------------------------------------------
    # Canonical two-strand trace z = q³/(q² + 1) extraction at both pins
    # -----------------------------------------------------------------
    chain_muon = ladder_chain(Q0_CANONICAL, q_beta_codata_mev)
    chain_proton = ladder_chain(Q0_PROTON, q_beta_codata_mev)
    u = chain_muon["u"]
    c3_muon = chain_muon["c3"]
    c4_muon = chain_muon["c4"]
    c3_proton = chain_proton["c3"]
    c4_proton = chain_proton["c4"]

    sens_diff_muon = mp.fabs(c3_muon - c3_sens_d_muon)
    sens_diff_proton = mp.fabs(c3_proton - c3_sens_d_proton)
    max_sens_diff = max(sens_diff_muon, sens_diff_proton)
    max_c4_abs = max(mp.fabs(c4_muon), mp.fabs(c4_proton))
    trace_shift_vs_hist_cache = mp.fabs(c3_muon - c3_hist_muon)

    print("\n  extraction chain under two-strand trace z = q³/(q² + 1):")
    print(f"    u = b·ℏ_q² (muon)        = {mp.nstr(u, 25)}")
    print(f"    c_3 sensitivity (muon)   = {mp.nstr(c3_muon, 30)}")
    print(f"    c_3 sensitivity (proton) = {mp.nstr(c3_proton, 30)}")
    print(f"    |Δ vs sensitivity ref|   = {mp.nstr(max_sens_diff, 6)}")
    print(f"    shift vs z=√q/(1+q) cache= {mp.nstr(trace_shift_vs_hist_cache, 10)}")
    print(f"    max |c_4| (exact chain)  = {mp.nstr(max_c4_abs, 6)}")

    # -----------------------------------------------------------------
    # Error propagation — both consistent z = q³/(q²+1) and historical cache
    # -----------------------------------------------------------------
    dc3_dQ_muon = (q_beta_codata_mev / chain_muon["Q_N2"]) / (chain_muon["u"] ** 3)
    dc3_dQ_proton = (q_beta_codata_mev / chain_proton["Q_N2"]) / (chain_proton["u"] ** 3)
    dc4_dQ_muon = (q_beta_codata_mev / chain_muon["Q_N3"]) / (chain_muon["u"] ** 4)

    slope_c3_two_strand = (c3_proton - c3_muon) / (Q0_PROTON - Q0_CANONICAL)
    slope_c3_hist = (c3_hist_proton - c3_hist_muon) / (Q0_PROTON - Q0_CANONICAL)

    scenarios = []
    scenario_d3_vals: list[mp.mpf] = []
    for label, sigma_q in (
        ("actual sigma(Q)=0.78ppm", SIGMA_Q_REL_ACTUAL),
        ("optimistic sigma(Q)=7.8ppb", SIGMA_Q_REL_OPTIMISTIC),
    ):
        for frame_tag, anchor, pin_rel, q_pin, c3_val, dc3_dQ_val, slope_val in (
            ("z=q^3/(q^2+1)", "proton", PIN_REL_PROTON, Q0_PROTON,
             c3_proton, dc3_dQ_proton, slope_c3_two_strand),
            ("z=q^3/(q^2+1)", "muon", PIN_REL_MUON, Q0_CANONICAL,
             c3_muon, dc3_dQ_muon, slope_c3_two_strand),
            ("historical_z=sqrt(q)/(1+q)_cache", "proton", PIN_REL_PROTON,
             Q0_PROTON, c3_hist_proton, dc3_dQ_proton, slope_c3_hist),
            ("historical_z=sqrt(q)/(1+q)_cache", "muon", PIN_REL_MUON,
             Q0_CANONICAL, c3_hist_muon, dc3_dQ_muon, slope_c3_hist),
        ):
            dq = pin_rel * q_pin
            err_c3_Q = sigma_q * dc3_dQ_val
            err_c3_pin = mp.fabs(slope_val) * dq
            err_c3 = mp.sqrt(err_c3_Q ** 2 + err_c3_pin ** 2)
            err_c4 = sigma_q * dc4_dQ_muon
            d3 = eff_digits_mpf(c3_val, err_c3)
            d4 = eff_digits_mpf(c4_muon, err_c4)
            scenario_d3_vals.append(d3)
            scenarios.append({
                "trace_frame": frame_tag,
                "scenario": label,
                "anchor": anchor,
                "err_c3_from_Q": mp.nstr(err_c3_Q, 6),
                "err_c3_from_pin": mp.nstr(err_c3_pin, 6),
                "err_c3_total": mp.nstr(err_c3, 6),
                "eff_digits_c3": fmt_2dp(d3),
                "err_c4_from_Q": mp.nstr(err_c4, 6),
                "eff_digits_c4": fmt_2dp(d4),
            })

    spread = mp.fabs(c3_hist_muon - C3_EMP_MUON_HOPF)
    d_spread = eff_digits_mpf(c3_hist_muon, spread)

    # -----------------------------------------------------------------
    # Entropy budget vs requirement (exact mpmath log10)
    # -----------------------------------------------------------------
    budgets = []
    budget_reqs: list[mp.mpf] = []
    for n_terms, height, note in (
        (4, 100, "MINIMAL basis (kill threshold per task spec)"),
        (6, 10, "full basis {1,√3,π²,Vol(4₁),ζ(3)} + target, H=10"),
        (6, 100, "full basis + target, H=100"),
    ):
        d_req = mp.mpf(n_terms) * mp.log10(mp.mpf(2 * height))
        budget_reqs.append(d_req)
        budgets.append({
            "n_terms": n_terms,
            "height_bound": height,
            "digits_required": fmt_2dp(d_req),
            "digits_required_with_margin": fmt_2dp(d_req + MARGIN_DIGITS),
            "note": note,
        })

    d_eff_best = max(scenario_d3_vals)
    d_eff_best_hist = max(scenario_d3_vals[2], scenario_d3_vals[3],
                          scenario_d3_vals[6], scenario_d3_vals[7])
    d_req_min = budget_reqs[0]
    deficit_min = d_req_min - d_eff_best
    entropy_blocked = bool(d_eff_best < d_req_min)
    n_max_h10 = int(mp.floor(d_eff_best / mp.log10(mp.mpf(20))))
    sigma_needed_hist = (
        (mp.mpf(10) ** (-d_req_min)) * mp.fabs(c3_hist_muon) / dc3_dQ_muon
    )
    sigma_needed_two_strand = (
        (mp.mpf(10) ** (-d_req_min)) * mp.fabs(c3_muon) / dc3_dQ_muon
    )

    verdict = "ENTROPY-BLOCKED" if entropy_blocked else "STAGE-1-PASS"
    print(f"\n  best-case D_eff(c_3) at z = q³/(q²+1)      = {fmt_2dp(d_eff_best)}")
    print(f"  best-case D_eff(c_3) on historical cache    = {fmt_2dp(d_eff_best_hist)}")
    print(f"  minimal requirement (n=4, H=100)            = {fmt_2dp(d_req_min)}")
    print(f"  STAGE 1 VERDICT: {verdict}")

    stage2 = None
    if not entropy_blocked:
        stage2 = run_stage2(c3_proton, c3_muon)
    else:
        print("  Stage 2 PSLQ NOT RUN — running PSLQ on noise is forbidden.")

    vol41 = mp.mpf(2) * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / mp.mpf(3))))
    out = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "qbeta-ck-basis-constrained-pslq",
        "scriptFile": "qbeta_ck_basis_constrained_pslq.py",
        "commitSha": subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip(),
        "description": (
            "PROBE 4 (avenues audit §3.D, 80 dps): two-stage basis-constrained "
            "PSLQ audit for Q_β ladder coefficients c_3/c_4 against the "
            "arithmetic basis {1, √3, π², Vol(4₁), ζ(3)}. Stage 1 propagates "
            "experimental Q_β and q₀-pin uncertainties through "
            "c_3 = (Q_CODATA/Q_N2 − 1)/u³ (1/u³ ≈ 1.6e6 amplifier) under the "
            "canonical two-strand Markov trace z = q³/(q² + 1) alongside the "
            "historical z = √q/(1 + q) cache reference. Even under the 100×-"
            "optimistic σ(Q_β) = 7.8 ppb, D_eff(c_3) ≤ 4.89 < 9.20 digits "
            "(ENTROPY-BLOCKED), so Stage 2 PSLQ is not run. The −974.382 "
            "readout under z = q³/(q² + 1) is a sensitivity diagnostic of "
            "substituting z = q³/(q² + 1) into α = (z − 1)h/2, not a proposed "
            "c_3 value; nothing is wired."
        ),
        "precisionMetadata": {
            "compute_dps": 80,
            "output_dps": 60,
            "guard_digits": 20,
            "truncation_bound": "1e-60",
        },
        "data": {
            "q0_canonical": mp.nstr(Q0_CANONICAL, 60, strip_zeros=False),
            "q0_proton": mp.nstr(Q0_PROTON, 60, strip_zeros=False),
            "q0_proton_50dps_pin": mp.nstr(Q0_PROTON_50, 50, strip_zeros=False),
            "Q_beta_codata_MeV": mp.nstr(q_beta_codata_mev, 15),
            "u_substrate": mp.nstr(u, 50),
            "u_cubed": mp.nstr(u ** 3, 25),
            "u_fourth": mp.nstr(u ** 4, 25),
            "c3_reproduced_canonical": mp.nstr(c3_muon, 50),
            "c3_reproduced_proton_two_strand": mp.nstr(c3_proton, 50),
            "c3_sensitivity_witness_max_diff": mp.nstr(max_sens_diff, 12),
            "c3_trace_shift_vs_historical_sqrt_cache": mp.nstr(
                trace_shift_vs_hist_cache, 20
            ),
            "c3_cache_value": mp.nstr(c3_hist_muon, 30),
            "c3_proton_on_record": mp.nstr(c3_hist_proton, 30),
            "c3_muon_hopf_on_record": mp.nstr(C3_EMP_MUON_HOPF, 8),
            "c4_reproduced_canonical": mp.nstr(c4_muon, 20),
            "c4_reproduced_proton": mp.nstr(c4_proton, 20),
            "c4_artifact_note": (
                "c_4 is identically 0 when c_3 is extracted without rounding "
                "against the same Q_β reference (Q_N3 = Q_CODATA identically); "
                "quoted nonzero c_4 values are rounding residuals of a "
                "truncated c_3 and carry zero independent empirical content."
            ),
            "amplifier_dc3_dQrel": mp.nstr(dc3_dQ_muon, 15),
            "amplifier_dc4_dQrel": mp.nstr(dc4_dQ_muon, 15),
            "anchor_slope_dc3_dq_two_strand": mp.nstr(slope_c3_two_strand, 15),
            "anchor_slope_dc3_dq_historical_cache": mp.nstr(slope_c3_hist, 15),
            "sigma_Q_rel_actual": mp.nstr(SIGMA_Q_REL_ACTUAL, 4),
            "sigma_Q_rel_optimistic_reading": mp.nstr(SIGMA_Q_REL_OPTIMISTIC, 4),
            "error_scenarios": scenarios,
            "inter_producer_spread_c3": mp.nstr(spread, 6),
            "inter_producer_stable_digits": fmt_2dp(d_spread),
            "entropy_budgets": budgets,
            "margin_digits": "3.00",
            "best_case_eff_digits_c3": fmt_2dp(d_eff_best),
            "best_case_eff_digits_c3_historical_cache": fmt_2dp(d_eff_best_hist),
            "minimal_requirement_digits": fmt_2dp(d_req_min),
            "digit_deficit": fmt_2dp(deficit_min),
            "max_supportable_basis_terms_at_H10": n_max_h10,
            "sigma_Q_rel_needed_for_minimal_budget_two_strand": mp.nstr(
                sigma_needed_two_strand, 4
            ),
            "sigma_Q_rel_needed_for_minimal_budget": mp.nstr(
                sigma_needed_hist, 4
            ),
            "arithmetic_basis_not_run": {
                "1": "1",
                "sqrt3": mp.nstr(mp.sqrt(mp.mpf(3)), 50),
                "pi^2": mp.nstr(mp.pi ** 2, 50),
                "Vol(4_1)=2*Cl_2(pi/3)=6*Lambda(pi/3)": mp.nstr(vol41, 50),
                "zeta(3)": mp.nstr(mp.zeta(3), 50),
            },
            "upstream_witness_hashes": upstream_records,
        },
        "assertions": [
            {
                "name": "two_strand_chain_matches_sensitivity_reference",
                "computed": mp.nstr(max_sens_diff, 10),
                "expected": "0",
                "passed": bool(max_sens_diff < mp.mpf("1e-12")),
                "tolerance": "1e-12",
                "source": (
                    "80-dps extraction under z = q³/(q² + 1) at both muon and "
                    "proton anchors matches the 16-digit sensitivity values in "
                    "qbeta-c3-ladder-trace-convention-sensitivity.witness.json "
                    "(−974.3821470795362 / −974.4318877467484, sensitivity "
                    "readout only — NOT a proposed c_3 and NOT wired; differs "
                    "from the historical z = √q/(1 + q) cache by ~972.362)."
                ),
            },
            {
                "name": "c4_identically_zero_at_exact_extraction",
                "computed": mp.nstr(max_c4_abs, 10),
                "expected": "0",
                "passed": bool(max_c4_abs < mp.mpf("1e-70")),
                "tolerance": "1e-70",
                "source": (
                    "Q_N3 = Q_N2·(1 + c_3·u³) = Q_CODATA identically at 80 dps "
                    "when c_3 is unrounded, so rung 4 carries zero independent "
                    "empirical content for PSLQ."
                ),
            },
            {
                "name": "stage1_entropy_verdict_is_blocked",
                "computed": 1 if entropy_blocked else 0,
                "expected": 1,
                "passed": entropy_blocked,
                "tolerance": 0,
                "source": (
                    "PSLQ entropy bound (PR #1805): best-case D_eff(c_3) = "
                    f"{fmt_2dp(d_eff_best)} digits (z = q³/(q² + 1)) and "
                    f"{fmt_2dp(d_eff_best_hist)} digits (historical cache) both "
                    f"fall strictly below minimal 4·log10(200) = "
                    f"{fmt_2dp(d_req_min)} digits; Stage 2 PSLQ not run."
                ),
            },
        ],
        "verdict": {
            "stage1": verdict,
            "stage2_run": stage2 is not None,
            "stage2": stage2,
            "conclusion": (
                "ENTROPY-BLOCKED at 80 dps: the extracted c_3 carries at most "
                f"{fmt_2dp(d_eff_best)} effective digits under z = q³/(q² + 1) "
                f"(and {fmt_2dp(d_eff_best_hist)} digits on the historical "
                "z = √q/(1 + q) cache; c_4: zero) even under the 100×-"
                "optimistic σ(Q_β) = 7.8 ppb, whereas the minimal 4-term "
                f"H ≤ 100 PSLQ basis requires {fmt_2dp(d_req_min)} digits "
                "(before margin). Stage 2 PSLQ was NOT run — any integer "
                "relation returned below the entropy floor is lattice noise. "
                "Moreover, the −974.382 readout under z = q³/(q² + 1) is an "
                "amplified sensitivity artifact of α = (z − 1)h/2, not a "
                "derived ladder coefficient; no c_k value is proposed or wired."
                if entropy_blocked
                else "Stage 1 passed; see stage2 results."
            ),
        },
    }
    out["allPassed"] = all(a["passed"] for a in out["assertions"])

    wpath = os.path.join(str(_HERE), "qbeta-ck-basis-constrained-pslq.witness.json")
    with open(wpath, "w") as f:
        out.setdefault("scriptFile", os.path.basename(__file__))
        out["markov_convention"] = "D"
        out["markov_convention_reason"] = (
            "Evaluates ladder_chain under the canonical two-strand Markov "
            "trace z = q**3 / (q**2 + 1) at 80 dps, recording −974.382147... "
            "(muon) and −974.431887... (proton) purely as sensitivity "
            "diagnostics alongside the historical z = sqrt(q)/(1 + q) cache "
            "readouts; Stage 1 is ENTROPY-BLOCKED in both frames and nothing "
            "is wired."
        )
        WitnessBuilder.stamp_staleness_metadata(
            out,
            script_path=__file__,
            engine=None,
            q0_anchor="ambiguous",
            q0_anchor_reason=(
                "Evaluates BOTH canonical pins on purpose at 80 dps: "
                "data.q0_canonical (muon) and data.q0_proton (proton) to "
                "propagate cross-anchor slope dc_3/dq into the Stage-1 PSLQ "
                "entropy bound; listed under `ambiguous` in "
                "q0_anchor_manifest.json."
            ),
        )
        json.dump(out, f, indent=2)
    print(f"\n  witness → {wpath}")
    return out


def run_stage2(c3_proton: mp.mpf, c3_muon: mp.mpf):
    """STAGE 2 — per-coefficient, per-anchor PSLQ against the arithmetic
    basis {1, √3, π², Vol(4₁), ζ(3)}. GATED: called only if Stage 1 passes
    the entropy bound."""
    basis = [
        mp.mpf(1),
        mp.sqrt(mp.mpf(3)),
        mp.pi ** 2,
        mp.mpf(2) * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / mp.mpf(3)))),
        mp.zeta(3),
    ]
    results = {}
    for name, c3_val in (("proton", c3_proton), ("muon", c3_muon)):
        vec = [c3_val] + basis
        rel = mp.pslq(vec, maxcoeff=100, maxsteps=10 ** 5)
        results[name] = [int(x) for x in rel] if rel else None
    anchor_stable = (
        results["proton"] is not None and results["proton"] == results["muon"]
    )
    return {
        "per_anchor": results,
        "anchor_stable": anchor_stable,
        "tier": "near-match at best; NEVER a derivation; NOT wired",
    }


if __name__ == "__main__":
    main()
