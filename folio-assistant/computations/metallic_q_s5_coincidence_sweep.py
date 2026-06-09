#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only sweep across counterfactual q.
"""
S(5) — exact n=5 metallic coincidence sweep + LP active-set checkpoints.

Extends the n=3/n=4 exact-Gram probe (`metallic_q_s4_exact_lp_sweep.py`,
PR #2081) to the 120-word T_w basis of H_5(q).  Two structural lessons
from n≤4 shape the design:

  * the LP active set was CONSTANT under the exact Gram at n ≥ 3, so
    the full per-point Gram sweep (120² concatenation traces per q) is
    replaced by LP solves at ~25 checkpoints (metallic points ± ε and
    interval midpoints) to re-test constancy;
  * the scientific payload is the COST-COINCIDENCE set: pairwise
    t_i(q) = t_j(q) roots of the trace-class representatives over a
    fine grid, mpfr-refined at metallic candidates.

Conventions, validations and witness discipline are inherited from the
n≤4 module (imported, not duplicated).  Prediction under test:
S(5) = {δ_silver} (silver-only, continuing n=2,3,4), against the
sharpened-(M2) alternative S(5) ⊆ {δ_1..δ_5}.
"""

from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import pyhecke_native as pn

from metallic_q_s4_exact_lp_sweep import (
    METALLIC, METALLIC_NAMES, Q0, coincidence_roots, reduced_words,
    solve_lp, t_and_gram, trace_classes, validations, word_label,
)

mp.mp.dps = 50
HERE = Path(__file__).parent

N = 5
TOP_K = 5


def lp_checkpoints() -> list[mp.mpf]:
    eps = mp.mpf("0.02")
    pts: list[mp.mpf] = [Q0 + eps]
    anchors = [Q0] + [METALLIC[k] for k in range(1, TOP_K + 1)]
    for a, b in zip(anchors, anchors[1:]):
        pts += [(a + b) / 2, b - eps, b, b + eps]
    pts.append(METALLIC[TOP_K] + mp.mpf("0.3"))
    return pts


def main() -> None:
    t0 = time.time()
    print("S(5) sweep — inherited validations…", file=sys.stderr)
    checks = validations()
    hard = ["v1_n2_proved_closed_forms", "v2_silver_exact",
            "v3_canonical_markov_stable", "v4_hecke_relation",
            "v5_trace_symmetry"]
    assert all(checks[k] for k in hard), f"validation failure: {checks}"

    shapes = pn.partitions_of(N)
    basis = reduced_words(N)
    words = [w for _, w in basis]
    labels = [word_label(w) for w in words]
    print(f"basis: {len(words)} words; partitions: {len(shapes)}",
          file=sys.stderr)

    # trace classes (per convention) — also a deliverable
    classes = {conv: trace_classes(N, shapes, words, conv)
               for conv in ("plancherel", "canonical")}
    for conv, cls in classes.items():
        print(f"  [{conv}] {len(cls)} trace classes", file=sys.stderr)

    # coincidence roots over the fine grid
    coinc = {}
    for conv in ("plancherel", "canonical"):
        print(f"coincidence grid [{conv}]…", file=sys.stderr)
        coinc[conv] = coincidence_roots(
            N, shapes, words, labels, conv, 1.02,
            float(METALLIC[TOP_K]) + 0.45, TOP_K,
        )
        met = [c for c in coinc[conv] if c["metallic"]]
        print(f"  [{conv}] {len(coinc[conv])} roots, {len(met)} metallic",
              file=sys.stderr)
        for c in met:
            print(f"    METALLIC {c['pair']} q*={c['q_root']:.9f} "
                  f"{c['metallic']} exact={c.get('metallic_exact')}",
                  file=sys.stderr)

    # LP active-set checkpoints (exact Gram — the heavy part)
    lp_rows = []
    for q in lp_checkpoints():
        row: dict = {"q": str(q)}
        for conv in ("plancherel", "canonical"):
            t, G = t_and_gram(N, shapes, words, float(q), conv)
            lp = solve_lp(t, G)
            row[conv] = {
                "active_set": lp.get("active_set"),
                "status": lp["status"],
            }
            if any(abs(q - METALLIC[k]) < 1e-12 for k in range(1, TOP_K + 1)):
                row[conv]["lp_full"] = lp
        lp_rows.append(row)
        print(f"  LP q={float(q):.5f}: "
              f"pl={row['plancherel']['active_set']} "
              f"can={row['canonical']['active_set']}", file=sys.stderr)

    active_constant = {}
    for conv in ("plancherel", "canonical"):
        sets = [r[conv]["active_set"] for r in lp_rows
                if r[conv]["active_set"] is not None]
        active_constant[conv] = bool(sets and all(s == sets[0] for s in sets))

    def s_set(conv: str) -> list[str]:
        return sorted({c["metallic"] for c in coinc[conv] if c["metallic"]})

    verdict = {f"S(5)_{conv}": s_set(conv)
               for conv in ("plancherel", "canonical")}
    print(json.dumps(verdict, indent=2), file=sys.stderr)

    witness = {
        "description": (
            "S(5) exact metallic coincidence sweep on the 120-word T_w "
            "basis of H_5(q) with LP active-set checkpoints (exact "
            "Gram).  Design informed by the n≤4 result: coincidence "
            "grid is the payload; LP constancy re-tested at ~25 "
            "checkpoints instead of a dense Gram sweep.  Conventions, "
            "validations, dual-emission and mpfr refinement inherited "
            "from metallic_q_s4_exact_lp_sweep.py."
        ),
        "computed_at": datetime.now(timezone.utc).isoformat(),
        "script": "metallic_q_s5_coincidence_sweep.py",
        "engine": "pyhecke_native " + getattr(pn, "__version__", "0.9.0"),
        "validations": checks,
        "n": N,
        "n_basis_words": len(words),
        "trace_class_counts": {k: len(v) for k, v in classes.items()},
        "trace_classes_labels": {
            conv: [[labels[i] for i in cl] for cl in cls]
            for conv, cls in classes.items()
        },
        "coincidences": coinc,
        "lp_checkpoints": lp_rows,
        "lp_active_set_constant": active_constant,
        "S_sets": verdict,
        "metallic_ladder": {METALLIC_NAMES[k]: mp.nstr(METALLIC[k], 30)
                            for k in range(1, TOP_K + 1)},
        "limitations": [
            "LP solved at checkpoints (metallic points ± 0.02 and "
            "interval midpoints), not on a dense grid — justified by "
            "the n=3/n=4 exact-Gram constancy result this re-tests.",
            "coincidence roots f64-bisected; metallic candidates "
            "re-verified at 40-dps mpfr (plancherel convention).",
        ],
        "runtime_seconds": round(time.time() - t0, 1),
    }
    out = HERE / "metallic-q-s5-coincidence-sweep.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"Saved witness: {out}", file=sys.stderr)
    print(f"TOTAL {witness['runtime_seconds']} s", file=sys.stderr)


if __name__ == "__main__":
    main()
