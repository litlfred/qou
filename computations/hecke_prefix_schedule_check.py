#!/usr/bin/env python3
"""hecke_prefix_schedule_check — the mid-prefix cancellation is forced, and why.

The tail taught this arc that a step *inventory* is not a schedule. This asks
the same question of the prefix — the remaining `a² + a + 5` steps — and of
`tailChain` (§4am) itself, which was written assuming a two-term source.

**Why a list and not a dict.** The confluence engine carries the element as a
map word → coefficient and *cleans* zero entries away. Lean carries it as
`AlgElement.ofTerms L` for an explicit list, and every lemma in the file reads
its redex off the shape `L₁ ++ (W, c) :: L₂` — needing `W` to occur **exactly
once** in `L`. The models agree until the prefix's mid-way cancellation, where
two terms reconverge on one word with opposite coefficients: the engine drops
both, the list keeps both. A dict-based probe cannot see the difference, and
the difference is the whole question.

## Measured

  * `dup_sources = 0` — no step ever rewrites a duplicated word. So the dead
    pair is inert *as a source*: on that count alone it could just be carried.
  * `entries_at_T_pre = 4` (2 live + the dead word twice), against the **2**
    that `tailChain` is stated on.
  * `dead_words_extending_a_block_context = 1` — and this is what decides it.
    `blockPass`'s `hpark` forbids any other term from extending the block's
    left context `A`, and one of the carried dead words does exactly that.

So carrying the dead pair into the tail breaks `tailChain`'s hypotheses even
though the dead entries are never rewritten. `ofTerms_cancel_pair` is
**forced** — not by any word being reduced twice, which was this arc's earlier
guess, but by `hpark` being a condition on *every* other entry, live or not.

## What discharges it

Nothing new. `Basic.lean` §6 already carries `SingleStepReduction.of_coeffEq_left`
and `MultiStepReduction.congr_source` (whose conclusion is a disjunction —
either the chain restarts at the coefficientwise-equal source, or that source
was already the endpoint; the second disjunct is what the syntactic `refl`
constructor costs, and `reducesToZero_congr` shows how to absorb it). So the
assembly is: prefix to the cancellation, `ofTerms_cancel_pair`, `congr_source`,
then the rest of the prefix and `tailChain` on a genuine two-entry list.

Emits `hecke-prefix-schedule-check.witness.json`. Bean qou-auq3.
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


def run(i, a, b):
    """Replay the whole chain, keeping BOTH models in step."""
    f = start_element(i, a, b)
    # the list model starts as the engine's cleaned element, one entry per word
    L = [[w, c] for w, c in sorted(f.items(), key=lambda kv: eng.deglex_key(kv[0]))]
    rows, dup, dead_word, dead_at, dead_later = [], [], None, None, False
    max_entries = len(L)
    pre = a * a + a + 5
    at_pre = None
    for k in range(6000):
        t = next_redex(f)
        if t is None:
            break
        w, name, kk = t
        # --- list model: locate the redex, require a unique occurrence
        hits = [idx for idx, e in enumerate(L) if e[0] == w]
        if len(hits) != 1:
            dup.append({"step": k, "word_occurrences": len(hits),
                        "rule": name})
            if dead_word is not None and w == dead_word:
                dead_later = True
        idx = hits[0] if hits else None
        left, right = w[:kk], w[kk + len(eng.LM[name]):]
        img = eng.context_mul(left, eng.REL[name], right)
        coeff = sp.expand(f[w] / eng.LC[name])
        if idx is not None:
            c_here = L[idx][1]
            new = [[u, sp.expand(-coeff * cu)] for u, cu in img.items() if u != w]
            # the redex entry itself is consumed (monic: coefficient cancels)
            L = L[:idx] + new + L[idx + 1:]
            _ = c_here
        max_entries = max(max_entries, len(L))
        f = eng.clean(eng.combine(f, img, -coeff))
        # --- detect the cancellation: a word now carried twice with opposite
        #     coefficients, i.e. present in the list but gone from the dict
        if dead_word is None:
            for u in {e[0] for e in L}:
                occ = [e for e in L if e[0] == u]
                if len(occ) > 1 and sp.simplify(sum(e[1] for e in occ)) == 0:
                    dead_word, dead_at = u, k
                    break
        rows.append(k)
        if len(rows) == pre:
            at_pre = [[list(e[0]), str(e[1])] for e in L]
    return {"steps": len(rows), "max_entries": max_entries,
            "entries_at_T_pre": at_pre, "final_entries": len(L),
            "dup_sources": dup, "dead_at": dead_at,
            "dead_word_later_source": dead_later,
            "dead_pair_span": (len(rows) - dead_at) if dead_at is not None else None}


def main():
    started = time.monotonic()
    rows, bad = [], 0
    for a in range(3, 6):
        for b in range(a + 1, a + 3):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            retune(n)
            r = run(i, a, b)
            pre = a * a + a + 5
            # Does tailChain's 2-entry source shape match what the prefix
            # leaves? And if not, do the extra entries satisfy the tail's
            # two hpark conditions -- i.e. do they extend A1 or A2?
            ent = r.pop("entries_at_T_pre") or []
            words = [tuple(e[0]) for e in ent]
            rel = lambda w: tuple(i - x for x in w)
            live = [w for w in words
                    if sum(sp.sympify(e[1]) for e in ent
                           if tuple(e[0]) == w) != 0]
            dead = [w for w in words if w not in live]
            def core_ctx(word):
                def dW(x, y):
                    return tuple(range(x, y + 1)) if x <= y else ()
                core = (dW(0, a - 3) + (a - 1, a - 2, a) + (a - 1,)
                        + dW(a + 1, b))
                rw = rel(word)
                for la in range(len(rw) + 1):
                    if rw[la:la + len(core)] == core:
                        return rw[:la]
                return None
            ctxs = [c for c in (core_ctx(w) for w in set(live)) if c]
            clash = [list(rel(d)) for d in set(dead)
                     for c in ctxs if rel(d)[:len(c)] == c]
            # in the list model the peak is one HIGHER than the dict's 4: the
            # cancelled pair is carried rather than dropped
            ok = not r["dead_word_later_source"]
            bad += not ok
            rows.append({"a": a, "b": b, "n": n, "i": i, "prefix": pre, **r,
                         "dead_entries_are_inert": ok,
                         "entries_at_T_pre": len(ent),
                         "live_at_T_pre": len(set(live)),
                         "dead_at_T_pre": len(set(dead)),
                         "tailChain_2_entry_shape_matches": len(ent) == 2,
                         "dead_words_extending_a_block_context": clash})

    w = WitnessBuilder("hecke-prefix-schedule-check", engine="sympy",
                       start_time=started)
    w.set_description(
        "The corner's a <= b chain simulated in the LIST model Lean actually "
        "uses (AlgElement.ofTerms L, every lemma reading its redex off "
        "L1 ++ (W, c) :: L2 and so needing W to occur exactly once), rather "
        "than the confluence engine's cleaned word -> coefficient map. The two "
        "agree until the prefix's mid-way cancellation, where two terms "
        "reconverge on one word with opposite coefficients: the engine drops "
        "both, the list keeps both. Measured: the dead pair is never rewritten "
        "(dup_sources = 0), so on that count it could be carried -- but it "
        "leaves 4 entries at T_pre against the 2 tailChain is stated on, and "
        "ONE of the dead words extends a live term's block context, which is "
        "exactly what blockPass's hpark forbids. So ofTerms_cancel_pair is "
        "FORCED, not by any word being reduced twice (this arc's earlier "
        "guess) but by hpark being a condition on every other entry, live or "
        "dead. Nothing new is needed to discharge it: Basic.lean §6 already "
        "has SingleStepReduction.of_coeffEq_left and "
        "MultiStepReduction.congr_source.")
    w.add_parameter("list_model",
                    "entries are never merged; a step replaces its redex entry "
                    "in place with the rule's images")
    w.add_assertion("chains_where_the_dead_pair_is_later_rewritten",
                    computed=str(bad), expected="0")
    carryable = sum(1 for r in rows
                    if r["tailChain_2_entry_shape_matches"]
                    or not r["dead_words_extending_a_block_context"])
    w.add_assertion(
        "chains_where_the_dead_pair_could_be_carried_into_the_tail",
        computed=str(carryable), expected="0")
    w.add_parameter(
        "tailChain_shape_gap",
        "tailChain is stated on a 2-entry list; carrying the dead pair leaves "
        "4, and one dead word extends a live term's block context -- so the "
        "cancellation must be discharged BEFORE the tail, not after")
    w.add_parameter(
        "discharged_by",
        "ofTerms_cancel_pair (this file) + MultiStepReduction.congr_source / "
        "SingleStepReduction.of_coeffEq_left (Basic.lean §6) -- all already "
        "present; no new bridging infrastructure")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "Follows the engine's deg-lex schedule. The tail showed that schedule "
        "can violate a lemma hypothesis where a reordering does not, so every "
        "count here is a statement about THIS order only -- including the "
        "clash that forces the cancellation. A different prefix schedule might "
        "not produce it; none has been searched for.")
    w.add_caveat(
        "The clash is measured against the block contexts of the LIVE terms at "
        "T_pre, i.e. against the contexts tailChain would use. It is not a "
        "sweep of every hypothesis of every lemma along the prefix -- the "
        "prefix assembly itself has not been attempted.")
    w.add_caveat(
        "a = 3..5, b in {a+1, a+2}. The diagonal is excluded, as in the tail "
        "measurements.")
    path = w.save()

    print("  a   b  steps  max  dup  dead@  T_pre entries (live+dead)  "
          "tail shape  clashes")
    for r in rows:
        print(f" {r['a']:>2}  {r['b']:>2} {r['steps']:>6} {r['max_entries']:>4}"
              f" {len(r['dup_sources']):>4}  {str(r['dead_at']):>5}"
              f"   {r['entries_at_T_pre']:>3} ({r['live_at_T_pre']}+"
              f"{r['dead_at_T_pre']})           "
              f"{str(r['tailChain_2_entry_shape_matches']):<10}"
              f"  {len(r['dead_words_extending_a_block_context'])}")
    print(f"\ncases: {len(rows)}   dead pair later rewritten: {bad}")
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
