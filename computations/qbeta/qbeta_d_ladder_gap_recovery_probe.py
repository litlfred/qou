#!/usr/bin/env python3
"""How much of the convention-D Q_beta gap do the DERIVED D-frame rungs recover?

Bean qou-cds1 (epic qou-wxhi), issue #7939. Owner task 2026-11-16: "build the
c_k ladder under convention D; derive the rungs, do not fit them; report how
much of the gap they recover."

WHAT IS DERIVED UNDER D, AND NOTHING ELSE IS USED
  * The N=2 rung c_2 = -1 with b^2 = [3]_q/[2]_q^2, forced by the D weights
    (qbeta_d_frame_c2_invariant_probe.py, exact over Q(q)). Its factor is
    1 - u^2 with u = b*hbar_q^2. Assertion 1 re-checks b^2 = [3]/[2]^2 against
    the Hoefsmit b used by the production ladder.
  * No other rung is derived in either convention: c_3 is a near-match,
    c_k (k >= 4) were calibrated against CODATA, and the N=1 phase alpha is
    asserted in both frames (bean qou-pdix). They are NOT applied here.

CELLS. The scored base (gamma-gamma V^3, two-term trace, read from the
dashboard) plus every historical convention-D census cell, at the proton pin:
tr^{z_D} of the four census elements is READ from
qbeta-option-e-required-level.witness.json (the dashboard's source), times
E_0 in both forms from qbeta_e0 (tower-summed = canonical, order-zero).

WHAT IS MEASURED
  * F_req = Q_codata / Q_base per cell, and ln F_req.
  * recovery = ln(1 - u^2) / ln F_req: the share of the log-gap the derived
    rung closes. It is NEGATIVE: the rung is below 1, the gap needs above 1.
  * C_min = (1 - 1/F)(1 - u)/u^2, the smallest uniform |c_k| bound that could
    reach F at all (Weierstrass bound, QOU.QBeta.LadderUniformBound, sorry-free).

WHAT IS NOT CLAIMED. No rung is fitted, no cell is selected, nothing is
re-scored. That the residual is a base/assembly problem rather than a rung
problem is already the corpus's position (qbeta_ladder_uniform_coefficient_
bound_probe.py, docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-
state.md). This probe adds the per-cell recovery of the one derived D rung,
and covers both E_0 forms for all four census elements.

PRECISION. mpmath at 60 dps end to end; no float anywhere.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from mpmath import mp, mpf, log, sqrt

mp.dps = 60

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate"),
                str(HERE.parents[1] / "tools" / "qou-substrate" / "python")]

from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from qbeta_e0 import canonical as e0_tower, order_zero as e0_order_zero  # noqa: E402

CENSUS = HERE / "qbeta-option-e-required-level.witness.json"
DASHBOARD = HERE.parent / "per-observable-100x-status.witness.json"
GG_SEGMENT = HERE.parent / "probes" / "gg_gluon_segment" / "gg-gluon-segment.witness.json"


def fmt(x, n=30):
    return mp.nstr(x, n)


def main() -> int:
    q = mpf(q_at(mp.dps))
    hbar = (q - 1) / q
    two = q + 1 / q            # [2]_q, symmetric
    three = q**2 + 1 + q**-2   # [3]_q
    b_hoef = sqrt(1 - q**2 / (q**2 + 1)**2)
    b_sq_forced = three / two**2
    u = b_hoef * hbar**2
    n2 = 1 - u**2
    G = u**2 / (1 - u)
    qc = mpf(Q_BETA_MEV)
    me = mpf(M_E_MEV)

    census = json.loads(CENSUS.read_text())
    per = census["data"]["per_candidate"]
    e0s = {"tower": e0_tower(q=q, m_e=me), "order_zero": e0_order_zero(q=q, m_e=me)}

    cells, checks = {}, []
    for elem, rec in per.items():
        tr = mpf(str(rec["tr_conv_D"]))
        for form, e0 in e0s.items():
            qb = abs(tr) * e0
            F = qc / qb
            lnF = log(F)
            cells[f"{elem}|{form}"] = {
                "tr_zD": fmt(tr), "E0_form": form, "Q_base_MeV": fmt(qb),
                "Q_base_err_pct": fmt((qb / qc - 1) * 100, 12),
                "F_required": fmt(F), "ln_F_required": fmt(lnF),
                "derived_rung_factor": fmt(n2),
                "recovery_pct_of_log_gap": fmt(log(n2) / lnF * 100, 12),
                "Q_after_derived_rung_err_pct": fmt((qb * n2 / qc - 1) * 100, 12),
                "C_min_uniform": fmt((1 - 1 / F) / G, 12),
            }

    # The currently scored base (owner 2026-11-20/21): gamma-gamma V^3 with the
    # photon 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1, scored on the TWO-TERM
    # Lagrangian trace (covariant all-pairs; its connected matter term is 0 on V^3).
    # CONDITIONAL on conjectures C1-C3. Read from the dashboard, not recomputed.
    dash = json.loads(DASHBOARD.read_text())
    rows = dash["data"]["rows"] if "data" in dash else dash["rows"]
    qrow = next(r for r in rows if r.get("obs") == "Q_beta")
    qb = mpf(qrow["two_term_qed_diagnostics"]["pred_two_term_scored_MeV"])
    assert qrow["scored_form"].startswith("two_term"), qrow["scored_form"]
    F = qc / qb
    cells["V3_gamma_gamma|two-term scored (conditional on C1-C3)"] = {
        "Q_base_MeV": fmt(qb), "Q_base_err_pct": fmt((qb / qc - 1) * 100, 12),
        "F_required": fmt(F), "ln_F_required": fmt(log(F)),
        "derived_rung_factor": fmt(n2),
        "recovery_pct_of_log_gap": fmt(log(n2) / log(F) * 100, 12),
        "Q_after_derived_rung_err_pct": fmt((qb * n2 / qc - 1) * 100, 12),
        "C_min_uniform": fmt((1 - 1 / F) / G, 12),
        "source": "per-observable-100x-status.witness.json Q_beta two_term_qed_diagnostics.pred_two_term_scored_MeV",
    }

    live = cells["nuc11_interleaved|tower"]
    checks.append(("b^2 = [3]_q/[2]_q^2 equals the Hoefsmit b^2 (D-forced)",
                   abs(b_hoef**2 - b_sq_forced) < mpf(10)**-50))
    # Calibration: the base is a recorded corpus number. F itself moved when
    # Q_beta switched to the CODATA-2022 registry (owner ruling 2026-11-20),
    # so F is not pinned here; the base is.
    gg = json.loads(GG_SEGMENT.read_text())
    recorded_base = mpf(gg["reference_nuc11_interleaved"]["Q_beta_MeV"])
    checks.append((f"nuc11_interleaved|tower base reproduces the recorded {recorded_base} MeV",
                   abs(mpf(live["Q_base_MeV"]) - recorded_base) < mpf(10)**-10))
    checks.append(("every D cell needs F > 1",
                   all(mpf(c["F_required"]) > 1 for c in cells.values())))
    checks.append(("the derived rung moves every cell AWAY (recovery < 0)",
                   all(mpf(c["recovery_pct_of_log_gap"]) < 0 for c in cells.values())))
    checks.append(("|recovery| < 0.1 % on every cell",
                   all(abs(mpf(c["recovery_pct_of_log_gap"])) < mpf("0.1")
                       for c in cells.values())))
    checks.append(("live C_min reproduces the uniform-bound probe (2279.45)",
                   abs(mpf(live["C_min_uniform"]) - mpf("2279.45")) < mpf("0.01")))

    print(f"u = {fmt(u, 15)}   derived N=2 factor 1 - u^2 = {fmt(n2, 15)}")
    print(f"{'cell':52s} {'F_req':>12s} {'recovery %':>12s} {'C_min':>10s}")
    for k, c in cells.items():
        print(f"{k:52s} {mp.nstr(mpf(c['F_required']), 8):>12s} "
              f"{mp.nstr(mpf(c['recovery_pct_of_log_gap']), 5):>12s} "
              f"{mp.nstr(mpf(c['C_min_uniform']), 6):>10s}")
    failures = [n for n, ok in checks if not ok]
    for n, ok in checks:
        print(("PASS " if ok else "FAIL ") + n)

    wb = WitnessBuilder("qbeta-d-ladder-gap-recovery")
    wb.set_description(
        "Convention-D Q_beta ladder: the only derived D rung (c_2 = -1, "
        "b^2 = [3]_q/[2]_q^2) gives 1 - u^2 = 0.99992746 and recovers between "
        "-0.008 % and -0.05 % of the log-gap on every D cell, including the scored "
        "gamma-gamma V^3 base (wrong direction); a ladder closing the gap would need "
        "uniform |c_k| >= 1997..7982. "
        "No rung fitted, no cell selected, nothing re-scored. Bean qou-cds1.")
    wb.add_data("substrate", {"q0": fmt(q), "u": fmt(u), "b_sq": fmt(b_hoef**2),
                              "b_sq_forced_3_over_2sq": fmt(b_sq_forced),
                              "derived_rung_factor_N2": fmt(n2),
                              "geometric_total_G": fmt(G),
                              "Q_beta_codata_MeV": fmt(qc)})
    wb.add_data("cells", cells)
    wb.add_data("not_applied", {
        "c_3": "near-match (-2 = J_Hopf(q=1)), not derived",
        "c_k_k_ge_4": "calibrated against CODATA (fit), not derived",
        "N1_phase_alpha": "asserted in both frames, derived in neither (qou-pdix)"})
    wb.add_data("verdict", (
        "The derived convention-D rungs recover none of the 12-43 % Q_beta gap; "
        "the one forced rung moves every cell away by ~72.5 ppm. Any ladder that "
        "closed it would need coefficients ~1000x the largest the corpus records, "
        "i.e. a non-perturbative object whose value is set by an unfixed pole -- a "
        "fit. Scope (a). The gap lives in the base (element qou-99qc / meaning of "
        "epsilon), not the ladder."))
    for i, (n, ok) in enumerate(checks, 1):
        wb.add_assertion(f"{i}. {n}", "PASS" if ok else "FAIL", "PASS")
    out = wb.save(extra={"q0Anchor": "proton",
                         "q0AnchorReason": "proton pin q_at; census traces are proton-pinned"})
    print(f"Witness: {out}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
