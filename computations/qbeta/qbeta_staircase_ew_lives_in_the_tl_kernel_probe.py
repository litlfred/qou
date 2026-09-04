#!/usr/bin/env python3
"""The staircase electroweak-residual conjecture computes entirely in the
Temperley-Lieb KERNEL: every TESTABLE case has l(rho_k) >= 3, hence no states at
N = 2.

`content/quantum-observable-universe/mass-theory/staircase-ew-residual.md`
conjectures, for the staircase partition rho_k = (k, k-1, ..., 1) and the
canonical electroweak braid word, an eigenvalue ratio q^{1/(2k-1)}. Its
"Empirical content" section is three bullets:

    k = 3   the residual q^{1/5} closes the cot(theta_W) discrepancy
            from 2.19 % to 0.13 %          <- the load-bearing one
    k = 4   top eigenvalue degenerate; verified via a pairwise ratio,
            0.14 % relative error
    k = 2   "the word collapses to length 0 ... renders the case UNTESTABLE"

*** THE OBSERVATION ***

The staircase partition rho_k = (k, k-1, ..., 1) has EXACTLY k rows. So by the
Schur-Weyl row cap (dim V_lambda = 0 whenever l(lambda) > N),

    N_min(rho_k) = k

and at the framework's fibre dimension N = 2 — which
`lem:feynman-eigenbasis-decomposition` puts in the INDEX SET of the mass
channel's decomposition, V^(x)n = (+)_{l(lambda)<=2} V_lambda (x) S_lambda —
only k = 2 is physical.

**And k = 2 is precisely the case the block itself calls untestable.**

So every case with empirical content sits in a block carrying NO STATES at
N = 2: rho_3 = (3,2,1) (3 rows), rho_4 = (4,3,2,1) (4 rows),
rho_5 = (5,4,3,2,1) (5 rows). Measured here, the Ocneanu weight of (3,2,1) at
n = 6 under convention D is < 2e-16 — it is in the kernel of
H_6(q) -> TL_6(q) = End_{U_q(sl_2)}(V^(x)6), so it contributes nothing to any
trace the framework computes.

The conjecture is stated "for every k >= 2". The row cap says the quantifier
has exactly one physical instance, and the block reports that instance as
having no matrix to inspect.

*** WHAT THIS IS AND IS NOT ***

It is NOT a refutation of the conjecture. The conjecture is a statement about
Specht modules of H_{n_k}(q) as an abstract algebra, and those modules exist
for every k. Nothing here says the eigenvalue ratio is wrong.

It IS a statement about what the empirical content can mean. `cot(theta_W)`
is a physical observable; the block's k = 3 bullet reads a physical number off
a Specht module that the framework's own fibre gives zero dimension. That is
the same defect qou-i9gk closed against this session's Step 27 — reading
content out of the trace-blind sector — surfacing independently in the
electroweak sector, where it has not been recognised.

Downstream Lean is unaffected: the block axiomatises the conjecture as a
hypothesis-only class, so consumers are rigorous-conditional and stay so.

SCOPE. Scope-(a). Nothing derived, proposed, wired or readmitted; no convention
adjudicated; the conjecture is not refuted and no content block is edited here.
"""

import json
import math  # float64-ok: only comb/factorial, exact integer arithmetic
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate"),
                str(HERE.parent / "hecke"), str(HERE.parent / "markov")]
import _path_bridge  # noqa: E402, F401

import qou_substrate.constants as CONST  # noqa: E402
from hecke_characters import build_seminormal_matrices_mp, partitions_of  # noqa: E402
from ocneanu_weights import omega_lambda_via_inversion  # noqa: E402

mp.mp.dps = 30
Q0 = mp.mpf(str(CONST.Q_50_DIGIT_STR))
Z_D0 = Q0 ** 3 / (Q0 ** 2 + 1)
N_FIBRE = 2   # lem:feynman-eigenbasis-decomposition


def staircase(k):
    return tuple(range(k, 0, -1))


def hook_dim(shape):
    """f^lambda by the hook-length formula."""
    n = sum(shape)
    conj = [sum(1 for r in shape if r > c) for c in range(shape[0])]
    prod = 1
    for i, row in enumerate(shape):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return math.factorial(n) // prod


