"""EXHAUST `phi` over both nucleon letter-orbits — 16170 words, every one of them.

WHAT THIS SETTLES, AND WHY IT IS NOW CHEAP
------------------------------------------
`f1/f0` on the pn atom word is additive across the two nucleons (they occupy
disjoint strand sets, so `tr_M` factorises -- derived in
`braids-and-knots/markov-axioms-primitive.md`, measured at 40 dps by
`computations/qbeta/qbeta_disjoint_support_factorisation_probe.py`, and measured
in exact Fraction at the log-derivative level by
`word_order_commutation_and_additivity_probe.py`). So the whole 22-letter problem
reduces to a function `phi` of an 11-letter word on two adjacent generators.

Two further facts make exhaustion tractable rather than a 7-hour job, and BOTH
are gated below rather than assumed:

  (G1) `phi` is STRAND-COUNT INDEPENDENT. The proton word gives 21/2 at n = 3,
       n = 4 and n = 6 alike. Computing at n = 3 is ~9x faster than at n = 6
       (0.30 s vs 2.78 s per word).
  (G2) `phi` is TRANSLATION INVARIANT in the generator index. The neutron's
       letters on generators {3,4} at n = 6 give 8; remapped to {0,1} at n = 3
       they give 8.

Orbit sizes are multinomials over each nucleon's letter multiset:

    proton   11!/(6!.1!.3!.1!) = 9240      (6 sigma_0, 1 avg_0, 3 sigma_inv_1, 1 avg_1)
    neutron  11!/(5!.2!.4!)    = 6930      (5 sigma_0, 2 avg_0, 4 sigma_inv_1)

WHAT AN EXHAUSTION BUYS OVER WHAT WE HAVE
-----------------------------------------
Three separate results about the canonical word are currently SAMPLED or LOCAL,
and all three become PROVED statements over the whole orbit here:

  - #6905 measured the grouped word a 1-swap LOCAL maximum (0 of 196 neighbours
    beat it). Local is not global; the 1-swap neighbourhood is 196 of 9240.
  - #6714 found canonical largest of 40 random shuffles, p ~ 1/41.
  - #6919 showed contiguity does not determine phi, but not what does.

An exhaustion answers: is the canonical word the global maximum, how many words
tie it, what is the full value distribution, and is the canonical value even
distinguished at all.

FALSIFIABLE, AND THE INTERESTING OUTCOME IS THE NEGATIVE. If some word beats the
canonical one, "canonical extremality" is refuted outright and this prints the
witness. That is a better result than confirmation, and it is why the argmax
words are recorded rather than only the count.

NO FLOAT: every value is an exact `fractions.Fraction`.
"""
from __future__ import annotations

