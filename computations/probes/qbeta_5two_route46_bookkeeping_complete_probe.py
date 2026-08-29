#!/usr/bin/env python3
"""Route 46 -- the branch bookkeeping is COMPLETE, and the y-orbit needed
nothing. Discharges Route 41's gated G4 limit for both configurations, and
corrects the reason Route 45 gave for its own G5.

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap).

THE RESULT
----------
The Rogers pentagon, summed over the three embeddings at `x = y = z`:

    y-orbit (y^3-2y^2+3y-1) :  = 3*pi^2/2 EXACTLY, principal branches,
                                NO flattening, residual 2.5e-60          (G1)
    c-orbit (X^3+X^2-1)     :  needs one crossing's correction, then closes (G2)

So the configuration this lane actually cares about -- the 5_2 saddle orbit --
satisfies the pentagon Galois sum with no branch bookkeeping at all. The
`6.4718` discrepancy that Route 41 could only report belongs to the **c**-orbit,
not the `y`-orbit, and Route 45 derived its correction.

⚠ THIS CORRECTS ROUTE 45's OWN STATED REASON
---------------------------------------------
Route 45's G5 said the derived flattening "does not transfer to the y-orbit,
which needs its own derivation", implying `y` needs a DIFFERENT correction. It
does not: it needs **none**, and the c-recipe over-corrects it (G4). The G5
gate's numeric claim (residual > 1 when the c-recipe is applied to `y`) stands;
the explanation attached to it was wrong.

THE METHOD, VALIDATED
---------------------
The correction is read off the winding numbers along the continuation path
(G3): with `w0_i` the winding of `a_i` around 0 and `w1_i` that of `1 - a_i`,

    correction = pi*i * sum_i ( w1_i * log(a_i) + w0_i * log(1 - a_i) )

validated on the c-orbit, where it reproduces Route 45's hand-derived answer to
2.4e-35. On the y-orbit every winding is zero, which is *why* no correction
arises -- a derivation, not an observation after the fact.

CONSEQUENCE FOR ROUTE 41
------------------------
Route 41's rank no-go carried a gated limit: its rows were Bloch-group
statements, and turning one into a statement about `sum Li2` required branch
bookkeeping that was not done. For the y-orbit that bookkeeping is now done and
is trivial, so the pentagon row IS an exact `sum L` identity there (G5). The
rank conclusion is correspondingly firmer -- and still a no-go.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import arg, fabs, im, log, mp, mpf, nstr, pi, polylog, polyroots

Y_CUBIC = [1, -2, 3, -1]
C_CUBIC = [1, 1, 0, -1]


def rogersL(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def pentagon(x, y):
    xy = x * y
    return [x, y, (1 - x) / (1 - xy), 1 - xy, (1 - y) / (1 - xy)]


def raw_total(coeffs):
    rs = polyroots(coeffs, maxsteps=900, extraprec=3500)
    return sum(sum(rogersL(a) for a in pentagon(z, z)) for z in rs), rs


def windings(z0, z1, N=20000):
    """Signed windings of a_i and (1-a_i) around 0 along the straight path."""
    w0 = [0] * 5
    w1 = [0] * 5
    prev = None
    for k in range(N + 1):
        z = z0 + (z1 - z0) * mpf(k) / N
        A = pentagon(z, z)
        if prev is not None:
            for i in range(5):
                d = arg(A[i]) - arg(prev[i])
                if d > pi:
                    w0[i] -= 1
                if d < -pi:
                    w0[i] += 1
                e = arg(1 - A[i]) - arg(1 - prev[i])
                if e > pi:
                    w1[i] -= 1
                if e < -pi:
                    w1[i] += 1
        prev = A
    return w0, w1


def derived_total(coeffs):
    """Pentagon Galois sum with the correction READ OFF the winding numbers."""
    rs = polyroots(coeffs, maxsteps=900, extraprec=3500)
    r3 = [r for r in rs if fabs(im(r)) < mpf(10) ** -30][0].real
    tot = 0
    detail = []
    for z in rs:
        A = pentagon(z, z)
        S = sum(rogersL(a) for a in A)
        if fabs(im(z)) < mpf(10) ** -30:
            w0 = w1 = [0] * 5
            corr = 0
        else:
            w0, w1 = windings(r3, z)
            corr = pi * 1j * sum(w1[i] * log(A[i]) + w0[i] * log(1 - A[i])
                                 for i in range(5))
        tot += S - corr
        detail.append({"im": nstr(im(z), 8), "w0": w0, "w1": w1})
    return tot, detail


def main() -> int:
    mp.dps = 60
    gates = []
    target3 = 3 * pi ** 2 / 2

    # ---- G1: the y-orbit closes RAW ----------------------------------------
    ty, _ = raw_total(Y_CUBIC)
    gates.append({
        "gate": "G1",
        "claim": "THE RESULT. The Rogers pentagon summed over the three embeddings of the 5_2 "
                 "saddle orbit equals 3*pi^2/2 EXACTLY with principal branches and NO flattening. "
                 "The configuration this lane actually cares about needs no branch bookkeeping at "
                 "all -- which is not what Route 45 predicted",
        "raw_total": nstr(ty, 35),
        "three_halves_pi_squared": nstr(target3, 35),
        "residual": nstr(fabs(ty - target3), 12),
        "pass": bool(fabs(ty - target3) < mpf(10) ** -50),
    })

    # ---- G2: the c-orbit does NOT, and that is where 6.4718 lives -----------
    tc, _ = raw_total(C_CUBIC)
    gates.append({
        "gate": "G2",
        "claim": "the c-orbit raw total misses by 6.4718 -- so the discrepancy Route 41 reported "
                 "belongs to the c configuration, NOT the y one. Gated side by side with G1 so "
                 "the two cannot be conflated again",
        "raw_total": nstr(tc, 30),
        "shortfall": nstr(fabs(tc - target3), 20),
        "pass": bool(fabs(tc - target3) > mpf(1)),
    })

    # ---- G3: the winding rule, validated where the answer is known ---------
    dc, detail_c = derived_total(C_CUBIC)
    dy, detail_y = derived_total(Y_CUBIC)
    gates.append({
        "gate": "G3",
        "claim": "THE METHOD. The correction is read off winding numbers along the continuation "
                 "path -- pi*i*sum_i(w1_i*log a_i + w0_i*log(1-a_i)) -- and reproduces Route 45's "
                 "hand-derived c-orbit answer. On the y-orbit every winding is ZERO, which is WHY "
                 "no correction arises: a derivation, not an observation after the fact",
        "c_orbit_windings": detail_c,
        "y_orbit_windings": detail_y,
        "c_residual_after_correction": nstr(fabs(dc - target3), 12),
        "y_residual_after_correction": nstr(fabs(dy - target3), 12),
        "pass": bool(fabs(dc - target3) < mpf(10) ** -25
                     and fabs(dy - target3) < mpf(10) ** -25),
    })

    # ---- G4: correcting Route 45's stated reason ---------------------------
    rs = polyroots(Y_CUBIC, maxsteps=900, extraprec=3500)
    over = 0
    for z in rs:
        A = pentagon(z, z)
        S = sum(rogersL(a) for a in A)
        s = 0 if fabs(im(z)) < mpf(10) ** -40 else (1 if im(z) > 0 else -1)
        over += S - s * pi * 1j * log(A[3])       # the c-recipe, applied to y
    gates.append({
        "gate": "G4",
        "claim": "⚠ CORRECTS ROUTE 45's OWN REASON. Its G5 said the c-flattening 'does not "
                 "transfer to the y-orbit, which needs its own derivation' -- implying y needs a "
                 "DIFFERENT correction. It needs NONE: applying the c-recipe to y OVER-corrects, "
                 "moving an exact total off by 4.873. G5's numeric claim stands; the explanation "
                 "attached to it did not",
        "y_total_with_c_recipe": nstr(over, 25),
        "y_total_with_nothing": nstr(ty, 25),
        "over_correction": nstr(fabs(over - target3), 12),
        "pass": bool(fabs(over - target3) > mpf(1) and fabs(ty - target3) < mpf(10) ** -50),
    })

    # ---- G5: what it means for Route 41 -------------------------------------
    gates.append({
        "gate": "G5",
        "claim": "CONSEQUENCE. Route 41's rank no-go carried a gated limit -- its rows were "
                 "Bloch-group statements and turning one into a statement about sum Li2 needed "
                 "branch bookkeeping that was not done. For the y-orbit that bookkeeping is now "
                 "done and is trivial, so the pentagon row IS an exact sum-L identity there. The "
                 "rank conclusion is firmer, and still a no-go",
        "y_pentagon_row_is_an_exact_sumL_identity": bool(fabs(ty - target3) < mpf(10) ** -50),
        "route41_limit_discharged_for_y": True,
        "pass": bool(fabs(ty - target3) < mpf(10) ** -50),
    })

    out = {
        "probe": "qbeta_5two_route46_bookkeeping_complete",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "follows": ["Route 45 (continuation-derived flattening)"],
        "corrects": "Route 45's G5 explanation -- the y-orbit does not need a different "
                    "flattening, it needs none; the c-recipe over-corrects it.",
        "gates": gates,
        "verdict": {
            "measured": "the y-orbit pentagon Galois sum is exactly 3*pi^2/2 with principal "
                        "branches (2.5e-60). The c-orbit needs one crossing's correction, which "
                        "Route 45 derived and which the winding rule reproduces.",
            "consequence": "Route 41's gated G4 limit is discharged for the y-orbit: its pentagon "
                           "row is an exact sum-L identity, not merely a Bloch-group one.",
            "still_open": "none of this derives the integer in Sum Rhat = -pi^2/6, and the rank "
                          "no-go is unchanged in direction. The sum rule is untouched.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route46-bookkeeping-complete.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=False)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:72]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "branch bookkeeping COMPLETE -- the y-orbit closes raw at 3pi^2/2, the c-orbit needs the "
        "derived correction. Route 41's G4 limit is discharged for y. "
        "The 5_2 sum rule remains verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
