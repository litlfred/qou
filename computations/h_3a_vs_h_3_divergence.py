#!/usr/bin/env python3
"""
h_3a_vs_h_3_divergence.py — H_3 Jones-Markov reference + H_{3A}
extension scaffolding (P3 from `docs/coordination/1ppb.md`).

**Important — author's correction (2026-05-08):** an earlier draft
of this script used `hecke_3a_weights.wedderburn_weights_3a` which
returns the **symmetric Plancherel weight** w_λ = dim_q² / [n]_q!.
Per `markov_weights_symbolic.py:18-23`, that is **NOT** the correct
Jones-Markov weight y_λ(q) for q ≠ 1; they coincide only at the
classical Plancherel point q = 1.  The QOU paper requires y_λ via
Wenzl's Schur principal specialization.  This script now uses the
correct y_λ.

**Scope (this session, A = 1 only):**

The Wenzl-formula `markov_weights_symbolic.solve_y_lambda(n)` is
symbolic in q and scales combinatorially with the partition count
p(n).  At p(3) = 3 it is fast (cached witness available); at
p(6) = 11, p(9) = 30, p(12) = 77 the symbolic computation exceeds
session-time budgets.  This script is therefore scoped to the
**H_3 reference table only**, reading from the existing
`markov_weights_symbolic.witness.json` cache.

The H_{3A} extension for A ≥ 2 is **deferred** to a follow-up
audit that can (a) run `solve_y_lambda(3A)` overnight, or
(b) implement a faster numerical-from-the-start path that
substitutes q = q_0 before the symbolic Schur evaluation.

References:
- prop:atomic-mass-gb-nf
- prop:per-nucleon-shift-additive-linearity
- 1ppb workplan §P3 (`docs/coordination/1ppb.md`)
- markov_weights_symbolic.solve_y_lambda — canonical Jones-Markov
  weight calculator via Wenzl's principal specialization formula
- `markov-weights-symbolic.witness.json` — cached H_3 reference

Witness: `h-3a-vs-h-3-divergence.witness.json`
Audit-only: docs/audits/2026-05-08-p3-h-3a-divergence.md

@module folio-assistant/computations/h_3a_vs_h_3_divergence
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

import markov_weights_symbolic as m  # noqa: E402
from q_parameter import Q as Q_FLOAT  # noqa: E402  — single source of truth
from witness_base import WitnessBuilder  # noqa: E402

# Substrate parameter (q_0 from CODATA / paper).
Q_SYM = sp.symbols("q", positive=True)
Q_0 = sp.Float(Q_FLOAT, 30)


def _y_lambda_numeric(n: int) -> dict[tuple, float]:
    """Numerical Jones-Markov y_λ(q_0) at H_n via Wenzl's principal
    specialization, with **numerical-q-from-start**: substitutes
    q = q_0 BEFORE the Wenzl normalisation, avoiding the symbolic
    sp.cancel bottleneck on rational expressions.

    For n=3: ~0.05s.  For n=6: ~3.5s.  For n=9: ~65s (30 partitions).
    For n ≥ 12: too slow for interactive sessions; defer to overnight
    runs with intermediate caching.
    """
    shapes = [tuple(s) for s in m.partitions_of(n)]
    s_vals_num = {}
    for sh in shapes:
        s_vals_num[sh] = (
            m.schur_principal_symbolic(list(sh))
             .subs(Q_SYM, Q_0)
             .evalf(30)
        )
    Z = sp.Integer(0)
    for sh in shapes:
        hs, _ = m.hooks_and_contents(list(sh))
        prod = 1
        for h in hs:
            prod *= h
        f_lam = factorial(n) // prod
        Z = Z + s_vals_num[sh] * f_lam
    return {sh: float(s_vals_num[sh] / Z) for sh in shapes}


def main() -> int:
    builder = (
        WitnessBuilder(name="h-3a-vs-h-3-divergence", engine="sympy")
        .set_description(
            "P3 (1ppb workplan): compare H_3 (legacy shortcut) vs "
            "H_{3A} **Jones-Markov** weight tables for n ∈ {3, 6, 9} "
            "(A ∈ {1, 2, 3}). Reports per-partition y_λ(q_0) via "
            "Wenzl's Schur principal specialization with numerical-q-"
            "from-start (substitutes q = q_0 before sp.cancel, "
            "avoiding the symbolic-rational bottleneck). H_12 (⁴He) "
            "is deferred — feasible but ~150–300s, too long for "
            "interactive session."
        )
        .set_audit_only("docs/audits/2026-05-08-p3-h-3a-divergence.md")
    )

    h_3a_tables: dict[int, dict[tuple, float]] = {}
    for n in (3, 6, 9):
        t0 = time.monotonic()
        ys = _y_lambda_numeric(n)
        elapsed = time.monotonic() - t0
        print(f"  n={n}: {len(ys)} partitions, {elapsed:.2f}s",
              file=sys.stderr)
        h_3a_tables[n] = ys

    n_to_atom: dict[int, list[str]] = {
        3: ["p", "n"],     # A=1
        6: ["D"],          # A=2
        9: ["T", "3He"],   # A=3
    }
    h_3 = h_3a_tables[3]
    h_3_total_y = sum(h_3.values())

    rows = []
    for n in (3, 6, 9):
        h_n = h_3a_tables[n]
        total_y = sum(h_n.values())
        partition_count = len(h_n)
        # Per-atom rows
        for atom in n_to_atom[n]:
            divergence_pct = (
                100.0 * (total_y - h_3_total_y) / h_3_total_y
                if h_3_total_y
                else 0.0
            )
            sorted_by_y = sorted(h_n.items(), key=lambda kv: -abs(kv[1]))[:3]
            top_3 = [
                {"partition": list(lam), "y_at_q0": float(y)}
                for lam, y in sorted_by_y
            ]
            rows.append({
                "atom": atom,
                "n_strands": n,
                "h_3a_partition_count": partition_count,
                "h_3a_sum_y_at_q0": float(total_y),
                "h_3_sum_y_at_q0": float(h_3_total_y),
                "divergence_vs_h_3_pct": float(divergence_pct),
                "top_3_partitions_by_abs_y": top_3,
            })

        builder.add_assertion(
            name=f"h_n_{n}_partition_count_eq_p_of_n",
            computed=partition_count,
            expected={3: 3, 6: 11, 9: 30}[n],
        )
        # Σ y_λ should be finite + positive (Wenzl/Jones normalisation
        # gives Σ y_λ · f^λ = 1 where f^λ are SYT counts; the bare
        # Σ y_λ is not 1 but is finite + atom-dependent).
        builder.add_assertion(
            name=f"h_n_{n}_y_lambda_sum_finite_positive",
            computed=str(0 < total_y < 100),
            expected="True",
        )

    # Divergence assertions per atom
    for row in rows:
        if row["n_strands"] == 3:
            continue  # H_3 vs H_3 = 0
        builder.add_assertion(
            name=f"divergence_above_1ppb_floor[{row['atom']}]",
            computed=str(abs(row["divergence_vs_h_3_pct"]) > 0.001),
            expected="True",
        )

    builder.add_data("atomic_divergence_table", rows)
    builder.add_data(
        "h_3_jones_markov_table_at_q0",
        [
            {"partition": list(lam), "y_at_q0": float(y)}
            for lam, y in sorted(h_3.items(), key=lambda kv: -abs(kv[1]))
        ],
    )
    builder.add_data(
        "h_6_jones_markov_table_at_q0",
        [
            {"partition": list(lam), "y_at_q0": float(y)}
            for lam, y in sorted(
                h_3a_tables[6].items(), key=lambda kv: -abs(kv[1])
            )
        ],
    )
    builder.add_data(
        "h_9_jones_markov_table_at_q0",
        [
            {"partition": list(lam), "y_at_q0": float(y)}
            for lam, y in sorted(
                h_3a_tables[9].items(), key=lambda kv: -abs(kv[1])
            )
        ],
    )
    builder.add_data(
        "method",
        {
            "weight_formula": (
                "Jones-Markov y_λ(q) via Wenzl's Schur principal "
                "specialization, NUMERICAL-q-from-start: substitutes "
                "q = q_0 before sp.cancel.  Avoids the symbolic-"
                "rational bottleneck that made naive "
                "solve_y_lambda(n) intractable for n ≥ 6 in "
                "interactive sessions."
            ),
            "wrong_weight_to_avoid": (
                "Symmetric Plancherel w_λ = dim_q² / [n]_q! (used by "
                "hecke_3a_weights.py and paper_six_term_shadow_price_"
                "sweep.w_lambda).  These coincide with y_λ ONLY at "
                "q = 1; the QOU paper at q = q_0 requires y_λ."
            ),
            "p_of_n_growth": {
                "n=3 (A=1, p, n)": "p(3) = 3",
                "n=6 (A=2, D)": "p(6) = 11",
                "n=9 (A=3, T, 3He)": "p(9) = 30",
                "n=12 (A=4, 4He)": (
                    "p(12) = 77 — feasible but ~150-300s "
                    "via numerical-q-from-start; deferred"
                ),
            },
            "downstream_action": (
                "#564 mass-table integration should consume y_λ from "
                "this witness's h_*_jones_markov_table_at_q0 sections "
                "or call markov_weights_symbolic.solve_y_lambda(3A) "
                "directly (overnight runs for A ≥ 4)."
            ),
        },
    )

    out_path = builder.save()

    print(f"\n✓ {len(rows)} atomic rows checked", file=sys.stderr)
    for row in rows:
        print(f"  {row['atom']} (n={row['n_strands']}): "
              f"H_n partitions={row['h_3a_partition_count']}, "
              f"Σ y={row['h_3a_sum_y_at_q0']:.6f}, "
              f"div vs H_3={row['divergence_vs_h_3_pct']:+.4f}%",
              file=sys.stderr)
    print(f"  Wrote {out_path}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
