#!/usr/bin/env python3
"""Route 25 -- the sum rule as a single dilogarithm TRACE equal to pi^2/2.

Bean `qou-0yqu`. Follows Route 24, which located the difficulty and pointed the
attack at explicit five-term functional equations. This route reformulates the
target into the shape those equations act on.

THE REFORMULATION
-----------------
The saddle condition is (1-y)^3 = y^2 (`cubic_iff_sq_eq_cube`, already Lean).
Taking logs, log(1-y) = (2/3) log y + (2 pi i/3) m for an integer m per
embedding. Feed that into the Rogers dilogarithm

    L(y) = Li2(y) + (1/2) log y log(1-y)   ->   Li2(y) + (1/3) log^2 y
                                                       + (pi i m/3) log y

and take the trace over the three embeddings of y (one real, one complex pair).
G3 finds that at m = -2 the trace is EXACTLY pi^2/2, to 120 dps, difference 0.0.

    sum_sigma [ Li2(sigma y) + (1/2) log(sigma y) * log(omega_sigma (1 - sigma y)) ]
        = pi^2 / 2

with omega = 1 on the real embedding and a primitive cube root of unity on the
complex pair. That is one clean equation where the Li2 form (Route 24 G4) needed
four terms -- pi^2, L^2, th^2 and pi*th all disappear into the trace.

⚠ WHAT THE OBJECT IS, AND IS NOT
--------------------------------
G4 is the honesty gate and it matters. m = -2 is **not** a branch of log(1-y1).
The principal branch has m = -1, so the legitimate branches are m = -1 + 3k, i.e.
m in {..., -4, -1, 2, ...}; m = -2 is not of that form. Measured: at m = -2,
exp(lg)/(1-y1) is exactly a primitive cube root of unity, arg = -2pi/3.

So this is Rogers L with 1-y twisted by omega -- NOT Rogers L. The twist is not
arbitrary: solving (1-y)^3 = y^2 for 1-y determines it only up to a cube root of
unity, and the clean value picks one of the three. But the object must be named
honestly, because "the Rogers-L trace is pi^2/2" would be FALSE. With genuine
Rogers L the trace is pi^2/2 - (2/3) pi th (G2), theta-dependent.

WHAT THIS DOES NOT DO
---------------------
G5: the reformulation is ALGEBRAICALLY equivalent to Route 24's closed form --
expanding Lambda in the {pi^2, L^2, th^2, pi*th} basis returns it identically. So
this is a repackaging, not new information, and it proves nothing. What it buys
is a target of the right SHAPE: a single trace equal to pi^2/2, which is what
five-term functional equations produce, and `rogersL_fiveTerm` is already a
sorry-free Lean theorem on this branch.

G6 flags a coincidence without claiming it: pi^2/2 is exactly the value of the
corpus's PROVED level-7 identity `extended_sum`. Different field (disc -23 here,
disc 49 there), so it cannot be the same identity.

G1 is the negative result that forces the trace framing: L(y_3) at the real root
alone is NOT a rational multiple of pi^2, and Li2(y_3) is not in the Q-span of
{pi^2, L^2}. The identity does not split into three; it is irreducibly a sum over
embeddings.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (arg, conj, exp, fabs, im, log, mp, mpf, nstr, pi, polylog,
                    polyroots, pslq, re)


def main() -> int:
    mp.dps = 120
    TOL = mpf(10) ** -95
    gates = []

    rts = polyroots([1, -2, 3, -1], maxsteps=2000, extraprec=6000)
    y3 = [r for r in rts if fabs(im(r)) < mpf(10) ** -90][0].real
    y1 = [r for r in rts if im(r) > mpf(10) ** -90][0]
    L, th = log(y3), arg(y1)
    I = polylog(2, y3) + 2 * re(polylog(2, y1))

    # ---- G1: the identity does NOT split -- the real root alone has no ladder
    Ly3 = polylog(2, y3) + log(y3) * log(1 - y3) / 2
    p1 = pslq([Ly3, pi ** 2], maxcoeff=10 ** 10, maxsteps=10 ** 6, tol=mpf(10) ** -100)
    p2 = pslq([Ly3, pi ** 2, L ** 2], maxcoeff=10 ** 8, maxsteps=10 ** 5, tol=TOL)
    p3 = pslq([polylog(2, y3), pi ** 2, L ** 2], maxcoeff=10 ** 8, maxsteps=10 ** 5, tol=TOL)
    gates.append({
        "gate": "G1",
        "claim": "the identity is IRREDUCIBLY a sum over embeddings: at the real root alone, "
                 "L(y_3) is not a rational multiple of pi^2 (PSLQ to coeff 1e10 at 120 dps "
                 "finds nothing), and Li2(y_3) is not in the Q-span of {pi^2, L^2}. So no "
                 "root-by-root ladder exists and the trace framing is forced",
        "L_y3": nstr(Ly3, 30), "L_y3_over_pi2": nstr(Ly3 / pi ** 2, 30),
        "pslq_L_pi2": p1, "pslq_L_pi2_L2": p2, "pslq_Li2_pi2_L2": p3,
        "pass": bool(p1 is None and p2 is None and p3 is None),
    })

    # ---- G2: the genuine Rogers-L trace, and it is theta-dependent ----------
    Lr = lambda z: polylog(2, z) + log(z) * log(1 - z) / 2
    tr_principal = re(Lr(y3) + Lr(y1) + Lr(conj(y1)))
    rel2 = pslq([tr_principal, pi ** 2, pi * th], maxcoeff=10 ** 8, maxsteps=10 ** 5, tol=TOL)
    rel2b = pslq([tr_principal, pi ** 2, pi * th, L ** 2, th ** 2],
                 maxcoeff=10 ** 8, maxsteps=10 ** 5, tol=TOL)
    gates.append({
        "gate": "G2",
        "claim": "with GENUINE Rogers L on principal branches the trace is pi^2/2 - (2/3) pi th "
                 "-- PSLQ gives [6,-3,4] on {tr, pi^2, pi*th}, and adding L^2, th^2 leaves their "
                 "coefficients ZERO. Already a simplification: the Li2 form needs four terms, "
                 "this needs two. But it is theta-dependent, so not yet a clean ladder",
        "trace_principal": nstr(tr_principal, 35),
        "pslq_2term": rel2, "pslq_4term": rel2b,
        "pass": bool(rel2 == [6, -3, 4] and rel2b is not None and rel2b[3] == 0
                     and rel2b[4] == 0),
    })

    # ---- G3: at m = -2 the trace is EXACTLY pi^2/2 --------------------------
    def trace_m(m):
        a = polylog(2, y3) + log(y3) * (mpf(2) / 3 * log(y3)) / 2
        lg = mpf(2) / 3 * log(y1) + (2j * pi / 3) * m
        return a + 2 * re(polylog(2, y1) + log(y1) * lg / 2)

    tbl = {m: nstr(re(trace_m(m)) - pi ** 2 / 2, 12) for m in range(-4, 3)}
    tm2 = re(trace_m(-2))
    rel3 = pslq([tm2, pi ** 2], maxcoeff=10 ** 10, maxsteps=10 ** 6, tol=mpf(10) ** -100)
    gates.append({
        "gate": "G3",
        "claim": "at m = -2 the trace is EXACTLY pi^2/2, to 120 dps (difference 0.0), and PSLQ "
                 "returns [-2,1]. Unique in m: the trace moves by (2/3) pi th per unit step, so "
                 "no other integer works. One clean equation where the Li2 form needed four terms",
        "trace_minus_pi2_over_2_by_m": tbl,
        "trace_at_m_eq_-2": nstr(tm2, 60),
        "pi2_over_2": nstr(pi ** 2 / 2, 60),
        "difference": nstr(fabs(tm2 - pi ** 2 / 2), 10),
        "pslq": rel3,
        "pass": bool(fabs(tm2 - pi ** 2 / 2) < mpf(10) ** -100 and rel3 == [-2, 1]),
    })

    # ---- G4: HONESTY -- m = -2 is not a branch of log(1-y) -----------------
    principal_m = re((3 * log(1 - y1) - 2 * log(y1)) / (2j * pi))
    twists = {}
    for m in [-4, -2, -1, 2]:
        lg = mpf(2) / 3 * log(y1) + (2j * pi / 3) * m
        r = exp(lg) / (1 - y1)
        twists[m] = {"ratio": nstr(r, 12), "abs": nstr(fabs(r), 8),
                     "arg_over_pi": nstr(arg(r) / pi, 8)}
    gates.append({
        "gate": "G4",
        "claim": "HONESTY GATE. m = -2 is NOT a branch of log(1-y1). The principal branch has "
                 "m = -1, so legitimate branches are m = -1 + 3k, i.e. {...,-4,-1,2,...}; -2 is "
                 "not of that form. At m = -2, exp(lg)/(1-y1) is a primitive CUBE ROOT OF UNITY "
                 "(arg = -2pi/3). So the object is Rogers L with 1-y twisted by omega, NOT "
                 "Rogers L -- the twist being exactly the ambiguity in solving (1-y)^3 = y^2 "
                 "for 1-y. Saying 'the Rogers-L trace is pi^2/2' would be FALSE",
        "principal_branch_m": nstr(principal_m, 10),
        "legitimate_m": "m = -1 + 3k",
        "exp_lg_over_one_minus_y1": twists,
        "pass": bool(fabs(principal_m + 1) < TOL
                     and fabs(fabs(exp(mpf(2) / 3 * log(y1) + (2j * pi / 3) * (-2))
                                   / (1 - y1)) - 1) < TOL
                     and fabs(arg(exp(mpf(2) / 3 * log(y1) + (2j * pi / 3) * (-2))
                                  / (1 - y1)) / pi + mpf(2) / 3) < TOL),
    })

    # ---- G5: it is a REPACKAGING, algebraically equivalent -----------------
    # Lambda-trace expanded in the {pi^2, L^2, th^2, pi*th} basis must reproduce
    # Route 24's closed form 6I = 3pi^2 - 3L^2 + 4th^2 - 8 pi th.
    predicted = I + L ** 2 / 2 - mpf(2) / 3 * th ** 2 + mpf(4) / 3 * pi * th
    gates.append({
        "gate": "G5",
        "claim": "this is a REPACKAGING, not new information: expanding the trace gives "
                 "I + L^2/2 - (2/3)th^2 + (4/3) pi th, and setting that to pi^2/2 returns Route "
                 "24's 6I = 3pi^2 - 3L^2 + 4th^2 - 8 pi th identically. It proves nothing. What "
                 "it buys is a target of the right SHAPE -- a single trace equal to pi^2/2, "
                 "which is what five-term functional equations produce",
        "expanded_trace": nstr(predicted, 40),
        "trace_at_m_eq_-2": nstr(tm2, 40),
        "diff": nstr(fabs(predicted - tm2), 10),
        "pass": bool(fabs(predicted - tm2) < mpf(10) ** -100),
    })

    # ---- G6: the constant coincides with the PROVED level-7 value ----------
    gates.append({
        "gate": "G6",
        "claim": "flagged, NOT claimed: pi^2/2 is exactly the value of the corpus's PROVED "
                 "level-7 identity `extended_sum` (sum_k (2L(w_k) + L(-w_k)) = pi^2/2). The "
                 "fields differ -- disc -23 here, disc 49 (totally real, cyclotomic) there -- so "
                 "it cannot be the same identity and the proved one cannot supply this one. "
                 "Recorded because a shared constant is worth a look, not because it is evidence",
        "this_trace": nstr(tm2, 30), "level7_extended_sum": nstr(pi ** 2 / 2, 30),
        "disc_here": -23, "disc_level7": 49,
        "same_identity": False,
        "pass": bool(fabs(tm2 - pi ** 2 / 2) < mpf(10) ** -100),
    })

    out = {
        "probe": "qbeta_5two_route25_rogers_trace",
        "bean": "qou-0yqu", "dps": mp.dps,
        "gates": gates,
        "verdict": {
            "reformulation": "sum over the three embeddings of [Li2(y) + (1/2) log y * "
                             "log(omega (1-y))] = pi^2/2 exactly, with omega = 1 on the real "
                             "embedding and a primitive cube root of unity on the complex pair. "
                             "One equation where the Li2 form needed four terms.",
            "what_the_object_is": "NOT Rogers L. m = -2 is not a branch of log(1-y) (legitimate "
                                  "branches are m = -1 + 3k); the ratio exp(lg)/(1-y) is a "
                                  "primitive cube root of unity. The twist is exactly the "
                                  "ambiguity in solving (1-y)^3 = y^2 for 1-y. With genuine "
                                  "Rogers L the trace is pi^2/2 - (2/3) pi th.",
            "does_not_prove_anything": "G5: algebraically equivalent to Route 24's closed form. "
                                       "A repackaging. Its value is the SHAPE -- a single trace "
                                       "equal to pi^2/2 is what five-term functional equations "
                                       "produce, and rogersL_fiveTerm is already Lean-proved here.",
            "why_a_trace_at_all": "G1: no root-by-root ladder exists -- L(y_3) is not a rational "
                                  "multiple of pi^2 and Li2(y_3) is not in span{pi^2, L^2}. The "
                                  "identity is irreducibly a sum over embeddings.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route25-rogers-trace.witness.json")
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
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: sum rule <=> a single twisted-Rogers trace = pi^2/2. Repackaging, not proof.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
