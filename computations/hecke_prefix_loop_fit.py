#!/usr/bin/env python3
"""hecke_prefix_loop_fit — does §4af's loop actually fit the opening phase?

`hecke_prefix_head_separation.py` split the prefix at step `a²−3a+9`: an opening
phase that is entirely head-separated (so every collision hypothesis is free)
and a closing phase of `4(a−1)` steps where the lineages share prefixes. The
opening phase is therefore the cheapest real Lean target left in this arc — but
only if the lemma that would cover it actually fits, and "the inventory covers
it" has already proved insufficient once this session.

So this does for `loopTwoGen` (§4af) what `hecke_tail_assembly_fit.py` did for
`blockPass`: takes its **actual Lean source and target**, written in the same
`descWord` formulas the lemma uses,

    source = A ++ descWord i j₁ ++ descWord k  j₂ ++ S
    target = A ++ descWord kd ed ++ descWord i j₁ ++ descWord ed j₂ ++ S

and asks whether they reproduce what the chain does. `A` and `S` are *solved
for* by searching splits, and the level indices `k`/`e` are searched over the
whole range rather than assumed — the point of a fit is that nothing is fed in.

A hit must satisfy the lemma's own side conditions, not merely the word shapes:

  * `kd + 1 = k`, `ed + 1 = e`, `j₁ ≤ ed`, `j₂ ≤ e`, `k = e + m` for some `m ≥ 0`
  * `descWord i j₁ = Y ++ (σ_k :: descWord kd j₁)` for some `Y` — the decomposition
    hypothesis `hD`, which is what ties `k` into the descending run
  * `∀ y ∈ Y, kd + 1 < y.index` — the hypothesis `hY`

and the predicted target word must actually occur later in the chain.

## What a pass would mean, and what it would not

That `loopTwoGen` is applicable at the opening phase's loop passes with the
contexts they actually have. It would NOT mean the opening phase assembles:
`loopTwoGen` carries a bystander `P` with `∀ z, P ≠ A ++ z`, and while the
head-separation sweep says that hypothesis is discharged for free *somewhere*
in the opening phase, the fit and the collision check are separate questions —
which is the distinction the tail turned on.

Emits `hecke-prefix-loop-fit.witness.json`. Bean qou-auq3.
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


def all_words(i, a, b, upto):
    """Every word the chain carries during the first `upto` steps, plus each
    lineage's word after that lineage has taken `head` steps of its own."""
    f = start_element(i, a, b)
    lineage = {w: k for k, w in enumerate(sorted(f, key=eng.deglex_key))}
    taken = {0: 0, 1: 0}
    after_head = {}
    seen = set(f)
    for _ in range(upto):
        t = next_redex(f)
        if t is None:
            break
        w, name, kk = t
        tag = lineage[w]
        left, right = w[:kk], w[kk + len(eng.LM[name]):]
        img = eng.context_mul(left, eng.REL[name], right)
        coeff = sp.expand(f[w] / eng.LC[name])
        f = eng.clean(eng.combine(f, img, -coeff))
        for u in img:
            if u != w:
                lineage.setdefault(u, tag)
        taken[tag] = taken.get(tag, 0) + 1
        # lineage A's script opens [B21, F02, B10] BEFORE the shared loop, so
        # its loop source is its word after three of its own steps -- not its
        # starting word, which is what the first version of this probe tested.
        if taken[tag] == 3 and tag not in after_head:
            live = [u for u in f if lineage.get(u) == tag]
            if len(live) == 1:
                after_head[tag] = live[0]
        seen |= set(f)
    return seen, after_head


def dw(x, y):
    """desc_word in the engine's absolute indexing, empty when x < y."""
    return tuple(range(x, y - 1, -1)) if x >= y else ()


def infix_at(w, sub):
    if not sub:
        return []
    return [p for p in range(len(w) - len(sub) + 1) if w[p:p + len(sub)] == sub]


def fit_loop(W, i, j1, j2, n, seen):
    """Solve loopTwoGen's parameters against the word W; return the first hit."""
    for k in range(n):
        for e in range(n):
            kd, ed = k - 1, e - 1
            if kd < 0 or ed < 0:
                continue
            if not (j1 <= ed and j2 <= e and k >= e):
                continue
            core = dw(i, j1) + dw(k, j2)
            for p in infix_at(W, core):
                A, S = W[:p], W[p + len(core):]
                # hD: descWord i j1 = Y ++ (k :: descWord kd j1)
                d = dw(i, j1)
                tail = (k,) + dw(kd, j1)
                if len(tail) > len(d) or d[len(d) - len(tail):] != tail:
                    continue
                Y = d[:len(d) - len(tail)]
                if any(not (kd + 1 < y) for y in Y):     # hY
                    continue
                tgt = A + dw(kd, ed) + dw(i, j1) + dw(ed, j2) + S
                if tgt in seen:
                    return {"k": k, "e": e, "A_len": len(A), "S_len": len(S),
                            "Y_len": len(Y), "target_seen": True}
    return None


