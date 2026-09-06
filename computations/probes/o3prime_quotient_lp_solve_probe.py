"""O3' SOLVED: pose the operator-selection program on the radical quotient.

Owner ruling 2026-09-05 authorised O3' -- re-pose the degenerate
operator-selection LP as a block program over the RADICAL QUOTIENT, i.e. over
the Wedderburn blocks of nonzero Markov weight.  The Lean half is
`QOU.MassTheory.BlockSDPNondegeneracy` (5 declarations, sorry-free).  This is
the compute half.

WHAT THE FULL LP DOES, AND WHY IT NEEDS REPLACING
-------------------------------------------------
`prop:operator-selection-lp` is degenerate (commit 6b7d2ec4a8): the NF basis
contains the identity, so the first Frobenius row IS the objective vector, the
program minimises t.x subject to t.x >= 0, its optimum is IDENTICALLY 0, and by
strong duality the net-constraint dual is y_0* = 0 -- so the program cannot
price its own net constraint at any n_target.  Confirmed by every committed
solve (`y0_star` ~ 1e-47 in a-K-via-lp-dual-full.witness.json).

THE O3' PROGRAM
---------------
Restrict to SURVIVING blocks (w_lambda != 0; under SU(2) exactly the <=2-row
partitions), and pose

    min  sum_lambda t_lambda x_lambda
    s.t. sum_lambda x_lambda = n_target,     (net)
         w_lambda x_lambda >= 0              (Frobenius positivity, per block)

with t_lambda = w_lambda * chi^lambda(W_atom) and G = diag(w_lambda), which is
what `aK_via_lp_dual_full.py` already builds.  On the quotient every
w_lambda > 0, so the Frobenius rows are x_lambda >= 0 and the identity-row
coincidence that caused the degeneracy is GONE: G's rows are w_lambda * e_lambda
and none of them is t.

This is the SDP under the natural lift T_lambda = t_lambda * I.  With that lift
the block program sees only tr(Phi_lambda), so it reduces exactly to the scalar
LP above -- which is why the canonical LP entry point is the right solver and a
dense-PSD cone is not needed here.  A genuinely matrix-valued T_lambda would NOT
reduce this way; that is a different program and is not what is solved here.

FALSIFIERS, STATED BEFORE THE RUN
---------------------------------
The reduction in the proposal's §9c predicts three things.  Any one failing
means §9c is wrong and the correction it makes to §8 must be retracted.

  F1  optimal value == n_target * min_lambda t_lambda
  F2  the primal support is the argmin block (selection)
  F3  y_0* == min_lambda t_lambda, and in particular y_0* != 0
      -- this is the whole point: the full LP prices nothing, so if the
      quotient program ALSO returns y_0* = 0 then O3' has not repaired the
      defect it was chosen to repair.

F3 is the load-bearing one.  F1 and F2 restate the reduction; F3 is the claim
that the reduction BUYS something.

PRECISION: EXACT END TO END
---------------------------
t_lambda and G come from the witness's decimal STRINGS and are handed to the
solver as strings; `_solve_operator_selection_lp_clarabel` takes decimal strings
for t, G and n_target and they reach the MPFR solver intact ("pass 50-dps
strings upstream for full precision").  Everything read back comes from the
`*_str` fields the LP-dual contract requires.  `backend` is FORCED to clarabel
so an unavailable binary raises rather than silently downgrading to scipy f64.
There is no float64 in the path.

This was NOT the first version, and the audit is why.  The first version built
np.ndarray inputs and serialized the solver's float64 mirrors through `fmt` --
stamping 50 dps onto 53 bits, exactly the "never report a float64 agreement as
exact" defect.  `mpf_mixed_arithmetic_audit` flagged four sites and pushed the
corpus ratchet from 3 to 7 over baseline.  Reading the `*_str` fields fixed
three of the four; the audit still (correctly) tainted the rest, because the
solver's INPUTS were f64, so its 50 digits described a float64-specified
problem.  Passing strings in removes the taint at its source rather than
arguing about it: the ratchet returned to 3 over baseline, its pre-existing
value, with this file named zero times.

Do not "simplify" the string plumbing back to np.ndarray, and do not relax
`backend="clarabel"`.

SCOPE
-----
Reads t_lambda and w_lambda from the committed partition-LP witness rather than
recomputing chi^lambda(W_atom); this probe is about the PROGRAM, not about the
characters.  It does not wire O3' into `hecke_core_legacy` -- that recomputes
every binding number and is a separate change.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401,E402

import numpy as np  # noqa: E402
from mpmath import mp  # noqa: E402

from live_channels import is_live  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()

sys.path.insert(0, str(HERE.parents[1] / "tools" / "pyhecke" / "python"))
from pyhecke.lp_dual_solver import solve_operator_selection_lp  # noqa: E402

CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""),
          flush=True)


WIT = HERE.parent / "a-K-via-lp-dual-full.witness.json"


def main() -> int:
    rows = json.load(WIT.open())["data"]["rows"]
    print(f"=== O3' on the radical quotient — {len(rows)} committed rows ===",
          flush=True)

    out = []
    f1 = f2 = f3 = True
    all_y0_nonzero = True
    for idx, r in enumerate(rows):
        # `is_live`, not `!= 0`.  This read `mp.mpf(p["y_lambda"]) != 0` until
        # 2026-09-05, which worked only because the pre-regeneration chi caches
        # serialized the SU(2)-suppressed weights as exact 0; the rebuilt ones
        # serialize the arithmetic residual (1e-73).  `live_channels.is_live`
        # is the corpus's existing correct implementation -- DEAD_TOL = 1e-30,
        # which separates 1e-73 from the 1e-3..1e-1 live weights by forty
        # orders -- and its docstring settles the definition: "Defined by the
        # weight, not by the row count".  Third probe found carrying this
        # proxy; consolidating on the library rather than inventing a cut.
        surv = [p for p in r["per_partition"] if is_live(mp.mpf(p["y_lambda"]))]
        n = sum(surv[0]["partition"])
        # EXACT from the witness's decimal strings.  These carry the checks and
        # everything serialized; the float64 arrays below exist ONLY because the
        # canonical solver's signature takes np.ndarray.
        t_mp = [mp.mpf(p["contribution"]) for p in surv]
        n_target = mp.mpf(1)

        # STRINGS IN, strings out.  `_solve_operator_selection_lp_clarabel`
        # accepts decimal strings for t, G and n_target and they reach the
        # MPFR solver INTACT ("pass 50-dps strings upstream for full
        # precision").  Passing np.ndarray would enter as f64 and taint every
        # value read back -- which the mixed-arithmetic audit correctly flags.
        # backend is FORCED so an unavailable clarabel raises instead of
        # silently downgrading to scipy float64.
        t_str = [p["contribution"] for p in surv]
        G_str = [[(p["y_lambda"] if i == j else "0")
                  for j, _ in enumerate(surv)]
                 for i, p in enumerate(surv)]
        res = solve_operator_selection_lp(
            t_str, G_str, "1", backend="clarabel",
        )
        d = res.to_dict()

        t_min = min(t_mp)
        arg = min(range(len(t_mp)), key=lambda i: t_mp[i])
        # Read the solver's MPFR strings, never its float64 mirrors -- pushing a
        # float64 through `fmt` would stamp 50 dps onto 53 bits.
        obj = mp.mpf(d["primal_obj_str"])
        y0 = mp.mpf(d["y0_star_str"])
        gap = mp.mpf(d["duality_gap_str"])
        x = [mp.mpf(v) for v in d["x_star_str"]]

        tol = mp.mpf("1e-7") * max(mp.mpf(1), abs(t_min))
        ok1 = abs(obj - n_target * t_min) <= tol
        support = [i for i, xi in enumerate(x) if abs(xi) > mp.mpf("1e-7")]
        ok2 = support == [arg]
        ok3 = abs(y0 - t_min) <= tol
        f1 &= ok1; f2 &= ok2; f3 &= ok3
        all_y0_nonzero &= abs(y0) > mp.mpf("1e-12")

        print(f"  row {idx}  n={n:<3} surv={len(surv):<2} "
              f"argmin={surv[arg]['partition']}  obj={mp.nstr(obj, 11)}  "
              f"n_t*t_min={mp.nstr(n_target * t_min, 11)}  "
              f"y0*={mp.nstr(y0, 11)}  gap={mp.nstr(gap, 3)}  "
              f"F1={ok1} F2={ok2} F3={ok3}", flush=True)

        out.append({
            "row": idx, "n": n, "n_survivors": len(surv),
            "argmin_partition": surv[arg]["partition"],
            "t_min": fmt(t_min),
            "primal_obj": fmt(obj),
            "y0_star": fmt(y0),
            "duality_gap": fmt(gap),
            "support_indices": support,
            "F1_value": ok1, "F2_selects": ok2, "F3_priced": ok3,
        })

    print(flush=True)
    check("F1 — optimal value is n_target * min_lambda t_lambda, every row", f1)
    check("F2 — the primal support IS the argmin block: the program SELECTS", f2)
    check("F3 — y_0* = min t_lambda, so the net constraint is PRICED", f3)
    check("y_0* is NONZERO on every row — the full LP's degeneracy is GONE "
          "(there y_0* = 0 identically, ~1e-47 in the committed solves)",
          all_y0_nonzero)
    check("the quotient is non-empty at every n, so the program exists",
          all(r["n_survivors"] > 0 for r in out))

    w = WitnessBuilder("o3prime-quotient-lp-solve", engine="python+numpy+clarabel")
    w.set_description(
        "O3' compute half (owner ruling 2026-09-05): the operator-selection "
        "program re-posed on the RADICAL QUOTIENT -- surviving Wedderburn "
        "blocks only (w_lambda != 0; under SU(2) the <=2-row partitions). "
        "Solved via the canonical solve_operator_selection_lp. Tests three "
        "falsifiers stated in advance: optimal value = n_target*min t_lambda; "
        "the primal support is the argmin block (SELECTION); and y_0* = "
        "min t_lambda, i.e. NONZERO -- where the full NF-indexed LP has "
        "y_0* = 0 identically and prices nothing. Under the natural lift "
        "T_lambda = t_lambda*I the block SDP reduces exactly to this LP; a "
        "matrix-valued T_lambda would not and is a different program."
    )
    w.set_audit_only(
        "docs/proposals/2026-09-05-operator-selection-objective-replacement.md")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("n_target", "1")
    w.add_data("rows", out)
    for name, ok in CHECKS:
        w.add_assertion(name, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="o3prime_quotient_lp_solve_probe")
    print(f"\n  witness: {w.save()}", flush=True)
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed",
          flush=True)
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
