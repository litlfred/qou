#!/usr/bin/env python3
"""l2_row_independence_probe — how many INDEPENDENT failures are on the L2 list?

## The question

The per-observable 100x dashboard reports 7 observables, 5 of them failing:
m_p (437x), m_n (420x), Delta_pn (163x), Q_beta (164x), m_mu (964x).  Read
as a scoreboard that says "five separate things are broken" — and therefore
as five places to look for a fix.

It does not.  Three of those five rows are algebraically dependent on the
other two, in BOTH the prediction and the comparison target:

    Delta_pn  ==  Q_beta + m_e            (definitionally, both sides)
    m_n       ==  m_p + Q_beta + m_e      (definitionally, both sides)

The target side is dependent because `M_N_MEV_AME_DERIVED` is *constructed*
as `M_P_MEV + M_E_MEV + Q_BETA_MEV_AME` — the neutron "measurement" the
dashboard scores against is built from the proton registry and the AME
beta-decay Q-value, not measured independently of them.

So `m_n` and `Delta_pn` contribute no information the {m_p, Q_beta} rows do
not already carry.  Combined with the companion finding that the `m_p` row
is a registry-vintage artifact (codata_registry_triangulation_probe.py), the
five failures reduce to **two independent physical failures**: Q_beta and
m_mu.

## Why this matters

L2 planning that treats the list as five fronts will over-count the work and
mis-rank it.  There are two levers: the Q_beta / Habiro closure (bean `kehn`)
and the mu-p substrate tension.  Everything else on the fail list is those
two, re-expressed.

## What this probe does NOT claim

- It does not claim the dependent rows are *wrong* to report. Reporting m_n
  in MeV is useful; the point is only that it is not an independent test.
- It does not claim m_mu and Q_beta are the only *possible* failures — only
  that they are the only independent ones among the rows currently scored.
- It says nothing about whether the corpus holds a genuinely independent
  neutron measurement. `M_N_MEV_CODATA_DIRECT` exists and IS independent;
  it is simply not what the dashboard scores against (see the companion
  probe's L2 projection, which uses it).

AUDIT-ONLY.  Changes no prediction and re-scores nothing.

Refs:
- computations/codata_registry_triangulation_probe.py  (companion finding)
- docs/audits/2026-08-09-codata-registry-vintage-straddle.md
- AGENTS.md SS"Precision goals" (the L2 leg)
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

import codata_2022_source as CS  # noqa: E402

COMPUTE_DPS = set_compute_dps()
_UPSTREAM: list = []


def main() -> int:
    mp.dps = COMPUTE_DPS
    n = lambda x, d=6: mp.nstr(x, d)  # noqa: E731

    dash = record_upstream(_HERE / "per-observable-100x-status.witness.json", _UPSTREAM)
    rows = {r["obs"]: r for r in dash["data"]["rows"]}
    m_e = mpf(CS.M_E_MEV)

    def pred(o):
        return mpf(rows[o]["pred_MeV"])

    def targ(o):
        return mpf(rows[o]["codata_MeV"])

    # The dashboard serializes pred_MeV / codata_MeV to ~12 significant
    # figures, so an exact identity shows up as a residual at that granularity
    # (~1e-9 MeV on a ~1e3 MeV quantity), NOT as a bitwise zero. Score against
    # that granularity, not against zero.
    ser_tol_MeV = mpf("1e-8")

    checks = [
        ("Delta_pn == Q_beta + m_e",
         pred("Delta_pn") - (pred("Q_beta") + m_e),
         targ("Delta_pn") - (targ("Q_beta") + m_e)),
        ("m_n == m_p + Q_beta + m_e",
         pred("m_n") - (pred("m_p") + pred("Q_beta") + m_e),
         targ("m_n") - (targ("m_p") + targ("Q_beta") + m_e)),
    ]

    print("=" * 78)
    print("  L2 row independence — how many INDEPENDENT failures are listed?")
    print("=" * 78)
    print(f"\n  compute dps = {COMPUTE_DPS}")
    print(f"  identity tolerance = {n(ser_tol_MeV)} MeV"
          f"  (the dashboard's own ~12-sig-fig serialization)\n")

    print("  SCORED ROWS (as published):")
    for o in ("m_p", "m_n", "Delta_pn", "Q_beta", "m_mu"):
        r = rows[o]
        print(f"    {o:9s} err {r['err_ppb']:>9s} ppb   miss {r['miss_factor']:>8s}x")

    print("\n  DEPENDENCE CHECKS (must hold on BOTH sides to be redundant):")
    all_dep = True
    for label, dp, dt in checks:
        ok = abs(dp) < ser_tol_MeV and abs(dt) < ser_tol_MeV
        all_dep &= ok
        print(f"    {label}")
        print(f"      prediction side residual = {n(dp, 4):>10s} MeV")
        print(f"      target     side residual = {n(dt, 4):>10s} MeV"
              f"   <- target is CONSTRUCTED, not independently measured")
        print(f"      => {'REDUNDANT' if ok else 'independent'}")

    print("\n  CONCLUSION:")
    print("    m_p       artifact  — pin-anchor round-trip vs a stale registry")
    print("                          (see codata_registry_triangulation_probe)")
    print("    m_n       redundant — == m_p + Q_beta + m_e on both sides")
    print("    Delta_pn  redundant — == Q_beta + m_e on both sides")
    print("    Q_beta    INDEPENDENT FAILURE  (lever: Habiro closure, bean kehn)")
    print("    m_mu      INDEPENDENT FAILURE  (lever: mu-p substrate tension)")
    print("\n    => 5 reported failures are 2 independent ones.")

    w = WitnessBuilder("l2-row-independence", engine="mpmath")
    w.set_description(
        "Shows that 3 of the 5 failing rows on the per-observable 100x L2 "
        "dashboard are algebraically dependent on the other 2, in both the "
        "prediction and the comparison target (the neutron target is "
        "constructed as M_P + M_E + Q_BETA, not measured independently). With "
        "the m_p row separately shown to be a registry-vintage artifact, the "
        "five reported failures reduce to two independent ones: Q_beta and "
        "m_mu. Audit-only; re-scores nothing."
    )
    w.set_audit_only("docs/audits/2026-08-09-codata-registry-vintage-straddle.md")
    w.add_parameter("compute_dps", COMPUTE_DPS)
    w.add_parameter("identity_tolerance_MeV", str(ser_tol_MeV))

    for label, dp, dt in checks:
        key = label.split(" ==")[0].strip()
        w.add_data(f"residual_pred_{key}_MeV", n(dp, 6))
        w.add_data(f"residual_target_{key}_MeV", n(dt, 6))
    w.add_data("independent_failures", ["Q_beta", "m_mu"])
    w.add_data("redundant_rows", ["m_n", "Delta_pn"])
    w.add_data("artifact_rows", ["m_p"])
    w.add_data(
        "caveat",
        "Redundant does not mean wrong to report — m_n in MeV is a useful "
        "number. It means the row is not an independent test, so L2 planning "
        "must not count it as a separate front. M_N_MEV_CODATA_DIRECT IS an "
        "independent neutron value; it is simply not what this dashboard "
        "scores against.",
    )

    w.add_assertion(
        name="dependent_rows_are_redundant_on_both_sides",
        computed=1.0 if all_dep else 0.0,
        expected=1.0,
        tolerance=0.0,
        source="Indicator (1 = both Delta_pn == Q_beta + m_e and "
               "m_n == m_p + Q_beta + m_e hold, on the prediction side AND "
               "the target side, to the dashboard's serialization "
               "granularity). Residuals are ~1e-10 MeV, i.e. the rounding of "
               "the stored 12-significant-figure strings — not physics.",
    )

    path = w.save(extra={"upstream": _UPSTREAM} if _UPSTREAM else None)
    print(f"\n  Witness: {path}")
    return 0 if all_dep else 1


if __name__ == "__main__":
    raise SystemExit(main())