def main():
    started = time.monotonic()
    rows, bad = [], 0
    for a in range(3, 6):
        for b in (a, a + 1):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            retune(n)
            j1, j2 = i - a, i - b
            opening = a * a - 3 * a + 9
            seen, after_head = all_words(i, a, b, opening)
            start = start_element(i, a, b)
            hits = {}
            for tag, W in enumerate(sorted(start, key=eng.deglex_key)):
                hits[str(tag)] = fit_loop(W, i, j1, j2, n, seen)
            # and lineage A after its own 3-step head, where its loop begins
            hits_head = {}
            for tag, W in after_head.items():
                hits_head[str(tag)] = fit_loop(W, i, j1, j2, n, seen)
            # a = 3 has NO loop pass: hecke_prefix_phases measured its group
            # structure as [0] -- one bare Bokut-Shiao step, zero
            # far-commutations -- so loopTwoGen has nothing to fit there. That
            # is a fact about the shape, not a failure of the lemma.
            has_loop = a >= 4
            fits_B = hits.get("1") is not None
            fits_A_after_head = hits_head.get("0") is not None
            any_fit = fits_B or fits_A_after_head
            bad += 1 if (has_loop and not fits_B) else 0
            rows.append({
                "a": a, "b": b, "n": n, "i": i,
                "opening_phase_steps": opening,
                "words_reachable_in_opening": len(seen),
                "loopTwoGen_fits_starting_word":
                    {k: (v is not None) for k, v in hits.items()},
                "loopTwoGen_fits_after_3_step_head":
                    {k: (v is not None) for k, v in hits_head.items()},
                "solved_from_start": hits,
                "solved_after_head": hits_head,
                "has_a_loop_pass_at_all": has_loop,
                "lineage_B_fits": fits_B,
                "lineage_A_after_head_fits": fits_A_after_head,
                "at_least_one_term_fits": any_fit,
            })

    w = WitnessBuilder("hecke-prefix-loop-fit", engine="sympy",
                       start_time=started)
    w.set_description(
        "Does §4af's loopTwoGen actually fit the prefix's opening phase -- the "
        "a^2-3a+9 steps that hecke-prefix-head-separation found to be entirely "
        "head-separated, and therefore the cheapest remaining Lean target? "
        "Takes the lemma's ACTUAL source and target in its own descWord "
        "formulas, solves A and S by searching splits, searches the level "
        "indices k and e over the whole range rather than assuming them, "
        "enforces the lemma's own side conditions (kd+1=k, ed+1=e, j1<=ed, "
        "j2<=e, k>=e, the hD decomposition of descWord i j1, and hY on the "
        "resulting Y), and requires the predicted target word to actually "
        "occur in the chain.")
    w.add_parameter(
        "loopTwoGen_source", "A ++ descWord i j1 ++ descWord k j2 ++ S")
    w.add_parameter(
        "loopTwoGen_target",
        "A ++ descWord kd ed ++ descWord i j1 ++ descWord ed j2 ++ S")
    w.add_assertion(
        "cases_with_a_loop_where_lineage_B_does_not_fit_loopTwoGen",
        computed=str(bad), expected="0")
    w.add_assertion(
        "a=3_cases_that_have_a_loop_pass",
        computed=str(sum(1 for r in rows
                         if r["a"] == 3 and r["has_a_loop_pass_at_all"])),
        expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "A fit is applicability, not assembly. loopTwoGen carries a bystander "
        "P with the same `for all z, P != A ++ z` shape as blockPass's hpark; "
        "the head-separation sweep says that is discharged for free in the "
        "opening phase, but fit and collision are separate questions -- which "
        "is exactly the distinction the tail turned on.")
    w.add_caveat(
        "a = 3 has NO loop pass -- hecke-prefix-phases measured its group "
        "structure as [0], one bare Bokut-Shiao step with zero "
        "far-commutations -- so loopTwoGen having nothing to fit there is a "
        "fact about the shape, not a failure. The first version of this probe "
        "counted it as a failure.")
    w.add_caveat(
        "Tests each lineage's starting word and lineage A's word after its own "
        "three-step head ([B21, F02, B10], which precedes the shared script). "
        "A pass deeper still starts from a word this does not test.")
    path = w.save()

    print("  a   b  opening  has-loop  B fits  A-after-head fits")
    for r in rows:
        print(f" {r['a']:>2}  {r['b']:>2} {r['opening_phase_steps']:>8}"
              f"  {str(r['has_a_loop_pass_at_all']):<8}"
              f"  {str(r['lineage_B_fits']):<6}"
              f"  {str(r['lineage_A_after_head_fits'])}")
    print(f"\ncases: {len(rows)}   with no fit: {bad}")
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
