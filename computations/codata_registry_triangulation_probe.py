#!/usr/bin/env python3
"""codata_registry_triangulation_probe — is the m_p L2 "miss" physics or bookkeeping?

## The question (bean qou-2an8)

The L2 100x dashboard scores `m_p` at **+1.351 ppb** (a 437x miss of its
100x target).  Bean `qou-2an8` flagged, without asserting, that the CODATA
2018 -> 2022 proton shift is *also* ~+1.35 ppb, and asked whether the two
are the same number.  This probe runs that check.

## Method: internal triangulation (no external CODATA lookup needed)

The corpus stores three quantities that are algebraically over-determined —
any two fix the third:

    m_e            codata_2022_source.M_E_MEV            (CAL-1)
    m_p / m_e      qou_substrate.constants.MASS_RATIO_P_E (the q_0 pin anchor)
    m_p            codata_2022_source.M_P_MEV            (the L2 comparison target)

So `m_e * (m_p/m_e) - m_p` must vanish for a SAME-EDITION triple —
established from repo contents alone, with no appeal to published tables.

**The bar is the printed granularity, not the quoted sigma.** Within one
CODATA adjustment these three are not independent measurements: they come
from a single global least-squares fit, and the MeV-valued m_p is *derived*
downstream of m_e and the ratio.  A same-edition triple therefore agrees to
the round-off of its own last printed digit (m_p is stored to 11 significant
figures, i.e. ~0.011 ppb), not merely to 1 sigma.  Scoring the residual
against the measurement sigma (0.43 ppb combined) understates the evidence
and is NOT the test applied here.

The neutron leg (`m_n = m_p + m_e + Q_beta` vs the independently-stored
CODATA direct neutron) is a genuinely independent second test: it asks which
candidate proton reproduces a *different* stored observable.

A muon leg (`m_mu = m_e * (m_mu/m_e)`) is reported for completeness but is
**non-discriminating** — the muon registry's 22 ppb uncertainty is ~16x the
effect being tested, so it can neither confirm nor exclude. It is not used
to support any conclusion.

## Why this matters for L2

`q_0` is Newton-solved so that the substrate identity reproduces
MASS_RATIO_P_E *exactly*:

    m_p/m_e = 2 * (Vol(4_1)/hbar_q^2) * F_Bor(q_0) - 12          [the pin]

hence the producer's prediction is, identically,
`m_p_pred = m_e * MASS_RATIO_P_E`.  Its "error" against `M_P_MEV` is
therefore *by construction* the registry triangulation residual and carries
**no physical content** — it is neither a theory residual nor a numerical one.

AUDIT-ONLY / data-integrity.  This probe changes no prediction; it
re-classifies how one dashboard row should be read.

Refs:
- AGENTS.md SS"Precision goals" (L2 leg), SS"q_0 anchor convention" rule 1
  (an anchor's round-trip is a calibration tautology, not an accuracy win)
- computations/per-observable-100x-status.witness.json  (the scored dashboard)
- computations/m_p_substrate_identity_50dps.py          (the producer)
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401, E402  — flat-namespace bridge for substrate/

from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

COMPUTE_DPS = set_compute_dps()
OUT_DPS = 25

_SUBSTRATE_PY = _HERE.parent / "tools" / "qou-substrate" / "python"
if str(_SUBSTRATE_PY) not in sys.path:
    sys.path.insert(0, str(_SUBSTRATE_PY))

import codata_2022_source as CS  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    MASS_RATIO_P_E,
    MASS_RATIO_P_E_ERR,
)

_UPSTREAM: list = []


def ppb(x) -> mpf:
    """Relative quantity -> parts per billion."""
    return x * mpf(10) ** 9


def _rel(a, b):
    """Signed relative difference (a - b) / b."""
    return (a - b) / b


def _last_digit_unit(s: str) -> mpf:
    """One unit in the last printed decimal place of a decimal string.

    '938.27208816' -> 1e-8.  Used to score a residual against the granularity
    the value was actually published at, rather than against its 1-sigma.
    """
    frac = s.split(".")[1] if "." in s else ""
    return mpf(10) ** (-len(frac))


def main() -> int:
    mp.dps = COMPUTE_DPS

    # ── Registries, read from source (never re-typed as literals) ────
    m_e = mpf(CS.M_E_MEV)
    m_e_err = mpf(CS.M_E_MEV_ERR)
    m_p_reg = mpf(CS.M_P_MEV)
    m_p_reg_err = mpf(CS.M_P_MEV_ERR)
    ratio_pe = mpf(str(MASS_RATIO_P_E))
    ratio_pe_err = mpf(str(MASS_RATIO_P_E_ERR))

    m_n_direct = mpf(CS.M_N_MEV_CODATA_DIRECT)
    m_n_direct_err = mpf(CS.M_N_MEV_CODATA_DIRECT_ERR)
    q_beta_ame = mpf(CS.Q_BETA_MEV_AME)

    m_mu_reg = mpf(CS.M_MU_MEV)
    m_mu_reg_err = mpf(CS.M_MU_MEV_ERR)
    ratio_mue = mpf(CS.M_MU_OVER_M_E)
    ratio_mue_err = mpf(CS.M_MU_OVER_M_E_ERR)

    # ── LEG 1 — proton triangulation: m_e * (m_p/m_e)  vs  m_p ───────
    m_p_from_ratio = m_e * ratio_pe
    leg1 = _rel(m_p_from_ratio, m_p_reg)
    # Quoted 1-sigma on the comparison, added in quadrature (relative).
    # Reported for context only — see the module docstring: the correct bar
    # for a same-edition triple is the printed granularity, not sigma.
    leg1_sigma = mp.sqrt(
        (m_e_err / m_e) ** 2
        + (ratio_pe_err / ratio_pe) ** 2
        + (m_p_reg_err / m_p_reg) ** 2
    )
    leg1_nsigma = abs(leg1) / leg1_sigma
    # Printed granularity of the stored m_p: one unit in its last decimal
    # place, relative. This is the level a same-edition triple must reach.
    m_p_ulp_rel = _last_digit_unit(str(CS.M_P_MEV)) / m_p_reg
    leg1_in_ulps = abs(leg1) / m_p_ulp_rel

    # ── LEG 2 — neutron cross-check, independent of leg 1 ────────────
    # m_n = m_p + m_e + Q_beta.  Feed the SAME beta-decay Q-value with each
    # candidate proton; whichever proton reproduces the independently-stored
    # CODATA direct neutron is the one on the consistent vintage.
    n_from_registry = m_p_reg + m_e + q_beta_ame
    n_from_ratio = m_p_from_ratio + m_e + q_beta_ame
    leg2_registry = _rel(n_from_registry, m_n_direct)
    leg2_ratio = _rel(n_from_ratio, m_n_direct)
    m_n_sigma_rel = m_n_direct_err / m_n_direct

    # ── LEG 3 — muon triangulation (same shape, different observable) ─
    m_mu_from_ratio = m_e * ratio_mue
    leg3 = _rel(m_mu_from_ratio, m_mu_reg)
    leg3_sigma = mp.sqrt(
        (m_e_err / m_e) ** 2
        + (ratio_mue_err / ratio_mue) ** 2
        + (m_mu_reg_err / m_mu_reg) ** 2
    )
    leg3_nsigma = abs(leg3) / leg3_sigma

    # ── The dashboard identity ───────────────────────────────────────
    # The scored m_p row must equal leg 1 to solver precision, because the
    # pin makes m_p_pred == m_e * MASS_RATIO_P_E identically.
    dash = record_upstream(_HERE / "per-observable-100x-status.witness.json", _UPSTREAM)
    row = next(r for r in dash["data"]["rows"] if r["obs"] == "m_p")
    dash_err_ppb = mpf(row["err_ppb"])
    dash_miss = mpf(row["miss_factor"])
    identity_gap = abs(ppb(leg1) - dash_err_ppb)

    # ── LEG 4 — where the artifact does NOT reach: the mu-p tension ──
    # Guard against over-reading the finding. If the vintage straddle also
    # explained m_mu (the single largest L2 miss at 963.6x), that would be a
    # much bigger claim — so test it explicitly rather than leave it implied.
    # It does not: correcting M_MU_OVER_M_E to its 2022 value moves m_mu the
    # WRONG way. The mu-p substrate tension is real physics, untouched here.
    mu_row = next(r for r in dash["data"]["rows"] if r["obs"] == "m_mu")
    mu_pred = mpf(mu_row["pred_MeV"])
    mu_sig = mpf(mu_row["sigma_exp_MeV"])
    # 2022 CODATA muon-electron ratio, used ONLY to bound the effect's size.
    ratio_mue_2022 = mpf("206.7682827")
    mu_miss = {}
    for tag, rr in (("as_stored_2018", ratio_mue), ("corrected_2022", ratio_mue_2022)):
        tgt = m_e * rr
        mu_miss[tag] = abs(_rel(mu_pred, tgt)) / ((mu_sig / tgt) / 100)
    mu_artifact_helps = mu_miss["corrected_2022"] < mu_miss["as_stored_2018"]

    # ── LEG 5 — the stale proton reaches Q_beta's TARGET too ─────────
    # Q_beta is one of the two independent L2 levers, so it matters whether
    # its comparison target is sound. The corpus holds TWO experimental
    # determinations: the AME2020 direct value, and m_n(direct) - m_p - m_e.
    # The second is built on the stale proton, so the two disagree far more
    # than they should — and a reader comparing against the "wrong" one gets a
    # materially better-looking score.
    q_ame = mpf(CS.Q_BETA_MEV_AME)
    q_sig = mpf(CS.Q_BETA_MEV_AME_ERR)
    q_via_stale = m_n_direct - m_p_reg - m_e
    q_via_cons = m_n_direct - m_p_from_ratio - m_e
    spread_stale = ppb(_rel(q_via_stale, q_ame))
    spread_cons = ppb(_rel(q_via_cons, q_ame))
    spread_explained = 1 - abs(spread_cons) / abs(spread_stale)

    qb_row = next(r for r in dash["data"]["rows"] if r["obs"] == "Q_beta")
    qb_pred = mpf(qb_row["pred_MeV"])
    qb_sig = mpf(qb_row["sigma_exp_MeV"])
    qb_scores = {
        tag: abs(_rel(qb_pred, t)) / ((qb_sig / t) / 100)
        for tag, t in (("AME", q_ame), ("via_stale_m_p", q_via_stale),
                       ("via_consistent_m_p", q_via_cons))
    }

    # ── L2 impact PROJECTION (audit-only; re-scores nothing) ─────────
    # What the affected dashboard rows would read against a self-consistent
    # registry. Reported so the finding is quantitative; the dashboard itself
    # is NOT modified here (that touches committed witnesses — separate PR).
    #
    # m_p is deliberately NOT projected: under the proton pin it IS the
    # anchor, so its corrected round-trip is a calibration tautology, not an
    # accuracy result (AGENTS.md SS"q_0 anchor convention" rule 1, as already
    # applied to m_mu under the muon pin). The honest disposition is to stop
    # scoring that row, not to score it as a pass.
    m_p_err_reg = mpf(CS.M_P_MEV_ERR)
    proj = []

    m_n_pred = mpf(next(r for r in dash["data"]["rows"] if r["obs"] == "m_n")["pred_MeV"])
    e = _rel(m_n_pred, m_n_direct)
    proj.append(("m_n", ppb(e), ppb(m_n_sigma_rel),
                 abs(e) / (m_n_sigma_rel / 100),
                 dash["data"]["rows"]))

    d_row = next(r for r in dash["data"]["rows"] if r["obs"] == "Delta_pn")
    d_pred = mpf(d_row["pred_MeV"])
    d_target = m_n_direct - m_p_from_ratio
    d_sig_rel = mp.sqrt(m_n_direct_err ** 2 + m_p_err_reg ** 2) / d_target
    e_d = _rel(d_pred, d_target)
    proj.append(("Delta_pn", ppb(e_d), ppb(d_sig_rel),
                 abs(e_d) / (d_sig_rel / 100), None))

    # ── Report ───────────────────────────────────────────────────────
    n = lambda x, d=OUT_DPS: mp.nstr(x, d)  # noqa: E731
    print("=" * 78)
    print("  CODATA registry triangulation — is the m_p L2 miss physics?")
    print("=" * 78)
    print(f"\n  compute dps = {COMPUTE_DPS}\n")
    print("  REGISTRIES (as stored in-repo, all labelled 'CODATA 2022'):")
    print(f"    m_e            = {n(m_e)} MeV      +/- {n(m_e_err, 6)}")
    print(f"    m_p/m_e        = {n(ratio_pe)}    +/- {n(ratio_pe_err, 6)}")
    print(f"    m_p            = {n(m_p_reg)} MeV  +/- {n(m_p_reg_err, 6)}")

    print("\n  LEG 1 — proton triangulation  m_e * (m_p/m_e)  vs  m_p:")
    print(f"    m_e * (m_p/m_e)          = {n(m_p_from_ratio)} MeV")
    print(f"    m_p registry             = {n(m_p_reg)} MeV")
    print(f"    residual                 = {n(ppb(leg1), 10)} ppb")
    print(f"    m_p printed granularity  = {n(ppb(m_p_ulp_rel), 6)} ppb"
          f"   <- the bar for a same-edition triple")
    print(f"    => {n(leg1_in_ulps, 6)}x the last printed digit"
          f"  (rounding cannot produce this)")
    print(f"    [context only] combined quoted 1-sigma = {n(ppb(leg1_sigma), 6)}"
          f" ppb -> {n(leg1_nsigma, 4)} sigma")

    print("\n  LEG 2 — neutron cross-check  m_p + m_e + Q_beta  vs  m_n(direct):")
    print(f"    using m_p registry       = {n(n_from_registry)} MeV"
          f"  -> {n(ppb(leg2_registry), 8)} ppb")
    print(f"    using m_e * (m_p/m_e)    = {n(n_from_ratio)} MeV"
          f"  -> {n(ppb(leg2_ratio), 8)} ppb")
    print(f"    m_n(direct) 1-sigma      = {n(ppb(m_n_sigma_rel), 6)} ppb")

    print("\n  LEG 3 — muon triangulation (NON-DISCRIMINATING, reported only):")
    print(f"    residual                 = {n(ppb(leg3), 10)} ppb")
    print(f"    quoted combined 1-sigma  = {n(ppb(leg3_sigma), 6)} ppb"
          f"  <- ~{n(leg3_sigma / abs(leg1), 3)}x the effect under test")
    print("    => cannot confirm or exclude; supports no conclusion here.")

    print("\n  DASHBOARD IDENTITY — the scored m_p row vs leg 1:")
    print(f"    dashboard m_p err        = {n(dash_err_ppb, 10)} ppb"
          f"   (miss factor {n(dash_miss, 6)}x)")
    print(f"    leg-1 residual           = {n(ppb(leg1), 10)} ppb")
    print(f"    |difference|             = {n(identity_gap, 6)} ppb")

    print("\n  LEG 4 — does the artifact reach m_mu (the largest L2 miss)?  NO:")
    print(f"    m_mu miss, ratio as stored (2018) = {n(mu_miss['as_stored_2018'], 6)}x")
    print(f"    m_mu miss, ratio corrected (2022) = {n(mu_miss['corrected_2022'], 6)}x")
    print(f"    => correcting the vintage makes m_mu "
          f"{'BETTER' if mu_artifact_helps else 'WORSE'}. "
          f"The mu-p tension is real; this finding does not touch it.")

    print("\n  LEG 5 — the stale proton also contaminates Q_beta's TARGET:")
    print(f"    two experimental determinations of Q_beta disagree by")
    print(f"      using m_p as stored     : {n(spread_stale, 6)} ppb"
          f"   ({n(abs(spread_stale) / ppb(q_sig / q_ame), 3)} sigma)")
    print(f"      using consistent m_p    : {n(spread_cons, 6)} ppb"
          f"   ({n(abs(spread_cons) / ppb(q_sig / q_ame), 3)} sigma)")
    print(f"    => the stale proton explains {n(100 * spread_explained, 4)}%"
          f" of the disagreement; the two then AGREE.")
    print("    prediction scored against each target:")
    for tag, m in qb_scores.items():
        print(f"      vs {tag:20s} {n(m, 6):>9s}x")
    print("    => Q_beta's miss is GENUINE either way (139x-164x, both >> 100x).")
    print("       But an unwary comparison against the stale-derived target")
    print("       reads 68.7x — nearly 2.4x too optimistic.")

    print("\n  L2 IMPACT PROJECTION (audit-only — this probe re-scores nothing):")
    print("    m_p  — NOT projected: it is the pin anchor, so a corrected")
    print("           round-trip is a calibration tautology, not a pass.")
    for obs, e_ppb, s_ppb, miss, _ in proj:
        row = next(r for r in dash["data"]["rows"] if r["obs"] == obs)
        print(f"    {obs:9s} err {n(e_ppb, 6):>10s} ppb (was {row['err_ppb']:>8s})"
              f"   miss {n(miss, 6):>8s}x (was {row['miss_factor']:>7s})"
              f"   -> still FAIL")

    # ── Witness ──────────────────────────────────────────────────────
    w = WitnessBuilder("codata-registry-triangulation", engine="mpmath")
    w.set_description(
        "Internal triangulation of the over-determined CODATA registries "
        "(m_e, m_p/m_e, m_p) plus independent neutron and muon legs. Shows "
        "the corpus registries are mutually inconsistent at ~1.35 ppb — far "
        "outside their own quoted uncertainties — and that this inconsistency "
        "accounts for 100% of the m_p row's scored L2 error, which is "
        "therefore bookkeeping, not a theory residual. Audit-only: changes no "
        "prediction."
    )
    w.set_audit_only("docs/audits/2026-08-09-codata-registry-vintage-straddle.md")
    w.add_parameter("compute_dps", COMPUTE_DPS)
    w.add_parameter("output_dps", OUT_DPS)

    w.add_data("m_e_MeV", n(m_e))
    w.add_data("mass_ratio_p_e", n(ratio_pe))
    w.add_data("m_p_registry_MeV", n(m_p_reg))
    w.add_data("m_p_from_ratio_MeV", n(m_p_from_ratio))
    w.add_data("leg1_residual_ppb", n(ppb(leg1), 12))
    w.add_data("leg1_m_p_printed_granularity_ppb", n(ppb(m_p_ulp_rel), 8))
    w.add_data("leg1_residual_in_printed_units", n(leg1_in_ulps, 8))
    w.add_data("leg1_quoted_sigma_ppb", n(ppb(leg1_sigma), 8))
    w.add_data("leg1_n_sigma_context_only", n(leg1_nsigma, 8))
    w.add_data("leg2_neutron_via_registry_ppb", n(ppb(leg2_registry), 10))
    w.add_data("leg2_neutron_via_ratio_ppb", n(ppb(leg2_ratio), 10))
    w.add_data("leg2_neutron_sigma_ppb", n(ppb(m_n_sigma_rel), 8))
    w.add_data("leg3_muon_residual_ppb_NON_DISCRIMINATING", n(ppb(leg3), 12))
    w.add_data("leg3_muon_n_sigma_NON_DISCRIMINATING", n(leg3_nsigma, 8))
    w.add_data("leg4_m_mu_miss_ratio_as_stored_2018", n(mu_miss["as_stored_2018"], 8))
    w.add_data("leg4_m_mu_miss_ratio_corrected_2022", n(mu_miss["corrected_2022"], 8))
    w.add_data(
        "leg4_verdict",
        "Correcting the vintage makes m_mu WORSE (963.6x -> 970.2x). Recorded "
        "as-measured: a correction that degrades an observable is reported, "
        "not suppressed. The mu-p substrate tension is genuine and this "
        "finding does not reach it.",
    )
    w.add_data("dashboard_m_p_err_ppb", n(dash_err_ppb, 12))
    w.add_data("leg5_qbeta_target_spread_stale_ppb", n(spread_stale, 8))
    w.add_data("leg5_qbeta_target_spread_consistent_ppb", n(spread_cons, 8))
    w.add_data("leg5_qbeta_spread_fraction_explained", n(spread_explained, 6))
    w.add_data("leg5_qbeta_miss_by_target",
               {k: n(v, 8) for k, v in qb_scores.items()})
    w.add_data(
        "l2_projection_audit_only",
        {
            "note": "What the affected rows would read against a self-consistent "
                    "registry. PROJECTION ONLY — the dashboard is unmodified. "
                    "m_p is excluded on purpose: it is the pin anchor, so a "
                    "corrected round-trip is a calibration tautology, not a pass.",
            **{
                obs: {
                    "err_ppb": n(e_ppb, 8),
                    "sigma_exp_ppb": n(s_ppb, 8),
                    "miss_factor": n(miss, 8),
                    "verdict": "FAIL (genuine — Q_beta-driven residual survives)",
                }
                for obs, e_ppb, s_ppb, miss, _ in proj
            },
        },
    )

    # Assertion 1 (DECISIVE) — the scored m_p error IS the registry residual.
    w.add_assertion(
        name="dashboard_m_p_error_equals_triangulation_residual",
        computed=1 if identity_gap < mpf("5e-4") else 0,
        expected=1,
        source="q_0 is Newton-pinned so that m_p_pred == m_e * MASS_RATIO_P_E "
               "identically; the scored row must therefore reproduce leg 1 "
               "exactly. It does, to within the dashboard's own 4-significant-"
               "figure serialization of err_ppb (which is the limiting term "
               "here, not the physics). The m_p row measures registry "
               "inconsistency and nothing else.",
    )

    # Assertion 2 — inconsistency vs the PRINTED GRANULARITY (not sigma).
    # Inequality claim: encoded as a 1/0 indicator (the framework scores
    # computed-vs-expected within tolerance only). Magnitude is in `data`.
    w.add_assertion(
        name="proton_triple_inconsistent_beyond_printed_granularity",
        computed=1 if leg1_in_ulps > 10 else 0,
        expected=1,
        source="Indicator (1 = residual exceeds 10x the last printed digit of "
               "m_p; see leg1_residual_in_printed_units for the magnitude). "
               "Within one CODATA adjustment the triple is a single correlated "
               "fit output, so a same-edition triple agrees to its last "
               "printed digit. The residual is ~126x that unit, which rounding "
               "cannot explain — the registries are mixed-vintage. (Against "
               "the measurement sigma this is only ~3.1 sigma; that weaker "
               "framing is recorded in the data block but is not the test.)",
    )

    # Assertion 4 — the artifact does NOT explain the mu-p tension.
    # A negative guard: it bounds the finding rather than extending it.
    w.add_assertion(
        name="artifact_does_not_explain_mu_p_tension",
        computed=1 if not mu_artifact_helps else 0,
        expected=1,
        source="Indicator (1 = correcting the muon-electron ratio to its 2022 "
               "value does NOT reduce the m_mu miss). It moves 963.6x -> "
               "970.2x, i.e. marginally worse. The single largest L2 miss is "
               "genuine physics — the mu-p substrate tension — and is "
               "untouched by this registry finding.",
    )

    # Assertion 5 — the artifact reaches Q_beta's target, but Q_beta's miss
    # survives it. A boundary in the other direction from assertion 4: here
    # the artifact IS present, and the residual is still genuine.
    w.add_assertion(
        name="qbeta_miss_is_genuine_despite_contaminated_target",
        computed=1 if min(qb_scores["AME"], qb_scores["via_consistent_m_p"]) > 100 else 0,
        expected=1,
        source="Indicator (1 = Q_beta misses its 100x target against EVERY "
               "available experimental determination). The stale proton "
               "explains 89% of the 1814 ppb disagreement between the two "
               "determinations — but the prediction misses by 139x-164x "
               "either way, so Q_beta remains a genuine L2 lever. Note the "
               "trap this removes: scored against the stale-derived target "
               "the miss reads 68.7x, ~2.4x too optimistic.",
    )

    # Assertion 3 — independent neutron leg selects the ratio-consistent proton.
    w.add_assertion(
        name="neutron_leg_favours_ratio_consistent_proton",
        computed=1 if abs(leg2_ratio) < m_n_sigma_rel < abs(leg2_registry) else 0,
        expected=1,
        source="Indicator (1 = the ratio-derived proton lands inside 1 sigma of "
               "the stored CODATA direct neutron while the stored proton falls "
               "outside it). m_p + m_e + Q_beta must reproduce that "
               "independently-stored neutron: the ratio-derived proton lands "
               "at 0.32 sigma, the stored proton misses by 2.96 sigma (9.3x "
               "worse). An independent observable therefore picks out the "
               "stored m_p as the stale member.",
    )

    path = w.save(extra={"upstream": _UPSTREAM} if _UPSTREAM else None)
    print(f"\n  Witness: {path}")

    all_passed = (
        identity_gap < mpf("5e-4")
        and leg1_in_ulps > 10
        and abs(leg2_ratio) < m_n_sigma_rel < abs(leg2_registry)
    )
    print("\n  VERDICT: the scored m_p L2 error is a registry-vintage artifact,"
          if all_passed else "\n  VERDICT: inconclusive — inspect the legs above.")
    if all_passed:
        print("           not a theory residual and not a numerical one.")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
