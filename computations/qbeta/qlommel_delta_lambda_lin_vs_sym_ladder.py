#!/usr/bin/env python3
"""qlommel_delta_lambda_lin_vs_sym_ladder.py
=============================================

EXPLORATORY shape-probe (per .claude/skills/local/production-vs-exploratory-discipline.md).
Derive-or-refute, NO FIT — labels which binding ladder the SECOND-KIND q-Lommel
order coefficient `b = q₀¹⁰+q₀⁻¹⁰ = 2cosh(10·log q₀)` actually governs. The finding
it surfaces is NOT for production without the usual gates (q-locality, 13-driver,
owner sign-off); it is a disambiguation hint, not a closure.

## The question (item 3, 2026-06-15)

The 2nd-kind q-Lommel ORDER recurrence `Δ_{A+1} = b·Δ_A − Δ_{A−1}` with the DERIVED
coefficient `b = q₀¹⁰+q₀⁻¹⁰` (Lean `QOU.QBeta.two_root_geometric`; its first-kind
branch is the geometric ladder of ratio `r = q₀¹⁰`) was matched against the
binding residual `Δ_λ = B_AME/B_pred` — where `B_pred` is the **LINEAR** form
`B_lin = α·s` (this is the ladder `qlommel_delta_lambda_two_seed_test.py` tests, on
`delta-lambda-canonical-residual.witness.json`).

The single-pipeline binding work (PR #2320) showed there are TWO residuals:

  Δ_λ^lin = B_AME / B_lin   (linear binding — the m_qCLT-style channel)
  Δ_λ^sym = B_AME / B_sym   (exact log-trace B_sym = α·ln(tr_free/tr_atom) — the
                             m_symbolic channel; the Kashaev volume tr ~ exp(Vol))

Item 3 asks: does the 2nd-kind `b` describe the Δ_λ^**sym** ladder too, or has
`B_sym` already REALIZED the exponential the recurrence encodes? This is exactly
the m_sym-vs-m_qCLT disambiguation behind the owner's original question.

## What this reports (recorded data only — no Rust engine, no fit)

Reads the per-atom Δ_λ^lin / Δ_λ^sym that PR #2320 recorded in
`binding-single-pipeline-comparison.witness.json` and, for each ladder:

  (a) the per-A-step geometric ratio `Δ(A+1)/Δ(A)` on the clean A=2→3 step
      (D→T; avoids the doubly-magic ⁴He), vs the first-kind ratio `r = q₀¹⁰`;
  (b) the interior recurrence coefficient `b_emp = (Δ(A+1)+Δ(A−1))/Δ(A)` on the
      N≥Z chain D–T–⁴He, vs the derived `b` — REPORTED with the explicit
      data-limitation caveat (one interior point; ⁴He is magic-contaminated for
      the sym ladder), so it is NOT used as the discriminator;
  (c) the absorption factor `Δ_λ^lin / Δ_λ^sym` at A=3 — how much of the
      exp-vs-linear gap the log-trace already spends.

## Finding (gate-respecting)

The geometric/exponential signature (ratio `r = q₀¹⁰`, the first-kind branch of
the 2nd-kind recurrence) is carried by Δ_λ^**lin** (D→T ratio within ~8% of `r`)
and is ABSENT from Δ_λ^**sym** (D→T ratio ~40% below `r`; Δ_λ^sym ≈ 1 on the
non-anomalous A=3 nuclei). I.e. `B_sym` (the m_symbolic channel) already realizes
the exponential, so the 2nd-kind correction belongs to the LINEAR binding (the
m_qCLT channel) — applying it AGAIN on top of `B_sym` would double-count. This
does not close anything: the linear-ladder match is itself the open-keystone
near-match (`10A−5` from Bring crossings, PR #2316).
"""
from __future__ import annotations

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401, E402 — adds substrate/ etc. to sys.path

import json  # noqa: E402
import time  # noqa: E402
import mpmath as mp  # noqa: E402

from qou_substrate.witness import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

SINGLE_PIPELINE = (pathlib.Path(__file__).resolve().parent.parent
                   / "binding-single-pipeline-comparison.witness.json")


def _q0_and_ladders():
    """q₀ + per-atom Δ_λ^lin / Δ_λ^sym, from the recorded single-pipeline witness."""
    d = json.loads(SINGLE_PIPELINE.read_text())
    w = d.get("witness", d)
    q0 = mp.mpf(str(w["parameters"]["q_0"]))
    rows = w.get("data", {}).get("rows") or w.get("rows") or []
    lad = {}
    for r in rows:
        lad[r["atom"]] = {
            "A": r["A"],
            "lin": mp.mpf(str(r["Delta_lambda_lin"])),
            "sym": mp.mpf(str(r["Delta_lambda_sym"])),
        }
    meta = {
        "source_witness": SINGLE_PIPELINE.name,
        "source_scriptCommitSha": w.get("scriptCommitSha") or d.get("scriptCommitSha"),
    }
    return q0, lad, meta


