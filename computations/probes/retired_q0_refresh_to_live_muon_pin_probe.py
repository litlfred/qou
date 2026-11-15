#!/usr/bin/env python3
"""THE REFRESH. Every closed-form figure carrying the retired `q0`, recomputed at
the live muon pin, per block and complete (`qou-i229`).

THE OWNER RULING THIS EXECUTES
-------------------------------
`qou-i229` established that six published figures across four blocks were
computed at

    q0_retired = 1.1099785955541805752815940796095093779932822799587

which survives only in `fsh-guts/deprecated/computations/` and is neither live anchor. It
is the **CODATA-2018 vintage of the muon pin** — recovered by inverting CAL-2 at
`m_mu/m_e = 206.7682830` — and the 2026-08-15 substrate fix that moved to the
NIST table reached `computations/` and `tools/` but not `content/`.

The two candidate muon values `qou-po7i` catalogued have since **converged**, so
there is one live muon pin and no ruling left to make about which:

    q0_muon = 1.109978595642739046681795129380001752700065561029011556974045769999095

from the canonical `q-pinning-50-digit.witness.json`.

THE CONSTRAINT THAT MADE A FIRST ATTEMPT WRONG
------------------------------------------------
An earlier pass substituted only the SIX FLAGGED figures and was reverted. The
sweep that found them looks for figures with *no* provenance; a block's other
`q0`-derived rows have some, so they were never flagged — and refreshing one
column while its siblings stay at the old pin leaves a table the reader can no
longer recompute from itself. **Worse than the stale value.**

So the unit is the block, not the figure. In `hecke-log-decomposition-table-data`
that means **all seven rows move**, not the three the sweep found.

WHAT MOVES AND WHAT DOES NOT
------------------------------
Constants and experimental inputs are fixed and must NOT be touched:
`2/(3*pi)`, CODATA `1/alpha = 137.035999177(21)`, `Q_beta^CODATA`. Everything
`q0`-derived moves. This probe computes both columns so the diff is checkable.

TWO PRE-EXISTING TRANSCRIPTION SLIPS, SEPARATE FROM THE PIN
-------------------------------------------------------------
Reproducing the old table at the retired pin does not recover two of its
figures:

    1 + q0             published 2.10997859556   retired gives 2.10997859555
    log(1/hbar_q)      published 2.31181024982   retired gives 2.31181024985
    log(1 + q0)        published 0.74667780313   retired gives 0.74667780315

`1e-11` to `3e-11`. Small, real, and independent of the pin question — they were
wrong at their own anchor. The refresh corrects them by construction; recorded so
the diff is not mistaken for a larger pin effect than it is.

A fourth discrepancy is **not** an error: `q [9]_q [10]_q` published
`136.823219654` against `136.823219654561` is a **truncation**, a legitimate
rendering, and it is the same one that defeats a half-ulp matcher — see
`scripts/witness-block-agreement.py`. Distinguishing the two cases is the whole
point of checking against the unrounded value rather than the printed one.

SCOPE
-----
Closed-form figures only. `E_0`, `Q_beta` and the spectral-bridge quantities are
producer outputs whose values also depend on the trace convention, and the
qbeta channel's C->D migration is `qou-cds1`'s; refreshing a pin under a
convention that is itself about to change would produce numbers nobody has
checked. Those blocks are handled from their producers, not here.
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

mp.mp.dps = 60

# reference-literal-intentional: the RETIRED pin is this probe's SUBJECT, not
# an input — the whole point is to measure it against the live muon pin below.
# Routing it to the registry would delete the comparison.
RETIRED = mp.mpf("1.1099785955541805752815940796095093779932822799587")
MUON = mp.mpf("1.109978595642739046681795129380001752700065561029011556974045769999095")


def qint(n, q):
    """Balanced quantum integer `[n]_q = (q^n - q^-n)/(q - q^-1)`."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def hecke_log_rows(q):
    """`tbl:hecke-log-decomposition-table-data` — all seven rows are q0-derived."""
    h, hb = q - 1 / q, (q - 1) / q
    return [
        ("h(q_0)", h, 11),
        ("hbar_q(q_0) = (q_0-1)/q_0", hb, 11),
        ("1 + q_0", 1 + q, 11),
        ("log(1/h(q_0))", mp.log(1 / h), 11),
        ("log(1/hbar_q(q_0))", mp.log(1 / hb), 11),
        ("log(1 + q_0)", mp.log(1 + q), 11),
        ("log(1/hbar_q) - log(1+q_0)", mp.log(1 / hb) - mp.log(1 + q), 11),
    ]


