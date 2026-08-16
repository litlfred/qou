#!/usr/bin/env python3
"""hecke_corner_le_regime — the shape of the corner's `a ≤ b` regime.

The `a > b` regime is a loop over one index, each pass a Bokut–Shiao step plus a
far-commutation transport, and it is proved in Lean at every pair of depths
(`UGB.GrobnerShirshov.Hecke.CornerGeneral.resolves`). This measures the other
regime, the one that remains, before any Lean is written for it — the same order
of work that `hecke_corner_block_blueprint.py` did for the first.

The chain splits as

    prefix(a)     a² + a + 5 steps, depending on `a` alone, and containing both
                  applications of the quadratic rule
    block(a,b)    ab − a² + 2a − 3 far-commutations, and nothing else
    two steps
    block(a,b)    the very same sequence again

    a² + a + 5 + 2[ab − a² + 2a − 3] + 2  =  2ab − a² + 5a + 1   ✓

which reproduces the fitted length exactly. Both formulas are quadratic; an
earlier guess that the prefix was linear (`6a − 1`) fitted `a = 2, 3` and failed
from `a = 4` on, which is why this checks the split at each `(a, b)` rather than
inferring it from the length.

The block is itself a **nested double loop**: `a` levels, level `p` a run of
far-commutations `F_{p,q}` with `q` ascending to `b`, of lengths `2, 3, 4, …`
capped at `b − a + 2`. That is why the length depends on both depths rather than
one, which the `a > b` regime did not.

The prefix, in turn, splits as `A · B₁₀ · C · D` with

    A = (a² − 3a + 10)/2      C = a(a+1)/2      D = 2a − 1

and it is **self-similar**: `C = A[2:] ++ small(a)` and
`D = [B₁₀, B₂₁] ++ small(a)`, where `small(a)` is a far-commutation block of
length `2a − 3` — the same "block · two steps · block" shape the whole chain has.
More: `A` is `[B₂₁ F₀₂]`, then passes of exactly the `a > b` regime's loop — a
Bokut–Shiao step at top `d` followed by `d` far-commutations, for `d = 1 … a−3` —
then one more Bokut–Shiao step, then `Y_{a,a−1} Q_a`. So the loop already proved
in Lean recurs inside this regime, and the only steps in the whole chain that are
not loop passes or far-commutations are those two: the chain uses the quadratic
rule exactly twice, at the end of `A` and at the end of `C`'s non-block part.

Rule names are resolved through a map replayed from the engine's own
`build_rules` rather than parsed from the strings, which are ambiguous once an
index reaches two digits.

Emits `hecke-corner-le-regime.witness.json`. Bean qou-auq3.
"""
from __future__ import annotations
import importlib.util, sys
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402
_spec = importlib.util.spec_from_file_location("eng", HERE / "hecke_gs_confluence_n4.py")
eng = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(eng)

RMAP = {}


def retune(n):
    eng.N = n
    eng.RULES = eng.build_rules()
    eng.LM = {name: lm for name, _, lm in eng.RULES}
    eng.REL = {name: rel for name, rel, _ in eng.RULES}
    eng.LC = {name: eng.REL[name][eng.LM[name]] for name in eng.LM}
    global RMAP
    RMAP = {}
    for i in range(n):
        RMAP[f"Q{i}"] = ("Q", i)
    for ip in range(n):
        if ip + 1 < n:
            RMAP[f"Y{ip}{ip+1}"] = ("Y", ip, ip + 1)
    for i in range(n):
        for j in range(n):
            if j + 1 < i:
                RMAP[f"F{i}{j}"] = ("F", i, j)
    for ip in range(n):
        if ip + 1 >= n:
            continue
        for j in range(n):
            if j <= ip:
                RMAP[f"B{ip}{ip+1}{j}"] = ("B", ip, ip + 1, j)
    assert len(RMAP) == len(eng.RULES), \
        f"rule-name collision at n={n}: {len(RMAP)} names for {len(eng.RULES)} rules"


def chain(i, a, b):
    j1, j2 = i - a, i - b
    d1, e2 = eng.desc_word(i, j1), eng.desc_word(i - 1, j2)
    n1, n2 = f"B{i-1}{i}{j1}", f"B{i-1}{i}{j2}"
    f = dict(eng.clean(eng.combine(
        {w: eng.LC[n2] * c
         for w, c in eng.context_mul((), eng.REL[n1], e2 + (i,)).items()},
        {w: eng.LC[n1] * c
         for w, c in eng.context_mul(d1, eng.REL[n2], ()).items()}, -1)))
    out = []
    for _ in range(4000):
        target = None
        for w in sorted(f.keys(), key=eng.deglex_key):
            for name in eng.LM:
                if eng.infix_positions(w, eng.LM[name]):
                    target = (w, name, eng.infix_positions(w, eng.LM[name])[0]); break
            if target:
                break
        if target is None:
            return out
        w, name, k = target
        left, right = w[:k], w[k + len(eng.LM[name]):]
        coeff = sp.expand(f[w] / eng.LC[name])
        out.append(RMAP[name])
        f = eng.clean(eng.combine(f, eng.context_mul(left, eng.REL[name], right),
                                  -coeff))
    raise RuntimeError("no normal form")


def rel_of(r, i):
    """A rule description in indices relative to `i`."""
    return (r[0],) + tuple(i - x for x in r[1:])


