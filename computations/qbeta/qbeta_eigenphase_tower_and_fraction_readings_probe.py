#!/usr/bin/env python3
"""qou-cds1 Step 24: both readings of the 0.0566-vs-2.0204 gap are CLOSED.

Step 22 found Delta_L = NF(n) - NF(p) elliptic with eigenphase theta_eig =
2.0204450, against a required ladder phase theta_req = 0.0565947 -- a factor
35.70. Step 23 showed the ellipticity is structural (the nucleons are nearly
parallel in sl_2). Two readings could have closed the remaining gap. Neither does.

======================================================================
CHECK A -- does the phase differ in a HIGHER tower block?  NO, structurally.
======================================================================

Measured: across k = 3,4,5,6 and every partition, the ONLY distinct |arg| of a
complex eigenvalue of rho_lambda(Delta_L) anywhere in the tower is

    2.02044502

The blocks that have complex eigenvalues all have exactly that phase; the rest
are entirely real (the 1-dimensional ones, and the fully-symmetric/antisymmetric
rows). Dimensions range from 1 to 16 and nothing new appears.

THE REASON IS STRUCTURAL, not a numerical accident, and it is standard
representation theory rather than anything proved here: Delta_L is an element of
H_3, and an H_3 element acts on lambda|H_3 block-diagonally with respect to the
H_3-isotypic decomposition. So

    spec rho_lambda(x) = union over mu of spec rho_mu(x), with multiplicity
                         mult_mu(lambda restricted to H_3)

for every x in H_3. The tower can only REPEAT the H_3 spectrum; it cannot add to
it. Going up in k is therefore not a way to find a different phase for ANY
H_3-induced operator, and this reading is closed for the whole class rather than
just for Delta_L.

What that leaves open, and it is precisely what Step 22's correction opened: a
genuinely LEVEL-k operator, not induced from H_3. Nothing here touches that.

======================================================================
CHECK B -- is theta_req a FRACTION of theta_eig?  NO, and not close.
======================================================================

theta_eig / theta_req = 35.70022775 -- not an integer and not near one.

PRE-DECLARED candidate list, fixed before computing and reported in full
including every miss (11 and 22 because both nucleon words are 11-crossing):

    theta/2                    1.01022251     ratio to required 17.850
    theta/11 (per crossing)    0.18367682     ratio to required  3.2455
    theta/22                   0.09183841     ratio to required  1.6227   <- closest
    2*pi - theta               4.26274029     ratio to required 75.320
    pi - theta                 1.12114763     ratio to required 19.810
    theta - 2                  0.02044502     ratio to required  0.36125
    2*theta                    4.04089004     ratio to required 71.400

The closest is 62 % off. No search beyond this list was run.

AND THE NON-NUMEROLOGICAL VERSION, which is what actually settles it. theta_req
is not an intrinsic property of any operator -- it is (z-1)h/2 - u/2, a FUNCTION
OF z. So "is the ladder phase a fraction of the eigenphase" is really "what z
does the eigenphase correspond to?", and that is a derivation, not a search:

    (z-1)h/2 - u/2 = +theta_eig  ->  z =  20.3696
    (z-1)h/2 - u/2 = -theta_eig  ->  z = -18.2881
    admissible:                       z_D = 0.6127,  z_C = 0.4993

Off by a factor of about 33, and outside any admissible range in both directions.
The two phases are not related by a rational factor; they are quantities of
different magnitude living in different ranges.

======================================================================
WHERE THIS LEAVES THE ARC
======================================================================

Delta_L supplies a genuine elliptic generator (Step 22) whose ellipticity is a
fact about the nucleons (Step 23) -- but its phase is simply not the ladder's,
and neither tower level nor a rational factor bridges the gap. The elliptic
generator EXISTS and is NOT the one the ladder needs.

The one reading Step 22 opened and nothing since has touched: a genuinely
level-k operator that is not induced from H_3. Check A shows that is the ONLY
place in the tower a different phase could come from.

SCOPE. Scope-(a). Nothing derived, proposed, wired or readmitted; no convention
adjudicated; no c_k value asserted. The block-diagonal argument in Check A is
standard representation theory, cited not proved -- what is verified here is that
the tower's measured spectra are consistent with it across k = 3..6.
Anchor: experimental (proton) pin, per the 2026-08-07 directive.
"""

import json
import os
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

from hecke_characters import build_seminormal_matrices_mp, partitions_of  # noqa: E402
from hecke_core import build_nucleon_nf_mp  # noqa: E402
from q_parameter import q_at  # noqa: E402

