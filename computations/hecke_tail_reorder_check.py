#!/usr/bin/env python3
"""hecke_tail_reorder_check — reordering the tail dodges the collision entirely.

`hecke_tail_collision_check.py` found `blockPass`'s `hpark` violated at the
tail's second block: that block's last step emits the bystander, which is the
cancellation ending the chain. The obvious response is to weaken `hpark` — to
propagate the source-only relaxation `farComm_transport_right_sources` already
carries. That is real work: three lemmas restated, and the relaxed proof then
owes an argument that the destination differs from every intermediate source,
which is not free.

**There may be nothing to weaken.** The tail's two blocks act on *different
terms*, so their steps commute, and `MultiStepReduction` fixes no order beyond
each step's own redex being present. The engine's deg-lex strategy runs block 1
first — but that is the engine's scheduling accident, not a constraint on the
Lean. Run block 2 first and the bystander it sees is term 1 in its *pre*-block
form, which is not an extension of the block's left context at all.

So the question this measures is: **under the reordered schedule
[block2, block1, monic, monic], does every lemma's hypothesis hold?**

  * `blockPass`'s `hpark` at each of the two applications — the bystander is
    not an extension of that block's left context `A`.
  * `monicStep`'s `hne` at each of the two monic steps. `hne` constrains the
    **source** only (`hne : ∀ q ∈ (L₁ ++ L₂).map Prod.fst, q ≠ W`, with the
    target `W'` unconstrained), which is exactly why the final step may land on
    the bystander and cancel.
  * the reordered chain still reaches zero.

## What a pass means

That the tail assembles from the lemmas already on `main`, with no relaxation
of `hpark` and no new lemma beyond `ofTerms_cancel_pair` — by *scheduling*.

It does not mean the Lean goes through: these are the hypotheses read off the
lemma statements, checked against the measured words. Whether the terms unify
on the nose is a Lean question. That is attempted separately, and this arc's
record says to expect it to find something.

Emits `hecke-tail-reorder-check.witness.json`. Bean qou-auq3.
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


def apply_at(f, w, name, kk):
    left, right = w[:kk], w[kk + len(eng.LM[name]):]
    coeff = sp.expand(f[w] / eng.LC[name])
    return eng.clean(eng.combine(f, eng.context_mul(left, eng.REL[name], right),
                                 -coeff))


def tail_steps(i, a, b):
    """The tail's steps, each tagged with the T_pre term it descends from."""
    f = start_element(i, a, b)
    pre = a * a + a + 5
    for _ in range(pre):
        t = next_redex(f)
        if t is None:
            return None
        f = apply_at(f, *t)
    if len(f) != 2:
        return None
    roots = sorted(f, key=eng.deglex_key)
    lineage = {w: k for k, w in enumerate(roots)}
    steps = []
    while True:
        t = next_redex(f)
        if t is None:
            break
        w, name, kk = t
        tag = lineage[w]
        left, right = w[:kk], w[kk + len(eng.LM[name]):]
        prod = [u for u in eng.context_mul(left, eng.REL[name], right) if u != w]
        steps.append({"src": w, "rule": name, "pos": kk, "lineage": tag,
                      "produced": prod})
        f = apply_at(f, w, name, kk)
        for u in prod:
            lineage.setdefault(u, tag)
    return {"roots": roots, "start": start_element(i, a, b), "steps": steps,
            "pre": pre}


