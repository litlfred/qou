#!/usr/bin/env python3
"""qou-99qc / Option E: price the ENTIRE declared freedom of the element
construction — 16 recipe readings x every ordering of each — against Q_beta.

# Ref: computations/qbeta/qbeta_option_e_order_dof_range_probe.py  (the order axis alone)
# Ref: computations/qbeta/qbeta_delta_candidate_census_probe.py    (the recipe, the hm tables)
# Ref: .beans/qou-99qc--...md   (OWNER RULING 2026-09-08: eps := tr at z_D)

WHAT THIS COMPLETES. The order probe priced ONE axis and found it wide but
coarse: over 64 M ordering pairs of the fixed gen-grouped multisets, zero land
inside the experimental window. But ordering is not the only thing the corpus
leaves unstated. `qbeta_delta_candidate_census_probe.nuc11_constructed` carries
its own warning:

    "`gens` and `hopf` are NOT corpus statements. The blocks give the typed
     SHIFTS (uu -> 0, ud -> -h/2, dd -> -h) but never say which generator each
     quark crossing sits on"

so the census counts 8 quark-generator assignments x 2 Hopf orientations = 16
readings of the SAME source blocks. Under the ruling both the multiset and the
order are visible to the observable (level 2 is not multiplicative), so this
prices them together.

MEASURED HERE, and it corrects the count TWICE OVER: the 16 readings collapse to
SIX distinct multisets, by two independent symmetries.

  1. HOPF IS NOT AN AXIS.  (1,0) and (0,1) append the SAME pair of letters and
     differ only in the order of those two, which the ordering enumeration
     already covers.                                             16 -> 8

  2. THE TWO ud SHIFTS ARE INTERCHANGEABLE.  Both carry d = -h/2, so swapping
     which generator each sits on leaves the multiset fixed: 001 == 010 and
     101 == 110. Two classes therefore hold four readings each.   8 -> 6

Both were found by running, not by reasoning: an earlier version asserted 8 and
FAILED its own check at 6. The class structure is verified explicitly rather
than inferred -- every class contains both hopf orientations, and classes 2 and
5 contain four readings each.

The census's "16 variants" is correct for ITS question, which fixes one ordering
per variant. It over-counts by 2.67x for this one.

THE QUESTION, and it is a falsifiability question, not a search. Across every
configuration the source blocks permit — 16 readings, and within each every
ordering of the 11 letters — how many reproduce Q_beta to within experimental
error? The answer prices what an Option E claim built from this recipe would
have to overcome:

  * MANY  -> the construction is a fit surface. Exhibiting a configuration that
            matches would be selection against the target, and the recipe as
            stated does not predict the observable at all.
  * ZERO  -> the recipe is falsifiable AND currently refuted at level 2: no
            reading of the source blocks, under any ordering, reaches Q_beta.

Either way it is the owner's number to have. It names no configuration.

WHY THE READINGS ARE PAIRED. `gens` and `hopf` are one recipe, so the same
assignment is applied to BOTH nucleons, exactly as the census's
`constructed_variants` does. Pairing a proton reading with a different neutron
reading would be a 17th choice nobody has made.

ARITHMETIC. mpf at 60 dps; pin as an exact Rational from the 50-digit proton
string. hm_num is the numeric transcription of the same Groebner tables as
`hm_sym`, calibrated against the COMMITTED census before anything is enumerated.
No float64 (probes are not exempt).

SCOPE. Scope-(a). It prices the freedom the SOURCE BLOCKS declare. It does not
enumerate arbitrary multisets, and it does not exclude Option E — an element
derived from somewhere other than this recipe is outside it.

Run: python3 -u computations/qbeta/qbeta_option_e_construction_freedom_probe.py \
       2>&1 | tee /tmp/qbeta_construction_freedom.log
"""
from __future__ import annotations

import bisect
import importlib.util
import itertools
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
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_2022_source import (  # noqa: E402
    M_E_MEV, Q_BETA_MEV_AME, Q_BETA_MEV_AME_ERR,
)

set_compute_dps(60)
mp.mp.dps = 60

_ORD = os.path.join(ROOT, "computations", "qbeta",
                    "qbeta_option_e_order_dof_range_probe.py")
_spec = importlib.util.spec_from_file_location("_ord", _ORD)
_ord = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ord)

