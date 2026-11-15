#!/usr/bin/env python3
"""The (1,2)-relation SYT counts have a closed form — and the 'mix' branch is
structurally unreachable.

STATUS: exact verification (integer arithmetic; Fraction for the character
ratio).  No fit, no tolerance, no selection.  This probe DECIDES a replacement
before it is made: it checks the proposed closed form against the existing
brute-force enumeration on EVERY partition up to n = N_MAX, and reports the
speedup.  A single mismatch fails it.

-----------------------------------------------------------------------------
WHY THIS EXISTS

Bean `qou-i7ju`: `hadron-knot-table.witness.json` is stale on `main` and its
producer cannot be re-run to completion (19 atoms; the witness is written once
at the end, so a bounded run yields nothing).  Bean `qou-r4w5` diagnoses the
cost as brute-force SYT enumeration in
`hecke_core_legacy._count_syts_by_12_relation`.

That function enumerates EVERY standard Young tableau of shape lambda -- f^lambda
of them -- in order to compute three counts.  f^lambda grows factorially: the
atoms use n = 3A strands, so 7Li is n = 21 where a single partition can carry
1e7+ tableaux.  This is why the table cannot finish.

-----------------------------------------------------------------------------
TWO CLAIMS BEING TESTED (both stated before any number is read)

(C1) THE 'MIX' BRANCH IS UNREACHABLE, so n_mix == 0 for every partition.
     In a standard Young tableau entries increase along rows and columns, so
     1 sits at (0,0) and 2 must occupy an addable cell of the single-cell
     shape -- i.e. (0,1) or (1,0).  Hence 2 is ALWAYS in the same row or the
     same column as 1, and 'neither' cannot occur.  (The producer's own `fill`
     enforces exactly this: value 1 is admissible only at row 0 column 0.)

(C2) THE TWO SURVIVING COUNTS ARE CLOSED-FORM.  Write f = f^lambda (hook-length
     formula) and Sum_c = sum over cells of the content c(i,j) = j - i.  At
     q = 1 the generator's row/column eigenvalues are +1 / -1, so
     n_row - n_col is the symmetric-group character on a transposition, which
     is the classical content result

         chi^lambda((12)) = f * Sum_c / C(n,2).

     With n_row + n_col = f this gives

         n_row = f * (1 + Sum_c / C(n,2)) / 2
         n_col = f * (1 - Sum_c / C(n,2)) / 2

     Both must come out as exact non-negative integers.

If C1 and C2 hold on every partition tested, the enumeration can be replaced by
O(n) arithmetic with no change to any downstream value -- which is what makes
regenerating the stale witness feasible rather than a budget question.

NOT CLAIMED: that this closes bean `qou-i7ju`.  It removes one wall; whether
the producer then finishes is a separate measurement.

-- Ref: computations/hecke_core_legacy.py::_count_syts_by_12_relation and
::partition_character_sigma1; beans qou-i7ju (stale witness), qou-r4w5 (cost
diagnosis).
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction
from math import comb, factorial
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
if str(_COMP) not in sys.path:
    sys.path.insert(0, str(_COMP))
from substrate.witness_base import WitnessBuilder  # noqa: E402

N_MAX = 10          # every partition of 1..N_MAX is checked exhaustively
N_TIME = 12         # separate timing point (brute force still feasible here)


def partitions(n: int, cap: int | None = None):
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def brute_counts(partition):
    """The EXISTING algorithm, transcribed verbatim in behaviour: enumerate
    every SYT and classify by where 2 sits relative to 1."""
    n = sum(partition)
    if n < 2:
        return (0, 0, 0)
    shape = list(partition)
    counts = [0, 0, 0]

    def fill(tab, val, rem):
        if val > n:
            pos_1 = pos_2 = None
            for r, row in enumerate(tab):
                for c, v in enumerate(row):
                    if v == 1:
                        pos_1 = (r, c)
                    if v == 2:
                        pos_2 = (r, c)
            if pos_1[0] == pos_2[0]:
                counts[0] += 1
            elif pos_1[1] == pos_2[1]:
                counts[1] += 1
            else:
                counts[2] += 1
            return
        for r in range(len(shape)):
            if rem[r] == 0:
                continue
            col = len(tab[r])
            if r > 0 and col >= len(tab[r - 1]):
                continue
            tab[r].append(val)
            rem[r] -= 1
            fill(tab, val + 1, rem)
            tab[r].pop()
            rem[r] += 1

    fill([[] for _ in shape], 1, list(shape))
    return (counts[0], counts[1], counts[2] // 2)


def hook_length_f(partition) -> int:
    """f^lambda by the hook-length formula (exact integer)."""
    n = sum(partition)
    if n == 0:
        return 1
    conj = [sum(1 for row in partition if row > j) for j in range(partition[0])]
    denom = 1
    for i, row in enumerate(partition):
        for j in range(row):
            denom *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // denom


def content_sum(partition) -> int:
    """Sum of contents c(i,j) = j - i over the cells of lambda."""
    return sum(j - i for i, row in enumerate(partition) for j in range(row))


def closed_counts(partition):
    """(n_row, n_col, n_mix) in closed form — no enumeration."""
    n = sum(partition)
    if n < 2:
        return (0, 0, 0)
    f = hook_length_f(partition)
    ratio = Fraction(content_sum(partition), comb(n, 2))
    nr = Fraction(f) * (1 + ratio) / 2
    nc = Fraction(f) * (1 - ratio) / 2
    if nr.denominator != 1 or nc.denominator != 1:
        raise ArithmeticError(f"non-integral counts for {partition}: {nr}, {nc}")
    return (int(nr), int(nc), 0)


def main() -> int:
    t0 = time.monotonic()
    mismatches, checked, mix_nonzero = [], 0, 0
    for n in range(1, N_MAX + 1):
        for lam in partitions(n):
            b = brute_counts(lam)
            c = closed_counts(lam)
            checked += 1
            if b[2] != 0:
                mix_nonzero += 1
            if b != c:
                mismatches.append({"partition": str(lam), "brute": str(b),
                                   "closed": str(c)})

    # timing at a single larger n where brute force is still feasible
    timing = []
    for lam in partitions(N_TIME):
        ta = time.monotonic()
        brute_counts(lam)
        t_brute = time.monotonic() - ta
        tb = time.monotonic()
        closed_counts(lam)
        t_closed = time.monotonic() - tb
        timing.append((lam, t_brute, t_closed))
    tot_brute = sum(t for _, t, _ in timing)
    tot_closed = sum(t for _, _, t in timing)
    speedup = (tot_brute / tot_closed) if tot_closed > 0 else float("inf")
    worst = max(timing, key=lambda r: r[1])

    ok = not mismatches and mix_nonzero == 0
    verdict = (
        f"VERIFIED on all {checked} partitions of n=1..{N_MAX}: the closed form "
        f"reproduces the brute-force counts EXACTLY ({len(mismatches)} "
        f"mismatches), and the 'mix' branch never fires ({mix_nonzero} nonzero) "
        f"— confirming it is structurally unreachable, since 1 sits at (0,0) and "
        f"2 must take (0,1) or (1,0). At n={N_TIME} the enumeration costs "
        f"{tot_brute:.3f}s across {len(timing)} partitions against "
        f"{tot_closed:.5f}s closed-form — {speedup:.0f}x, and the gap widens "
        f"factorially with n (the atoms run to n=3A, so 7Li is n=21). Replacing "
        f"the enumeration is exact, not approximate."
        if ok else
        f"FAILED: {len(mismatches)} mismatches, {mix_nonzero} nonzero-mix. "
        f"The closed form must NOT be substituted."
    )

    result = {
        "claims": {
            "C1_mix_unreachable": "n_mix == 0 always (1 at (0,0), 2 at (0,1) or (1,0))",
            "C2_closed_form": "n_row/n_col = f*(1 +- Sum_c/C(n,2))/2, f = hook length",
        },
        "exhaustive_check": {
            "n_max": N_MAX, "partitions_checked": checked,
            "mismatches": len(mismatches), "mismatch_detail": mismatches[:10],
            "brute_mix_nonzero_count": mix_nonzero,
        },
        "timing_at_n": {
            "n": N_TIME, "partitions": len(timing),
            "brute_total_s": f"{tot_brute:.4f}",
            "closed_total_s": f"{tot_closed:.6f}",
            "speedup_x": f"{speedup:.1f}",
            "worst_partition": str(worst[0]),
            "worst_brute_s": f"{worst[1]:.4f}",
        },
        "verdict": verdict,
    }
    payload = {
        "computation": "syt-12-relation-closed-form",
        "description": ("Exact verification that the (1,2)-relation SYT counts "
                        "have a closed form and that the 'mix' branch is "
                        "unreachable, enabling the factorial enumeration in "
                        "hecke_core_legacy to be replaced. Audit-only; exhaustive "
                        "integer check; no fit."),
        "tier": "exploratory (verification gate for a producer optimisation)",
        "result": result,
    }
    import platform
    wb = WitnessBuilder.wrap_legacy(
        "syt-12-relation-closed-form", payload,
        script_path=__file__, engine="python",
        engine_version=f"python {platform.python_version()}",
        output_dir=str(_HERE), start_time=t0,
    )
    wb.add_assertion("closed_form_matches_brute_force_exactly",
                     computed=str(len(mismatches)), expected="0")
    wb.add_assertion("mix_branch_never_fires",
                     computed=str(mix_nonzero), expected="0")
    wb.save(extra={"auditOnly": True, "q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal"})

    print("=== SYT (1,2)-relation: closed form vs brute-force enumeration ===")
    print(f"  exhaustive n=1..{N_MAX}: {checked} partitions, "
          f"{len(mismatches)} mismatches, mix-nonzero {mix_nonzero}")
    for m in mismatches[:5]:
        print(f"    MISMATCH {m}")
    print(f"  timing n={N_TIME}: brute {tot_brute:.4f}s vs closed "
          f"{tot_closed:.6f}s  -> {speedup:.0f}x")
    print(f"  worst single partition {worst[0]}: {worst[1]:.4f}s brute")
    print("  " + verdict)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
