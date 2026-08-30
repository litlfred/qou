#!/usr/bin/env python3
"""Route 58 -- a complete proof path for the 5_2 sum rule from an ALREADY-PROVED
theorem, with four elementary links.

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap). Follows Routes
54-57.

**THE 5_2 SUM RULE REMAINS VERIFIED TO 80 DPS, UNPROVED.** Nothing here proves
it. What this probe does is exhibit a chain from a Lean theorem that IS proved to
the sum rule's stated closed form, and gate every link. Four links are still open.
They are elementary -- branch bookkeeping on inversion and the anharmonic group,
not analysis -- but open is open.

THE CHAIN
---------
Route 54 proved, sorry-free
(`FiveTwoComplexPentagon.pentagonSum_eq_pi_sq_div_two`): for real `a` in (0,1)
and any `w` off both cuts, the complex five-term sum is `pi^2/2`. It applies at
BOTH `(y_3, y_1)` and `(y_3, y_2)` -- the saddle cubic's real root against each
complex one -- since `y_3 = 0.4301597...` lies in (0,1). That is G1.

Adding the two instances and using `a_5 = 1/a_3` (Route 55) gives

    Sum_y L + L(y_3) + inv_a + inv_b + L(a_4) + L(b_4) = pi^2                (G2)

with `a_4 = 1 - y_3 y_1 = 1 - 1/y_2` and `b_4 = 1 - 1/y_1`. Four elementary
evaluations then collapse it:

    inv_a = L(a_3) + L(1/a_3)   = (pi^2 + pi*th)/6 + i*pi*log(y_3)/4         (G3)
    L(a_4) - L(y_2)             = (3 pi*th - pi^2)/6 - i*pi*log(y_3)/4       (G4)
    (and the conjugates), giving   Sum_y L = pi^2/2 - (2 pi/3) th            (G5)

which is Route 47's closed form -- until now a numerical observation. The bridge
to the sum rule is the branch equation `2 log y - 3 log(1-y) = 2 pi i eps`:

    Sum log y log(1-y) = log(y_3)^2 - (4/3) th^2 + (4 pi/3) th               (G6)

and `Sum_y L - A = (1/2) Sum log y log(1-y)` by definition, so

    A = -pi^2/6 - log(y_3)^2/2 + (2/3)(th - pi)^2                            (G7)

which is exactly the sum rule's stated target.

WHAT IS STILL OPEN (G8)
-----------------------
G3, G4, G6 and the angle identity `arg(a_3) = (pi - arg y_1)/3` are **not
proved** -- here or in Lean. Each is elementary: inversion `L(z) + L(1/z)`, the
anharmonic relation `L(1-1/z) - L(z)`, and the saddle branch equation, with their
branches pinned. None is deep. All four are open.

So the honest statement is: the analytic input this lane lacked for years is now
a theorem, and what separates it from the sum rule is branch bookkeeping on
elementary identities. **That is not a proof.**
"""

import json
import pathlib

from mpmath import (arg, conj, fabs, im, log, mp, mpc, mpf, nstr, pi, polylog,
                    polyroots, pslq, re)

SADDLE = [1, -2, 3, -1]


