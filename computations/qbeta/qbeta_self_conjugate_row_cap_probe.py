#!/usr/bin/env python3
"""The row cap leaves exactly three self-conjugate shapes — none past level 4.

The symmetry energy DOES have a derived route in this corpus, and the binding arc
has been looking in the wrong channel. `mass-theory` carries the Wigner energy
`-Delta_W . T(T+1)/A` built from SELF-CONJUGATE shadow prices
(`unified-iterative-correction-proof.md`; the general rule is in
`figure-eight-branching-rule-proof.md`: self-conjugate partitions contribute the
isospin Casimir terms `T(T+1)/A`, `T(T+1)(T+2)/A^2`). That supersedes "the
symmetry energy has a named gap with NO available route" from a second,
independent direction. Bean `qou-a5jk`; instantiates
`QOU/Hecke/SelfConjugateRowCap.lean`.

*** THE TENSION ***

`QOU/Hecke/RowCap.lean` proves the fibre-dimension cap: a column of height >= 3
has no injective filling into a 2-dimensional fibre, so `l(lambda) > 2 =>
y_lambda = 0` under convention D. The Wigner mechanism names two shadow prices:

    lambda = (2,2)    k = 4    l = 2    SURVIVES the cap
    lambda = (3,1,1)  k = 5    l = 3    zero Markov weight

And it is not one shape. **Self-conjugacy forces `l(lambda) = lambda_1`** — the
diagram has as many rows as its first row has columns — so `l <= 2` means the
whole diagram fits in a 2x2 box. Exactly three survive:

    (1)      n = 1
    (2,1)    n = 3
    (2,2)    n = 4

and NONE at any `n >= 5`. The self-conjugate partitions do not stop existing —
2 at n = 8, 3 at n = 12 — they simply all have three or more rows.

*** 🛑 WHAT THIS IS NOT ***

This is a TENSION, not a refutation, and the difference is load-bearing. The
shadow prices `C_lambda` are described as q-integer products of hooks, contents
and Frobenius coordinates; `y_lambda` enters the same construction separately, as
the budget constraint `sum_lambda d_lambda y_lambda = 1`. **Whether
`y_lambda = 0` forces `C_lambda = 0` is not established anywhere in the corpus,
and nothing here assumes it.** Every assertion below is about partition shapes;
the Lean file likewise proves only list-length facts, with no dependency on the
LP. So the enumeration stands whichever way that question goes — and the question
is the successor.
"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
NMAX = 30


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def conj(lam):
    """Conjugate partition: column heights."""
    if not lam:
        return []
    return [sum(1 for x in lam if x > j) for j in range(lam[0])]


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield []
        return
    for f in range(min(n, mx), 0, -1):
        for rest in partitions(n - f, f):
            yield [f] + rest


def content_sum(lam):
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    print("=" * 78)
    print(f"1. EVERY SELF-CONJUGATE PARTITION WITH AT MOST TWO ROWS, n <= {NMAX}")
    print("=" * 78)
    survivors = []
    for n in range(1, NMAX + 1):
        for p in partitions(n):
            if p == conj(p) and len(p) <= 2:
                survivors.append({"n": n, "lambda": tuple(p), "ell": len(p),
                                  "content_sum": content_sum(p)})
                print(f"    n={n:>3}   lambda={str(tuple(p)):>8}   ell={len(p)}"
                      f"   c(lambda)={content_sum(p)}")
    ok &= chk("exactly_three_self_conjugate_shapes_survive_the_row_cap",
              [s["lambda"] for s in survivors], [(1,), (2, 1), (2, 2)],
              note="self-conjugacy forces ell(lambda) = lambda_1, so ell <= 2 "
                   "puts the whole diagram in a 2x2 box. Lean: "
                   "selfConj_two_row_enum")
    ok &= chk("and_all_of_them_have_at_most_four_cells",
              max(s["n"] for s in survivors), 4,
              note="so a mechanism resting on self-conjugate shadow prices has "
                   "NOTHING to draw on above k = 4. Lean: "
                   "selfConj_two_row_size_le_four")
    ok &= chk("all_three_have_content_sum_zero",
              [s["content_sum"] for s in survivors], [0, 0, 0],
              note="c(lambda) = 0 is the isospin-sensitive class in "
                   "figure-eight-branching-rule-proof.md's scaling rule "
                   "(positive -> volume, negative -> charge, zero -> "
                   "T(T+1)/A^p). So the survivors are all of the right TYPE; "
                   "there are just three of them")

    print()
    print("=" * 78)
    print("2. THE TWO WIGNER SHADOW PRICES THE CORPUS NAMES")
    print("=" * 78)
    print(f"    {'lambda':>10}{'k':>4}{'self-conj':>12}{'ell':>5}{'c':>4}   fate")
    named = []
    for p in ([2, 2], [3, 1, 1]):
        sc = (p == conj(p))
        fate = "SURVIVES" if len(p) <= 2 else "y_lambda = 0 (ell > 2)"
        named.append({"lambda": tuple(p), "k": sum(p), "self_conjugate": sc,
                      "ell": len(p), "content_sum": content_sum(p), "fate": fate})
        print(f"    {str(tuple(p)):>10}{sum(p):>4}{str(sc):>12}{len(p):>5}"
              f"{content_sum(p):>4}   {fate}")
    ok &= chk("the_k5_wigner_shape_has_three_rows",
              [n["ell"] for n in named], [2, 3],
              note="(2,2) survives, (3,1,1) does not. Both are self-conjugate "
                   "with c = 0, so the row cap is the ONLY thing separating them")

    print()
    print("=" * 78)
    print("3. SELF-CONJUGATE PARTITIONS DO NOT STOP EXISTING — THEY GET TALLER")
    print("=" * 78)
    print(f"    {'n':>4}{'self-conj':>12}{'survive ell<=2':>16}   shapes surviving")
    census = []
    for n in range(1, 13):
        sc = [p for p in partitions(n) if p == conj(p)]
        sv = [p for p in sc if len(p) <= 2]
        census.append({"n": n, "self_conjugate": len(sc), "surviving": len(sv)})
        print(f"    {n:>4}{len(sc):>12}{len(sv):>16}   "
              f"{[tuple(p) for p in sv] if sv else '--'}")
    ok &= chk("none_survive_at_any_level_five_or_above",
              [c["surviving"] for c in census if c["n"] >= 5], [0]*8,
              note="there are 2 self-conjugate partitions at n = 8 and 3 at "
                   "n = 12; every one of them has three or more rows")

    print()
    print("=" * 78)
    print("4. WHAT IS ESTABLISHED, AND THE ONE STEP DELIBERATELY NOT TAKEN")
    print("=" * 78)
    print("  ESTABLISHED: the enumeration, unconditionally. It is a fact about")
    print("  partition shapes and needs nothing from the LP.")
    print()
    print("  NOT ESTABLISHED: that this kills the Wigner term. C_lambda is a")
    print("  q-integer product of hooks, contents and Frobenius coordinates;")
    print("  y_lambda enters separately as the budget sum_lambda d_lambda")
    print("  y_lambda = 1. Whether y_lambda = 0 forces C_lambda = 0 is not")
    print("  established anywhere, and nothing here assumes it.")
    print()
    print("  THE SUCCESSOR is exactly that implication. If it holds, the Wigner")
    print("  mechanism is capped at k = 4 and the symmetry energy needs a")
    print("  non-self-conjugate source. If it does not, the mechanism is intact")
    print("  and the binding arc simply had the wrong channel all along.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-self-conjugate-row-cap",
        "q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"n_max": NMAX,
                       "row_cap": "l(lambda) > 2 => y_lambda = 0 (convention D, "
                                  "QOU/Hecke/RowCap.lean)",
                       "lean": "QOU/Hecke/SelfConjugateRowCap.lean",
                       "note": "TENSION, not refutation: whether y_lambda = 0 "
                               "forces C_lambda = 0 is NOT established and is "
                               "not assumed anywhere here"},
        "data": {"survivors": survivors, "named_wigner_shapes": named,
                 "census_by_level": census},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_self_conjugate_row_cap_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-self-conjugate-row-cap.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
