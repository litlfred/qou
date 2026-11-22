#!/usr/bin/env python3
"""The TL closure rule, found in the corpus and then CHECKED against the diagrams.

Bean `qou-cds1`. This probe closes the gap `tl_closure_rule_probe.py` left open,
and the way it closes it is the point.

## 🛑 CORRECTION to a merged artifact

`tl_closure_rule_probe.py` (PR #7096, on `main`) says, under a 🛑 heading:

> **What is NOT settled.** The `(I', J')` formula for the `loops = 0` branch.
> 2378 products, and none of the simple candidates fits [...] So the remaining
> rule is genuinely more intricate than an insertion.

The observation is correct and the verdict is wrong. **The rule was already in
this corpus when that was written.** `content/schema/references.ts` line 10450
registers Kim & Lee, *Gröbner-Shirshov bases for Temperley-Lieb algebras*
(Palestine J. Math. 7 (2018), Special Issue I, 11-17) — PDF held at
`library/fd58d8e182edda805fed0946606c5ab82f81/`, marked **"Read in full
2026-08-09"** — and the note on that entry states the two rewriting families
outright:

> the basis needs two families BEYOND the defining relations
> (`E_{i,j}E_i − E_{i−2,j}E_i` and `E_jE_{i,j} − E_jE_{i,j+2}`)

That is the missing formula, in the folio's own bibliography, eleven months
before the probe that called it unidentified. The failure was mine and it was
specifically **corpus-grep path 5** (ingested sources), which I ran only after
exhausting my guesses. The rule for next time is the one already written down:
run path 5 *first*, because an item can be open in this corpus and settled in a
paper we already hold.

## What the source says

Kim-Lee §3 reviews the type `A_{n-1}` case, quoting **Kang-Lee-Lee-Oh**,
*Hecke algebras, Specht modules and Gröbner-Shirshov bases*, J. Algebra 252
(2002) 258-292, **Prop. 6.2** — the primary, which this folio does NOT hold
(bean `qou-qspu`). Writing `E_{i,j} := E_i E_{i-1} ⋯ E_j` for `i ≥ j`, with the
convention `E_{i,i+1} = 1`, the Gröbner-Shirshov basis for degree-lex order with
`E_1 < E_2 < ⋯ < E_{n-1}` is

    (1)  E_i E_i        →  δ E_i
    (2)  E_i E_j        →  E_j E_i          (i > j+1)
    (3)  E_{i,j} E_i    →  E_{i-2,j} E_i    (i > j)
    (4)  E_j E_{i,j}    →  E_j E_{i,j+2}    (i > j)

and its standard monomials are `E_{i₁,j₁} ⋯ E_{i_p,j_p}` with
`i₁ < ⋯ < i_p`, `j₁ < ⋯ < j_p`, `j_r ≤ i_r`.

**That index set is exactly `NormalIdx m`** as already defined in
`QOU/MathlibExt/TemperleyLiebNormalForm.lean`, and `NormalIdx.word` is exactly
the standard monomial. So the two objects this arc built independently are the
published ones, and the count `card (NormalIdx m) = catalan (m+1)` — which the
Lean file currently has only for `m ≤ 6`, by `decide` — is Kang-Lee-Lee-Oh
Prop. 6.2. **It is a citation to formalise, not an open combinatorial search.**

## What this probe adds

The corpus recorded the rules; nobody checked them. Rules (1)-(4) are stated in
a source about type B, quoted from a primary we do not hold, in a δ convention
this folio had to match by hand. That is three places to be wrong. So:

1. **The rules reproduce the diagram product on all 3456 `e_k · elt(I,J)`
   products at `n = 2..7`** — the same products `tl_closure_rule_probe`
   measured, so this is checked against ground truth already validated against
   planar diagrams, not against itself. Both the resulting `(I', J')` and the δ
   power match.
2. **Closure on general products: 19,413 ordered pairs** of standard monomials
   at `n = 2..6` reduce to a standard monomial times `δ^k`, with no exceptions.
   This is the Remark after Kim-Lee Example 3.2 ("the product of two standard
   monomials becomes a standard monomial up to a scalar multiple"), verified.
3. **Confluence: 1000 words, 9 reduction orders each.** Random redex choice
   never yields two different normal forms. A Gröbner-Shirshov basis *is* a
   confluence claim, so this is the property being borrowed and it is the one
   `qou-43co` records the corpus getting wrong for `H_n(q)` — that system is
   NOT confluent, machine-refuted at `n = 4`. The TL quotient's is, and these
   two extra families are why.
4. **The paper's own worked examples**, from its Remark and Example 3.2:
   `(E₁E₂)(E_{2,1}E_{3,2}) = E₁E_{3,2}`, `E_{2,1}E_{3,1} = E_{2,1}E₃`, and the
   14 standard monomials of `A₃` — reproduced exactly.

## 🛑 A trap in implementing rule (4)

My first implementation matched rule (4) against the **maximal** descending run
after `E_j`, and reported **257 mismatches at n=7** — a wrong result about a
correct published rule, produced entirely by the checker. The redex
`E_j E_{i,j}` needs the run to end *at* `j`, which is in general a **prefix** of
the maximal run: in `E₂E₃E₂E₁` the maximal run after `E₂` is `E₃E₂E₁`, but the
redex is `E₂E₃E₂`, and `E₂E₃E₂E₁ = E₂E₁` is missed if only the maximal run is
tried. Rule (3) genuinely needs only the maximal run — a run prefix followed by
`E_i` cannot occur, since the run descends — and that asymmetry is what made
the wrong version look plausible.

## Arithmetic

Exact integers and tuples throughout. No floating point.
"""

