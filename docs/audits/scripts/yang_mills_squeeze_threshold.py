#!/usr/bin/env python3
"""Where the Yang-Mills surreal squeeze actually turns over, and what that
excludes.

## The claim under test

`rem:yang-mills-surreal-bound` states the squeeze

    delta^2 * eps^-1 > eps^3

and says it "holds strictly for every standard-real delta > 0 and degenerates
to the marginal equality at delta = 0". It then concludes that every
non-trivial excitation has delta >= Delta_q ~ eps^3.

## The lemma is fine; the block uses it outside its hypothesis

`lem:surreal-squeeze` reads: *"let delta > 0 be a **standard real** number.
Then delta^2 * eps^-1 > eps^3."* That hypothesis is the whole content -- a
standard real beats any infinitesimal, so the lemma is both true and narrow.

The block then invokes it at **two values of delta that are not standard
reals**: at delta = 0, and again in the conclusion, which quantifies over
excitations with delta ~ eps^3 (infinitesimal). Neither is reachable from the
lemma. This is the "conditional-proved != premise-established" pattern from
AGENTS.md -- a hypothesis-carrying result restated downstream with the
antecedent dropped.

## Three separate questions, and they do not all get the same answer

1. Does it hold for standard-real delta > 0?  Yes.
2. Does it degenerate to equality at delta = 0?  **No** -- at delta = 0 the
   left side is 0 and the right side is eps^3 > 0, so the inequality FAILS
   strictly. There is no equality there.
3. Is there a marginal-equality case at all?  **Yes, at delta = eps^2** --
   solve delta^2/eps = eps^3 for delta. So the block's mathematical content is
   real; it is attached to the wrong value of delta.

## The consequence that matters

Rearranged, the squeeze is just

    delta^2 * eps^-1 > eps^3   <=>   delta^2 > eps^4   <=>   |delta| > eps^2

so its threshold is **eps^2**. The block's own asserted mass gap is
Delta_q ~ eps^3, which is SMALLER by a factor of eps -- so an excitation
sitting exactly at the asserted gap FAILS the squeeze. The two statements in
the block are mutually inconsistent, and at most one of them can be right.

This is a scope-(a) finding: the squeeze as written does not support the eps^3
gap. It is NOT a refutation of the mass gap, and not a claim that no squeeze
supports it -- a squeeze with threshold eps^3 would need a different exponent
(delta^2 * eps^-3 > eps^3, i.e. delta > eps^3, is the obvious candidate) and
nothing here rules that out.

## Method

Surreal infinitesimals are modelled by a small positive real. Only the ORDERS
matter for an inequality between monomials in eps, so this is a faithful test
of which side is larger; it is run at two magnitudes to show the verdicts are
order-driven and not an artefact of one choice.

Usage:
  python3 -u docs/audits/scripts/yang_mills_squeeze_threshold.py
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from mpmath import mp, mpf

mp.dps = 60

OUT = Path(__file__).with_suffix(".witness.json")
REPO = Path(__file__).resolve().parents[3]


def verdict(delta: mpf, eps: mpf) -> tuple[str, mpf, mpf]:
    lhs = delta**2 / eps
    rhs = eps**3
    return (">" if lhs > rhs else "=" if lhs == rhs else "<"), lhs, rhs


def main() -> None:
    cases = [
        ("delta = 0", "the block says 'degenerates to marginal equality' here", lambda e: mpf(0)),
        ("delta = eps^3", "the block's own asserted mass gap Delta_q", lambda e: e**3),
        ("delta = eps^2", "the true marginal case", lambda e: e**2),
        ("delta = 1", "a standard real", lambda e: mpf(1)),
    ]
    rows = []
    for exp in (6, 12, 24):
        eps = mpf(10) ** (-exp)
        for name, note, f in cases:
            rel, lhs, rhs = verdict(f(eps), eps)
            rows.append(
                {
                    "eps": f"1e-{exp}",
                    "delta": name,
                    "note": note,
                    "relation": f"delta^2/eps {rel} eps^3",
                    "holds": rel == ">",
                }
            )
            if exp == 6:
                print(f"{name:14s} {rel}   {note}")

    # Every verdict must be identical across the three magnitudes, or the test
    # is measuring the choice of eps rather than the order structure.
    by_delta: dict[str, set[str]] = {}
    for r in rows:
        by_delta.setdefault(r["delta"], set()).add(r["relation"].split()[-2])
    order_driven = all(len(v) == 1 for v in by_delta.values())
    print(f"\nverdicts identical across eps = 1e-6, 1e-12, 1e-24: {order_driven}")
    print("threshold: delta^2/eps > eps^3  <=>  delta^2 > eps^4  <=>  |delta| > eps^2")

    OUT.write_text(
        json.dumps(
            {
                "schema": "qou-audit-probe/v1",
                "block": "rem:yang-mills-surreal-bound",
                "lemma_hypothesis": "delta > 0 a STANDARD REAL (lem:surreal-squeeze)",
                "questions": {
                    "holds_for_standard_real_delta": True,
                    "delta_zero_is_within_lemma_hypothesis": False,
                    "asserted_gap_eps3_is_within_lemma_hypothesis": False,
                    "degenerates_to_equality_at_delta_zero": False,
                    "marginal_equality_exists_at": "delta = eps^2",
                    "asserted_gap_eps3_passes_the_inequality": False,
                },
                "threshold": "|delta| > eps^2",
                "asserted_gap": "Delta_q ~ eps^3",
                "finding": (
                    "The squeeze's threshold is eps^2; the block's asserted gap is "
                    "eps^3, smaller by a factor of eps. An excitation at the "
                    "asserted gap fails the squeeze. Scope-(a): the squeeze as "
                    "written does not support the eps^3 gap. Not a refutation of "
                    "the mass gap, and not a claim that no squeeze supports it."
                ),
                "order_driven": order_driven,
                "rows": rows,
            },
            indent=2,
        )
        + "\n"
    )
    print(f"wrote {os.path.relpath(OUT, REPO)}")


if __name__ == "__main__":
    main()
