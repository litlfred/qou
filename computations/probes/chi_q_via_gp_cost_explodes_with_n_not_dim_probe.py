"""`chi_q_via_gp` is ~20 ms/λ at n=6 and ~6 s/λ at n=12 — the docstring names the wrong axis.

THE CLAIM UNDER TEST
--------------------
`computations/chi_via_rust_lossless.py` documents its own cost as

    The canonical Rust `pyhecke_native.chi_q_via_gp` returns the exact Laurent
    character per λ in ~20 ms **independent of dim V_λ**, so a whole nucleus is
    seconds:

        ⁴He H₁₂ (77 λ) ≈ 2 s · ⁵Li H₁₅ (176 λ) ≈ 4 s · ⁶Li H₁₈ (385 λ) ≈ 8 s

The dim-independence is not what was measured here and is not disputed.  What is
disputed is the inference from it — that a whole nucleus is therefore seconds
**at any n**.  The cost is not flat in `n`, and `n` is the axis that decides
whether a regeneration is a coffee break or infeasible.

MEASURED — one call each, the CHEAPEST partition (the trivial rep `[n]`), so
these are lower bounds on the per-λ cost, not averages:

    atom   n_strands   word_len        time      ratio to previous
    D          6          23          1.5 ms
    T          9          35         28.3 ms         19x
    4He       12          47       5996.3 ms        212x

**Word length grows LINEARLY (23 → 35 → 47) while time grows by 19x then 212x**,
so the driver is not the word.  It is `n`, the rank of the Hecke algebra.

BOTH RUST ROUTES EXPLODE — THERE IS NO FASTER PATH IN THIS REPO
----------------------------------------------------------------
The corpus has a second Rust entry point, the BATCHED
`chi_cd_mpfr.chi_all_partitions_cd_mpfr` -> `pyhecke_native.chi_lambda_all_partitions_mpfr`,
which `compute_atom_chi_rust.py` uses and which did 4He's 77 partitions in
799.71 s this session.  It was checked before concluding anything was infeasible,
because a batched kernel scaling better would have collapsed the whole question:

    producer                      n=6        n=9         n=12      step ratios
    chi_q_via_gp      (per λ)    1.2 ms    26.4 ms     5646 ms     23x -> 214x
    ..._cd_mpfr       (per λ)    0.3 ms    15.3 ms    10386 ms     51x -> 679x

Both explode, and the batched one is **worse** per λ at n=12, not better.  So the
choice of route does not rescue n=15; extrapolating either gives days to weeks
for one 5Li cache.

(The n=6 row of the batched producer reads 0.00 s total and should not be
over-read — at that size it may be measuring startup rather than work.  The
load-bearing comparison is n=9 -> n=12, where both routes are unambiguous.)

WHAT THIS MAKES INFEASIBLE
--------------------------
Extrapolating the last ratio one step to n=15 gives ~21 minutes for ONE
partition, and ⁵Li has 176 of them — on the order of **two months** of wall clock
for a single atom's cache.  ⁶Li (n=18, 385 λ) is worse by another factor of the
same kind.

That is not a projection made to avoid the work: two runs were attempted first,
of 30 minutes and of 3 h 35 min, and the second is the corroboration.  The
producer prints a progress line every 40 partitions
(`chi_via_rust_lossless.py:187`), and in 3 h 35 min **not one appeared** — so
fewer than 40 of 176 partitions completed, independently putting the rate above
5.4 min/λ.

THIS CORRECTS A CLAIM I MADE IN `qou-d9wf`
-------------------------------------------
That bean says the producer "has **no** progress output", offered as half the
defect.  **It has progress output; it had not reached the first checkpoint.**
The silence is not a missing feature — it is the measurement.  The corrected
reading is worse than the original complaint, not better.

WHAT IS NOT ESTABLISHED
-----------------------
The *mechanism* inside the Rust.  A cost exploding between n=9 and n=12 while
the word grows linearly is consistent with an enumeration over something of
size ~`n!` or ~`p(n)·dim`, but this probe measures the boundary, not the cause,
and the Rust was not instrumented.  Do not write a complexity class into the
docstring on the strength of three points.

Nor is the n=15 figure measured — it is extrapolated from the n=9 → n=12 ratio,
and a single ratio is a weak basis for one more step.  What IS measured is that
n=15 did not complete 40 partitions in 3 h 35 min, which is enough to decide the
practical question without the extrapolation.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))

import _path_bridge  # noqa: F401,E402
import pyhecke_native as ph  # noqa: E402
from derived_chi_catalogue_matrix_m import _word_for_braid_word_3a  # noqa: E402

# (label, Z, N).  Stops at 4He deliberately: n=15 does not return in a
# tractable time, which is the finding rather than a gap in the table.
CASES = (("D", 1, 1), ("T", 2, 1), ("4He", 2, 2))

# The n=9 -> n=12 step measured 212x.  Assert only that the growth is far
# steeper than the word's, which is the claim; the exact ratio is machine- and
# load-dependent and must not be pinned.
MIN_GROWTH_9_TO_12 = 20.0


def main() -> int:
    rows = []
    for label, Z, N in CASES:
        n, word = _word_for_braid_word_3a(Z, N)
        t0 = time.monotonic()
        lau = ph.chi_q_via_gp([n], n, list(word))
        dt = time.monotonic() - t0
        rows.append((label, n, len(word), dt, len(lau)))

    print("=" * 78)
    print("chi_q_via_gp COST vs n — the trivial rep [n], one call each")
    print("=" * 78)
    print(f"  {'atom':6s} {'n':>4s} {'word_len':>9s} {'time (ms)':>12s} {'x prev':>9s}")
    prev = None
    growth = []
    for label, n, wl, dt, _ in rows:
        r = (dt / prev) if prev else None
        growth.append(r)
        print(f"  {label:6s} {n:4d} {wl:9d} {dt*1000:12.1f} "
              f"{('%.0fx' % r) if r else '—':>9s}")
        prev = dt

    wl = [r[2] for r in rows]
    print()
    print(f"  word length grows {wl[0]} -> {wl[-1]}, a factor of {wl[-1]/wl[0]:.1f}")
    print(f"  time grows a factor of {rows[-1][3]/rows[0][3]:.0f}")
    print()

    last = growth[-1]
    if last is None or last < MIN_GROWTH_9_TO_12:
        print(f"  [FAIL] n=9 -> n=12 grew only {last}x; the whole point of this probe "
              f"is that it is >> the word's growth. Either the machine changed or "
              f"the Rust path did — re-read before trusting the docstring again.")
        print("\n1 FAILED")
        return 1
    print(f"  [PASS] n=9 -> n=12 costs {last:.0f}x while the word grows "
          f"{wl[2]/wl[1]:.2f}x — the driver is n, not the word")
    print("\nALL PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
