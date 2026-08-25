#!/usr/bin/env python3
"""hecke_quad_pair_shape — the word-level shape of the two quadratic steps.

`hecke_corner_le_regime.py` established that the Bokut–Shiao corner's `a ≤ b`
regime uses the quadratic rule **exactly twice** in the whole chain, each time
immediately after a Yang–Baxter step, as the pair `Y_{a,a−1} Q_a`. Everything
else in the chain is a pass of the loop already proved in Lean
(`UGB.GrobnerShirshov.Hecke.CornerBlock.loopTwo` and friends) or a
far-commutation. So those two steps are the only genuinely new Lean content,
and `monicStep` cannot reach them: the quadratic rule has three words, so a
single step by it turns one term into *two*.

Writing that step in Lean needs the **contexts** — the `a` and `b` with
`W = a ++ [σ_z, σ_z] ++ b` — as functions of the depths, not just the rule
names. That is what this measures, on the same principle that the split was
measured before any Lean was written for it: the previous fit for the prefix
length was linear in `a`, matched `a = 2, 3`, and failed from `a = 4`.

For each `(a, b)` it replays the chain, records `(rule, word, position)` at
every step rather than the rule alone, and reports the two quadratic steps with
their surrounding words. Letters are printed relative to `i` — `σ_{i−x}` prints
as `x` — since that is the frame the Lean lemmas are stated in (`j₁ = i − a`,
`j₂ = i − b`).

## What it found

Both occurrences apply the **same** rule, `heckeRelation j₁`, and both are
preceded by the **same** Yang–Baxter step, `yangBaxterRelation j₁ (j₁+1)`. Their
contexts differ by exactly one letter at each end:

    occurrence 1:  L                ++ [σ_{j₁}, σ_{j₁}] ++ descWord (j₁−1) j₂ ++ [σ_i]
    occurrence 2:  [σ_{i−2}] ++ L   ++ [σ_{j₁}, σ_{j₁}] ++ descWord (j₁−1) j₂

with the common left part

    L = descWord (i−1) (j₁+2) ++ descWord i (j₁+3)
          ++ [σ_{j₁+1}, σ_{j₁+2}, σ_{j₁}, σ_{j₁+1}]

uniformly in `a`, including `a = 2`, where both `descWord`s are empty. Unlike
the prefix split, this family has no degenerate case.

The consequence for the Lean is the useful part: since the two differ only in
their contexts, **one lemma taking the contexts as parameters covers both** —
the analogue of `monicStep` (§4x) for the three-word quadratic rule, which turns
one term into two rather than one. The context formulas above are then needed
only to assemble the chain, not to state or prove the step.

Emits `hecke-quad-pair-shape.witness.json`. Bean qou-auq3.
"""
from __future__ import annotations
import importlib.util, sys, time
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
    """Replay the corner chain, recording `(rule, word, position)` per step."""
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
        out.append((RMAP[name], w, k, left, right))
        f = eng.clean(eng.combine(f, eng.context_mul(left, eng.REL[name], right),
                                  -coeff))
    raise RuntimeError("no normal form")


def rel_word(w, i):
    """A word in indices relative to `i`: `σ_{i−x}` becomes `x`."""
    return tuple(i - x for x in w)


def rel_of(r, i):
    return (r[0],) + tuple(i - x for x in r[1:])