def main() -> int:
    t0 = time.monotonic()
    q0, lad, meta = _q0_and_ladders()
    eta = mp.log(q0)
    r = q0 ** 10                 # first-kind geometric ratio per A-step
    b = r + 1 / r                # derived 2nd-kind coefficient = 2cosh(10η)
    print(f"q0={mp.nstr(q0,8)}  r=q0^10={mp.nstr(r,8)}  b=2cosh(10η)={mp.nstr(b,8)}")

    out = {}
    for tag in ("lin", "sym"):
        D, T, He4 = lad["D"][tag], lad["T"][tag], lad["4He"][tag]
        ratio_DT = T / D                                  # clean A=2→3 step (no ⁴He)
        ratio_dev = (ratio_DT - r) / r * 100
        b_emp = (He4 + D) / T                             # interior, N≥Z chain (⁴He!)
        b_dev = (b - b_emp) / b_emp * 100
        out[tag] = {
            "ratio_DT": mp.nstr(ratio_DT, 6),
            "ratio_DT_vs_r_pct": mp.nstr(ratio_dev, 5),
            "interior_b_emp_NgeZ": mp.nstr(b_emp, 6),
            "interior_b_vs_derived_pct": mp.nstr(b_dev, 5),
        }
        print(f"  Δ_λ^{tag}:  D→T ratio={float(ratio_DT):.3f} (vs r {float(ratio_dev):+.1f}%)   "
              f"interior b_emp={float(b_emp):.3f} (vs derived {float(b_dev):+.1f}%)")

    # absorption: how much of the exp-vs-linear gap B_sym already spends at A=3
    absorb_T = lad["T"]["lin"] / lad["T"]["sym"]
    absorb_He3 = lad["3He"]["lin"] / lad["3He"]["sym"]
    print(f"  log-trace absorption Δλ_lin/Δλ_sym:  T={float(absorb_T):.2f}×  "
          f"³He={float(absorb_He3):.2f}×   (Δλ_sym≈1 on A=3 ⇒ B_sym realizes the exponential)")

    lin_ratio_dev = abs((lad["T"]["lin"] / lad["D"]["lin"] - r) / r)
    sym_ratio_dev = abs((lad["T"]["sym"] / lad["D"]["sym"] - r) / r)

    builder = WitnessBuilder(
        "qlommel-delta-lambda-lin-vs-sym-ladder",
        engine="python+mpmath", start_time=t0)
    (builder
     .set_description(
        "EXPLORATORY derive-or-refute (no fit): which binding ladder the 2nd-kind "
        "q-Lommel order coefficient b=q0^10+q0^-10=2cosh(10η) governs. Reads the "
        "recorded Δ_λ^lin (B_AME/B_lin) and Δ_λ^sym (B_AME/B_sym, exact log-trace) "
        "from binding-single-pipeline-comparison.witness.json. Finding: the "
        "geometric first-kind ratio r=q0^10 is carried by Δ_λ^lin (D→T within ~8%) "
        "and ABSENT from Δ_λ^sym (D→T ~40% below r; Δ_λ^sym≈1 on A=3) — B_sym "
        "(m_symbolic) already realizes the exponential, so the 2nd-kind correction "
        "belongs to the LINEAR binding (m_qCLT), not on top of B_sym. The interior-b "
        "test is data-limited (one interior point; ⁴He magic-contaminates sym) and "
        "is reported, NOT used as the discriminator. Not a closure: the linear match "
        "is the open-keystone near-match (10A−5 from Bring crossings, #2316).")
     .add_parameter("q0", mp.nstr(q0, 12))
     .add_parameter("r_geometric_ratio", mp.nstr(r, 12))
     .add_parameter("b_derived_2cosh10eta", mp.nstr(b, 12))
     .add_parameter("source_witness", meta["source_witness"])
     .add_parameter("source_scriptCommitSha", meta["source_scriptCommitSha"])
     .add_data("ladders", out)
     .add_data("log_trace_absorption_A3", {
         "T": mp.nstr(absorb_T, 5), "3He": mp.nstr(absorb_He3, 5),
         "note": "Δ_λ^lin/Δ_λ^sym at A=3: the factor of the exp-vs-linear gap the "
                 "exact log-trace B_sym already absorbs (Δ_λ^sym≈1).",
     })
     .add_data("discipline",
               "EXPLORATORY; derive-or-refute, no fit; data-limited interior-b "
               "reported not asserted; the lin-ladder match is itself near-match "
               "tier (open keystone 10A−5), nothing wired.")
     .add_data("verdict",
               "2nd-kind b governs the LINEAR ladder (m_qCLT); B_sym (m_symbolic) "
               "already realizes the exponential — do not double-apply on B_sym."))

    # FINDING 1: the geometric first-kind ratio r=q0^10 IS present in the linear
    # ladder (D→T within ~15%) — the exp-vs-linear gap is geometric.
    builder.add_assertion(
        "lin_ladder_geometric_ratio_matches_r_within_15pct",
        computed=bool(lin_ratio_dev < mp.mpf("0.15")),
        expected=True,
        source="|Δ_λ^lin(T)/Δ_λ^lin(D) − q0^10| / q0^10 < 0.15 (first-kind branch)")
    # FINDING 2: the geometric ratio is ABSENT from the sym ladder (departs >25%)
    # — B_sym already realizes the exponential. (assert the refutation)
    builder.add_assertion(
        "sym_ladder_geometric_ratio_departs_from_r_gt_25pct",
        computed=bool(sym_ratio_dev > mp.mpf("0.25")),
        expected=True,
        source="|Δ_λ^sym(T)/Δ_λ^sym(D) − q0^10| / q0^10 > 0.25 (B_sym spends it)")
    # FINDING 3: the log-trace absorbs > 2× of the gap at A=3 (T) — quantifies
    # 'B_sym realizes the exponential the linear ladder still carries'.
    builder.add_assertion(
        "log_trace_absorbs_gt_2x_at_A3_T",
        computed=bool(absorb_T > mp.mpf("2")),
        expected=True,
        source="Δ_λ^lin(T)/Δ_λ^sym(T) > 2 (exact log-trace spends the exp-vs-lin gap)")

    saved = builder.save()
    print(f"\n  verdict: 2nd-kind b → LINEAR ladder (m_qCLT); B_sym (m_sym) already "
          f"realizes the exponential.\n  Wrote {saved.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
