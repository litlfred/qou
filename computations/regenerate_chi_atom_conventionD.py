#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical evaluation at q_0; the chi values are
# read from the witness and are convention-independent.
"""Bring the producerless `chi-*-h6` atom witnesses to convention D, consistently.

`chi-dineutron-h6-at-q0-50dps` and `chi-diproton-h6-at-q0-50dps` record, per
partition `λ ⊢ 6`:

    partition, dim, y_lambda, chi_lambda, contribution   with   tr_M_at_q0 = Σ contribution

They have **no producer**: unlike their six siblings they are not in
`chi_at_q0_via_hoefsmit_mpfr`'s `ATOMS` (which has no dineutron `(0,2)` or
diproton `(2,0)` entry), and nothing else writes them. So they cannot be
regenerated, only re-derived in place.

## Why this is safe to do from the file itself

`χ^λ_q(β)` is a **character** — a trace of a representation matrix. It does not
depend on the Markov parameter `z`, so the convention change leaves every
`chi_lambda` in these files untouched and correct. Only the weights move:

    y_λ = [n − 2k + 1]_q / [2]_q^n      ℓ(λ) ≤ 2        (z_D = q³/(q²+1))
    y_λ = 0                             ℓ(λ) ≥ 3

## The consistency that matters

Rewriting `y_lambda` alone would leave `contribution` and `tr_M_at_q0` stale —
a file internally disagreeing with itself, which is worse than one that is
uniformly convention C. All three move together:

    contribution  = y_λ(D) · χ_λ        (χ from the file, unchanged)
    tr_M_at_q0    = Σ_λ contribution

and the result is checked against `Σ_λ dim_λ · y_λ = 1` before anything is
written. Only complete tables are eligible: a `partial` witness would give a
partial sum and a `tr_M` that is not the trace of anything.

Usage:
    python3 computations/regenerate_chi_atom_conventionD.py [--check]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
DPS = 50

TARGETS = [
    "chi-dineutron-h6-at-q0-50dps.witness.json",
    "chi-diproton-h6-at-q0-50dps.witness.json",
]


def qint(q, m: int):
    return (q ** m - q ** (-m)) / (q - 1 / q)


def y_lambda(q, n: int, lam: tuple[int, ...]):
    if len(lam) >= 3:
        return mp.mpf(0)
    k = lam[1] if len(lam) == 2 else 0
    return qint(q, n - 2 * k + 1) / qint(q, 2) ** n


def dim_irrep(n: int, lam: tuple[int, ...]) -> int:
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return int(sp.factorial(n) / prod)


def process(path: Path, write: bool) -> tuple[bool, str]:
    doc = json.loads(path.read_text())
    rows = doc.get("by_partition")
    if not rows:
        return False, "no by_partition"
    if doc.get("partial"):
        return False, "partial table — a partial sum is not a trace"
    n = int(doc.get("n_strands") or sum(rows[0]["partition"]))
    q = mp.mpf(str(doc["q_0_50dps"]))

    total = mp.mpf(0)
    norm = mp.mpf(0)
    for e in rows:
        lam = tuple(int(x) for x in e["partition"])
        y = y_lambda(q, n, lam)
        chi = mp.mpf(str(e["chi_lambda"]))
        contrib = y * chi
        e["y_lambda"] = mp.nstr(y, DPS, strip_zeros=False)
        e["contribution"] = mp.nstr(contrib, DPS, strip_zeros=False)
        total += contrib
        norm += dim_irrep(n, lam) * y

    tol = mp.mpf(10) ** (-(DPS - 6))
    if abs(norm - 1) > tol:
        return False, f"tr(1) = {mp.nstr(norm, 20)} != 1"
    for e in rows:
        lam = tuple(int(x) for x in e["partition"])
        if len(lam) >= 3 and mp.mpf(str(e["y_lambda"])) != 0:
            return False, f"λ={lam} nonzero at depth≥2"

    doc["tr_M_at_q0"] = mp.nstr(total, DPS, strip_zeros=False)
    doc["markov_convention"] = "D"
    doc["markov_parameter_symbolic"] = "q**3/(q**2 + 1)"
    doc["scriptFile"] = f"computations/{Path(__file__).name}"
    if write:
        path.write_text(json.dumps(doc, indent=2) + "\n")
    return True, f"n={n}, {len(rows)} λ, tr_M -> {mp.nstr(total, 12)}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--check", action="store_true", help="verify without writing")
    args = ap.parse_args()
    mp.mp.dps = DPS
    rc = 0
    for name in TARGETS:
        p = HERE / name
        if not p.exists():
            print(f"  SKIP {name} (absent)")
            continue
        ok, msg = process(p, write=not args.check)
        print(f"  {'OK  ' if ok else 'FAIL'} {name:<44} {msg}")
        if not ok:
            rc = 1
    if args.check:
        print("\n--check: nothing written.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
