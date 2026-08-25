#!/usr/bin/env python3
"""hecke_prefix_phases — the corner prefix is two terms running the same script.

What remains of the `a ≤ b` regime is the prefix: the `a² + a + 5` steps before
the first cancellation. The step list alone is hard to read, because the element
is multi-term there and the engine interleaves the terms by deg-lex order — so
consecutive steps in the chain often belong to *different* terms.

Tagging each step with the **term lineage** it acts on makes it legible. At
`a = 5`:

    A: B₂₁ F₀₂ ......... B₁₀ B₂₁ F₀₂ B₃₂ F₁₃ F₀₃ B₄₃ Y₅₄ Q₅ ... small(a)
    B: ....... B₂₁ F₀₂ B₃₂ F₁₃ F₀₃ B₄₃ Y₅₄ Q₅ ... small(a) B₁₀ B₂₁

The two terms run the **same script**, offset — but not quite in the tidy way
that phrasing suggests, and the lengths say so: `|A| = |B| + 1`, not `|B| + 3`.
The exact relation is that `A`'s script is `[B₂₁, F₀₂, B₁₀]` followed by **all
of `B`'s except its trailing two steps** `[B₁₀⟨b⟩, B₂₁]`, for which `A` has no
counterpart. And that shared script is

    for d = 1 … a−3:   one Bokut–Shiao step, then d far-commutations
    one more Bokut–Shiao step, with no far-commutations
    Y_{j₁,j₁+1}  then  Q_{j₁}

which is exactly §4af's loop followed by the quadratic pair. So the prefix
introduces **no new kind of step** — every piece already has a lemma:

    loop passes          §4af  (loopTwo / loopTwoGen / blockStep)
    the B and Y steps    monicStep      (§4x, two-word monic rules)
    the Q steps          quadStep       (§4ah, the three-word rule)
    small(a)             blockPassFromTwo (§4aj, once the tail T was freed)
    the cancellation     ofTerms_cancel_pair (§4ak)

That last one is why `small(a)` matters here: it is the *same* block shape as
the top level with a different trailing word, and a lemma hardcoding `[σ_i]`
does not reach it.

## What this does and does not establish

It establishes that the prefix's step *inventory* is covered. It does **not**
establish that the assembly goes through: the pieces still have to compose on
the nose, across an interleaving of two lineages, and this arc's record on
"remaining work is just wiring" is poor — five structural descriptions have
failed under measurement so far, including one about this very assembly. Treat
"no new lemma kinds" as an inventory result, not a schedule.

Emits `hecke-prefix-phases.witness.json`. Bean qou-auq3.
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


def prefix_by_lineage(i, a, b):
    """Replay the prefix, returning each term lineage's own ordered script."""
    j1, j2 = i - a, i - b
    d1, e2 = eng.desc_word(i, j1), eng.desc_word(i - 1, j2)
    n1, n2 = f"B{i-1}{i}{j1}", f"B{i-1}{i}{j2}"
    f = dict(eng.clean(eng.combine(
        {w: eng.LC[n2] * c
         for w, c in eng.context_mul((), eng.REL[n1], e2 + (i,)).items()},
        {w: eng.LC[n1] * c
         for w, c in eng.context_mul(d1, eng.REL[n2], ()).items()}, -1)))
    lineage = {w: chr(65 + k) for k, w in enumerate(sorted(f, key=eng.deglex_key))}
    scripts, order = {}, []
    pre = a * a + a + 5
    for k in range(pre):
        target = None
        for w in sorted(f.keys(), key=eng.deglex_key):
            for name in eng.LM:
                if eng.infix_positions(w, eng.LM[name]):
                    target = (w, name, eng.infix_positions(w, eng.LM[name])[0]); break
            if target:
                break
        if target is None:
            break
        w, name, kk = target
        rule = RMAP[name]
        rel = (rule[0],) + tuple(i - x for x in rule[1:])
        tag = lineage.get(w, "?")
        scripts.setdefault(tag, []).append("".join(str(x) for x in rel))
        order.append(tag)
        left, right = w[:kk], w[kk + len(eng.LM[name]):]
        coeff = sp.expand(f[w] / eng.LC[name])
        before = set(f)
        f = eng.clean(eng.combine(f, eng.context_mul(left, eng.REL[name], right),
                                  -coeff))
        for nw in set(f) - before:
            lineage.setdefault(nw, tag)
    return scripts, order


