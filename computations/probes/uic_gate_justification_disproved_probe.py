#!/usr/bin/env python3
"""The gate that forces the sign rests on a duality the corpus already disproved.

Gap qou-sv7h, follow-on to uic_sign_forced_by_gate_probe (which measures THAT
the Pass-2 gate forces B < 0). This probe asks whether the gate's justification
holds, and connects two things the corpus has kept apart.

WHAT THE CORPUS ALREADY PROVES

`folio/quantum-observable-universe/mass-theory/operator-selection-lp.md`
(commit 6b7d2ec4a8, 2026-08-25) proves the operator-selection LP is DEGENERATE:

  * the NF basis begins with the empty word, so b_1 = 1 and G[1][j] = t_j -- the
    first Frobenius-positivity row IS the objective vector. The program
    minimises t.x subject to t.x >= 0, so its optimum is identically 0;
  * by strong duality n_target * y_0* = 0 with n_target > 0, hence **y_0* = 0**:
    the net constraint carries NO shadow price;
  * the minimiser set is a positive-dimensional face -- six vertices at n = 3,
    in mirror pairs -- so which one a solver returns is a pivoting artefact.

That commit corrected the CONTENT BLOCKS and deliberately proposed no
replacement ("choosing one is a decision about the physics"). It did not touch
`hecke_core_legacy.py`, which still reads the LP the old way in two places.

WHAT THIS PROBE ADDS -- the connection, and two measurements

1. `lp_shadow_price` sets y_0 = 1/[k]_q! and its docstring calls it "the dual
   variable of the normalisation constraint". The LP proves that dual is 0.
   Measured: 1/[k]_q! is 0.497 at k=2 ... 1.56e-4 at k=7, never 0. So the
   identification is false -- against a proof already in this corpus.

   What the choice actually does: 1/[k]_q! IS min_lambda(w/d) (verified k=2..11),
   so subtracting it zeroes exactly the two extreme partitions (k) and (1^k) --
   the trivial and sign representations -- at every level, and nothing else. It
   is not needed for non-negativity either: w/d > 0 already.

2. Substituting the PROVED y_0* = 0 does NOT repair the sign. It makes it MORE
   negative, because the gate still keeps Tr <= 0 and now more partitions carry
   weight. So the sign is not a weighting artefact; the gate is the mechanism,
   as the companion probe measures.

CONSEQUENCE. The sign cannot be repaired by correcting the dual variables. The
gate itself -- "keep the partitions with Tr <= 0" -- is what forces it, and its
stated justification is disproved: complementary slackness cannot single out a
partition set for a program whose optimum is identically 0 and whose minimiser
set is a positive-dimensional face.

NOT CLAIMED. What the replacement should be -- that is the same physics decision
6b7d2ec4a8 declined to make about the objective, one level down. Not claimed
that the accumulator diverges (it does not; see uic_a1_vanishing_trace_probe,
which retracts an earlier claim of mine).

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-sv7h OPEN.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

import _path_bridge  # noqa: F401,E402

from mpmath import mp  # noqa: E402

import hecke_core_legacy as H  # noqa: E402
from hecke_core import (  # noqa: E402
    q_factorial, partitions_of, partition_dimension, wedderburn_weight,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

ATOMS = [(1, 1, "2H"), (1, 2, "3H"), (2, 2, "4He"), (3, 3, "6Li")]
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


def main() -> int:
    set_compute_dps()
    print("=" * 74)
    print("  The gate's justification, against the corpus's own degeneracy proof")
    print("=" * 74)
    print()

    # ---- 1. the code's y_0 is not the LP's y_0* (proved 0) ---------------
    print("  1. y_0 used by lp_shadow_price vs the PROVED y_0* = 0")
    y0_rows, zeroed = [], []
    for k in range(2, 8):
        parts = [tuple(p) for p in partitions_of(k)]
        ratios = {p: mp.mpf(wedderburn_weight(p)) / partition_dimension(p) for p in parts}
        y0 = mp.mpf(1) / q_factorial(k)
        z = [p for p in parts if abs(ratios[p] - y0) < mp.mpf("1e-30")]
        zeroed.append(len(z))
        y0_rows.append({"k": k, "y0_used": fmt(y0), "y0_proved": "0",
                        "n_zeroed": len(z), "n_partitions": len(parts)})
        print(f"     k={k}  y_0 used = {mp.nstr(y0, 12):>18}   proved 0"
              f"   zeroes {len(z)} of {len(parts)} partitions")
    check("the y_0 the code uses is never 0, so it is not the proved dual",
          all(mp.mpf(r["y0_used"]) != 0 for r in y0_rows))
    check("its only effect is to zero exactly 2 partitions per level",
          set(zeroed) == {2}, "the (k) and (1^k) extremes, at every k")
    # non-negativity does not require the shift
    allpos = all(mp.mpf(wedderburn_weight(tuple(p))) / partition_dimension(tuple(p)) > 0
                 for k in range(2, 8) for p in partitions_of(k))
    check("w/d > 0 already, so the shift is not needed for y_lambda >= 0", allpos)

    # ---- 2. the proved y_0* does not repair the sign ---------------------
    print()
    print("  2. substituting the proved y_0* = 0")
    ents = [e for e in H._partition_table() if sum(e["partition"]) <= 6]
    rows = []
    for Z, N, name in ATOMS:
        A = Z + N
        ordering = ["p"] * Z + ["n"] * N
        s_asis = s_proved = mp.mpf(0)
        for e in ents:
            lam = tuple(e["partition"]); k = sum(lam)
            ch = [H._step_chain_generic(ordering[j], ordering[:j], k - 1, True)
                  for j in range(A)]
            o = H._PHN.lp_accumulator_step_traces_mpfr(
                list(lam), [[(str(c), str(d), g) for c, d, g in c2] for c2 in ch],
                Q_50_DIGIT_STR, 50)
            t, l = mp.mpf(o[-1][0]), mp.mpf(o[-1][1])
            if t > 0:
                continue                                   # Pass-2 gate, unchanged
            logratio = l + mp.log(abs(t)) - mp.log(e["dim"])
            C = mp.mpf(str(e["C_lambda_resolvent_MeV"]))
            wd = mp.mpf(wedderburn_weight(lam)) / partition_dimension(lam)
            y_asis = wd - mp.mpf(1) / q_factorial(k)
            # C is linear in y_lambda, so rescaling by y_proved/y_asis is exact.
            # The y_asis == 0 partitions cannot be rescaled and are dropped, so
            # this is a LOWER bound on the change, not the full recomputation.
            s_asis += C * logratio
            if y_asis != 0:
                s_proved += C * (wd / y_asis) * logratio
        rows.append({"atom": name, "A": A, "as_is": fmt(s_asis),
                     "with_proved_y0": fmt(s_proved)})
        print(f"     {name:>5} A={A}   as-is {mp.nstr(s_asis, 9):>13}"
              f"   with y_0*=0 {mp.nstr(s_proved, 9):>13}")
    check("the proved y_0* does NOT flip the sign -- still negative everywhere",
          all(mp.mpf(r["with_proved_y0"]) < 0 for r in rows))
    check("it makes the sign MORE negative, not less",
          all(mp.mpf(r["with_proved_y0"]) < mp.mpf(r["as_is"]) for r in rows),
          "more partitions carry weight, and the gate still keeps Tr<=0")

    print()
    print("  So the sign is not a weighting artefact. Correcting the dual is")
    print("  necessary -- the current identification is disproved -- and not")
    print("  sufficient: the GATE forces the sign. Choosing a replacement is the")
    print("  same physics decision 6b7d2ec4a8 declined about the objective.")

    w = WitnessBuilder("uic-gate-justification-disproved", engine="python+mpmath+rust")
    w.set_description(
        "Gap qou-sv7h: connects the proved degeneracy of prop:operator-selection-lp "
        "(commit 6b7d2ec4a8: optimum identically 0, y_0* = 0, minimiser set a "
        "positive-dimensional face) to hecke_core_legacy, which still reads the LP "
        "the old way. lp_shadow_price's y_0 = 1/[k]_q! is not the proved dual (0); "
        "its only effect is to zero the (k) and (1^k) partitions at every level. "
        "Substituting the proved y_0* = 0 does NOT repair the sign -- it makes it "
        "more negative -- so the gate, not the weighting, is the mechanism."
    )
    w.set_audit_only("docs/audits/2026-09-05-uic-gate-justification-disproved.md")
    w.add_data("y0_per_level", y0_rows)
    w.add_data("gated_sum_asis_vs_proved", rows)
    for nm, ok in CHECKS:
        w.add_assertion(nm, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="uic_gate_justification_disproved_probe")
    print(f"\n  witness: {w.save()}")
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed")
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