mp.mp.dps = 30
Q0 = q_at(mp.mp.dps)
H = Q0 - 1 / Q0
HB = (Q0 - 1) / Q0
B_SUB = mp.sqrt((H ** 2 + 3) / (H ** 2 + 4))
U = B_SUB * HB ** 2
Z_C = mp.sqrt(Q0) / (1 + Q0)
Z_D = Q0 ** 3 / (Q0 ** 2 + 1)
TH_REQ = mp.fabs((Z_C - 1) * H / 2 - U / 2)
WORDS = [[], [0], [1], [0, 1], [1, 0], [0, 1, 0]]
# mpf builder, not `mp.mpf(str(build_nucleon_nf(...)))`: the float64 builder
# would put a 1e-16 floor under a difference of two nearly-equal vectors.
DL = [a - b for a, b in zip(build_nucleon_nf_mp(list("udd"), mp.mp.dps),
                            build_nucleon_nf_mp(list("uud"), mp.mp.dps))]


def blockmat(shape):
    g = build_seminormal_matrices_mp(tuple(shape), Q0)[0]
    d = g[0].rows
    M = mp.zeros(d, d)
    for c, w in zip(DL, WORDS):
        Bm = mp.eye(d)
        for i in w:
            Bm = Bm * g[i]
        M = M + c * Bm
    return M, d


