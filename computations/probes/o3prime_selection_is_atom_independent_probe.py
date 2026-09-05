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

WHY w WINS -- MEASURED BELOW; my first explanation is REFUTED BY THIS PROBE.

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

THE MECHANISM, MEASURED: w AND chi ARE ANTI-CORRELATED.

Spread is a marginal statistic; the product's argmin turns on how w and chi are
CORRELATED across partitions, not on their ranges separately.  Measured here,
they are systematically anti-correlated -- of the C(k,2) partition pairs on a
row, the fraction ordered the SAME way by w and by chi sits far below the 1/2
expected if the chi-ordering were unrelated to the w-ordering:

    row  n   k  pairs  concordant   w-spr  chi-spr  t-spr   flat   P(conc<=obs)
      0  3   2      1    0 (  0 %)   2.044    1.308  1.563  1.308x       1/2
      1  3   2      1    0 (  0 %)   2.044    1.516  1.348  1.516x       1/2
      2  6   4      6    1 ( 17 %)   7.625    2.724  3.951  1.930x       1/6
      3  9   5     10    2 ( 20 %)   5.915    6.448  4.696  1.259x      7/60
      4  9   5     10    1 ( 10 %)   5.915    6.712  4.266  1.386x      1/24
      5 12   7     21    5 ( 24 %)  17.34    12.51  10.18   1.703x    49/720

    aggregate 9/49 = 18 % concordant, against 24.5 expected under the null.

The last column is exact and distribution-free: P(concordant <= observed) when
the chi-ordering is a uniform random permutation of the w-ordering, computed by
enumerating all k! permutations -- no normality, no large-k limit, no fitted
parameter.  Multiplying the four DISTINCT values of n, taking the LEAST extreme
row within each n (rows 0/1 share n=3 and rows 3/4 share n=9, and two atoms'
characters at the same n are plausibly correlated, so treating those as
independent draws would overstate the evidence):

    1/2 * 1/6 * 7/60 * 49/720 = 343/518400 ~ 6.6e-4.

The all-six-rows product is 343/24883200 ~ 1.4e-5, and is reported alongside it
as the ANTI-CONSERVATIVE figure rather than as the result.

The consequence is in the t-spr and flat columns: the product is FLATTENED
relative to w on every row (t-spread < w-spread; flat = w-spread/t-spread > 1),
never amplified.  A large character lands preferentially on a small weight and
partly cancels it.  That is why chi-spread exceeding w-spread at n = 9 fails to
overturn the argmin -- chi is not an independent perturbation that might happen
to point the other way, it is a partial cancellation of the very ordering it
would have to reverse.

The cancellation is INCOMPLETE -- t-spread stays well above 1 on every row
(1.35x to 10.2x) -- so w's ordering survives into the product.  Complete
cancellation would flatten t to a constant and make the argmin arbitrary; that
is not what happens, and it is why the selection is stable rather than noise.

Both facts are asserted below and fail loudly on a row that breaks either.

The factorisation the whole account rests on is checked, not assumed: |t| =
w * |chi| holds in the committed data to 4e-50 relative, i.e. to the witness's
serialisation floor.

WHY THE ANTI-CORRELATION HOLDS: it REDUCES to the content sum.

w is a strictly increasing function of the content sum c(lambda) -- 49 of 49
pairs concordant, EVERY pair on EVERY row, no exceptions.  So ordering the
survivors by w IS ordering them by c(lambda), and

    conc(w, |chi|)  ==  conc(c(lambda), |chi|)   identically, row by row

-- not approximately, not on aggregate: the same integer on all six rows
(0/1, 0/1, 1/6, 2/10, 1/10, 5/21).  Both are asserted below.  The w-vs-chi
anti-correlation is therefore not a fact about the Markov weight at all; it is
a fact about the CONTENT SUM against the character, wearing w as a monotone
reparametrisation.

That decomposes it into three links, of which the first is exact:

    c(lambda) up  =>  w up          49/49 = 100.0 %  (exact, asserted)
    c(lambda) up  =>  dim down       6/49 =  12.2 %  (combinatorial)
    dim up        =>  |chi| up      43/49 =  87.8 %

For two-row partitions the middle link is the elementary one: [n] has the
largest content sum and dimension 1, and the balanced partition has the
smallest content sum and the largest dimension.  The third is the near-triviality
that a character of a bigger irrep is a sum of more terms.  Composing:
w up => c up => dim down => |chi| down.

