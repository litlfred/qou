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

**Head separation is a proxy; the sharper criterion is also measured.** A left
context `A` is necessarily a *prefix* of the source, since every lemma here
reads its source as `A ++ redex ++ tail`. So `hpark` — no other term `r` equals
`A ++ z` — holds exactly when `lcp(source, r) < |A|` for every other `r`, and
`|A|` reaches at most the redex offset. A working context therefore exists iff
`redex_offset > max lcp`. Measured, that rescues `2(a−2)` of the head-clashing
steps and leaves a hard core of **`2a`** where no length works.

**Expected to fail somewhere.** The prefix's two lineages descend from one
overlap, so early on they share long prefixes by construction. The question is
how far in the sharing persists and how deep it goes, not whether it exists.

And since *scheduling* is what repaired the tail's collision, the same two
lineage-grouped orders are measured here as well. They do not repair the
prefix: both are legal and reach the same endpoint, but one clashes exactly as
often as the engine's order and the other is strictly worse. That is a
**scope-limited** negative — these two groupings, alone, do not help — and not
a claim that no schedule can; the space of legal orders is far larger than
three.

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


def plan(i, a, b):
    """The prefix's steps in engine order, each tagged with its root lineage."""
    f = start_element(i, a, b)
    lineage = {w: k for k, w in
               enumerate(sorted(f, key=eng.deglex_key))}
    pre, steps = a * a + a + 5, []
    for k in range(pre):
        t = next_redex(f)
        if t is None:
            break
        w, name, kk = t
        left, right = w[:kk], w[kk + len(eng.LM[name]):]
        img = eng.context_mul(left, eng.REL[name], right)
        steps.append({"src": w, "rule": name, "pos": kk,
                      "lineage": lineage[w]})
        coeff = sp.expand(f[w] / eng.LC[name])
        f = eng.clean(eng.combine(f, img, -coeff))
        for u in img:
            if u != w:
                lineage.setdefault(u, steps[-1]["lineage"])
    return steps, f


def sweep(i, a, b, schedule):
    """Head separation along a given schedule, in the list model."""
    f = start_element(i, a, b)
    L = [[w, c] for w, c in sorted(f.items(), key=lambda kv: eng.deglex_key(kv[0]))]
    out = []
    for s in schedule:
        w, name, kk = s["src"], s["rule"], s["pos"]
        if w not in f:
            return None          # schedule illegal: redex absent
        others = [e[0] for e in L if e[0] != w]
        heads_ok = all(o[:1] != w[:1] for o in others)
        deepest = max((lcp(w, o) for o in others), default=0)
        # `hpark` for a left context A (necessarily a prefix of the source,
        # since the lemmas read the source as A ++ redex ++ tail) says no other
        # term r satisfies r = A ++ z -- i.e. lcp(source, r) < |A| for every r.
        # The lemma's A reaches at most to the redex, so |A| <= kk, and the
        # condition is satisfiable at this step exactly when kk > deepest.
        # `hpark` is only SUFFICIENT. What a single step actually needs is
        # `monicStep`'s `hne`: the SOURCE word absent from the rest of the
        # list, so its coefficient can be read off `L1 ++ (W, c) :: L2`. A
        # bundled lemma needs that at each of its own intermediate sources --
        # which is what `farComm_transport_right_sources` already asks one
        # level down, excluding only the split naming the final word.
        out.append({"step": len(out), "rule": name, "others": len(others),
                    "heads_separate": heads_ok,
                    "longest_common_prefix": deepest,
                    "redex_offset": kk,
                    "context_fits": kk > deepest,
                    "source_unique": w not in others})
        hits = [idx for idx, e in enumerate(L) if e[0] == w]
        left, right = w[:kk], w[kk + len(eng.LM[name]):]
        img = eng.context_mul(left, eng.REL[name], right)
        coeff = sp.expand(f[w] / eng.LC[name])
        if len(hits) == 1:
            idx = hits[0]
            L = L[:idx] + [[u, sp.expand(-coeff * cu)]
                           for u, cu in img.items() if u != w] + L[idx + 1:]
        f = eng.clean(eng.combine(f, img, -coeff))
    return out, f


