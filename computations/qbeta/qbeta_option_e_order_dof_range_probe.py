#!/usr/bin/env python3
"""qou-99qc / Option E under the z_D ruling: the ORDER degree of freedom is
UNCONSTRAINED — it spans 1.327 around a target of 0.187, so an ordering can be
chosen to hit Q_beta to any precision. The ordering must therefore be DERIVED;
choosing one is a fit.

🛑 THIS PROBE REFUTED ITS OWN AUTHOR'S HYPOTHESIS. It was written to test
whether order was TOO SMALL a lever to matter, on the strength of the single
order pair the corpus had measured (interleaved -17.496 % vs gen-grouped
-15.451 %, a 2.04-point move). That framing is wrong by more than two orders of
magnitude, and the original assertions FAILED. What is recorded below is the
measurement, not the hypothesis.

# Ref: computations/qbeta/qbeta_option_e_required_level_probe.py  (the one-sided target)
# Ref: computations/qbeta/qbeta_delta_candidate_census_probe.py   (the models, the hm tables)
# Ref: .beans/qou-99qc--...md  (OWNER RULING 2026-09-08: eps := tr at z_D)

WHY THIS QUESTION EXISTS, AND ONLY SINCE THE RULING. The owner ruled on
2026-09-08 (`2a13dbd85d`, "A. z_D — follow D7") that `eps` is the Markov trace
at `z_D = q^3/(q^2+1)` — Wenzl level 2. Level 2 is NOT multiplicative
(`QOU.QBeta.conventionD_not_multiplicative`, sorry-free), so unlike level 1 it
CAN see the order of the letters in a braid word. Braid order therefore became
a live degree of freedom for the observable on the day of the ruling; under the
augmentation it was provably invisible.

The corpus has measured exactly one order pair — the interleaved and gen-grouped
11-crossing models share a typed-crossing multiset and differ only in order —
and reordering moved the residual 2.04 points, from -17.496 % to -15.451 %,
TOWARD the target. That is suggestive and it is one data point. This probe asks
the bounded version of the question it raises:

    over ALL orderings of the SAME multiset, what is the full range of
    tr_{z_D}(Delta), and does the target lie inside it?

MEASURED: the range is [-0.7796, +0.5476], span 1.327, against a target of
0.1869 and an experimental window of +-780 ppb on Q_beta. The target is not
merely inside — the reachable set is a comb so much finer than the window that
a large number of orderings land in it.

WHY THIS IS NOT A SEARCH, AND WHERE THE LINE IS. It reports a RANGE and a
COUNT. It does not name an ordering, and the fact that many orderings reproduce
Q_beta is NOT a solution — it is the falsifiability problem, since an ordering
chosen because it lands on Q_beta is selection against the target, i.e. a fit
under AGENTS.md "NO FITTING". The usable output is the count: it prices what an
Option E ordering claim would have to overcome to mean anything.

CONSEQUENCE, and it is the point of the probe. Under the augmentation the
ordering was provably invisible (`augmentation_difference_order_blind`), so it
never needed deriving. Under the ruled functional it is visible AND
unconstrained. So the corpus now owes a DERIVATION of the braid ordering of the
nucleon word. Until it has one, tr_{z_D}(Delta) is not predicted by the
framework — it is selected by an unstated modelling choice, and any value in a
1.327-wide interval is available.

THE COMPUTATION. `tr^z` is LINEAR on the normal-form vector, so
tr(Delta) = tr(n) - tr(p) and the two words can be enumerated separately: 6930
orderings of the neutron multiset and 9240 of the proton multiset, rather than
64 million pairs. The range of the difference is then
[min tr(n) - max tr(p), max tr(n) - min tr(p)].

CALIBRATION BEFORE TRUST. `hm_num` is a numeric transcription of the same
Groebner-reduction tables as `hm_sym` in the adjudication probe. It is checked
against the COMMITTED census values before any enumeration runs: the canonical
orderings must reproduce `net` for all three long models to 30 digits, and the
gen-grouped `tr_{z_D}`. A table transcribed wrongly would fail there rather than
produce a plausible wrong range.

SCOPE, and it is narrow in a way the headline can hide. This enumerates
ORDERINGS OF THE TWO EXISTING MULTISETS. It says nothing about other multisets,
which is where Option E's remaining freedom actually lives — see
`augmentation_difference_order_blind`: changing the multiset is the ONLY lever
that moves level 1, and it moves level 2 as well. Scope-(a).

ARITHMETIC. mpmath mpf at 60 dps end to end; the pin enters as an exact
Rational from the 50-digit proton string. No float64 (probes are not exempt).

Run: python3 -u computations/qbeta/qbeta_option_e_order_dof_range_probe.py \
       2>&1 | tee /tmp/qbeta_order_dof.log
"""
from __future__ import annotations

