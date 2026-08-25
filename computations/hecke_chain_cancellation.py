#!/usr/bin/env python3
"""hecke_chain_cancellation — where the corner's `a ≤ b` chain loses terms.

Every *kind* of step in the `a ≤ b` chain now has a Lean lemma — loop passes
(§4af), the quadratic pairs (`quadStep` + `monicStep`), and the blocks
(`blockPass`, §4aj). The arc's notes therefore describe what is left as
"assembly: `MultiStepReduction.trans` over a longer list".

**That description is incomplete, and this measures the missing piece.** The
chain is not a sequence of rewrites on a fixed-shape term list. The quadratic
rule turns one term into two, so the element grows — and then, at two specific
steps, it *shrinks by two at once*, which no single rewrite can do. A
far-commutation rewrites one term into one term; a drop of two means the
rewritten word landed on a word already present, with the opposite coefficient,
and the pair **annihilated**.

Worked at `a = 4, b = 6`, immediately before and after step 24:

    before   h · (2,1,2,3,0,4,1,2,3,4,5,6)      <- rewritten by F(0,4)
            −h · (2,1,2,3,4,0,1,2,3,4,5,6)      <- already present
            −1 · (1,2,0,1,3,2,4,3,5,6,0)
             1 · (2,1,2,0,1,3,2,4,3,5,6)

    after   −1 · (1,2,0,1,3,2,4,3,5,6,0)
             1 · (2,1,2,0,1,3,2,4,3,5,6)

`F(0,4)` carries `σ_i σ_{i−4} → σ_{i−4} σ_i`, which takes the first word to the
second **exactly**; the coefficients are `h` and `−h`, so they cancel. The two
`h`-weighted terms are the ones the two quadratic applications created, and this
is where they reconverge.

**And the chain ENDS the same way.** Measured over all 20 pairs, there are
exactly **two** such events, both `−2`: this mid-prefix one, and the very last
step of the chain, which takes the surviving two terms to **zero**. So the
chain does not terminate by some separate mechanism — reaching zero *is* a
second pair-annihilation. An earlier version of this script asserted one
cancellation event and failed all 20 cases for that reason; the final collapse
is a cancellation too, and counting it is the whole correction.

## What this costs the Lean

`MultiStepReduction`'s obligations are stated through `AlgElement.CoeffEq`,
which compares *coefficients*, not term-list shapes — so the cancellation is
sound automatically. What the assembly needs is a **bridging lemma**: an
`ofTerms` list carrying `(w, c)` and `(w, −c)` is `CoeffEq` to the same list
with both dropped. Without it, every lemma downstream of the cancellation would
have to be stated against a four-term list whose first two are dead weight.

So "the assembly is wiring" understates it by one lemma — and that lemma is
used **twice**, the second use being what delivers "reduces to zero". It is
still bounded: two events per chain, at two identifiable steps.

Emits `hecke-chain-cancellation.witness.json`. Bean qou-auq3.
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


def profile(i, a, b):
    """Replay the chain, recording the term count and every drop event."""
    j1, j2 = i - a, i - b
    d1, e2 = eng.desc_word(i, j1), eng.desc_word(i - 1, j2)
    n1, n2 = f"B{i-1}{i}{j1}", f"B{i-1}{i}{j2}"
    f = dict(eng.clean(eng.combine(
        {w: eng.LC[n2] * c
         for w, c in eng.context_mul((), eng.REL[n1], e2 + (i,)).items()},
        {w: eng.LC[n1] * c
         for w, c in eng.context_mul(d1, eng.REL[n2], ()).items()}, -1)))
    counts, drops, grows = [], [], []
    for k in range(4000):
        before = len(f)
        counts.append(before)
        target = None
        for w in sorted(f.keys(), key=eng.deglex_key):
            for name in eng.LM:
                if eng.infix_positions(w, eng.LM[name]):
                    target = (w, name, eng.infix_positions(w, eng.LM[name])[0]); break
            if target:
                break
        if target is None:
            return counts, drops, grows, k
        w, name, kk = target
        rule = RMAP[name]
        left, right = w[:kk], w[kk + len(eng.LM[name]):]
        coeff = sp.expand(f[w] / eng.LC[name])
        f = eng.clean(eng.combine(f, eng.context_mul(left, eng.REL[name], right),
                                  -coeff))
        after = len(f)
        rel = (rule[0],) + tuple(i - x for x in rule[1:])
        if after < before:
            drops.append({"step": k, "rule": "".join(str(x) for x in rel),
                          "terms_before": before, "terms_after": after,
                          "delta": after - before})
        elif after > before:
            grows.append({"step": k, "rule": "".join(str(x) for x in rel),
                          "terms_before": before, "terms_after": after,
                          "delta": after - before})
    raise RuntimeError("no normal form")


def main():
    started = time.monotonic()
    rows, bad = [], 0
    for a in range(2, 7):
        for b in range(a, a + 4):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            retune(n)
            counts, drops, grows, total = profile(i, a, b)
            pre = a * a + a + 5

            # Measured shape: two growth events (the quadratic steps, +1 each)
            # and TWO cancellation events, both -2 -- the mid-prefix one, and
            # the FINAL step, which is how the chain reaches zero.
            two_grows = (len(grows) == 2 and all(g["delta"] == 1 for g in grows)
                         and all(g["rule"].startswith("Q") for g in grows))
            two_drops = len(drops) == 2 and all(d["delta"] == -2 for d in drops)
            drop_in_prefix = two_drops and drops[0]["step"] < pre
            ends_at_zero = (two_drops and drops[1]["step"] == total - 1
                            and drops[1]["terms_after"] == 0)
            peak = max(counts)
            ok = two_grows and two_drops and drop_in_prefix and ends_at_zero \
                and peak == 4
            bad += not ok
            rows.append({
                "a": a, "b": b, "n": n, "i": i, "steps": total,
                "prefix": pre, "peak_terms": peak,
                "growth_events": grows, "cancellation_events": drops,
                "cancellation_step": drops[0]["step"] if drops else None,
                "cancellation_rule": drops[0]["rule"] if drops else None,
                "final_collapse_step": drops[1]["step"] if len(drops) > 1 else None,
                "shape_holds": ok,
            })

    w = WitnessBuilder("hecke-chain-cancellation", engine="sympy",
                       start_time=started)
    w.set_description(
        "Term-count profile of the Bokut-Shiao corner's a <= b chain. The two "
        "quadratic steps each add one term (peak 4); exactly TWO later steps "
        "remove two at once, which no rewrite can do -- each is a pair of "
        "terms reconverging on one word with opposite coefficients and "
        "annihilating. The first is mid-prefix; the second IS the final step, "
        "so reaching zero is itself a cancellation rather than a separate "
        "terminating mechanism. The assembly needs a CoeffEq bridging lemma "
        "for this, used twice -- not just MultiStepReduction.trans.")
    w.add_parameter("peak_terms", "4")
    w.add_parameter("growth_events", "2, one per quadratic step, +1 each")
    w.add_parameter(
        "cancellation_events",
        "exactly 2, both delta -2: one inside the prefix, one AS THE FINAL "
        "STEP -- the chain reaches zero by the same pair-annihilation it uses "
        "mid-way, not by a distinct terminating mechanism")
    w.add_parameter(
        "lean_consequence",
        "needs a CoeffEq bridging lemma: ofTerms carrying (w, c) and (w, -c) "
        "equals ofTerms with both dropped. MultiStepReduction is stated on "
        "CoeffEq, so the cancellation is SOUND automatically; what is missing "
        "is the shape bridge.")
    w.add_assertion("chains_not_matching_the_term_count_shape",
                    computed=str(bad), expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "Measured over a = 2..6 and b = a..a+3 only, and against the reduction "
        "the engine's deg-lex strategy happens to produce. A Lean proof may "
        "follow a different chain, and a different chain could cancel at a "
        "different step or not at all.")
    w.add_caveat(
        "This does NOT say the cancellation is the only obstacle to the "
        "assembly. It says the arc's description of what remains -- "
        "'MultiStepReduction.trans over a longer list' -- omits it. Other "
        "omissions may remain; the assembly has not been attempted.")
    path = w.save()

    print("  a   b  steps  peak  grows  cancel@  rule")
    for r in rows:
        print(f" {r['a']:>2}  {r['b']:>2}  {r['steps']:>5} {r['peak_terms']:>5}"
              f"  {len(r['growth_events']):>5}  {str(r['cancellation_step']):>7}"
              f"  {r['cancellation_rule']}"
              f"{'' if r['shape_holds'] else '   <-- FAILS'}")
    print(f"\ncases: {len(rows)}   not matching: {bad}")
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
