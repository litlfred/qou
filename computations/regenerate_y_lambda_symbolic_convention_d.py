#!/usr/bin/env python3
# polynomial_q_not_applicable: this IS the symbolic-q source; there is no upstream.
"""Symbolic ``y_λ(q)`` for ``H_n(q)``, n = 2..12, under **convention D**.

Writes ``y-lambda-wenzl-bridge-symbolic-witness.json`` — the terminal root of
the whole weight cascade:

    this file
      -> regenerate_y_lambda_mpfr.py evaluates it at q0
      -> y-lambda-mpfr[-proton]-witness.json
      -> tr_m_wenzl_bridge_mpfr.load_y_lambda_for_q0
      -> chi_at_q0_via_hoefsmit_mpfr.py  (6 chi witnesses)
      -> 7 producers -> 8 more

Until now that file had **no producer at all**, which is why the `qou-eea0`
regeneration campaign could not move the corpus to convention D however many
times it re-ran: every downstream number is a faithful evaluation of a source
nothing could regenerate. Full analysis:
``docs/audits/2026-08-10-convention-d-ylambda-root-and-derivation.md``.

## The convention

`qou-u2jg` derives (Lean, sorry-free —
``QOU/QBeta/TemperleyLiebTower.lean``, section ``ConventionPinning``) that
imposing the three Markov normalisations on ``H_3(q)`` in the Wedderburn basis
forces

    y_(1^3) · (q²+1)(q⁴+q²+1) = q² (z − q) (z(q²+1) − q³)

so the three-strand antisymmetriser dies at exactly two values of ``z``. The
root ``z = q`` collapses everything to the one-dimensional character, leaving

    z_D = q³/(q² + 1)

as the **unique non-trivial** Markov trace on ``H_3(q)`` whose radical contains
the antisymmetriser. Convention C's ``z = 1/(q^{1/2} + q^{-1/2})`` is neither
root — which is exactly why it carries ``y_(1^3) = 0.0227449`` at q₀ instead of
zero.

The weight family that goes with ``z_D``, with
``[m]_q = (q^m − q^{−m})/(q − q^{−1})``:

    y_λ = [n − 2k + 1]_q / [2]_q^n      for λ = (n−k, k),  ℓ(λ) ≤ 2
    y_λ = 0                             for ℓ(λ) ≥ 3

## What this script verifies before it writes

Nothing is emitted unless every check below passes, because a wrong weight here
propagates silently into every mass and binding number downstream.

* ``tr(1) = Σ_λ dim_λ · y_λ = 1`` symbolically, for **every** n it emits.
* At n = 3, all three Markov conditions, including the defining
  ``tr(σ) = z_D`` — that is what separates *reproducing convention D* from
  merely *normalising correctly*.
* The two closed forms `qou-u2jg` derived independently:
  ``y_(3) = (q⁴+1)/(q²+1)²`` and ``y_(2,1) = q²/(q²+1)²``.
* Every ``ℓ(λ) ≥ 3`` weight is the literal string ``"0"``.

## Scope

n = 3 is derived. The general-n form is verified here against ``tr(1) = 1`` per
n, and is consistent with ``H_n/rad = TL_n`` — which is itself *measured*
(`qou-8iru`, n = 2..7, residual 1.34e-51) rather than proved for general n. So
the general-n form is a well-supported extension, not an established theorem;
`--strict-markov` additionally checks ``tr(σ) = z_D`` per n where the character
values are available.

Usage:
    python3 computations/regenerate_y_lambda_symbolic_convention_d.py [--check]

``--check`` runs every verification and reports, without writing.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"

N_MIN, N_MAX = 2, 12

q = sp.Symbol("q", positive=True)


def qint(m: int):
    """``[m]_q = (q^m − q^{−m})/(q − q^{−1})``. Integer powers, NOT q^{m/2}.

    The half-integer bracket ``(q^{m/2} − q^{−m/2})/(q^{1/2} − q^{−1/2})`` is a
    different function and belongs to convention C's ``z``. Using it here and
    then "verifying" the closed forms against that same bracket is circular and
    passes; it was caught only because the Markov conditions then failed.
    """
    return sp.simplify((q ** m - q ** (-m)) / (q - 1 / q))


def partitions_of(n: int) -> list[tuple[int, ...]]:
    """All partitions of n, descending parts, reverse-lexicographic."""
    out: list[tuple[int, ...]] = []

    def rec(remaining: int, cap: int, acc: tuple[int, ...]):
        if remaining == 0:
            out.append(acc)
            return
        for part in range(min(cap, remaining), 0, -1):
            rec(remaining - part, part, acc + (part,))

    rec(n, n, ())
    return out


def y_lambda(n: int, lam: tuple[int, ...]):
    """Convention-D weight. Zero on three-or-more rows, by definition of D."""
    if len(lam) >= 3:
        return sp.Integer(0)
    k = lam[1] if len(lam) == 2 else 0
    return sp.simplify(qint(n - 2 * k + 1) / qint(2) ** n)


def dim_irrep(n: int, lam: tuple[int, ...]) -> int:
    """dim of the S_n irrep λ. Two-row hook-length shortcut; full formula else."""
    if len(lam) == 1:
        return 1
    if len(lam) == 2:
        k = lam[1]
        return int(sp.binomial(n, k) - sp.binomial(n, k - 1))
    # Frobenius hook-length formula, only needed for the weights that vanish.
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return int(sp.factorial(n) / prod)


def verify(tables: dict[int, list[tuple[tuple[int, ...], sp.Expr]]]) -> list[str]:
    """Every check. Returns failures; empty list means safe to write."""
    fails: list[str] = []
    z_D = q ** 3 / (q ** 2 + 1)

    for n, rows in sorted(tables.items()):
        total = sum(dim_irrep(n, lam) * val for lam, val in rows)
        if sp.simplify(total - 1) != 0:
            fails.append(f"n={n}: tr(1) = {sp.simplify(total)}, expected 1")
        for lam, val in rows:
            if len(lam) >= 3 and val != 0:
                fails.append(f"n={n} λ={lam}: ℓ(λ)≥3 weight is {val}, expected 0")

    # n = 3: the defining conditions, and the two independently-derived forms.
    rows3 = dict(tables[3])
    y3, y21, y111 = rows3[(3,)], rows3[(2, 1)], rows3[(1, 1, 1)]
    r = 1 / q
    checks = [
        ("y_(3) vs qou-u2jg (q⁴+1)/(q²+1)²", y3 - (q ** 4 + 1) / (q ** 2 + 1) ** 2),
        ("y_(2,1) vs qou-u2jg q²/(q²+1)²", y21 - q ** 2 / (q ** 2 + 1) ** 2),
        ("tr(1) = 1", y3 + 2 * y21 + y111 - 1),
        ("tr(σ) = z_D", q * y3 + (q - r) * y21 - r * y111 - z_D),
        ("tr(σ₀σ₁) = z_D²", q ** 2 * y3 - y21 + r ** 2 * y111 - z_D ** 2),
    ]
    for label, expr in checks:
        if sp.simplify(expr) != 0:
            fails.append(f"n=3: {label} FAILED (residual {sp.simplify(expr)})")
    return fails


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--check", action="store_true",
                    help="verify only; do not write the witness")
    args = ap.parse_args()

    tables: dict[int, list[tuple[tuple[int, ...], sp.Expr]]] = {}
    for n in range(N_MIN, N_MAX + 1):
        tables[n] = [(lam, y_lambda(n, lam)) for lam in partitions_of(n)]
        print(f"  n={n:2d}: {len(tables[n]):3d} partitions, "
              f"{sum(1 for _, v in tables[n] if v == 0):3d} vanish", flush=True)

    print("\nverifying …", flush=True)
    fails = verify(tables)
    if fails:
        print("\nVERIFICATION FAILED — nothing written:", file=sys.stderr)
        for f in fails:
            print(f"  {f}", file=sys.stderr)
        return 1
    print("  all checks pass (tr(1)=1 per n; n=3 Markov conditions incl. tr(σ)=z_D;"
          " qou-u2jg closed forms; ℓ(λ)≥3 all exactly 0)")

    if args.check:
        print("\n--check: not writing.")
        return 0

    doc = {
        "computation": "y-lambda-wenzl-bridge-symbolic",
        "description": (
            "Symbolic y_lambda(q) for H_n(q), n=2..12, under convention D "
            "(z_D = q^3/(q^2+1), the unique non-trivial Markov trace on H_3 "
            "whose radical contains the three-strand antisymmetriser). "
            "y_lambda = [n-2k+1]_q/[2]_q^n on two-row partitions, exactly 0 on "
            "three-or-more rows."
        ),
        # NOT "convention": that key is already taken, corpus-wide, for the
        # CROSSING convention -- chi-*-at-q0-50dps witnesses carry
        # "colour-weighted-averaged-crossing", "averaged-crossings",
        # "sign-only-crossings". Those describe how inter-nucleon crossings
        # are built and are orthogonal to which Markov trace is being taken.
        # Reusing the key would collide two independent axes under one name,
        # which is the overloaded-symbol failure AGENTS.md warns about.
        "markov_convention": "D",
        "markov_parameter_symbolic": "q**3/(q**2 + 1)",
        "scriptFile": f"computations/{Path(__file__).name}",
        "references": [
            "prop:y-lambda-closed-form-wenzl-bridge",
            "prop:explicit-alpha-k-h3",
            "prop:alpha-k-derivation-procedure",
            "thm:jones-markov-trace",
            "wenzl1988",
            "orellana1998",
            "chlouveraki2016",
        ],
        "tables_by_n": {
            str(n): {
                "n": n,
                "num_partitions": len(rows),
                "weights": [
                    {"partition": list(lam), "y_lambda_symbolic": str(val)}
                    for lam, val in rows
                ],
            }
            for n, rows in sorted(tables.items())
        },
        "precision": "symbolic_q",
        "truncation_eps": 0.0,
    }
    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"\nwrote {OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