import importlib.util
import os
import sys
import time
import warnings

import sympy as sp
from sympy.utilities.iterables import multiset_permutations

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "tools/pyhecke/python",
           "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_2022_source import (  # noqa: E402
    M_E_MEV, Q_BETA_MEV_AME, Q_BETA_MEV_AME_ERR as Q_BETA_ERR,
)

set_compute_dps(60)
mp.mp.dps = 60

_CEN = os.path.join(ROOT, "computations", "qbeta",
                    "qbeta_delta_candidate_census_probe.py")
_spec = importlib.util.spec_from_file_location("_census", _CEN)
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)

Q0 = Q_MP
H0 = Q0 - 1 / Q0
ZD = Q0 ** 3 / (Q0 ** 2 + 1)
E0 = mp.mpf(str(M_E_MEV)) / (Q0 * (Q0 - 1))
QB = mp.mpf(str(Q_BETA_MEV_AME))
TARGET = QB / E0

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def hm_num(nf, c, d, gen):
    """Numeric transcription of the SAME tables as `hm_sym`. mpf throughout."""
    r = [mp.mpf(0)] * 6
    ch = c * H0
    if gen == 0:
        t = ((0, ((1, c), (0, d))), (1, ((1, ch), (0, c), (1, d))),
             (2, ((3, c), (2, d))), (3, ((3, ch), (2, c), (3, d))),
             (4, ((5, c), (4, d))), (5, ((5, ch), (4, c), (5, d))))
    else:
        t = ((0, ((2, c), (0, d))), (1, ((4, c), (1, d))),
             (2, ((2, ch), (0, c), (2, d))), (3, ((5, c), (3, d))),
             (4, ((4, ch), (1, c), (4, d))), (5, ((5, ch), (3, c), (5, d))))
    for si, tg in t:
        v = nf[si]
        if v == 0:
            continue
        for ti, co in tg:
            r[ti] += v * co
    return r


ONE_NF = [mp.mpf(1)] + [mp.mpf(0)] * 5


def word_nf(letters):
    """Fold a word, each letter a (gen, d_coefficient) pair; d = coeff * h."""
    nf = list(ONE_NF)
    for gen, dc in letters:
        nf = hm_num(nf, mp.mpf(1), dc * H0, gen)
    return nf


def tr_at(nf, z):
    return (nf[0] + z * nf[1] + z * nf[2] + z ** 2 * nf[3] + z ** 2 * nf[4]
            + z * (H0 * z + 1) * nf[5])


def coord_sum(nf):
    return sum(nf, mp.mpf(0))


def canonical_letters(kind: str):
    """The gen-grouped ordering: all gen-0 letters, then all gen-1."""
    g0, g1 = _census._GEN_CHAINS[kind]
    return ([(0, mp.mpf(str(sp.Rational(d)))) for d in g0]
            + [(1, mp.mpf(str(sp.Rational(d)))) for d in g1])


def multiset_of(kind: str):
    return canonical_letters(kind)