The 87.8 % link is the weakest and its exception is named rather than averaged
away: row 2 (n = 6) sits at exactly 3/6, i.e. dim and |chi| are UNCORRELATED
there, and it is also the row with the largest flattening (1.93x).  The other
five rows run 1/1, 1/1, 9/10, 10/10, 19/21.

w is NOT simply q^c(lambda).  The residual w * q^-c(lambda) is unimodal in the
content sum, moving 12.9x across row 5 (peak at [8,4]) -- so the monotonicity
above is a real fact about the weight, in which the q^c factor dominates a
non-monotone correction, and not an identity read off a closed form.

WHAT IS STILL OPEN, after that reduction: whether the 87.8 % dim-vs-|chi| link is
exact-with-a-degenerate-case or genuinely only statistical, and what n = 6 is
doing.  Six rows over four n cannot separate those.

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
from fractions import Fraction
from itertools import permutations
from math import factorial
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


def concordant(a: list, b: list) -> tuple[int, int]:
    """(#pairs ordered the same way by a and by b, #pairs).

    Sign comparison only, so exact-integer inputs (content sums, SYT counts)
    stay exact integers and never enter mpmath -- both cleaner and outside the
    f64-into-mpmath detector's reach.
    """
    k = len(a)
    pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
    return (sum(1 for i, j in pairs
                if (a[i] > a[j]) == (b[i] > b[j]) and a[i] != a[j] and b[i] != b[j]),
            len(pairs))


def f_lambda(lam: tuple[int, ...]) -> int:
    """#SYT(lambda) = dim of the S_n irrep, exact integer by hook lengths."""
    d = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            d *= arm + leg + 1
    return factorial(sum(lam)) // d


def tau_tail(k: int, obs: int) -> Fraction:
    """Exact P(concordant pairs <= obs) when the chi-ordering is a uniform
    random permutation of the w-ordering.

    Distribution-free and exact: enumerates all k! permutations.  k <= 7 here
    (5040 perms), so this is cheap.  Returns a Fraction, never a float --
    the corpus's NO-FLOAT64 discipline applies to a p-value as much as to a
    physical quantity.
    """
    hits = sum(1 for p in permutations(range(k))
               if sum(1 for i in range(k) for j in range(i + 1, k)
                      if p[i] < p[j]) <= obs)
    return Fraction(hits, factorial(k))


WIT = HERE.parent / "a-K-via-lp-dual-full.witness.json"