from __future__ import annotations

import json
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import tl_closure_rule_probe as tlc  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WITNESS = Path(__file__).with_name("tl-gs-reduction.witness.json")

MAX_N_PRODUCT = 7
MAX_N_PAIRS = 6
CONFLUENCE_WORDS = 200
CONFLUENCE_ORDERS = 8
SEED = 20260907


def run_end(w: tuple[int, ...], t: int) -> int:
    """End (exclusive) of the maximal descending-by-one run starting at `t`."""
    e = t + 1
    while e < len(w) and w[e] == w[e - 1] - 1:
        e += 1
    return e


def redexes(w: tuple[int, ...]) -> list[tuple[tuple[int, ...], int]]:
    """Every applicable rewrite, as `(new word, δ exponent gained)`."""
    n = len(w)
    out: list[tuple[tuple[int, ...], int]] = []
    # (1) E_i E_i -> δ E_i
    for t in range(n - 1):
        if w[t] == w[t + 1]:
            out.append((w[: t + 1] + w[t + 2 :], 1))
    # (3) E_{i,j} E_i -> E_{i-2,j} E_i   (maximal run suffices; see docstring)
    for t in range(n):
        e = run_end(w, t)
        i, j = w[t], w[e - 1]
        if i > j and e < n and w[e] == i:
            out.append((w[:t] + tuple(range(i - 2, j - 1, -1)) + (i,) + w[e + 1 :], 0))
    # (4) E_j E_{i,j} -> E_j E_{i,j+2}   (run PREFIX ending at j; the trap)
    for t in range(n - 1):
        j, i = w[t], w[t + 1]
        if i <= j:
            continue
        for e in range(t + 2, run_end(w, t + 1) + 1):
            if w[e - 1] == j:
                out.append((w[: t + 1] + tuple(range(i, j + 1, -1)) + w[e:], 0))
    # (2) E_i E_j -> E_j E_i  (i > j+1)
    for t in range(n - 1):
        if w[t] > w[t + 1] + 1:
            out.append((w[:t] + (w[t + 1], w[t]) + w[t + 2 :], 0))
    return out