def main():
    started = time.monotonic()
    rows, bad = [], 0
    for a in range(3, 7):
        for b in (a, a + 1, a + 2):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            retune(n)
            scripts, order = prefix_by_lineage(i, a, b)
            A, B = scripts.get("A", []), scripts.get("B", [])
            # 1. exactly two lineages act in the prefix
            two_lineages = set(scripts) == {"A", "B"}
            # 2. A's script is [B21, F02, B10] prepended to B's
            head_ok = (len(A) >= 3 and A[0].startswith("B21")
                       and A[1] == "F02" and A[2].startswith("B10"))
            # A after its 3-step head reproduces B EXACTLY UP TO B's last two
            # steps -- B ends with [B10<b>, B21] which A has no counterpart for.
            # (|A| = |B| + 1, so A is NOT the head prepended to all of B.)
            tail_len = 2
            shares = (head_ok and len(B) > tail_len
                      and A[3:] == B[:len(B) - tail_len]
                      and B[len(B) - tail_len].startswith("B10")
                      and B[len(B) - tail_len + 1].startswith("B21")
                      and len(A) == len(B) + 1)
            # 3. B's script begins with the loop + the quadratic pair
            qpos = [k for k, r in enumerate(B) if r.startswith("Q")]
            ypos = [k for k, r in enumerate(B) if r.startswith("Y")]
            pair_ok = (len(qpos) == 1 and len(ypos) == 1
                       and ypos[0] + 1 == qpos[0])
            # 4. before the pair: alternating B-step then d far-commutations,
            #    d = 1 … a-3, then one bare B
            head = B[:ypos[0]] if ypos else []
            groups, cur = [], None
            for r in head:
                if r.startswith("B"):
                    if cur is not None:
                        groups.append(cur)
                    cur = 0
                elif r.startswith("F") and cur is not None:
                    cur += 1
            if cur is not None:
                groups.append(cur)
            loop_ok = groups == list(range(1, a - 2)) + [0]
            ok = two_lineages and head_ok and shares and pair_ok and loop_ok
            bad += not ok
            rows.append({
                "a": a, "b": b, "prefix": a * a + a + 5,
                "lineages": sorted(scripts),
                "A_script": A, "B_script": B,
                "A_head_is_B21_F02_B10": head_ok,
                "A_tail_is_B_minus_its_last_two": shares,
                "len_A": len(A), "len_B": len(B),
                "B_has_one_YQ_pair_adjacent": pair_ok,
                "loop_group_far_counts": groups,
                "loop_groups_expected": list(range(1, a - 2)) + [0],
                "phases_hold": ok,
            })

    w = WitnessBuilder("hecke-prefix-phases", engine="sympy", start_time=started)
    w.set_description(
        "The Bokut-Shiao corner prefix, read by term lineage rather than by "
        "step order. Exactly two lineages act; they run the SAME script, "
        "offset -- A's is [B21, F02, B10] followed by all of B's except its "
        "trailing two steps [B10<b>, B21] (so len(A) = len(B) + 1). "
        "The shared script "
        "is 4af's loop (a Bokut-Shiao step then d far-commutations, "
        "d = 1..a-3, then one bare step) followed by the adjacent pair Y then "
        "Q. So the prefix introduces no new KIND of step: every piece already "
        "has a lemma (loopTwo, monicStep, quadStep, blockPassFromTwo, "
        "ofTerms_cancel_pair).")
    w.add_parameter("lineages_in_prefix", "exactly 2")
    w.add_parameter(
        "A_script",
        "[B21, F02, B10] ++ (B_script minus its trailing [B10<b>, B21]); "
        "equivalently len(A) = len(B) + 1, NOT len(B) + 3")
    w.add_parameter(
        "shared_script",
        "for d = 1..a-3: one Bokut-Shiao step then d far-commutations; "
        "then one bare Bokut-Shiao step; then Y_{j1,j1+1} Q_{j1} adjacent")
    w.add_assertion("prefixes_not_matching_the_two-lineage_phase_structure",
                    computed=str(bad), expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "Measured over a = 3..6 and b in {a, a+1, a+2} only, and against the "
        "reduction the engine's deg-lex strategy happens to produce. a = 2 is "
        "excluded: the loop is empty there and the head degenerates.")
    w.add_caveat(
        "This is an INVENTORY result, not a schedule. It says the prefix needs "
        "no new kind of lemma. It does NOT say the assembly composes -- the "
        "pieces must still meet on the nose across an interleaving of two "
        "lineages. Five structural descriptions in this arc have failed under "
        "measurement, one of them about this same assembly.")
    path = w.save()

    print("  a   b  pre  |A|  |B|  head  shares  YQ  loop-groups")
    for r in rows:
        print(f" {r['a']:>2}  {r['b']:>2} {r['prefix']:>4} "
              f"{len(r['A_script']):>4} {len(r['B_script']):>4}"
              f"  {str(r['A_head_is_B21_F02_B10']):<5}"
              f" {str(r['A_tail_is_B_minus_its_last_two']):<6}"
              f" {str(r['B_has_one_YQ_pair_adjacent']):<5}"
              f" {r['loop_group_far_counts']}"
              f"{'' if r['phases_hold'] else '   <-- FAILS'}")
    print(f"\ncases: {len(rows)}   not matching: {bad}")
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
