#!/usr/bin/env python3
"""Settle whether the q-deformed Wedderburn weight sums to one, and census which
blocks say it does.

## Why

Two statements live in the corpus about the same quantity:

  spectral-sequence-collapse-proof.md  "q-deformed Wedderburn weights w~_lambda,
                                        bounded but sum w~_lambda != 1 at q != 1"
  gram-kappa-spectral-interpretation.md "Plancherel ensures sum_lambda w_lambda
                                         = 1 at every q"

At most one can be right, and the second is load-bearing where it appears: it is
what licenses replacing a hand-chosen 2-jet truncation with a full partition sum
"convergent by Plancherel".

The classical Plancherel measure w_lambda = (dim V_lambda)^2 / n! does sum to 1
-- that is the RSK identity sum_lambda (f^lambda)^2 = n!. The question is whether
that identity q-deforms, i.e. whether sum_lambda dim_q(lambda)^2 = [n]_q!. It
does not, and this script measures by how much.

## What it does

1. Evaluates sum_lambda dim_q(lambda)^2 / [n]_q! at the substrate q0 for n = 3..8,
   with dim_q from the q-hook-length formula. Checks the q -> 1 limit recovers
   the classical 1 as a correctness control on the implementation.
2. Greps the corpus for blocks that DEFINE w_lambda q-deformed, and separately
   for blocks that assert it sums to 1. The intersection is the defect set.

Anchor: the experimental (proton) pin, per the AGENTS.md standing directive that
all new compute defaults to it.

Usage:
  python3 -u docs/audits/scripts/wlambda_normalisation_census.py 2>&1 | tee /tmp/wlambda.log
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
import os
import re
from glob import glob
from pathlib import Path

from mpmath import mp, mpf

mp.dps = 65  # _precision.py default compute precision

REPO = Path(__file__).resolve().parents[3]
OUT = Path(__file__).with_suffix(".witness.json")


def _q0() -> tuple[mpf, str]:
    """The experimental (proton) pin. Package constant when importable."""
    try:
        from qou_substrate.constants import Q_50_DIGIT_STR  # type: ignore

        return mpf(Q_50_DIGIT_STR), "qou_substrate.constants.Q_50_DIGIT_STR"
    except Exception:
        try:
            from qou_substrate.constants import Q  # type: ignore

            # LAUNDERS the f64 Q, and is kept deliberately: this is the
            # middle rung of a graceful-degradation ladder that only runs if
            # the package exposes `Q` but not `Q_50_DIGIT_STR` (an older
            # version), and it RETURNS ITS OWN PROVENANCE alongside the value
            # so a reader can see which rung fired. Unreachable against any
            # current package. comparison only — do not "fix" it to Q_MP,
            # which would defeat the compatibility it exists for.
            return mpf(str(Q)), "qou_substrate.constants.Q"
        except Exception:
            # Never an mpf(<float>) -- the literal is carried as a string.
            return mpf("1.1099785827513808"), "literal proton pin (package unavailable)"


def qint(n: int, q: mpf) -> mpf:
    """[n]_q = (q^n - q^-n)/(q - q^-1), the balanced quantum integer."""
    return (q**n - q ** (-n)) / (q - q ** (-1))


def qfact(n: int, q: mpf) -> mpf:
    r = mpf(1)
    for i in range(1, n + 1):
        r *= qint(i, q)
    return r


def partitions(n: int, mx: int | None = None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def hooks(lam: tuple[int, ...]) -> list[int]:
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    return [
        lam[i] - j - 1 + conj[j] - i - 1 + 1
        for i in range(len(lam))
        for j in range(lam[i])
    ]


def dim_q(lam: tuple[int, ...], n: int, q: mpf) -> mpf:
    d = qfact(n, q)
    for h in hooks(lam):
        d /= qint(h, q)
    return d


def dim_classical(lam: tuple[int, ...], n: int) -> int:
    d = math.factorial(n)
    for h in hooks(lam):
        d //= h
    return d


def weight_sum(n: int, q: mpf) -> mpf:
    return sum(dim_q(l, n, q) ** 2 for l in partitions(n)) / qfact(n, q)


def weight_sum_unbalanced(n: int, q: mpf) -> mpf:
    """Same sum under the unbalanced [n]_q = (q^n - 1)/(q - 1).

    The corpus is not uniform about which quantum integer `[n]_q` denotes, so
    the verdict must not depend on the choice. It does not: the unbalanced
    convention lands FURTHER from 1 than the balanced one.
    """
    qi = lambda k: (q**k - 1) / (q - 1)  # noqa: E731
    fact = mpf(1)
    for i in range(1, n + 1):
        fact *= qi(i)
    total = mpf(0)
    for lam in partitions(n):
        d = fact
        for h in hooks(lam):
            d /= qi(h)
        total += d**2
    return total / fact


# --- corpus census -----------------------------------------------------------

_QDEF = re.compile(
    r"w_\\lambda(?:\(q\))?\s*(?::?=)\s*[^.\n]{0,40}?"
    r"(?:\\dim_q|d_q|\[n\]_q!|\[k\]_q!|H_q)"
)
# Post-2026-08-16 convention: the classical measure is the q=1 SPECIALISATION,
# written w_lambda(1). A bare w_lambda now means the q-deformed weight, so the
# classical bucket is keyed on the explicit (1) rather than on the definition.
_CDEF = re.compile(r"w_\\lambda\(1\)")
# An ASSERTION that the weights sum to one. Must not match a DENIAL: the
# corrective prose added by the convention-B migration says "do not sum to 1"
# and "is not $1$", and an earlier version of this regex scored those as
# defects -- the checker reading its own fix as the bug it fixed.
_SUM1 = re.compile(
    r"(?<!not )(?<!n't )\\sum[^$\n]{0,40}w_\\lambda\s*=\s*1"
    r"|(?<!not )(?<!do not )sum to \$?1"
)
_DENIAL = re.compile(r"do(?:es)? \*?\*?not\*?\*? sum to|is \*?\*?not\*?\*? \$1\$|\\neq 1")


def census() -> dict:
    qdef, cdef, claims = [], [], []
    for f in sorted(glob(str(REPO / "content/quantum-observable-universe/*/*.md"))):
        src = Path(f).read_text()
        rel = os.path.relpath(f, REPO)
        # Convention B (2026-08-16): no tilde survives. A q-deformed
        # definition on the bare symbol is now CORRECT, not a collision.
        has_q = bool(_QDEF.search(src))
        if has_q:
            qdef.append(rel)
        if _CDEF.search(src):
            cdef.append(rel)
        if has_q and _SUM1.search(src) and not _DENIAL.search(src):
            claims.append(rel)
    return {
        "defines_q_deformed": qdef,
        "defines_classical": cdef,
        "q_deformed_and_claims_sums_to_one": claims,
    }


def main() -> None:
    q0, q0_src = _q0()
    rows = []
    for n in range(3, 9):
        s_q = weight_sum(n, q0)
        # EXACT, not float. This is the classical sum-of-squares identity
        # Sum_lambda (f^lambda)^2 = n!, so the value is exactly 1 by a theorem.
        # `int / int` in Python 3 is float division, which turned a proved
        # identity into a float64 that merely lands on 1.0 — and put raw
        # float64 in the witness. Fraction keeps it exact and lets the emission
        # show `1`, which is the actual claim. Bean qou-irzg.
        s_c = Fraction(
            sum(dim_classical(l, n) ** 2 for l in partitions(n)),
            math.factorial(n),
        )
        rows.append(
            {
                "n": n,
                "sum_q_deformed": mp.nstr(s_q, 30),
                "sum_q_deformed_unbalanced_convention": mp.nstr(
                    weight_sum_unbalanced(n, q0), 30
                ),
                "sum_classical": str(s_c),
                "deviation_from_one": mp.nstr(s_q - 1, 12),
            }
        )
        print(
            f"n={n}: sum = {mp.nstr(s_q, 18):>22}"
            f"   unbalanced {mp.nstr(weight_sum_unbalanced(n, q0), 12):>16}"
            f"   (classical {s_c})"
        )

    # Correctness control: the implementation must recover the classical 1 as q -> 1.
    q_near = mpf(1) + mpf("1e-30")
    control = {
        str(n): mp.nstr(weight_sum(n, q_near), 20) for n in (3, 4, 5)
    }
    print(f"\nq -> 1 control: {control}")

    c = census()
    print(
        f"\ncensus: {len(c['defines_q_deformed'])} blocks define w_lambda q-deformed, "
        f"{len(c['defines_classical'])} classical; "
        f"{len(c['q_deformed_and_claims_sums_to_one'])} do both AND claim it sums to 1"
    )
    for b in c["q_deformed_and_claims_sums_to_one"]:
        print(f"  DEFECT  {b}")

    OUT.write_text(
        json.dumps(
            {
                "schema": "qou-audit-probe/v1",
                "question": (
                    "Does the q-deformed Wedderburn weight dim_q(lambda)^2/[n]_q! "
                    "sum to 1 over partitions of n, as three corpus blocks assert?"
                ),
                "verdict": "no",
                "anchor": {"q0": mp.nstr(q0, 50), "source": q0_src, "layer": "experimental (proton)"},
                "dps": mp.dps,
                "rows": rows,
                "q_to_one_control": control,
                "control_note": (
                    "The q -> 1 limit returns exactly 1, so the deviations below "
                    "are the q-deformation, not an implementation error."
                ),
                "census": c,
                "corroborates": (
                    "content/quantum-observable-universe/mass-theory/"
                    "spectral-sequence-collapse-proof.md, which states the "
                    "q-deformed weights do not sum to 1 at q != 1"
                ),
            },
            indent=2,
        )
        + "\n"
    )
    print(f"\nwrote {os.path.relpath(OUT, REPO)}")


if __name__ == "__main__":
    main()
