"""The two chi kernels agree to ~1e-49 -- IF AND ONLY IF both are on the same word.

WHAT THIS CHECKS
----------------
The corpus computes chi^lambda(beta_atom) twice, by two independent routes:

    atom-chi-rust-<atom>.witness.json          pyhecke_native.chi_q_atomic
                                               (Geck-Pfeiffer + Hoefsmit
                                               seminormal, release Rust, MPFR)
    chi-<atom>-h<3A>-at-q0-50dps.witness.json  chi_at_q0_via_hoefsmit_mpfr.py
                                               (Python/mpmath Hoefsmit)

Different languages, different kernels, one mathematical object.  Their
agreement is therefore a real cross-implementation check and not a tautology.

WHY IT IS A STALENESS DETECTOR, WHICH IS THE POINT
--------------------------------------------------
Both routes call `atom_braid_word_3A(Z, N)`.  The intra-ordering ruling
(`qou-hu1f`, owner 2026-09-05) changed that word from GROUPED to alternating
(`intra_order="borromean"`), and a chi cache's key is `(q, dps)` -- so a
braid-word change is INVISIBLE to it and re-running a producer is a no-op.  The
stale caches have to be deleted.

That makes this probe the cheap detector for exactly that failure.  Measured
before the repair, rust-committed against canonical:

    2 of 11 agreed  (deuteron alone), max residual 21.335035

-- i.e. not a precision disagreement but a different object.  After the repair:

    D    n=11  max rel 1.089973e-49  at (2,2,1,1)
    T    n=30  max rel 1.169077e-49  at (5,3,1)
    3He  n=30  max rel 8.872588e-50  at (3,2,1,1,1,1)

4He FAILED WHEN THIS WAS WRITTEN, AND THE SHAPE OF THAT FAILURE WAS THE PROOF
-----------------------------------------------------------------------------
RESOLVED 2026-09-07, hours after the paragraph this replaces.  Recorded because
the failure is more informative than the pass, and because a docstring asserting
a live state is exactly the staleness this probe exists to catch -- leaving it
would have been the same defect one level up.

While 4He's regeneration was still running the rust family was SPLIT, and this
probe reported

    4He   n=77   max rel 5.562231e+00   75/77 over tolerance

with the two agreeing blocks being

    (12,)  and  (1,1,1,1,1,1,1,1,1,1,1,1)

-- EXACTLY the two 1-dimensional representations of S_12, and nothing else.
That is the part worth keeping.  A 1-dim character is a PRODUCT of per-letter
scalars, so it is fixed by the letter multiset and blind to the order; two
blocks surviving, and precisely those two, is the signature of a REORDERING of
the same letters rather than a change of letters.  Nobody told this probe to
expect that set -- it fell out of a cache pair.

So this probe and `one_dim_reps_are_blind_to_intra_order_probe.py` confirmed
each other from opposite directions: that one measures the invariance across a
known reorder, this one recovered the same invariant set from data it was given
no ruling about.

After the regeneration, 4He joins the other three:

    4He  n=77  max rel 8.416279e-49  at (8,3,1)   0/77 over tolerance

WHAT A FAILURE HERE MEANS, AND WHAT IT DOES NOT
------------------------------------------------
A residual near 1e-49 is the two kernels' shared floor at 50 dps.  A residual
ORDERS above it does NOT mean one kernel is wrong -- it means the two are
evaluating different words, and the far likelier cause is that one cache
predates a ruling.  Check the braid word before suspecting the arithmetic.

The converse is the limit worth stating: agreement here shows the two routes
computed the SAME word, not that the word is the CORRECT one.  Both could be
stale together.  `chi_caches_predate_the_intra_ordering_change_probe.py` is the
check for that, and this probe does not replace it.
"""

from __future__ import annotations

import json
import sys
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 80

HERE = Path(__file__).resolve().parent
COMP = HERE.parent

# The shared floor of two MPFR kernels at 50 dps, with an order of headroom.
# A stale word lands ~47 ORDERS above this, so the threshold is not delicate.
TOL = Decimal("1e-45")

PAIRS = (
    ("D",   "atom-chi-rust-d",   "chi-deuteron-h6-at-q0-50dps"),
    ("T",   "atom-chi-rust-t",   "chi-tritium-h9-at-q0-50dps"),
    ("3He", "atom-chi-rust-3he", "chi-helium-3-h9-at-q0-50dps"),
    ("4He", "atom-chi-rust-4he", "chi-helium-4-h12-at-q0-50dps"),
)


def _rust_blocks(w: dict) -> dict:
    return {tuple(x["partition"]): x["chi_lambda"] for x in w["data"]["atom"]["by_partition"]}


def _canon_blocks(w: dict) -> dict:
    return {tuple(x["partition"]): x["chi_lambda"] for x in w["by_partition"]}


def main() -> int:
    rows, failures, missing = [], [], []
    for atom, rust, canon in PAIRS:
        rp, cp = COMP / f"{rust}.witness.json", COMP / f"{canon}.witness.json"
        if not rp.exists() or not cp.exists():
            missing.append((atom, rp.name if not rp.exists() else cp.name))
            continue
        rb = _rust_blocks(json.loads(rp.read_text()))
        cb = _canon_blocks(json.loads(cp.read_text()))
        common = sorted(set(rb) & set(cb))
        if not common:
            failures.append(f"{atom}: no partitions in common between the two routes")
            continue
        worst, worst_lam, n_over = Decimal(0), None, 0
        for lam in common:
            a, b = Decimal(rb[lam]), Decimal(cb[lam])
            d = abs(a - b) / abs(a) if a else abs(a - b)
            if d > TOL:
                n_over += 1
            if d > worst:
                worst, worst_lam = d, lam
        rows.append((atom, len(common), worst, worst_lam, n_over))
        if n_over:
            failures.append(
                f"{atom}: {n_over}/{len(common)} blocks disagree beyond {TOL:.0e} "
                f"(worst {worst:.6e} at {worst_lam}) -- the two routes are on "
                "DIFFERENT braid words, not merely different arithmetic")

    print("=" * 76)
    print("RUST vs HOEFSMIT chi -- cross-implementation agreement on one word")
    print("=" * 76)
    print(f"  {'atom':5s} {'n':>4s} {'max rel':>14s}  {'over tol':>8s}   worst block")
    for atom, n, worst, lam, n_over in rows:
        print(f"  {atom:5s} {n:4d} {worst:14.6e}  {n_over:8d}   {lam}")
    if missing:
        print()
        for atom, f in missing:
            print(f"  [SKIP] {atom}: {f} not present")

    print()
    if failures:
        for f in failures:
            print(f"  [FAIL] {f}")
        print(f"\n{len(failures)} FAILED")
        return 1
    if not rows:
        print("  [FAIL] no atom pair could be compared")
        return 1
    print(f"  [PASS] {len(rows)} atom(s): every block agrees within {TOL:.0e}")
    if missing:
        print(f"  NOTE: {len(missing)} atom(s) skipped -- this is NOT a clean bill for them")
    print("\nALL PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
