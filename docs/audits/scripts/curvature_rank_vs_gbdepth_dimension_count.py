#!/usr/bin/env python3
"""Can the Coxeter-length filtration carry the partition grading? A counting test.

## What changed since the last pass, and what I got wrong

Bean `wpdb` recorded that the word-depth -> partition-depth bridge is stated
nowhere, and I then wrote (PR #5205, and in the bean) that the *sharper* question
was whether the word-side rank `r(T_w)` is even well defined on the quotient --
"on the face of it, it is not", because a word is not an element of `H_n(q)`.

**That was wrong, and reading the corpus settles it.**
`mba-step07-gb-filtration.md` defines the GB filtration independently and
concretely:

    F_l is the span of basis elements T_w with l(w) <= l

`T_w` is the standard Hecke basis, indexed by `w` in `S_n`, and `l` is the
Coxeter length -- a function on the *group*, independent of the choice of
reduced word by Matsumoto's theorem. So the filtration is perfectly well
defined and my objection does not apply. Retracted.

## The defect that is actually there

With `r = l` pinned, the two sides become *countable* and can be compared
without any Hecke machinery at all.

Four content blocks read

    Z^(k)(A) = span{ e_lambda : gbDepth(lambda) = k }

off `prop:curvature-rank-gb-stratification`, whose stratum is
`{T_w : r(T_w) = r}`, i.e. `gr_r` of the length filtration. Taking the
charitable reading -- that `Z^(k)` is the degree-`k` piece of the filtration
*induced on the centre*, `(Z cap F_k)/(Z cap F_{k-1})`, which embeds in `gr_k`
-- gives a necessary condition that needs nothing but dimensions:

    #{ lambda |- n : gbDepth(lambda) = k }  <=  #{ w in S_n : l(w) = k }   for every k

The left side is a dimension because the central idempotents `e_lambda` are
linearly independent (orthogonal idempotents). The right side is a dimension
because the `T_w` are a basis. Both are integers this script counts directly.

`gbDepth(lambda) = lambda_1 + lambda'_1 - 1` is the corner hook, proved as
`QOU.BraidKnot.gbDepth_eq_corner` (sorry-free), so the left side needs no
assumption either.

## Scope

**Scope-(a) where the condition holds, scope-(b) where it fails.** A failure is
a *proved* impossibility -- a subspace cannot have larger dimension than the
space containing it -- so where the count fails, that reading of the
identification is structurally excluded, not merely unsupported. What is
excluded is the *charitable reading* of the four blocks' identification; other
readings of `Z^(k)` are untouched, and this says nothing about whether the mass
results are right.

Usage:
  python3 -u docs/audits/scripts/curvature_rank_vs_gbdepth_dimension_count.py
"""
from __future__ import annotations

import json
import os
from itertools import permutations
from pathlib import Path

OUT = Path(__file__).with_suffix(".witness.json")
REPO = Path(__file__).resolve().parents[3]


def partitions(n: int, mx: int | None = None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def gb_depth(lam: tuple[int, ...]) -> int:
    """lambda_1 + lambda'_1 - 1, the corner hook (QOU.BraidKnot.gbDepth_eq_corner)."""
    return lam[0] + len(lam) - 1


def coxeter_length(w: tuple[int, ...]) -> int:
    """Coxeter length on S_n = the inversion count. Standard; this is the
    combinatorial model of the same `l` Mathlib's `CoxeterSystem.length` gives
    for type A, and it is what makes the filtration well defined."""
    return sum(
        1 for i in range(len(w)) for j in range(i + 1, len(w)) if w[i] > w[j]
    )


def length_distribution(n: int) -> dict[int, int]:
    """The Mahonian numbers: #{w in S_n : l(w) = k}."""
    dist: dict[int, int] = {}
    for w in permutations(range(n)):
        dist[coxeter_length(w)] = dist.get(coxeter_length(w), 0) + 1
    return dist


def depth_distribution(n: int) -> dict[int, int]:
    dist: dict[int, int] = {}
    for lam in partitions(n):
        d = gb_depth(lam)
        dist[d] = dist.get(d, 0) + 1
    return dist


def main() -> None:
    rows = []
    violations = []
    for n in range(2, 8):
        ell = length_distribution(n)
        dep = depth_distribution(n)
        bad = []
        for k, need in sorted(dep.items()):
            have = ell.get(k, 0)
            if need > have:
                bad.append(
                    {
                        "k": k,
                        "dim_Z_k_required": need,
                        "dim_gr_k_available": have,
                        "shortfall": need - have,
                    }
                )
        rows.append(
            {
                "n": n,
                "length_distribution": {str(k): v for k, v in sorted(ell.items())},
                "gbDepth_distribution": {str(k): v for k, v in sorted(dep.items())},
                "violations": bad,
                "condition_holds": not bad,
            }
        )
        if bad:
            violations.append(n)
        flag = "VIOLATION" if bad else "ok"
        print(
            f"n={n}: gbDepth {dict(sorted(dep.items()))}"
            f"   vs  lengths {dict(sorted(ell.items()))}   -> {flag}"
        )
        for b in bad:
            print(
                f"        k={b['k']}: need dim {b['dim_Z_k_required']}, "
                f"gr_{b['k']} has only {b['dim_gr_k_available']}"
            )

    print(f"\nnecessary condition FAILS at n = {violations}")
    print("holds at n = " + str([r["n"] for r in rows if r["condition_holds"]]))

    OUT.write_text(
        json.dumps(
            {
                "schema": "qou-audit-probe/v1",
                "question": (
                    "Can the Coxeter-length filtration F_l = span{T_w : l(w) <= l} "
                    "carry the partition grading Z^(k) = span{e_lambda : "
                    "gbDepth(lambda) = k} that four content blocks read off "
                    "prop:curvature-rank-gb-stratification?"
                ),
                "retraction": (
                    "This probe retracts my own claim (PR #5205, bean wpdb) that the "
                    "word-side rank is probably not well defined on the quotient. "
                    "mba-step07-gb-filtration.md defines the filtration by Coxeter "
                    "length on S_n, which is well defined by Matsumoto. The "
                    "objection does not apply."
                ),
                "necessary_condition": (
                    "#{lambda |- n : gbDepth = k} <= #{w in S_n : l(w) = k} for all k, "
                    "since the e_lambda are linearly independent and the T_w are a basis"
                ),
                "verdict": "fails at n = 2 and n = 3; holds for 4 <= n <= 7",
                "fails_at": violations,
                "why_it_matters": (
                    "n = 3 is the single-nucleon case -- H_3 is where the framework's "
                    "m_p / m_n results live. gbDepth is constant (= 3) on all three "
                    "partitions of 3, so the reading needs dim gr_3 >= 3, but only the "
                    "longest element of S_3 has length 3, so dim gr_3 = 1."
                ),
                "scope": (
                    "Scope-(b) where it fails -- a subspace cannot exceed the "
                    "dimension of its ambient space, so this is a proved exclusion "
                    "of the charitable reading of the identification, not a failed "
                    "probe. It is NOT a refutation of the mass results, and other "
                    "readings of Z^(k) are untouched."
                ),
                "rows": rows,
            },
            indent=2,
        )
        + "\n"
    )
    print(f"wrote {os.path.relpath(OUT, REPO)}")


if __name__ == "__main__":
    main()
