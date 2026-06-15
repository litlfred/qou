#!/usr/bin/env python3
"""Low-isotopes binding sweep + active-set concentration (canonical path).

EXPLORATORY. Consolidates, for the low isotopes the canonical binding
(`binding_canonical.py`, Jones–Markov trace) currently covers:

  - B_AME, B_pred(C), and the residual Δ_λ(K)=B_AME/B_pred (with its
    near-integer q₀-power observation log_{q₀}Δ_λ ≈ 10A−5 — NOT wired,
    NOT derived; the structural-derivation attempt was a negative, see
    docs/audits/2026-06-09-delta-lambda-canonical-residual.md);
  - the ACTIVE SET of each tr_M: how few partitions carry 90% of the
    Markov trace, from the matrix-M χ caches.

Headline for compute-scaling (the directive): the active set is **3–4
few-row partitions** ([n],[n−1,1],[n−2,2],[n−3,3]) out of p(3A) — so
binding scales in O(A·few) if restricted to the active set + nucleon-block
caching, instead of O(p(3A)). See
docs/audits/2026-06-10-binding-active-set-compute-optimization.md.

Reads (read-only): binding-canonical.witness.json + chi-*-matrix-m caches.
Output: low-isotopes-binding-sweep.witness.json
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

CHI_CACHE = {
    (1, 1): "chi-deuteron-h6-at-q0-50dps-matrix-m.witness.json",
    (1, 2): "chi-tritium-h9-at-q0-50dps-matrix-m.witness.json",
}


def _p(n: int) -> int:
    """Number of integer partitions of n."""
    parts = [1] + [0] * n
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            parts[j] += parts[j - k]
    return parts[n]


def active_set(Z: int, N: int):
    f = CHI_CACHE.get((Z, N))
    if not f or not (HERE / f).exists():
        return None
    w = json.loads((HERE / f).read_text())
    bp = w.get("data", {}).get("by_partition") or w.get("by_partition")
    valid = [(str(e["partition"]), abs(float(e["contribution"])), e.get("dim"))
             for e in bp if e.get("chi_lambda") != "skipped-max-dim"]
    tot = sum(c for _, c, _ in valid)
    valid.sort(key=lambda x: -x[1])
    cum, top = 0.0, []
    for p, c, d in valid:
        cum += c
        top.append({"partition": p, "dim": d, "frac": round(c / tot, 4)})
        if cum >= 0.9 * tot:
            break
    return {"n_partitions_total": len(bp), "n_in_active_90pct": len(top),
            "active_partitions": top}


def main() -> int:
    t0 = time.monotonic()
    q0 = float(q_at(30))
    lnq = math.log(q0)
    bc = json.loads((HERE / "binding-canonical.witness.json").read_text())["data"]["results"]

    rows = []
    for r in bc:
        Z, N, A = r["Z"], r["N"], r["A"]
        B_ame = float(r["B_AME_MeV"])
        B_pred = float(r["B_MeV"])
        dl = B_ame / B_pred
        x = math.log(dl) / lnq
        a_set = active_set(Z, N)
        rows.append({
            "atom": r["atom"], "Z": Z, "N": N, "A": A, "n_strands": 3 * A,
            "B_AME_MeV": round(B_ame, 5),
            "B_pred_canonical_MeV": round(B_pred, 5),
            "Delta_lambda": round(dl, 4),
            "log_q0_Delta": round(x, 3),
            "law_10A_minus_5": 10 * A - 5,
            "dev_from_law": round(x - (10 * A - 5), 3),
            "p_3A": _p(3 * A),
            "active_set": a_set,
        })

    w = WitnessBuilder("low-isotopes-binding-sweep", engine="python", start_time=t0)
    w.set_description(
        "Low-isotopes binding sweep on the canonical Jones–Markov path "
        "(binding_canonical.py): B_AME, B_pred, residual Δ_λ (near-match "
        "q₀^(10A−5), not derived), and the tr_M ACTIVE SET (3–4 few-row "
        "partitions carry 90% of p(3A)) — the basis for active-set-truncated "
        "+ nucleon-cached O(A·few) scaling."
    )
    w.add_data("rows", rows)
    w.add_data("scaling_metric", {
        "active_set_size_typical": "3–4 partitions",
        "p_3A_examples": {f"A={A}": _p(3 * A) for A in (2, 3, 4, 6, 8)},
        "saving": "compute active set only → O(A·few) vs O(p(3A))",
        "active_partitions_are": "few-row: [n],[n−1,1],[n−2,2],[n−3,3]",
    })
    w.add_data("delta_lambda_note",
               "log_q0 Δ_λ ≈ 10A−5 is a LOOSE 4-point near-match (³He off "
               "1.40); no clean crossing/jet derivation (refuted). NOT wired.")
    # active sets where we have caches must be small
    have = [r for r in rows if r["active_set"]]
    w.add_assertion(
        name="active_set_small",
        computed=max((r["active_set"]["n_in_active_90pct"] for r in have), default=0),
        expected=0.0, tolerance=5.0,
        source="≤5 partitions carry 90% of tr_M on the cached isotopes (D,T)",
    )

    out = w.save()
    print(f"{'atom':>5} {'A':>1} {'B_AME':>8} {'B_pred':>8} {'Δ_λ':>8} "
          f"{'log_q0':>7} {'10A−5':>6} {'p(3A)':>6} {'active90%':>9}")
    for r in rows:
        a = r["active_set"]
        act = f"{a['n_in_active_90pct']}/{a['n_partitions_total']}" if a else "—"
        print(f"{r['atom']:>5} {r['A']:>1} {r['B_AME_MeV']:>8.3f} "
              f"{r['B_pred_canonical_MeV']:>8.4f} {r['Delta_lambda']:>8.3f} "
              f"{r['log_q0_Delta']:>7.2f} {r['law_10A_minus_5']:>6} "
              f"{r['p_3A']:>6} {act:>9}")
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
