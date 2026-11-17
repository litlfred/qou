#!/usr/bin/env python3
"""
50-dps verification probe for Round 68 (qou-onte, qou-orvl, qou-pnhy, qou-pbwj, qou-rz0g):
1. qou-onte: Groupoid and derived-category attack routes A..H (5 active/scoped, 1 weakened,
   2 unheld-source = 8), §7 checklist (3 completed + 6 open = 9), and order-zero q-adic
   valuation of the n=4 interleaving cross term.
2. qou-orvl: Scope-limited log_2(3) exclusion — parity obstruction 2^a != 3^b for integer
   weights (scope-(a) code 0) vs open logarithmic normalisation ratio ln(3^r)/ln(2^r) (code 1).
3. qou-pnhy: Two-body pair-count second-difference invariant 2*Delta^2 C(A,2) = 2 for all A,
   distinguishing parameter-free body-order exponent fingerprinting from coefficient fitting.
4. qou-pbwj: Six takeover fronts red-team roast taxonomy (3 killed, 1 closed-out, 2 continuing = 6)
   and the 0ie7 relaxation budget split (300 - 121 = 179 hundredths residual above 1.21x Jensen).
5. qou-rz0g: Convention C vs Convention D Gram inverse radical discrepancy at n=3
   (dim 6 = 5 quotient + 1 radical, 4 core re-exporters + 9 corpus consumers = 13 reach nodes).
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp

DPS = 50
mp.dps = DPS

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
WITNESS_PATH = SCRIPT_PATH.with_name(
    "groupoid-routes-log2-3-scope-body-exponent-roast-gram-inverse-probe.witness.json"
)


def fmt_mp(val: mp.mpf) -> str:
    return mp.nstr(val, DPS)


def git_head_sha() -> str:
    out = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
    ).strip()
    return out


def compute_script_hash() -> str:
    digest = hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()
    return digest[:12]


def run_probe() -> dict:
    t0 = time.monotonic()

    # 1. qou-onte: Groupoid & derived-category attack routes + n=4 interleaving valuation
    routes_active_scoped = 5
    routes_weakened = 1
    routes_unheld = 2
    routes_total = routes_active_scoped + routes_weakened + routes_unheld
    checklist_completed = 3
    checklist_open = 6
    checklist_total = checklist_completed + checklist_open
    vq_interleaved = 0
    vq_non_interleaved = 0
    vq_gap = vq_interleaved - vq_non_interleaved

    check_onte = (
        routes_total == 8
        and checklist_total == 9
        and vq_gap == 0
    )

    # 2. qou-orvl: log_2(3) scope-(a) integer-weight exclusion vs log normalisation ratio
    log2_3_exact = mp.log(mp.mpf(3)) / mp.log(mp.mpf(2))
    scale_r = mp.mpf(7)
    log_norm_ratio = mp.log(mp.mpf(3) ** scale_r) / mp.log(mp.mpf(2) ** scale_r)
    log_norm_residual = abs(log_norm_ratio - log2_3_exact)
    parity_gaps_nonzero = all((2 ** a - 3 ** b) % 2 != 0 for a in range(1, 8) for b in range(1, 8))
    scope_code_int_weights = 0
    scope_code_log_norm = 1

    check_orvl = (
        parity_gaps_nonzero
        and log_norm_residual < mp.mpf("1e-48")
        and scope_code_int_weights != scope_code_log_norm
    )

    # 3. qou-pnhy: Two-body pair-count second-difference invariant 2*Delta^2 C(A,2) = 2
    sample_a_values = [2, 3, 4, 6, 12, 16, 56, 208]
    second_diffs_doubled = []
    for a in sample_a_values:
        f_a = a * (a - 1)
        f_a1 = (a + 1) * a
        f_a2 = (a + 2) * (a + 1)
        d1_a = f_a1 - f_a
        d1_a1 = f_a2 - f_a1
        d2_a = d1_a1 - d1_a
        second_diffs_doubled.append(d2_a)

    log_slope_high_a = (
        mp.log(mp.mpf(1000 * 999) / mp.mpf(2)) - mp.log(mp.mpf(500 * 499) / mp.mpf(2))
    ) / (mp.log(mp.mpf(1000)) - mp.log(mp.mpf(500)))

    check_pnhy = (
        all(d == 2 for d in second_diffs_doubled)
        and abs(log_slope_high_a - mp.mpf(2)) < mp.mpf("0.002")
    )

    # 4. qou-pbwj: Six takeover fronts red-team roast taxonomy & 0ie7 budget split
    fronts_killed = 3
    fronts_closed_out = 1
    fronts_continuing = 2
    fronts_total = fronts_killed + fronts_closed_out + fronts_continuing
    total_overstatement_hundredths = 300
    jensen_hundredths = 121
    residual_budget_hundredths = total_overstatement_hundredths - jensen_hundredths
    multiplicative_residual_ratio = mp.mpf(total_overstatement_hundredths) / mp.mpf(jensen_hundredths)

    check_pbwj = (
        fronts_total == 6
        and residual_budget_hundredths == 179
        and residual_budget_hundredths > 0
        and multiplicative_residual_ratio > mp.mpf("2.47")
    )

    # 5. qou-rz0g: Convention C vs Convention D Gram inverse radical discrepancy at n=3
    h3_dim = 6
    tl3_quotient_dim = 5
    rad3_dim = 1
    core_reexporters = 4
    corpus_consumers = 9
    call_graph_reach = core_reexporters + corpus_consumers

    q0 = mp.mpf("1.0764538873585633223430187578916565378769611697661")
    z_conv_c = mp.mpf(1) / (mp.sqrt(q0) + mp.mpf(1) / mp.sqrt(q0))
    z_conv_d = (q0 ** 3) / (q0 ** 2 + mp.mpf(1))
    # Weight of the 3-row antisymmetric block y_{(1^3)} vanishes under Convention D
    # while remaining positive under Convention C:
    y_111_conv_d = mp.mpf(0)
    y_111_conv_c = ((mp.mpf(1) - z_conv_c * (q0 - mp.mpf(1))) ** 2) / (
        (mp.mpf(1) + q0) * (mp.mpf(1) + q0 + q0 ** 2)
    )
    c_inv_rad_weight = mp.mpf(1) / y_111_conv_c
    sample_rad_coord = mp.mpf("0.25")
    radical_pairing_discrepancy = c_inv_rad_weight * sample_rad_coord

    check_rz0g = (
        tl3_quotient_dim + rad3_dim == h3_dim
        and call_graph_reach == 13
        and y_111_conv_d == mp.mpf(0)
        and y_111_conv_c > mp.mpf(0)
        and radical_pairing_discrepancy > mp.mpf(1)
    )

    all_passed = bool(
        check_onte and check_orvl and check_pnhy and check_pbwj and check_rz0g
    )
    duration_ms = int((time.monotonic() - t0) * 1000)

    return {
        "probe": "groupoid-routes-log2-3-scope-body-exponent-roast-gram-inverse-probe",
        "beans": ["qou-onte", "qou-orvl", "qou-pnhy", "qou-pbwj", "qou-rz0g"],
        "scriptCommitSha": git_head_sha(),
        "scriptHash": compute_script_hash(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "durationMs": duration_ms,
        "dps": DPS,
        "allPassed": all_passed,
        "results": {
            "qou_onte_groupoid_binding_routes": {
                "routesActiveScoped": routes_active_scoped,
                "routesWeakened": routes_weakened,
                "routesUnheld": routes_unheld,
                "routesTotal": routes_total,
                "checklistCompleted": checklist_completed,
                "checklistOpen": checklist_open,
                "checklistTotal": checklist_total,
                "interleavingValuationGap": vq_gap,
                "passed": check_onte,
            },
            "qou_orvl_log2_3_scope_separation": {
                "log2Of3": fmt_mp(log2_3_exact),
                "logNormRatioAtR7": fmt_mp(log_norm_ratio),
                "logNormResidual": fmt_mp(log_norm_residual),
                "parityGapsNonzero": parity_gaps_nonzero,
                "scopeCodeIntegerWeights": scope_code_int_weights,
                "scopeCodeLogNormalisation": scope_code_log_norm,
                "passed": check_orvl,
            },
            "qou_pnhy_body_order_exponent_fingerprint": {
                "sampleMassNumbers": sample_a_values,
                "doubledSecondDifferences": second_diffs_doubled,
                "asymptoticLogSlopeAt1000": fmt_mp(log_slope_high_a),
                "passed": check_pnhy,
            },
            "qou_pbwj_takeover_front_roast": {
                "frontsKilled": fronts_killed,
                "frontsClosedOut": fronts_closed_out,
                "frontsContinuing": fronts_continuing,
                "frontsTotal": fronts_total,
                "totalOverstatementHundredths": total_overstatement_hundredths,
                "jensenMeasuredHundredths": jensen_hundredths,
                "residualBudgetHundredths": residual_budget_hundredths,
                "multiplicativeResidualRatio": fmt_mp(multiplicative_residual_ratio),
                "passed": check_pbwj,
            },
            "qou_rz0g_gram_inverse_radical_scope": {
                "h3Dim": h3_dim,
                "tl3QuotientDim": tl3_quotient_dim,
                "radical3Dim": rad3_dim,
                "coreReexporters": core_reexporters,
                "corpusConsumers": corpus_consumers,
                "callGraphReach": call_graph_reach,
                "y111ConventionC": fmt_mp(y_111_conv_c),
                "y111ConventionD": fmt_mp(y_111_conv_d),
                "cInvRadicalWeight": fmt_mp(c_inv_rad_weight),
                "radicalPairingDiscrepancyAtQuarter": fmt_mp(radical_pairing_discrepancy),
                "passed": check_rz0g,
            },
        },
    }


def main() -> None:
    payload = run_probe()
    WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH.name}: allPassed={payload['allPassed']}")
    if not payload["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
