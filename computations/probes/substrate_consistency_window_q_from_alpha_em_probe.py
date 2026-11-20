#!/usr/bin/env python3
"""The two `q`-from-`alpha_EM` figures in `tbl:substrate-consistency-window-table1-data`
reproduce exactly — they were correct, and merely unwitnessed (`qou-i229`).

WHY THIS EXISTS
---------------
The unsourced-published-figures sweep (`scripts/unsourced-published-figures.py`)
flagged `1.11023043771` and `1.11023043782` as having no producer anywhere in the
repo. They sit in a table whose prose says only

    "Inverting the bare form for the 2018 and 2022 central values gives
     1.11023043771 and 1.11023043782 — a shift of 1.1e-10 ..."

with no formula, no script and no witness; the block's `.ts` is an
`extracted-table` citing a proposition and nothing computational. Every
`alpha_EM`-inversion module in the tree is under `fsh-guts/deprecated/computations/`.

That is the shape a stale figure has, so it was worth checking rather than
assuming. **It checks out.**

WHAT THE FIGURES ARE
--------------------
Not `q0`. The substrate anchor is `q0 = 1.10997858...` (proton-pinned, from the
lepton mass ratio); these are a DIFFERENT determination of `q`, obtained by
inverting the **bare** electromagnetic coupling

    alpha^-1_bare(q) = q [9]_q [10]_q,      [n]_q = (q^n - q^-n)/(q - q^-1)

at the measured `alpha^-1`. The bare form evaluates to `~136.82` at `q0`, so
solving it at the measured `137.036` necessarily lands away from `q0` — the gap
is the Chern-Simons dressing (`sec:fine-structure-data`), not a discrepancy. The
table's point is that three independent sectors bracket `q` in a narrow window,
and this is the electromagnetic one.

MEASURED, at 40 dps
-------------------
    CODATA 2018  alpha^-1 = 137.035999084  ->  q = 1.11023043770666  -> 1.11023043771
    CODATA 2022  alpha^-1 = 137.035999177  ->  q = 1.11023043781657  -> 1.11023043782

Both published figures are the correct roundings. The quoted shift
`1.1e-10` is also correct: the difference is `1.0991e-10`.

ONE FIGURE IN THE BLOCK IS OVERSTATED, SLIGHTLY
------------------------------------------------
The prose calls the shift "six orders of magnitude below the +-0.00002 quoted".
It is `2e-5 / 1.0991e-10 = 1.8e5`, i.e. **five** orders, not six. Corrected in
the block; the conclusion it supports — that the CODATA vintage does not move the
`q` determination — is untouched and if anything unaffected by the factor.

THE TRIAGE VERDICT
------------------
`qou-i229` category **(c) correct but unwitnessed**: the numbers are right, they
are DERIVED rather than experimental input, and the fix is to record the producer
— which is this probe — rather than to change or delete anything. Distinguish
from category (a), an experimental input that is correctly absent from
`computations/` (e.g. `0.00137748`, the CODATA neutron-proton mass split), and
from (b), a genuinely stale value, of which none has yet been found.

WHAT IS NOT CLAIMED
-------------------
Nothing about whether the bare form is the right model of `alpha_EM`, which is
`rem:em-coupling-chern-simons` and `rem:alpha-em-derivation-open-problems` and is
explicitly open. Nothing about the window's other two rows. No claim that `q0`
should equal this `q`: it should not, and the block does not say it does.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

mp.mp.dps = 40

#: CODATA central values for `alpha^-1`, the two vintages the block compares.
CODATA = (("2018", "137.035999084", "1.11023043771"),
          ("2022", "137.035999177", "1.11023043782"))


def qint(n, q):
    """Balanced quantum integer `[n]_q = (q^n - q^-n)/(q - q^-1)`."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def alpha_inv_bare(q):
    """`alpha^-1_bare(q) = q [9]_q [10]_q` (`sec:fine-structure-data`)."""
    return q * qint(9, q) * qint(10, q)


