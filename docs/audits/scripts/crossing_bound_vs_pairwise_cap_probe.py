#!/usr/bin/env python3
"""Are the C(n,2) in the crossing-count bound and the C(A,2) in the pairwise
saturation cap the same object, or two things that happen to count pairs?

## Why

Two results in the corpus carry the binomial C(n,2):

  QOU.Braiding.card_allPairs_le_length   (Ch 9, PR #5021)
      a braid word whose net permutation reverses ALL C(n,2) strand pairs has
      length >= C(n,2).                                    [LOWER bound, count]

  QOU.MassTheory.exchangeDet_pow_two_le_four (BindingSaturationCapA4.lean)
      rho_A(m) := b_A(m)/b_2(m) <= C(A,2), where
      b_A(m) = -ln det(I + m*(J-I)_A).                     [UPPER bound, ratio]

The second is the proved exclusion behind "the missing extensive binding term
must be super-pairwise". If the first were the same fact seen from the braid
side, it would constrain the same object and the two could be unified.

The prior is that this is a binomial coincidence -- C(n,2) appears wherever
pairs do -- so this probe is written to TEST that prior, not to confirm a
resemblance.

## What it measures

1. Whether C(A,2) in the cap is genuinely an edge count of K_A, by checking
   rho_A(m) -> C(A,2) as m -> 0. If the limit is C(A,2) the binomial is
   |E(K_A)| in both places, and the resemblance is at least real vocabulary.
2. Whether the cap is tight/attained, i.e. whether rho_A ever reaches C(A,2)
   for m in (0,1), which decides whether the ceiling is a saturation value or
   merely an upper envelope.
3. The counterexample to the tempting bridge: word length does not control the
   Markov trace, so a LOWER bound on letters yields no bound on any magnitude.

Anchor: none needed -- both objects are q-free. The cap's parameter m is its
own variable, swept, not pinned.

Usage:
  python3 -u docs/audits/scripts/crossing_bound_vs_pairwise_cap_probe.py 2>&1 \
      | tee /tmp/crossing_vs_cap.log
"""
from __future__ import annotations

import json
import os
import sys
from math import comb
from pathlib import Path

from mpmath import mp, mpf, log

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "computations" / "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

REPO = Path(__file__).resolve().parents[3]
OUT = Path(__file__).with_suffix(".witness.json")


def det_A(A: int, m) -> "mpf":
    """det(I + m*(J-I)_A) on the unsigned complete graph K_A.

    Spectrum is {1 + (A-1)m, (1-m)^{x(A-1)}}, so the determinant is
    (1 + (A-1)m) * (1-m)^(A-1).  This is the closed form the Lean file uses.
    """
    return (1 + (A - 1) * m) * (1 - m) ** (A - 1)


def b_A(A: int, m) -> "mpf":
    """The isospin-even log-det cumulant b_A(m) = -ln det_A(m)."""
    return -log(det_A(A, m))


def rho(A: int, m) -> "mpf":
    """The dimensionless magnitude ratio rho_A(m) = b_A(m)/b_2(m)."""
    return b_A(A, m) / b_A(2, m)


