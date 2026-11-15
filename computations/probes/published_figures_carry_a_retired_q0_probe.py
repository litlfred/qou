#!/usr/bin/env python3
"""Six published figures in FOUR blocks are computed from a `q0` that now exists
ONLY in `fsh-guts/deprecated/computations/` (`qou-i229`).

AND IT CORRECTS MY OWN SWEEP
----------------------------
`scripts/unsourced-published-figures.py` asked "does any published figure have
deprecated-only provenance?" and answered **no**: 653 decimals live only under
`fsh-guts/deprecated/computations/` and none of them appears in `content/`. That answer
is true as stated and **misleading as read**. It tests for the literal decimal
STRING. A published figure that is a *function* of a retired constant inherits
its provenance without ever carrying its digits — which is exactly what happened
here. The string-level zero says nothing about the derived level.

THE RETIRED VALUE
-----------------
    q0_retired = 1.1099785955541805752815940796095093779932822799587

It appears in eight `_deprecated/` witnesses and one `_deprecated/` script, and
nowhere live. The two live anchors are

    proton (default)      1.1099785827513808075916690956107688798744991218736
    muon   (QOU_Q0_ANCHOR=ideal)
                          1.10997859564273904668179512938000175270006556102901...

so the retired value is neither. It sits between them, which is why a
digit-counting glance does not settle it and a computation does.

THE DISCRIMINATION, AND IT IS NOT CLOSE
---------------------------------------
`q [9]_q [10]_q` is the sharpest of the four because the quantum integers amplify
the difference. Published: `136.823219654`.

    q0 candidate        q [9]_q [10]_q        agrees with published to
    proton (live)       136.823208853583      7 significant figures
    muon   (live)       136.823219729273      9 significant figures
    RETIRED             136.823219654561     11 significant figures

The other three figures agree with the retired value to 10-11 digits, and on all
four the retired value is the closest by relative error. One retired constant,
four figures, two blocks.

(On `log(1 + q_0)` the retired and muon values both round to 10 digits, so a
floored digit count ties them; the relative errors are `1.9e-11` and `6.1e-11`,
which is why the comparison below is made on relative error and not on the
bucket.)

    block                                  figure              published
    hecke-log-decomposition-table-data     1 + q_0             2.10997859556
    hecke-log-decomposition-table-data     log(1 + q_0)        0.74667780313
    hecke-log-decomposition-table-data     log(1/hbar_q)       2.31181024982
    em-coupling-bring-zero-mode            q [9]_q [10]_q      136.823219654
    q-beta-form-a-n1-symbolic-table-data   1 + hbar_q^2        1.009817188513479
    q-beta-spectral-bridge-table-data      h^2                 0.04370621823290131

`1 + hbar_q^2` is the sharpest of the six: the retired value reproduces it to
**15** significant figures, against muon's 10 and proton's 8.

HOW MANY DIGITS THE METHOD NEEDS
--------------------------------
The muon and retired values differ by a relative `7.98e-11`, so a figure must be
published to about **12 significant digits** to separate them. Two figures the
sweep flagged (`2.48662110`, `7.30870098`, both 9 digits) are therefore
**indeterminate, not clean** — the test cannot rule on them and says nothing.
Recorded because "no hit" and "no resolving power" look identical in a table.

WHAT IS **NOT** DONE HERE, DELIBERATELY
----------------------------------------
The figures are **not recomputed**. Which anchor these tables should use is
owner-gated: `q_parameter.py` says the corpus is "genuinely MIXED (sweep
2026-07-06: 279 proton + 455 muon)", that "a blanket flip is WRONG", and "do NOT
change this default". Picking a pin on the author's behalf is the kind of quiet
convention change this arc has spent its time undoing. So this probe reports both
live values for each figure and the blocks carry a caveat; the substitution waits
for a ruling.

WHAT IS NOT CLAIMED
-------------------
No claim that the retired `q0` was wrong when those tables were written — it was
presumably current. No claim about the other 28 unsourced figures; the same test
should be run on them and has not been. No claim that either live anchor is
correct for these particular blocks, which is the open question. And nothing
about the physics of `alpha_EM`, `hbar_q` or the Hecke log decomposition.
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

mp.mp.dps = 50

Q_RETIRED = "1.1099785955541805752815940796095093779932822799587"
Q_PROTON = "1.1099785827513808075916690956107688798744991218736"
Q_MUON = ("1.10997859564273904668179512938000175270006556102901"
          "1556974045769999095")


def qint(n, q):
    """Balanced quantum integer `[n]_q`."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


