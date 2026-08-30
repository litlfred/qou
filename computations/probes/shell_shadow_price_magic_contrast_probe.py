#!/usr/bin/env python3
"""Does the shell shadow price distinguish magic A? Measured: NO, at all.

`pyhecke.sdp.solve_shell_magic_sdp` is the level-4 shell-closure feasibility
check -- the one piece of machinery in the corpus that poses an SDP ABOVE H_3
(at H_{3*A_magic}, so H_24 for the 8-shell). It forms the 2x2 PSD block
[[1, y],[y, 1]] with y = shell_shadow_price(a_magic)["shadow_price_abs"] and
declares feasibility iff |y| <= 1, its docstring noting that "closed-shell
magic numbers are expected to satisfy it by construction".

TWO DEFECTS, both measured here.

1. THE WRAPPER REFUSES NON-MAGIC INPUT, so it can never produce a contrast.
   `solve_shell_magic_sdp` returns infeasible unless `a_magic in MAGIC_NUMBERS`.
   The underlying `sigma_shell_characterization.shell_shadow_price` has no such
   guard, so the contrast IS computable and simply had never been run. This is
   the same shape as the delta^2-Phi table tabulating only magic Z, and as
   `magic_ladder_member` being a hardcoded copy of the magic list.

2. THE QUANTITY HAS NO FEATURE AT MAGIC A. Over A = 2..30 at the function's own
   default partition (k-1, 1) with k = 3A, `shadow_price_abs` is a smooth,
   monotone-decreasing function of A -- falling ~6 orders per unit A, from
   5.3e-3 at A=2 to 2.6e-237 at A=30. Magic and non-magic values interleave
   along one curve with no discontinuity, no local extremum, and no change of
   slope at 2, 8, 20 or 28.

   Worse for the feasibility test: |y| <= 1 is satisfied by **29 of 29** values
   -- 4/4 magic AND 25/25 non-magic -- and satisfied by up to 237 orders of
   margin. The docstring's "by construction" is literally correct, and that is
   precisely why the condition is vacuous: it cannot fail for any A, so passing
   it says nothing about shell closure.

SCOPE (a). A negative about this statistic at the standard-rep partition
(k-1, 1), which is the function's default and the one its callers use. Other
partitions of 3A are untested here and could in principle behave differently;
that is the open question this leaves, not a claim that none can work.

PRECISION. `shell_shadow_price` returns decimal STRINGS; they are parsed with
mp.mpf at 40 dps and never through float(). The conclusion is a monotone decay
across 234 orders of magnitude, so no precision question arises.
"""
from __future__ import annotations

import sys
from pathlib import Path
from mpmath import mp

_ROOT = Path(__file__).resolve().parents[1]
for _p in (_ROOT, _ROOT / "substrate",
           _ROOT.parent / "tools" / "pyhecke" / "python",
           _ROOT.parent / "tools" / "qou-substrate" / "python"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from sigma_shell_characterization import shell_shadow_price   # noqa: E402
from qou_substrate.witness import WitnessBuilder              # noqa: E402

mp.dps = 40
MAGIC = {2, 8, 20, 28, 50, 82, 126}
A_MAX = 30


def main() -> int:
    rows, errs = [], []
    for A in range(2, A_MAX + 1):
        d = shell_shadow_price(A)
        if "error" in d:
            errs.append({"A": A, "error": d["error"]})
            continue
        rows.append((A, mp.mpf(d["shadow_price_abs"])))

    magic = [(A, y) for A, y in rows if A in MAGIC]
    other = [(A, y) for A, y in rows if A not in MAGIC]

    # monotone decreasing in A?
    monotone = all(rows[i][1] > rows[i + 1][1] for i in range(len(rows) - 1))
    # any local extremum at a magic A?
    extrema = []
    for i in range(1, len(rows) - 1):
        A, y = rows[i]
        if (y > rows[i - 1][1] and y > rows[i + 1][1]) or \
           (y < rows[i - 1][1] and y < rows[i + 1][1]):
            extrema.append(A)

    feas_m = sum(1 for _, y in magic if abs(y) <= 1)
    feas_o = sum(1 for _, y in other if abs(y) <= 1)

    print(f"A range                  : 2..{A_MAX}  (k = 3A, so H_6..H_{3*A_MAX})")
    print(f"monotone decreasing in A : {monotone}")
    print(f"local extrema at any A   : {extrema or 'NONE'}")
    print(f"feasible |y|<=1, magic   : {feas_m}/{len(magic)}")
    print(f"feasible |y|<=1, other   : {feas_o}/{len(other)}")
    print(f"y(A=2)  = {mp.nstr(rows[0][1], 8)}")
    print(f"y(A={A_MAX}) = {mp.nstr(rows[-1][1], 8)}")

    w = WitnessBuilder("shell-shadow-price-magic-contrast", engine="mpmath")
    w.set_description(
        "Magic vs non-magic contrast for the level-4 shell shadow price "
        "(pyhecke.sdp.solve_shell_magic_sdp), the only SDP in the corpus posed "
        "above H_3. The wrapper refuses non-magic a_magic so the contrast had "
        "never been run; the underlying shell_shadow_price has no such guard. "
        "Measured over A=2..30 at the default partition (k-1,1): the shadow "
        "price is smooth and monotone decreasing in A with no feature at any "
        "magic A, and the |y|<=1 feasibility condition holds for 29/29 values "
        "(4/4 magic, 25/25 non-magic) by up to 237 orders of margin. The "
        "condition cannot fail, so passing it carries no shell-closure content."
    )
    w.add_parameter("A_max", A_MAX)
    w.add_parameter("partition", "(3A-1, 1)  [function default, standard rep]")
    w.add_data("monotone_decreasing_in_A", monotone)
    w.add_data("local_extrema_A", extrema)
    w.add_data("feasible_magic", f"{feas_m}/{len(magic)}")
    w.add_data("feasible_nonmagic", f"{feas_o}/{len(other)}")
    w.add_data("shadow_price_abs_by_A",
               {str(A): mp.nstr(y, 20) for A, y in rows})
    w.add_data("errors", errs)
    w.add_assertion("no_local_extremum_at_any_A", len(extrema), 0, tolerance=0,
                    source="a magic feature would appear as an extremum")
    w.add_assertion("feasibility_holds_for_every_A",
                    feas_m + feas_o, len(rows), tolerance=0,
                    source="|y|<=1 satisfied by magic and non-magic alike")
    w.add_assertion("monotone_so_no_magic_structure",
                    1 if monotone else 0, 1, tolerance=0,
                    source="smooth monotone decay admits no shell signal")
    w.add_caveat(
        "Scope (a): the default standard-rep partition (k-1, 1) only. Other "
        "partitions of 3A are untested and are the open question this leaves."
    )
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
