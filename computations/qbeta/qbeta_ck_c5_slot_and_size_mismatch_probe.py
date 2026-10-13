#!/usr/bin/env python3
"""qbeta_ck_c5_slot_and_size_mismatch_probe.py — the N=4/N=5 signature depends on
WHICH c_5, and I merged the wrong one.

Bean `qou-cds1` / `qou-54g5`.  Scope-(a).

## What this corrects, and it is mine

PR #6564 (merged, `56c47a0782`) replaced the canonical framing doc's
monotonicity argument -- which was genuinely unsound -- with a SIZE-MISMATCH
argument, and wrote it into `AGENTS.md`:

    "For an exact series the residual after truncating at N tracks the first
     OMITTED term, so the N=4 residual should sit near |c_5*u^5| = 0.577 ppb.
     Convention C measured it at 0.055 ppb, ~10x smaller -- an anomalously good
     landing, which is the fit signature."

**That figure uses the SUPERSEDED c_5.**  The corpus settled the slot in
`qbeta_ladder_c5_slot_provenance_probe.py` (bean `qou-54g5`, on main):

    SDP extraction        -1.2229
    -(b^2 + 1/2)          -1.2527    2.4 % off        SIX sites, CURRENT
    3c_3^2 + b           +12.8676    ~10x, wrong sign  TWO sites, SUPERSEDED

`qbeta_ck_truncation_order_analysis.py` -- the script #6564 read -- carries the
SUPERSEDED family at its line 57.  I saw +12.87 there, saw two probes carrying an
`empirical_c5` near it, and concluded c_5 was "live, positive".  It is neither.

**And the premise I "corrected" was right.**  My own earlier PR #6424 had already
recorded that the non-monotonicity "was produced by the superseded positive
c_5 ... it does not survive that supersession".  I read that, called it wrong,
and did not check the carrier count.

## The size mismatch evaporates

With the LIVE c_5 the first omitted term is |c_5*u^5| = 0.0561 ppb against a
measured N=4 residual of 0.055 ppb -- **2 % agreement, exactly what an exact
series predicts.**  There is no anomalously good landing.  So the argument I put
in AGENTS.md is not merely differently-supported; with the correct coefficient it
points the OTHER WAY.

## But the signature itself SURVIVES -- and #6424 was also wrong

#6424 said that with the live c_5 "the column is strictly decreasing at both
pins".  That reads the SIGNED residual.  The claim at issue is that the residual
"ticks back UP", which is about MAGNITUDE.  Recomputed here at the proton pin:

    N      |residual|, LIVE c_5      |residual|, SUPERSEDED c_5
    4          6.1698 ppb                 6.1698 ppb
    5          6.2260 ppb   INCREASES     5.5551 ppb   decreases

So the non-monotonicity exists under the LIVE coefficient and NOT under the
superseded one -- the opposite of what #6424 concluded.  Both of my PRs got a
piece of this wrong, in opposite directions, and the probe records both.

## Net effect on the AGENTS.md clause

The CONCLUSION ("the N=4 -> N=5 non-monotonicity is the experimental signature")
stands, and now for the first time on a correct coefficient.  What must change is
the ARGUMENT: not "monotone" (unsound, #6564 was right to drop it), and not the
size mismatch (computed on a superseded c_5).  What supports it is that the
residual MAGNITUDE increases from N=4 to N=5 under the live family.

## Caveat, stated because it is load-bearing

`c_3` is taken as the recorded proton-pin extraction -2.0693425728, hardcoded,
not re-extracted here; and only the proton pin is computed.  The magnitude
crossing is 0.9 % (6.1698 -> 6.2260), so it is NOT robust to a large c_3 move.
A full settlement re-extracts c_3 at both pins.  This probe establishes the
DIRECTION and the coefficient question, not a final margin.

## Precision

mpmath at 50 dps; `q_0` from `q_at` (proton pin); `m_e` / `Q_beta` from
`codata_constants`.  No float64.
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

from mpmath import mp                                          # noqa: E402

from codata_constants import M_E_MEV, Q_BETA_MEV               # noqa: E402
from q_parameter import q_at                                   # noqa: E402

DPS = 50
mp.dps = DPS   # before the module-scope mpf literals below (import-time dps ratchet)
C3_PROTON = mp.mpf("-2.0693425728")     # recorded extraction; see Caveat
AGENTS_QUOTED_OMITTED_TERM = mp.mpf("0.577")   # ppb, as written into AGENTS.md

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    results.append((name, bool(ok), detail))


def main() -> int:
    mp.dps = DPS
    q = q_at(DPS)
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    me = mp.mpf(str(M_E_MEV))
    Q_exp = mp.mpf(str(Q_BETA_MEV))
    Q_A = me * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    alpha = (mp.sqrt(q) / (1 + q) - 1) * h / 2      # convention C, the ladder's frame

    c5_live = -(b ** 2 + mp.mpf(1) / 2)
    c5_super = 3 * C3_PROTON ** 2 + b
    fam_live = {2: mp.mpf(-1), 3: C3_PROTON, 4: C3_PROTON * b ** 4, 5: c5_live}
    fam_super = {**fam_live, 5: c5_super}

    print("=" * 78)
    print(" The N=4/N=5 signature depends on WHICH c_5 — and #6564 merged the wrong one")
    print("=" * 78)
    print(f"\n  q0 = {mp.nstr(q, 20)} (proton pin)   u = {mp.nstr(u, 12)}")
    print(f"  c_5 LIVE       -(b^2+1/2) = {mp.nstr(c5_live, 12)}   (six sites)")
    print(f"  c_5 SUPERSEDED  3c_3^2+b  = {mp.nstr(c5_super, 12)}   (two sites)")

    print("\n[1] the size-mismatch argument I wrote into AGENTS.md")
    om_live = abs(c5_live) * u ** 5 * 10 ** 9
    om_super = abs(c5_super) * u ** 5 * 10 ** 9
    print(f"    |c_5*u^5| with SUPERSEDED = {mp.nstr(om_super, 8)} ppb   "
          f"(AGENTS.md quotes {mp.nstr(AGENTS_QUOTED_OMITTED_TERM, 4)})")
    print(f"    |c_5*u^5| with LIVE       = {mp.nstr(om_live, 8)} ppb")
    print(f"    measured N=4 residual (convention C, as quoted) = 0.055 ppb")
    print(f"    LIVE prediction vs measurement: "
          f"{mp.nstr(abs(om_live - mp.mpf('0.055')) / mp.mpf('0.055') * 100, 4)} % apart")
    check(
        "agents_md_omitted_term_used_the_superseded_c5",
        abs(om_super - AGENTS_QUOTED_OMITTED_TERM) / AGENTS_QUOTED_OMITTED_TERM
        < abs(om_live - AGENTS_QUOTED_OMITTED_TERM) / AGENTS_QUOTED_OMITTED_TERM,
        f"AGENTS.md's 0.577 ppb tracks the SUPERSEDED c_5 "
        f"(|c_5 u^5| = {mp.nstr(om_super, 6)}), not the live one "
        f"({mp.nstr(om_live, 6)}); the figure is off by "
        f"{mp.nstr(om_super / om_live, 4)}x",
    )
    check(
        "size_mismatch_evaporates_under_the_live_c5",
        abs(om_live - mp.mpf("0.055")) / mp.mpf("0.055") < mp.mpf("0.1"),
        f"with the live c_5 the first omitted term is {mp.nstr(om_live, 6)} ppb "
        f"against a measured 0.055 ppb -- 2 % apart, exactly what an EXACT "
        f"series predicts. The 'anomalously good landing, ~10x smaller' is an "
        f"artifact of the superseded coefficient and points the other way.",
    )

    print("\n[2] the signature itself, recomputed under both families")
    cols: dict[str, dict[int, mp.mpf]] = {}
    for nm, fam in (("live", fam_live), ("superseded", fam_super)):
        Q = Q_A * mp.cos(alpha - u / 2)
        col = {1: (Q - Q_exp) / Q_exp * 10 ** 9}
        for k in (2, 3, 4, 5):
            Q *= 1 + fam[k] * u ** k
            col[k] = (Q - Q_exp) / Q_exp * 10 ** 9
        cols[nm] = col
    print("      N      |resid| live        |resid| superseded")
    for k in (3, 4, 5):
        print(f"      {k}   {mp.nstr(abs(cols['live'][k]), 8):>16}"
              f"   {mp.nstr(abs(cols['superseded'][k]), 8):>16}")
    live_up = abs(cols["live"][5]) > abs(cols["live"][4])
    super_up = abs(cols["superseded"][5]) > abs(cols["superseded"][4])
    print(f"    magnitude N=4 -> N=5 increases?   live: {live_up}   "
          f"superseded: {super_up}")
    check(
        "nonmonotonicity_holds_under_LIVE_and_not_under_superseded",
        live_up and not super_up,
        f"|residual| goes {mp.nstr(abs(cols['live'][4]), 6)} -> "
        f"{mp.nstr(abs(cols['live'][5]), 6)} ppb under the LIVE c_5 (increases, "
        f"so the signature holds) and "
        f"{mp.nstr(abs(cols['superseded'][4]), 6)} -> "
        f"{mp.nstr(abs(cols['superseded'][5]), 6)} under the superseded one "
        f"(decreases) -- the OPPOSITE of what my PR #6424 concluded, which read "
        f"the SIGNED column",
    )

    print("\n[3] the caveat, which is load-bearing")
    margin = (abs(cols["live"][5]) - abs(cols["live"][4])) / abs(cols["live"][4]) * 100
    print(f"    the live magnitude crossing is {mp.nstr(margin, 4)} % — NOT robust")
    print(f"    to a large c_3 move. c_3 is hardcoded at the recorded proton")
    print(f"    extraction and only the proton pin is computed here.")
    check(
        "crossing_margin_is_small_and_is_reported_as_such",
        margin < 5,
        f"the N=4 -> N=5 magnitude crossing under the live family is only "
        f"{mp.nstr(margin, 4)} %, computed with a hardcoded c_3 at one pin; a "
        f"full settlement re-extracts c_3 at both pins. This probe establishes "
        f"the direction and the coefficient question, not a final margin.",
    )

    print("\n  assertions:")
    for name, ok, detail in results:
        print(f"    [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"           {detail}")
    all_passed = all(ok for _, ok, _ in results)
    print(f"\n  allPassed: {all_passed}  ({sum(ok for _, ok, _ in results)}/{len(results)})")

    out = {
        "probe": "qbeta_ck_c5_slot_and_size_mismatch_probe",
        "bean": "qou-cds1",
        "corrects": "PR #6564 (merged 56c47a0782) and PR #6424, in opposite directions",
        "question": "does the N=4/N=5 signature survive, and which c_5 does "
                    "AGENTS.md's size-mismatch figure use?",
        "answer": "AGENTS.md's 0.577 ppb uses the SUPERSEDED c_5; under the live "
                  "c_5 the first omitted term is 0.0561 ppb against a measured "
                  "0.055, so the size mismatch evaporates. The signature itself "
                  "SURVIVES on magnitude under the live family and does not "
                  "under the superseded one.",
        "scope": "(a); c_3 hardcoded at the proton extraction, proton pin only",
        "q0": mp.nstr(q, 20), "q0_pin": "proton (q_at)", "q0Anchor": "proton", "dps": DPS,
        "u": mp.nstr(u, 20),
        "c5_live": mp.nstr(c5_live, 20),
        "c5_superseded": mp.nstr(c5_super, 20),
        "omitted_term_ppb_live": mp.nstr(om_live, 20),
        "omitted_term_ppb_superseded": mp.nstr(om_super, 20),
        "residual_ppb": {
            nm: {str(k): mp.nstr(v, 20) for k, v in col.items()}
            for nm, col in cols.items()
        },
        "crossing_margin_pct_live": mp.nstr(margin, 20),
        "assertions": [{"name": n, "passed": ok, "detail": d} for n, ok, d in results],
        "allPassed": all_passed,
    }
    dest = _HERE.parent / "qbeta-ck-c5-slot-and-size-mismatch.witness.json"
    dest.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"\n  witness -> {dest.relative_to(_COMP.parent)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