def main() -> int:
    rows = json.load(WIT.open())["data"]["rows"]
    print(f"=== does the character move O3''s argmin? — {len(rows)} rows ===",
          flush=True)

    out, by_n, tails, chain = [], {}, {}, []
    agree = 0
    fact_max = mp.mpf(0)
    for idx, r in enumerate(rows):
        surv = [p for p in r["per_partition"] if mp.mpf(p["y_lambda"]) != 0]
        n = sum(surv[0]["partition"])
        arg_t = min(surv, key=lambda p: mp.mpf(p["contribution"]))
        arg_w = min(surv, key=lambda p: mp.mpf(p["y_lambda"]))
        same = arg_t["partition"] == arg_w["partition"]
        agree += same

        w_vals = [mp.mpf(p["y_lambda"]) for p in surv]
        c_vals = [abs(mp.mpf(p["chi_lambda"])) for p in surv]
        t_vals = [abs(mp.mpf(p["contribution"])) for p in surv]
        w_spread = max(w_vals) / min(w_vals)
        c_spread = max(c_vals) / min(c_vals)
        t_spread = max(t_vals) / min(t_vals)

        # The mechanism is a CORRELATION between w and chi, not a ratio of
        # their ranges.  Count concordant pairs and price the count exactly.
        k = len(surv)
        pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
        conc = sum(1 for i, j in pairs
                   if (w_vals[i] - w_vals[j]) * (c_vals[i] - c_vals[j]) > 0)
        tail = tau_tail(k, conc)
        tails.setdefault(n, []).append(tail)

        # WHY: w is a monotone reparametrisation of the content sum, so the
        # anti-correlation is really content-vs-character.  Content sums and
        # SYT counts stay exact ints; only w and chi are mpf.
        cs = [p["content_sum"] for p in surv]
        dim = [f_lambda(tuple(p["partition"])) for p in surv]
        c_cs_w, _ = concordant(cs, w_vals)
        c_cs_chi, _ = concordant(cs, c_vals)
        c_cs_dim, _ = concordant(cs, dim)
        c_dim_chi, _ = concordant(dim, c_vals)
        chain.append({"cs_w": c_cs_w, "cs_chi": c_cs_chi, "cs_dim": c_cs_dim,
                      "dim_chi": c_dim_chi, "pairs": len(pairs),
                      "w_chi": conc})

        # |t| = w * |chi| is what the whole account rests on -- check it here
        # rather than assuming it from the algebra.
        fact_err = max((abs(t_vals[i] - w_vals[i] * c_vals[i]) / t_vals[i]
                        if t_vals[i] != 0 else mp.mpf(0)) for i in range(k))
        fact_max = max(fact_max, fact_err)

        print(f"  row {idx}  n={n:<3} argmin(t)={str(arg_t['partition']):>10} "
              f"argmin(w)={str(arg_w['partition']):>10}  same={same}  "
              f"w-spread={mp.nstr(w_spread, 4)}x  chi-spread={mp.nstr(c_spread, 4)}x  "
              f"t-spread={mp.nstr(t_spread, 4)}x  flat={mp.nstr(w_spread / t_spread, 4)}x  "
              f"conc={conc}/{len(pairs)}  P={tail}",
              flush=True)

        by_n.setdefault(n, []).append(
            (str(arg_t["partition"]), fmt(mp.mpf(arg_t["contribution"]))))
        out.append({
            "row": idx, "n": n, "n_survivors": len(surv),
            "argmin_t": arg_t["partition"], "argmin_w": arg_w["partition"],
            "same": same,
            "price_t_min": fmt(mp.mpf(arg_t["contribution"])),
            "w_spread": fmt(w_spread), "chi_spread": fmt(c_spread),
            "t_spread": fmt(t_spread), "flattening": fmt(w_spread / t_spread),
            "n_pairs": len(pairs), "concordant": conc,
            "tau_tail": str(tail),
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

    # The mechanism that DOES hold, asserted so it fails loudly if a seventh
    # row breaks it.
    anti = [r for r in out if 2 * r["concordant"] < r["n_pairs"]]
    check("w and chi are ANTI-correlated on EVERY row — concordant pairs fall "
          "below the independent expectation of half, so a large character "
          "lands preferentially on a small weight",
          len(anti) == len(out),
          f"{sum(r['concordant'] for r in out)}/{sum(r['n_pairs'] for r in out)}"
          f" = {sum(r['concordant'] for r in out) * 100 // sum(r['n_pairs'] for r in out)}%"
          f" concordant vs {sum(r['n_pairs'] for r in out) / 2:.1f} expected")

    flat = [r for r in out if mp.mpf(r["flattening"]) > 1]
    check("the product is FLATTENED relative to w on EVERY row — chi partly "
          "CANCELS the weight ordering rather than adding to it, and the "
          "cancellation is incomplete, so w's argmin survives into t",
          len(flat) == len(out),
          "flattening " + ", ".join(mp.nstr(mp.mpf(r["flattening"]), 4)
                                    for r in out) + "x")

    # WHY it holds: w is a monotone reparametrisation of the content sum, so
    # the whole effect is content-vs-character.  Two EXACT facts, asserted.
    mono = [c for c in chain if c["cs_w"] == c["pairs"]]
    check("w is a strictly INCREASING function of the content sum on EVERY row "
          "— so ordering the survivors by w IS ordering them by c(lambda)",
          len(mono) == len(chain),
          f"{sum(c['cs_w'] for c in chain)}/{sum(c['pairs'] for c in chain)} "
          f"pairs concordant")

    ident = [c for c in chain if c["cs_chi"] == c["w_chi"]]
    check("conc(w, |chi|) == conc(c(lambda), |chi|) IDENTICALLY on every row — "
          "the anti-correlation is a fact about the CONTENT SUM against the "
          "character, not about the Markov weight",
          len(ident) == len(chain),
          "w~chi " + ",".join(str(c["w_chi"]) for c in chain)
          + "  vs  cs~chi " + ",".join(str(c["cs_chi"]) for c in chain))

    tp = sum(c["pairs"] for c in chain)
    print(f"\n  the reduction, as three links over {tp} pairs:"
          f"\n    c(lambda) up  =>  w up      {sum(c['cs_w'] for c in chain):>3}/{tp}"
          f"  = {sum(c['cs_w'] for c in chain) * 100 // tp:>3}%   (exact)"
          f"\n    c(lambda) up  =>  dim down  {sum(c['cs_dim'] for c in chain):>3}/{tp}"
          f"  = {sum(c['cs_dim'] for c in chain) * 100 // tp:>3}%   (combinatorial)"
          f"\n    dim up        =>  |chi| up  {sum(c['dim_chi'] for c in chain):>3}/{tp}"
          f"  = {sum(c['dim_chi'] for c in chain) * 100 // tp:>3}%   (weakest link;"
          f" per row " + ",".join(f"{c['dim_chi']}/{c['pairs']}" for c in chain) + ")",
          flush=True)

    # Conservative: one row per distinct n, the LEAST extreme in each group.
    # Two atoms at the same n plausibly have correlated characters, so
    # multiplying all six would overstate the evidence.
    p_cons = Fraction(1)
    for _n, ts in sorted(tails.items()):
        p_cons *= max(ts)
    p_all = Fraction(1)
    for _n, ts in sorted(tails.items()):
        for t in ts:
            p_all *= t
    print(f"\n  anti-correlation, exact and distribution-free:"
          f"\n    conservative (one row per n, least extreme) = {p_cons}"
          f" ~ {float(p_cons):.2e}   <- the result"
          f"\n    all six rows (assumes more independence)    = {p_all}"
          f" ~ {float(p_all):.2e}"
          f"\n  |t| = w*|chi| max relative residual = {mp.nstr(fact_max, 3)}"
          f"  (serialisation floor)", flush=True)

    w = WitnessBuilder("o3prime-selection-is-atom-independent",
                       engine="python+mpmath")
    w.set_description(
        "O3' selects a block, but NOT the bound state's block. The objective "
        "t_lambda = w_lambda * chi^lambda(W_atom) factors into an "
        "atom-INDEPENDENT weight and an atom-dependent character; measured over "
        "all six committed rows, argmin(t) == argmin(w) every time, so the "
        "character never moves the selection. Two atoms at n=3 and two at n=9 "
        "give the SAME block with DIFFERENT prices. Mechanism UNEXPLAINED: the "
        "first spread-dominance account is refuted here -- chi-spread exceeds "
        "w-spread at n=9 and the argmin is unmoved anyway. THE MECHANISM THAT DOES "
        "hold is an ANTI-CORRELATION between w and chi: concordant partition "
        "pairs are 9/49 = 18% against 24.5 expected, so a large character lands "
        "preferentially on a small weight and the product is FLATTENED relative "
        "to w on every row (never amplified) -- chi is a partial cancellation of "
        "the ordering it would have to reverse, not an independent perturbation. "
        "Exact distribution-free tail, one row per distinct n and the least "
        "extreme within each: 343/518400 ~ 6.6e-4. Cancellation is INCOMPLETE "
        "(t-spread 1.35x-10.2x), so w's argmin survives. WHY the anti-correlation "
        "holds REDUCES to the content sum: w is a strictly increasing function "
        "of c(lambda) on 49/49 pairs, so conc(w,|chi|) == conc(c(lambda),|chi|) "
        "IDENTICALLY row by row, and the effect decomposes as c up => w up "
        "(49/49 exact), c up => dim down (6/49), dim up => |chi| up (43/49). "
        "For two-row partitions [n] has max content and dim 1 while the balanced "
        "partition has min content and max dim. Still open: whether the 43/49 "
        "link is exact-with-a-degenerate-case (n=6 sits at exactly 3/6) or only "
        "statistical. CONSEQUENCE: PR #6752's "
        "reading of the selection as 'which Wedderburn blocks the bound state "
        "saturates' is WRONG and is corrected; the pricing result (y_0* nonzero "
        "and atom-dependent, where the full LP has y_0* = 0 identically) STANDS."
    )
    w.set_audit_only(
        "docs/proposals/2026-09-05-operator-selection-objective-replacement.md")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("rows", out)
    w.add_data("content_sum_reduction", chain)
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