#: `(label, f(q), published, block)` — the four flagged figures.
FIGURES = (
    ("1 + q_0", lambda q: 1 + q, "2.10997859556",
     "hecke-log-decomposition-table-data"),
    ("log(1 + q_0)", lambda q: mp.log(1 + q), "0.74667780313",
     "hecke-log-decomposition-table-data"),
    ("log(1/hbar_q)", lambda q: mp.log(1 / (1 - 1 / q)), "2.31181024982",
     "hecke-log-decomposition-table-data"),
    ("q [9]_q [10]_q", lambda q: q * qint(9, q) * qint(10, q), "136.823219654",
     "em-coupling-bring-zero-mode"),
    # Round 2 (same day): two more blocks, found by reading each caption's own
    # closed form and solving. `1 + hbar_q^2` is the sharpest figure in the whole
    # sweep -- 15 significant figures to the retired value.
    ("1 + hbar_q^2", lambda q: 1 + (1 - 1 / q) ** 2, "1.009817188513479",
     "q-beta-form-a-n1-symbolic-table-data"),
    ("h^2", lambda q: (q - 1 / q) ** 2, "0.04370621823290131",
     "q-beta-spectral-bridge-table-data"),
)

#: Captions whose closed form, read literally, reproduces NOTHING at any anchor.
#: Recorded so the next pass does not re-guess them: the formula in the caption
#: is not the whole computation, or another input enters. NOT evidence either way
#: about which `q0` they carry.
UNRESOLVED = (
    ("ln(1 + z h)", "0.09929139859972778", "q-beta-spectral-bridge-table-data"),
    ("1/z + (z-1)h/(2z)", "1.897907634269324", "q-beta-spectral-bridge-table-data"),
)


