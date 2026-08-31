#!/usr/bin/env python3
"""qbeta_d_frame_two_block_forced_weights_probe.py — under D the decay weights
are FORCED, not fitted: two surviving blocks, two constraints, one solution.

BEAN `qou-cds1`. The re-derivation is stuck at "a genuinely new form is needed".
Everything tried so far has been `admissible base x one multiplicative
correction`, and 2026-08-29 measured that whole class as a negative. This probe
changes the SHAPE of the question rather than searching the same class again.

THE COUNTING ARGUMENT, which is the entire content of this probe.

Under convention D the Wenzl two-row cap annihilates the three-row block:
`y_(1^3)(z_D) = 0` (QOU.QBeta.AdmissibleRoots). So the D-frame trace of the
decay element has exactly TWO free block weights, not three:

    tr^D(Delta_S) = y_3 * chi^(3)(Delta_S) + y_21 * chi^(2,1)(Delta_S)

And there are exactly TWO constraints available without fitting anything:

    (1) NORMALISATION   sum_lambda dim_lambda * y_lambda = 1
                        => y_3 + 2*y_21 = 1        (dims 1, 2, 1; y_111 = 0)
    (2) THE ANCHOR      tr^D(Delta_S) = T_required, the trace value that
                        reproduces the CODATA Q-value, given base ∝ tr_M(Delta_S)
                        (verified to 1.3e-11 in the 08-29 audit)

Two equations, two unknowns, unique solution. **There is no free parameter to
fit.** That is what makes this different from the correction search: it does not
propose a correction at all, it asks what the block weights would have to BE,
and the answer is forced.

The question this then poses -- and it is a question, not a claim -- is whether
the forced pair (y_3*, y_21*) is a RECOGNISABLE q-rational, or noise.

ANTI-FIT DISCIPLINE, since "recognisable" is exactly where a fit hides. The
comparison list is declared as a module constant BELOW, BEFORE any solving, and
is short and principled: the Markov D pair itself, the two other admissible
evaluations, and the handful of q-rationals the corpus already uses for block
weights. A match counts only if it is isolated by an order of magnitude. If the
nearest candidate is merely nearest, that is a basket coincidence and the
verdict is a scope-(a) negative -- which is a real result here, because the
counting argument says nothing else in this class is available.

WHAT THIS IS NOT. It does not derive Q_beta. It does not wire anything. If the
forced pair is unrecognisable, the two-block route is closed the same way the
correction route is, and that CLOSES a class rather than opening one.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp
from mpmath import mp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    BASIS, N, basis_vec, reg_char, length, q, h,
)
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 60

# From the 2026-08-29 admissible-base correction search (self-test targets).
F_REQUIRED_TRM = mp.mpf("1.75923699054610623")
F_REQUIRED_AUG = mp.mpf("0.88912581036021176")


def candidate_forms(qs):
    """DECLARED BEFORE SOLVING. Short, principled, and closed.

    The Markov D pair, the other admissible evaluation, and the q-rationals the
    corpus already uses as H_3 block weights. Nothing is added after seeing the
    answer; adding one later would make this a fit.
    """
    return {
        "y_3^D = (q^4+1)/(q^2+1)^2": (qs ** 4 + 1) / (qs ** 2 + 1) ** 2,
        "y_21^D = q^2/(q^2+1)^2": qs ** 2 / (qs ** 2 + 1) ** 2,
        "1/[2]_q^2": 1 / (qs + 1 / qs) ** 2,
        "1/[2]_q": 1 / (qs + 1 / qs),
        "1/[3]_q": 1 / (qs ** 2 + 1 + 1 / qs ** 2),
        "1/2": sp.Rational(1, 2),
        "1/3": sp.Rational(1, 3),
        "1/4": sp.Rational(1, 4),
        "q^2/(q^4+1)": qs ** 2 / (qs ** 4 + 1),
        "(q^4+1)/(q^2+1)^2 at 1/q": (qs ** -4 + 1) / (qs ** -2 + 1) ** 2,
    }


def main() -> int:
    ok = True
    checks = []

    def check(name, passed, detail=""):
        nonlocal ok
        ok = ok and bool(passed)
        checks.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))

    z = sp.symbols("z")

    # ---- characters on the H_3 NF basis (corpus machinery) ----
    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    # ---- the general-z block weights, solved from the trace (qou-isu5 weight) ----
    CHI = [chi3, chi21, chi111]
    TRV = [sp.Integer(1), z, z, z ** 2, z ** 2, z * (h * z + 1)]
    yv = sp.symbols("y3 y21 y111")
    sol = sp.solve([sp.Eq(sum(yv[k] * CHI[k](basis_vec(i)) for k in range(3)), TRV[i])
                    for i in range(N)], yv, dict=True)[0]
    y3g, y21g, y111g = [sp.cancel(sp.simplify(sol[yv[k]])) for k in range(3)]

    zD = q ** 3 / (q ** 2 + 1)
    y3D = sp.cancel(sp.simplify(y3g.subs(z, zD)))
    y21D = sp.cancel(sp.simplify(y21g.subs(z, zD)))
    check("y_(1^3) vanishes at z_D (the two-row cap)",
          sp.simplify(y111g.subs(z, zD)) == 0)
    check("normalisation y_3 + 2 y_21 = 1 at z_D",
          sp.simplify(y3D + 2 * y21D - 1) == 0)
    print(f"\n[1] the Markov D weights (both closed forms confirmed)")
    print(f"    y_3^D  = {sp.factor(y3D)}")
    print(f"    y_21^D = {sp.factor(y21D)}")
    check("y_3^D == (q^4+1)/(q^2+1)^2",
          sp.simplify(y3D - (q ** 4 + 1) / (q ** 2 + 1) ** 2) == 0)
    check("y_21^D == q^2/(q^2+1)^2",
          sp.simplify(y21D - q ** 2 / (q ** 2 + 1) ** 2) == 0)

    # ---- the decay element Delta_S, via its AFFINE trace signature ----
    # 08-29 established tr_M(Delta_S)(z) = h^2/2 - h*z, affine in z. That pins
    # the NF support to {gamma, sigma_0, sigma_1}: c_gamma = h^2/2 and
    # c_s0 + c_s1 = -h, with the two length-2 and the length-3 coefficients
    # zero. The three CHARACTERS turn out independent of how -h splits between
    # sigma_0 and sigma_1, which the check below verifies rather than assumes.
    a = sp.symbols("a")
    dS = [h ** 2 / 2, a, -h - a, 0, 0, 0]
    c3, c21, c111 = chi3(dS), chi21(dS), chi111(dS)
    for nm, c in (("chi^(3)", c3), ("chi^(2,1)", c21), ("chi^(1^3)", c111)):
        check(f"{nm}(Delta_S) is independent of the sigma_0/sigma_1 split",
              sp.simplify(sp.diff(c, a)) == 0)
    c3, c21, c111 = [sp.simplify(x.subs(a, 0)) for x in (c3, c21, c111)]

    # THE FINDING. Three exact facts, each asserted rather than observed.
    # Together they say the decay element is invisible to the (2,1) block at
    # EVERY z, so the two-row cap does not take the carrier 3 blocks -> 2, it
    # takes it 2 -> 1.
    regS = sp.simplify(reg_char(dS).subs(a, 0))
    check("reg_char(Delta_S) = 0 exactly (traceless in the regular rep)",
          sp.simplify(regS) == 0, f"= {regS}")
    check("chi^(2,1)(Delta_S) = 0 exactly (the 2-dim block NEVER carries decay)",
          sp.simplify(c21) == 0)
    check("chi^(3)(Delta_S) = -chi^(1^3)(Delta_S) exactly",
          sp.simplify(c3 + c111) == 0)
    # consequence, verified rather than asserted: the trace sees only y_3 - y_111
    anti = sp.simplify(sp.cancel((y3g - y111g) * c3 - (h ** 2 / 2 - h * z)))
    check("tr(Delta_S) = (y_3 - y_(1^3)) * chi^(3), for ALL z", anti == 0)

    print(f"\n[2] block characters of the decay element")
    print(f"    chi^(3)  (Delta_S) = {sp.factor(c3)}")
    print(f"    chi^(2,1)(Delta_S) = {sp.factor(c21)}")
    print(f"    chi^(1^3)(Delta_S) = {sp.factor(c111)}")

    # cross-check: the general-z decomposition must reproduce the affine trace
    recon = sp.simplify(y3g * c3 + y21g * c21 + y111g * c111)
    check("block decomposition reproduces tr_M(Delta_S) = h^2/2 - h z",
          sp.simplify(recon - (h ** 2 / 2 - h * z)) == 0,
          f"recon = {sp.factor(recon)}")

    # ---- THE SOLVE: two constraints, two unknowns, no free parameter ----
    Y3, Y21 = sp.symbols("Y3 Y21")
    trD = sp.simplify(h ** 2 / 2 - h * zD)
    F = sp.Symbol("F")                      # the required multiplicative factor
    T_req = trD * F
    forced = sp.solve([sp.Eq(Y3 + 2 * Y21, 1),
                       sp.Eq(Y3 * c3 + Y21 * c21, T_req)], [Y3, Y21], dict=True)[0]
    Y3s, Y21s = sp.cancel(forced[Y3]), sp.cancel(forced[Y21])
    print(f"\n[3] FORCED weights (unique; F = the required correction factor)")
    print(f"    y_3*  = {sp.factor(sp.simplify(Y3s))}")
    print(f"    y_21* = {sp.factor(sp.simplify(Y21s))}")

    # ---- evaluate at the pin, both admissible targets ----
    q0 = q_at(55)
    ev = lambda e, Fv: sp.lambdify((q, F), e, "mpmath")(q0, Fv)
    rows = {}
    for nm, Fv in (("tr_M base (F=1.75924)", F_REQUIRED_TRM),
                   ("augmentation base (F=0.88913)", F_REQUIRED_AUG)):
        rows[nm] = {"y_3_star": mp.nstr(ev(Y3s, Fv), 14),
                    "y_21_star": mp.nstr(ev(Y21s, Fv), 14)}
    y3D_n = sp.lambdify(q, y3D, "mpmath")(q0)
    y21D_n = sp.lambdify(q, y21D, "mpmath")(q0)
    print(f"\n[4] at the proton pin")
    print(f"    {'target':<32} {'y_3*':>18} {'y_21*':>18}")
    for nm, r in rows.items():
        print(f"    {nm:<32} {r['y_3_star']:>18} {r['y_21_star']:>18}")
    print(f"    {'Markov D (for reference)':<32} {mp.nstr(y3D_n,14):>18} {mp.nstr(y21D_n,14):>18}")

    # ---- is the forced pair RECOGNISABLE? (list declared above, pre-solve) ----
    cands = candidate_forms(q)
    cand_n = {k: mp.mpf(str(sp.N(v.subs(q, sp.Float(str(q0), 50)), 40)))
              for k, v in cands.items()}
    match = {}
    print(f"\n[5] nearest DECLARED form to each forced weight")
    for nm, r in rows.items():
        for which in ("y_3_star", "y_21_star"):
            val = mp.mpf(r[which])
            d = sorted(((abs(val - cv) / abs(val) if val else mp.inf, ck)
                        for ck, cv in cand_n.items()))
            best, second = d[0], d[1]
            isolated = second[0] > 10 * best[0]
            match[f"{nm} / {which}"] = {
                "value": mp.nstr(val, 14), "nearest": best[1],
                "rel_err": mp.nstr(best[0], 6), "second": second[1],
                "second_rel_err": mp.nstr(second[0], 6),
                "isolated_by_10x": bool(isolated),
            }
            print(f"    {nm[:22]:<22} {which:<10} {mp.nstr(val,12):>14}  "
                  f"-> {best[1][:26]:<26} {mp.nstr(best[0]*100,4):>9} %   "
                  f"isolated={isolated}")

    any_hit = any(m["isolated_by_10x"] and mp.mpf(m["rel_err"]) < mp.mpf("1e-3")
                  for m in match.values())
    recognised = ("LEAD — a forced weight matches a declared form, isolated"
                  if any_hit else
                  "no forced weight matches any declared form")

    # The structural verdict, which is stronger than the recognition test and
    # does not depend on it. chi^(2,1)(Delta_S) = 0 means the SOLVE ABOVE IS
    # DEGENERATE: the anchor constrains y_3 alone, y_21 is normalisation's
    # leftover and is INVISIBLE to Q_beta. That is why y_3* came out as exactly
    # F * y_3^D -- the anchor can only rescale the single carrying weight.
    y21_invisible = sp.simplify(sp.diff(Y3s * c3 + Y21s * c21, Y21)) == 0
    check("y_21 is INVISIBLE to Q_beta (the solve is degenerate, by construction)",
          bool(y21_invisible) or sp.simplify(c21) == 0)
    structural = (
        "SCOPE-(a) CLASS CLOSURE — under D the decay is carried by a SINGLE "
        "1-dimensional block. chi^(2,1)(Delta_S) = 0 exactly, at every z, so the "
        "two-row cap takes the carrier 2 blocks -> 1, not 3 -> 2. With one weight "
        "and that weight fixed by the trace axioms, BLOCK RE-WEIGHTING CANNOT "
        "SOURCE THE CORRECTION: the forced solve returns y_3* = F * y_3^D exactly, "
        "i.e. the anchor can only rescale the one carrying weight, and y_21* is "
        "normalisation's leftover with no effect on Q_beta. The new form the D "
        "re-derivation needs cannot come from the Wedderburn decomposition.")
    print(f"\n[6] recognition test: {recognised}")
    print(f"\n[7] {structural}")
    verdict = structural

    wb = WitnessBuilder("qbeta-d-frame-two-block-forced-weights", engine="sympy+mpmath")
    wb.set_description(
        "Under convention D the two-row cap leaves TWO block weights, and "
        "normalisation plus the anchor are TWO constraints, so the D-frame decay "
        "weights are FORCED with zero free parameters. Asks whether the forced "
        "pair is a recognisable q-rational, against a candidate list declared "
        "before solving. Derives nothing and wires nothing; a negative closes the "
        "two-block class the way 2026-08-29 closed the correction class.")
    wb.add_data("markov_D_weights", {"y_3": str(sp.factor(y3D)), "y_21": str(sp.factor(y21D))})
    wb.add_data("decay_block_characters",
                {"chi_3": str(sp.factor(c3)), "chi_21": str(sp.factor(c21)),
                 "chi_111": str(sp.factor(c111))})
    wb.add_data("forced_weights_symbolic",
                {"y_3_star": str(sp.factor(sp.simplify(Y3s))),
                 "y_21_star": str(sp.factor(sp.simplify(Y21s)))})
    wb.add_data("forced_weights_at_pin", rows)
    wb.add_data("markov_D_at_pin", {"y_3": mp.nstr(y3D_n, 14), "y_21": mp.nstr(y21D_n, 14)})
    wb.add_data("nearest_declared_form", match)
    wb.add_data("candidate_list_declared_before_solving", sorted(cands))
    wb.add_data("free_parameters", 0)
    wb.add_data("verdict", verdict)
    wb.add_data("recognition_test", recognised)
    wb.add_data("scope", "(a) — a class closure or a lead, never a derivation of Q_beta")
    wb.add_data("q0Anchor", "proton")
    wb.add_data("q0Value", mp.nstr(q0, 50))
    for c in checks:
        wb.add_assertion(c["name"],
                         computed=mp.mpf(1) if c["passed"] else mp.mpf(0),
                         expected=mp.mpf(1), tolerance=mp.mpf("0.5"), unit="bool")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