def reduce_word(w, rng=None):
    """Reduce to normal form; returns `(word, δ exponent)`."""
    d = 0
    guard = 0
    while True:
        rs = redexes(w)
        if not rs:
            return w, d
        w, dd = rng.choice(rs) if rng is not None else rs[0]
        d += dd
        guard += 1
        if guard >= 50000:
            raise AssertionError(f"reduction did not terminate on {w!r}")


def blocks(w: tuple[int, ...]) -> str:
    """Render a word in the paper's `E_{i,j}` block notation."""
    if not w:
        return "1"
    parts, t = [], 0
    while t < len(w):
        e = run_end(w, t)
        i, j = w[t], w[e - 1]
        parts.append(f"E{i}" if i == j else f"E{i},{j}")
        t = e
    return "".join(parts)


def check_products() -> dict:
    """(1) GS reduction vs the diagram-computed `e_k · elt(I,J)`."""
    rows, total, bad = [], 0, 0
    for n in range(2, MAX_N_PRODUCT + 1):
        prods = list(tlc.products(n))
        m = 0
        for (k, I, J, Ip, Jp, loops) in prods:
            red, d = reduce_word((k,) + tlc.pair_word(I, J))
            if red != tlc.pair_word(Ip, Jp) or d != loops:
                m += 1
        rows.append({"n": n, "products": len(prods), "mismatches": m})
        total += len(prods)
        bad += m
    return {"rows": rows, "products": total, "mismatches": bad, "pass": bad == 0}


def check_closure() -> dict:
    """(2) Product of two standard monomials is standard times δ^k."""
    rows, total, bad = [], 0, 0
    for n in range(2, MAX_N_PAIRS + 1):
        pairs = tlc.normal_pairs(n - 1)
        nf = {tlc.pair_word(I, J) for (I, J) in pairs}
        off = 0
        for a in pairs:
            wa = tlc.pair_word(*a)
            for b in pairs:
                red, _ = reduce_word(wa + tlc.pair_word(*b))
                if red not in nf:
                    off += 1
        rows.append({"n": n, "pairs": len(pairs) ** 2, "non_standard": off})
        total += len(pairs) ** 2
        bad += off
    return {"rows": rows, "pairs": total, "non_standard": bad, "pass": bad == 0}


def check_confluence() -> dict:
    """(3) Randomised redex choice never diverges."""
    rng = random.Random(SEED)
    rows, total, bad = [], 0, 0
    for n in range(3, MAX_N_PRODUCT + 1):
        pairs = tlc.normal_pairs(n - 1)
        diff = 0
        for _ in range(CONFLUENCE_WORDS):
            a, b = rng.choice(pairs), rng.choice(pairs)
            w = tlc.pair_word(*a) + tlc.pair_word(*b)
            outs = {reduce_word(w, rng) for _ in range(CONFLUENCE_ORDERS)}
            outs.add(reduce_word(w))
            if len(outs) != 1:
                diff += 1
        rows.append({"n": n, "words": CONFLUENCE_WORDS, "divergent": diff})
        total += CONFLUENCE_WORDS
        bad += diff
    return {
        "rows": rows,
        "words": total,
        "orders_per_word": CONFLUENCE_ORDERS + 1,
        "divergent": bad,
        "pass": bad == 0,
    }


def check_paper_examples() -> dict:
    """(4) Kim-Lee Example 3.2 and the Remark after it."""
    got = sorted(blocks(tlc.pair_word(I, J)) for (I, J) in tlc.normal_pairs(3))
    want = sorted(
        [
            "1", "E1", "E2,1", "E2", "E1E2", "E3,1", "E3,2", "E3",
            "E1E3,2", "E1E3", "E2,1E3,2", "E2,1E3", "E2E3", "E1E2E3",
        ]
    )
    r1, d1 = reduce_word((1, 2, 2, 1, 3, 2))   # (E1E2)(E2,1E3,2)
    r2, d2 = reduce_word((2, 1, 3, 2, 1))      # E2,1 E3,1
    return {
        "a3_standard_monomials": got,
        "a3_matches_example_3_2": got == want,
        "remark_1_lhs": "(E1E2)(E2,1E3,2)",
        "remark_1_result": blocks(r1),
        "remark_1_delta_power": d1,
        "remark_1_matches_paper": blocks(r1) == "E1E3,2",
        "remark_2_lhs": "E2,1E3,1",
        "remark_2_result": blocks(r2),
        "remark_2_delta_power": d2,
        "remark_2_matches_paper": blocks(r2) == "E2,1E3" and d2 == 0,
        "pass": got == want and blocks(r1) == "E1E3,2" and blocks(r2) == "E2,1E3",
    }