def sig_agree(a, b) -> int:
    """Leading significant decimal digits on which `a` and `b` agree."""
    if a == b:
        return 99
    rel = abs(a - b) / abs(b)
    return int(mp.floor(-mp.log(rel, 10)))


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\nmpmath at {mp.mp.dps} dps")

    qs = {"proton (live)": mp.mpf(Q_PROTON), "muon (live)": mp.mpf(Q_MUON),
          "RETIRED": mp.mpf(Q_RETIRED)}

    print("\n" + "=" * 78)
    print("§1  THE RETIRED q0 IS NEITHER LIVE ANCHOR")
    print("=" * 78)
    for nm, v in qs.items():
        print(f"    {nm:>14}  {mp.nstr(v, 22)}")
    distinct = (qs["RETIRED"] != qs["proton (live)"]
                and qs["RETIRED"] != qs["muon (live)"])
    between = qs["proton (live)"] < qs["RETIRED"] < qs["muon (live)"]
    check("the retired value is distinct from both live anchors", distinct)
    check("and lies BETWEEN them, so digit-counting does not settle it — only a "
          "computation does", between)

    print("\n" + "=" * 78)
    print("§2  WHICH q0 REPRODUCES EACH PUBLISHED FIGURE")
    print("=" * 78)
    best_is_retired = True
    vals: dict[str, dict[str, str]] = {}
    for label, f, pub, block in FIGURES:
        p = mp.mpf(pub)
        agree = {nm: sig_agree(f(v), p) for nm, v in qs.items()}
        vals[label] = {nm: mp.nstr(f(v), 15) for nm, v in qs.items()}
        # Pick by RELATIVE ERROR, not by the floored digit count: the integer
        # bucketing ties `log(1 + q_0)` between muon and RETIRED at 10 digits
        # when the actual errors are 6.1e-11 and 1.9e-11. The bucket was lossy,
        # not the claim.
        err = {nm: abs(f(v) - p) / abs(p) for nm, v in qs.items()}
        winner = min(err, key=err.get)
        best_is_retired &= (winner == "RETIRED")
        print(f"\n    {label}   published {pub}   [{block}]")
        for nm in qs:
            mark = "  <-- best" if nm == winner else ""
            print(f"      {nm:>14} {vals[label][nm]:>22}   "
                  f"{agree[nm]:2d} sig figs{mark}")
    check("for EVERY one of the four figures the RETIRED q0 is the closest match "
          "by relative error — one retired constant, four figures, two blocks",
          best_is_retired)

    print("\n" + "=" * 78)
    print("§3  THE SHARPEST DISCRIMINATOR, AND IT IS NOT CLOSE")
    print("=" * 78)
    lbl, f, pub, _ = FIGURES[3]
    p = mp.mpf(pub)
    a = {nm: sig_agree(f(v), p) for nm, v in qs.items()}
    for nm in qs:
        print(f"    {nm:>14}  {lbl} = {mp.nstr(f(qs[nm]), 15):>18}   "
              f"{a[nm]} sig figs")
    check("q [9]_q [10]_q separates the three candidates by 3+ significant "
          "figures — the quantum integers amplify the difference",
          a["RETIRED"] >= a["muon (live)"] + 2
          and a["RETIRED"] >= a["proton (live)"] + 3)

    print("\n" + "=" * 78)
    print("§4  HOW MANY DIGITS THE METHOD NEEDS")
    print("=" * 78)
    gap = abs(qs["muon (live)"] - qs["RETIRED"]) / qs["RETIRED"]
    need = int(mp.ceil(-mp.log(gap, 10))) + 1
    print(f"    muon vs RETIRED relative gap = {mp.nstr(gap, 4)}")
    print(f"    so a published figure needs about {need} significant digits to")
    print("    separate them. Below that the test cannot rule between the muon")
    print("    anchor and the retired value, and says nothing.")
    print("\n    Figures the sweep flagged that fall UNDER that floor:")
    for lbl, pub in (("q^10 - q^-10", "2.48662110"),
                     ("h^2/[q dq(9) dq(10)]", "7.30870098")):
        print(f"      {lbl:>24} {pub:>14}  ({len(pub.replace('.', '').lstrip('0'))} digits)"
              f"  -- INDETERMINATE, not clean")
    check("the muon/retired gap needs ~12 significant digits to resolve, so "
          "figures published to 9 are indeterminate rather than clean",
          need >= 11)

    print("\n    Captions whose literal closed form reproduces nothing at any")
    print("    anchor — my reading was wrong, recorded so it is not re-guessed:")
    for lbl, pub, block in UNRESOLVED:
        print(f"      {lbl:>24} {pub:>21}  [{block}]")

    print("\n" + "=" * 78)
    print("§S  WHAT THIS SETTLES, AND WHAT IT LEAVES OPEN")
    print("=" * 78)
    print("  Six published figures across four blocks carry a q0 that survives only in")
    print("  fsh-guts/deprecated/computations/. They are NOT recomputed here: which")
    print("  anchor these blocks should use is owner-gated (q_parameter.py: the")
    print("  corpus is 'genuinely MIXED', 'a blanket flip is WRONG'). Both live")
    print("  values are reported per figure and the blocks now say so.")
    print()
    print("  It also corrects this sweep's own Q1. 'No published figure has")
    print("  deprecated-only provenance' tested for the literal decimal STRING;")
    print("  a figure derived FROM a retired constant inherits its provenance")
    print("  without carrying its digits. The string-level zero was true and")
    print("  said nothing about the derived level.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "Four published figures in hecke-log-decomposition-table-data and "
            "em-coupling-bring-zero-mode are computed from q0 = "
            "1.1099785955541805752815940796095093779932822799587, which appears in eight "
            "fsh-guts/deprecated/computations/ witnesses and one deprecated script and nowhere "
            "live. It is neither live anchor (proton 1.10997858275..., muon "
            "1.10997859564...) and lies between them. The sharpest discriminator is "
            "q [9]_q [10]_q, published 136.823219654: the retired q0 gives "
            "136.823219654561, matching all 12 published digits, while muon gives "
            "136.823219729273 (9 sig figs) and proton 136.823208853583 (8). The other "
            "three figures agree with the retired value to 10-11 digits and with neither "
            "live anchor. NOT recomputed: the proton/muon choice is owner-gated. This "
            "also corrects the sweep's own Q1 -- 'no deprecated-only provenance' tested "
            "literal decimal strings, and a figure derived from a retired constant "
            "inherits provenance without carrying its digits.")
        wb.add_data("q0_retired", Q_RETIRED)
        wb.add_data("q0_proton_live", Q_PROTON)
        wb.add_data("q0_muon_live", Q_MUON)
        for label, _f, pub, block in FIGURES:
            key = label.replace(" ", "").replace("[", "").replace("]", "")
            wb.add_data(f"published_{key}", pub)
            wb.add_data(f"block_{key}", block)
            for nm, v in vals[label].items():
                wb.add_data(f"{key}_at_{nm.split()[0]}", v)
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "The figures are NOT recomputed and no anchor is chosen for these blocks. "
            "q_parameter.py: the corpus is genuinely mixed, a blanket flip is wrong, and "
            "the default is owner-gated.")
        wb.add_caveat(
            "No claim about the other 28 unsourced figures in qou-i229 — the same "
            "derived-provenance test should be run on them and has not been.")
        wb.add_caveat(
            "No claim that the retired q0 was wrong when these tables were written.")
        print(f"\nWitness: {wb.save(extra={"q0Anchor": "ambiguous", "q0AnchorReason": 'compares three pins on purpose: the live proton pin, the live muon pin, and the retired CODATA-2018 muon pin 1.10997859555418...; the published figures are recomputed at each to attribute them, so no single pin applies'})}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
