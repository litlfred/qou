#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical evaluation at q_0 of a closed form whose
# symbolic source is y-lambda-wenzl-bridge-symbolic-witness.json.
"""Regenerate ``y-lambda-jones-markov-witness.json`` under **convention D**.

The witness carries Jones–Markov block weights ``y_λ`` at ``H_n(q₀)`` for
``n = 2 … 12`` and is read by live consumers, so it cannot simply be retired
with its producer (which sits in ``_deprecated/``):

| consumer | kind |
|---|---|
| ``binding_a3plus_joint_ji_combiner.py:112`` (``["tables_by_n"]``) | live producer |
| ``mass-theory/alpha-k-derivation-procedure-proof.md`` | content block |
| ``mass-theory/wedderburn-bratteli-recursion.lean`` | content block sibling |
| ``mass-theory/wedderburn-bratteli-recursion-proof.md`` | content block |

## What changes

The retired producer solved a linear system — ``tr_M(w_μ) = z^{n−ℓ(μ)}`` over
cycle-type representatives — at convention C's ``z = 1/(q^{1/2}+q^{-1/2})``.
Convention D fixes ``z_D = q³/(q²+1)`` (`qou-u2jg`, Lean, sorry-free), and at
that ``z`` the weights have a closed form, so there is no system to solve:

    y_λ = [n − 2k + 1]_q / [2]_q^n      for λ = (n−k, k),  ℓ(λ) ≤ 2
    y_λ = 0                             for ℓ(λ) ≥ 3

In this witness's own vocabulary — it labels each partition with
``depth = ℓ(λ) − 1``, verified against the committed n=3 and n=4 tables — that
second line reads **``y_λ = 0`` exactly when ``depth ≥ 2``**.

Two consequences worth seeing in the diff:

* n=3 currently holds ``0.415396 / 0.280930 / 0.022745`` — the three registry
  convention-C fingerprints, verbatim.
* n=4 currently holds ``y_(1,1,1,1) = −0.000843``, a **negative** Markov weight.
  Convention D sends it to exactly ``0``.

## Fields

``crt_probes`` and ``diagnostics`` are **dropped**. They recorded
``condition_number`` and ``linear_system_residual`` — diagnostics of the linear
solve that convention D removes. Carrying them forward would describe a
computation that no longer happens. The verification this producer *does* run is
recorded instead, under ``verification``.

## Anchor: proton (re-pinned 2026-11-20)

Until 2026-11-20 this producer held the **muon** ``q₀ = 1.1099785955541805``
(CODATA 2018) fixed, so that the convention-D migration moved one axis at a
time. That left a layer straddle: the live consumer
``binding_a3plus_joint_ji_combiner.py`` pins ``q₀`` from
``q_parameter.Q_50_DIGIT_STR`` (proton, ``physical_proton`` in the manifest)
while reading these weights at the muon value. On owner instruction
(bean ``qou-w8cg``) the producer now takes ``q₀`` from the same
``q_parameter.Q_50_DIGIT_STR``, so the two layers agree by construction.
Values are serialised as ``_precision.fmt`` strings, not ``float``.

Usage:
    python3 computations/regenerate_y_lambda_jones_markov_conventionD.py [--check]
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE_DIR = Path(__file__).resolve().parent
if str(HERE_DIR) not in sys.path:
    sys.path.insert(0, str(HERE_DIR))
import _path_bridge  # noqa: F401, E402
from _precision import fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

HERE = Path(__file__).resolve().parent
OUT = HERE / "y-lambda-jones-markov-witness.json"

N_MIN, N_MAX = 2, 12
DPS = 50

#: Proton-pinned q₀, the same string the consumer reads (see module docstring).
Q0_STR = Q_50_DIGIT_STR


def qint(q, m: int):
    """``[m]_q = (q^m − q^{−m})/(q − q^{−1})``, integer powers."""
    return (q ** m - q ** (-m)) / (q - 1 / q)


def partitions_of(n: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []

    def rec(rem: int, cap: int, acc: tuple[int, ...]):
        if rem == 0:
            out.append(acc)
            return
        for part in range(min(cap, rem), 0, -1):
            rec(rem - part, part, acc + (part,))

    rec(n, n, ())
    return out


def y_lambda(q, n: int, lam: tuple[int, ...]):
    """Convention-D weight. Exactly zero once the shape has three rows."""
    if len(lam) >= 3:
        return mp.mpf(0)
    k = lam[1] if len(lam) == 2 else 0
    return qint(q, n - 2 * k + 1) / qint(q, 2) ** n


def dim_irrep(n: int, lam: tuple[int, ...]) -> int:
    """dim of the S_n irrep λ, for the normalisation check."""
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return int(mp.factorial(n) / prod)


def build(q):
    """{n: [(partition, depth, y_λ)]} plus the per-n verification."""
    tables, checks = {}, {}
    z_D = q ** 3 / (q ** 2 + 1)
    for n in range(N_MIN, N_MAX + 1):
        rows = [(lam, len(lam) - 1, y_lambda(q, n, lam)) for lam in partitions_of(n)]
        tables[n] = rows
        # tr(1) = Σ_λ dim_λ · y_λ = 1. One scalar per n — it cannot separate the
        # individual weights, which is why the n=3 identities below matter too.
        total = sum(dim_irrep(n, lam) * y for lam, _, y in rows)
        checks[n] = total
    return tables, checks, z_D


def verify(tables, checks, q, z_D) -> list[str]:
    fails = []
    tol = mp.mpf(10) ** (-(DPS - 6))
    for n, total in sorted(checks.items()):
        if abs(total - 1) > tol:
            fails.append(f"n={n}: tr(1) = {mp.nstr(total, 20)}, expected 1")
    for n, rows in tables.items():
        for lam, depth, y in rows:
            if depth >= 2 and y != 0:
                fails.append(f"n={n} λ={lam}: depth {depth} weight is {y}, expected 0")
    # n=3, the defining Markov conditions — this is what distinguishes
    # reproducing convention D from merely normalising to 1.
    r3 = {lam: y for lam, _, y in tables[3]}
    y3, y21, y111 = r3[(3,)], r3[(2, 1)], r3[(1, 1, 1)]
    r = 1 / q
    for label, got, want in (
        ("tr(1)", y3 + 2 * y21 + y111, mp.mpf(1)),
        ("tr(σ)", q * y3 + (q - r) * y21 - r * y111, z_D),
        ("tr(σ₀σ₁)", q ** 2 * y3 - y21 + r ** 2 * y111, z_D ** 2),
    ):
        if abs(got - want) > tol:
            fails.append(f"n=3 {label}: {mp.nstr(got, 20)} != {mp.nstr(want, 20)}")
    return fails


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--check", action="store_true", help="verify without writing")
    args = ap.parse_args()

    mp.mp.dps = DPS
    q = mp.mpf(Q0_STR)
    tables, checks, z_D = build(q)
    for n in sorted(tables):
        vanish = sum(1 for _, d, _ in tables[n] if d >= 2)
        print(f"  n={n:2d}: {len(tables[n]):3d} partitions, {vanish:3d} at depth>=2 -> 0",
              flush=True)

    fails = verify(tables, checks, q, z_D)
    if fails:
        print("\nVERIFICATION FAILED — nothing written:", file=sys.stderr)
        for f in fails:
            print(f"  {f}", file=sys.stderr)
        return 1
    print(f"\n  z_D = {mp.nstr(z_D, 20)}")
    print("  verified: tr(1)=1 per n; depth>=2 all exactly 0; "
          "n=3 Markov conditions incl. tr(σ)=z_D")

    if args.check:
        print("\n--check: not writing.")
        return 0

    doc = {
        "description": (
            "Jones-Markov block weights y_λ at H_n(q₀) for n = 2..12, "
            "CONVENTION D (z_D = q^3/(q^2+1), the unique non-trivial Markov "
            "trace on H_3 whose radical contains the three-strand "
            "antisymmetriser). Closed form y_λ = [n-2k+1]_q/[2]_q^n on two-row "
            "shapes, exactly 0 at depth >= 2. Replaces the convention-C linear "
            "solve whose producer is in _deprecated/."
        ),
        "markov_convention": "D",
        "markov_parameter_symbolic": "q**3/(q**2 + 1)",
        "scriptFile": f"computations/{Path(__file__).name}",
        "references": [
            "prop:y-lambda-closed-form-wenzl-bridge",
            "thm:jones-markov-trace",
            "wenzl1988",
        ],
        "q0Anchor": "proton",
        "q0Layer": "experimental / Physical-Observations",
        "q0Value": Q0_STR,
        "dps": DPS,
        "tables_by_n": {
            str(n): {
                "n": n,
                "num_partitions": len(rows),
                "q_0": fmt(q),
                "z_markov": fmt(z_D),
                "weights": [
                    {"partition": list(lam), "depth": depth,
                     "y_lambda": fmt(y)}
                    for lam, depth, y in rows
                ],
            }
            for n, rows in sorted(tables.items())
        },
        "verification": {
            "normalisation_per_n": "tr(1) = sum_lambda dim_lambda * y_lambda = 1",
            "depth_ge_2_vanishes": True,
            "n3_markov_conditions": ["tr(1)=1", "tr(sigma)=z_D", "tr(s0s1)=z_D^2"],
        },
        "computedAt": datetime.now(timezone.utc).isoformat(),
    }
    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"\nwrote {OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
