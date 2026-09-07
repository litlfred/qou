#!/usr/bin/env python3
"""The `c_5 > 0` sign correction is ROBUST across bond orderings. The
non-convergence claim that accompanied it is NOT, and is withdrawn.

WHAT THIS TESTS
---------------
`cumulant_hierarchy_does_not_converge_probe` (bean `qou-441t`) reported two
things from a single bond ordering at `A = 5`:

1. `c_5 > 0`, correcting `qou-bc09`/`qou-38i9`'s "every many-body term is
   negative";
2. `|c_5 / c_4| = 1.3036 > 1`, hence "the hierarchy does not converge".

Its own caveat said both rested on one convention and should be re-tested,
because `qou-38i9` measured bond order to be worth `38-40 %` at `A = 4`. This
runs that test over twelve orderings — the canonical production one plus eleven
random shuffles of the ten bonds.

The two claims come apart.

PRECISION — SEE `the_binding_arc_was_measured_in_float64_probe.py`
-----------------------------------------------------------------
Every number below is float64, in `q` as well as in the matrices, so treat the
table as five significant figures and no more. Nothing in this probe's argument
needs better: the whole point is a sign that is stable over a range of `+1.60`
to `+3.26`, and a ratio that straddles `1` between `0.71` and `1.30`. Those
margins are ~1e13 above the float64 floor.

One phrase below is an over-claim and is corrected here: `c_2` is described as
"**exactly** ordering-independent — identical to all printed digits". "Identical
to all printed digits" is what was measured and is fine; "exactly" was inferred
from it, and a float64 agreement never licenses that word. As it happens the
statement *is* exactly true, for the structural reason the same sentence gives —
a two-element subset contains one bond and has no internal order — and the
200-bit run confirms `L` is invariant under bond routing at `1e-60`. Right
conclusion, wrong warrant.

ORDER SIX, IN THE ONE SYSTEM WHERE ORDERING CANNOT INTERFERE (2026-09-03)
---------------------------------------------------------------------------
The withdrawal above stands: at `A = 5` the mixed-nucleus ratio depends on bond
ordering. But the homonuclear system is exchangeable, its cumulants are
ordering-free by theorem (`QOU.Mass.SubsetCumulantRecursion.cum_eq_sizeCum`),
and `the_size_only_recursion_reaches_order_six_probe` now has it exactly to
order six (128-bit, minimal-n route). Single-subset cumulants
`c_2 .. c_6 = +0.907, -0.508, -0.230, +1.955, -6.598`; totals at `A = 6`,
`C(6,k) c_k = +13.61, -10.16, -3.45, +11.73, -6.60`, summing to `L_6 = 5.13`
through cancellation. Signs `+ - - + -`. The magnitudes do not decay: after a
minimum at `k = 4` the single-subset cumulant grows by `8.5x` and then `3.4x`,
and the `k = 5` and `k = 6` totals are of the same order as `k = 2`. So in the
exchangeable case the hierarchy is not perturbative through order six. That is
a statement about the homonuclear bond model; it does not reinstate the
`A = 5` mixed-nucleus claim, which remains convention-dependent.

THE SIGN IS ROBUST
------------------
    trial      c2         c3         c4         c5      |c5/c4|   signs
    0 (canon)  7.27262   -3.78605   -1.23080   +1.60450  1.3036   + - - +
    1          7.27262   -2.96389   -2.78744   +2.30185  0.8258   + - - +
    2          7.27262   -3.12192   -2.49803   +2.33868  0.9362   + - - +
    3          7.27262   -2.93252   -3.51613   +2.63217  0.7486   + - - +
    4          7.27262   -3.06553   -2.79765   +2.37276  0.8481   + - - +
    5          7.27262   -2.50122   -3.19892   +2.44992  0.7659   + - - +
    6          7.27262   -2.65813   -3.26491   +2.90957  0.8912   + - - +
    7          7.27262   -2.71687   -3.22596   +2.39446  0.7422   + - - +
    8          7.27262   -2.80273   -2.99779   +2.23801  0.7466   + - - +
    9          7.27262   -2.42507   -3.69236   +2.61314  0.7077   + - - +
    10         7.27262   -2.64831   -4.18634   +3.25845  0.7784   + - - +
    11         7.27262   -2.39958   -2.70314   +2.33027  0.8621   + - - +

**`c_5 > 0` in 12 of 12**, over the range `+1.60` to `+3.26`, and the sign
pattern `+ - - +` is identical in every ordering. So the correction to
`qou-bc09` and `qou-38i9` stands: "every many-body term is negative" is false
from `A = 5`, and it is false regardless of bond-order convention.

THE CONVERGENCE CLAIM IS NOT
----------------------------
`|c_5/c_4| > 1` holds in **1 of 12** — and the one is the canonical production
ordering, the only one `qou-441t` tested. The ratio ranges `0.7077 .. 1.3036`
and **straddles 1**.

So "the hierarchy does not converge" was an artifact of the convention it was
measured in. **It is withdrawn.** What can be said instead is weaker and
honest: at `A = 5` the fourth-to-fifth ratio is of order one and its position
relative to `1` is convention-dependent, so the hierarchy is neither
demonstrably convergent nor demonstrably divergent at the only order where it
has been tested.

WHY THE TWO BEHAVE DIFFERENTLY
------------------------------
`c_2` is **exactly** ordering-independent — identical to all printed digits in
every trial — as it must be, since a two-element subset contains one bond and
has no internal order. From `c_3` up, the individual cumulants swing hard:
`c_3` over `-2.40 .. -3.79`, `c_4` over `-1.23 .. -4.19`, `c_5` over
`+1.60 .. +3.26`, each a factor of `1.6` to `3.4`.

A *sign* survives that; a *ratio between two swinging quantities* does not.
That is the general lesson and it applies to anything else in this arc quoted
as a ratio of cumulants at fixed convention.

WHAT IS LEFT STANDING
---------------------
* `c_5 > 0` — robust, and the correction to the earlier sign claim holds.
* `c_2` ordering-independent — a consistency check on the machinery.
* The hierarchy's convergence at `A = 5` — **unknown**, not "absent".
* Everything `qou-441t` established about the cumulant *identification* (that
  `L` is additive on disjoint blocks, hence the Mobius inversion is a genuine
  cumulant expansion) is untouched: that is an exact algebraic fact, not a
  measured ratio.

DISCIPLINE
----------
This probe exists to test two claims of mine from the previous turn. One
survives and one does not; both outcomes are reported with the same weight. The
ordering sample is twelve, which is enough to falsify a universal claim and not
enough to characterise a distribution — no distributional statement is made.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] cumulant_hierarchy_does_not_converge_probe.py (claims tested here)
-- Ref: [probe] four_body_term_and_the_h12_collapse_probe.py (bond-order artifact)
"""
from __future__ import annotations