def main():
    started = time.monotonic()
    rows, bad = [], 0
    for a in range(3, 6):
        for b in (a, a + 1, a + 2):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            retune(n)
            steps, f_end = plan(i, a, b)
            st, _ = sweep(i, a, b, steps)
            # Does a lineage-grouped schedule repair the clashes, as it did in
            # the tail? Both groupings, each lineage keeping its own order.
            alts = {}
            for tag, sched in (
                ("lineage0_first", [s for s in steps if s["lineage"] == 0]
                                   + [s for s in steps if s["lineage"] == 1]),
                ("lineage1_first", [s for s in steps if s["lineage"] == 1]
                                   + [s for s in steps if s["lineage"] == 0])):
                got = sweep(i, a, b, sched)
                if got is None:
                    alts[tag] = {"legal": False}
                    continue
                so, fo = got
                alts[tag] = {
                    "legal": True,
                    "same_endpoint": (fo == f_end),
                    "clashing": sum(1 for x in so if not x["heads_separate"]),
                    "max_lcp": max((x["longest_common_prefix"] for x in so
                                    if not x["heads_separate"]), default=0),
                }
            clashes = [s for s in st if not s["heads_separate"]]
            # Are the clashes a contiguous SUFFIX? If so the prefix splits
            # into a collision-free opening phase and a closing phase where
            # the two lineages have converged enough to share prefixes.
            cidx = [s["step"] for s in clashes]
            contiguous_suffix = bool(cidx) and cidx == list(
                range(cidx[0], len(st)))
            # the sharper reading: of the head-clashing steps, how many still
            # admit a working left context because the redex sits past the
            # shared prefix?
            rescued = [s for s in clashes if s["context_fits"]]
            genuine = [s for s in clashes if not s["context_fits"]]
            # Do the hard-core steps satisfy the PRECISE condition even though
            # they fail hpark? If so the 2a figure measures a lemma-shape
            # problem, not a mathematical obstruction.
            hard_core_hne = all(x["source_unique"] for x in genuine)
            all_hne = all(x["source_unique"] for x in st)
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
                "reordered": alts,
                "clashing_but_context_fits": len(rescued),
                "context_does_not_fit": len(genuine),
                "context_fail_steps": [s["step"] for s in genuine],
                "context_fail_rules": sorted({s["rule"][0] for s in genuine}),
                "context_fail_offsets": [[s["redex_offset"],
                                          s["longest_common_prefix"]]
                                         for s in genuine],
                "hard_core_sources_all_unique": hard_core_hne,
                "every_step_source_unique": all_hne,
                "clashes_are_contiguous_suffix": contiguous_suffix,
                "first_clash_step": cidx[0] if cidx else None,
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
    w.add_parameter("head_clashing_steps", "4(a-1), independent of b")
    w.add_parameter(
        "steps_with_NO_satisfiable_left_context", "2a, independent of b")
    w.add_parameter(
        "but_the_precise_condition_holds_at_all_of_them",
        "hpark is SUFFICIENT, not necessary. What a step needs is that its "
        "SOURCE be absent from the rest of the list (monicStep's hne), and a "
        "bundled lemma needs that at each of its own intermediate sources -- "
        "which is exactly the relaxation farComm_transport_right_sources "
        "already carries, excluding only the split naming the final word. "
        "Measured: every source in the chain is unique, the 2a hard-core "
        "steps included. So the 2a figure measures a LEMMA-SHAPE problem "
        "(blockTransportRight / blockPassFromTwo / blockPass / loopTwoGen do "
        "not propagate the relaxation), not a mathematical obstruction.")
    w.add_parameter(
        "phase_split",
        "the clashes are a CONTIGUOUS SUFFIX beginning at step a^2-3a+9: the "
        "prefix opens with a^2-3a+9 steps that are entirely head-separated "
        "and therefore need no collision reasoning at all, and closes with "
        "4(a-1) steps where the two lineages have converged enough to share "
        "prefixes")
    w.add_parameter(
        "hpark_criterion",
        "a left context A is necessarily a PREFIX of the source (the lemmas "
        "read the source as A ++ redex ++ tail), so hpark -- no other term r "
        "is A ++ z -- holds exactly when lcp(source, r) < |A| for every r. "
        "|A| reaches at most the redex offset kk, so a working context exists "
        "iff kk > max_r lcp. This is the ACTUAL criterion; head separation is "
        "only a proxy for it, and overstates the difficulty by 2(a-2).")
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
    w.add_assertion(
        "hard_core_steps_whose_source_is_NOT_unique_in_the_list",
        computed=str(sum(0 if r["hard_core_sources_all_unique"] else 1
                         for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_some_step_source_is_not_unique",
        computed=str(sum(0 if r["every_step_source_unique"] else 1
                         for r in rows)),
        expected="0")
    w.add_assertion(
        "cases_where_the_clashes_are_not_a_contiguous_suffix",
        computed=str(sum(1 for r in rows
                         if not r["clashes_are_contiguous_suffix"])),
        expected="0")
    w.add_assertion(
        "cases_where_the_first_clash_is_not_at_step_a^2-3a+9",
        computed=str(sum(1 for r in rows
                         if r["first_clash_step"]
                         != r["a"] ** 2 - 3 * r["a"] + 9)),
        expected="0")
    w.add_assertion(
        "a_values_where_the_unsatisfiable_count_differs_from_2a",
        computed=str(sum(1 for r in rows
                         if r["context_does_not_fit"] != 2 * r["a"])),
        expected="0")
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
        "Head separation is SUFFICIENT, not necessary -- see the sharper "
        "kk > lcp criterion, which is what actually decides satisfiability.")
    w.add_caveat(
        "`context_fits` is OPTIMISTIC: it says a working left context EXISTS "
        "at the full redex offset. A given lemma may force a shorter A (e.g. "
        "blockPass's A stops where the block begins), in which case that step "
        "is harder than this column suggests. The 2a `context_does_not_fit` "
        "figure is the robust one -- there NO length works.")
    w.add_parameter(
        "reordering",
        "both lineage-grouped schedules are measured too, since scheduling is "
        "exactly what repaired the tail's clash; both are legal and reach the "
        "same endpoint, and NEITHER reduces the clash count")
    w.add_caveat(
        "Only three schedules are measured -- the engine's and the two "
        "lineage-groupings. The space of legal orders is far larger, so a "
        "clash surviving all three is not proved unavoidable.")
    path = w.save()

    print("  a   b  steps  head-clash  ctx-fits  ctx-FAILS  hne-ok  |  "
          "L0-first  L1-first")
    for r in rows:
        z = r["reordered"]
        f0, f1 = z["lineage0_first"], z["lineage1_first"]
        c0 = f0.get("clashing") if f0.get("legal") else "illegal"
        c1 = f1.get("clashing") if f1.get("legal") else "illegal"
        print(f" {r['a']:>2}  {r['b']:>2} {r['prefix_steps']:>6}"
              f" {r['steps_clashing']:>11} {r['clashing_but_context_fits']:>9}"
              f" {r['context_does_not_fit']:>10}"
              f"  {str(r['hard_core_sources_all_unique']):<6}  |"
              f" {str(c0):>9} {str(c1):>9}")
    print(f"\ncases: {len(rows)}   a-values whose counts depend on b: {bad}")
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