def q_from_alpha(alpha_inv):
    """Invert the bare form at a measured `alpha^-1`."""
    return mp.findroot(lambda q: alpha_inv_bare(q) - mp.mpf(alpha_inv),
                       mp.mpf("1.11"))


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\nmpmath at {mp.mp.dps} dps; bare form alpha^-1 = q [9]_q [10]_q")

    print("\n" + "=" * 78)
    print("§1  INVERTING THE BARE FORM AT EACH CODATA VINTAGE")
    print("=" * 78)
    from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

    q0 = Q_MP
    print(f"    substrate anchor q0        = {mp.nstr(q0, 18)}")
    print(f"    alpha^-1_bare(q0)          = {mp.nstr(alpha_inv_bare(q0), 12)}"
          f"   (measured is ~137.036; the gap is the CS dressing)")
    print(f"\n    {'vintage':>8} {'alpha^-1':>16} {'q solved':>22} {'published':>16}")
    roots = {}
    ok_all = True
    for vint, a, pub in CODATA:
        r = q_from_alpha(a)
        roots[vint] = r
        rounded = mp.nstr(r, 12)
        agree = abs(r - mp.mpf(pub)) < mp.mpf("5e-12")
        ok_all &= agree
        print(f"    {vint:>8} {a:>16} {mp.nstr(r, 15):>22} {pub:>16}"
              f"   {'match' if agree else 'MISMATCH'}")
    check("both published figures are the correct roundings of the bare-form "
          "inversion at their CODATA vintage — the numbers were right, only "
          "unwitnessed", ok_all)

    print("\n" + "=" * 78)
    print("§2  THE QUOTED SHIFT, AND THE ONE OVERSTATEMENT")
    print("=" * 78)
    shift = roots["2022"] - roots["2018"]
    quoted_unc = mp.mpf("0.00002")
    orders = mp.log(quoted_unc / shift, 10)
    print(f"    shift 2018 -> 2022         = {mp.nstr(shift, 8)}"
          f"   (block says 1.1e-10)")
    print(f"    quoted uncertainty         = +-{mp.nstr(quoted_unc, 3)}")
    print(f"    ratio                      = {mp.nstr(quoted_unc / shift, 6)}"
          f"  =  {mp.nstr(orders, 4)} orders of magnitude")
    check("the quoted 1.1e-10 shift is correct",
          abs(shift - mp.mpf("1.1e-10")) < mp.mpf("1e-11"))
    check("but it is FIVE orders below the quoted uncertainty, not six — the "
          "block said six and is corrected", mp.mpf(5) < orders < mp.mpf(6))

    print("\n" + "=" * 78)
    print("§S  TRIAGE VERDICT FOR qou-i229")
    print("=" * 78)
    print("  Category (c): CORRECT BUT UNWITNESSED. The figures are derived, not")
    print("  experimental input, and they reproduce exactly. The fix is to record")
    print("  the producer — this probe — not to change anything. Distinguish from")
    print("  (a) an experimental input correctly absent from computations/, and")
    print("  (b) a stale value, of which none has yet been found.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "Triages the two q-from-alpha_EM figures in "
            "tbl:substrate-consistency-window-table1-data, flagged by the "
            "unsourced-published-figures sweep as having no producer anywhere in the "
            "repo (every alpha_EM inversion module is deprecated, and the block's .ts "
            "cites nothing computational). Inverting the bare form "
            "alpha^-1 = q [9]_q [10]_q at 40 dps: CODATA 2018 (137.035999084) gives "
            "q = 1.11023043770666 and CODATA 2022 (137.035999177) gives "
            "q = 1.11023043781657, whose roundings are exactly the published "
            "1.11023043771 and 1.11023043782. The quoted 1.1e-10 shift is also correct "
            "(measured 1.0991e-10). One overstatement corrected: that shift is FIVE "
            "orders below the quoted +-0.00002, not six. Verdict: correct but "
            "unwitnessed; the fix is to record the producer, not to change the numbers. "
            "These are NOT q0 -- they are the electromagnetic determination of q, and "
            "the bare form gives ~136.82 at q0, the gap being the Chern-Simons dressing.")
        for vint, a, _pub in CODATA:
            wb.add_data(f"alpha_inv_codata_{vint}", a)
            wb.add_data(f"q_from_bare_alpha_{vint}", mp.nstr(roots[vint], 20))
        wb.add_data("shift_2018_to_2022", mp.nstr(shift, 10))
        wb.add_data("orders_below_quoted_uncertainty", mp.nstr(orders, 6))
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Says nothing about whether the bare form is the right model of alpha_EM; "
            "that is rem:em-coupling-chern-simons and rem:alpha-em-derivation-open-"
            "problems, explicitly open.")
        wb.add_caveat(
            "These q values are NOT the substrate anchor q0 and are not meant to equal "
            "it. The block does not claim they do.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