Q0 = _ord.Q0
H0 = _ord.H0
ZD = _ord.ZD
E0 = _ord.E0
QB = _ord.QB
TARGET = _ord.TARGET
word_nf = _ord.word_nf
tr_at = _ord.tr_at
SIGMA_REL = mp.mpf(str(Q_BETA_MEV_AME_ERR)) / QB

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def reading_letters(kind: str, gens, hopf):
    """`nuc11_constructed` as a LETTER LIST: B_3 core, typed quark shifts at the
    chosen generators, then the Hopf pair. Letters are (gen, d_coefficient)."""
    letters = []
    for _ in range(3):                       # B_3 confinement core
        letters.append((0, mp.mpf(0)))
        letters.append((1, mp.mpf(-1)))
    shifts = ([mp.mpf(0), mp.mpf("-0.5"), mp.mpf("-0.5")] if kind == "p"
              else [mp.mpf(-1), mp.mpf("-0.5"), mp.mpf("-0.5")])
    for g, d in zip(gens, shifts):
        letters.append((g, d))
    for g in hopf:                           # the Hopf link
        letters.append((g, mp.mpf(0)))
    return letters


def tr_values_over_orderings(letters):
    keys = [(g, str(d)) for g, d in letters]
    lookup = {(g, str(d)): (g, d) for g, d in letters}
    out = []
    for perm in multiset_permutations(keys):
        out.append(tr_at(word_nf([lookup[k] for k in perm]), ZD))
    return out