def main() -> int:
    _t0 = time.time()
    prod = check_products()
    clos = check_closure()
    conf = check_confluence()
    ex = check_paper_examples()

    print("Kim-Lee Prop. 3.1 GS reduction, checked against this folio's diagrams")
    print(f"  1. e_k·elt(I,J) vs diagrams: {prod['products']} products, "
          f"{prod['mismatches']} mismatches -> {'PASS' if prod['pass'] else 'FAIL'}")
    for r in prod["rows"]:
        print(f"       n={r['n']}: {r['products']:5d} products, mismatches={r['mismatches']}")
    print(f"  2. closure on monomial pairs: {clos['pairs']} pairs, "
          f"{clos['non_standard']} non-standard -> {'PASS' if clos['pass'] else 'FAIL'}")
    print(f"  3. confluence: {conf['words']} words x {conf['orders_per_word']} orders, "
          f"{conf['divergent']} divergent -> {'PASS' if conf['pass'] else 'FAIL'}")
    print(f"  4. paper's own examples: Example 3.2 "
          f"{'matches' if ex['a3_matches_example_3_2'] else 'DIFFERS'}; "
          f"{ex['remark_1_lhs']} = δ^{ex['remark_1_delta_power']}·{ex['remark_1_result']}; "
          f"{ex['remark_2_lhs']} = {ex['remark_2_result']} -> "
          f"{'PASS' if ex['pass'] else 'FAIL'}")

    all_pass = prod["pass"] and clos["pass"] and conf["pass"] and ex["pass"]

    witness = {
        "description": (
            "The Temperley-Lieb Gröbner-Shirshov reduction of Kim-Lee Prop. 3.1 "
            "(quoting Kang-Lee-Lee-Oh 2002 Prop. 6.2), checked against this folio's "
            "planar-diagram ground truth. Corrects tl_closure_rule_probe's claim that "
            "the (I',J') rule was unidentified: it was already in references.ts:10450, "
            "read 2026-08-09. Exact integer arithmetic; no floating point."
        ),
        "bean": "qou-cds1",
        "source": {
            "citation_key": "kimlee2018",
            "statement": "Prop. 3.1, quoting Kang-Lee-Lee-Oh, J. Algebra 252 (2002) 258-292, Prop. 6.2",
            "pdf": "library/fd58d8e182edda805fed0946606c5ab82f81/",
            "primary_not_held": "qou-qspu",
        },
        "rules": [
            "E_i E_i -> delta E_i",
            "E_i E_j -> E_j E_i   (i > j+1)",
            "E_{i,j} E_i -> E_{i-2,j} E_i   (i > j)",
            "E_j E_{i,j} -> E_j E_{i,j+2}   (i > j)",
        ],
        "checks": {
            "products_vs_diagrams": prod,
            "closure_on_pairs": clos,
            "confluence": conf,
            "paper_examples": ex,
        },
        "all_pass": all_pass,
    }
    WitnessBuilder.wrap_legacy(
        "tl-gs-reduction", witness, script_path=__file__,
        output_dir=WITNESS.parent, start_time=_t0,
    ).save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Pure Temperley-Lieb combinatorics: normal-form words, planar "
            "diagrams and set/tuple indices, over exact integers. No substrate "
            "q0 is read on any path, and delta appears only as a symbolic "
            "exponent count, never as a number."
        ),
    })
    print(f"\nWROTE {WITNESS.name} — all_pass={all_pass}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