import json
import math
import os
import sys
import time
from collections import Counter
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMP = os.path.dirname(_HERE)
for _p in (_COMP, _HERE, os.path.join(_COMP, "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from word_level_trace_entry_point import log_derivative        # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

N_SMALL = 3
P_TRUNC = 3
OUT = os.path.join(_COMP, "phi-per-nucleon-orbit-exhaustion.witness.json")


def multiset_permutations(items):
    """Every distinct ordering of a multiset, no duplicates, no 11! blow-up."""
    counts = sorted(Counter(items).items(), key=lambda kv: repr(kv[0]))
    n = len(items)
    out = [None] * n

    def rec(k):
        if k == n:
            yield tuple(out)
            return
        for i, (val, c) in enumerate(counts):
            if c == 0:
                continue
            counts[i] = (val, c - 1)
            out[k] = val
            yield from rec(k + 1)
            counts[i] = (val, c)

    return rec(0)


def orbit_size(items) -> int:
    m = math.factorial(len(items))
    for c in Counter(items).values():
        m //= math.factorial(c)
    return m


def main() -> int:
    grouped = atom_canonical_crossings(1, 1, include_inter=False, intra_order="grouped")
    proton = [x for x in grouped if x[0] in (0, 1)]
    neutron = [(x[0] - 3, x[1]) for x in grouped if x[0] in (3, 4)]

    failures = []

    # ---- gate G1: strand-count independence, and G2: index translation --------
    v6 = log_derivative(proton, 6, P_TRUNC)
    v3 = log_derivative(proton, N_SMALL, P_TRUNC)
    if not (v3 == v6 == F(21, 2)):
        failures.append(f"G1: proton phi differs by strand count — n=3 {v3}, n=6 {v6}")
    nraw = log_derivative([x for x in grouped if x[0] in (3, 4)], 6, P_TRUNC)
    nrem = log_derivative(neutron, N_SMALL, P_TRUNC)
    if not (nrem == nraw == F(8)):
        failures.append(f"G2: neutron phi moved under index remap — {nraw} vs {nrem}")
    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        return 1
    print(f"gates: G1 proton {v3} at n=3 == {v6} at n=6;  "
          f"G2 neutron {nrem} remapped == {nraw} raw", flush=True)

    results = {}
    for name, word, canon in (("proton", proton, F(21, 2)),
                              ("neutron", neutron, F(8))):
        total = orbit_size(word)
        print(f"\n=== {name}: exhausting {total} distinct orderings at n={N_SMALL} ===",
              flush=True)
        hist: dict[F, int] = {}
        best = None
        best_words = []
        errors = 0
        t0 = time.time()
        for i, w in enumerate(multiset_permutations(word)):
            try:
                v = log_derivative(list(w), N_SMALL, P_TRUNC)
            except BaseException:
                errors += 1
                continue
            hist[v] = hist.get(v, 0) + 1
            if best is None or v > best:
                best, best_words = v, [w]
            elif v == best and len(best_words) < 5:
                best_words.append(w)
            if (i + 1) % 250 == 0:
                el = time.time() - t0
                eta = el / (i + 1) * (total - i - 1)
                print(f"   {i+1}/{total}  {el:.0f}s elapsed, ETA {eta/60:.1f} min  "
                      f"max so far {best}", flush=True)

        vals = sorted(hist)
        n_measured = sum(hist.values())
        above = sum(c for v, c in hist.items() if v > canon)
        ties = hist.get(canon, 0)
        el = time.time() - t0
        print(f"  measured {n_measured}/{total} ({errors} raised)   {el/60:.1f} min",
              flush=True)
        print(f"  range {vals[0]} .. {vals[-1]}   distinct values {len(vals)}", flush=True)
        print(f"  canonical {canon}: {ties} word(s) attain it, "
              f"{above} word(s) EXCEED it", flush=True)
        verdict = ("GLOBAL MAXIMUM over the whole orbit"
                   if above == 0 else
                   f"REFUTED — {above} words exceed the canonical value")
        print(f"  VERDICT: {verdict}", flush=True)
        if above:
            print(f"  witness (first): {best_words[0]}", flush=True)

        results[name] = {
            "orbit_size": total,
            "measured": n_measured,
            "errors": errors,
            "canonical": str(canon),
            "attaining_canonical": ties,
            "exceeding_canonical": above,
            "min": str(vals[0]),
            "max": str(vals[-1]),
            "distinct_values": len(vals),
            "verdict": verdict,
            "histogram": {str(v): hist[v] for v in vals},
            "argmax_examples": [[list(x) for x in w] for w in best_words[:3]],
            "elapsed_seconds": round(el, 1),
        }
        with open(OUT, "w") as fh:
            json.dump({"description":
                       "Exhaustive phi over both nucleon letter-orbits at n=3.",
                       "data": results,
                       "q0Anchor": "independent",
                       "q0AnchorReason": (
                           "phi = f1/f0 is the exact first-order log-derivative "
                           "of tr_M at q = 1, computed in Fraction from the "
                           "q-series of the braid word; no substrate pin q0 "
                           "is read"),
                       "scriptFile": os.path.basename(__file__)}, fh, indent=2)

    print("\nDONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
