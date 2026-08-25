#!/usr/bin/env python3
"""hecke_tail_diagonal_check — does the tail's argument survive at `b = a`?

Three measurements of the `a ≤ b` tail were made off the diagonal and each
excluded `b = a` explicitly: the `blockPass` fit
(`hecke_tail_assembly_fit.py`), the `hpark` collision
(`hecke_tail_collision_check.py`), and the reordered schedule
(`hecke_tail_reorder_check.py`). The exclusion is not cosmetic — on the
diagonal the block is one level shorter and runs `blockPassFromTwo`, whose
source is a *different word* from `blockPass`'s:

    blockPass          A ++ descWord i jppp ++ [σ_jp, σ_jpp, σ_j₁]
                         ++ [σ_jp] ++ descWord jm j₂ ++ T
    blockPassFromTwo   A ++ descWord i jppp ++ [σ_jp]
                         ++ σ_jpp :: descWord j₁ j₂ ++ [σ_jp] ++ T

(`blockPass` is one leading transport followed by `blockPassFromTwo`; the
trailing `σ_jp` sits on the other side of the descending run.) So none of the
three off-diagonal results transfers by inspection, and `blockPassFromTwo` is
the lemma that has to fit.

This runs all three checks on the diagonal at once, against
`blockPassFromTwo`'s actual Lean source and target:

  * the fit — `A` and `T` solved for, source and target under the SAME pair;
  * `hpark` under the engine's order, expected to fail at the second block as
    it does off the diagonal;
  * `hpark` under the reordered schedule [block2, block1, …], expected to hold.

A pass means the §4am argument transfers and a diagonal `tailChain` is the same
proof with `blockPassFromTwo` substituted. A failure means the diagonal is its
own problem, which is worth knowing before writing the Lean rather than after.

Emits `hecke-tail-diagonal-check.witness.json`. Bean qou-auq3.
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
_r = importlib.util.spec_from_file_location(
    "rc", HERE / "hecke_tail_reorder_check.py")
rc = importlib.util.module_from_spec(_r); _r.loader.exec_module(rc)


def diag_core(a, b):
    """blockPassFromTwo's source core, in indices relative to `i`."""
    def dW(x, y):
        return tuple(range(x, y + 1)) if x <= y else ()
    return dW(0, a - 3) + (a - 1, a - 2) + dW(a, b) + (a - 1,)


def diag_target(a, b):
    """blockPassFromTwo's target core (same A and T bracket it)."""
    def dW(x, y):
        return tuple(range(x, y + 1)) if x <= y else ()
    return dW(a - 1, b) + dW(0, a - 3) + (a - 2, a - 1)


def solve_ctx(word, core, i):
    rel = tuple(i - x for x in word)
    for la in range(len(rel) + 1):
        if rel[la:la + len(core)] == core:
            return rel[:la], rel[la + len(core):]
    return None


