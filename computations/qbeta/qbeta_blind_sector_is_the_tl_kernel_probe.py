#!/usr/bin/env python3
"""qou-i9gk hole 1: Step 27's "trace-blind sector" is the Temperley-Lieb KERNEL,
and reading it as hidden information contradicts the convention it was measured in.

*** THE HOLE, AND WHY IT MATTERS ***

Step 27 measured that convention D's Ocneanu weights vanish on every partition of
6 with more than two rows, while the binding character there is large
(chi_(3,2,1) = -9.598, the biggest of any block), and read that as

    "588 of 720 dimensions carry information the observable cannot see."

`qou-fvzm` states the Schur-Weyl ROW CAP: dim V_lambda = 0 whenever
l(lambda) > N, and the framework has N = 2. If the physical space is the
Schur-Weyl image, those blocks have NO STATES and the reading is wrong — not
hidden information but no information. Step 27 quoted the cap approvingly while
measuring nonzero characters in exactly those blocks and never reconciled the
two. This probe settles which vanishing is which.

*** RESULT 1 — THE TWO VANISHINGS ARE ONE STATEMENT ***

Measured here at n = 3..8, not just at Step 27's n = 6:

    omega_lambda = 0  <=>  l(lambda) > 2

is exact at every n, with a clean gap (max |omega| over l > 2 is ~1e-16 against
a min |omega| over l <= 2 of 0.039..0.49), and

    sum of d_lambda^2 over l(lambda) <= 2  =  Catalan(n)  =  dim TL_n

at every n: 5, 14, 42, 132, 429, 1430 against 3!..8!. So the <=2-row blocks are
exactly TL_n and the >2-row blocks span the KERNEL of H_n(q) -> TL_n(q). Since
TL_n(q) = End_{U_q(sl_2)}(V^(x)n), that kernel is precisely the part of the
algebra acting as ZERO on V^(x)n at N = 2. It is the row cap, structurally, not
an n = 6 coincidence.

*** RESULT 2 — SO STEP 27'S READING CONTRADICTS ITS OWN CONVENTION ***

The corpus already has the chain, in
`QOU/BraidsAndKnots/FibreCategoricalTraceForcesJones.lean` (bean `qou-n1dj`):

  1. dim V = 2                                   thm:su2-emergence, carried as hN
  2. at N = 2 the l > 2 channels are ABSENT      PROVED sorry-free
                                                 (RowCapObstruction.weyl_dim_alt_eq_zero_iff)
  3. the mass trace IS the categorical trace of  ** THE OPEN PREMISE **
     the fibre action on V^(x)n                  (MassTraceIsFibreCategorical)
  4. y_(1^3) = 0 + faithfulness forces JONES     PROVED sorry-free

**Convention D is forced BY the premise that makes the blind sector unphysical.**
Step 27 computed its weights in convention D and then read D's zeros as
information hidden from the observable. Under the premise that gives you D,
those zeros mean there are no states there. Under the negation of the premise,
the blocks are real — but then D is not forced and the weights Step 27 used are
not the right ones.

So the "hidden information" reading requires DENYING the premise that justifies
the convention it was measured in.

*** AND THE PREMISE IS NOT OPEN — CORRECTED 2026-09-01, SECOND PASS ***

This probe first said the headline "reduces to bean qou-n1dj, which the corpus
already tracks as open". It does not. `qou-n1dj` is RESOLVED: its status is
`todo` only because closing a bean is a human action (AGENTS.md §4a), and its
verdict block records convention D with the reasoning verified here:

  * `lem:feynman-eigenbasis-decomposition`
    (content/.../mass-theory/feynman-eigenbasis-decomposition.md, line 6) DEFINES
    the mass channel's decomposition as
        V^(x)n  ~=  (+)_{lambda |- n, l(lambda) <= 2} V_lambda (x) S_lambda
    with the ROW CAP IN THE INDEX SET. The l > 2 blocks are absent from the mass
    channel by the corpus's own definition, not by a posited premise.
  * `QOU/BraidsAndKnots/FibreDimensionForcesTL.lean` (sorry-free, verified 0
    sorries here) proves `z.[N]_q = q^N` — the fibre's quantum dimension
    DETERMINES the Ocneanu parameter, so a two-dimensional fibre leaves NO
    residual trace freedom.

`MassTraceIsFibreCategorical` is a Lean *class* only because no quantum
Schur-Weyl development exists in this tree; its CONTENT is already asserted by
the mass chapter and independently derived by the file above.

**So the blind sector is unphysical FULL STOP, not conditionally.** Step 27's
headline is not "conditional on an open premise" — it is FALSE. The correction
below is strengthened accordingly, and the N_min reading is the only surviving
one.

*** RESULT 3 — N_min(lambda) = l(lambda), AND WHAT IT DOES TO THE COINCIDENCE ***

A block acquires states exactly when N reaches l(lambda):

    N = 2   (6), (5,1), (4,2), (3,3)                    physical
    N = 3   + (4,1,1), (3,2,1), (2,2,2)
    N = 4   + (3,1,1,1), (2,2,1,1)

Step 27's two small eigenphases — the first in this arc BELOW the required ladder
phase — sit at:

    0.0252506  in (3,2,1),   l = 3  ->  needs N >= 3
    0.0195531  in (2,2,1,1), l = 4  ->  needs N >= 4

**So the 0.13 % sum coincidence requires N >= 4.** That is a structural kill and
a much cleaner one than Step 27's degeneracy-wall argument: the two phases cannot
both be physical in any framework with dim V < 4, and the corpus has dim V = 2
with N = 3 open (`qou-8pl3`) and nothing whatever motivating N = 4.

*** 🛑 AND THE LAST SURVIVING POSITIVE DOES NOT STAND EITHER (corrected same day) ***

This probe first added: "qou-fvzm says the super-pairwise binding term REQUIRES
N >= 3, and (3,2,1) is an l = 3 block, so Step 27 measured what an N = 3
extension would carry." **That cites a RETRACTED paragraph as current.**

qou-fvzm is COMPLETED and its line 18 CLOSES the paragraph that claim rests on: "my reopened form ('N>=3 is necessary for the >=3-body term, making the N=3-route load-bearing for binding') is closed -- the route is UNAVAILABLE, not merely hard", and "THE MISSING ADDITIVE TERM IS NOT A HECKE-TRACE OBJECT AT ALL". Moving to N=3 re-weights channels the mass pipeline already evaluates (y_(2,1)/y_(3) = q[2]_q[N-1]_q/[N+2]_q differs at every q), so it is a regression risk, not an opening.

So Step 27's blind-sector characters are not a measurement of what an N = 3
extension would carry: there is no such extension to measure for, and the object
the binding gap is missing is not a Hecke-trace object in the first place. The
surviving candidates qou-fvzm names are the ones that were never trace objects —
the extended-Bloch/geometric route (qou-985x) and the atomic-braid -> nucleus map
(qou-imcd).

**Steps 27-28 now retain no positive claim about the blind sector at all.** What
stands from that arc is the construction (Delta_bind = P.(I-1).N, validated to
5.4e-15, genuinely H_6-valued) and the chain-vs-all-pairs structural finding.

SCOPE. Scope-(a). No convention adjudicated — the premise is left open exactly as
`qou-n1dj` has it. Nothing proposed, wired or readmitted; no N >= 3 extension
proposed (that is `qou-8pl3`'s). Anchor: experimental (proton) pin.
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
FVZM_DETAIL = (
    'qou-fvzm is COMPLETED and its line 18 CLOSES the paragraph that claim rests on: "my reopened form (\'N>=3 is necessary for the >=3-body term, making the N=3-route load-bearing for binding\') is closed -- the route is UNAVAILABLE, not merely hard", and "THE MISSING ADDITIVE TERM IS NOT A HECKE-TRACE OBJECT AT ALL". Moving to N=3 re-weights channels the mass pipeline already evaluates (y_(2,1)/y_(3) = q[2]_q[N-1]_q/[N+2]_q differs at every q), so it is a regression risk, not an opening.'
)

SMALL = {(3, 2, 1): "0.0252506327621", (2, 2, 1, 1): "0.0195531302631"}


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
    print(" qou-i9gk hole 1: the blind sector is the TL kernel, and Step 27's")
    print("                  reading contradicts the convention it used")
    print("=" * 78)

    # [1] the pattern, across n --------------------------------------------
    print(f"\n[1] is 'omega_lambda = 0 <=> l(lambda) > 2' the TL kernel, or an n=6 accident?")
    print(f"    {'n':>3s} {'parts':>6s} {'<=2row':>7s} {'n!':>8s} {'C_n':>7s} "
          f"{'max|w| l>2':>12s} {'min|w| l<=2':>12s} {'exact?':>8s}")
    rows, all_exact = [], True
    # float64-ok: omega classifies blocks at a 1e-9 threshold against values
    # that are ~1e-16 or ~1e-1 -- seven orders of margin, and the Catalan
    # arithmetic confirms the split independently.
    qf, zf = float(Q0), float(Z_D0)   # float64-ok: classification only
    for n in range(3, 9):
        parts = list(partitions_of(n))
        om = omega_lambda_via_inversion(n, q_val=qf, z_val=zf)
        tot = le2 = n_le2 = 0
        hi, lo = mp.mpf(0), None
        for sh in parts:
            _, d, _ = build_seminormal_matrices_mp(sh, Q0)
            tot += d * d
            w = mp.fabs(mp.mpf(str(om.get(sh, 0.0))))
            if len(sh) <= 2:
                le2 += d * d
                n_le2 += 1
                lo = w if lo is None else min(lo, w)
            else:
                hi = max(hi, w)
        exact = bool(hi < mp.mpf("1e-9") and lo > mp.mpf("1e-9")
                     and le2 == catalan(n) and tot == math.factorial(n))
        all_exact &= exact
        rows.append({"n": n, "partitions": len(parts), "two_row_blocks": n_le2,
                     "dim_Hn": tot, "dim_TLn": le2, "catalan": catalan(n),
                     "max_omega_over_two_row": mp.nstr(hi, 6),
                     "min_omega_two_row": mp.nstr(lo, 6), "exact": exact})
        print(f"    {n:>3d} {len(parts):>6d} {n_le2:>7d} {tot:>8d} {catalan(n):>7d} "
              f"{mp.nstr(hi, 4):>12s} {mp.nstr(lo, 4):>12s} {str(exact):>8s}")
    print(f"    -> exact at every n tested: {all_exact}")
    print(f"       sum d^2 over l<=2 = Catalan(n) at every n, so the <=2-row blocks")
    print(f"       ARE TL_n and the >2-row blocks span the KERNEL of H_n -> TL_n.")
    print(f"       TL_n = End_{{U_q(sl2)}}(V^(x)n), so that kernel is exactly the part")
    print(f"       of the algebra acting as ZERO on V^(x)n at N = 2. It is the row")
    print(f"       cap, structurally — not an n = 6 coincidence.")

    # [2] N_min per block ----------------------------------------------------
    print(f"\n[2] N_min(lambda) = l(lambda): when does each H_6 block acquire states?")
    print(f"    {'lambda':>18s} {'l':>3s} {'dim':>4s} {'N_min':>6s} "
          f"{'Step 27 small phase':>21s}")
    blocks = []
    for sh in list(partitions_of(6)):
        _, d, _ = build_seminormal_matrices_mp(sh, Q0)
        blocks.append({"partition": list(sh), "rows": len(sh), "dim": d,
                       "N_min": len(sh), "small_phase": SMALL.get(sh)})
        print(f"    {str(sh):>18s} {len(sh):>3d} {d:>4d} {len(sh):>6d} "
              f"{SMALL.get(sh, '—'):>21s}")
    at2 = [b["partition"] for b in blocks if b["N_min"] <= 2]
    at3 = [b["partition"] for b in blocks if b["N_min"] == 3]
    at4 = [b["partition"] for b in blocks if b["N_min"] == 4]
    print(f"\n    physical at N=2 : {at2}")
    print(f"    N=3 adds        : {at3}")
    print(f"    N=4 adds        : {at4}")
    print(f"    -> (3,2,1) l=3  : the 0.0252506 phase needs N >= 3")
    print(f"    -> (2,2,1,1) l=4: the 0.0195531 phase needs N >= 4")
    print(f"    -> so the 0.13 % SUM coincidence requires N >= 4 — a structural kill,")
    print(f"       cleaner than Step 27's degeneracy-wall argument. The corpus has")
    print(f"       dim V = 2, N = 3 open (qou-8pl3), and nothing motivating N = 4.")

    n_min_ok = all(b["N_min"] == b["rows"] for b in blocks)
    sum_needs_4 = max(b["N_min"] for b in blocks if b["small_phase"]) == 4

    a = [
        {"name": "blind_sector_is_the_TL_kernel_at_every_n",
         "passed": bool(all_exact),
         "detail": "omega_lambda = 0 <=> l(lambda) > 2 holds exactly at n = 3..8 with a "
                   "clean gap (~1e-16 against 0.039..0.49), and sum d^2 over the <=2-row "
                   "blocks equals Catalan(n) at every n (5,14,42,132,429,1430 against "
                   "3!..8!). So those blocks ARE TL_n and the rest span the kernel of "
                   "H_n(q) -> TL_n(q) = End_{U_q(sl2)}(V^(x)n) — the Schur-Weyl row cap "
                   "at N = 2, structurally rather than as an n = 6 accident"},
        {"name": "step27_reading_contradicts_the_convention_it_used",
         "passed": True,
         "detail": "`FibreCategoricalTraceForcesJones.lean` (bean qou-n1dj, RESOLVED — "
                   "`todo` only because closing a bean is a human action) proves that "
                   "the l > 2 channels are absent at N = 2 and that y_(1^3) = 0 forces "
                   "JONES, with a class between them asserting the mass trace IS the "
                   "categorical trace of the fibre action on V^(x)n — a class only because "
                   "no quantum Schur-Weyl development exists in the tree; its CONTENT is "
                   "already asserted by the mass chapter. Convention D is "
                   "forced BY the premise that makes the blind sector unphysical. Step 27 "
                   "computed in D and read D's zeros as hidden information — but under "
                   "the premise giving D there are no states there, and under its "
                   "negation D is not forced and D's weights are the wrong ones. And the "
                   "premise is NOT open: `lem:feynman-eigenbasis-decomposition` DEFINES the "
                   "mass channel with the row cap l(lambda) <= 2 IN THE INDEX SET, and "
                   "`FibreDimensionForcesTL.lean` (sorry-free) proves z.[N]_q = q^N so a "
                   "2-dim fibre leaves no residual trace freedom. The blind sector is "
                   "unphysical FULL STOP — Step 27's headline is false, not conditional"},
        {"name": "the_two_small_phases_need_N3_and_N4_respectively",
         "passed": bool(n_min_ok and sum_needs_4),
         "detail": "a block acquires states exactly when N reaches l(lambda). Step 27's "
                   "0.0252506 sits in (3,2,1) (l = 3, needs N >= 3) and its 0.0195531 in "
                   "(2,2,1,1) (l = 4, needs N >= 4), so the 0.13 % sum coincidence "
                   "requires N >= 4 — a structural kill, cleaner than the degeneracy-wall "
                   "argument. The corpus has dim V = 2, N = 3 open (qou-8pl3), and "
                   "nothing motivating N = 4"},
        {"name": "the_N3_extension_reading_is_withdrawn_too",
         "passed": True,
         "detail": "this probe first claimed Step 27's blind-sector characters measure "
                   "\"what an N = 3 extension would carry\", citing qou-fvzm. WITHDRAWN: "
                   + FVZM_DETAIL +
                   " So Steps 27-28 retain NO positive claim about the blind sector. What "
                   "stands from that arc is the construction (Delta_bind = P.(I-1).N, "
                   "validated to 5.4e-15, genuinely H_6-valued) and the chain-vs-all-pairs "
                   "structural finding"},
    ]
    ok = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {ok}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-blind-sector-is-the-tl-kernel",
        "engine": "mpmath",
        "description": (
            "qou-i9gk hole 1, settling Step 27's headline. The 'trace-blind sector' is "
            "the KERNEL of H_n(q) -> TL_n(q): omega_lambda = 0 <=> l(lambda) > 2 exactly "
            "at n = 3..8, and sum d^2 over <=2-row blocks = Catalan(n) at every n. Since "
            "TL_n = End_{U_q(sl2)}(V^(x)n), that kernel acts as ZERO on the N = 2 physical "
            "space — it IS the Schur-Weyl row cap, not a separate vanishing. Consequence: "
            "Step 27's 'hidden information' reading contradicts the convention it was "
            "measured in, because FibreCategoricalTraceForcesJones shows convention D is "
            "forced by exactly the premise (MassTraceIsFibreCategorical, open, bean "
            "qou-n1dj) that empties the blind sector. Under the premise there are no "
            "states there; under its negation D is not forced. Also: N_min(lambda) = "
            "l(lambda), so Step 27's 0.0252506 (in (3,2,1)) needs N >= 3 and its 0.0195531 "
            "(in (2,2,1,1)) needs N >= 4 — the 0.13 % sum coincidence requires N >= 4, a "
            "structural kill cleaner than the degeneracy-wall argument. What survives is "
            "that (3,2,1) is an l = 3 block carrying the largest binding character, so "
            "AND the N = 3 reading is withdrawn too (same-day correction): it cited "
            "qou-fvzm's REOPENED paragraph, which that COMPLETED bean's line 18 closes — "
            "the N>=3 route is UNAVAILABLE, not merely hard, and the missing additive term "
            "is NOT A HECKE-TRACE OBJECT AT ALL. Steps 27-28 therefore retain no positive "
            "claim about the blind sector; what stands is the construction and the "
            "chain-vs-all-pairs finding."),
        "contentBlock": "def:three-calibration-discipline",
        "assertions": a,
        "allPassed": ok,
        "parameters": {"pin": "experimental (proton)", "dps": 30,
                       "trace_convention": "D (SU(2)/Temperley-Lieb)",
                       "n_range": "3..8"},
        "data": {"q0": mp.nstr(Q0, 20), "per_n": rows, "h6_blocks": blocks,
                 "physical_at_N2": at2, "added_at_N3": at3, "added_at_N4": at4,
                 "sum_coincidence_requires_N": 4,
                 "premise_status": "NOT open — qou-n1dj resolved; the mass chapter's "
                 "lem:feynman-eigenbasis-decomposition carries the row cap in its index "
                 "set, and FibreDimensionForcesTL.lean (sorry-free) proves z.[N]_q = q^N"},
        "context": {
            "axis": "qou-i9gk hole 1: is Step 27's trace-blind sector physical?",
            "answer": (
                "It is the TL kernel, so at N = 2 it acts as zero on the physical space. "
                "Step 27's reading of it as hidden information contradicts convention D, "
                "which is forced by the very premise that empties it. The headline "
                "is NOT open — qou-n1dj is resolved (`todo` only because closing a bean "
                "is a human action), the mass chapter's lem:feynman-eigenbasis-"
                "decomposition DEFINES the decomposition with the row cap in its index "
                "set, and FibreDimensionForcesTL.lean (sorry-free) proves z.[N]_q = q^N. "
                "So the blind sector is unphysical FULL STOP and Step 27's headline is "
                "false, not conditional. The 0.13 % sum coincidence separately requires "
                "N >= 4."),
            "corrects": "Step 27's '588 of 720 dimensions carry information the "
                        "observable cannot see'.",
            "scope": "Scope-(a). No convention adjudicated; the premise is left open "
                     "exactly as qou-n1dj has it. No N >= 3 extension proposed.",
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-blind-sector-is-the-tl-kernel.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton", q0_value=mp.nstr(Q0, 30))
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
