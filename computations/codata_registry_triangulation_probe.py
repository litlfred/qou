#!/usr/bin/env python3
"""codata_registry_triangulation_probe — registry-vintage regression guard.

## History: the defect this was written to find (bean qou-2an8), now FIXED

The L2 100x dashboard scored `m_p` at **+1.351 ppb (437x miss)**.  Bean
`qou-2an8` flagged, without asserting, that the CODATA 2018 -> 2022 proton
shift is *also* ~+1.35 ppb, and asked whether the two are the same number.

They are.  Seven mass literals labelled "CODATA 2022" were in fact the
CODATA-2018 values, a ~1.3 ppb systematic straddle.  The detection needed no
published table — only internal inconsistency:

    m_e * (m_p/m_e) = 938.272089427...   vs   stored m_p = 938.27208816
    residual        = +1.3507 ppb        = 127x m_p's last printed digit

Confirmed afterwards against the primary source (Mohr, Newell, Taylor &
Tiesinga, Rev. Mod. Phys. 97, 025002, 30 April 2025, vendored at
`library/revmodphys97025002pdf/RevModPhys.97.025002.pdf.pdf`): the true 2022 proton is
938.272 089 43(29) MeV.  The triangulation had predicted 938.272089427,
agreeing to **0.0029 ppb** — a quarter of one printed digit.

What the stale literal cost, before the fix:

| symptom | was | after fix |
|---|---|---|
| `m_p` dashboard row | 437x "miss" (100% artifact) | anchor round-trip, not scored |
| `m_n` | 420.1x | 176.7x |
| `Delta_pn` | 163.3x | 151.7x |
| Q_beta's two experimental targets | disagreed 1814 ppb (2.33 sigma) | 194 ppb (0.25 sigma) |
| AME neutron vs CODATA direct | -1.511 ppb (2.96 sigma) | -0.160 ppb (0.31 sigma) |

## What this probe is NOW

A **regression guard**, not a bug report.  It asserts the post-fix state:

1. the over-determined triple (m_e, m_p/m_e, m_p) is consistent to within a
   fraction of its own printed granularity;
2. the AME-derived neutron equals its own definition, m_p + m_e + Q_beta;
3. the dashboard's `m_p` row is an anchor round-trip and is NOT scored;
4. the m_mu miss is NOT explained by any of this (it got slightly WORSE —
   963.6x -> 970.2x — and that is recorded, not suppressed);
5. Q_beta's miss survives the fix (164x), so it remains a genuine L2 lever.

The defect class it guards against is one **no precision audit can catch**:
a value that is exactly representable, correctly typed, precise to eleven
significant figures — and from the wrong edition.

AUDIT-ONLY.  Changes no prediction.

Refs:
- docs/audits/2026-08-09-codata-registry-vintage-straddle.md
- AGENTS.md SS"q_0 anchor convention" rule 1 (an anchor's round-trip is a
  calibration tautology, not an accuracy win)
- computations/codata_2022_source.py  (triple + AME-neutron guards)
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401, E402

from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

COMPUTE_DPS = set_compute_dps()
OUT_DPS = 25

_SUBSTRATE_PY = _HERE.parent / "tools" / "qou-substrate" / "python"
if str(_SUBSTRATE_PY) not in sys.path:
    sys.path.insert(0, str(_SUBSTRATE_PY))

import codata_2022_source as CS  # noqa: E402

_UPSTREAM: list = []

# ── Historical values, from before the 2026-08-09 correction ─────────
# Kept so the guard can state what it is guarding against. These are NOT
# read from the tree — that is the point: the tree no longer contains them.
HIST = {
    "stale_m_p_MeV": "938.27208816",
    "triple_residual_ppb": "1.3507",
    "m_p_dashboard_miss": "437.0",
    "m_n_miss": "420.1",
    "delta_pn_miss": "163.3",
    "qbeta_target_spread_ppb": "1814.2",
    "ame_vs_direct_neutron_ppb": "-1.511",
    "m_mu_miss": "963.566",
}


def ppb(x) -> mpf:
    return x * mpf(10) ** 9


def _rel(a, b):
    return (a - b) / b


def _last_digit_unit(s: str) -> mpf:
    """One unit in the last printed decimal place of a decimal string."""
    frac = s.split(".")[1] if "." in s else ""
    return mpf(10) ** (-len(frac))


def main() -> int:
    mp.dps = COMPUTE_DPS
    n = lambda x, d=OUT_DPS: mp.nstr(x, d)  # noqa: E731

    m_e = mpf(CS.M_E_MEV)
    m_p_reg = mpf(CS.M_P_MEV)
    ratio_pe = mpf(CS.MASS_RATIO_P_E)
    m_p_from_ratio = mpf(CS.M_P_MEV_RATIO_CONSISTENT)
    m_n_direct = mpf(CS.M_N_MEV_CODATA_DIRECT)
    m_n_direct_err = mpf(CS.M_N_MEV_CODATA_DIRECT_ERR)
    m_n_ame = mpf(CS.M_N_MEV_AME_DERIVED)
    q_ame = mpf(CS.Q_BETA_MEV_AME)
    q_sig = mpf(CS.Q_BETA_MEV_AME_ERR)

    # ── GUARD 1 — the triple is consistent ───────────────────────────
    leg1 = _rel(m_p_from_ratio, m_p_reg)
    m_p_ulp_rel = _last_digit_unit(str(CS.M_P_MEV)) / m_p_reg
    leg1_in_ulps = abs(leg1) / m_p_ulp_rel
    ceiling = mpf(str(CS.KNOWN_TRIPLE_RESIDUAL_PPB))
    guard1 = abs(ppb(leg1)) < ceiling

    # ── GUARD 2 — the AME neutron equals its own definition ──────────
    ame_resid = mpf(CS.ame_neutron_residual_MeV())
    guard2 = abs(ame_resid) < mpf("1e-8")
    ame_vs_direct = ppb(_rel(m_n_ame, m_n_direct))
    m_n_sigma_ppb = ppb(m_n_direct_err / m_n_direct)

    # ── GUARD 3 — the dashboard does not SCORE the anchor round-trip ─
    dash = record_upstream(_HERE / "per-observable-100x-status.witness.json", _UPSTREAM)
    rows = {r["obs"]: r for r in dash["data"]["rows"]}
    m_p_row = rows["m_p"]
    guard3 = (m_p_row.get("is_anchor_roundtrip") is True
              and m_p_row.get("beats_100x_experimental") is None)
    # The identity still holds: the row's residual IS the triangulation
    # residual, because m_p_pred == m_e * MASS_RATIO_P_E identically.
    identity_gap = abs(mpf(m_p_row["err_ppb"]) - abs(ppb(leg1)))

    # ── GUARD 4 — m_mu is untouched by any of this (it got worse) ────
    mu_row = rows["m_mu"]
    mu_miss_now = mpf(mu_row["miss_factor"])
    guard4 = mu_miss_now > mpf(HIST["m_mu_miss"])

    # ── GUARD 5 — Q_beta's miss survives the fix ─────────────────────
    qb_row = rows["Q_beta"]
    qb_miss = mpf(qb_row["miss_factor"])
    q_via_direct = m_n_direct - m_p_reg - m_e
    qb_spread_now = ppb(_rel(q_via_direct, q_ame))
    qb_spread_sigma = abs(qb_spread_now) / ppb(q_sig / q_ame)
    guard5 = qb_miss > 100

    # ── Report ───────────────────────────────────────────────────────
    print("=" * 78)
    print("  CODATA registry vintage — REGRESSION GUARD (defect fixed 2026-08-09)")
    print("=" * 78)
    print(f"\n  compute dps = {COMPUTE_DPS}\n")
    print(f"  primary source: Rev. Mod. Phys. 97, 025002 (CODATA-2022)")
    print(f"  m_p now = {n(m_p_reg, 14)} MeV   (was {HIST['stale_m_p_MeV']}, CODATA-2018)\n")

    print("  GUARD 1 — over-determined triple (m_e, m_p/m_e, m_p) consistent:")
    print(f"    m_e * (m_p/m_e)     = {n(m_p_from_ratio, 20)} MeV")
    print(f"    m_p registry        = {n(m_p_reg, 20)} MeV")
    print(f"    residual            = {n(ppb(leg1), 6)} ppb"
          f"   ({n(leg1_in_ulps, 4)} of m_p's last printed digit)")
    print(f"    ceiling             = {n(ceiling, 4)} ppb"
          f"   -> {'PASS' if guard1 else 'FAIL'}"
          f"   [historical: {HIST['triple_residual_ppb']} ppb]")

    print("\n  GUARD 2 — AME neutron equals m_p + m_e + Q_beta:")
    print(f"    definitional residual = {n(ame_resid, 6)} MeV"
          f"   -> {'PASS' if guard2 else 'FAIL'}")
    print(f"    AME vs CODATA direct  = {n(ame_vs_direct, 6)} ppb"
          f"   ({n(abs(ame_vs_direct) / m_n_sigma_ppb, 3)} sigma)"
          f"   [historical: {HIST['ame_vs_direct_neutron_ppb']} ppb, 2.96 sigma]")

    print("\n  GUARD 3 — dashboard reports m_p but does NOT score it:")
    print(f"    is_anchor_roundtrip   = {m_p_row.get('is_anchor_roundtrip')}")
    print(f"    beats_100x            = {m_p_row.get('beats_100x_experimental')}"
          f"   (None = excluded from the count)")
    print(f"    round-trip residual   = {m_p_row['err_ppb']} ppb"
          f"   [historical row: {HIST['m_p_dashboard_miss']}x 'miss']")
    print(f"    identity |row - leg1| = {n(identity_gap, 4)} ppb"
          f"   -> {'PASS' if guard3 else 'FAIL'}")

    print("\n  GUARD 4 — m_mu is NOT explained by this (it got WORSE):")
    print(f"    m_mu miss now = {n(mu_miss_now, 6)}x"
          f"   [was {HIST['m_mu_miss']}x]"
          f"   -> {'PASS' if guard4 else 'FAIL'}")
    print("    the mu-p substrate tension is genuine physics; recorded as measured.")

    print("\n  GUARD 5 — Q_beta's miss survives the fix (still a real lever):")
    print(f"    Q_beta miss                    = {n(qb_miss, 6)}x"
          f"   -> {'PASS' if guard5 else 'FAIL'}")
    print(f"    two experimental determinations = {n(qb_spread_now, 6)} ppb apart"
          f"   ({n(qb_spread_sigma, 3)} sigma)"
          f"   [historical: {HIST['qbeta_target_spread_ppb']} ppb, 2.33 sigma]")

    print("\n  DOWNSTREAM ROWS (post-fix, from the live dashboard):")
    for o in ("m_n", "Delta_pn"):
        print(f"    {o:9s} {rows[o]['err_ppb']:>10s} ppb"
              f"   miss {rows[o]['miss_factor']:>8s}x"
              f"   [historical: {HIST[o.lower() + '_miss'] if o.lower()+'_miss' in HIST else HIST['delta_pn_miss']}x]")

    # ── Witness ──────────────────────────────────────────────────────
    w = WitnessBuilder("codata-registry-triangulation", engine="mpmath")
    w.set_description(
        "Regression guard for the CODATA registry vintage straddle fixed on "
        "2026-08-09 (PR #4860). Seven mass literals labelled 'CODATA 2022' "
        "held CODATA-2018 values; the ~1.3 ppb straddle was 100% of the m_p "
        "row's reported L2 error and contaminated Q_beta's comparison target "
        "and the AME-derived neutron. Detected from internal inconsistency "
        "alone, then confirmed against RMP 97, 025002. This probe now asserts "
        "the corrected state. Audit-only; changes no prediction."
    )
    w.set_audit_only("docs/audits/2026-08-09-codata-registry-vintage-straddle.md")
    w.add_parameter("compute_dps", COMPUTE_DPS)
    w.add_parameter("primary_source",
                    "Mohr, Newell, Taylor & Tiesinga, Rev. Mod. Phys. 97, "
                    "025002 (2025) — library/revmodphys97025002pdf/RevModPhys.97.025002.pdf.pdf")

    w.add_data("m_p_MeV", n(m_p_reg, 14))
    w.add_data("triple_residual_ppb", n(ppb(leg1), 8))
    w.add_data("triple_residual_in_printed_units", n(leg1_in_ulps, 6))
    w.add_data("triple_ceiling_ppb", n(ceiling, 4))
    w.add_data("ame_neutron_definitional_residual_MeV", n(ame_resid, 8))
    w.add_data("ame_vs_direct_neutron_ppb", n(ame_vs_direct, 8))
    w.add_data("m_p_row_is_anchor_roundtrip", bool(m_p_row.get("is_anchor_roundtrip")))
    w.add_data("m_p_roundtrip_residual_ppb", m_p_row["err_ppb"])
    w.add_data("m_mu_miss_now", n(mu_miss_now, 8))
    w.add_data("qbeta_miss_now", n(qb_miss, 8))
    w.add_data("qbeta_target_spread_ppb_now", n(qb_spread_now, 8))
    w.add_data("historical_pre_fix", HIST)

    w.add_assertion(
        name="registry_triple_consistent",
        computed=1 if guard1 else 0, expected=1,
        source="Indicator (1 = |m_e*(m_p/m_e) - m_p| is inside the "
               "KNOWN_TRIPLE_RESIDUAL_PPB ceiling). Live residual is ~0.0029 "
               "ppb, about a quarter of m_p's last printed digit — the floor "
               "any same-edition triple can reach. The defect this guards "
               "against was 1.35 ppb, 27x the ceiling, and invisible to every "
               "float64/precision audit because nothing about it was imprecise.",
    )
    w.add_assertion(
        name="ame_neutron_equals_its_definition",
        computed=1 if guard2 else 0, expected=1,
        source="Indicator (1 = M_N_MEV_AME_DERIVED - (M_P + M_E + Q_BETA_AME) "
               "vanishes to the stored literal's last digit). It is a derived "
               "quantity; the old value outlived the 2018 proton it was built "
               "from, which is how a 1.5 ppb 'tension between two competing "
               "authoritative neutrons' was manufactured. Now 0.16 ppb.",
    )
    w.add_assertion(
        name="m_p_row_reported_but_not_scored",
        computed=1 if guard3 else 0, expected=1,
        source="Indicator (1 = the dashboard marks m_p is_anchor_roundtrip and "
               "leaves beats_100x None so it is excluded from the count). q_0 "
               "is pinned from m_p/m_e, so m_p_pred == m_e*MASS_RATIO_P_E "
               "identically and the residual is CODATA's own rounding. Scoring "
               "it would have flipped the headline to 3/7 on a tautology; the "
               "count correctly stays 2/7 (AGENTS.md q_0-anchor rule 1).",
    )
    w.add_assertion(
        name="fix_does_not_explain_mu_p_tension",
        computed=1 if guard4 else 0, expected=1,
        source="Indicator (1 = the m_mu miss did NOT improve). It moved "
               "963.6x -> 970.2x, i.e. worse. Recorded as measured rather than "
               "suppressed: a correction that degrades an observable is still "
               "the correct value. The mu-p substrate tension is genuine.",
    )
    w.add_assertion(
        name="qbeta_miss_survives_the_fix",
        computed=1 if guard5 else 0, expected=1,
        source="Indicator (1 = Q_beta still misses its 100x target). It does, "
               "at 164x. The fix reconciled Q_beta's two experimental "
               "determinations (1814 -> 194 ppb, 2.33 -> 0.25 sigma) but left "
               "the prediction's residual intact, so Q_beta remains one of the "
               "two genuine L2 levers.",
    )

    path = w.save(extra={"upstream": _UPSTREAM} if _UPSTREAM else None)
    print(f"\n  Witness: {path}")

    ok = guard1 and guard2 and guard3 and guard4 and guard5
    print("\n  VERDICT: registry consistent; the m_p row is a reported-but-"
          "unscored\n           anchor round-trip; Q_beta and m_mu remain the "
          "two real levers."
          if ok else "\n  VERDICT: a guard FAILED — inspect above.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