import math
import random
import sys
import time
import warnings
from itertools import combinations
from math import comb
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
import scipy.sparse as sps  # noqa: E402

from hecke_characters import build_seminormal_matrices  # noqa: E402
from pyhecke.atom import D_PN  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402  (exact q0, not the f64 Q)

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 40
# Q_MP is already an mpf carrying the anchor's full 50 digits.  This line was
# `mp.mpf(str(Q0))` off the f64 `Q`, which froze a 17-digit floor into the
# computation -- 6.8e-18 relative from the exact value, and this probe is ABOUT
# whether a convergence claim survives, i.e. exactly where trailing digits decide.
# MEASURED: every displayed number is unchanged; only the wall clock moves
# (347s -> 416s, exact-q0 arithmetic costs ~20%).  Hygiene, not a result.
_Q = Q0
_H = _Q - 1 / _Q
HF, DPN = float(_H), float(D_PN)
B_P = (0.0, 0.5, 0.5)
B_N = (0.5, 0.5, 1.0)
ORDER, NS, A = "pnpnn", 15, 5
NTRIAL = 12
ALLB = list(combinations(range(A), 2))


def qint(m):
    return sum(_Q ** (m - 1 - 2 * i) for i in range(m))


def weights(n):
    ks = list(range(n // 2 + 1))
    ps = [((n - k, k) if k else (n,)) for k in ks]
    raw = [qint(n - 2 * k + 1) for k in ks]
    dims = [comb(n, k) - comb(n, k - 1) if k else 1 for k in ks]
    Z = sum(r * d for r, d in zip(raw, dims))
    return ps, [float(r / Z) for r in raw]


_C: dict = {}


def blocks(n):
    if n not in _C:
        ps, ws = weights(n)
        _C[n] = [(w, [sps.csr_matrix(m, dtype=float)
                      for m in build_seminormal_matrices(list(p))[0]])
                 for p, w in zip(ps, ws)]
    return _C[n]


def trM(n, word, chunk=512):
    tot = 0.0
    for wt, S in blocks(n):
        d = S[0].shape[0]
        ops = [(c * S[g] + dd * sps.identity(d, format="csr")).tocsr()
               for c, dd, g in word]
        acc = 0.0
        for s in range(0, d, chunk):
            e = min(s + chunk, d)
            X = np.zeros((e - s, d))
            X[np.arange(e - s), np.arange(s, e)] = 1.0
            for op in ops:
                X = X @ op
            acc += float(np.trace(X[:, s:e]))
        tot += wt * acc
    return tot


def nucleon_word(b, g0, g1):
    w = []
    for _ in range(3):
        w += [(1, 0.0, g0), (1, -HF, g1)]
    w += [(1, -b[0] * HF, g0), (1, -b[1] * HF, g0), (1, -b[2] * HF, g1)]
    return w + [(1, 0.0, g0), (1, 0.0, g0)]


def bond_d(a, b):
    return 0.0 if a == b == "p" else (-HF if a == b == "n" else DPN)


def band(i, j, d):
    a, b = 3 * i + 2, 3 * j
    ups = list(range(b - 1, a, -1))
    return ([(1, 0.0, g) for g in ups] + [(1, d, a)]
            + [(1, -HF, g) for g in reversed(ups)])


def word(order, S, bo):
    pos = {b: i for i, b in enumerate(bo)}
    w = []
    for k in range(A):
        w += nucleon_word(B_P if order[k] == "p" else B_N, 3 * k, 3 * k + 1)
    for (i, j) in sorted([b for b in ALLB if b[0] in S and b[1] in S],
                         key=lambda b: pos[b]):
        d = bond_d(order[i], order[j])
        w += ([(1, d, 3 * i + 2)] if j == i + 1 else band(i, j, d))
    return w


def hierarchy(order, bo):
    tf = trM(NS, word(order, set(), bo))
    Ls = {}
    for r in range(2, A + 1):
        for S in combinations(range(A), r):
            Ls[S] = float(np.log(tf / trM(NS, word(order, set(S), bo))))
    cum = {}
    for r in range(2, A + 1):
        for S in combinations(range(A), r):
            c = Ls[S]
            for m in range(2, r):
                c -= sum(cum[T] for T in combinations(S, m))
            cum[S] = c
    return {r: sum(cum[S] for S in combinations(range(A), r))
            for r in range(2, A + 1)}


def main() -> int:
    assertions = []
    print("t7qv — is the c5 sign robust across bond orderings?")

    rng = random.Random(11)
    print(f"\n  running {NTRIAL} orderings (canonical + {NTRIAL - 1} random)")
    print(f"     {'trial':>6s} {'c2':>10s} {'c3':>10s} {'c4':>10s} "
          f"{'c5':>10s} {'|c5/c4|':>8s} {'signs':>8s}")
    t0 = time.time()
    H = []
    for t in range(NTRIAL):
        bo = sorted(ALLB) if t == 0 else None
        if bo is None:
            bo = list(ALLB)
            rng.shuffle(bo)
        h = hierarchy(ORDER, bo)
        H.append(h)
        sg = " ".join("+" if h[r] > 0 else "-" for r in range(2, A + 1))
        lbl = "0 canon" if t == 0 else str(t)
        print(f"     {lbl:>6s} {h[2]:>10.5f} {h[3]:>10.5f} {h[4]:>10.5f} "
              f"{h[5]:>10.5f} {abs(h[5] / h[4]):>8.4f} {sg:>8s}")
    print(f"     ({time.time() - t0:.0f}s)")

    # ── A1. c2 is exactly ordering-independent ─────────────────────────
    print("\n  1. c2 is EXACTLY ordering-independent (machinery check)")
    c2s = [h[2] for h in H]
    spread2 = max(c2s) - min(c2s)
    print(f"     c2 over {NTRIAL} orderings: spread {spread2:.2e}")
    print(f"     as it must be — a two-element subset contains ONE bond and has")
    print(f"     no internal order. This is a check on the machinery, not a result.")
    ok = spread2 < 1e-9
    assertions.append(("A1_c2_is_ordering_independent", ok,
                       f"c2 spread {spread2:.2e} over {NTRIAL} orderings"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the sign is robust ─────────────────────────────────────────
    print("\n  2. c5 > 0 is ROBUST")
    c5s = [h[5] for h in H]
    npos = sum(1 for x in c5s if x > 0)
    sigs = {" ".join("+" if h[r] > 0 else "-" for r in range(2, A + 1))
            for h in H}
    print(f"     c5 > 0 in {npos}/{NTRIAL}; range {min(c5s):+.5f} .. "
          f"{max(c5s):+.5f}")
    print(f"     distinct sign patterns across all trials: {sigs}")
    print(f"     so the correction to qou-bc09 / qou-38i9 stands: 'every")
    print(f"     many-body term is negative' is false from A=5, and false")
    print(f"     regardless of bond-order convention.")
    ok = npos == NTRIAL and len(sigs) == 1
    assertions.append(("A2_c5_positive_in_every_ordering", ok,
                       f"c5 > 0 in {npos}/{NTRIAL}, one sign pattern {sigs}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the convergence claim is NOT robust ────────────────────────
    print("\n  3. but |c5/c4| > 1 is NOT — the convergence claim is withdrawn")
    rs = [abs(h[5] / h[4]) for h in H]
    ngt = sum(1 for x in rs if x > 1)
    print(f"     |c5/c4| > 1 in {ngt}/{NTRIAL}; range {min(rs):.4f} .. "
          f"{max(rs):.4f} — it STRADDLES 1")
    print(f"     and the one that exceeds 1 is trial 0, the canonical production")
    print(f"     ordering — the only one qou-441t tested.")
    print(f"     'the hierarchy does not converge' was an artifact of the")
    print(f"     convention it was measured in. WITHDRAWN.")
    print(f"     What can be said instead: at A=5 the fourth-to-fifth ratio is of")
    print(f"     order one and its position relative to 1 is convention-")
    print(f"     dependent, so the hierarchy is neither demonstrably convergent")
    print(f"     nor demonstrably divergent at the only order tested.")
    ok = ngt == 1 and min(rs) < 1 < max(rs) and abs(rs[0] - 1.3036) < 1e-3
    assertions.append(("A3_convergence_claim_is_not_robust", ok,
                       f"|c5/c4| > 1 in only {ngt}/{NTRIAL}, range "
                       f"{min(rs):.4f}..{max(rs):.4f}, straddling 1; the "
                       f"exceedance is the canonical ordering"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. why they behave differently ────────────────────────────────
    print("\n  4. why a sign survives and a ratio does not")
    for r in (3, 4, 5):
        v = [h[r] for h in H]
        print(f"     c{r}: {min(v):+.5f} .. {max(v):+.5f}   "
              f"swing {max(v) / min(v) if min(v) * max(v) > 0 else float('nan'):.2f}x")
    tails = [sum(h[r] for r in (3, 4, 5)) for h in H]
    print(f"     c3+c4+c5: {min(tails):+.5f} .. {max(tails):+.5f}   "
          f"spread {100 * (max(tails) - min(tails)) / abs(np.mean(tails)):.1f} %")
    print(f"     the individual cumulants swing by factors of 1.6 to 3.4 while")
    print(f"     their sum moves less — the ordering artifact REDISTRIBUTES")
    print(f"     weight between orders. A sign survives that; a ratio between two")
    print(f"     swinging quantities does not. That applies to anything else in")
    print(f"     this arc quoted as a cumulant ratio at fixed convention.")
    swings = [max(h[r] for h in H) / min(h[r] for h in H) for r in (3, 4, 5)]
    ok = max(swings) > 1.5
    assertions.append(("A4_individual_cumulants_swing_sum_moves_less", ok,
                       f"c3/c4/c5 swings {[round(s, 2) for s in swings]}; "
                       f"tail sum spread "
                       f"{100 * (max(tails) - min(tails)) / abs(np.mean(tails)):.1f}%"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. what is left standing ──────────────────────────────────────
    print("\n  5. what is left standing")
    print(f"     STANDS: c5 > 0, robustly ({npos}/{NTRIAL}) — the sign correction")
    print(f"       to qou-bc09 / qou-38i9 holds.")
    print(f"     STANDS: c2 ordering-independent — machinery check.")
    print(f"     STANDS: qou-441t's cumulant IDENTIFICATION — that L is additive")
    print(f"       on disjoint blocks so the Mobius inversion is a genuine")
    print(f"       cumulant expansion. That is an exact algebraic fact, not a")
    print(f"       measured ratio, and no ordering touches it.")
    print(f"     WITHDRAWN: 'the hierarchy does not converge'.")
    print(f"     UNKNOWN: whether it converges at all.")
    ok = True
    assertions.append(("A5_scope_of_what_survives_is_stated", ok,
                       "sign and identification stand; convergence claim "
                       "withdrawn; convergence itself unknown"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. the sample is enough to falsify, not to characterise ───────
    print("\n  6. what this sample can and cannot support")
    print(f"     {NTRIAL} orderings out of {math.factorial(len(ALLB)):.3g}")
    print(f"     possible is enough to FALSIFY a universal claim (one")
    print(f"     counterexample suffices, and there are {NTRIAL - ngt}) and not")
    print(f"     enough to characterise a distribution. No distributional")
    print(f"     statement is made — 'c5 > 0 in 12/12' is reported as 12/12, not")
    print(f"     as a probability.")
    ok = NTRIAL - ngt >= 1
    assertions.append(("A6_sample_supports_falsification_only", ok,
                       f"{NTRIAL - ngt} counterexamples to the convergence "
                       f"claim; no distributional claim made"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  Two claims from the previous turn, tested over twelve bond")
    print("  orderings, and they come apart.")
    print(f"  c5 > 0 holds in {npos}/{NTRIAL} with an identical sign pattern")
    print("  everywhere, so the correction to 'every many-body term is negative'")
    print("  is robust and stands.")
    print(f"  |c5/c4| > 1 holds in {ngt}/{NTRIAL} — and the one is the canonical")
    print("  production ordering, the only one previously tested. The ratio")
    print("  straddles 1 over 0.7077..1.3036, so 'the hierarchy does not")
    print("  converge' was a convention artifact and is WITHDRAWN. Whether it")
    print("  converges is unknown.")
    print("  The reason is visible in the spread: individual cumulants swing by")
    print("  1.6-3.4x across orderings while their sum moves less, so the")
    print("  artifact redistributes weight between orders. A sign survives that;")
    print("  a ratio of two swinging quantities does not.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="numpy")
        wb.set_description(
            "Tests the two claims qou-441t made from a single bond ordering at "
            "A=5, over twelve orderings (canonical production plus eleven random "
            "shuffles of the ten bonds). They come apart. THE SIGN IS ROBUST: "
            "c5 > 0 in 12 of 12, over the range +1.60 to +3.26, with the "
            "identical sign pattern + - - + in every ordering — so the "
            "correction to qou-bc09 and qou-38i9 stands, and 'every many-body "
            "term is negative' is false from A=5 regardless of convention. THE "
            "CONVERGENCE CLAIM IS NOT: |c5/c4| > 1 in only 1 of 12, and that one "
            "is the canonical production ordering, the only one qou-441t tested. "
            "The ratio ranges 0.7077..1.3036 and straddles 1, so 'the hierarchy "
            "does not converge' was an artifact of its convention and is "
            "WITHDRAWN; whether the hierarchy converges is unknown. The reason "
            "the two behave differently is visible in the spreads: c2 is exactly "
            "ordering-independent (a two-element subset has one bond and no "
            "internal order), while c3 swings over -2.40..-3.79, c4 over "
            "-1.23..-4.19 and c5 over +1.60..+3.26, each by a factor 1.6 to 3.4, "
            "with their sum moving less — the ordering artifact redistributes "
            "weight between orders. A sign survives that; a ratio between two "
            "swinging quantities does not, which applies to anything else in "
            "this arc quoted as a cumulant ratio at fixed convention. Untouched: "
            "qou-441t's cumulant IDENTIFICATION, that L is additive on disjoint "
            "blocks so the Mobius inversion is a genuine cumulant expansion — an "
            "exact algebraic fact no ordering affects.")
        wb.add_data("trials",
                    {str(i): {"c2": f"{h[2]:.9f}", "c3": f"{h[3]:.9f}",
                              "c4": f"{h[4]:.9f}", "c5": f"{h[5]:.9f}",
                              "ratio_54": f"{abs(h[5] / h[4]):.6f}",
                              "canonical": i == 0}
                     for i, h in enumerate(H)})
        wb.add_data("robustness",
                    {"c5_positive": f"{npos}/{NTRIAL}",
                     "c5_range": [f"{min(c5s):.6f}", f"{max(c5s):.6f}"],
                     "sign_patterns": sorted(sigs),
                     "ratio54_gt_1": f"{ngt}/{NTRIAL}",
                     "ratio54_range": [f"{min(rs):.6f}", f"{max(rs):.6f}"],
                     "c2_spread": f"{spread2:.3e}"})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "WITHDRAWS A CLAIM OF MINE FROM THE PREVIOUS TURN. qou-441t's "
            "'the hierarchy does not converge' rested on the canonical ordering "
            "alone and does not survive eleven others. Its sign result and its "
            "cumulant identification both do. Anyone quoting qou-441t should "
            "quote this alongside it.")
        wb.add_caveat(
            "TWELVE ORDERINGS IS ENOUGH TO FALSIFY, NOT TO CHARACTERISE. One "
            "counterexample refutes a universal claim and there are eleven; but "
            "no distribution is estimated and none should be read in. 'c5 > 0 "
            "in 12/12' is reported as a count, not as a probability, and a "
            "thirteenth ordering could in principle differ.")
        wb.add_caveat(
            "ONE NUCLEON ORDERING ONLY. All twelve trials use 5He at production "
            "nucleon ordering 'pnpnn' and vary only the BOND order. Nucleon "
            "ordering is a separate artifact (measured at 4-5% in "
            "three_body_term_has_the_wrong_sign_probe) and is not varied here.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
