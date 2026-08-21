#!/usr/bin/env python3
"""hecke_prefix_head_separation — is the prefix separated at the first letter?

The tail's every context hypothesis was discharged by **one letter**: the
bystander began `σ_{i−2}` where the block's left context began `σ_{i−1}`, so
`r ≠ A ++ z` followed from `List.cons.inj` and nothing else. That is the
cheapest possible discharge, and it is lemma-independent: if no other term
shares the source's first letter, then *every* hypothesis of the form "no other
term extends this context" holds for free, whatever context the lemma picks.

`hecke_prefix_schedule_check.py` established the **necessary** condition across
the whole chain — `dup_sources = 0`, no step's redex word is ever duplicated in
the list. This measures the **sufficient** one, per step:

    at each prefix step, does every other list entry differ from the source
    in its FIRST LETTER?

Where it holds, the prefix needs no collision reasoning at all. Where it fails,
the step needs a real argument — a longer common prefix has to be compared, or
the lemma's context has to be chosen to avoid the clash, or the schedule has to
move (which is what the tail turned out to need).

Reported per step: the number of other entries, the longest common prefix with
any of them, and whether the heads separate. The longest-common-prefix column is
the one that says *how much* work a failing step needs — a clash at length 1 is
a different problem from a clash at length 9.

**Expected to fail somewhere.** The prefix's two lineages descend from one
overlap, so early on they share long prefixes by construction. The question is
how far in the sharing persists and how deep it goes, not whether it exists.

Emits `hecke-prefix-head-separation.witness.json`. Bean qou-auq3.
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


def retune(n):
    eng.N = n
    eng.RULES = eng.build_rules()
    eng.LM = {name: lm for name, _, lm in eng.RULES}
    eng.REL = {name: rel for name, rel, _ in eng.RULES}
    eng.LC = {name: eng.REL[name][eng.LM[name]] for name in eng.LM}


def start_element(i, a, b):
    j1, j2 = i - a, i - b
    d1, e2 = eng.desc_word(i, j1), eng.desc_word(i - 1, j2)
    n1, n2 = f"B{i-1}{i}{j1}", f"B{i-1}{i}{j2}"
    return dict(eng.clean(eng.combine(
        {w: eng.LC[n2] * c
         for w, c in eng.context_mul((), eng.REL[n1], e2 + (i,)).items()},
        {w: eng.LC[n1] * c
         for w, c in eng.context_mul(d1, eng.REL[n2], ()).items()}, -1)))


def next_redex(f):
    for w in sorted(f.keys(), key=eng.deglex_key):
        for name in eng.LM:
            pos = eng.infix_positions(w, eng.LM[name])
            if pos:
                return w, name, pos[0]
    return None


def lcp(u, v):
    k = 0
    while k < len(u) and k < len(v) and u[k] == v[k]:
        k += 1
    return k


def sweep(i, a, b):
    f = start_element(i, a, b)
    L = [[w, c] for w, c in sorted(f.items(), key=lambda kv: eng.deglex_key(kv[0]))]
    pre, steps = a * a + a + 5, []
    for k in range(pre):
        t = next_redex(f)
        if t is None:
            break
        w, name, kk = t
        others = [e[0] for e in L if e[0] != w]
        heads_ok = all(o[:1] != w[:1] for o in others)
        deepest = max((lcp(w, o) for o in others), default=0)
        steps.append({"step": k, "rule": name, "others": len(others),
                      "heads_separate": heads_ok, "longest_common_prefix": deepest})
        hits = [idx for idx, e in enumerate(L) if e[0] == w]
        left, right = w[:kk], w[kk + len(eng.LM[name]):]
        img = eng.context_mul(left, eng.REL[name], right)
        coeff = sp.expand(f[w] / eng.LC[name])
        if len(hits) == 1:
            idx = hits[0]
            L = L[:idx] + [[u, sp.expand(-coeff * cu)]
                           for u, cu in img.items() if u != w] + L[idx + 1:]
        f = eng.clean(eng.combine(f, img, -coeff))
    return steps


def main():
    started = time.monotonic()
    rows, bad = [], 0
    for a in range(3, 6):
        for b in (a, a + 1, a + 2):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            retune(n)
            st = sweep(i, a, b)
            clashes = [s for s in st if not s["heads_separate"]]
            first_ok = next((s["step"] for s in st if s["heads_separate"]), None)
            # the run of leading steps that are NOT head-separated
            lead = 0
            for s in st:
                if s["heads_separate"]:
                    break
                lead += 1
            rows.append({
                "a": a, "b": b, "prefix_steps": len(st),
                "steps_head_separated": len(st) - len(clashes),
                "steps_clashing": len(clashes),
                "leading_clash_run": lead,
                "first_separated_step": first_ok,
                "max_lcp_over_clashing": max(
                    (s["longest_common_prefix"] for s in clashes), default=0),
                "clash_steps": [s["step"] for s in clashes],
                "clash_rules": sorted({s["rule"][0] for s in clashes}),
            })

    w = WitnessBuilder("hecke-prefix-head-separation", engine="sympy",
                       start_time=started)
    w.set_description(
        "Every context hypothesis in the tail was discharged by ONE letter: no "
        "other term shared the source's first letter, so 'no other term "
        "extends this context' followed from List.cons.inj regardless of which "
        "context the lemma picked. This measures that sufficient condition "
        "step by step across the prefix, alongside the longest common prefix "
        "with any other entry -- which says how much work a failing step "
        "needs, a clash at length 1 being a different problem from one at "
        "length 9. The necessary condition (no duplicated redex word) was "
        "already measured clean chain-wide by hecke-prefix-schedule-check.")
    w.add_parameter("head_separation",
                    "no other list entry shares the source word's first letter")
    w.add_parameter("why_it_matters",
                    "where it holds, the step needs no collision reasoning at "
                    "all, for any lemma and any choice of left context")
    w.add_parameter("clashing_steps", "4(a-1), independent of b")
    w.add_parameter("head_separated_steps", "a^2 - 3a + 9")
    w.add_parameter("deepest_shared_prefix", "2a + 1, independent of b")
    # the measured regularity: the clash structure is a function of `a`
    # alone -- b (hence the block length) does not move any of the counts.
    by_a = {}
    for r in rows:
        by_a.setdefault(r["a"], []).append(
            (r["steps_clashing"], r["steps_head_separated"],
             r["max_lcp_over_clashing"]))
    bad = sum(1 for a, v in by_a.items() if len(set(v)) != 1)
    w.add_assertion("a_values_where_the_clash_counts_depend_on_b",
                    computed=str(bad), expected="0")
    w.add_assertion("a_values_where_clashes_differ_from_4(a-1)",
                    computed=str(sum(1 for r in rows
                                     if r["steps_clashing"] != 4 * (r["a"] - 1))),
                    expected="0")
    w.add_assertion("a_values_where_max_lcp_differs_from_2a+1",
                    computed=str(sum(1 for r in rows
                                     if r["max_lcp_over_clashing"]
                                     != 2 * r["a"] + 1)),
                    expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "Head separation is SUFFICIENT, not necessary. A clashing step is not "
        "a proved obstruction -- it is a step whose collision hypothesis needs "
        "a real argument rather than a one-letter one.")
    w.add_caveat(
        "Engine deg-lex order only. The tail showed a schedule can turn a "
        "clash into a non-clash; no reordering is searched for here.")
    path = w.save()

    print("  a   b  steps  separated  clashing  lead-run  max-lcp  rules")
    for r in rows:
        print(f" {r['a']:>2}  {r['b']:>2} {r['prefix_steps']:>6}"
              f" {r['steps_head_separated']:>10} {r['steps_clashing']:>9}"
              f" {r['leading_clash_run']:>9} {r['max_lcp_over_clashing']:>8}"
              f"  {','.join(r['clash_rules'])}")
    print(f"\ncases: {len(rows)}   a-values whose counts depend on b: {bad}")
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
