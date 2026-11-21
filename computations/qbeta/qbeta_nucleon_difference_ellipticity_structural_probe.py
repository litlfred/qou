#!/usr/bin/env python3
"""qou-cds1 Step 23: Delta_L's ellipticity is STRUCTURAL, not a word-choice artefact.

THE QUESTION. Step 22 found Delta_L = NF(n) - NF(p) elliptic in the (2,1) block
while Delta_S and the individual nucleon normal forms are hyperbolic. Is that a
property of the nucleons, or of the particular 11-crossing words?

Structural. Three independent lines say so, and the third is the one that matters.

1. WORD ORDERINGS. 8 of the 9 quark-word orderings of uud / udd give an elliptic
   difference. HONEST CAVEAT, stated because the raw count overstates it: the 9
   orderings collapse to only THREE distinct (tr, det) pairs, of which 2 are
   elliptic. So the counting evidence alone is weak.

2. RANDOM CONTROL. NF vectors resampled at matched scale give an elliptic
   difference 8.9 % of the time (4000 draws). The nucleon family is an order of
   magnitude enriched over its own null. Note this null is NOT the textbook
   Gaussian 1 - 1/sqrt(2) = 29 % for a generic real 2x2: the NF-vector-to-matrix
   map is not that ensemble, so the right baseline is the resampled one.

3. THE MECHANISM, which is what actually carries it. For traceless 2x2 matrices,

       det(A_0 - B_0) = det A_0 + det B_0 + tr(A_0 B_0)

   (Lean `det_sub_traceless`, by ring; verified numerically against the direct
   det of Delta_L's traceless part). A traceless real 2x2 is HYPERBOLIC when
   det < 0 and ELLIPTIC when det > 0, so the difference of two hyperbolic
   directions is elliptic exactly when their Killing pairing exceeds
   -(det A_0 + det B_0) -- i.e. when they are sufficiently ALIGNED. Measured:

       det A_0 (proton)  = -1.041656     hyperbolic
       det B_0 (neutron) = -1.056560     hyperbolic
       tr(A_0 B_0)       =  2.107175
       sum               =  0.0089591 > 0   => ELLIPTIC

   with the exact-parallel threshold 2*sqrt(det A_0 det B_0) = 2.098163. The
   neutron and proton traceless parts are aligned to within 0.43 % of parallel.
   THAT IS THE NEAR-DEGENERACY OF THE NUCLEONS (m_n - m_p = 1.29 MeV out of 939),
   not a property of any particular word.

4. ROBUST IN q. The discriminant tr^2 - 4det stays negative with NO sign change
   across q in [1.01, 1.61], varying smoothly from -0.0338 to -0.0448. So this is
   not fine-tuning at q_0. (A first reading of the 0.43 % alignment excess as a
   "thin margin" was wrong: the margin in the alignment is small, the margin in
   the discriminant is not, and the discriminant is what decides.)

AN OBSERVATION NOT CLAIMED AS A THEOREM. det rho(NF(p)) and det rho(NF(n)) agree
to 1.4e-16 relative (-1.0219724938077791 vs -1.0219724938077790). That looks like
an exact identity -- both nucleon words have 11 crossings -- but it is NOT proved
here and is not used in any argument above. Recorded as a plausible exact fact
for someone to settle.

WHAT THIS DOES AND DOES NOT SETTLE. It explains why an elliptic generator EXISTS
in the corpus, and that its existence is a fact about the nucleons rather than
about a word. It does NOT make it the right generator: the eigenphase is 2.020445
against a required 0.056595, a factor 35.7 (Step 22), and nothing here changes
that.

SCOPE. Scope-(a). Nothing derived, proposed, wired or readmitted; no convention
adjudicated; no c_k value asserted. Anchor: experimental (proton) pin.
LEAN: `QOU/QBeta/TracelessDifferenceEllipticity.lean`, sorry-free.
"""

import itertools
import json
import os
import random
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate"),
                str(HERE.parent / "hecke")]
import _path_bridge  # noqa: E402, F401

from hecke_characters import build_seminormal_matrices_mp  # noqa: E402
from hecke_core import build_nucleon_nf_mp  # noqa: E402
from q_parameter import q_at  # noqa: E402