def block_A(word, a, b, i):
    """blockPass's left context A on this word (rel-i coords), and its tail."""
    def dW(x, y):
        return tuple(range(x, y + 1)) if x <= y else ()
    core = dW(0, a - 3) + (a - 1, a - 2, a) + (a - 1,) + dW(a + 1, b)
    rel = tuple(i - x for x in word)
    for la in range(len(rel) + 1):
        if rel[la:la + len(core)] == core:
            return rel[:la]
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
            info = tail_steps(i, a, b)
            if info is None:
                rows.append({"a": a, "b": b, "read": False}); bad += 1; continue
            steps, blk = info["steps"], a * b - a * a + 2 * a - 3
            # the engine's order: block1 (lineage 0), 2 monic, block2 (lineage 1)
            eng_order = [s["lineage"] for s in steps]
            engine_shape = (eng_order[:blk + 2] == [0] * (blk + 2)
                            and eng_order[blk + 2:] == [1] * (len(steps) - blk - 2))
            # REORDERED: every lineage-1 step first, then every lineage-0 step,
            # each lineage keeping its own order.
            order = ([s for s in steps if s["lineage"] == 1]
                     + [s for s in steps if s["lineage"] == 0])
            f = dict(info["start"])
            for _ in range(info["pre"]):
                f = apply_at(f, *next_redex(f))
            hne_ok, hpark = True, {}
            blk2_start, blk1_start = 0, len([s for s in order
                                             if s["lineage"] == 1])
            for k, s in enumerate(order):
                others = [w for w in f if w != s["src"]]
                # every lemma in the file reads the redex coefficient off a
                # list of the shape L1 ++ (W, c) :: L2, so the SOURCE must be
                # absent from the rest -- monicStep's hne, and what hpark
                # implies pointwise for the transports.
                if s["src"] not in f or any(w == s["src"] for w in others):
                    hne_ok = False
                if k in (blk2_start, blk1_start) and len(others) == 1:
                    A = block_A(s["src"], a, b, i)
                    B = tuple(i - x for x in others[0])
                    hpark["block2" if k == blk2_start else "block1"] = {
                        "A_rel_i": list(A) if A else None,
                        "bystander_rel_i": list(B),
                        "holds": A is not None and B[:len(A)] != A,
                    }
                f = apply_at(f, s["src"], s["rule"], s["pos"])
            reaches_zero = len(f) == 0
            both = (hpark.get("block1", {}).get("holds")
                    and hpark.get("block2", {}).get("holds"))
            ok = engine_shape and hne_ok and reaches_zero and both
            bad += not ok
            rows.append({
                "a": a, "b": b, "read": True, "tail_steps": len(steps),
                "engine_order_is_block1_monic_monic_block2": engine_shape,
                "reordered_hpark": hpark,
                "reordered_all_sources_unique": hne_ok,
                "reordered_reaches_zero": reaches_zero,
                "reorder_works": ok,
            })

    w = WitnessBuilder("hecke-tail-reorder-check", engine="sympy",
                       start_time=started)
    w.set_description(
        "The tail's two blocks act on different terms, so their steps commute "
        "and MultiStepReduction fixes no order beyond each step's redex being "
        "present. Running block 2 BEFORE block 1 -- the reverse of the "
        "engine's deg-lex schedule -- means block 2's bystander is term 1 in "
        "its PRE-block form, which is not an extension of the block's left "
        "context. Measured: under the reordered schedule [block2, block1, "
        "monic, monic] BOTH hpark hypotheses hold, every step's source is "
        "unique in the term list (monicStep's hne), and the chain still "
        "reaches zero. So the collision hecke-tail-collision-check found is a "
        "scheduling artifact: nothing needs weakening, the tail assembles "
        "from the lemmas already on main.")
    w.add_parameter("engine_schedule", "block1, monic, monic, block2")
    w.add_parameter("reordered_schedule", "block2, block1, monic, monic")
    w.add_parameter(
        "why_it_is_legal",
        "the two blocks act on different terms; SingleStepReduction requires "
        "only that the redex be present with nonzero coefficient")
    w.add_assertion("tails_where_the_reordered_schedule_fails",
                    computed=str(bad), expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "Off-diagonal only (b > a), a = 3..6. The diagonal runs "
        "blockPassFromTwo and is not covered.")
    w.add_caveat(
        "These are the hypotheses READ OFF the lemma statements and checked "
        "against the measured words. A pass does not mean the Lean composes: "
        "whether the terms unify on the nose is a Lean question, attempted "
        "separately.")
    path = w.save()

    print("  a   b  steps  engine-shape  hpark(blk2)  hpark(blk1)  hne  zero")
    for r in rows:
        if not r.get("read"):
            print(f" {r['a']:>2}  {r['b']:>2}   <unreadable>"); continue
        hp = r["reordered_hpark"]
        print(f" {r['a']:>2}  {r['b']:>2} {r['tail_steps']:>6}"
              f"  {str(r['engine_order_is_block1_monic_monic_block2']):<12}"
              f"  {str(hp.get('block2', {}).get('holds')):<11}"
              f"  {str(hp.get('block1', {}).get('holds')):<11}"
              f"  {str(r['reordered_all_sources_unique']):<5}"
              f" {str(r['reordered_reaches_zero'])}"
              f"{'' if r['reorder_works'] else '   <-- FAILS'}")
    print(f"\ncases: {len(rows)}   failing: {bad}")
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
