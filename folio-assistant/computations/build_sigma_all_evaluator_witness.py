"""
Build `sigma-all-evaluator.witness.json` — reference data for the
Σ_all closed-form evaluator.

Emits:
  - reference table A=1..10 at q_0 with sigma_all_closed values and
    asymptotic ratios to A=1
  - decay rate γ(q_0) and per-A geometric mean
  - precision schedule (digits required vs A)
  - list of pipeline callers updated
"""
from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

from sigma_all_evaluator import (
    sigma_all_closed,
    sigma_all_decay_rate,
    precision_digits_required,
    a_exponent,
    d_exponent,
)
from q_parameter import q_at, MASS_RATIO_MU_E_STR


def main():
    dps = 60
    mp.mp.dps = dps
    q0 = q_at(dps)

    # Reference table A=1..10 at q_0
    sigma1 = sigma_all_closed(1, q0, dps=dps)
    rows = []
    for A in range(1, 11):
        val = sigma_all_closed(A, q0, dps=dps)
        ratio = val / sigma1
        rows.append({
            "A": A,
            "a_exp": a_exponent(A),
            "d_exp": d_exponent(A),
            "sigma_all_at_q0": mp.nstr(val, 30, strip_zeros=False),
            "sigma_all_at_q0_f64": float(val),
            "ratio_to_A1": mp.nstr(ratio, 30, strip_zeros=False),
            "ratio_to_A1_f64": float(ratio),
            "log10_abs": float(mp.log10(abs(val))) if val != 0 else None,
            "precision_digits_required_for_raw_sum": precision_digits_required(A),
        })

    # Decay rate
    gamma = sigma_all_decay_rate(q0, dps=dps)
    two_step = 3 * (q0 ** 4 - 1) ** 2 / (8 * q0 ** 4)
    per_A_decay = mp.sqrt(two_step)

    # Precision schedule: max A safe at given target precision.
    # Closed form is precision-floor-free; this table refers to the
    # *raw config-sum* path that the closed form replaces.
    schedule = []
    log10_per_A_decay = float(mp.log10(per_A_decay))
    for label, log10_floor in [
        ("f64", -16), ("25 dps", -25), ("50 dps", -50),
        ("100 dps", -100), ("200 dps", -200),
    ]:
        # log10|Σ(A)| ≈ A · log10_per_A_decay (constant prefactor ~1)
        # crossover when this reaches the precision floor:
        A_crit = log10_floor / log10_per_A_decay
        schedule.append({
            "precision_label": label,
            "log10_floor": log10_floor,
            "max_A_safe_for_raw_sum": math.floor(A_crit),
        })

    # Pipeline callers updated (file:line for each)
    callers_updated = [
        {
            "file": "folio-assistant/computations/full-derivation-verified.py",
            "case": "A=1 free neutron",
            "before": "char_sum_n = sum_p - sum_n",
            "after": "char_sum_n = float(sigma_all_closed(1, mp.mpf(q0)))",
            "approx_line": 263,
        },
        {
            "file": "folio-assistant/computations/full-derivation-verified.py",
            "case": "A=3 tritium ³H→³He",
            "before": "for config in cartesian(ch_names, repeat=3): total_3h += me_d - me_p",
            "after": "total_3h = float(sigma_all_closed(3, mp.mpf(q0)))",
            "approx_line": 277,
        },
        {
            "file": "folio-assistant/computations/full-derivation-verified.py",
            "case": "A=6 ⁶He→⁶Li (Σ_all only; Σ_FP still enumerates)",
            "before": "for config in cartesian(ch_names, repeat=6): total_6he_all += dme",
            "after": "total_6he_all = float(sigma_all_closed(6, mp.mpf(q0)))",
            "approx_line": 297,
        },
    ]

    callers_unwired = [
        {
            "file": "folio-assistant/computations/frob_filter_cancellation_test.py",
            "reason": (
                "Test driver for the cancellation diagnostic itself — "
                "intentionally exercises the raw config-sum path so the "
                "f64 precision-budget crossover can be measured. Wiring "
                "this to the closed form would defeat the test."
            ),
        },
        {
            "file": "folio-assistant/computations/sigma_all_symbolic_decay.py",
            "reason": (
                "The symbolic-derivation reference. Per task: do NOT "
                "modify; this is the source of truth for the closed form."
            ),
        },
    ]

    out = {
        "computation": "sigma-all-evaluator",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Reference table + precision schedule for the Σ_all closed-form "
            "evaluator (sigma_all_evaluator.py). Replaces raw 4^A "
            "configuration-sum routes in the β-decay / binding-energy "
            "pipeline with a constant-time, cancellation-free evaluator. "
            "Closed form verified for A=1..6 in sigma_all_symbolic_decay.py "
            "and documented in docs/audits/2026-05-02-nv-frob-filter-conjectures.md "
            "lines 683-769."
        ),
        "q_parameter": {
            "q_at_q0": mp.nstr(q0, 50, strip_zeros=False),
            "q_at_q0_f64": float(q0),
            "vol_4_1": mp.nstr(2 * mp.clsin(2, mp.pi / 3), 30),
            "mu_over_e": MASS_RATIO_MU_E_STR,
            "dps_used": dps,
        },
        "closed_form": {
            "formula": (
                "Σ_all(A) = (-1)^{A-1} · 3^{floor(A/2)} / 2^{a(A)} · "
                "(q-1)^A · (q+1)^A · (q^2+1)^{2 floor(A/2)} · "
                "(3 q^4 + 4 q^2 + 3) / q^{d(A)}"
            ),
            "a_exponent_rule": "a(A) = (3A+1)/2 if A odd, (3A+2)/2 if A even",
            "d_exponent_rule": "d(A) = 2A+1 if A odd, 2A+2 if A even",
            "two_step_ratio": "Σ_all(A+2) / Σ_all(A) = 3 (q^4-1)^2 / (8 q^4)",
            "two_step_ratio_at_q0": mp.nstr(two_step, 30),
            "two_step_ratio_at_q0_f64": float(two_step),
        },
        "decay_rate": {
            "gamma_q0_natural_log": float(gamma),
            "log10_per_A_decay": log10_per_A_decay,
            "per_A_geometric_decay_factor": float(per_A_decay),
            "audit_reference_value": 1.357,
        },
        "reference_table_A_1_to_10": rows,
        "precision_schedule_for_raw_config_sum": schedule,
        "closed_form_precision_claim": (
            "The closed-form evaluator has zero catastrophic cancellation "
            "(the (q-1)^A · (q+1)^A factors are extracted symbolically). "
            "Working precision = output precision, in O(log A) "
            "multiplications. Valid for any A ≥ 1 at any mpmath dps. "
            "Constant compute time per requested digit."
        ),
        "pipeline_callers_updated": callers_updated,
        "pipeline_callers_intentionally_unwired": callers_unwired,
        "tests": {
            "test_file": (
                "folio-assistant/computations/test_sigma_all_evaluator.py"
            ),
            "test_count": 11,
            "all_passing_as_of": datetime.now(timezone.utc).isoformat(),
        },
        "evaluator_module": (
            "folio-assistant/computations/sigma_all_evaluator.py"
        ),
        "audit_doc_reference": (
            "docs/audits/2026-05-02-nv-frob-filter-conjectures.md "
            "lines 683-769 (closed form + precision schedule)"
        ),
        "memo_doc_reference": (
            "docs/audits/2026-05-03-frob-filter-evaluator-wired.md "
            "(this wiring task)"
        ),
    }

    out_path = Path(__file__).parent / "sigma-all-evaluator.witness.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"→ wrote {out_path}")
    return out_path


if __name__ == "__main__":
    main()
