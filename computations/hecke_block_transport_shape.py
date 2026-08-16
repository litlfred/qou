#!/usr/bin/env python3
"""hecke_block_transport_shape — is every far-commutation run a right-transport?

The Bokut–Shiao corner's `a ≤ b` regime has, after the two quadratic steps, only
far-commutations left: `small(a)` inside the prefix and `block(a,b)` twice at top
level. `hecke_corner_le_regime` measured the block as a nested double loop —
`a` levels, level `p` a run of `F_{p,q}` with `q` ascending — and conjectured it
should be "a nested application of `farComm_transport_left_sources`".

**That conjecture names the wrong direction**, which is what this checks. Within
a level the *high* letter `σ_{i−p}` is fixed and passes successively lower ones,
so the shape is

    a ++ (σ_x :: (w ++ b))   →   a ++ (w ++ (σ_x :: b))

which is `farComm_transport_right` (§4y), not `farComm_transport_left` (§4v).
The two are mirrors and not interchangeable: `_left` moves a generator *below*
the block leftwards, `_right` moves one *above* it rightwards.

## Method

The check is positional, which is what makes it a check rather than a restatement.
A right-transport of one letter across `k` others is `k` single steps whose
rewrite *position advances by exactly one each time*, with the same high letter
at the position throughout. So: group the chain's steps into maximal runs of
consecutive far-commutations sharing a high letter **and acting on the same
term** — see `far_runs` for why that last clause is load-bearing rather than
pedantic — then require of each run that

  1. the position advances by exactly 1 per step,
  2. the letter at the position is the run's high letter at every step,
  3. every letter passed is at least two below it — the far-commutation
     hypothesis `∀ y ∈ w, y + 1 < x` that `farComm_transport_right` asks for,
  4. the run's net effect on the word is the transport's source → target shape.

A run failing (1) or (2) would be some other rearrangement that merely happens
to use the same rule; only a run passing all four is a transport.

This covers the loop passes' far-commutations too, not just the blocks, so it
says something about the whole chain rather than the part being built next.

Emits `hecke-block-transport-shape.witness.json`. Bean qou-auq3.
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
        out.append((RMAP[name], w, k))
        f = eng.clean(eng.combine(f, eng.context_mul(left, eng.REL[name], right),
                                  -coeff))
    raise RuntimeError("no normal form")


def swap_at(w, p):
    """The word after a far-commutation applied at position `p`."""
    return w[:p] + (w[p + 1], w[p]) + w[p + 2:]


def far_runs(steps):
    """Maximal runs of consecutive far-commutations sharing a high letter **and
    acting on the same term**.

    The same-term test is the part that is easy to get wrong and that matters.
    A chain step rewrites one monomial of a multi-term element, and the element
    becomes multi-term as soon as the quadratic rule fires — it replaces one
    term by two. So two adjacent steps of the chain may act on entirely
    different words, and grouping on "consecutive, same high letter" alone
    silently welds them into one bogus run. An earlier version of this script
    did exactly that and reported a spurious failure at `a = b = 2`, where
    steps 10 and 11 both apply `F(0,2)` but to terms of length 6 and 5.

    The test: step `t+1` continues step `t`'s term iff its word is what step
    `t` produced, i.e. `w_{t+1} = swap_at(w_t, pos_t)`.

    Yields `(start_index, high_letter, [(word, position, low_letter), ...])`.
    """
    runs, cur, cur_x, cur_start = [], [], None, None
    for k, (rule, w, pos) in enumerate(steps):
        if rule[0] == "F":
            x = rule[1]                       # absolute index of the high letter
            if cur and x == cur_x and w == swap_at(cur[-1][0], cur[-1][1]):
                cur.append((w, pos, rule[2]))
                continue
            if cur:
                runs.append((cur_start, cur_x, cur))
            cur, cur_x, cur_start = [(w, pos, rule[2])], x, k
        elif cur:
            runs.append((cur_start, cur_x, cur)); cur, cur_x, cur_start = [], None, None
    if cur:
        runs.append((cur_start, cur_x, cur))
    return runs


def main():
    started = time.monotonic()
    rows = []
    bad_position, bad_letter, bad_far, bad_shape = 0, 0, 0, 0
    for a in range(2, 7):
        for b in (a, a + 1, a + 3):
            n, i = a + b + 3, a + b + 1
            if i >= n or i - b < 0:
                continue
            retune(n)
            steps = chain(i, a, b)
            for (start, x, run) in far_runs(steps):
                w0, pos0, _ = run[0]
                passed = [low for (_, _, low) in run]
                # 1. position advances by exactly one per step
                p_ok = all(run[t][1] == pos0 + t for t in range(len(run)))
                # 2. the high letter sits at the position at every step
                l_ok = all(run[t][0][run[t][1]] == x for t in range(len(run)))
                # 3. every letter passed is at least two below the high one
                f_ok = all(low + 1 < x for low in passed)
                # 4. net effect is the transport's source -> target shape
                src_ok = tuple(w0[pos0:pos0 + 1 + len(passed)]) == (x,) + tuple(passed)
                wN, posN, _ = run[-1]
                tgt = tuple(wN[:posN]) + tuple(wN[posN + 1:posN + 2]) + (x,) \
                    + tuple(wN[posN + 2:])
                s_ok = src_ok and tgt[pos0:pos0 + 1 + len(passed)] \
                    == tuple(passed) + (x,)
                bad_position += not p_ok
                bad_letter += not l_ok
                bad_far += not f_ok
                bad_shape += not s_ok
                rows.append({
                    "a": a, "b": b, "n": n, "i": i,
                    "first_step": start, "length": len(run),
                    "high_letter_rel_i": i - x,
                    "passed_rel_i": [i - low for low in passed],
                    "position_advances_by_one": p_ok,
                    "high_letter_at_position": l_ok,
                    "far_hypothesis_holds": f_ok,
                    "transport_shape_holds": s_ok,
                })

    w = WitnessBuilder("hecke-block-transport-shape", engine="sympy",
                       start_time=started)
    w.set_description(
        "Every maximal run of consecutive far-commutations sharing a high "
        "letter, in the Bokut-Shiao corner's a <= b chain, is a RIGHT "
        "transport: the high letter sits at the rewrite position throughout, "
        "the position advances by exactly one per step, every letter passed is "
        "at least two below it, and the run's net effect is "
        "a ++ (x :: (w ++ b)) -> a ++ (w ++ (x :: b)). That is "
        "farComm_transport_right, NOT farComm_transport_left.")
    w.add_parameter("lean_lemma", "UGB.GrobnerShirshov.Hecke.farComm_transport_right")
    w.add_parameter("transport_direction", "rightwards: high letter moves right")
    w.add_assertion("runs_whose_position_does_not_advance_by_one",
                    computed=str(bad_position), expected="0")
    w.add_assertion("runs_not_headed_by_the_high_letter",
                    computed=str(bad_letter), expected="0")
    w.add_assertion("runs_violating_the_far_commutation_hypothesis",
                    computed=str(bad_far), expected="0")
    w.add_assertion("runs_whose_net_effect_is_not_the_transport_shape",
                    computed=str(bad_shape), expected="0")
    w.add_data("runs_checked", len(rows))
    w.add_data("runs", rows)
    w.add_caveat(
        "Measured over a = 2..6 and b in {a, a+1, a+3} only, and against the "
        "reduction the engine's deg-lex strategy happens to produce. A Lean "
        "proof may follow a different chain.")
    w.add_caveat(
        "Runs are grouped by high letter AND by same-term continuation. "
        "Grouping on the high letter alone is wrong: an element becomes "
        "multi-term the moment the quadratic rule fires, so two adjacent chain "
        "steps can rewrite different terms. Without the same-term test this "
        "script reported a spurious failing run at a = b = 2 -- steps 10 and 11 "
        "both apply F(0,2), but to words of length 6 and 5.")
    w.add_caveat(
        "This says each run IS a right-transport. It does not say the Lean "
        "lemma applies as-is: farComm_transport_right carries the UNRESTRICTED "
        "collision hypothesis (every split of w, including the one naming the "
        "transport's own final word). farComm_transport_left needed a _sources "
        "variant with u != [] for exactly that reason in the a > b regime, so "
        "the right-hand mirror may need one too. Not measurable here -- it is a "
        "property of the bystanding terms, not of the run.")
    path = w.save()

    print("  a   b  first  len  high  passed")
    for r in rows:
        flag = "" if (r["position_advances_by_one"] and r["high_letter_at_position"]
                      and r["far_hypothesis_holds"] and r["transport_shape_holds"]) else "  <-- FAILS"
        print(f" {r['a']:>2}  {r['b']:>2}  {r['first_step']:>5} {r['length']:>4}"
              f"  {r['high_letter_rel_i']:>4}  {r['passed_rel_i']}{flag}")
    total_bad = bad_position + bad_letter + bad_far + bad_shape
    print(f"\nruns: {len(rows)}   failing: position {bad_position}, "
          f"letter {bad_letter}, far {bad_far}, shape {bad_shape}")
    print(f"witness -> {path}")
    return 0 if not total_bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
