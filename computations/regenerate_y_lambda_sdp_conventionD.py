#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical evaluation of a closed form at q_0; the
# convention-D weights come from the Lean pinning in QOU/QBeta/TemperleyLiebTower.
"""Bring `y-lambda-sdp-witness.json` to convention D.

The last `y_λ` orphan. It records, per `n ∈ 2..6`, the weights as a **positional**
list `y_ls` with no partition labels, together with the feasibility question it
was built to answer: does the Frobenius system admit a *non-negative* solution?

## The pairing is proved, not assumed

`y_ls` carries no partition labels, so the descending-lex reading has to be
earned before anything is rewritten. The gate is

    Σ_λ dim_λ · y_λ = 1        (tr(1) = 1)

evaluated on the **stored** convention-C values against descending-lex dims.
This is order-sensitive — the dimensions differ per partition, so a wrong
pairing misses 1 — and it is a property of any Markov trace, so it holds for
the file as it stands. If it fails, the pairing is wrong and nothing is
written.

## What the file was measuring, and what happens to it

Convention C **violates** the non-negativity it was checking: `n = 4, 5, 6` each
carry negative weights (`positivity_holds: false`, down to `-8.4e-4`). Under
convention D the question resolves exactly, and in the affirmative:

    y_λ = [n − 2k + 1]_q / [2]_q^n > 0     ℓ(λ) ≤ 2   (n − 2k + 1 ≥ 1)
    y_λ = 0                                ℓ(λ) ≥ 3

Every surviving weight is strictly positive and every other is exactly zero, so
`y ≥ 0` holds at every `n` with no slack and no tolerance. The C-era violators
are precisely partitions that D sends to zero.

## Dropped fields

`ls_status`, `ls_residual` and `cross_check` are diagnostics of a cvxpy solve
and a linear solve — neither of which happens here. Carrying them forward would
be a residual reported for a computation that was not run. They are removed
rather than restated; `min_y_lambda`, `max_y_lambda`, `positivity_holds` and
`positivity_violators` are properties of the weights themselves and are
recomputed.

## Anchor

The file's own `q` is kept per table (the muon/ideal pin it was built at), so
only the convention moves — AGENTS.md §"q₀ anchor convention", never straddle.

Usage:
    python3 computations/regenerate_y_lambda_sdp_conventionD.py [--check]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
TARGET = HERE / "y-lambda-sdp-witness.json"
DPS = 50


def partitions_desc(n: int) -> list[tuple[int, ...]]:
    """Partitions of n in descending lexicographic order."""
    out: list[tuple[int, ...]] = []

    def rec(rest: int, cap: int, acc: list[int]) -> None:
        if rest == 0:
            out.append(tuple(acc))
            return
        for part in range(min(cap, rest), 0, -1):
            rec(rest - part, part, acc + [part])

    rec(n, n, [])
    return out


def dim_irrep(n: int, lam: tuple[int, ...]) -> int:
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return int(sp.factorial(n) / prod)


def qint(q, m: int):
    return (q ** m - q ** (-m)) / (q - 1 / q)


def y_lambda(q, n: int, lam: tuple[int, ...]):
    if len(lam) >= 3:
        return mp.mpf(0)
    k = lam[1] if len(lam) == 2 else 0
    return qint(q, n - 2 * k + 1) / qint(q, 2) ** n


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--check", action="store_true", help="verify without writing")
    args = ap.parse_args()
    mp.mp.dps = DPS

    doc = json.loads(TARGET.read_text())
    tables = doc["tables_by_n"]

    # Gate 1 -- the pairing. tr(1) = 1 on the STORED convention-C weights.
    for key, tab in sorted(tables.items(), key=lambda kv: int(kv[0])):
        n = int(tab["n"])
        parts = partitions_desc(n)
        ys = tab["y_ls"]
        if len(parts) != len(ys):
            print(f"FAIL n={n}: {len(ys)} weights vs {len(parts)} partitions",
                  file=sys.stderr)
            return 1
        tr1 = sum(dim_irrep(n, lam) * mp.mpf(str(y)) for lam, y in zip(parts, ys))
        if abs(tr1 - 1) > mp.mpf("1e-12"):
            print(f"FAIL n={n}: descending-lex pairing gives tr(1) = "
                  f"{mp.nstr(tr1, 18)}, not 1 -- pairing unproved, refusing",
                  file=sys.stderr)
            return 1
        print(f"  pairing n={n}: tr(1) = {mp.nstr(tr1, 18)} on stored C weights  OK")

    # Rewrite.
    for key, tab in sorted(tables.items(), key=lambda kv: int(kv[0])):
        n = int(tab["n"])
        q = mp.mpf(str(tab["q"]))
        parts = partitions_desc(n)
        ys = [y_lambda(q, n, lam) for lam in parts]

        tr1 = sum(dim_irrep(n, lam) * y for lam, y in zip(parts, ys))
        if abs(tr1 - 1) > mp.mpf(10) ** (-(DPS - 6)):
            print(f"FAIL n={n}: convention-D tr(1) = {mp.nstr(tr1, 20)}",
                  file=sys.stderr)
            return 1
        for lam, y in zip(parts, ys):
            if len(lam) >= 3 and y != 0:
                print(f"FAIL n={n} λ={lam}: depth≥2 weight {y} != 0", file=sys.stderr)
                return 1

        violators = [{"index": i, "y_lambda": float(y)}
                     for i, y in enumerate(ys) if y < 0]
        tab["y_ls"] = [float(y) for y in ys]
        tab["z"] = float(q ** 3 / (q ** 2 + 1))
        tab["min_y_lambda"] = float(min(ys))
        tab["max_y_lambda"] = float(max(ys))
        tab["positivity_holds"] = not violators
        tab["positivity_violators"] = violators
        tab["n_support"] = sum(1 for y in ys if y != 0)
        for stale in ("ls_status", "ls_residual", "cross_check"):
            tab.pop(stale, None)

        print(f"  n={n}: {len(ys)} weights, support {tab['n_support']}, "
              f"min {tab['min_y_lambda']:.6g}, positivity "
              f"{'holds' if tab['positivity_holds'] else 'VIOLATED'}")

    doc["description"] = (
        "Ocneanu weights y_λ at the convention-D Markov parameter z = q³/(q²+1), "
        "with the non-negativity question the convention-C version of this "
        "witness was built to test. Under C it failed at n = 4, 5, 6; under D "
        "every ℓ(λ) ≤ 2 weight is strictly positive and every ℓ(λ) ≥ 3 weight is "
        "exactly zero, so y ≥ 0 holds at each n with no tolerance. Weights are "
        "listed in descending lexicographic partition order; the pairing is "
        "verified by tr(1) = Σ dim_λ y_λ = 1 before rewriting."
    )
    doc["markov_convention"] = "D"
    doc["markov_parameter_symbolic"] = "q**3/(q**2 + 1)"
    doc["scriptFile"] = f"computations/{Path(__file__).name}"
    doc["partition_order"] = "descending-lex"

    if args.check:
        print("\n--check: nothing written.")
    else:
        TARGET.write_text(json.dumps(doc, indent=2) + "\n")
        print(f"\nwrote {TARGET.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
