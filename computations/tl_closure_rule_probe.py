#!/usr/bin/env python3
"""The TL closure rule, read off the diagrams and stated on the `(I,J)` index.

Bean `qou-cds1`. `QOU/MathlibExt/TemperleyLiebNormalForm.lean` defines the
general normal-form index `NormalIdx m` as a pair of subsets `(I, J)`, because
`tl_normal_form_basis_probe.py` established that word length CANNOT be a
termination measure. What that file still lacks -- and what blocks
`dim TL_n = catalan n` -- is the **closure lemma**: a formula for

    e_k · elt(I, J)   =   δ^loops · elt(I', J')

with `(I', J')` and `loops` given as functions of `(k, I, J)`.

This probe does not guess that formula. It computes the product by planar
diagrams (the ground truth `tl_normal_form_basis_probe` already validated),
indexes both sides by their `(I, J)` data, and then TESTS candidate rules
against every product at `n = 2..7` -- 3456 of them.

## What is settled

**The δ rule is complete**, and it is a condition on `I` alone:

    loops = 1   ⟺   (I', J') = (I, J)          [the δ appears exactly at fixed points]
    loops = 1   ⟺   k ∈ I  ∧  k-1 ∉ I          [and that is the test]

Both hold on all 3456 products. The second is sharp, and the near misses show
it: `k ∈ I` alone fails 650, `k ∈ I ∧ k+1 ∉ I` fails 882, `k ∈ I ∧ k ∉ J` fails
846. **`J` does not enter the δ condition at all.**

The reason is visible once stated: `e_k` commutes past an earlier block iff that
block's top index is `≤ k-2`, i.e. iff `k-1 ∉ I`; it then meets its own block
top and `e_k² = δ e_k` fires. So this is a lemma with a proof, not a fit.

**Two further invariants**, on all 3456:

    k ∈ I'          always -- every product lands on a normal form whose I contains k
    |I'| = |J'|     always -- as it must, but it is checked rather than assumed

## 🛑 CORRECTED — the `(I', J')` rule was IN THIS CORPUS all along

The section below said the `loops = 0` rule was "NOT identified" and "genuinely
more intricate than an insertion". The measurement is right; the verdict is
wrong. **It is a published Gröbner-Shirshov reduction and the folio's own
bibliography records it** — `content/schema/references.ts` line 10450,
`[kimlee2018]`, marked "Read in full 2026-08-09", names the two rewriting
families `E_{i,j}E_i − E_{i−2,j}E_i` and `E_jE_{i,j} − E_jE_{i,j+2}` outright.
Those two, with `E_i² → δE_i` and far commutation, reproduce **all 3456
products below with zero mismatches**; `tl_gs_reduction_probe.py` checks it,
together with closure on 19,413 monomial pairs and confluence.

The rule is more intricate than an insertion — but it is *known*, and the
sentence "none of the simple candidates fits" was a statement about my search,
not about the corpus. What failed was corpus-grep **path 5** (ingested
sources), run only after the guesses were exhausted rather than before them.

The original text follows, uncorrected, because the numbers in it stand.

**The `(I', J')` formula for the `loops = 0` branch.** 2378 products, and none
of the simple candidates fits: `I' = I ∪ {k}` fails 1821, `I' ⊆ I ∪ {k}` fails
348, `J' ⊆ J ∪ {k}` fails 129. The size moves in both directions --
`|I'| - |I| ∈ {-1, 0, +1}` with 302 / 1519 / 557 -- and that **decrease is
exactly the source of the word-length non-monotonicity** the first probe found.
So the remaining rule is genuinely more intricate than an insertion, which is
consistent with, and explains, that earlier negative.

This probe therefore closes the δ half of the closure lemma and leaves the
`(I', J')` half open, with its shape measured rather than guessed.

## Three further measurements (added after the δ half was proved)

4. **No natural measure is monotone.** A spanning proof would like an induction
   on some measure of `(I, J)` that the rewriting respects. **Twelve candidates
   were tested and every one INCREASES on some product** -- `|I|`,
   `sum I`, `sum J`, `sum I + sum J`, `sum of block lengths` (= word length),
   `sum (i-j)`, `max I`, `min I`, the lex orders on `(|I|, sum I)` and
   `(sum I, |I|)`, and the lex orders on the tuples `I` and `J`. So the earlier
   word-length negative was **not special**: it is one row of a general pattern,
   and an induction of that shape does not exist.

5. **The map is not injective, and its image has exactly `catalan(n-1)`
   elements -- for every `k`.** 1, 2, 5, 14, 42, 132 at `n = 2..7`. That is
   `dim TL_{n-1}`, i.e. the tower relation `dim(e_k · TL_n) = dim TL_{n-1}`
   appearing directly in the normal-form combinatorics, and it does not depend
   on which generator is used.

6. **`k in I'` is necessary but not sufficient.** Every product lands on a
   normal form whose `I` contains `k` (check 2), but for `n >= 3` the image is a
   PROPER subset of `{(I,J) : k in I}` -- at `n = 3` the image has 2 elements
   while that set has 3. So the image is cut out by more than the membership
   condition.

7. **The tower map is NOT the naive index surgery.** Finding 5 says the image
   has the size of `NF(n-1)`, so the obvious guess is that dropping `k` from
   `I'` and closing the gap -- `(I',J') |-> (shift(I' ,k), shift(J', k))` --
   carries the image bijectively onto `NF(n-1)`. **It does, but only for
   `k = 1`.** For every `k >= 2`, at every `n = 3..7`, the map is neither
   injective nor onto.

   Recorded as a caught error rather than a finding: the first run printed only
   the `k = 1` row and read as a clean bijection at every `n`. It is a
   one-generator coincidence. This is consistent with finding 6 -- the image is
   a proper subset of `{(I,J) : k in I}` -- and says the same thing from the
   other side: the tower identification exists numerically and is not given by
   re-indexing.

Finding 5 is the one that points somewhere: it suggests proving closure through
the tower structure rather than through a rewriting measure, which finding 4
rules out. Finding 7 says that route still needs the right map, and the cheap
one is not it.

## Arithmetic

Exact integers, sets and tuples. No floating point anywhere.
"""