def bring_zero_mode_rows(q):
    """`prop:em-coupling-bring-zero-mode`. `2/(3pi)` is a CONSTANT and is fixed."""
    bare = q * qint(9, q) * qint(10, q)
    zm = 2 / (3 * mp.pi)
    total = bare + zm
    codata = mp.mpf("137.035999177")
    resid = (total - codata) / codata
    alpha_4pi = 1 / (codata * 4 * mp.pi)
    total2 = total + alpha_4pi
    return [
        ("q [9]_q [10]_q", bare, 9),
        ("2/(3 pi)  [CONSTANT, fixed]", zm, 9),
        ("sum", total, 9),
        ("residual relative", resid, None),
        ("alpha/(4 pi)", alpha_4pi, None),
        ("residual after second term", (total2 - codata) / codata, None),
    ]


def qbeta_form_a_closed_rows(q):
    """The CLOSED-FORM subset of `tbl:q-beta-form-a-n1-symbolic-table-data`.

    `E_0` and `Q_beta` are producer outputs and convention-dependent; they are
    deliberately absent. See the module docstring.
    """
    hb = (q - 1) / q
    return [
        ("hbar_q = (q-1)/q", hb, 15),
        ("1 + hbar_q^2", 1 + hb ** 2, 15),
        ("per-braid N=1 ceiling hbar_q^4/(1-hbar_q^2) [ppm]",
         hb ** 4 / (1 - hb ** 2) * 10 ** 6, 1),
    ]


BLOCKS = {
    "tbl:hecke-log-decomposition-table-data": hecke_log_rows,
    "prop:em-coupling-bring-zero-mode": bring_zero_mode_rows,
    "tbl:q-beta-form-a-n1-symbolic-table-data (closed-form subset)":
        qbeta_form_a_closed_rows,
}

#: What each block published at the retired pin, for the reproduction check.
PUBLISHED = {
    "tbl:hecke-log-decomposition-table-data": {
        "h(q_0)": "0.20906032199", "hbar_q(q_0) = (q_0-1)/q_0": "0.09908172644",
        "1 + q_0": "2.10997859556", "log(1/h(q_0))": "1.56513244670",
        "log(1/hbar_q(q_0))": "2.31181024982", "log(1 + q_0)": "0.74667780313",
        "log(1/hbar_q) - log(1+q_0)": "1.56513244670"},
    "prop:em-coupling-bring-zero-mode": {
        "q [9]_q [10]_q": "136.823219654", "2/(3 pi)  [CONSTANT, fixed]": "0.212206591",
        "sum": "137.035426245"},
    "tbl:q-beta-form-a-n1-symbolic-table-data (closed-form subset)": {
        "hbar_q = (q-1)/q": "0.099081726435699",
        "1 + hbar_q^2": "1.009817188513479"},
}