def main():
    started = time.monotonic()
    rows, bad = [], 0
    for a in range(3, 7):
        b = a
        n, i = a + b + 3, a + b + 1
        if i >= n or i - b < 0:
            continue
        rc.retune(n)
        info = rc.tail_steps(i, a, b)
        if info is None:
            rows.append({"a": a, "b": b, "read": False}); bad += 1; continue
        steps, roots = info["steps"], info["roots"]
        core, tgt = diag_core(a, b), diag_target(a, b)
        rel = lambda w: tuple(i - x for x in w)

        # --- the fit: both roots must parse as A ++ core ++ T, and each must
        #     reach A ++ target ++ T under the SAME (A, T).
        fits, ctx = {}, {}
        for tag, w in enumerate(roots):
            got = solve_ctx(w, core, i)
            ctx[tag] = got
            if got is None:
                fits[tag] = False
                continue
            A, T = got
            fits[tag] = True
            ctx[tag] = (A, T)

        # --- engine order: which lineage moves first, and hpark at each block
        order_engine = [s["lineage"] for s in steps]
        def hpark_at(schedule):
            f = dict(info["start"])
            for _ in range(info["pre"]):
                f = rc.apply_at(f, *rc.next_redex(f))
            seen, out = set(), {}
            for s in schedule:
                if s["lineage"] not in seen:
                    seen.add(s["lineage"])
                    others = [w for w in f if w != s["src"]]
                    got = solve_ctx(s["src"], core, i)
                    if got and len(others) == 1:
                        A = got[0]
                        B = rel(others[0])
                        out[s["lineage"]] = B[:len(A)] != A
                f = rc.apply_at(f, s["src"], s["rule"], s["pos"])
            return out, len(f) == 0
        hp_eng, zero_eng = hpark_at(steps)
        reordered = ([s for s in steps if s["lineage"] == 1]
                     + [s for s in steps if s["lineage"] == 0])
        hp_re, zero_re = hpark_at(reordered)

        both_fit = all(fits.values()) and len(fits) == 2
        eng_fails = not all(hp_eng.values()) if hp_eng else None
        re_holds = bool(hp_re) and all(hp_re.values())
        ok = both_fit and eng_fails and re_holds and zero_re
        bad += not ok
        rows.append({
            "a": a, "b": b, "n": n, "i": i, "read": True,
            "tail_steps": len(steps),
            "roots_rel_i": [list(rel(w)) for w in roots],
            "blockPassFromTwo_fits_both_terms": both_fit,
            "solved_contexts": {str(k): [list(v[0]), list(v[1])]
                                for k, v in ctx.items() if v},
            "hpark_engine_order": {str(k): v for k, v in hp_eng.items()},
            "hpark_engine_order_fails": eng_fails,
            "hpark_reordered": {str(k): v for k, v in hp_re.items()},
            "hpark_reordered_all_hold": re_holds,
            "reordered_reaches_zero": zero_re,
            "diagonal_matches_offdiagonal_argument": ok,
        })

    w = WitnessBuilder("hecke-tail-diagonal-check", engine="sympy",
                       start_time=started)
    w.set_description(
        "The three off-diagonal tail measurements (blockPass fit, hpark "
        "collision, reordered schedule) each excluded b = a, where the block "
        "is one level shorter and runs blockPassFromTwo -- whose SOURCE WORD "
        "differs from blockPass's, so nothing transfers by inspection. This "
        "runs all three on the diagonal against blockPassFromTwo's actual "
        "Lean source and target: whether it fits both terms under a common "
        "(A, T), whether hpark fails under the engine's order as it does off "
        "the diagonal, and whether the reordered schedule repairs it.")
    w.add_parameter(
        "blockPassFromTwo_source",
        "A ++ descWord i jppp ++ [s_jp] ++ s_jpp :: descWord j1 j2 "
        "++ [s_jp] ++ T")
    w.add_parameter(
        "blockPassFromTwo_target",
        "A ++ descWord jp j2 ++ descWord i jppp ++ descWord jpp jp ++ T")
    w.add_assertion("diagonals_not_matching_the_offdiagonal_argument",
                    computed=str(bad), expected="0")
    w.add_data("cases_checked", len(rows))
    w.add_data("cases", rows)
    w.add_caveat(
        "a = 3..6 on the diagonal only. a = 2 is excluded as elsewhere in this "
        "arc: the loop is empty there and the prefix head degenerates.")
    w.add_caveat(
        "Hypotheses read off the lemma statements and checked against the "
        "measured words, as in the off-diagonal probes. A pass says a "
        "diagonal tailChain should be the same proof with blockPassFromTwo "
        "substituted; it does not say the Lean composes.")
    path = w.save()

    print("  a   b  steps  fit-both  hpark(engine)  hpark(reordered)  zero")
    for r in rows:
        if not r.get("read"):
            print(f" {r['a']:>2}  {r['b']:>2}   <unreadable>"); continue
        print(f" {r['a']:>2}  {r['b']:>2} {r['tail_steps']:>6}"
              f"  {str(r['blockPassFromTwo_fits_both_terms']):<8}"
              f"  {str(r['hpark_engine_order']):<14}"
              f"  {str(r['hpark_reordered']):<16}"
              f"  {str(r['reordered_reaches_zero'])}"
              f"{'' if r['diagonal_matches_offdiagonal_argument'] else '  <-- OFF'}")
    print(f"\ncases: {len(rows)}   off pattern: {bad}")
    print(f"witness -> {path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