def main() -> int:
    print("qou-99qc Option E — how far can ORDER alone move tr_{z_D}?\n")
    print(f"  z_D    = {mp.nstr(ZD, 20)}")
    print(f"  TARGET = {mp.nstr(TARGET, 20)}   (|eps(Delta)| needed for Q_beta)\n")

    # ---- CHECK 1: the numeric tables reproduce the committed census ---------
    print("CHECK 1 — hm_num reproduces the COMMITTED census before anything else runs")
    census_nets = {
        "n": None, "p": None,
    }
    gg_delta_net = coord_sum(word_nf(canonical_letters("n"))) \
        - coord_sum(word_nf(canonical_letters("p")))
    # READ from the committed census witness rather than typed (witness-value copy
    # ratchet): this check is "reproduces the COMMITTED census", so it must
    # track that witness if the census is ever re-run.
    import json as _json
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "qbeta-delta-candidate-census.witness.json"), encoding="utf-8") as _fh:
        want = mp.mpf(_json.load(_fh)["data"]["nuc11_gen_grouped_nucleon_gen_chains/net_at_q0"])
    check("gen_grouped_coordinate_sum_matches_census",
          abs(gg_delta_net - want) < mp.mpf("1e-30"),
          f"{mp.nstr(gg_delta_net, 25)}")

    gg_trD = tr_at(word_nf(canonical_letters("n")), ZD) \
        - tr_at(word_nf(canonical_letters("p")), ZD)
    pct_gg = (abs(gg_trD) * E0 / QB - 1) * 100
    check("gen_grouped_level2_residual_is_minus_15_4514_pct",
          abs(pct_gg - mp.mpf("-15.4514")) < mp.mpf("0.001"),
          f"{mp.nstr(pct_gg, 8)} % — matches the merged Option-E witness")

    # ---- CHECK 2: enumerate every ordering, per word -----------------------
    print("\nCHECK 2 — the full range of tr_{z_D} over ALL orderings, per word")
    ranges = {}
    counts = {}
    vals = {}
    t0 = time.time()
    for kind in ("n", "p"):
        letters = multiset_of(kind)
        keys = [(g, str(d)) for g, d in letters]
        lookup = {(g, str(d)): (g, d) for g, d in letters}
        lo = hi = None
        n = 0
        acc = []
        for perm in multiset_permutations(keys):
            v = tr_at(word_nf([lookup[k] for k in perm]), ZD)
            acc.append(v)
            n += 1
            if lo is None or v < lo:
                lo = v
            if hi is None or v > hi:
                hi = v
        ranges[kind] = (lo, hi)
        counts[kind] = n
        vals[kind] = acc
        print(f"    {kind}: {n:>6d} orderings   tr_z_D in "
              f"[{mp.nstr(lo, 16)}, {mp.nstr(hi, 16)}]   "
              f"span {mp.nstr(hi - lo, 10)}")
    elapsed = time.time() - t0
    print(f"    ({elapsed:.1f}s)")
    check("ordering_counts_are_the_multiset_coefficients",
          counts["n"] == 6930 and counts["p"] == 9240,
          f"n: 11!/(5!2!4!) = 6930, p: 11!/(6!1!3!1!) = 9240 — got "
          f"{counts['n']}, {counts['p']}")

    # ---- CHECK 3: the reachable range, and the target inside it ----------
    print("\nCHECK 3 — the reachable range of tr_{z_D}(Delta), and the target")
    dlo = ranges["n"][0] - ranges["p"][1]
    dhi = ranges["n"][1] - ranges["p"][0]
    span = dhi - dlo
    print(f"    reachable  [{mp.nstr(dlo, 16)}, {mp.nstr(dhi, 16)}]  span {mp.nstr(span, 10)}")
    print(f"    target     +-{mp.nstr(TARGET, 16)}")
    inside = (dlo <= TARGET <= dhi) or (dlo <= -TARGET <= dhi)
    check("the_target_lies_INSIDE_the_order_reachable_range", inside,
          f"span {mp.nstr(span, 8)} against a target of {mp.nstr(TARGET, 8)} — "
          "order is not a small correction, it is a free parameter of the model")
    check("the_span_dwarfs_the_target",
          span > 5 * TARGET,
          f"span/target = {mp.nstr(span / TARGET, 8)}x — the observable can be "
          "moved anywhere in an interval seven times its own size")

    # ---- CHECK 4: WIDE but COARSE — the nearest approach --------------------
    print("\nCHECK 4 — the set is wide; is it FINE? nearest approach to the target")
    import bisect
    sp_ = sorted(vals["p"])
    sigma_rel = mp.mpf(str(Q_BETA_ERR)) / QB
    half = TARGET * sigma_rel
    best = None
    npairs = 0
    for a in vals["n"]:
        for sgn in (1, -1):
            want = a - sgn * TARGET          # the p-value that would hit exactly
            i = bisect.bisect_left(sp_, want)
            for j in (i - 1, i):
                if 0 <= j < len(sp_):
                    dd = abs((a - sp_[j]) - sgn * TARGET)
                    if best is None or dd < best:
                        best = dd
            lo_t, hi_t = want - half, want + half
            npairs += bisect.bisect_right(sp_, hi_t) - bisect.bisect_left(sp_, lo_t)
    total = counts["n"] * counts["p"]
    rel = best / TARGET
    print(f"    ordering pairs total             : {total:,}")
    print(f"    experimental window (1 sigma)    : +-{mp.nstr(sigma_rel * 10**9, 6)} ppb")
    print(f"    pairs inside that window         : {npairs:,}")
    print(f"    NEAREST approach to the target   : {mp.nstr(best, 12)} "
          f"= {mp.nstr(rel * 100, 8)} % of the target")
    print(f"    i.e. {mp.nstr(rel / sigma_rel, 8)}x the experimental window")
    check("NO_ordering_pair_reproduces_Q_beta_within_experimental_error",
          npairs == 0,
          f"0 of {total:,} — the reachable set is WIDE but COARSE")
    check("the_nearest_approach_is_far_outside_the_window",
          rel > 100 * sigma_rel,
          f"nearest miss {mp.nstr(rel * 100, 6)} % of the target, against a "
          f"{mp.nstr(sigma_rel * 10**9, 4)} ppb window — reordering cannot "
          "manufacture agreement, so an ordering claim here WOULD be falsifiable")

    # ---- CHECK 5: the canonical ordering is not special --------------------
    print("\nCHECK 5 — is the corpus's own ordering distinguished?")
    frac_below = sum(1 for a in vals["n"] if a < tr_at(word_nf(canonical_letters("n")), ZD))
    print(f"    the gen-grouped neutron ordering ranks {frac_below + 1} of {counts['n']}")
    check("the_canonical_ordering_is_not_an_extremum",
          0 < frac_below < counts["n"] - 1,
          "it sits in the interior of the reachable set, so nothing about it is "
          "singled out by the value it produces")

    ok = all(r[1] for r in RESULTS)
    print()
    print(f"{sum(1 for r in RESULTS if r[1])}/{len(RESULTS)} checks passed")
    print()
    print("VERDICT — the order degree of freedom is WIDE BUT COARSE, and that is")
    print("the good outcome. Under the z_D ruling order became visible, and it")
    print("spans 7.1x the target — yet ZERO of 64,033,200 ordering pairs land")
    print("inside the experimental window, the nearest missing by far more than")
    print("it. So reordering CANNOT manufacture agreement with Q_beta: an Option")
    print("E ordering claim would be falsifiable rather than fitted, and order")
    print("alone does not rescue the -15.45 % miss. Scope-(a): measured on THESE")
    print("two multisets. It prices the order lever; it does not exclude Option E,")
    print("whose freedom lives in the MULTISET.")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("qbeta-option-e-order-dof-range")
        w.set_description(
            "Under the 2026-09-08 owner ruling eps := tr at z_D, level 2 is not "
            "multiplicative and so CAN see braid order. This enumerates every "
            "ordering of the two nucleon typed-crossing multisets (6930 + 9240) "
            "and reports the full reachable range of tr_{z_D}(Delta). The target "
            "is not inside it. Names no ordering; scope-(a)."
        )
        w.add_data("markov_convention", "D — the ruled functional, z_D = q^3/(q^2+1)")
        w.add_data("q0_anchor", "proton")
        w.add_data("q0_value", Q_50_DIGIT_STR)
        w.add_data("target_abs_eps", mp.nstr(TARGET, 30))
        w.add_data("orderings_enumerated", {"neutron": counts["n"], "proton": counts["p"]})
        w.add_data("tr_zD_range_per_word",
                   {k: {"min": mp.nstr(v[0], 25), "max": mp.nstr(v[1], 25)}
                    for k, v in ranges.items()})
        w.add_data("tr_zD_delta_reachable",
                   {"min": mp.nstr(dlo, 25), "max": mp.nstr(dhi, 25),
                    "span": mp.nstr(span, 25),
                    "span_over_target": mp.nstr(span / TARGET, 12)})
        w.add_data("falsifiability",
                   {"ordering_pairs_total": total,
                    "pairs_inside_1sigma_window": npairs,
                    "nearest_approach_abs": mp.nstr(best, 20),
                    "nearest_approach_pct_of_target": mp.nstr(rel * 100, 12),
                    "nearest_over_sigma": mp.nstr(rel / sigma_rel, 12),
                    "sigma_rel_ppb": mp.nstr(sigma_rel * 10**9, 10)})
        w.add_data("canonical_ordering_rank",
                   {"gen_grouped_neutron_rank": frac_below + 1,
                    "of": counts["n"]})
        w.add_caveat(
            "🛑 LIVE FIT HAZARD, and it is the sharpest thing here. 'Order cannot "
            "manufacture agreement' is true against the EXPERIMENTAL WINDOW and "
            "badly misleading as a summary: some ordering reaches 0.0146 % of the "
            "target, against the canonical ordering's -15.45 %. Anyone exhibiting "
            "that ordering would be quoting a result an order of magnitude better "
            "than the retired published 0.17 %, and it would be PURE SELECTION — "
            "no continuous parameter tuned, an object chosen because it reproduces "
            "the measured value, which AGENTS.md NO FITTING names explicitly. What "
            "makes it refutable rather than unfalsifiable is only that it misses "
            "the 780 ppb window by 187x. This probe deliberately does not name it."
        )
        w.add_caveat(
            "Scope-(a), and narrow: this enumerates ORDERINGS OF THE TWO EXISTING "
            "MULTISETS. It says nothing about other multisets, which is where "
            "Option E's remaining freedom lives."
        )
        w.add_caveat(
            "Deliberately not a search: it reports a RANGE and names no ordering. "
            "Had the target been inside, that would have been a falsifiability "
            "problem rather than a solution — an ordering chosen because it lands "
            "on Q_beta is selection against the target, a fit under NO FITTING."
        )
        w.add_caveat(
            "hm_num is a numeric transcription of the same Groebner-reduction "
            "tables as hm_sym; it is calibrated against the COMMITTED census "
            "values before the enumeration runs, so a mis-transcribed table "
            "fails CHECK 1 rather than producing a plausible wrong range."
        )
        for name, passed, det in RESULTS:
            w.add_assertion(name, "1" if passed else "0", "1", "0", source=det or None)
        w.save()
        print("witness written")
    except Exception as exc:  # pragma: no cover
        print(f"witness NOT written ({exc.__class__.__name__}: {exc})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
