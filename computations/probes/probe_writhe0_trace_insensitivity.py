"""Bean `qou-n1dj` part 2: what IS true about writhe-0, pi=id braids?

The scope note of `prop:h3-markov-wenzl-weights`
(`mass-theory/h3-markov-wenzl-weights-context.md`) claims the Jones/TL trace
(convention **D**) and the full-Hecke Ocneanu trace (convention **C**)
"coincide ... on the observable combination carried by writhe-0, pi=id braids
-- which is why every *physical* mass prediction is insensitive to the
distinction". beta_Bor is writhe-0 with pi=id, and D(beta_Bor) - C(beta_Bor) =
1.9554e-4 exactly, so the claim as written is FALSE.

Nobody writes that by accident. This probe isolates the true statement nearby
and measures exactly how much of it survives.

THE TRUE LEMMA (proved here symbolically, and in Lean:
`QOU/BraidsAndKnots/MarkovTraceWrithe0.lean`).  For any normalised Markov
trace on H_3(q) -- i.e. any `tr = sum_lambda y_lambda chi^lambda` with
`sum_lambda y_lambda d_lambda = 1`, `d = (1,2,1)` -- and any braid
`beta in B_3` with writhe 0 and `pi(beta) = id`:

    tr_M(beta) = 1 + y_(2,1) * (chi^(2,1)(beta) - 2).

Consequences, exactly:

  * the one-dimensional channels contribute `chi^(3) = q^w = 1` and
    `chi^(1^3) = (-q^-1)^w = 1` at `w = 0`, so only the SUM
    `y_(3) + y_(1^3)` enters -- and normalisation already pins that sum to
    `1 - 2 y_(2,1)`.  Hence the SPLIT between `y_(3)` and `y_(1^3)` is
    invisible on writhe-0 pi=id braids.  This is the defensible version of
    the scope note's claim, and it is exactly the chirality / transpose-pair
    (`y_(3)` vs `y_(1^3)`) asymmetry that the same content block's
    "Non-uniformity of the weights" section is about.
  * `y_(2,1)` is NOT invisible.  Two conventions agree on such a braid iff
    they share `y_(2,1)` or `chi^(2,1)(beta) = 2`.  C and D share neither:
        y_(2,1)(D) = 1/[2]_q^2,   y_(2,1)(C) != 1/[2]_q^2,
        chi^(2,1)(beta_Bor) = 2 - 3h^4 - h^6 != 2   (q != 1).
    The whole D - C gap on beta_Bor is therefore the single product
        (y_(2,1)(D) - y_(2,1)(C)) * (-3h^4 - h^6).

The parent bean also floated "the traces agree on braids whose image lies in
TL_3".  That is checked and REFUTED here as a scope-(b) structural exclusion:
`chi^(1^3)(beta) = (-q^-1)^{w(beta)}` is a unit for every braid, so no braid
image has vanishing three-row component and no braid image lies in the TL_3
part.  The invariant is the invertibility of the one-dimensional characters.

Run: python3 -u computations/probes/probe_writhe0_trace_insensitivity.py
No production value is read or written.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
import _path_bridge  # noqa: F401,E402
for _sub in ("markov", "substrate", "hecke"):
    sys.path.insert(0, str(ROOT / _sub))

import sympy as sp  # noqa: E402

from hecke_character_symbolic import q_character_on_braid_word  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

qs = sp.symbols("q", positive=True)
z = sp.symbols("z")
q0 = sp.Float(str(Q0), 50)

PARTS = [(3,), (2, 1), (1, 1, 1)]
DIMS = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
CLASSES = {
    "1": [],
    "s0": [(0, "sigma")],
    "s0s1": [(0, "sigma"), (1, "sigma")],
}
TARGET = {"1": sp.Integer(1), "s0": z, "s0s1": z ** 2}

# beta_Bor = (sigma_0 sigma_1^-1)^3 -- writhe 0, pi = id in S_3.
BOR = [(0, "sigma"), (1, "sigma_inv")] * 3


def qint(n):
    return sp.cancel((qs ** n - qs ** -n) / (qs - qs ** -1))


def weights_of_z():
    """y_lambda as rational functions of the Ocneanu parameter z."""
    rows, rhs = [], []
    for cname, word in CLASSES.items():
        rows.append([sp.cancel(sp.together(sp.sympify(
            q_character_on_braid_word(lam, word, qs)))) for lam in PARTS])
        rhs.append(TARGET[cname])
    sol = sp.Matrix(rows).solve(sp.Matrix(rhs))
    return {lam: sp.cancel(sp.together(sol[i])) for i, lam in enumerate(PARTS)}


def main() -> int:
    fails = []
    y_of_z = weights_of_z()
    z_C = sp.cancel(1 / (sp.sqrt(qs) + 1 / sp.sqrt(qs)))
    z_D = sp.cancel(qs ** 3 / (qs ** 2 + 1))

    print("Ocneanu parameters")
    print("  z_C = 1/(q^1/2 + q^-1/2) = %s   -> %s"
          % (z_C, sp.N(z_C.subs(qs, q0), 20)))
    print("  z_D = q^3/(q^2+1)        = %s   -> %s"
          % (z_D, sp.N(z_D.subs(qs, q0), 20)))

    yC = {lam: sp.cancel(sp.together(y_of_z[lam].subs(z, z_C))) for lam in PARTS}
    yD = {lam: sp.cancel(sp.together(y_of_z[lam].subs(z, z_D))) for lam in PARTS}

    print("\nWedderburn weights on lambda |- 3")
    print("  %-10s %-24s %-24s" % ("lambda", "convention C", "convention D"))
    for lam in PARTS:
        print("  %-10s %-24s %-24s" % (
            str(lam), sp.N(yC[lam].subs(qs, q0), 18),
            sp.N(yD[lam].subs(qs, q0), 18)))

    # --- normalisation sanity: sum y_lambda d_lambda = 1 for both -----------
    for name, yy in (("C", yC), ("D", yD)):
        s = sp.simplify(sum(yy[lam] * DIMS[lam] for lam in PARTS) - 1)
        ok = s == 0
        print("  sum_lambda y_lambda d_lambda == 1  (%s): %s" % (name, ok))
        if not ok:
            fails.append("normalisation fails for convention %s" % name)

    # --- D is the TL/Jones vector; C is not --------------------------------
    y21_jones = sp.cancel(1 / qint(2) ** 2)
    dD = sp.simplify(sp.cancel(yD[(2, 1)] - y21_jones))
    dC = sp.simplify(sp.cancel(yC[(2, 1)] - y21_jones))
    print("\n  y_(2,1)(D) - 1/[2]_q^2 == 0 : %s" % (dD == 0))
    print("  y_(2,1)(C) - 1/[2]_q^2 == 0 : %s   (value at q0: %s)"
          % (dC == 0, sp.N(dC.subs(qs, q0), 12)))
    print("  y_(1^3)(D) == 0             : %s" % (sp.simplify(yD[(1, 1, 1)]) == 0))
    print("  y_(1^3)(C) == 0             : %s   (value at q0: %s)"
          % (sp.simplify(yC[(1, 1, 1)]) == 0,
             sp.N(yC[(1, 1, 1)].subs(qs, q0), 12)))
    if dD != 0:
        fails.append("convention D is not the Jones y_(2,1) = 1/[2]_q^2")
    if dC == 0:
        fails.append("convention C unexpectedly shares the Jones y_(2,1)")

    # --- the writhe-0, pi=id lemma, symbolically ---------------------------
    print("\nThe writhe-0, pi=id lemma")
    chi = {lam: sp.cancel(sp.together(sp.sympify(
        q_character_on_braid_word(lam, BOR, qs)))) for lam in PARTS}
    print("  chi^(3)  (beta_Bor) = %s" % sp.simplify(chi[(3,)]))
    print("  chi^(1^3)(beta_Bor) = %s" % sp.simplify(chi[(1, 1, 1)]))
    for lam in ((3,), (1, 1, 1)):
        if sp.simplify(chi[lam] - 1) != 0:
            fails.append("chi^%s(beta_Bor) != 1 (writhe-0 premise broken)" % (lam,))
    print("  both one-dim characters == 1 at writhe 0: %s"
          % all(sp.simplify(chi[lam] - 1) == 0 for lam in ((3,), (1, 1, 1))))

    h = qs - 1 / qs
    chi21_closed = 2 - 3 * h ** 4 - h ** 6
    print("  chi^(2,1)(beta_Bor) - (2 - 3h^4 - h^6) == 0 : %s"
          % (sp.simplify(sp.cancel(chi[(2, 1)] - chi21_closed)) == 0))
    if sp.simplify(sp.cancel(chi[(2, 1)] - chi21_closed)) != 0:
        fails.append("chi^(2,1)(beta_Bor) closed form mismatch")

    # generic-y form of the lemma: for arbitrary y_(3), y_(1^3) subject to
    # normalisation, the trace on a writhe-0 pi=id braid depends only on y_(2,1)
    y3s, y21s, y13s = sp.symbols("y3 y21 y13")
    tr_generic = y3s * chi[(3,)] + y21s * chi[(2, 1)] + y13s * chi[(1, 1, 1)]
    # impose normalisation y3 + 2 y21 + y13 = 1 by eliminating y3
    tr_norm = sp.simplify(sp.cancel(tr_generic.subs(y3s, 1 - 2 * y21s - y13s)))
    lemma_rhs = 1 + y21s * (chi[(2, 1)] - 2)
    lemma_ok = sp.simplify(sp.cancel(tr_norm - lemma_rhs)) == 0
    print("  tr = 1 + y_(2,1)*(chi^(2,1) - 2) for ALL (y_(3), y_(1^3)) "
          "with sum y d = 1: %s" % lemma_ok)
    print("  => the (y_(3), y_(1^3)) SPLIT is invisible; y_(2,1) is NOT.")
    if not lemma_ok:
        fails.append("writhe-0 lemma failed symbolically")
    # the split really is free: y_(1^3) does not appear in tr_norm
    split_free = sp.simplify(sp.diff(tr_norm, y13s)) == 0
    print("  d(tr)/d(y_(1^3)) == 0 at fixed y_(2,1): %s" % split_free)
    if not split_free:
        fails.append("the (y_(3), y_(1^3)) split is not actually invisible")

    # --- the gap is one product -------------------------------------------
    trD = sp.cancel(sum(yD[lam] * chi[lam] for lam in PARTS))
    trC = sp.cancel(sum(yC[lam] * chi[lam] for lam in PARTS))
    gap = sp.cancel(sp.together(trD - trC))
    predicted = sp.cancel(sp.together(
        (yD[(2, 1)] - yC[(2, 1)]) * (chi[(2, 1)] - 2)))
    print("\nThe D - C gap on beta_Bor")
    print("  D(beta_Bor) = %s" % sp.N(trD.subs(qs, q0), 18))
    print("  C(beta_Bor) = %s" % sp.N(trC.subs(qs, q0), 18))
    print("  D - C       = %s" % sp.N(gap.subs(qs, q0), 12))
    print("  relative    = %s ppm" % sp.N(gap.subs(qs, q0)
                                          / trD.subs(qs, q0) * 10 ** 6, 8))
    gap_ok = sp.simplify(sp.cancel(gap - predicted)) == 0
    print("  gap == (y_(2,1)(D) - y_(2,1)(C)) * (chi^(2,1) - 2) exactly: %s"
          % gap_ok)
    if not gap_ok:
        fails.append("gap is not the single y_(2,1) product")

    # D matches the Lean BorromeanMarkovTrace closed form
    lean_D = sp.cancel((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))
    lean_ok = sp.simplify(sp.cancel(trD - lean_D)) == 0
    print("  D == Lean (4+h^2-3h^4-h^6)/(h^2+4) exactly: %s" % lean_ok)
    if not lean_ok:
        fails.append("D does not equal the Lean BorromeanMarkovTrace form")

    # --- the "image lies in TL_3" candidate, refuted ----------------------
    print("\nThe 'braid image lies in TL_3' candidate -- refuted, scope (b)")
    print("  chi^(1^3) on a braid word of writhe w is (-q^-1)^w, a UNIT:")
    for w, word in ((1, [(0, "sigma")]),
                    (0, BOR),
                    (-2, [(0, "sigma_inv"), (1, "sigma_inv")])):
        v = sp.simplify(sp.sympify(q_character_on_braid_word(
            (1, 1, 1), word, qs)))
        print("    w = %-3s  chi^(1^3) = %-14s  nonzero: %s"
              % (w, v, sp.simplify(v) != 0))
        if sp.simplify(v) == 0:
            fails.append("found a braid with vanishing chi^(1^3)")
    print("  => no braid image has a vanishing three-row component, so")
    print("     'lies in TL_3' is never satisfied by a braid image.")

    print("\n%s  (%d check(s) failed)"
          % ("FAIL" if fails else "PASS", len(fails)))
    for f in fails:
        print("  - %s" % f)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