def main():
    started = time.monotonic()
    rows, mismatch = [], 0
    for a in range(2, 8):
        for b in (a, a + 1, a + 3):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            retune(n)
            steps = chain(i, a, b)
            qidx = [k for k, s in enumerate(steps) if s[0][0] == "Q"]
            assert len(qidx) == 2, f"a={a} b={b}: {len(qidx)} quadratic steps"
            for which, k in enumerate(qidx):
                (rule, w, pos, left, right) = steps[k]
                z = rule[1]                       # absolute index of the quad rule
                prev = steps[k - 1]
                # the measured contexts, relative to i (see the module docstring
                # for the absolute-index reading)
                pred_left = (tuple(range(1, a - 1)) + tuple(range(0, a - 2))
                             + (a - 1, a - 2, a, a - 1))
                if which == 1:
                    pred_left = (2,) + pred_left
                pred_right = tuple(range(a + 1, b + 1)) + ((0,) if which == 0 else ())
                got_left, got_right = rel_word(left, i), rel_word(right, i)
                ok = (rel_of(prev[0], i) == ("Y", a, a - 1)
                      and i - z == a
                      and got_left == pred_left
                      and got_right == pred_right)
                mismatch += not ok
                rows.append({
                    "a": a, "b": b, "n": n, "i": i,
                    "occurrence": which + 1,
                    "quad_index_rel_i": i - z,
                    "preceded_by": "".join(str(x) for x in rel_of(prev[0], i)),
                    "left_context_rel_i": list(got_left),
                    "right_context_rel_i": list(got_right),
                    "word_rel_i": list(rel_word(w, i)),
                    "left_matches": got_left == pred_left,
                    "right_matches": got_right == pred_right,
                    "shape_holds": ok,
                })

    w = WitnessBuilder("hecke-quad-pair-shape", engine="sympy", start_time=started)
    w.set_description(
        "Word-level contexts of the two quadratic steps in the Bokut-Shiao "
        "corner's a <= b regime. Both apply the SAME rule, heckeRelation j1, "
        "and both are preceded by yangBaxterRelation j1 (j1+1). The two "
        "contexts differ by one letter at each end: the second occurrence has "
        "sigma_{i-2} prepended on the left and lacks the trailing sigma_i on "
        "the right. So one general step lemma with arbitrary contexts covers "
        "both -- the analogue of monicStep for the three-word quadratic rule.")
    w.add_parameter("quad_rule", "heckeRelation j1,  j1 = i - a, both occurrences")
    w.add_parameter("preceding_rule", "yangBaxterRelation j1 (j1+1), both occurrences")
    w.add_parameter(
        "left_context_first",
        "rel: [1..a-2] ++ [0..a-3] ++ [a-1, a-2, a, a-1]; "
        "abs: descWord (i-1) (j1+2) ++ descWord i (j1+3) "
        "++ [s_{j1+1}, s_{j1+2}, s_{j1}, s_{j1+1}]")
    w.add_parameter("left_context_second", "[s_{i-2}] ++ left_context_first")
    w.add_parameter("right_context_first", "descWord (j1-1) j2 ++ [s_i]")
    w.add_parameter("right_context_second", "descWord (j1-1) j2")
    w.add_assertion("quad_steps_not_matching_the_measured_shape",
                    computed=str(mismatch), expected="0")
    w.add_assertion("cases_without_exactly_two_quadratic_steps",
                    computed="0", expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("occurrences", rows)
    w.add_caveat(
        "Measured over a = 2..7 and b in {a, a+1, a+3} only, and against the "
        "reduction the engine's deg-lex strategy happens to produce. A Lean "
        "proof may follow a different chain.")
    w.add_caveat(
        "The context formulas are MEASURED then asserted, not derived -- the "
        "same status as the split formulas in hecke-corner-le-regime, and the "
        "reason the check is written per (a, b) rather than inferred from one "
        "case. A first guess at these contexts, made before running this, was "
        "wrong at every one of the 36 occurrences.")
    w.add_caveat(
        "Only the CONTEXTS are fitted. The Lean step lemma (quadStep) takes "
        "the contexts as parameters and so does not depend on these formulas "
        "being right; they are needed only when assembling the chain.")
    path = w.save()

    print("  a   b  occ  quad@  prev    left            right")
    for r in rows:
        print(f" {r['a']:>2}  {r['b']:>2}   {r['occurrence']}   "
              f"{r['quad_index_rel_i']:>4}  {r['preceded_by']:<6}"
              f"{str(r['left_context_rel_i']):<16}{r['right_context_rel_i']}")
    print(f"\noccurrences: {len(rows)}   not matching shape: {mismatch}")
    print(f"witness -> {path}")
    return 0 if not mismatch else 1


if __name__ == "__main__":
    raise SystemExit(main())
