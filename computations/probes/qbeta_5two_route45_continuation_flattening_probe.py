#!/usr/bin/env python3
"""Route 45 -- the flattening DERIVED by analytic continuation, not searched.
Closes Route 41's gated G4 branch-bookkeeping gap for the c-orbit, and shows by
an off-configuration check that the result does not transfer to the y-orbit.

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap). Follows Routes 43
and 44.

THE METHOD
----------
Route 44 established that flattenings form a torsor modulo the branch relation,
so no tuple is "the" flattening and searching for one was the wrong move. The
right move is to DERIVE it: the Rogers pentagon is an exact analytic identity in
two complex variables (G1), so continuing it from a real embedding -- where it
holds with principal branches and no correction -- to a complex one, and
tracking which argument crosses which cut, produces the flattening with no
search at all.

WHAT IT GIVES
-------------
Along the straight path from the real embedding of `c` to a complex one, exactly
one crossing occurs: `1 - a_4 = x*y` winds once around 0, so `log(1 - a_4)`
jumps (G2). The correction that restores the identity is

    subtract  s * pi*i * log(a_4)      a_4 = 1 - x*y,  s = sign(Im z)

i.e. `q = 2*s` on the fourth pentagon argument and nothing elsewhere. With it,
all three embeddings of the c-orbit close to 2e-50 and total exactly `3*pi^2/2`
(G4). **That closes Route 41's G4 gap: the 6.4718 discrepancy is exactly
`2*Re(pi*i*log(1 - c_1^2))`.**

⚠ TWO THINGS THIS SESSION GOT WRONG FIRST, BOTH GATED
------------------------------------------------------
1. **The compensation is a VARYING FUNCTION, not a constant.** A first pass
   modelled the crossing as a one-off step and subtracted the jump as a
   constant, leaving 3.379 (G3). After a crossing, principal branches differ
   from the continuation by `-pi*i*log(a_4(t))`, which keeps moving with `t` --
   which is why the sum drifts *after* the jump rather than stepping once. A
   jump detector with a hardcoded threshold (`|d| > 1`) also reported ZERO
   jumps, because this one has magnitude 0.35.
2. **It does NOT transfer.** Applying the same flattening to the y-orbit -- the
   configuration this lane actually cares about -- leaves a residual of 4.873
   (G5). Each configuration's continuation crosses different cuts, exactly as
   Route 44's torsor structure predicts, so the y-orbit needs its own
   derivation. Checked off the configuration it was derived on, which is the
   only reason it was caught.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import fabs, im, log, mp, mpf, nstr, pi, polylog, polyroots, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

C_CUBIC = [1, 1, 0, -1]        # c^3 + c^2 - 1, the generator c = 1/rho
Y_CUBIC = [1, -2, 3, -1]       # the 5_2 saddle cubic


def rogersL(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def pentagon(x, y):
    xy = x * y
    return [x, y, (1 - x) / (1 - xy), 1 - xy, (1 - y) / (1 - xy)]


def emb_sign(z):
    if fabs(im(z)) < mpf(10) ** -40:
        return 0
    return 1 if im(z) > 0 else -1


def flattened_pentagon(z):
    """Pentagon sum at x = y = z with the continuation-derived flattening."""
    A = pentagon(z, z)
    S = sum(rogersL(a) for a in A)
    return S - emb_sign(z) * pi * 1j * log(A[3])


def orbit(coeffs):
    return polyroots(coeffs, maxsteps=800, extraprec=3000)


def main() -> int:
    set_compute_dps()
    gates = []
    target = pi ** 2 / 2

    # ---- G1: the pentagon is an exact ANALYTIC identity ---------------------
    pts = [(mpf(3) / 10, mpf(4) / 10),
           (mpf(3) / 10 + mpf(1) / 10 * 1j, mpf(4) / 10 + mpf(1) / 20 * 1j),
           (mpf(3) / 10 + mpf(1) / 2 * 1j, mpf(2) / 10 - mpf(4) / 10 * 1j)]
    worst = max(fabs(sum(rogersL(a) for a in pentagon(X, Y)) - target) for X, Y in pts)
    gates.append({
        "gate": "G1",
        "claim": "the Rogers pentagon is an exact identity in two COMPLEX variables, not merely "
                 "on the real square -- which is what licenses deriving the flattening by "
                 "analytic continuation instead of searching for it",
        "worst_residual_over_real_and_complex_points": nstr(worst, 12),
        "pass": bool(worst < mpf(10) ** -28),
    })

    # ---- G2: exactly one crossing on the path, and it is log(1 - a_4) -------
    C = orbit(C_CUBIC)
    c3 = [r for r in C if fabs(im(r)) < mpf(10) ** -40][0].real
    c1 = [r for r in C if im(r) > 0][0]
    N = 4000
    prev = None
    jumps = []
    for k in range(N + 1):
        z = c3 + (c1 - c3) * mpf(k) / N
        A = pentagon(z, z)
        S = sum(rogersL(a) for a in A)
        if prev is not None and fabs(S - prev[0]) > mpf(1) / 100:
            jumps.append({"t": nstr(mpf(k) / N, 8),
                          "delta": nstr(S - prev[0], 14),
                          "minus_pi_i_log_a4": nstr(-pi * 1j * log(A[3]), 14)})
        prev = (S, A)
    gates.append({
        "gate": "G2",
        "claim": "exactly ONE branch crossing occurs on the straight path from the real embedding "
                 "of c to a complex one, and the jump equals -pi*i*log(a_4) at that point -- the "
                 "signature of log(1-a_4) = log(x*y) crossing its cut. ⚠ A hardcoded threshold "
                 "of |d| > 1 reported ZERO jumps here, because this jump has magnitude 0.35; the "
                 "threshold must be scaled to the smooth step, not guessed",
        "jumps": jumps,
        "n_jumps": len(jumps),
        "pass": bool(len(jumps) == 1),
    })

    # ---- G3: the compensation is a VARYING function, not a constant ---------
    A_end = pentagon(c1, c1)
    S_end = sum(rogersL(a) for a in A_end)
    # the constant model subtracts the jump as measured AT the crossing point,
    # which is the plausible-and-wrong thing to do:
    zc = c3 + (c1 - c3) * mpf(jumps[0]["t"]) if jumps else c1
    A_cross = pentagon(zc, zc)
    const_model = S_end + pi * 1j * log(A_cross[3])
    varying = S_end - pi * 1j * log(A_end[3])
    gates.append({
        "gate": "G3",
        "claim": "THE CORRECTION SO NEARLY MISSED. Modelling the crossing as a one-off step and "
                 "subtracting the jump as a CONSTANT leaves a large residual; the true "
                 "compensation is -pi*i*log(a_4(t)), a function that keeps moving after the "
                 "crossing. That is why the sum drifts smoothly AFTER the jump instead of "
                 "stepping once, and why the constant model looks plausible and is wrong",
        "constant_model_residual": nstr(fabs(const_model - target), 12),
        "varying_model_residual": nstr(fabs(varying - target), 12),
        "pass": bool(fabs(varying - target) < mpf(10) ** -40
                     and fabs(const_model - target) > mpf(1)),
    })

    # ---- G4: the c-orbit closes -- Route 41's G4 gap is closed --------------
    tot_c = sum(flattened_pentagon(z) for z in C)
    gap = 2 * re(pi * 1j * log(pentagon(c1, c1)[3]))
    gates.append({
        "gate": "G4",
        "claim": "ROUTE 41'S G4 GAP IS CLOSED for the c-orbit. With the continuation-derived "
                 "flattening (q = 2*sign(Im z) on a_4, zero elsewhere) all three embeddings close "
                 "and total exactly 3*pi^2/2. The 6.4718 discrepancy Route 41 could only report "
                 "is exactly 2*Re(pi*i*log(1 - c_1^2)) -- an identified quantity now, not a gap",
        "total": nstr(tot_c, 30),
        "three_halves_pi_squared": nstr(3 * target, 30),
        "residual": nstr(fabs(tot_c - 3 * target), 12),
        "route41_gap_identified_as": nstr(gap, 20),
        "pass": bool(fabs(tot_c - 3 * target) < mpf(10) ** -40),
    })

    # ---- G5: it does NOT transfer to the y-orbit ----------------------------
    Y = orbit(Y_CUBIC)
    tot_y = sum(flattened_pentagon(z) for z in Y)
    gates.append({
        "gate": "G5",
        "claim": "THE OFF-CONFIGURATION CHECK, and it fails as Route 44 predicts. The same "
                 "flattening applied to the y-orbit -- the configuration this lane actually cares "
                 "about -- leaves a residual of 4.873. Each configuration's continuation crosses "
                 "different cuts, so the y-orbit needs its own derivation; the c-orbit result is "
                 "a method validated, not a general flattening",
        "total_on_y_orbit": nstr(tot_y, 25),
        "three_halves_pi_squared": nstr(3 * target, 25),
        "residual": nstr(fabs(tot_y - 3 * target), 12),
        "pass": bool(fabs(tot_y - 3 * target) > mpf(1)),
    })

    out = {
        "probe": "qbeta_5two_route45_continuation_flattening",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "follows": ["Route 43 (flattened Rogers)", "Route 44 (the torsor)"],
        "closes": "qou-0yqu Route 41's gated G4 branch-bookkeeping gap, for the c-orbit: the "
                  "6.4718 discrepancy is exactly 2*Re(pi*i*log(1 - c_1^2)).",
        "gates": gates,
        "verdict": {
            "method": "the flattening is DERIVED by analytic continuation from a real embedding, "
                      "not searched: the pentagon is an exact identity in two complex variables, "
                      "so tracking which argument crosses which cut produces the correction.",
            "result": "for the c-orbit the correction is q = 2*sign(Im z) on a_4 = 1-xy, and the "
                      "three embeddings then total exactly 3*pi^2/2 (residual 2e-50).",
            "limit": "it does NOT transfer to the y-orbit (residual 4.873). Consistent with "
                     "Route 44's torsor structure -- each configuration needs its own "
                     "continuation. The y-orbit derivation is the next step.",
            "method_traps": "a constant-compensation model of the crossing is wrong (the "
                            "correction is a varying function), and a hardcoded jump threshold "
                            "of |d| > 1 misses a jump of magnitude 0.35 entirely.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route45-continuation-flattening.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:72]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "the flattening is derivable by continuation and Route 41's G4 gap is CLOSED for the "
        "c-orbit (6.4718 = 2 Re(pi i log(1-c_1^2))). It does not transfer to the y-orbit, which "
        "needs its own derivation. The 5_2 sum rule remains verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