from __future__ import annotations

import json
import os
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import tl_normal_form_basis_probe as tlp  # noqa: E402  (guarded by __main__)

catalan = tlp.catalan

WITNESS = Path(__file__).with_name("tl-closure-rule.witness.json")

MAX_N = 7


def normal_pairs(m: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    """`(I, J)` for `TL_{m+1}`, generators `1..m` to match `tlp.gen`."""
    out = []
    for k in range(0, m + 1):
        for I in combinations(range(1, m + 1), k):
            for J in combinations(range(1, m + 1), k):
                if all(J[r] <= I[r] for r in range(k)):
                    out.append((I, J))
    return out


def pair_word(I: tuple[int, ...], J: tuple[int, ...]) -> tuple[int, ...]:
    w: list[int] = []
    for r in range(len(I)):
        w.extend(range(I[r], J[r] - 1, -1))
    return tuple(w)


def products(n: int):
    """Every `e_k · elt(I,J)`, as `(k, I, J, I', J', loops)`."""
    m = n - 1
    pairs = normal_pairs(m)
    d2p = {}
    for (I, J) in pairs:
        d, l = tlp.word_diagram(n, pair_word(I, J))
        assert l == 0, f"normal form {(I, J)} is not loop-free"
        assert d not in d2p, f"two normal forms share a diagram at n={n}"
        d2p[d] = (I, J)
    rows = []
    for k in range(1, n):
        ek = tlp.gen(n, k)
        for (I, J) in pairs:
            dw, _ = tlp.word_diagram(n, pair_word(I, J))
            d, loops = tlp.mul(n, ek, dw)
            assert d in d2p, f"e_{k}·{(I, J)} left the normal forms at n={n}"
            rows.append((k, I, J, *d2p[d], loops))
    return rows


def main() -> int:
    allrows = {n: products(n) for n in range(2, MAX_N + 1)}
    flat = [r for rs in allrows.values() for r in rs]
    total = len(flat)
    print(f"{total} products e_k · elt(I,J) over n = 2..{MAX_N}\n", flush=True)

    ok = True
    checks = []

    def rule(name, pred, subset=None):
        rows = flat if subset is None else subset
        bad = [r for r in rows if (r[5] == 1) != pred(r)]
        return {"rule": name, "counterexamples": len(bad), "of": len(rows),
                "holds": not bad}

    delta_rules = [
        rule("loops=1 <=> (I',J')=(I,J)", lambda r: (r[3], r[4]) == (r[1], r[2])),
        rule("loops=1 <=> k in I and k-1 not in I",
             lambda r: r[0] in r[1] and (r[0] - 1) not in r[1]),
        rule("loops=1 <=> k in I", lambda r: r[0] in r[1]),
        rule("loops=1 <=> k in I and k+1 not in I",
             lambda r: r[0] in r[1] and (r[0] + 1) not in r[1]),
        rule("loops=1 <=> k in I and k not in J",
             lambda r: r[0] in r[1] and r[0] not in r[2]),
    ]
    for d in delta_rules:
        verdict = "HOLDS" if d["holds"] else "fails %d" % d["counterexamples"]
        print("  %-44s %s" % (d["rule"], verdict), flush=True)
    ok &= delta_rules[0]["holds"] and delta_rules[1]["holds"]
    checks.append({"check": "delta_rule", "rules": delta_rules,
                   "pass": delta_rules[0]["holds"] and delta_rules[1]["holds"],
                   "note": ("the δ appears exactly at the fixed points, and the test "
                            "is on I alone -- J does not enter it")})

    # invariants on every product
    inv = {
        "k_in_I_prime": all(r[0] in r[3] for r in flat),
        "card_I_prime_eq_card_J_prime": all(len(r[3]) == len(r[4]) for r in flat),
        "loops_at_most_one": all(r[5] <= 1 for r in flat),
    }
    ok &= all(inv.values())
    print(flush=True)
    for k_, v in inv.items():
        print(f"  invariant {k_:32s} {'HOLDS' if v else '*** FAILS ***'}", flush=True)
    checks.append({"check": "invariants", "results": inv, "pass": all(inv.values())})

    # the open branch
    zero = [r for r in flat if r[5] == 0]
    def S(t):
        return frozenset(t)
    open_cands = [
        {"candidate": "I' = I union {k}",
         "counterexamples": sum(1 for r in zero if S(r[3]) != S(r[1]) | {r[0]})},
        {"candidate": "I' subset of I union {k}",
         "counterexamples": sum(1 for r in zero if not S(r[3]) <= S(r[1]) | {r[0]})},
        {"candidate": "J' subset of J union {k}",
         "counterexamples": sum(1 for r in zero if not S(r[4]) <= S(r[2]) | {r[0]})},
    ]
    dist = Counter(len(r[3]) - len(r[1]) for r in zero)
    print(flush=True)
    print(f"  loops=0 branch: {len(zero)} products, formula NOT identified", flush=True)
    for c in open_cands:
        print(f"     candidate {c['candidate']:28s} fails {c['counterexamples']}", flush=True)
    print(f"     |I'|-|I| distribution: {dict(sorted(dist.items()))}"
          f"   <- the negative entries are the source of the word-length "
          f"non-monotonicity", flush=True)
    checks.append({
        "check": "loops_zero_branch_formula",
        "status": "OPEN -- no candidate fits",
        "products": len(zero),
        "rejected_candidates": open_cands,
        "card_I_delta_distribution": {str(a): b for a, b in sorted(dist.items())},
        "pass": True,   # this check RECORDS an open item; it does not assert one
        "note": ("recorded as open. The |I'| decrease is what makes word length "
                 "non-monotone, so an insertion-shaped rule cannot be right."),
    })

    # 4-6. measures, injectivity, image
    print(flush=True)
    measures = [
        ("card_I", lambda I, J: len(I)),
        ("sum_block_lengths_eq_word_length",
         lambda I, J: sum(i - j + 1 for i, j in zip(I, J))),
        ("sum_I", lambda I, J: sum(I)),
        ("sum_J", lambda I, J: sum(J)),
        ("sum_i_minus_j", lambda I, J: sum(i - j for i, j in zip(I, J))),
        ("max_I", lambda I, J: max(I) if I else 0),
        ("min_I", lambda I, J: min(I) if I else 10 ** 6),
        ("sum_I_plus_sum_J", lambda I, J: sum(I) + sum(J)),
        ("lex_card_then_sum_I", lambda I, J: (len(I), sum(I))),
        ("lex_sum_then_card_I", lambda I, J: (sum(I), len(I))),
        ("tuple_I_lex", lambda I, J: I),
        ("tuple_J_lex", lambda I, J: J),
    ]
    mrows = []
    for name, f in measures:
        dec = eq = inc = 0
        for r in zero:
            a, b = f(r[1], r[2]), f(r[3], r[4])
            if b < a:
                dec += 1
            elif b == a:
                eq += 1
            else:
                inc += 1
        mrows.append({"measure": name, "decreases": dec, "equal": eq,
                      "increases": inc, "monotone": inc == 0})
        print(f"  measure {name:34s} down {dec:5d}  eq {eq:5d}  UP {inc:5d}",
              flush=True)
    any_monotone = any(r["monotone"] for r in mrows)
    ok &= not any_monotone or True   # this check RECORDS; it does not gate
    checks.append({
        "check": "no_natural_measure_is_monotone",
        "measures": mrows,
        "any_monotone": any_monotone,
        "pass": True,
        "note": ("every candidate increases on some product, so the word-length "
                 "negative is one row of a general pattern rather than special; "
                 "an induction of that shape does not exist"),
    })

    print(flush=True)
    img_rows = []
    for n in range(2, MAX_N + 1):
        rows = allrows[n]
        per_k = {}
        for (k, I, J, I2, J2, _l) in rows:
            per_k.setdefault(k, set()).add((I2, J2))
        allnf = {(I, J) for (k, I, J, _, _, _) in rows if k == 1}
        sizes = sorted(len(v) for v in per_k.values())
        eq_cat = all(sz == catalan(n - 1) for sz in sizes)
        cut_by_mem = all(img == {(I, J) for (I, J) in allnf if k in I}
                         for k, img in per_k.items())
        img_rows.append({"n": n, "normal_forms": len(allnf),
                         "image_sizes_per_k": sizes,
                         "catalan_n_minus_1": catalan(n - 1),
                         "image_size_eq_catalan_n_minus_1": eq_cat,
                         "image_eq_k_in_I_set": cut_by_mem})
        ok &= eq_cat
        print(f"  n={n}: |NF|={len(allnf):4d}  image sizes {sizes}  "
              f"catalan({n-1})={catalan(n-1):4d}  "
              f"{'MATCH' if eq_cat else '*** NO ***'}   "
              f"image = {{k in I}}: {'yes' if cut_by_mem else 'no'}", flush=True)
    checks.append({
        "check": "image_size_is_catalan_n_minus_one",
        "rows": img_rows,
        "pass": all(r["image_size_eq_catalan_n_minus_1"] for r in img_rows),
        "note": ("dim(e_k · TL_n) = dim TL_{n-1}, the tower relation, visible in "
                 "the normal-form combinatorics and independent of k; and for "
                 "n >= 3 the image is a PROPER subset of {(I,J) : k in I}, so "
                 "membership of k in I' does not cut it out"),
    })

    # 7. is the tower map the naive index surgery?
    print(flush=True)
    def _shift(t, k):
        return tuple(x if x < k else x - 1 for x in t if x != k)
    tower_rows = []
    for n in range(3, MAX_N + 1):
        target = set(normal_pairs(n - 2))
        per_k = {}
        for (k, I, J, I2, J2, _l) in allrows[n]:
            per_k.setdefault(k, set()).add((I2, J2))
        per_k_bij = {}
        for k, img in per_k.items():
            out = [(_shift(I, k), _shift(J, k)) for (I, J) in img]
            per_k_bij[k] = len(set(out)) == len(out) and set(out) == target
        tower_rows.append({"n": n, "target_size": len(target),
                           "bijection_per_k": {str(k): v for k, v in
                                               sorted(per_k_bij.items())},
                           "only_k_eq_1": all(v == (k == 1)
                                              for k, v in per_k_bij.items())})
        print(f"  n={n}: naive surgery is a bijection onto NF({n-2}) for k = "
              + ", ".join(f"{k}:{'yes' if v else 'no'}"
                          for k, v in sorted(per_k_bij.items())), flush=True)
    checks.append({
        "check": "tower_map_is_not_the_naive_index_surgery",
        "rows": tower_rows,
        "pass": True,
        "note": ("dropping k from I' and closing the gap carries the image "
                 "bijectively onto NF(n-1) for k = 1 ONLY; for every k >= 2 it is "
                 "neither injective nor onto. Recorded as a caught error: the "
                 "first run printed only the k = 1 row and read as general."),
    })

    payload = {
        "description": (
            "Closure of left multiplication on the Jones normal forms, indexed by "
            "(I,J). The δ rule is COMPLETE and holds on all "
            f"{total} products at n=2..{MAX_N}: loops=1 iff (I',J')=(I,J) iff "
            "k in I and k-1 not in I -- a condition on I alone. The (I',J') "
            "formula for the loops=0 branch is NOT identified and is recorded as "
            "open. Separately: no natural measure on (I,J) is monotone under the "
            "rewriting (12 tested, all increase somewhere), and the image of e_k "
            "has exactly catalan(n-1) elements for every k -- the tower relation "
            "dim(e_k TL_n) = dim TL_{n-1}."
        ),
        "bean": "qou-cds1",
        "products_tested": total,
        "arithmetic": "exact integers, sets and tuples; no floating point",
        "scope": ("checked at n <= 7, not proved at general n; the δ rule has a "
                  "proof sketch (e_k commutes past a block iff its top is <= k-2, "
                  "then e_k^2 = δ e_k) and is ready to formalise. Wires to nothing."),
        "checks": checks,
        "all_pass": ok,
    }
    payload.setdefault("scriptFile", os.path.basename(__file__))
    try:
        from qou_substrate.witness import WitnessBuilder as _WB
        _WB.stamp_staleness_metadata(payload, script_path=__file__, engine=None,
                                     q0_anchor=None)
    except Exception as exc:
        payload["provenance_note"] = f"stamp unavailable: {exc!r}"
    WITNESS.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"\nWROTE {WITNESS.name} — all_pass={ok}", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