def rogersL(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def pentagon(x, y):
    d = 1 - x * y
    return [x, y, (1 - x) / d, d, (1 - y) / d]


def main() -> int:
    mp.dps = 60
    tol = mpf(10) ** -45
    gates = []

    roots = polyroots(SADDLE, maxsteps=1500, extraprec=8000)
    y3 = re([r for r in roots if fabs(im(r)) < tol][0])
    y1 = [r for r in roots if im(r) > tol][0]
    y2 = conj(y1)
    th, ly3 = arg(y1), log(y3)
    I = mpc(0, 1)

    A1, A2 = pentagon(y3, y1), pentagon(y3, y2)
    a3, a4, a5 = A1[2], A1[3], A1[4]
    b3, b4, b5 = A2[2], A2[3], A2[4]
    inv_a, inv_b = rogersL(a3) + rogersL(a5), rogersL(b3) + rogersL(b5)
    sum_y = sum(rogersL(z) for z in roots)
    A = re(sum(polylog(2, z) for z in roots))

    # ---- G1: the two PROVED instances --------------------------------------
    p1 = sum(rogersL(z) for z in A1)
    p2 = sum(rogersL(z) for z in A2)
    gates.append({
        "gate": "G1",
        "claim": "the starting point is PROVED, not assumed. Route 54's "
                 "FiveTwoComplexPentagon.pentagonSum_eq_pi_sq_div_two (Lean, sorry-free, standard "
                 "axioms) applies at BOTH (y_3,y_1) and (y_3,y_2), since y_3 = 0.4301597 lies in "
                 "(0,1) and y_1, y_2 are off both cuts. Both instances evaluate to pi^2/2",
        "y3": nstr(y3, 25), "y3_in_unit_interval": bool(0 < y3 < 1),
        "residual_at_y3_y1": nstr(fabs(p1 - pi ** 2 / 2), 8),
        "residual_at_y3_y2": nstr(fabs(p2 - pi ** 2 / 2), 8),
        "pass": bool(fabs(p1 - pi ** 2 / 2) < tol and fabs(p2 - pi ** 2 / 2) < tol
                     and 0 < y3 < 1),
    })

    # ---- G2: adding them, with a5 = 1/a3 -----------------------------------
    lhs = sum_y + rogersL(y3) + inv_a + inv_b + rogersL(a4) + rogersL(b4)
    gates.append({
        "gate": "G2",
        "claim": "adding the two instances and using a_5 = 1/a_3 (Route 55, exact and equivalent "
                 "to the cubic) gives Sum_y L + L(y_3) + inv_a + inv_b + L(a_4) + L(b_4) = pi^2, "
                 "with a_4 = 1 - y_3 y_1 = 1 - 1/y_2. Pure bookkeeping on G1 -- no new input",
        "a5_minus_inv_a3": nstr(fabs(a5 - 1 / a3), 8),
        "a4_minus_one_minus_inv_y2": nstr(fabs(a4 - (1 - 1 / y2)), 8),
        "residual": nstr(fabs(lhs - pi ** 2), 8),
        "pass": bool(fabs(lhs - pi ** 2) < tol and fabs(a5 - 1 / a3) < tol
                     and fabs(a4 - (1 - 1 / y2)) < tol),
    })

    # ---- G3: the inversion evaluation (OPEN) -------------------------------
    inv_pred = (pi ** 2 + pi * th) / 6 + I * pi * ly3 / 4
    ang = arg(a3)
    ang_rel = pslq([ang, th, pi], tol=tol, maxcoeff=10 ** 8, maxsteps=60000)
    gates.append({
        "gate": "G3",
        "claim": "LINK 1, OPEN. inv_a = L(a_3) + L(1/a_3) = (pi^2 + pi*th)/6 + i*pi*log(y_3)/4. "
                 "The log-squared terms cancel in an inversion pair, leaving only pi^2 and pi "
                 "times a log or an angle -- which is why the shape has no log^2. Rests on the "
                 "angle identity arg(a_3) = (pi - arg y_1)/3 and on |a_3|^2 = y_3. NOT PROVED, "
                 "here or in Lean; elementary but open",
        "inv_a": nstr(inv_a, 25),
        "predicted": nstr(inv_pred, 25),
        "residual_a": nstr(fabs(inv_a - inv_pred), 8),
        "residual_b": nstr(fabs(inv_b - conj(inv_pred)), 8),
        "arg_a3": nstr(ang, 25),
        "arg_a3_pslq_vs_[arg_y1, pi]": ang_rel,
        "arg_identity_residual": nstr(fabs(ang - (pi - th) / 3), 8),
        "abs_a3_sq_minus_y3": nstr(fabs(fabs(a3) ** 2 - y3), 8),
        "proved": False,
        "pass": bool(fabs(inv_a - inv_pred) < tol and fabs(inv_b - conj(inv_pred)) < tol
                     and fabs(ang - (pi - th) / 3) < tol),
    })

    # ---- G4: the anharmonic evaluation (OPEN) ------------------------------
    anh_pred = (3 * pi * th - pi ** 2) / 6 - I * pi * ly3 / 4
    gates.append({
        "gate": "G4",
        "claim": "LINK 2, OPEN. L(a_4) - L(y_2) = (3 pi*th - pi^2)/6 - i*pi*log(y_3)/4, i.e. the "
                 "anharmonic relation L(1 - 1/z) - L(z) with its branch pinned. Route 55 showed "
                 "y -> 1 - 1/y carries the saddle cubic onto X^3-X+1 as an identity of rational "
                 "functions, so this is that map read on L. NOT PROVED; elementary but open",
        "L_a4_minus_L_y2": nstr(rogersL(a4) - rogersL(y2), 25),
        "predicted": nstr(anh_pred, 25),
        "residual_a": nstr(fabs((rogersL(a4) - rogersL(y2)) - anh_pred), 8),
        "residual_b": nstr(fabs((rogersL(b4) - rogersL(y1)) - conj(anh_pred)), 8),
        "proved": False,
        "pass": bool(fabs((rogersL(a4) - rogersL(y2)) - anh_pred) < tol
                     and fabs((rogersL(b4) - rogersL(y1)) - conj(anh_pred)) < tol),
    })

    # ---- G5: Route 47's closed form, now DERIVED ---------------------------
    sl_derived = pi ** 2 / 2 - (2 * pi / 3) * th
    gates.append({
        "gate": "G5",
        "claim": "G2 + G3 + G4 collapse to Sum_y L = pi^2/2 - (2 pi/3) arg(y_1) -- Route 47's "
                 "closed form, until now a numerical observation with no derivation. It is now "
                 "the consequence of a PROVED theorem and two elementary links",
        "sum_y_L": nstr(re(sum_y), 32),
        "derived": nstr(sl_derived, 32),
        "residual": nstr(fabs(sum_y - sl_derived), 8),
        "pass": bool(fabs(sum_y - sl_derived) < tol),
    })

    # ---- G6: the bridge to A (OPEN) ----------------------------------------
    loglog = sum(log(z) * log(1 - z) for z in roots)
    loglog_pred = ly3 ** 2 - mpf(4) / 3 * th ** 2 + (4 * pi / 3) * th
    gates.append({
        "gate": "G6",
        "claim": "LINK 3, OPEN. Sum log y log(1-y) = log(y_3)^2 - (4/3) th^2 + (4 pi/3) th. This "
                 "follows from the saddle branch equation 2 log y - 3 log(1-y) = 2 pi i eps with "
                 "eps = (+1,-1,0), plus |y_1|^2 = 1/y_3: it reduces to (2/3) Sum log^2 y - "
                 "(2 pi i/3) Sum eps log y. NOT PROVED here; the integrality of eps IS a "
                 "sorry-free theorem on main (branch_data_of_cubic), the evaluation is not",
        "sum_log_log": nstr(re(loglog), 30),
        "predicted": nstr(loglog_pred, 30),
        "residual": nstr(fabs(loglog - loglog_pred), 8),
        "bridge_identity_residual": nstr(fabs((sum_y - A) - loglog / 2), 8),
        "proved": False,
        "pass": bool(fabs(loglog - loglog_pred) < tol
                     and fabs((sum_y - A) - loglog / 2) < tol),
    })

    # ---- G7: the sum rule's target, reached --------------------------------
    a_derived = sl_derived - loglog_pred / 2
    a_corpus = -pi ** 2 / 6 - ly3 ** 2 / 2 + mpf(2) / 3 * (th - pi) ** 2
    gates.append({
        "gate": "G7",
        "claim": "the chain reaches the sum rule's STATED target: A = -pi^2/6 - log(y_3)^2/2 + "
                 "(2/3)(th - pi)^2, the same expression the corpus already records. So the chain "
                 "is not a new statement -- it is a route to the existing one",
        "A_measured": nstr(A, 32),
        "A_from_chain": nstr(a_derived, 32),
        "A_corpus_target": nstr(a_corpus, 32),
        "residual_chain": nstr(fabs(A - a_derived), 8),
        "residual_corpus": nstr(fabs(A - a_corpus), 8),
        "pass": bool(fabs(A - a_derived) < tol and fabs(A - a_corpus) < tol),
    })

    # ---- G8: what is still open --------------------------------------------
    gates.append({
        "gate": "G8",
        "claim": "THE GATE THAT MATTERS. Links G3, G4, G6 and the angle identity arg(a_3) = "
                 "(pi - arg y_1)/3 are NOT PROVED, here or in Lean. Each is elementary -- "
                 "inversion, the anharmonic relation, and the saddle branch equation, with "
                 "branches pinned -- and none is deep, but open is open. The 5_2 sum rule is NOT "
                 "proved by this probe and must not be reported as proved",
        "open_links": ["inv_a evaluation (G3)", "arg(a_3) = (pi - arg y_1)/3 (G3)",
                       "L(1-1/z) - L(z) evaluation (G4)",
                       "Sum log y log(1-y) evaluation (G6)"],
        "proved_input": "FiveTwoComplexPentagon.pentagonSum_eq_pi_sq_div_two (Lean, sorry-free)",
        "sum_rule_proved": False,
        "pass": True,
    })

    out = {
        "probe": "qbeta_5two_route58_proof_path",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "follows": "Routes 54-57",
        "lean_input": "QOU/QBeta/FiveTwoComplexPentagon.lean -- pentagonSum_eq_pi_sq_div_two",
        "gates": gates,
        "verdict": {
            "chain": "the PROVED one-variable five-term identity, applied at (y_3,y_1) and "
                     "(y_3,y_2), plus four elementary evaluations, gives Route 47's closed form "
                     "and then the sum rule's stated target for A.",
            "open": "those four evaluations are not proved. They are branch bookkeeping on "
                    "inversion, the anharmonic relation and the saddle branch equation.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route58-proof-path.witness.json")
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
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:70]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "a complete chain from a PROVED Lean theorem to the sum rule's stated target for A, with "
        "four elementary links -- inversion, the anharmonic relation, an angle identity, and the "
        "saddle branch equation -- all verified numerically to ~1e-60 and NONE of them proved. "
        "The 5_2 sum rule remains verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
