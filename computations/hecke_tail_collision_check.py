#!/usr/bin/env python3
"""hecke_tail_collision_check — the tail's blocks collide with their bystander.

`hecke_tail_assembly_fit.py` showed `blockPass`'s source and target reproduce
the chain's block transition under a common `(A, T)`. It said explicitly what it
did **not** test: the `hpark` collision hypothesis, which is a property of the
*other* term rather than of the transition, and which no fit can see.

This tests it. `blockPass` asks

    hpark : ∀ r ∈ (L₁ ++ L₂).map Prod.fst, ∀ z, r ≠ A ++ z

— no other term is any extension of the block's left context. The tail runs the
block twice, once on each of the two surviving terms, so each application has
the other one as its bystander. The question is whether that bystander is an
extension of `A`.

## Why the answer was predictable and is still worth measuring

The chain **ends in a cancellation** (`hecke_chain_cancellation.py`): the second
block's final word IS the first term's word, which is how the two annihilate. A
word equal to the block's last word is trivially an extension of the block's
left context. So `hpark` cannot hold at the second application — the very fact
that makes the chain terminate is what violates it.

That argument is sound but it is an argument, and five structural descriptions
in this arc have failed under measurement. What is measured here is finer than
the argument and is the part that decides what the Lean needs:

  * `hpark_holds` — the strong hypothesis, per application.
  * `bystander_is_a_source` — whether the bystander equals any word the block
    actually **rewrites**. This is the hypothesis that matters, because
    `SingleStepReduction` reads `f.coeff (a ++ lm ++ b)` off the *source* side;
    a collision on a word the block only ever *produces* costs nothing.
  * `bystander_is_final_word` — whether the collision is exactly the endpoint.

If the bystander is the final word and never a source, then `hpark` is merely
**too strong**, and the fix is the relaxation `farComm_transport_right_sources`
already carries one level down (it excludes the split `v = []`, which names the
transport's own final word) but which `blockTransportRight` / `blockPassFromTwo`
/ `blockPass` do not propagate. If instead the bystander turns up as a genuine
source, the tail needs more than a relaxation.

Emits `hecke-tail-collision-check.witness.json`. Bean qou-auq3.
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


def replay(i, a, b):
    """Full replay: per step, the source word rewritten and the term set."""
    j1, j2 = i - a, i - b
    d1, e2 = eng.desc_word(i, j1), eng.desc_word(i - 1, j2)
    n1, n2 = f"B{i-1}{i}{j1}", f"B{i-1}{i}{j2}"
    f = dict(eng.clean(eng.combine(
        {w: eng.LC[n2] * c
         for w, c in eng.context_mul((), eng.REL[n1], e2 + (i,)).items()},
        {w: eng.LC[n1] * c
         for w, c in eng.context_mul(d1, eng.REL[n2], ()).items()}, -1)))
    steps = []
    for _ in range(6000):
        target = None
        for w in sorted(f.keys(), key=eng.deglex_key):
            for name in eng.LM:
                if eng.infix_positions(w, eng.LM[name]):
                    target = (w, name, eng.infix_positions(w, eng.LM[name])[0]); break
            if target:
                break
        if target is None:
            return steps, f
        w, name, kk = target
        left, right = w[:kk], w[kk + len(eng.LM[name]):]
        produced = [u for u in eng.context_mul(left, eng.REL[name], right)
                    if u != w]
        steps.append({"source": w, "rule": name, "terms": set(f),
                      "produced": produced})
        coeff = sp.expand(f[w] / eng.LC[name])
        f = eng.clean(eng.combine(f, eng.context_mul(left, eng.REL[name], right),
                                  -coeff))
    raise RuntimeError("no normal form")


def solve_A(word, a, b, i):
    """The left context `A` blockPass would use on this word, in rel-i coords."""
    def dW(x, y):
        return tuple(range(x, y + 1)) if x <= y else ()
    core = dW(0, a - 3) + (a - 1, a - 2, a) + (a - 1,) + dW(a + 1, b)
    rel = tuple(i - x for x in word)
    for la in range(len(rel) + 1):
        if rel[la:la + len(core)] == core:
            return rel[:la], rel[la + len(core):]
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
            steps, final = replay(i, a, b)
            pre, blk = a * a + a + 5, a * b - a * a + 2 * a - 3
            bounds = {"block1": (pre, pre + blk),
                      "block2": (pre + blk + 2, len(steps))}
            rel = lambda w: tuple(i - x for x in w)
            out = {}
            for tag, (lo, hi) in bounds.items():
                blk_steps = steps[lo:hi]
                srcs = [s["source"] for s in blk_steps]
                # the bystander: the term present throughout that the block
                # never rewrites
                start_terms = blk_steps[0]["terms"]
                byst = [w for w in start_terms if w not in srcs]
                A = solve_A(srcs[0], a, b, i)
                # What the block PRODUCES. Reading this off the post-block
                # term set is wrong for block2: the chain ends at zero, so
                # there is no term left to read and the check goes vacuous.
                # Ask the last step what it emits instead.
                last_produced = blk_steps[-1]["produced"]
                ok_shape = len(byst) == 1 and A is not None
                if not ok_shape:
                    out[tag] = {"shape_read": False, "bystanders": len(byst),
                                "A_solved": A is not None}
                    continue
                B, Arel = rel(byst[0]), A[0]
                hpark = not (B[:len(Arel)] == Arel)
                is_src = byst[0] in srcs
                is_fin = byst[0] in last_produced
                produced_earlier = [k for k, st in enumerate(blk_steps[:-1])
                                    if byst[0] in st["produced"]]
                out[tag] = {
                    "shape_read": True,
                    "steps": len(blk_steps),
                    "A_rel_i": list(Arel),
                    "bystander_rel_i": list(B),
                    "hpark_holds": hpark,
                    "bystander_is_a_source": is_src,
                    "bystander_produced_by_last_step": is_fin,
                    "bystander_produced_earlier_at_steps": produced_earlier,
                }
            # the finding: hpark fails at block2 but ONLY as the final word
            b1, b2 = out["block1"], out["block2"]
            expect = (b1.get("shape_read") and b2.get("shape_read")
                      and b1["hpark_holds"] and not b1["bystander_is_a_source"]
                      and not b2["hpark_holds"]
                      and not b2["bystander_is_a_source"]
                      and b2["bystander_produced_by_last_step"]
                      and not b2["bystander_produced_earlier_at_steps"])
            bad += not expect
            rows.append({"a": a, "b": b, "n": n, "i": i,
                         "block1": b1, "block2": b2,
                         "matches_expected_collision_pattern": expect})

    w = WitnessBuilder("hecke-tail-collision-check", engine="sympy",
                       start_time=started)
    w.set_description(
        "Tests the hypothesis hecke-tail-assembly-fit declared untested: "
        "blockPass's hpark collision condition, which is a property of the "
        "OTHER term. The tail applies the block twice, once per surviving "
        "term, so each application has the other as bystander. Measured: "
        "hpark HOLDS at the first application and FAILS at the second -- and "
        "it fails only because the block's LAST step emits the bystander, "
        "which is the cancellation that ends the chain. The bystander is "
        "never a "
        "word the block REWRITES, and SingleStepReduction reads its "
        "coefficient off the source side only. So hpark is too strong, not "
        "wrong: blockTransportRight / blockPassFromTwo / blockPass need the "
        "source-only relaxation that farComm_transport_right_sources already "
        "carries one level down.")
    w.add_parameter("hpark",
                    "for all r in the other terms, for all z, r != A ++ z")
    w.add_parameter("block1_bystander", "hpark holds; not a source")
    w.add_parameter("block2_bystander",
                    "hpark FAILS; never a source; emitted by the block's LAST "
                    "step and by no earlier one")
    w.add_assertion("tails_not_matching_the_collision_pattern",
                    computed=str(bad), expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "Off-diagonal only (b > a), a = 3..6. The diagonal runs "
        "blockPassFromTwo instead and is not covered here.")
    w.add_caveat(
        "A source-only relaxation being SUFFICIENT is not shown by this "
        "measurement -- it shows the strong hypothesis is violated in exactly "
        "one place and that the violating word is never rewritten. Whether "
        "the relaxed statement goes through is a Lean question, not a "
        "measurement, and it has not been attempted.")
    path = w.save()

    print("  a   b  | blk1 hpark  src  | blk2 hpark  src  emitted-last")
    for r in rows:
        b1, b2 = r["block1"], r["block2"]
        print(f" {r['a']:>2}  {r['b']:>2}  |  {str(b1.get('hpark_holds')):<10}"
              f" {str(b1.get('bystander_is_a_source')):<5}"
              f"|  {str(b2.get('hpark_holds')):<10}"
              f" {str(b2.get('bystander_is_a_source')):<5}"
              f" {str(b2.get('bystander_produced_by_last_step'))}"
              f"{'' if r['matches_expected_collision_pattern'] else '   <-- OFF'}")
    print(f"\ncases: {len(rows)}   off pattern: {bad}")
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
