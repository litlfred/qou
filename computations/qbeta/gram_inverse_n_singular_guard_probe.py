#!/usr/bin/env python3
"""The general-n Gram inverse refuses — and why the residual check cannot catch it.

Bean `qou-cds2`. Companion to `tl3_gram_nonsingular_probe.py` (`qou-8iru`),
which establishes where the inverse DOES exist; this one pins down where it
does not, and why the failure is silent.

## What was found

`pyhecke.gram.gram_inverse` was deleted under `qou-cds2` because the
convention-D Markov-Gram form is singular. Its general-n successor,
`computations/pyhecke_n_generic.py::gram_inverse_n`, did a bare
``np.linalg.inv(G)`` — the guard did not come with the generalisation, and the
module's own header actively recommended migrating onto it.

## Why a warning would not have been enough

numpy raises nothing, and the returned matrix passes the obvious check:

    n=3   dim 3   rank 2   corank 1   max|G^-1| 5.03e16   ||G.G^-1 - I|| = 1.11e-16
    n=4   dim 5   rank 3   corank 2   max|G^-1| 3.27e16   ||G.G^-1 - I|| = 0

At n=4 the residual is EXACTLY ZERO. The entries are large enough that the
product rounds to the identity in float64, so a consumer validating
``G @ G_inv ≈ I`` is handed a clean bill of health on a meaningless inverse.
There is no downstream check that would notice — hence a hard raise.

## The rank is not arbitrary

It is the number of partitions of `n` with at most two rows — the
Temperley-Lieb structure established from the `y_λ` side in `qou-8iru`,
arriving here independently from the rank of a numerically-built Gram.

    n=3:  partitions 3  ->  {(3), (2,1)}          rank 2
    n=4:  partitions 5  ->  {(4), (3,1), (2,2)}   rank 3

## Scope

Scope-(a): the defect is these call sites. It does NOT build the quotient —
that is `qou-8iru` — and it wires nothing. float64 appears here only because
the object under test IS the float64 path; the mathematical facts it asserts
(rank, corank) are integer-valued and basis-structural, and the exact ℚ(q)
statement of non-singularity on the quotient lives in the companion probe.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

_CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    _CHECKS.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")


def _partitions(n: int) -> list[tuple[int, ...]]:
    if n == 0:
        return [()]
    out = []

    def rec(rem: int, mx: int, cur: tuple[int, ...]) -> None:
        if rem == 0:
            out.append(cur)
            return
        for k in range(min(rem, mx), 0, -1):
            rec(rem - k, k, cur + (k,))

    rec(n, n, ())
    return out


def main() -> int:
    from pyhecke_n_generic import gram_matrix_n, gram_inverse_n

    for n in (3, 4):
        G = np.asarray(gram_matrix_n(n), dtype=float)
        dim = G.shape[0]
        rank = int(np.linalg.matrix_rank(G))

        check(f"n{n}_form_is_singular",
              rank < dim,
              f"rank {rank} of {dim} (corank {dim - rank}), "
              f"cond {np.linalg.cond(G):.2e}")

        # The rank is the count of partitions with at most two rows — the TL
        # structure of qou-8iru, reached here from the numerical rank instead.
        two_row = [p for p in _partitions(n) if len(p) <= 2]
        check(f"n{n}_rank_is_the_two_row_partition_count",
              rank == len(two_row),
              f"rank {rank} == |{{lambda |- {n} : rows <= 2}}| = {len(two_row)} "
              f"{two_row}")

        # THE POINT: the residual check does not detect the failure.
        Gi = np.linalg.inv(G)           # deliberately unguarded, to measure it
        resid = float(np.linalg.norm(G @ Gi - np.eye(dim)))
        big = float(np.max(np.abs(Gi)))
        check(f"n{n}_residual_check_is_deceptive",
              resid < 1e-9 and big > 1e10,
              f"max|G^-1| = {big:.3e} (garbage) yet ||G.G^-1 - I|| = {resid:.3g} "
              f"(looks perfect) — no consumer-side check would catch this")

        # And the guard now refuses rather than returning it.
        try:
            gram_inverse_n(n=n)
            check(f"n{n}_gram_inverse_n_refuses", False,
                  "RETURNED — the guard is not in place")
        except NotImplementedError as exc:
            check(f"n{n}_gram_inverse_n_refuses", True,
                  f"raises NotImplementedError naming rank {rank}/{dim}"
                  if str(rank) in str(exc) else "raises NotImplementedError")

    n_fail = sum(1 for _n, p, _d in _CHECKS if not p)
    print()
    print("=== general-n Gram inverse: refuses, and the residual cannot catch it ===")
    print(f"VERDICT: {len(_CHECKS) - n_fail}/{len(_CHECKS)} PASS. gram_inverse_n was the "
          f"unguarded general-n successor to the deleted pyhecke.gram.gram_inverse. "
          f"It now raises. The finding worth keeping is that a WARNING would have "
          f"been insufficient: numpy is silent and the residual rounds to ~0 (exactly "
          f"0 at n=4) on an inverse with 1e16 entries, so nothing downstream would "
          f"have noticed. Scope-(a); builds no quotient and wires nothing.")
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
