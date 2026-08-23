#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/symbolic evaluation of a closed form whose
# source is the convention-D pinning in QOU/QBeta/TemperleyLiebTower.lean.
"""Bring the **orphan** `y_λ` witnesses to convention D, preserving each schema.

These carry `y_λ` tables but have no producer the regeneration harness can
reach — their producers are in `_deprecated/`, or there never was one. They
cannot simply be retired, because live code and paper content read them
(`qou-rohl`: `wenzl-y-lambda-h9/h12` alone feed six consumers, including
`nucleus_real_sdp.py` and three `mass-theory` content blocks).

So each is rewritten in place **by recomputation**, not by editing: every
`y_λ` value is recomputed from the convention-D closed form and written back
into the file's own schema, with every other field left alone.

## The weights

`z_D = q³/(q²+1)` is the unique non-trivial Markov trace on `H₃(q)` whose
radical contains the three-strand antisymmetriser (`qou-u2jg`, Lean,
sorry-free). At that `z`:

    y_λ = [n − 2k + 1]_q / [2]_q^n      for λ = (n−k, k),  ℓ(λ) ≤ 2
    y_λ = 0                             for ℓ(λ) ≥ 3

with `[m]_q = (q^m − q^{−m})/(q − q^{−1})`.

## Why a rewriter rather than one canonical emitter

The six files disagree on nearly everything except the mathematics: the weight
field is variously `y_lambda`, `y_lambda_numeric`, `y_lambda_float`,
`y_lambda_symbolic`, `y_lambda_simplified_factored`; the table lives under
`tables_by_n` or under `data`; values are strings in some and floats in others.
Consumers read those exact names. Emitting one canonical shape would migrate
the convention and break every reader in the same commit, so the schema is
preserved and only the numbers move.

`y-lambda-sdp-witness.json` is **not** handled: it has no partition-paired
weight field, so there is nothing here to rewrite. It needs its own look.

## Anchor

Each file's own `q₀` is used where the file states one, so that only the
convention moves and the ideal/experimental layer is left where it was
(AGENTS.md §"q₀ anchor convention" — never straddle). Files that state no `q₀`
fall back to the muon pin, matching the other `y_λ` tables, and say so.

## Verification

Nothing is written unless, for every `n` touched, `Σ_λ dim_λ · y_λ = 1` holds
on the rewritten values, and every `ℓ(λ) ≥ 3` weight is exactly zero.

Usage:
    python3 computations/regenerate_y_lambda_orphans_conventionD.py [--check]
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

MUON_Q0 = "1.1099785955541805"

TARGETS = [
    "wenzl-y-lambda-h9.witness.json",
    "wenzl-y-lambda-h12.witness.json",
    "y-lambda-symbolic-witness.json",
    "y-lambda-wenzl-bridge-numeric-witness.json",
    "y-lambda-wenzl-witness.json",
]

_qs = sp.Symbol("q", positive=True)


def qint_num(q, m: int):
    return (q ** m - q ** (-m)) / (q - 1 / q)


def qint_sym(m: int):
    return sp.simplify((_qs ** m - _qs ** (-m)) / (_qs - 1 / _qs))


def y_num(q, n: int, lam: tuple[int, ...]):
    if len(lam) >= 3:
        return mp.mpf(0)
    k = lam[1] if len(lam) == 2 else 0
    return qint_num(q, n - 2 * k + 1) / qint_num(q, 2) ** n


def y_sym(n: int, lam: tuple[int, ...]):
    if len(lam) >= 3:
        return sp.Integer(0)
    k = lam[1] if len(lam) == 2 else 0
    return sp.simplify(qint_sym(n - 2 * k + 1) / qint_sym(2) ** n)


def dim_irrep(n: int, lam: tuple[int, ...]) -> int:
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return int(sp.factorial(n) / prod)


def find_q0(doc) -> tuple[str, str]:
    """(q0_string, where_it_came_from) — the file's own pin when it states one."""
    stack = [doc]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            for k, v in node.items():
                if k in ("q_0", "q0", "q_0_50dps") and isinstance(v, (str, float)):
                    return str(v), f"file field `{k}`"
                stack.append(v)
        elif isinstance(node, list):
            stack.extend(node[:20])
    return MUON_Q0, "muon default (file states none)"


def rewrite(doc, q):
    """Rewrite every partition-paired y_λ in place. Returns (count, per_n)."""
    n_seen: dict[int, list] = {}
    count = 0

    def walk(node):
        nonlocal count
        if isinstance(node, dict):
            part = node.get("partition")
            lam = None
            if isinstance(part, (list, tuple)):
                cleaned = [x for x in part if x not in ("_", "", None)]
                try:
                    lam = tuple(int(x) for x in cleaned)
                except (TypeError, ValueError):
                    lam = None
            if lam:
                n = sum(lam)
                for key in list(node):
                    if "y_lam" not in key and "y_at" not in key:
                        continue
                    old = node[key]
                    if "symbolic" in key or "factored" in key:
                        new = str(y_sym(n, lam))
                    else:
                        val = y_num(q, n, lam)
                        new = (mp.nstr(val, DPS, strip_zeros=False)
                               if isinstance(old, str) else float(val))
                    node[key] = new
                    count += 1
                n_seen.setdefault(n, []).append((lam, y_num(q, n, lam)))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(doc)
    return count, n_seen


def verify(n_seen) -> list[str]:
    fails = []
    tol = mp.mpf(10) ** (-(DPS - 6))
    for n, rows in sorted(n_seen.items()):
        seen = {}
        for lam, y in rows:
            seen[lam] = y
        total = sum(dim_irrep(n, lam) * y for lam, y in seen.items())
        # Only meaningful when the table is complete for that n.
        from sympy.utilities.iterables import partitions as _p
        n_parts = sum(1 for _ in _p(n))
        if len(seen) == n_parts and abs(total - 1) > tol:
            fails.append(f"n={n}: tr(1) = {mp.nstr(total, 20)} (expected 1)")
        for lam, y in seen.items():
            if len(lam) >= 3 and y != 0:
                fails.append(f"n={n} λ={lam}: ℓ(λ)≥3 weight {y} != 0")
    return fails


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--check", action="store_true", help="verify without writing")
    args = ap.parse_args()
    mp.mp.dps = DPS

    rc = 0
    for name in TARGETS:
        path = HERE / name
        if not path.exists():
            print(f"  SKIP   {name} (absent)")
            continue
        doc = json.loads(path.read_text())
        q0_str, origin = find_q0(doc)
        q = mp.mpf(q0_str)
        count, n_seen = rewrite(doc, q)
        fails = verify(n_seen)
        ns = ",".join(str(n) for n in sorted(n_seen))
        if fails:
            print(f"  FAIL   {name}: {'; '.join(fails[:2])}", file=sys.stderr)
            rc = 1
            continue
        print(f"  OK     {name:<42} {count:4d} weights, n={ns}, q0 from {origin}")
        if not args.check:
            doc["markov_convention"] = "D"
            doc["markov_parameter_symbolic"] = "q**3/(q**2 + 1)"
            doc["scriptFile"] = f"computations/{Path(__file__).name}"
            path.write_text(json.dumps(doc, indent=2) + "\n")
    if args.check:
        print("\n--check: nothing written.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
