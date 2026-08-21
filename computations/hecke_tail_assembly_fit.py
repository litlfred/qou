#!/usr/bin/env python3
"""hecke_tail_assembly_fit — does `blockPass` actually fit the measured chain?

`hecke_prefix_phases.py` established an **inventory** result: every kind of step
in the `a ≤ b` chain has a Lean lemma. It said explicitly that this is not a
schedule — the pieces still have to compose against the real chain, and this arc
has had five structural descriptions fail under measurement.

This is the first direct test of the inventory. It takes `blockPass`'s **actual
Lean statement** — source and target, written out in the same `descWord`
formulas the lemma uses — and asks whether they reproduce the chain's measured
block transition, for a free left context `A` and free tail `T`.

    source = A ++ descWord i jppp ++ [σ_jp, σ_jpp, σ_j₁] ++ [σ_jp]
                                  ++ descWord jm j₂ ++ T
    target = A ++ descWord jp j₂ ++ descWord i jppp ++ descWord jpp jp ++ T

In indices relative to `i` (so `σ_{i−x}` prints as `x`, and `descWord X Y`
becomes the ascending run `X_rel … Y_rel`), with `j₁ = a`, `jp = a−1`,
`jpp = a−2`, `jppp = a−3`, `jm = a+1`, `j₂ = b`.

The test is a fit, not a restatement: `A` and `T` are *solved for*, by searching
splits of the measured word, and both the source and the target must come out
right under the **same** `(A, T)`. A lemma whose source matched under one
context and whose target matched under another would not compose, and this
would catch that.

## What a pass means, and what it does not

A pass means `blockPass` is applicable at the block transition the engine
actually performs, with the contexts it actually has. That is genuinely more
than the inventory claimed.

It does **not** mean the tail assembles. The collision hypotheses
(`hpark`) are properties of the *other* term, not of this transition, and are
not tested here. Nor is the ordering: the Lean chain may take the steps in a
different order than the engine does.

Emits `hecke-tail-assembly-fit.witness.json`. Bean qou-auq3.
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


def stages(i, a, b):
    """The chain's element at the tail's stage boundaries, in rel coords."""
    j1, j2 = i - a, i - b
    d1, e2 = eng.desc_word(i, j1), eng.desc_word(i - 1, j2)
    n1, n2 = f"B{i-1}{i}{j1}", f"B{i-1}{i}{j2}"
    f = dict(eng.clean(eng.combine(
        {w: eng.LC[n2] * c
         for w, c in eng.context_mul((), eng.REL[n1], e2 + (i,)).items()},
        {w: eng.LC[n1] * c
         for w, c in eng.context_mul(d1, eng.REL[n2], ()).items()}, -1)))
    pre, blk = a * a + a + 5, a * b - a * a + 2 * a - 3
    marks = {pre: "T_pre", pre + blk: "T_b1", pre + blk + 2: "T_mid"}
    out = {}
    rel = lambda w: tuple(i - x for x in w)
    for k in range(pre + 2 * blk + 4):
        if k in marks:
            out[marks[k]] = {rel(w): sp.simplify(c) for w, c in f.items()}
        target = None
        for w in sorted(f.keys(), key=eng.deglex_key):
            for name in eng.LM:
                if eng.infix_positions(w, eng.LM[name]):
                    target = (w, name, eng.infix_positions(w, eng.LM[name])[0]); break
            if target:
                break
        if target is None:
            out["T_end"] = {rel(w): sp.simplify(c) for w, c in f.items()}
            break
        w, name, kk = target
        left, right = w[:kk], w[kk + len(eng.LM[name]):]
        coeff = sp.expand(f[w] / eng.LC[name])
        f = eng.clean(eng.combine(f, eng.context_mul(left, eng.REL[name], right),
                                  -coeff))
    return out


def fit_blockpass(before, after, a, b):
    """Solve for (A, T) making blockPass's source/target equal the measured pair.

    Both must hold under the SAME (A, T) -- that is the part worth testing.
    """
    def dW(x, y):
        return tuple(range(x, y + 1)) if x <= y else ()
    def src(A, T):
        return A + dW(0, a - 3) + (a - 1, a - 2, a) + (a - 1,) + dW(a + 1, b) + T
    def tgt(A, T):
        return A + dW(a - 1, b) + dW(0, a - 3) + (a - 2, a - 1) + T
    for la in range(len(before) + 1):
        A = before[:la]
        for lt in range(len(before) - la + 1):
            T = before[len(before) - lt:] if lt else ()
            if src(A, T) == before and tgt(A, T) == after:
                return A, T
    return None


def main():
    started = time.monotonic()
    rows, bad = [], 0
    for a in range(3, 7):
        for b in range(a + 1, a + 3):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            retune(n)
            st = stages(i, a, b)
            pre_t, b1_t = st["T_pre"], st["T_b1"]
            # the one word block1 changes, and what it becomes
            gone = [w for w in pre_t if w not in b1_t]
            new = [w for w in b1_t if w not in pre_t]
            fit = (fit_blockpass(gone[0], new[0], a, b)
                   if len(gone) == 1 and len(new) == 1 else None)
            # the chain ends on a cancelling pair: same word, opposite coeffs
            mid = st["T_mid"]
            ends_cancelling = (len(st.get("T_end", {"x": 1})) == 0
                               and len(mid) == 2
                               and sp.simplify(sum(mid.values())) != 0)
            ok = fit is not None
            bad += not ok
            rows.append({
                "a": a, "b": b,
                "block1_word_before": list(gone[0]) if gone else None,
                "block1_word_after": list(new[0]) if new else None,
                "solved_A_rel_i": list(fit[0]) if fit else None,
                "solved_T_rel_i": list(fit[1]) if fit else None,
                "blockPass_fits": ok,
                "chain_ends_at_zero": len(st.get("T_end", {"x": 1})) == 0,
            })

    w = WitnessBuilder("hecke-tail-assembly-fit", engine="sympy",
                       start_time=started)
    w.set_description(
        "First direct test of the a <= b inventory: does blockPass's ACTUAL "
        "Lean source and target -- written in the same descWord formulas the "
        "lemma uses -- reproduce the chain's measured block transition? The "
        "left context A and tail T are solved for by searching splits, and "
        "both source and target must come out right under the SAME (A, T). A "
        "lemma matching its source under one context and its target under "
        "another would not compose, and this catches that.")
    w.add_parameter(
        "blockPass_source",
        "A ++ descWord i jppp ++ [s_jp, s_jpp, s_j1] ++ [s_jp] "
        "++ descWord jm j2 ++ T")
    w.add_parameter(
        "blockPass_target",
        "A ++ descWord jp j2 ++ descWord i jppp ++ descWord jpp jp ++ T")
    w.add_assertion("block_transitions_blockPass_does_not_fit",
                    computed=str(bad), expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "A pass means blockPass is APPLICABLE at the transition the engine "
        "performs, with the contexts it actually has -- more than the "
        "inventory claimed. It does NOT mean the tail assembles: the hpark "
        "collision hypotheses are properties of the OTHER term and are not "
        "tested here, and the Lean chain may order its steps differently from "
        "the engine.")
    w.add_caveat(
        "Off-diagonal only (b > a). blockPass itself does not cover b = a -- "
        "that is what blockPassFromTwo is for -- so the diagonal needs its own "
        "fit check, not yet written.")
    path = w.save()

    print("  a   b   blockPass fits   solved A (rel)        solved T (rel)")
    for r in rows:
        print(f" {r['a']:>2}  {r['b']:>2}   {str(r['blockPass_fits']):<14}"
              f" {str(r['solved_A_rel_i']):<21} {r['solved_T_rel_i']}")
    print(f"\ncases: {len(rows)}   not fitting: {bad}")
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