def fmt(v, dp):
    return mp.nstr(v, 12) if dp is None else f"{mp.mpf(v):.{dp}f}"


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\n  retired  {mp.nstr(RETIRED, 25)}")
    print(f"  muon     {mp.nstr(MUON, 25)}   <- refresh target")
    print(f"  relative move  {mp.nstr(abs(MUON - RETIRED) / MUON, 6)}")

    results = {}
    slips = []
    truncations = []
    for block, fn in BLOCKS.items():
        print("\n" + "=" * 78)
        print(f"  {block}")
        print("=" * 78)
        old, new = fn(RETIRED), fn(MUON)
        pub = PUBLISHED.get(block, {})
        print(f"    {'row':<48} {'published':>18} {'REFRESHED':>18}")
        rows = []
        for (name, ov, dp), (_n, nv, _d) in zip(old, new):
            o, n = fmt(ov, dp), fmt(nv, dp)
            p = pub.get(name)
            mark = ""
            if p is not None and p != o and dp is not None:
                # Distinguish a TRUNCATION -- a legitimate rendering, where
                # published <= true < published + 10^-dp -- from a genuine slip,
                # which is neither the rounding nor the truncation of its own
                # anchor's value. Only the second is an error.
                tr = mp.mpf(p) <= ov < mp.mpf(p) + mp.mpf(10) ** (-dp)
                if tr:
                    mark = "  <- truncation, not an error"
                    truncations.append((block, name, p, o))
                else:
                    mark = "  <- published != retired (pre-existing SLIP)"
                    slips.append((block, name, p, o))
            print(f"    {name:<48} {(p or o):>18} {n:>18}{mark}")
            rows.append({"row": name, "published": p, "at_retired_pin": o,
                         "refreshed_at_muon_pin": n})
        results[block] = rows

    print("\n" + "=" * 78)
    print("§A  EVERY ROW MOVES — WHICH IS WHY THE UNIT IS THE BLOCK")
    print("=" * 78)
    hl_old, hl_new = hecke_log_rows(RETIRED), hecke_log_rows(MUON)
    moved = sum(1 for (n, o, d), (_, v, _) in zip(hl_old, hl_new)
                if fmt(o, d) != fmt(v, d))
    print(f"    hecke-log-decomposition: {moved} of {len(hl_old)} rows change")
    print(f"    the sweep flagged only 3 — refreshing those alone would leave "
          f"{moved - 3} siblings")
    print(f"    at the old pin in the same table, which is worse than the stale "
          f"value.")
    check("all seven rows of hecke-log-decomposition move, so a figure-by-figure "
          "refresh would have broken the table's internal recomputability",
          moved == len(hl_old))

    print("\n" + "=" * 78)
    print("§B  CONSTANTS AND EXPERIMENTAL INPUTS DO NOT MOVE")
    print("=" * 78)
    zm_o = [v for n, v, d in bring_zero_mode_rows(RETIRED) if n.startswith("2/(3")][0]
    zm_n = [v for n, v, d in bring_zero_mode_rows(MUON) if n.startswith("2/(3")][0]
    print(f"    2/(3 pi)  retired {mp.nstr(zm_o, 12)}   muon {mp.nstr(zm_n, 12)}")
    check("2/(3 pi) is a pure constant and is identical at both pins — it must "
          "not be touched by the refresh", zm_o == zm_n)

    print("\n" + "=" * 78)
    print("§C  TWO PRE-EXISTING SLIPS, INDEPENDENT OF THE PIN")
    print("=" * 78)
    print("    SLIPS — neither the rounding nor the truncation of their own anchor:")
    for b, n, p, o in slips:
        print(f"      {n:<32} published {p}   at retired pin {o}")
    print("    TRUNCATIONS — a legitimate rendering, not an error:")
    for b, n, p, o in truncations:
        print(f"      {n:<32} published {p}   at retired pin {o}")
    check("three published figures are neither the rounding nor the truncation "
          "of the retired pin's own value — wrong at their own anchor by 1e-11 "
          "to 3e-11, independent of the pin question, and corrected here by "
          "construction", len(slips) == 3)
    check("the fourth discrepancy is a TRUNCATION and not an error — the same "
          "rendering that defeats a half-ulp matcher, documented in "
          "scripts/witness-block-agreement.py", len(truncations) == 1)

    print("\n" + "=" * 78)
    print("§D  MAGNITUDE — NOTHING PHYSICAL MOVES")
    print("=" * 78)
    zb_o = dict((n, v) for n, v, d in bring_zero_mode_rows(RETIRED))
    zb_n = dict((n, v) for n, v, d in bring_zero_mode_rows(MUON))
    print(f"    q0 itself                  {mp.nstr(abs(MUON-RETIRED)/MUON, 4)} relative")
    print(f"    alpha^-1 residual  retired {mp.nstr(zb_o['residual relative'], 6)}")
    print(f"                       muon    {mp.nstr(zb_n['residual relative'], 6)}")
    check("the refresh moves q0 by 8e-11 relative; the alpha^-1 residual stays at "
          "-4.2e-6 and no stated conclusion changes",
          abs(zb_o["residual relative"] - zb_n["residual relative"]) < mp.mpf("1e-9"))

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_content_block("tbl:hecke-log-decomposition-table-data")
        wb.set_description(
            "THE REFRESH. Recomputes every closed-form published figure that carried "
            "the retired q0 = 1.1099785955541805752... at the live muon pin "
            "1.109978595642739046681795129380001752700065561029011556974045769999095 "
            "from the canonical q-pinning-50-digit witness. The retired value is the "
            "CODATA-2018 vintage of the muon anchor and survives only in "
            "fsh-guts/deprecated/computations/; the 2026-08-15 substrate fix reached "
            "computations/ and tools/ but not content/. Refreshes per BLOCK, not per "
            "figure: an earlier pass substituted only the six sweep-flagged figures "
            "and was reverted because each table's other q0-derived rows were never "
            "flagged (the sweep looks for figures with NO provenance), leaving a "
            "table the reader could not recompute from itself. All seven rows of "
            "hecke-log-decomposition move, not the three flagged. Constants "
            "(2/(3pi)) and experimental inputs (CODATA 1/alpha, Q_beta^CODATA) are "
            "fixed and untouched. Two pre-existing transcription slips surfaced: "
            "1+q0 published 2.10997859556 where the retired pin gives ...555, and "
            "log(1/hbar_q) published 2.31181024982 where it gives ...985 -- 1e-11 "
            "and 3e-11, wrong at their own anchor and independent of the pin, "
            "corrected by construction. Nothing physical moves: q0 shifts 8e-11 "
            "relative and the alpha^-1 residual stays at -4.2e-6. E_0, Q_beta and "
            "the spectral-bridge quantities are OUT OF SCOPE -- producer outputs "
            "whose values also depend on the trace convention, and the qbeta C->D "
            "migration is qou-cds1's. qou-i229.")
        wb.add_data("pins", {
            "retired": mp.nstr(RETIRED, 50),
            "live_muon": mp.nstr(MUON, 50),
            "relative_move": mp.nstr(abs(MUON - RETIRED) / MUON, 8),
            "source": "computations/q-pinning-50-digit.witness.json",
        })
        for block, rows in results.items():
            wb.add_data(block.replace(":", "_").replace(" ", "_"), rows)
        wb.add_data("pre_existing_slips", [
            {"block": b, "row": n, "published": p, "at_retired_pin": o}
            for b, n, p, o in slips])
        wb.add_data("truncations_not_errors", [
            {"block": b, "row": n, "published": p, "at_retired_pin": o}
            for b, n, p, o in truncations])
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Closed-form figures ONLY. E_0, Q_beta and the spectral-bridge "
            "quantities are producer outputs and convention-dependent; refreshing a "
            "pin under a convention that is itself about to change would produce "
            "numbers nobody has checked. Those come from their producers.")
        wb.add_caveat(
            "Constants and experimental inputs are deliberately NOT refreshed: "
            "2/(3pi), CODATA 1/alpha = 137.035999177(21), Q_beta^CODATA. A refresh "
            "that moved them would be a different and wrong change.")
        print(f"\nWitness: {wb.save(extra={"q0Anchor": "ambiguous", "q0AnchorReason": 'compares two pins on purpose: the retired CODATA-2018 muon pin 1.10997859555418... and the live muon pin 1.10997859564273...; it recomputes each published figure at both, so no single pin applies'})}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