def phases(M, d):
    if d == 1:
        return []
    for dps in (30, 80):
        try:
            with mp.workdps(dps):
                ev = mp.eig(M, left=False, right=False)
            return sorted({mp.nstr(mp.fabs(mp.arg(e)), 10) for e in ev
                           if abs(mp.im(e)) > mp.mpf(10) ** (-(dps // 2))})
        except Exception:
            continue
    return None


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" Step 24: both readings of the 0.0566-vs-2.0204 gap")
    print("=" * 78)

    print("\n[A] Delta_L's eigenphases across the tower\n")
    print(f"  {'k':>2s}{'lambda':>17s}{'dim':>5s}  distinct |arg| of complex eigenvalues")
    allph, failed, rows = set(), 0, {}
    for k in (3, 4, 5, 6):
        for shape in partitions_of(k):
            M, d = blockmat(shape)
            ph = phases(M, d)
            if ph is None:
                failed += 1
                print(f"  {k:>2d}{str(tuple(shape)):>17s}{d:>5d}  (eig failed)")
                continue
            allph.update(ph)
            rows[f"k{k}_{tuple(shape)}"] = {"dim": d, "phases": ph}
            print(f"  {k:>2d}{str(tuple(shape)):>17s}{d:>5d}  "
                  f"{ph if ph else '— all real —'}")
    print(f"\n  DISTINCT eigenphases anywhere in the tower: {sorted(allph)}")
    print(f"  eig failures: {failed}")
    print(f"  Reason (standard rep theory, cited not proved): Delta_L is an H_3")
    print(f"  element, so it acts block-diagonally on the H_3-isotypic decomposition")
    print(f"  of lambda|H_3. The tower REPEATS the H_3 spectrum; it cannot add to it.")
    print(f"  => going up in k cannot give a new phase for ANY H_3-induced operator.")

    th = mp.mpf(sorted(allph)[0])
    print(f"\n[B] is theta_req a fraction of theta_eig?")
    print(f"  theta_eig = {mp.nstr(th, 12)}   theta_req = {mp.nstr(TH_REQ, 12)}"
          f"   ratio = {mp.nstr(th / TH_REQ, 10)}")
    cands = [("theta/2", th / 2), ("theta/11 (per crossing)", th / 11),
             ("theta/22", th / 22), ("2*pi - theta", 2 * mp.pi - th),
             ("pi - theta", mp.pi - th), ("theta - 2", th - 2),
             ("2*theta", 2 * th)]
    print(f"  PRE-DECLARED list (fixed before computing, all reported):")
    best = None
    for nm, v in cands:
        r = v / TH_REQ
        off = mp.fabs(r - 1)
        if best is None or off < best[1]:
            best = (nm, off, v, r)
        print(f"    {nm:26s} = {mp.nstr(v, 12):>14s}   ratio {mp.nstr(r, 8)}")
    print(f"  closest: {best[0]} at ratio {mp.nstr(best[3], 8)}"
          f"  ({mp.nstr(best[1] * 100, 4)} % off)")

    zs = [1 + 2 * (U / 2 + s * th) / H for s in (1, -1)]
    print(f"\n  NON-NUMEROLOGICAL VERSION — what z does theta_eig correspond to?")
    print(f"    +theta_eig -> z = {mp.nstr(zs[0], 12)}")
    print(f"    -theta_eig -> z = {mp.nstr(zs[1], 12)}")
    print(f"    admissible: z_D = {mp.nstr(Z_D, 10)}, z_C = {mp.nstr(Z_C, 10)}")
    print(f"    off by ~{mp.nstr(zs[0] / Z_D, 5)}x and outside any admissible range.")

    a = [
        {"name": "one_eigenphase_only_across_the_whole_tower",
         "passed": bool(len(allph) == 1 and failed == 0),
         "detail": f"the only distinct |arg| anywhere in k=3..6 is {sorted(allph)[0]}, in "
                   f"blocks of dimension 1..16, with {failed} eig failures — the tower "
                   "repeats the H_3 spectrum and adds nothing"},
        {"name": "higher_blocks_cannot_carry_a_new_phase_for_H3_induced_operators",
         "passed": bool(len(allph) == 1),
         "detail": "structural: an H_3 element acts block-diagonally on the H_3-isotypic "
                   "decomposition, so spec at level k is the H_3 spec with multiplicity. "
                   "Standard rep theory, cited not proved; the measurement is consistent "
                   "with it at every block"},
        {"name": "no_declared_fraction_lands",
         "passed": bool(best[1] > mp.mpf("0.5")),
         "detail": f"closest of 7 pre-declared candidates is {best[0]} at ratio "
                   f"{mp.nstr(best[3], 6)}, {mp.nstr(best[1] * 100, 4)} % off. No search "
                   "beyond the declared list"},
        {"name": "eigenphase_read_as_a_ladder_phase_needs_inadmissible_z",
         "passed": bool(zs[0] > 10 and zs[1] < -10),
         "detail": f"z = {mp.nstr(zs[0], 8)} or {mp.nstr(zs[1], 8)} against admissible "
                   f"z_D = {mp.nstr(Z_D, 8)}, z_C = {mp.nstr(Z_C, 8)} — the two phases are "
                   "not related by a rational factor, they live in different ranges"},
        {"name": "both_readings_closed_elliptic_generator_is_not_the_ladders",
         "passed": bool(len(allph) == 1 and best[1] > mp.mpf("0.5")),
         "detail": "Delta_L supplies a genuine elliptic generator whose ellipticity is a "
                   "fact about the nucleons (Step 23), but its phase is not the ladder's "
                   "and neither tower level nor a rational factor bridges the gap"},
    ]
    ok = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {ok}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-eigenphase-tower-and-fraction-readings",
        "engine": "mpmath",
        "description": (
            "qou-cds1 Step 24: both readings of the 0.0566-vs-2.0204 gap are CLOSED. "
            "CHECK A -- across k=3..6 and every partition, the ONLY distinct |arg| of a "
            "complex eigenvalue of rho_lambda(Delta_L) is 2.02044502, in blocks of "
            "dimension 1..16. The reason is structural and is standard representation "
            "theory: an H_3 element acts block-diagonally on the H_3-isotypic decomposition "
            "of lambda|H_3, so the tower REPEATS the H_3 spectrum and cannot add to it -- "
            "closing this reading for every H_3-induced operator, not just Delta_L. "
            "CHECK B -- theta_eig/theta_req = 35.700, not an integer; seven pre-declared "
            "fraction candidates all miss, the closest (theta/22) by 62 %. The "
            "non-numerological version settles it: theta_req is (z-1)h/2 - u/2, a function "
            "of z, so reading theta_eig as a ladder phase requires z = 20.37 or -18.29 "
            "against admissible z_D = 0.6127, z_C = 0.4993 -- different ranges, not a "
            "rational factor. What remains open is the one thing Step 22's correction "
            "opened: a genuinely level-k operator not induced from H_3."),
        "contentBlock": "def:three-calibration-discipline",
        "assertions": a,
        "allPassed": ok,
        "parameters": {"pin": "experimental (proton)", "dps": 30,
                       "declared_candidates": [c[0] for c in cands],
                       "anti_fit": "candidate list fixed before computing; all reported"},
        "data": {
            "q0": mp.nstr(Q0, 20), "theta_eig": mp.nstr(th, 14),
            "theta_required": mp.nstr(TH_REQ, 14),
            "ratio": mp.nstr(th / TH_REQ, 12),
            "distinct_tower_phases": sorted(allph),
            "eig_failures": failed,
            "per_block": rows,
            "declared_candidates": {nm: {"value": mp.nstr(v, 12),
                                         "ratio_to_required": mp.nstr(v / TH_REQ, 10)}
                                    for nm, v in cands},
            "closest_candidate": best[0],
            "z_from_eigenphase": [mp.nstr(zs[0], 12), mp.nstr(zs[1], 12)],
            "z_D": mp.nstr(Z_D, 12), "z_C": mp.nstr(Z_C, 12),
        },
        "context": {
            "axis": "qou-cds1: can tower level or a rational factor bridge 0.0566 vs 2.0204?",
            "answer": (
                "Neither. The tower carries exactly one eigenphase for any H_3-induced "
                "operator (block-diagonal on the isotypic decomposition), and reading the "
                "eigenphase as a ladder phase requires an inadmissible z ~ 20.4 or -18.3. "
                "The elliptic generator exists and is not the ladder's."),
            "leaves_open": (
                "a genuinely level-k operator not induced from H_3 — the one thing Step 22's "
                "correction opened, and by Check A the only place in the tower a different "
                "phase could come from."),
            "scope": ("Scope-(a). The block-diagonal argument is standard rep theory, cited "
                      "not proved; what is verified is that the measured spectra agree with "
                      "it at every block k=3..6. Nothing derived, proposed or wired."),
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-eigenphase-tower-and-fraction-readings.witness.json"
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
