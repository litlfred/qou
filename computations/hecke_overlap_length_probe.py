#!/usr/bin/env python3
"""Overlap lengths in `heckeCompletedRewritingSystem`.

Every `_resolves` namespace in `HeckeCompletion.lean` is indexed by the SHAPE of
the composition, not by the kinds of its two rules, and every one of them fixes
`overlap` to a single letter (`CyclicQuad`, `CyclicQuadLeft`, `BraidSelfOverlap`,
`FarCommCyclic`, `CyclicFarCommLow`, `BokutShiaoBraid`, `BraidBokutShiao`,
`BokutShiaoFarComm`, and the `CornerGeneral` family).  The criterion, by
contrast, quantifies over every `OverlapComposition` -- so the question that
decides how much of the criterion those namespaces can reach is:

    can a composition of two rules of the completed system have
    `overlap.length > 1`?

This enumerates the rules at small `n`, forms every `(left, overlap, right)` with
`lm1 = left ++ overlap`, `lm2 = overlap ++ right` and `overlap != []`, and
reports the length distribution -- split by whether the composition is PROPER
(both contexts non-empty, the case `IsGrobnerShirshovBasis.overlap_resolves`
actually has content for) or degenerate.

Leading monomials, from the four `_lm` lemmas:

    heckeRelation i        [i, i]
    yangBaxterRelation i j [j, i, j]           j = i+1
    farCommRelation  i j   [i, j]              j+1 < i
    bokutShiaoRelation i' i j
                           descWord i j ++ [i] = [i, i-1, ..., j, i]
                                                  i'+1 = i, j <= i'

No floats anywhere: this is pure list combinatorics over `Fin n` indices, so the
NO-FLOAT64 family of gates is satisfied by construction.
"""
from collections import Counter
from itertools import product


def desc_word(i: int, j: int) -> tuple:
    """descWord i j = [i, i-1, ..., j]; `descWord_self` gives [i] at j = i."""
    return tuple(range(i, j - 1, -1))


def rules(n: int):
    """(kind, indices, leading monomial) for every rule of the completed system."""
    out = []
    for i in range(n):
        out.append(("quad", (i,), (i, i)))
    for i in range(n):
        j = i + 1
        if j < n:
            out.append(("yb", (i, j), (j, i, j)))
    for i in range(n):
        for j in range(n):
            if j + 1 < i:
                out.append(("fc", (i, j), (i, j)))
    for i in range(n):
        for ip in range(n):
            if ip + 1 != i:
                continue
            for j in range(n):
                if j <= ip:
                    out.append(("bs", (ip, i, j), desc_word(i, j) + (i,)))
    return out


def compositions(n: int):
    """Every (r1, r2, left, overlap, right) with a non-empty overlap."""
    rs = rules(n)
    for (k1, x1, lm1), (k2, x2, lm2) in product(rs, repeat=2):
        for k in range(1, min(len(lm1), len(lm2)) + 1):
            if lm1[len(lm1) - k:] == lm2[:k]:
                yield (k1, x1, lm1), (k2, x2, lm2), lm1[:len(lm1) - k], lm1[len(lm1) - k:], lm2[k:]


def report(n: int):
    proper, degen, by_pair = Counter(), Counter(), Counter()
    long_examples = []
    for r1, r2, left, ov, right in compositions(n):
        if left and right:
            proper[len(ov)] += 1
            by_pair[(r1[0], r2[0])] += 1
            if len(ov) > 1:
                long_examples.append((r1, r2, left, ov, right))
        else:
            degen[len(ov)] += 1
    return proper, degen, by_pair, long_examples


def shape_counts(n: int):
    """§4k counts SHAPES: it deduplicates leading monomials first (`completedLMSet`),
    because two rules on one leading monomial give one shape.  This reproduces
    that count, which is a different number from the rule-level count above."""
    lms = sorted({lm for _, _, lm in rules(n)})
    proper, degen = set(), set()
    for lm1, lm2 in product(lms, repeat=2):
        for k in range(1, min(len(lm1), len(lm2)) + 1):
            if lm1[len(lm1) - k:] == lm2[:k]:
                shape = (lm1, lm2, lm1[:len(lm1) - k], lm1[len(lm1) - k:], lm2[k:])
                (proper if (shape[2] and shape[4]) else degen).add(shape)
    return len(lms), proper, degen


def main() -> int:
    print("n | rules | proper | overlap-length histogram (proper) | degenerate")
    print("--+-------+--------+-----------------------------------+-----------")
    all_long = []
    for n in range(2, 9):
        proper, degen, by_pair, long_examples = report(n)
        hist = " ".join(f"len{k}={v}" for k, v in sorted(proper.items()))
        print(f"{n} | {len(rules(n)):5d} | {sum(proper.values()):6d} | "
              f"{hist:33s} | {sum(degen.values())}")
        all_long.extend(long_examples)
        if n == 4:
            n4 = (proper, degen, by_pair)

    print()
    print("Shape-level counts (leading monomials deduplicated, as §4k counts them):")
    print("n | distinct lms | proper shapes | degenerate shapes")
    for n in range(2, 9):
        nlm, sp, sd = shape_counts(n)
        print(f"{n} | {nlm:12d} | {len(sp):13d} | {len(sd)}")

    print()
    print("Proper compositions at n = 4, by rule-kind pair (RULE level, not shape):")
    for pair, c in sorted(n4[2].items()):
        print(f"  {pair[0]:>4s} x {pair[1]:<4s} {c}")

    print()
    if all_long:
        print(f"MULTI-LETTER proper overlaps found: {len(all_long)}")
        for e in all_long[:10]:
            print("   ", e)
    else:
        total = sum(sum(report(n)[0].values()) for n in range(2, 9))
        print(f"MULTI-LETTER proper overlaps found: 0, out of {total} proper")
        print("  compositions at n = 2..8.  Every proper composition of the")
        print("  completed system overlaps in exactly ONE letter -- which is the")
        print("  shape every `_resolves` namespace in HeckeCompletion.lean fixes.")

    # --- assertions ---------------------------------------------------------
    for n in range(2, 9):
        pr, _, _, _ = report(n)
        assert set(pr) == {1}, f"n={n}: proper overlap lengths {sorted(pr)} != [1]"

    nlm4, sp4, sd4 = shape_counts(4)
    assert len(rules(4)) == 16, f"n=4 rule count {len(rules(4))} != 16"
    assert nlm4 == 13, f"n=4 distinct leading monomials {nlm4} != 13"
    assert len(sp4) == 45, f"n=4 proper SHAPES {len(sp4)} != 45"
    assert len(sd4) == 13, f"n=4 degenerate SHAPES {len(sd4)} != 13"
    assert len(sp4) + len(sd4) == 58, "4k's total shape count is 58"
    assert sum(n4[0].values()) == 70, "n=4 rule-level proper count is 70, not 45"
    assert sum(n4[2].values()) == 70 and len(n4[2]) == 15, \
        "15 of the 16 rule-kind pairs occur at n=4"
    print()
    print("assertions: 8/8 pass")
    print("  16 rules -> 13 distinct leading monomials -> 58 shapes = 45 proper")
    print("  + 13 degenerate, reproducing §4k exactly.  At RULE level the proper")
    print("  count is 70, not 45: the two differ because 3 leading monomials")
    print("  carry two rules each (§4j).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