def main() -> None:
    rows = []
    # (1) small-m limit: is C(A,2) the edge count of K_A?
    print("=== (1) rho_A(m) as m -> 0, against C(A,2) ===")
    for A in range(2, 9):
        target = comb(A, 2)
        vals = {}
        for e in (3, 6, 9, 12):
            m = mpf(10) ** (-e)
            vals[f"1e-{e}"] = mp.nstr(rho(A, m), 20)
        limit_err = abs(rho(A, mpf(10) ** -12) - target)
        rows.append(
            {
                "A": A,
                "C_A_2": target,
                "rho_at_m": vals,
                "abs_err_vs_C_A_2_at_1e-12": mp.nstr(limit_err, 6),
            }
        )
        print(
            f"  A={A}: C(A,2)={target:>3}   rho(1e-12)={mp.nstr(rho(A, mpf(10)**-12), 18):>22}"
            f"   |err|={mp.nstr(limit_err, 4)}"
        )

    # (2) is the cap attained anywhere on (0,1), or only approached as m -> 0?
    print("\n=== (2) sup of rho_A over m in (0,1) — attained, or approached? ===")
    sup_rows = []
    for A in (2, 4, 6, 8):
        target = comb(A, 2)
        best, best_m = mpf(0), None
        # coarse sweep; the question is only whether rho ever EXCEEDS or MEETS C(A,2)
        for i in range(1, 1000):
            m = mpf(i) / 1000
            r = rho(A, m)
            if r > best:
                best, best_m = r, m
        sup_rows.append(
            {
                "A": A,
                "C_A_2": target,
                "max_rho_on_grid": mp.nstr(best, 20),
                "argmax_m": mp.nstr(best_m, 6),
                "exceeds_cap": bool(best > target),
            }
        )
        print(
            f"  A={A}: C(A,2)={target:>3}   max rho on (0,1) = {mp.nstr(best, 18):>22}"
            f"   at m={mp.nstr(best_m, 6)}   exceeds cap: {best > target}"
        )

    # (3) the bridge that does not exist: length does not control the trace.
    #     A length-2 word can be the identity, so no lower bound on word length
    #     induces any lower bound on a trace-derived magnitude.
    print("\n=== (3) does word length control magnitude? ===")
    counterexample = {
        "word": "sigma_1 * sigma_1^{-1}",
        "length": 2,
        "net_permutation": "identity",
        "crossed_pairs": 0,
        "point": (
            "Word length is not monotone in anything the binding reads. The "
            "Markov trace of a length-2 word here equals that of the empty "
            "word, so a LOWER bound on letters induces no lower bound on a "
            "trace-derived magnitude. The crossing bound therefore cannot "
            "constrain rho_A from below, which is the only direction that "
            "would interact with an UPPER cap."
        ),
    }
    print(f"  {counterexample['word']}: length 2, net permutation identity, 0 pairs crossed")
    print("  => length gives no magnitude bound; the two results do not meet.")

    verdict = {
        "same_object": False,
        "scope": "(a) scope-limited negative",
        "summary": (
            "Not the same object. The shared C(n,2) is |E(K_n)| in both places, "
            "so the vocabulary is genuinely shared -- but that is what 'pairwise' "
            "MEANS, not evidence of common content. The bounds run in opposite "
            "directions on different quantities (lower bound on a word length vs "
            "upper bound on a log-det ratio), and no bridge exists because word "
            "length does not control any trace-derived magnitude."
        ),
        "trap_recorded": (
            "The tempting inference 'the braiding has no n-ary generator, so the "
            "extensive term cannot be super-pairwise' is a CATEGORY ERROR of the "
            "kind AGENTS.md names: a Markov trace of a word in 2-strand letters "
            "is already a many-body object. prop:pairwise-interaction-decomposition "
            "forbids a super-pairwise GENERATOR, not a super-pairwise VALUE. The "
            "saturation cap's conclusion stands untouched."
        ),
    }

    OUT.write_text(
        json.dumps(
            {
                "schema": "qou-audit-probe/v1",
                "question": (
                    "Is the C(n,2) in QOU.Braiding.card_allPairs_le_length the same "
                    "object as the C(A,2) in QOU.MassTheory.exchangeDet_pow_two_le_four?"
                ),
                "verdict": verdict,
                "dps": mp.dps,
                "small_m_limit": rows,
                "sup_over_unit_interval": sup_rows,
                "length_does_not_control_magnitude": counterexample,
            },
            indent=2,
        )
        + "\n"
    )
    print(f"\nverdict: NOT the same object (scope-(a))")
    print(f"wrote {os.path.relpath(OUT, REPO)}")


if __name__ == "__main__":
    main()
