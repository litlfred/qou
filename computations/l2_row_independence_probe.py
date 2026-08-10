#!/usr/bin/env python3
"""l2_row_independence_probe — how many INDEPENDENT failures does L2 list?

## The question

The per-observable 100x dashboard reports 7 observables. Read as a scoreboard,
its fail list says "several separate things are broken", and therefore
"several separate places to look for a fix". It does not.

The distinction that matters is **which side** of each comparison is
redundant — the framework's prediction, or the experimental target. They are
answered separately here, because the answers differ and only one of them
bears on where the physics work is.

## Side 1 — the PREDICTIONS are exactly redundant (this is the load-bearing one)

    Delta_pn_pred  ==  Q_beta_pred + m_e
    m_n_pred       ==  m_p_pred + Q_beta_pred + m_e

Both hold to ~1e-11 MeV, i.e. exactly, by construction of Path C. So the
framework contributes **nothing** to m_n and Delta_pn beyond what it already
contributes to m_p and Q_beta. Combined with m_p being a pin-anchor
round-trip (see codata_registry_triangulation_probe), the framework has
exactly **two** independent quantities on the fail list: **Q_beta and m_mu**.

That is the number that governs planning: two levers, not five fronts.

## Side 2 — the TARGETS are no longer redundant (changed 2026-08-09)

Before the CODATA vintage fix, the neutron target was
`M_N_MEV_AME_DERIVED`, *constructed* as `M_P + M_E + Q_BETA` — so the target
side was redundant too, and the m_n row tested literally nothing new. The fix
repointed it at `M_N_MEV_CODATA_DIRECT`, an independent CODATA determination.

The target-side residual is now ~1.5e-7 MeV rather than ~0, so m_n and
Delta_pn now do carry a small amount of genuinely independent experimental
information (~0.16 ppb on the neutron). This is a real improvement in the
dashboard's information content, and it is *why* the two sides are reported
separately rather than collapsed into one verdict.

**It does not change the planning conclusion.** Independent *targets* do not
create independent *framework levers*: a better measurement to compare
against still compares against the same two predicted quantities.

AUDIT-ONLY. Re-scores nothing.

Refs:
- computations/codata_registry_triangulation_probe.py  (companion guard)
- docs/audits/2026-08-09-codata-registry-vintage-straddle.md
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

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

#: The dashboard serializes pred_MeV / codata_MeV to ~12 significant figures,
#: so an exact identity appears as a residual at that granularity (~1e-9 MeV
#: on a ~1e3 MeV quantity), not as a bitwise zero. Score against that.
SER_TOL_MEV = mpf("1e-8")


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

    checks = [
        ("Delta_pn == Q_beta + m_e",
         pred("Delta_pn") - (pred("Q_beta") + m_e),
         targ("Delta_pn") - (targ("Q_beta") + m_e)),
        ("m_n == m_p + Q_beta + m_e",
         pred("m_n") - (pred("m_p") + pred("Q_beta") + m_e),
         targ("m_n") - (targ("m_p") + targ("Q_beta") + m_e)),
    ]

    print("=" * 78)
    print("  L2 row independence — how many INDEPENDENT levers does the list have?")
    print("=" * 78)
    print(f"\n  compute dps = {COMPUTE_DPS}")
    print(f"  identity tolerance = {n(SER_TOL_MEV)} MeV"
          f"  (the dashboard's own ~12-sig-fig serialization)\n")

    print("  SCORED ROWS (as published):")
    for o in ("m_p", "m_mu", "Q_beta", "m_n", "Delta_pn"):
        r = rows[o]
        print(f"    {o:9s} err {r['err_ppb']:>9s} ppb   miss {r['miss_factor']:>22s}")

    preds_redundant = True
    targets_redundant = True
    print("\n  SIDE 1 — PREDICTIONS (the load-bearing check):")
    for label, dp, _ in checks:
        ok = abs(dp) < SER_TOL_MEV
        preds_redundant &= ok
        print(f"    {label:32s} residual {n(dp, 4):>10s} MeV"
              f"  -> {'REDUNDANT' if ok else 'independent'}")

    print("\n  SIDE 2 — TARGETS (repointed by the 2026-08-09 CODATA fix):")
    for label, _, dt in checks:
        ok = abs(dt) < SER_TOL_MEV
        targets_redundant &= ok
        print(f"    {label:32s} residual {n(dt, 4):>10s} MeV"
              f"  -> {'REDUNDANT' if ok else 'independent'}")
    if not targets_redundant:
        print("    the neutron target is now M_N_MEV_CODATA_DIRECT (an independent")
        print("    CODATA determination), not the constructed M_P + M_E + Q_BETA.")
        print("    Pre-fix both sides were redundant and the m_n row tested nothing new.")

    print("\n  CONCLUSION — framework levers on the fail list:")
    print("    m_p       anchor round-trip, reported but NOT scored")
    print("    m_n       prediction adds nothing beyond {m_p, Q_beta}")
    print("    Delta_pn  prediction adds nothing beyond {Q_beta}")
    print("    Q_beta    INDEPENDENT LEVER  (Habiro closure, bean kehn)")
    print("    m_mu      INDEPENDENT LEVER  (mu-p substrate tension)")
    print("\n    => TWO independent levers, not five fronts.")
    print("       (Targets being partly independent does not create a third")
    print("        lever — it improves what the same two are measured against.)")

    w = WitnessBuilder("l2-row-independence", engine="mpmath")
    w.set_description(
        "Separates prediction-side from target-side redundancy on the L2 "
        "dashboard. The PREDICTIONS for m_n and Delta_pn are exactly "
        "Q_beta/m_p plus m_e, so the framework has only two independent "
        "quantities on the fail list (Q_beta, m_mu) once m_p is recognised as "
        "an unscored anchor round-trip. The TARGETS stopped being redundant on "
        "2026-08-09 when the CODATA vintage fix repointed the neutron at the "
        "independent direct determination — a gain in the dashboard's "
        "information content that does not add a third lever. Audit-only."
    )
    w.set_audit_only("docs/audits/2026-08-09-codata-registry-vintage-straddle.md")
    w.add_parameter("compute_dps", COMPUTE_DPS)
    w.add_parameter("identity_tolerance_MeV", str(SER_TOL_MEV))

    for label, dp, dt in checks:
        key = label.split(" ==")[0].strip()
        w.add_data(f"residual_pred_{key}_MeV", n(dp, 6))
        w.add_data(f"residual_target_{key}_MeV", n(dt, 6))
    w.add_data("predictions_redundant", bool(preds_redundant))
    w.add_data("targets_redundant", bool(targets_redundant))
    w.add_data("independent_framework_levers", ["Q_beta", "m_mu"])
    w.add_data("prediction_redundant_rows", ["m_n", "Delta_pn"])
    w.add_data("anchor_roundtrip_rows", ["m_p"])
    w.add_data(
        "caveat",
        "Prediction-redundant does not mean wrong to publish — m_n in MeV is a "
        "useful number. It means the row is not an independent test OF THE "
        "FRAMEWORK, so L2 planning must not count it as a separate front.",
    )
    w.add_data(
        "target_side_change_2026_08_09",
        "Pre-fix the neutron target was M_N_MEV_AME_DERIVED, constructed as "
        "M_P + M_E + Q_BETA, so the target side was redundant too and the m_n "
        "row tested nothing new. It now points at M_N_MEV_CODATA_DIRECT, so "
        "~0.16 ppb of independent experimental information enters.",
    )

    w.add_assertion(
        name="predictions_for_m_n_and_delta_pn_add_no_framework_content",
        computed=1 if preds_redundant else 0,
        expected=1,
        source="Indicator (1 = both Delta_pn == Q_beta + m_e and m_n == m_p + "
               "Q_beta + m_e hold on the PREDICTION side to the dashboard's "
               "serialization granularity). Residuals are ~1e-11 MeV. This is "
               "the load-bearing claim: the framework has two independent "
               "quantities on the fail list, not five.",
    )
    w.add_assertion(
        name="targets_are_no_longer_redundant_after_the_codata_fix",
        computed=1 if not targets_redundant else 0,
        expected=1,
        source="Indicator (1 = the TARGET side is no longer an exact identity). "
               "Pre-fix it was, because the neutron target was constructed from "
               "the proton and Q_beta. Repointing it at the independent CODATA "
               "direct determination is a gain in information content — "
               "asserted so a regression back to the constructed target would "
               "fail here rather than pass silently.",
    )

    path = w.save(extra={"upstream": _UPSTREAM} if _UPSTREAM else None)
    print(f"\n  Witness: {path}")
    ok = preds_redundant and not targets_redundant
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
