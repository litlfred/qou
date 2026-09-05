"""O3' selects a block, but NOT the bound state's block — argmin t = argmin w.

Follows PR #6752 (merged), which established that the O3' quotient program
prices its net constraint (y_0* nonzero where the full LP has y_0* = 0
identically) and that its optimum is supported on argmin_lambda t_lambda.  That
PR then read the selection as "which Wedderburn blocks the bound state actually
saturates" -- the corpus's own physical framing.

THIS PROBE TESTS THAT READING, AND IT FAILS.

The objective coefficient factors as

    t_lambda = w_lambda * chi^lambda(W_atom)

where w_lambda is the Markov/Plancherel weight -- a function of the PARTITION
and q only, identical for every atom at a given n -- and chi^lambda(W_atom) is
the character, which is where all atom-dependence lives.

So the question is sharp: does the character move the argmin?

  * If argmin(t) != argmin(w) somewhere, the character selects and the block
    carries atom-specific content.
  * If argmin(t) == argmin(w) everywhere, the block is argmin of an
    ATOM-INDEPENDENT quantity -- a function of n alone -- and calling it "the
    block this bound state saturates" is wrong, because every bound state at
    that n gets the same block.

MEASURED: they agree in 6 of 6 committed rows.  The character never moves it.

Corroborated directly: the witness holds TWO atoms at n=3 and TWO at n=9.  Same
n, different atom, SAME selected block -- while the PRICE differs (0.4470 vs
0.4206 at n=3; 0.01655 vs 0.02879 at n=9).  So the price is atom-dependent and
the block is not.

WHY w WINS -- UNEXPLAINED, and my first explanation is REFUTED BY THIS PROBE.

The obvious mechanism is spread dominance: at n=6 the surviving w span 0.0151 ->
0.1153 (7.6x) while the characters span 1.560 -> 4.249 (2.7x), so w would move
the product more than chi can.  That is what this probe originally asserted.

IT IS FALSE.  Measured here, chi-spread EXCEEDS w-spread at n = 9:

    row 2  n=6    w-spread  7.625x   chi-spread   2.724x
    row 3  n=9    w-spread  5.915x   chi-spread   6.448x
    row 4  n=9    w-spread  5.915x   chi-spread   6.712x
    row 5  n=12   w-spread 17.34x    chi-spread  12.51x

and the argmin is unmoved anyway.  So spread dominance is not the mechanism, and
the assertion that it was now fails by design in this probe rather than being
quietly dropped.

WHAT THE MECHANISM IS: OPEN.  Spread is a marginal statistic and the product's
argmin depends on how w and chi are CORRELATED across partitions, not on their
ranges separately.  A second guess is not offered here -- the corpus's standing
discipline is that an unexplained regularity is information and a replacement
mechanism invented to fit six rows is not.

WHAT SURVIVES FROM #6752, AND WHAT DOES NOT
-------------------------------------------
SURVIVES: O3' prices its net constraint.  y_0* = min t_lambda is nonzero on
every row and DOES vary by atom, where the full NF-indexed LP has y_0* = 0
identically for every atom and every n_target.  That was the defect O3' was
chosen to repair and the repair is real.

DOES NOT: the reading that the selected block answers "which Wedderburn blocks
the bound state actually saturates".  It does not.  The block is a function of
n, and at fixed n it is the same for the proton, the neutron, and every other
atom the witness carries.

FALSIFIER FOR THIS PROBE'S OWN CLAIM
------------------------------------
A single row where argmin(t) != argmin(w) would refute it.  Six rows agree; the
probe asserts that and would fail loudly on the seventh row that disagreed.
Note the sample is what the corpus has computed -- 6 rows over 4 distinct n --
and a character large enough to overturn a 7.6x weight spread is not excluded by
these rows, only unobserved in them.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401,E402

from mpmath import mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""),
          flush=True)


WIT = HERE.parent / "a-K-via-lp-dual-full.witness.json"


def main() -> int:
    rows = json.load(WIT.open())["data"]["rows"]
    print(f"=== does the character move O3''s argmin? — {len(rows)} rows ===",
          flush=True)

    out, by_n = [], {}
    agree = 0
    for idx, r in enumerate(rows):
        surv = [p for p in r["per_partition"] if mp.mpf(p["y_lambda"]) != 0]
        n = sum(surv[0]["partition"])
        arg_t = min(surv, key=lambda p: mp.mpf(p["contribution"]))
        arg_w = min(surv, key=lambda p: mp.mpf(p["y_lambda"]))
        same = arg_t["partition"] == arg_w["partition"]
        agree += same

        w_vals = [mp.mpf(p["y_lambda"]) for p in surv]
        c_vals = [abs(mp.mpf(p["chi_lambda"])) for p in surv]
        w_spread = max(w_vals) / min(w_vals)
        c_spread = max(c_vals) / min(c_vals)

        print(f"  row {idx}  n={n:<3} argmin(t)={str(arg_t['partition']):>10} "
              f"argmin(w)={str(arg_w['partition']):>10}  same={same}  "
              f"w-spread={mp.nstr(w_spread, 4)}x  chi-spread={mp.nstr(c_spread, 4)}x",
              flush=True)

        by_n.setdefault(n, []).append(
            (str(arg_t["partition"]), fmt(mp.mpf(arg_t["contribution"]))))
        out.append({
            "row": idx, "n": n, "n_survivors": len(surv),
            "argmin_t": arg_t["partition"], "argmin_w": arg_w["partition"],
            "same": same,
            "price_t_min": fmt(mp.mpf(arg_t["contribution"])),
            "w_spread": fmt(w_spread), "chi_spread": fmt(c_spread),
        })

    print(flush=True)
    check("argmin(t) == argmin(w) on EVERY row — the character never moves the "
          "selection", agree == len(rows), f"{agree}/{len(rows)}")

    multi = {n: v for n, v in by_n.items() if len(v) > 1}
    same_block = all(len({b for b, _ in v}) == 1 for v in multi.values())
    diff_price = all(len({p for _, p in v}) > 1 for v in multi.values())
    check("same n, different atoms -> SAME selected block", same_block,
          f"n in {sorted(multi)}")
    check("same n, different atoms -> DIFFERENT price, so the price IS "
          "atom-dependent", diff_price)
    # NOT an assertion that w dominates -- that was the first guess and it is
    # false.  Assert the REFUTATION, so the negative is carried by the probe.
    counterex = [r for r in out
                 if mp.mpf(r["chi_spread"]) > mp.mpf(r["w_spread"])]
    check("the spread-dominance explanation is REFUTED — chi-spread exceeds "
          "w-spread on at least one row and the argmin is unmoved anyway, so "
          "the mechanism is NOT that w varies more",
          len(counterex) > 0,
          f"{len(counterex)} counterexample row(s): n="
          f"{sorted({r['n'] for r in counterex})}")

    w = WitnessBuilder("o3prime-selection-is-atom-independent",
                       engine="python+mpmath")
    w.set_description(
        "O3' selects a block, but NOT the bound state's block. The objective "
        "t_lambda = w_lambda * chi^lambda(W_atom) factors into an "
        "atom-INDEPENDENT weight and an atom-dependent character; measured over "
        "all six committed rows, argmin(t) == argmin(w) every time, so the "
        "character never moves the selection. Two atoms at n=3 and two at n=9 "
        "give the SAME block with DIFFERENT prices. Mechanism UNEXPLAINED: the "
        "obvious spread-dominance account is refuted here -- chi-spread exceeds "
        "w-spread at n=9 and the argmin is unmoved anyway. CONSEQUENCE: PR #6752's "
        "reading of the selection as 'which Wedderburn blocks the bound state "
        "saturates' is WRONG and is corrected; the pricing result (y_0* nonzero "
        "and atom-dependent, where the full LP has y_0* = 0 identically) STANDS."
    )
    w.set_audit_only(
        "docs/proposals/2026-09-05-operator-selection-objective-replacement.md")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("rows", out)
    for name, ok in CHECKS:
        w.add_assertion(name, computed="1" if ok else "0", expected="1",
                        tolerance="0",
                        source="o3prime_selection_is_atom_independent_probe")
    print(f"\n  witness: {w.save()}", flush=True)
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed",
          flush=True)
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
