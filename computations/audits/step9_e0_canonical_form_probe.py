#!/usr/bin/env python3
"""Step 9's `E_0` line is wrong TWICE, and the corpus fixes both — no judgement needed.

BACKGROUND.  The canonical-chain walk (#7362, merged `e8289b4971`) found that
the cheat sheet's step-9 row gives two forms for the energy scale,

    E_0 = m_e/(q_0(q_0-1)) = m_e c_q^2 hbar_q     (lept)
    E_0 = Q_beta / |h(h-2)/2|                      (had)

and that substituting the second into step 11's `Q_beta = |Delta(net)| . E_0`
returns `Q_beta` identically -- the step derives its own input.  The walk left
that as a judgement for the author.

IT IS NOT A JUDGEMENT.  `computations/qbeta/qbeta_e0.py` opens

    "qbeta_e0 -- the ONE place E_0, the Q_beta energy scale, is defined."

and its entire public API is three functions:

    order_zero(q, m_e)    = m_e/(q(q-1))                 <- "NOT canonical"
    tower_summed(q, m_e)  = m_e/(q(q-1))/(1 - hbar_q^2)  <- canonical
    canonical(q, m_e)     = tower_summed(q, m_e)         <- "the form every new
                                                            producer should call"

**There is no hadronic variant.**  One scale, both channels.

SO THE CHEAT-SHEET LINE IS WRONG TWICE, not once:

  (1) its "lept" form IS `order_zero`, which the module explicitly marks NOT
      canonical and keeps only "so a historical figure stays reproducible";
  (2) its "had" form names an object that does not exist in the canonical API
      at all -- and is circular besides, which is what the walk measured.

AND THE FIX IS COMPLETED, OWNER-INSTRUCTED WORK THE DOCUMENT HAS NOT ABSORBED.
The module's own docstring records that `E_0` had two live forms differing by
0.9915 % "with no signal at either call site", and that they were "Unified here
on owner instruction, 2026-09-12", with `tower_summed` canonical by the
2026-09-03 full-tower ruling.

So the corpus-determined correct form of the step-9 row is:

    E_0 = m_e/(q_0(q_0-1))/(1 - hbar_q^2)      -- one scale, tower-summed,
                                                  canonical by the 2026-09-03
                                                  ruling; call qbeta_e0.canonical()

🛑 WHAT IS *NOT* CLAIMED, and the module says it first.  That the tower sum IS
`sum_k hbar_q^{2k} = 1/(1 - hbar_q^2)` is **taken from one live precedent, not
derived** -- the module says so itself and tracks it as bean `qou-y3bm`.  So
"canonical" here means BY RULING, not "proved".  This probe does not upgrade
that, and a later agent deriving a different tower sum changes `qbeta_e0`, not
this probe's conclusion about which form the document should name.

🛑 AND THE SCALE, so nobody reads this as fixing Q_beta.  Quoting the module:
"E_0 moves Q_beta by 0.9915 %.  The convention-D functional moves it by 257x
(base to base).  These are not comparable and fixing E_0 does not address the
gap."  This probe is about a documentation line, not about the Q_beta residual.

NO CONTENT IS EDITED HERE.  This measures; the wording is the author's.

NO-FLOAT64: mpmath at dps = 60 throughout; no float anywhere.

Run:  python3 computations/audits/step9_e0_canonical_form_probe.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
for p in ("computations", "computations/qbeta", "tools/qou-substrate/python"):
    sys.path.insert(0, str(REPO / p))

from mpmath import mp  # noqa: E402

mp.dps = 60

FAILURES: list[str] = []
CHECKS = 0

E0_SRC = REPO / "computations" / "qbeta" / "qbeta_e0.py"
CHEAT = REPO / "docs" / "canonical-derivation-cheat-sheet.md"


def check(ok: bool, label: str, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


def section1() -> str:
    print("\n=== 1. the corpus has ONE place E_0 is defined ===\n")
    src = E0_SRC.read_text(encoding="utf-8")
    check(
        "the ONE place E_0, the Q_beta energy scale, is defined" in src,
        "qbeta_e0.py declares itself the single definition site",
        f"{E0_SRC.relative_to(REPO)}",
    )
    check(
        "Unified here on owner instruction" in src and "2026-09-12" in src,
        "and it was unified ON OWNER INSTRUCTION, 2026-09-12",
        "because two live forms differed by 0.9915 % 'with no signal at\n"
        "either call site' -- completed work the cheat sheet has not absorbed.",
    )
    # the public API, read from __all__
    m = re.search(r"__all__\s*=\s*\[([^\]]*)\]", src)
    api = sorted(re.findall(r'"([^"]+)"', m.group(1))) if m else []
    check(
        api == ["TOWER_FACTOR_DOC", "canonical", "order_zero", "tower_summed"],
        "its ENTIRE public API is order_zero / tower_summed / canonical",
        f"__all__ = {api}",
    )
    check(
        not re.search(r"\b(hadron|hadronic|had_|_had)\b", src, re.I),
        "🛑 there is NO hadronic variant anywhere in the module",
        "one scale, both channels -- so the cheat sheet's lept/had SPLIT is\n"
        "itself obsolete, not merely mis-stated on one side.",
    )
    return src


def section2(src: str) -> None:
    print("\n=== 2. which form is canonical, and which the cheat sheet names ===\n")
    import qbeta_e0  # noqa: E402

    oz = qbeta_e0.order_zero()
    ts = qbeta_e0.tower_summed()
    cn = qbeta_e0.canonical()

    print(f"    order_zero()   = {mp.nstr(oz, 20)} MeV")
    print(f"    tower_summed() = {mp.nstr(ts, 20)} MeV   <- canonical")
    print(f"    canonical()    = {mp.nstr(cn, 20)} MeV")
    print(f"    ratio          = {mp.nstr(ts / oz, 12)}   (+{mp.nstr((ts/oz - 1)*100, 6)} %)\n")

    check(cn == ts, "canonical() IS tower_summed(), bit for bit")
    check(
        "NOT canonical" in src,
        "and order_zero() is explicitly marked NOT canonical in its own docstring",
        "kept only 'so a historical figure stays reproducible'",
    )

    # The cheat sheet's two forms.
    cheat = CHEAT.read_text(encoding="utf-8")
    check(
        r"\mathfrak{E}_0 = m_e/(q_0(q_0-1))" in cheat,
        "the cheat sheet's \"lept\" form is m_e/(q_0(q_0-1)) -- i.e. ORDER_ZERO",
        "so the document names the NON-canonical form as its leptonic scale.",
    )
    check(
        r"\mathfrak{E}_0 = Q_\beta/|h(h-2)/2|" in cheat,
        "and its \"had\" form is Q_beta/|h(h-2)/2| -- ABSENT from the module",
        "it names an object the canonical API does not have, and is circular\n"
        "besides (the walk's step-11 measurement, on main).",
    )


def section3() -> None:
    print("\n=== 3. did the unification actually take? ===\n")
    qb = REPO / "computations" / "qbeta"
    callers, handrolled = [], []
    for f in sorted(qb.glob("*.py")):
        if f.name == "qbeta_e0.py":
            continue
        t = f.read_text(encoding="utf-8")
        if "qbeta_e0" in t:
            callers.append(f.name)
        elif re.search(r"E0\s*=\s*.*M_E.*Q0\s*\*\s*\(\s*Q0\s*-\s*1", t) or \
                re.search(r"E0\s*=\s*.*m_e\s*/\s*\(\s*q0?\s*\*\s*\(", t):
            handrolled.append(f.name)
    print(f"    producers routing through qbeta_e0 : {len(callers)}")
    print(f"    still hand-rolling an E_0          : {len(handrolled)}")
    for n in handrolled[:8]:
        print(f"        {n}")
    print()
    check(
        len(callers) > 0,
        "the canonical module has live callers",
        f"{len(callers)} file(s) in computations/qbeta/",
    )
    print("    NOTE: a hand-rolled E_0 is not necessarily a defect -- several are")
    print("    deliberately order-zero for a historical comparison.  The count is")
    print("    reported, not adjudicated; adjudicating it is qou-y3bm's business,")
    print("    not this probe's.")


def section4() -> None:
    print("\n=== 4. the corpus-determined correct form ===\n")
    print("""    E_0 = m_e/(q_0(q_0-1))/(1 - hbar_q^2)

      - ONE scale, both channels -- the lept/had split is obsolete
      - tower-summed, canonical by the 2026-09-03 full-tower ruling
      - call qbeta_e0.canonical()

    So defect #1 needs no judgement: the corpus fixes the answer, and a
    reviewer can check it against qbeta_e0.py rather than against my
    reasoning -- which is exactly the test AGENTS.md sets for a
    corpus-derived correction.

    🛑 "Canonical" here means BY RULING, not proved.  The module itself says
    the geometric series 1/(1 - hbar_q^2) is "taken from the one live
    precedent, NOT derived", tracked as bean qou-y3bm.  This probe does not
    upgrade that.

    🛑 And this is a DOCUMENTATION line, not the Q_beta residual.  Quoting the
    module: E_0 moves Q_beta by 0.9915 %; the convention-D functional moves it
    by 257x.  Fixing E_0 does not address the gap.\n""")


def main() -> int:
    print("step 9 — E_0 canonical form probe")
    print("=" * 72)
    src = section1()
    section2(src)
    section3()
    section4()
    print("=" * 72)
    if FAILURES:
        print(f"FAILED {len(FAILURES)}/{CHECKS}")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print(f"all {CHECKS} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