def main():
    import time
    started = time.monotonic()
    rows, bad = [], 0
    for a in range(2, 6):
        for b in range(a, a + 5):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            retune(n)
            c = [rel_of(r, i) for r in chain(i, a, b)]
            pred = 2 * a * b - a * a + 5 * a + 1
            blk = a * b - a * a + 2 * a - 3
            pre = a * a + a + 5
            b1 = c[pre:pre + blk]
            mid = c[pre + blk:pre + blk + 2]
            b2 = c[pre + blk + 2:]
            # the prefix's own split, and its self-similarity
            P = c[:pre]
            # the two B10 steps bracket C; on the diagonal b = a they carry the
            # same bottom, so take the first and the last rather than match on it
            bpos = [k for k, r in enumerate(P)
                    if r[0] == "B" and r[1] == 1 and r[2] == 0]
            apos, dpos = bpos[0], bpos[-1]
            A, C, D = P[:apos], P[apos + 1:dpos], P[dpos:]
            small = 2 * a - 3
            # at a = 2 the rule at top i-1 degenerates to the braid word, and the
            # engine names it Y rather than B; both are in the system
            toprule = D[1] in (("B", 2, 1, a), ("Y", 2, 1))
            selfsim = (len(A) == (a * a - 3 * a + 10) // 2
                       and len(C) == a * (a + 1) // 2 and len(D) == 2 * a - 1
                       and C == A[2:] + C[len(C) - small:]
                       and D[0] == ("B", 1, 0, b) and toprule
                       and D[2:] == C[len(C) - small:])
            good = (len(c) == pred and pre + 2 * blk + 2 == pred
                    and len(b2) == blk and b1 == b2
                    and all(r[0] == "F" for r in b1 + b2)
                    and all(r[0] != "F" for r in mid)
                    and sum(1 for r in c if r[0] == "Q") == 2
                    and all(r[0] != "Q" for r in c[pre:])
                    and selfsim)
            bad += not good
            rows.append({"a": a, "b": b, "n": n, "i": i, "steps": len(c),
                         "predicted_steps": pred, "prefix": pre, "block": blk,
                         "quadratic_steps": sum(1 for r in c if r[0] == "Q"),
                         "prefix_A": len(A), "prefix_C": len(C),
                         "prefix_D": len(D),
                         "decomposition_holds": good})

    w = WitnessBuilder("hecke-corner-le-regime", engine="sympy",
                       start_time=started)
    w.set_description(
        "The Bokut-Shiao corner's a <= b regime splits as prefix(a) . block(a,b) "
        ". two steps . block(a,b), with prefix = a^2 + a + 5 and block = "
        "ab - a^2 + 2a - 3 far-commutations, summing to the fitted "
        "2ab - a^2 + 5a + 1. Both quadratic; the block is a nested double loop.")
    w.add_parameter("prefix_formula", "a^2 + a + 5")
    w.add_parameter("block_formula", "ab - a^2 + 2a - 3")
    w.add_parameter("total_formula", "2ab - a^2 + 5a + 1")
    w.add_parameter("prefix_split", "A . B10 . C . D")
    w.add_parameter("prefix_A_formula", "(a^2 - 3a + 10)/2")
    w.add_parameter("prefix_C_formula", "a(a+1)/2")
    w.add_parameter("prefix_D_formula", "2a - 1")
    w.add_parameter("self_similarity", "C = A[2:] ++ small(a),  D = [B10,B21] ++ small(a)")
    w.add_parameter("small_block", "2a - 3")
    w.add_parameter("lean_theorem_for_the_other_regime",
                    "UGB.GrobnerShirshov.Hecke.CornerGeneral.resolves")
    w.add_assertion("cases_where_the_decomposition_fails",
                    computed=str(bad), expected="0")
    w.add_assertion("chains_not_using_the_quadratic_rule_exactly_twice",
                    computed=str(sum(1 for r in rows if r["quadratic_steps"] != 2)),
                    expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "Measured over a = 2..5 and b = a..a+4 only, and against the reduction "
        "the engine's deg-lex strategy happens to produce. A Lean proof may "
        "follow a different chain, as it does in the a > b regime at a = b + 1.")
    w.add_caveat(
        "The formulas are fitted and checked, not derived. An earlier fit for "
        "the prefix, linear in a, matched a = 2 and 3 and failed at a = 4.")
    path = w.save()

    print("  a   b    len  pred  prefix  block   split")
    for r in rows:
        print(f" {r['a']:>2}  {r['b']:>2}  {r['steps']:>5} {r['predicted_steps']:>5}"
              f"  {r['prefix']:>6} {r['block']:>6}   "
              f"{'ok' if r['decomposition_holds'] else 'FAILS'}")
    print(f"\ncases: {len(rows)}   failing: {bad}")
    print("\nblock, by level:")
    for a in (2, 3, 4, 5):
        b = a + 2
        n, i = a + b + 3, a + b + 1
        retune(n)
        c = [rel_of(r, i) for r in chain(i, a, b)]
        blk, pre = a * b - a * a + 2 * a - 3, a * a + a + 5
        print(f"  a={a} b={b}: "
              + " ".join(f"F{r[1]}{r[2]}" for r in c[pre:pre + blk]))
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