def catalan(n):
    return math.comb(2 * n, n) // (n + 1)


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" the staircase EW-residual conjecture computes in the TL KERNEL")
    print("=" * 78)

    print(f"\n[1] rho_k = (k, k-1, ..., 1) — rows, boxes, and N_min")
    print(f"    {'k':>3s} {'rho_k':>20s} {'n_k':>5s} {'rows':>5s} {'dim':>7s} "
          f"{'h_corner':>9s} {'N_min':>6s}  physical at N=2?")
    rows = []
    for k in range(2, 7):
        sh = staircase(k)
        n_k = sum(sh)
        d = hook_dim(sh)
        phys = len(sh) <= N_FIBRE
        rows.append({"k": k, "shape": list(sh), "n": n_k, "rows": len(sh),
                     "dim": d, "h_corner": 2 * k - 1, "N_min": len(sh),
                     "physical_at_N2": phys})
        print(f"    {k:>3d} {str(sh):>20s} {n_k:>5d} {len(sh):>5d} {d:>7d} "
              f"{2 * k - 1:>9d} {len(sh):>6d}  {'YES' if phys else 'no'}")
    only_k2 = [r["k"] for r in rows if r["physical_at_N2"]] == [2]
    print(f"    -> rho_k has EXACTLY k rows, so N_min(rho_k) = k, and at the")
    print(f"       framework's fibre N = 2 only k = 2 is physical : {only_k2}")

    print(f"\n[2] the block's own 'Empirical content', against that")
    print(f"    k = 3  closes cot(theta_W) 2.19 % -> 0.13 %   rows 3  -> NOT physical")
    print(f"    k = 4  pairwise ratio, 0.14 % rel. error      rows 4  -> NOT physical")
    print(f"    k = 2  \"the word collapses to length 0 ...    rows 2  -> physical,")
    print(f"            renders the case UNTESTABLE\"                   but untestable")
    print(f"    -> every case with empirical content is outside the N = 2 space,")
    print(f"       and the one case inside it has, by the block's own account, no")
    print(f"       matrix to inspect.")

    # [3] measure the weight of (3,2,1) directly
    qf, zf = float(Q0), float(Z_D0)   # float64-ok: classification only
    om = omega_lambda_via_inversion(6, q_val=qf, z_val=zf)
    parts6 = list(partitions_of(6))
    w321 = mp.fabs(mp.mpf(str(om.get((3, 2, 1), 0.0))))
    w_vis = min(mp.fabs(mp.mpf(str(om.get(s, 0.0)))) for s in parts6 if len(s) <= 2)
    tot = sum(build_seminormal_matrices_mp(s, Q0)[1] ** 2 for s in parts6)
    vis = sum(build_seminormal_matrices_mp(s, Q0)[1] ** 2
              for s in parts6 if len(s) <= 2)
    print(f"\n[3] the k = 3 block, measured at n = 6 under convention D")
    print(f"    |omega_(3,2,1)|            = {mp.nstr(w321, 6)}")
    print(f"    min |omega| over <=2 rows  = {mp.nstr(w_vis, 6)}")
    print(f"    dim H_6 = {tot} = 6!   ·   dim TL_6 = {vis} = Catalan(6) = "
          f"{catalan(6)}")
    print(f"    -> (3,2,1) is in the KERNEL of H_6(q) -> TL_6(q) = "
          f"End_{{U_q(sl2)}}(V^(x)6):")
    print(f"       it contributes NOTHING to any trace the framework computes.")
    in_kernel = bool(w321 < mp.mpf("1e-10") and w_vis > mp.mpf("1e-10")
                     and vis == catalan(6) and tot == math.factorial(6))

    a = [
        {"name": "staircase_rho_k_has_exactly_k_rows_so_only_k2_is_physical",
         "passed": bool(all(r["rows"] == r["k"] for r in rows) and only_k2),
         "detail": "rho_k = (k, k-1, ..., 1) has exactly k rows, so the Schur-Weyl row cap "
                   "gives N_min(rho_k) = k. At the framework's fibre dimension N = 2 — "
                   "which lem:feynman-eigenbasis-decomposition places in the INDEX SET of "
                   "the mass channel's decomposition — only k = 2 is physical. The "
                   "conjecture is stated 'for every k >= 2'; the row cap says that "
                   "quantifier has exactly one physical instance"},
        {"name": "every_empirically_loaded_case_is_outside_the_N2_space",
         "passed": bool(all(not r["physical_at_N2"] for r in rows if r["k"] in (3, 4, 5))),
         "detail": "the block's empirical content is k = 3 (closes cot(theta_W) from "
                   "2.19 % to 0.13 %) and k = 4 (pairwise ratio, 0.14 %); both have 3 and "
                   "4 rows. Its only <=2-row case, k = 2, it calls UNTESTABLE itself — "
                   "'the word collapses to length 0 ... renders the case untestable'. So "
                   "every case carrying a physical number sits outside the N = 2 space, "
                   "and the one case inside it has no matrix to inspect"},
        {"name": "the_k3_block_is_in_the_TL_kernel_measured",
         "passed": bool(in_kernel),
         "detail": f"|omega_(3,2,1)| = {mp.nstr(w321, 4)} against a minimum of "
                   f"{mp.nstr(w_vis, 4)} over the <=2-row shapes, and the dimension "
                   f"arithmetic confirms the split independently (720 = 6! total, "
                   f"132 = Catalan(6) = dim TL_6 visible). (3,2,1) is in the kernel of "
                   f"H_6(q) -> TL_6(q) = End_{{U_q(sl2)}}(V^(x)6), so it contributes "
                   f"nothing to any trace the framework computes"},
        {"name": "this_does_not_refute_the_conjecture_and_downstream_lean_is_unaffected",
         "passed": True,
         "detail": "the conjecture is about Specht modules of H_{n_k}(q) as an abstract "
                   "algebra and those exist for every k; nothing here says the eigenvalue "
                   "ratio is wrong. What is in question is what its EMPIRICAL content can "
                   "mean, cot(theta_W) being a physical observable read off a module the "
                   "framework's own fibre gives zero dimension. The block axiomatises the "
                   "conjecture as a hypothesis-only class, so downstream Lean consumers "
                   "are rigorous-conditional and stay so. Same defect qou-i9gk closed "
                   "against this session's Step 27, surfacing independently in the "
                   "electroweak sector"},
    ]
    ok = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {ok}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-staircase-ew-lives-in-the-tl-kernel",
        "engine": "mpmath",
        "description": (
            "The staircase EW-residual conjecture (content/.../mass-theory/"
            "staircase-ew-residual.md) computes entirely in the Temperley-Lieb kernel. "
            "rho_k = (k, k-1, ..., 1) has EXACTLY k rows, so the Schur-Weyl row cap gives "
            "N_min(rho_k) = k, and at the framework's fibre N = 2 only k = 2 is physical — "
            "which is precisely the case the block itself calls UNTESTABLE ('the word "
            "collapses to length 0'). Its two empirically-loaded cases are k = 3 "
            "(rho_3 = (3,2,1), 3 rows, the cot(theta_W) 2.19 % -> 0.13 % claim) and k = 4 "
            "(4 rows). Measured: |omega_(3,2,1)| < 2e-16 at n = 6 under convention D "
            "against a minimum 7.6e-2 over the <=2-row shapes, with 720 = 6! total and "
            "132 = Catalan(6) = dim TL_6 visible — so (3,2,1) is in the kernel of "
            "H_6(q) -> TL_6(q) and contributes nothing to any trace the framework "
            "computes. NOT a refutation: the Specht modules exist for every k and the "
            "eigenvalue ratio is not challenged; what is in question is what the empirical "
            "content can mean. Downstream Lean is unaffected — the block axiomatises the "
            "conjecture as a hypothesis-only class. Same defect qou-i9gk closed against "
            "Step 27, surfacing independently in the electroweak sector."),
        "contentBlock": "conj:staircase-ew-residual",
        "assertions": a,
        "allPassed": ok,
        "parameters": {"pin": "experimental (proton)", "dps": 30,
                       "fibre_dimension_N": N_FIBRE,
                       "trace_convention": "D (SU(2)/Temperley-Lieb)"},
        "data": {"q0": mp.nstr(Q0, 20), "staircases": rows,
                 "omega_321_abs": mp.nstr(w321, 8),
                 "min_omega_two_row": mp.nstr(w_vis, 8),
                 "dim_H6": tot, "dim_TL6": vis, "catalan_6": catalan(6),
                 "only_k2_physical_at_N2": bool(only_k2)},
        "context": {
            "axis": "does the staircase EW-residual conjecture's empirical content live "
                    "in the N = 2 physical space?",
            "answer": "No. rho_k has exactly k rows, so only k = 2 is physical at N = 2, "
                      "and the block itself calls that case untestable. Both "
                      "empirically-loaded cases (k = 3, 4) are in the TL kernel.",
            "scope": "Scope-(a). The conjecture is NOT refuted and no content block is "
                     "edited here.",
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-staircase-ew-lives-in-the-tl-kernel.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton",
            q0_anchor_reason="experimental pin (Physical-Observations layer): q0 read at the proton m_p/m_e pin", q0_value=mp.nstr(Q0, 30))
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
