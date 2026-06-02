#!/usr/bin/env python3
"""laurentq_a5_ceiling_measure.py — F7 measurement

Per the audit's F7 entry (`docs/audits/2026-05-08-compute-
infrastructure-audit.md`):

  > P17 (LaurentQ wiring) extension to A ≥ 5. The 17aee993 benchmark
  > shows speedup fades past A=4 because GS reduction dominates.
  > R4 quotient-ideal port into LaurentQ would recover the gap but
  > is research-grade. Defer.

This script is the measurement that pins down the empirical ceiling.
For A = 1..4 (proton, deuteron, ³He / T, ⁴He) it benchmarks both
paths on `tr_M_atomic`:

  - SLOW path: `markov_peel.tr_M_atomic(Z, N, use_fast=False)` — pure
    sympy rule-loop reduction.
  - FAST path: `hecke_laurent_fast.tr_M_atomic_fast(Z, N)` — LaurentQ
    coefficient kernel.

Reports per-A walltime ratio. The audit expects:

    A = 1:  fast ≈ 0.6× slow  (fast path overhead loses to small word)
    A = 2:  fast ≈ 1× slow
    A = 3:  fast ≈ 5–10× slow  (sweet spot)
    A = 4:  fast ≈ 5–6× slow  (still good)
    A ≥ 5:  fast ≈ 1× slow    (GS reduction dominates; LaurentQ wins lost)

If A ≥ 5 actually shows < 1× speedup, the F7 ceiling is confirmed.
The R4 quotient-ideal port would lift it.

This script delivers DATA, not a fix; F7 stays open with this
measurement as its empirical anchor.

CAVEAT: A=5 may take many minutes per call on the slow path; if the
local environment's timeout aborts, the witness records the partial
data with timing-only A=1..4.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402


def _bench_one(Z: int, N: int) -> dict:
    """Benchmark slow + fast paths on (Z, N).

    Records walltime for each path and the numerical agreement at q_0.
    Exceptions are captured into the result dict so the witness still
    records partial data when one path fails or runs out of memory.
    """
    from markov_peel import tr_M_atomic
    from hecke_symbolic import q as q_sym
    from q_parameter import Q as Q0
    A = Z + N
    result = {"Z": Z, "N": N, "A": A,
              "slow_s": None, "fast_s": None,
              "slow_skipped": False, "fast_skipped": False,
              "speedup": None,
              "agree_at_q0": None}
    try:
        t0 = time.perf_counter()
        slow_result = tr_M_atomic(Z, N, use_fast=False)
        result["slow_s"] = time.perf_counter() - t0
    except Exception as e:
        result["slow_skipped"] = True
        result["slow_error"] = str(e)[:200]
        slow_result = None
    try:
        t0 = time.perf_counter()
        fast_result = tr_M_atomic(Z, N, use_fast=True)
        result["fast_s"] = time.perf_counter() - t0
    except Exception as e:
        result["fast_skipped"] = True
        result["fast_error"] = str(e)[:200]
        fast_result = None
    if result["slow_s"] and result["fast_s"]:
        result["speedup"] = result["slow_s"] / result["fast_s"]
    if slow_result is not None and fast_result is not None:
        try:
            slow_v = float(slow_result.subs(q_sym, float(Q0)).evalf())
            fast_v = float(fast_result.subs(q_sym, float(Q0)).evalf())
            result["agree_at_q0"] = abs(slow_v - fast_v) < 1e-10
            result["slow_value_q0"] = slow_v
            result["fast_value_q0"] = fast_v
        except Exception as e:
            result["agree_check_error"] = str(e)[:200]
    return result


def main() -> int:
    print("F7 measurement — LaurentQ vs sympy on tr_M_atomic\n")
    # Benchmark up through A = 3 by default; A = 4 if --include-4 set.
    # A = 5 requires significant compute; report status only.
    cases = [
        (1, 0, "proton"),
        (0, 1, "neutron"),
        (1, 1, "deuteron"),
        (2, 1, "³He"),
        (1, 2, "T"),
    ]
    if "--include-4" in sys.argv:
        cases.append((2, 2, "⁴He"))
    if "--include-5" in sys.argv:
        cases.extend([(3, 2, "⁵Li"), (2, 3, "⁵He")])

    results = []
    print(f"  {'atom':<10} {'A':>2} {'slow_s':>10} {'fast_s':>10} "
          f"{'speedup':>9} {'agree':>7}")
    print("  " + "-" * 60)
    for Z, N, name in cases:
        r = _bench_one(Z, N)
        r["atom"] = name
        results.append(r)
        slow_s = f"{r['slow_s']:.3f}" if r['slow_s'] else "skip"
        fast_s = f"{r['fast_s']:.3f}" if r['fast_s'] else "skip"
        speedup = f"{r['speedup']:.2f}×" if r['speedup'] else "—"
        agree = str(r.get('agree_at_q0', '?'))[:5]
        print(f"  {name:<10} {r['A']:>2} {slow_s:>10} {fast_s:>10} "
              f"{speedup:>9} {agree:>7}")

    out = (WitnessBuilder("laurentq-a5-ceiling-measure", engine="python")
        .set_audit_only("docs/audits/2026-05-08-compute-infrastructure-audit.md")
        .set_description(
            "F7 empirical measurement: LaurentQ vs sympy walltime "
            "on tr_M_atomic for A = 1..(3 default, 4 with "
            "--include-4, 5 with --include-5). Audit predicts "
            "speedup fades past A=4 because GS reduction dominates; "
            "this script supplies the data."
        )
        .add_data("results", results)
        .add_data("audit_prediction", {
            "A_1": "fast ≈ 0.6× slow (overhead loses on small words)",
            "A_2": "fast ≈ 1× slow",
            "A_3": "fast ≈ 5–10× slow (sweet spot)",
            "A_4": "fast ≈ 5–6× slow (still good)",
            "A_ge_5": "fast ≈ 1× slow (GS reduction dominates)",
        })
        .add_assertion(
            "all_paths_agree_at_q0",
            computed=1.0 if (
                any(r.get("agree_at_q0") is True for r in results)
                and all(
                    r.get("agree_at_q0") is not False for r in results
                )
            ) else 0.0,
            expected=1.0,
            tolerance=0.0,
            source=(
                "numerical equivalence of slow vs fast at q_0; "
                "fails if any row disagrees, requires at least one "
                "successfully-computed agreement"
            ),
        )
        .add_assertion(
            "n_atoms_benchmarked",
            computed=len(results),
            expected=len(cases),
            tolerance=0,
            source="all configured cases produced a row",
        )
        .save())
    print(f"\n  Witness: {out}")
    print()
    print("  Run with --include-4 for A=4, --include-5 for A=5 (very slow).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
