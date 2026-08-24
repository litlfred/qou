#!/usr/bin/env python3
"""Corner-removal induction step for Piece A, checked exhaustively.

Backs `lem:piece-a-corner-removal-obligation` and its proof block in
`content/quantum-observable-universe/mass-theory/`.

Piece A is the per-partition hook-content identity
`Sum_c h(c)^2 = Sum_c content(c)^2 + n^2`.  Lean proves it by the arm-leg /
beta-set route (`QOU.BraidKnot.PieceA.pieceA`).  The corner-removal induction
is a SECOND route, and it is not formalised anywhere in the repository -- so
this probe is the only mechanical backing the corner blocks have.  It checks
the five supporting steps and the assembled obligation on every corner of
every partition of n = 1..16, plus the two facts that make the obligation the
right induction step:

  * the obligation's left side really is `sumHookSq(lambda) - sumHookSq(mu)`
    for mu = lambda with the corner removed, and
  * `sumContentSq(lambda) - sumContentSq(mu) = content(corner)^2`,

so that obligation = content(corner)^2 + (n^2 - (n-1)^2) is exactly what the
induction on |lambda| has to discharge.

Everything here is exact integer arithmetic on `List[int]` partitions: no
substrate modulus, no float, no q.  Hence `q0Anchor: independent`.
"""
from __future__ import annotations

import json
import os
import sys
import time

NMAX = 16


def partitions(m: int, cap: int | None = None):
    cap = m if cap is None else cap
    if m == 0:
        yield ()
        return
    for first in range(min(m, cap), 0, -1):
        for rest in partitions(m - first, first):
            yield (first,) + rest


def col_len(lam, j: int) -> int:
    """Number of rows reaching column `j` (0-indexed columns)."""
    return sum(1 for p in lam if j < p)


def hook(lam, i: int, j: int) -> int:
    """h(i,j) = (lambda_i - j) + (colLen(j) - i) - 1."""
    return (lam[i] - j) + (col_len(lam, j) - i) - 1


def sum_hook_sq(lam) -> int:
    return sum(hook(lam, i, j) ** 2 for i in range(len(lam)) for j in range(lam[i]))


def sum_content_sq(lam) -> int:
    return sum((j - i) ** 2 for i in range(len(lam)) for j in range(lam[i]))


def corners(lam):
    """Cells (r, s) with s = lambda_r - 1 that are removable corners."""
    for r in range(len(lam)):
        if r + 1 < len(lam) and lam[r + 1] == lam[r]:
            continue
        yield r, lam[r] - 1


def main() -> int:
    t0 = time.time()
    total = 0
    ok = {
        "col_len_corner": 0,
        "row_sum_closed_form": 0,
        "column_sum_closed_form": 0,
        "size_decomposition": 0,
        "corner_removal_obligation": 0,
        "obligation_is_hook_sq_difference": 0,
        "content_sq_difference_is_corner_content_sq": 0,
        "piece_a_holds": 0,
    }
    piece_a_checked = 0

    for n in range(1, NMAX + 1):
        for lam in partitions(n):
            piece_a_checked += 1
            if sum_hook_sq(lam) == sum_content_sq(lam) + n * n:
                ok["piece_a_holds"] += 1
            for r, s in corners(lam):
                total += 1
                sum_r = sum(2 * hook(lam, r, j) - 1 for j in range(s))
                sum_s = sum(2 * hook(lam, i, s) - 1 for i in range(r))
                prefix_rows = sum(lam[i] for i in range(r))
                prefix_cols = sum(col_len(lam, j) for j in range(s))

                if col_len(lam, s) == r + 1:
                    ok["col_len_corner"] += 1
                if sum_r == 2 * prefix_cols + s * s - 2 * r * s:
                    ok["row_sum_closed_form"] += 1
                if sum_s == 2 * prefix_rows + r * r - 2 * s * r:
                    ok["column_sum_closed_form"] += 1
                if prefix_rows + prefix_cols - r * s + 1 == n:
                    ok["size_decomposition"] += 1

                obligation = 1 + sum_r + sum_s
                if obligation == (s - r) ** 2 + 2 * n - 1:
                    ok["corner_removal_obligation"] += 1

                mu = tuple(x for x in lam[:r] + (lam[r] - 1,) + lam[r + 1:] if x > 0)
                if obligation == sum_hook_sq(lam) - sum_hook_sq(mu):
                    ok["obligation_is_hook_sq_difference"] += 1
                if sum_content_sq(lam) - sum_content_sq(mu) == (s - r) ** 2:
                    ok["content_sq_difference_is_corner_content_sq"] += 1

    assertions = []
    for name, got in ok.items():
        expected = piece_a_checked if name == "piece_a_holds" else total
        assertions.append({
            "name": name,
            "computed": got,
            "expected": expected,
            "passed": got == expected,
            "source": "piece_a_corner_removal_probe",
        })

    witness = {
        "computation": "piece-a-corner-removal",
        "engine": "python",
        "scriptFile": "computations/probes/piece_a_corner_removal_probe.py",
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Exact integer arithmetic on partitions only. No substrate modulus, no "
            "q, no float: the import cone is json/os/sys/time. Nothing here can "
            "depend on the q0 anchor."),
        "parameters": {
            "n_max": NMAX,
            "partitions_checked": piece_a_checked,
            "corners_checked": total,
            "lean": "QOU.BraidKnot.PieceA.pieceA (arm-leg route; the corner "
                    "induction checked here is NOT formalised)",
        },
        "data": {
            "per_step_pass_counts": ok,
        },
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
    }

    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, os.path.join(root, "tools", "qou-substrate", "python"))
    from qou_substrate.witness import WitnessBuilder
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python",
        engine_version=sys.version.split()[0], q0_anchor="independent")
    witness["durationMs"] = int((time.time() - t0) * 1000)

    out = os.path.join(root, "computations", "probes",
                       "piece-a-corner-removal.witness.json")
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2)
        fh.write("\n")
    nf = sum(1 for a in assertions if not a["passed"])
    print(f" partitions n = 1..{NMAX}: {piece_a_checked}; corners: {total}")
    print(f" assertions: {len(assertions) - nf}/{len(assertions)} passed")
    print(f" witness: {out}")
    return 0 if nf == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