mp.mp.dps = 30
Q0 = q_at(mp.mp.dps)
WORDS = [[], [0], [1], [0, 1], [1, 0], [0, 1, 0]]
H = Q0 - 1 / Q0


def basis(qv):
    g = build_seminormal_matrices_mp((2, 1), qv)[0]
    out = []
    for w in WORDS:
        M = mp.eye(2)
        for i in w:
            M = M * g[i]
        out.append(M)
    return out


BAS = basis(Q0)


def blk(v, bas=None):
    bas = bas or BAS
    M = mp.zeros(2, 2)
    for c, B in zip(v, bas):
        M = M + mp.mpf(c) * B
    return M


def tr(M):
    return M[0, 0] + M[1, 1]


def det(M):
    return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]


def traceless(M):
    t = tr(M) / 2
    return mp.matrix([[M[0, 0] - t, M[0, 1]], [M[1, 0], M[1, 1] - t]])


def nf(w):
    # mpf builder: `mp.mpf(str(build_nucleon_nf(...)))` reads a float64 as
    # exact at this file's dps.
    return build_nucleon_nf_mp(list(w), mp.mp.dps)


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" is Delta_L's ellipticity structural, or a word-choice artefact?")
    print("=" * 78)

    # ---- 1. word orderings --------------------------------------------
    P = sorted(set("".join(x) for x in itertools.permutations("uud")))
    N = sorted(set("".join(x) for x in itertools.permutations("udd")))
    print(f"\n[1] quark-word orderings   proton {P}   neutron {N}")
    print(f"    {'n - p':>12s}{'tr':>15s}{'det':>15s}{'tr^2-4det':>16s}  kind")
    ell = 0
    seen = set()
    for pw in P:
        for nw in N:
            d = [nf(nw)[i] - nf(pw)[i] for i in range(6)]
            M = blk(d)
            D = tr(M) ** 2 - 4 * det(M)
            e = D < 0
            ell += e
            seen.add((mp.nstr(tr(M), 12), mp.nstr(det(M), 12)))
            print(f"    {nw + ' - ' + pw:>12s}{mp.nstr(tr(M), 10):>15s}"
                  f"{mp.nstr(det(M), 10):>15s}{mp.nstr(D, 10):>16s}  "
                  f"{'ELLIPTIC' if e else 'real'}")
    print(f"    elliptic: {ell}/9   BUT only {len(seen)} DISTINCT (tr,det) pairs —")
    print(f"    the raw count overstates the evidence; the mechanism below carries it.")

    # ---- 2. random control --------------------------------------------
    random.seed(11)
    scale = [max(abs(x), abs(y)) for x, y in zip(nf("uud"), nf("udd"))]
    n_draw, hit = 4000, 0
    for _ in range(n_draw):
        v = [mp.mpf(random.uniform(-1, 1)) * s for s in scale]
        M = blk(v)
        hit += (tr(M) ** 2 - 4 * det(M)) < 0
    frac = mp.mpf(hit) / n_draw
    print(f"\n[2] random control, NF vectors resampled at matched scale, {n_draw} draws")
    print(f"    elliptic: {hit}/{n_draw} = {mp.nstr(frac * 100, 4)} %"
          f"   -> the nucleon family is ~{mp.nstr(mp.mpf(8) / 9 / frac, 4)}x enriched")

    # ---- 3. the mechanism ---------------------------------------------
    A, Bm = blk(nf("uud")), blk(nf("udd"))
    A0, B0 = traceless(A), traceless(Bm)
    dA, dB, cross = det(A0), det(B0), tr(A0 * B0)
    lhs, rhs = det(traceless(A - Bm)), dA + dB + cross
    par = 2 * mp.sqrt(dA * dB)
    print(f"\n[3] the mechanism — sl_2 geometry")
    print(f"    det A_0 (proton)  = {mp.nstr(dA, 12)}   hyperbolic: {dA < 0}")
    print(f"    det B_0 (neutron) = {mp.nstr(dB, 12)}   hyperbolic: {dB < 0}")
    print(f"    tr(A_0 B_0)       = {mp.nstr(cross, 12)}")
    print(f"    det A_0 + det B_0 + tr(A_0 B_0) = {mp.nstr(rhs, 12)}")
    print(f"    direct det(traceless(A - B))    = {mp.nstr(lhs, 12)}"
          f"   identity holds: {mp.fabs(lhs - rhs) < mp.mpf('1e-20')}")
    print(f"    exact-parallel threshold 2*sqrt(dA*dB) = {mp.nstr(par, 12)}")
    print(f"    alignment excess = {mp.nstr((cross / par - 1) * 100, 6)} %"
          f"   -> the nucleons are nearly the SAME sl_2 direction")

    # ---- 4. robustness in q -------------------------------------------
    print(f"\n[4] robustness in q")
    signs = []
    for i in range(0, 31):
        qv = mp.mpf(1) + mp.mpf(i) * mp.mpf("0.02") + mp.mpf("0.01")
        bs = basis(qv)
        Mq = blk([nf("udd")[j] - nf("uud")[j] for j in range(6)], bs)
        signs.append(tr(Mq) ** 2 - 4 * det(Mq))
    flips = sum(1 for i in range(1, len(signs)) if (signs[i] < 0) != (signs[i - 1] < 0))
    print(f"    q in [1.01, 1.61], 31 samples: discriminant from "
          f"{mp.nstr(signs[0], 8)} to {mp.nstr(signs[-1], 8)}")
    print(f"    sign changes: {flips}   -> not fine-tuning at q_0")

    # ---- an observation, not a claim ----------------------------------
    dp, dn = det(A), det(Bm)
    print(f"\n[5] OBSERVATION, not claimed as a theorem")
    print(f"    det rho(NF(p)) = {mp.nstr(dp, 20)}")
    print(f"    det rho(NF(n)) = {mp.nstr(dn, 20)}")
    print(f"    relative difference {mp.nstr(mp.fabs(dp - dn) / mp.fabs(dp), 4)}"
          f" — looks exact (both words are 11 crossings) but is NOT proved,")
    print(f"    and is NOT used in any argument above.")

    a = [
        {"name": "mechanism_identity_holds",
         "passed": bool(mp.fabs(lhs - rhs) < mp.mpf("1e-20")),
         "detail": f"det(A_0 - B_0) = det A_0 + det B_0 + tr(A_0 B_0): "
                   f"{mp.nstr(lhs, 12)} vs {mp.nstr(rhs, 12)} (Lean det_sub_traceless)"},
        {"name": "both_nucleon_directions_are_hyperbolic",
         "passed": bool(dA < 0 and dB < 0),
         "detail": f"det A_0 = {mp.nstr(dA, 10)}, det B_0 = {mp.nstr(dB, 10)} — so the "
                   "elliptic difference requires genuine ALIGNMENT, it is not free"},
        {"name": "nucleons_are_nearly_parallel_in_sl2",
         "passed": bool(cross > par and (cross / par - 1) < mp.mpf("0.05")),
         "detail": f"tr(A_0 B_0) = {mp.nstr(cross, 10)} against the exact-parallel "
                   f"{mp.nstr(par, 10)} — aligned to {mp.nstr((cross / par - 1) * 100, 5)} %. "
                   "This is the near-degeneracy of the nucleons"},
        {"name": "enriched_over_its_own_random_null",
         "passed": bool(frac < mp.mpf("0.2")),
         "detail": f"resampled NF differences are elliptic {mp.nstr(frac * 100, 4)} % of the "
                   f"time ({hit}/{n_draw}); the nucleon orderings give 8/9"},
        {"name": "counting_evidence_is_weaker_than_it_looks",
         "passed": bool(len(seen) < 9),
         "detail": f"the 9 orderings collapse to {len(seen)} distinct (tr,det) pairs, so 8/9 "
                   "overstates it — stated because it would be easy to quote the 8/9 alone"},
        {"name": "elliptic_across_the_whole_q_range_no_fine_tuning",
         "passed": bool(flips == 0 and all(s < 0 for s in signs)),
         "detail": f"discriminant negative at all 31 samples over q in [1.01,1.61], "
                   f"{flips} sign changes, smooth from {mp.nstr(signs[0], 6)} to "
                   f"{mp.nstr(signs[-1], 6)}"},
    ]
    ok = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {ok}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-nucleon-difference-ellipticity-structural",
        "engine": "mpmath",
        "description": (
            "qou-cds1 Step 23: Delta_L's ellipticity is STRUCTURAL, not an artefact of the "
            "11-crossing word choice. The mechanism is the traceless-2x2 identity "
            "det(A_0-B_0) = det A_0 + det B_0 + tr(A_0 B_0): both nucleon traceless parts "
            "are HYPERBOLIC (det -1.041656, -1.056560) and their Killing pairing 2.107175 "
            "exceeds the exact-parallel threshold 2*sqrt(dA dB) = 2.098163 by 0.43 %, so the "
            "difference is elliptic BECAUSE the neutron and proton are nearly the same sl_2 "
            "direction -- the near-degeneracy of the nucleons, not a word. Supported by: "
            "8/9 quark-word orderings elliptic (caveat: only 3 distinct values, so the count "
            "overstates it); a random control at matched scale giving 8.9 % (4000 draws), an "
            "order of magnitude below; and no sign change in the discriminant across "
            "q in [1.01,1.61], so no fine-tuning at q_0. Does NOT make it the right "
            "generator: the eigenphase stays a factor 35.7 from the ladder phase. Lean: "
            "QOU/QBeta/TracelessDifferenceEllipticity.lean, sorry-free."),
        "contentBlock": "def:three-calibration-discipline",
        "assertions": a,
        "allPassed": ok,
        "parameters": {"pin": "experimental (proton)", "dps": 30,
                       "lean": "QOU/QBeta/TracelessDifferenceEllipticity.lean",
                       "lean_theorems": ["det_sub_traceless",
                                         "sub_elliptic_iff_pairing_large",
                                         "threshold_pos_of_both_hyperbolic"],
                       "random_draws": n_draw, "random_seed": 11},
        "data": {
            "q0": mp.nstr(Q0, 20),
            "det_A0_proton": mp.nstr(dA, 14), "det_B0_neutron": mp.nstr(dB, 14),
            "killing_pairing": mp.nstr(cross, 14),
            "sum_equals_det_of_difference": mp.nstr(rhs, 14),
            "direct_det_traceless_difference": mp.nstr(lhs, 14),
            "parallel_threshold": mp.nstr(par, 14),
            "alignment_excess_pct": mp.nstr((cross / par - 1) * 100, 8),
            "orderings_elliptic": f"{ell}/9",
            "distinct_tr_det_pairs": len(seen),
            "random_elliptic_fraction_pct": mp.nstr(frac * 100, 6),
            "q_scan_discriminant_first": mp.nstr(signs[0], 10),
            "q_scan_discriminant_last": mp.nstr(signs[-1], 10),
            "q_scan_sign_changes": flips,
            "det_nucleon_nf_proton": mp.nstr(dp, 20),
            "det_nucleon_nf_neutron": mp.nstr(dn, 20),
            "det_relative_difference": mp.nstr(mp.fabs(dp - dn) / mp.fabs(dp), 6),
        },
        "context": {
            "axis": "qou-cds1: is Delta_L's ellipticity structural or a word artefact?",
            "answer": (
                "Structural. The difference of two hyperbolic sl_2 directions is elliptic "
                "exactly when they are aligned past 2*sqrt(dA dB), and the nucleons clear "
                "that by 0.43 % -- which IS their near-degeneracy. Robust in q, enriched "
                "10x over its own random null."),
            "not_claimed": (
                "that det rho(NF(p)) = det rho(NF(n)) exactly (they agree to 1.4e-16 "
                "relative and both words have 11 crossings, but it is not proved and not "
                "used); and NOT that Delta_L is the right generator -- the eigenphase "
                "remains a factor 35.7 from the ladder phase."),
            "scope": "Scope-(a). Nothing derived, proposed, wired or readmitted.",
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-nucleon-difference-ellipticity-structural.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton", q0_value=mp.nstr(Q0, 30))
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