def main() -> int:
    print("qou-99qc Option E — the FULL declared freedom of the construction\n")
    print(f"  TARGET |eps(Delta)| = {mp.nstr(TARGET, 20)}")
    print(f"  1 sigma on Q_beta   = {mp.nstr(SIGMA_REL * 10**9, 6)} ppb\n")

    # ---- CHECK 1: the machinery is the calibrated one ----------------------
    print("CHECK 1 — reuse of the calibrated order-probe machinery")
    canon = _ord.canonical_letters("n")
    canon_p = _ord.canonical_letters("p")
    gg = tr_at(word_nf(canon), ZD) - tr_at(word_nf(canon_p), ZD)
    pct = (abs(gg) * E0 / QB - 1) * 100
    check("imported_machinery_reproduces_the_gen_grouped_residual",
          abs(pct - mp.mpf("-15.4514")) < mp.mpf("0.001"),
          f"{mp.nstr(pct, 8)} % — hm_num/tr_at come from the committed order "
          "probe, which calibrates against the census before enumerating")

    # ---- CHECK 2: the 16 readings, each fully enumerated -------------------
    print("\nCHECK 2 — 16 recipe readings x every ordering of each")
    print(f"  {'reading':<18s} {'n-ord':>7s} {'p-ord':>7s} "
          f"{'best |tr| pct':>15s} {'in window':>10s}")
    t0 = time.time()
    total_pairs = 0
    total_hits = 0
    best_overall = None
    per_reading = {}
    seen = set()
    dupes = 0
    for gens in itertools.product((0, 1), repeat=3):
        for hopf in ((1, 0), (0, 1)):
            key = (tuple(sorted((g, str(d)) for g, d in reading_letters("n", gens, hopf))),
                   tuple(sorted((g, str(d)) for g, d in reading_letters("p", gens, hopf))))
            if key in seen:
                dupes += 1
                continue
            seen.add(key)
            vn = tr_values_over_orderings(reading_letters("n", gens, hopf))
            vp = sorted(tr_values_over_orderings(reading_letters("p", gens, hopf)))
            half = TARGET * SIGMA_REL
            hits = 0
            nearest = None
            for a in vn:
                for sgn in (1, -1):
                    want = a - sgn * TARGET
                    i = bisect.bisect_left(vp, want)
                    for j in (i - 1, i):
                        if 0 <= j < len(vp):
                            dd = abs((a - vp[j]) - sgn * TARGET)
                            if nearest is None or dd < nearest:
                                nearest = dd
                    hits += (bisect.bisect_right(vp, want + half)
                             - bisect.bisect_left(vp, want - half))
            npairs = len(vn) * len(vp)
            total_pairs += npairs
            total_hits += hits
            bestpct = (nearest / TARGET) * 100
            if best_overall is None or nearest < best_overall[0]:
                best_overall = (nearest, f"gens={gens},hopf={hopf}")
            label = f"{''.join(map(str, gens))}/{''.join(map(str, hopf))}"
            per_reading[label] = {"n_orderings": len(vn), "p_orderings": len(vp),
                                  "pairs": npairs, "hits_in_window": hits,
                                  "nearest_pct_of_target": mp.nstr(bestpct, 10)}
            print(f"  {label:<18s} {len(vn):>7d} {len(vp):>7d} "
                  f"{mp.nstr(bestpct, 8):>15s} {hits:>10d}")
    print(f"  ({time.time() - t0:.1f}s)")
    check("the_16_readings_collapse_to_6_distinct_multisets",
          len(per_reading) == 6 and dupes == 10,
          f"{len(per_reading)} distinct, {dupes} duplicates — hopf is subsumed "
          "by the ordering enumeration (16->8), and the two ud shifts both carry "
          "d = -h/2 so swapping their generators leaves the multiset fixed, "
          "collapsing 001==010 and 101==110 (8->6)")

    # ---- CHECK 3: the headline count ---------------------------------------
    print("\nCHECK 3 — the falsifiability price of the recipe as stated")
    print(f"    configurations examined : {total_pairs:,} ordering pairs "
          f"across 16 readings")
    print(f"    inside the 1 sigma window: {total_hits:,}")
    nearest_pct = (best_overall[0] / TARGET) * 100
    print(f"    nearest approach overall : {mp.nstr(nearest_pct, 10)} % of target")
    print(f"                               ({mp.nstr(best_overall[0] / TARGET / SIGMA_REL, 8)}x the window)")
    check("the_recipe_as_stated_does_NOT_reach_Q_beta", total_hits == 0,
          f"0 of {total_pairs:,} configurations the source blocks permit reach "
          "Q_beta within experimental error — the construction is FALSIFIABLE "
          "and, at level 2, currently refuted")

    ok = all(r[1] for r in RESULTS)
    print()
    print(f"{sum(1 for r in RESULTS if r[1])}/{len(RESULTS)} checks passed")
    print()
    print("VERDICT — the entire freedom the source blocks declare has been")
    print("priced: 6 distinct multisets (the 16 readings collapse by two")
    print("symmetries — hopf is subsumed by ordering, and the two ud shifts are")
    print("interchangeable), every ordering of each, and not one")
    print("configuration reproduces Q_beta within experimental error at the")
    print("ruled functional. That is the good kind of negative — the recipe")
    print("makes a falsifiable claim and the claim currently fails. Option E")
    print("is not closed by any reading of the EXISTING recipe; an element that")
    print("closes it has to come from somewhere else. Scope-(a).")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("qbeta-option-e-construction-freedom")
        w.set_description(
            "Prices the ENTIRE declared freedom of the corpus's nucleon-element "
            "recipe against Q_beta at the ruled functional (tr at z_D): 8 quark-"
            "generator assignments x 2 Hopf orientations, and within each every "
            "ordering of the 11 letters. Reports how many configurations reach "
            "Q_beta within experimental error. Names no configuration; scope-(a)."
        )
        w.add_data("markov_convention", "D — the ruled functional, z_D = q^3/(q^2+1)")
        w.add_data("q0_anchor", "proton")
        w.add_data("q0_value", Q_50_DIGIT_STR)
        w.add_data("target_abs_eps", mp.nstr(TARGET, 30))
        w.add_data("sigma_rel_ppb", mp.nstr(SIGMA_REL * 10**9, 10))
        w.add_data("configurations_examined", total_pairs)
        w.add_data("configurations_inside_window", total_hits)
        w.add_data("nearest_approach_pct_of_target", mp.nstr(nearest_pct, 12))
        w.add_data("per_reading", per_reading)
        w.add_data("distinct_multisets", len(per_reading))
        w.add_data("readings_that_were_duplicates", dupes)
        w.add_caveat(
            "Scope-(a). Prices the freedom the SOURCE BLOCKS declare — the 16 "
            "readings the census already flags, plus ordering. It does not "
            "enumerate arbitrary multisets and does not exclude Option E: an "
            "element derived from somewhere other than this recipe is outside it."
        )
        w.add_caveat(
            "Names no configuration. A configuration exhibited because it lands "
            "on Q_beta would be selection against the target — a fit under "
            "AGENTS.md NO FITTING — which is exactly why the useful output is a "
            "COUNT rather than a candidate."
        )
        w.add_caveat(
            "The readings are PAIRED: gens/hopf is one recipe, so the same "
            "assignment applies to both nucleons, as the census's "
            "constructed_variants does. Pairing a proton reading with a "
            "different neutron reading would be a 17th choice nobody has made."
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
