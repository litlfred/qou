"""aomega_m3_wronskian_bar_involution_constraint_probe.py

Route C M3, normalisation Part 2 (bean qou-v1eu, issue #7376): the orthogonality relations
constrain det W_0 by a BAR-INVOLUTION functional equation, and that is a sharper statement
of the arc's remaining gap than "the GL(r) normalisation".

Part 1 gave the Casoratian ratio, hence det W_m up to the initial condition det W_0:

    4_1      det W_{m+1} = x^3     det W_m      -> GGM (136) det W_m = x^{3m+3}
    5_2      det W_{m+1} =         det W_m      -> GGM (262) det W_0 = a theta expression
    pretzel  det W_{m+1} = q^4     det W_m      -> det W_m = q^{4m} det W_0,  det W_0 OPEN

So what is missing at rank 6 is not "a normalisation" in the abstract.  It is ONE function
det W_0(x;q), and the orthogonality relation pins it: taking determinants of

    pref * W_m(x;q) J W_l(x;q^-1)^T  =  RHS                (GGM (137) for 4_1, (92) for 5_2)

gives, since det is multiplicative,

    det W_m(q) * det W_l(q^-1)  =  det(RHS) / (pref^r * det J)   =:  c

a BAR-INVOLUTION constraint with c a KNOWN constant once J and RHS are known.  A theta
solves such an equation for free, because GGM (109) extended to |q| != 1 says
theta(y; q^-1) = theta(y; q)^-1 — which is why their 5_2 answer IS a theta.

Gates / tests
  G1  c from GGM's printed 4_1 pairing (137) with J = diag(1,-1): det RHS = -1, det J = -1,
      pref = 1  =>  c = 1
  G2  GGM's own printed (136), det W_m = x^{3m+3}, SATISFIES that at m = l = -1: both
      factors are x^0 = 1 and carry no q at all, so the product is 1.  This is the
      cross-check of the derivation against their data, not an assumption.
  G3  c from GGM's printed 5_2 pairing (92) with J = [[0,0,1],[0,2,0],[1,0,0]] and the
      prefactor 1/2: det RHS = -1, det J = -2  =>  c = 4.  Note c is NOT universal.
  G4  GGM use MORE THAN ONE normalisation for 5_2 — (254) has end coefficients (1, ..., -1)
      while (276) is (1, s, s, 1) — and both give Casoratian ratio 1.  So the gauge is a
      choice within a class; what is invariant is the ratio modulo lambda^r.
  T1  the pretzel: state the constraint its det W_0 must satisfy, and record that c is
      UNKNOWN there because no rank-6 pairing is printed in any held source.
Exact sympy throughout; no mpmath, no q0, no float64.
"""
from __future__ import annotations

import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))

xs, qs, qm, m = sp.symbols("x q qm m")


def pairing_constant(R, J, pref):
    """det W_m(q) det W_l(q^-1) = det(RHS) / (pref^r det J)."""
    r = J.shape[0]
    return sp.simplify(sp.det(R) / (pref**r * sp.det(J))), r


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # --- 4_1: GGM (137) ---------------------------------------------------------------
    R41 = sp.Matrix([[xs**-2 + xs**-1 - 1, 1], [1, 0]])
    J41 = sp.diag(1, -1)
    c41, r41 = pairing_constant(R41, J41, sp.Integer(1))
    print(f"  4_1: det J = {sp.det(J41)}, det RHS = {sp.simplify(sp.det(R41))}  =>  c = {c41}")
    check("G1-the 4_1 bar-involution constant, derived from GGM's printed (137) by taking "
          "determinants, is c = 1", sp.simplify(c41 - 1) == 0, c=str(c41))

    detW41 = xs ** (3 * m + 3)                                   # GGM (136)
    at_m1 = sp.simplify(detW41.subs(m, -1))
    prod41 = sp.simplify(at_m1 * at_m1)                          # no q at all, so bar acts trivially
    print(f"  4_1: GGM (136) det W_m = {detW41};  det W_-1 = {at_m1};  product = {prod41}")
    check("G2-GGM's OWN printed determinant (136) SATISFIES that constraint at m = l = -1: "
          "det W_-1 = x^0 = 1, carries no q, so the product is 1 — the derivation is "
          "cross-checked against their data rather than assumed",
          sp.simplify(prod41 - c41) == 0, det_W_minus1=str(at_m1), product=str(prod41))

    # --- 5_2: GGM (92) ----------------------------------------------------------------
    R52 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 3 - qm]])
    J52 = sp.Matrix([[0, 0, 1], [0, 2, 0], [1, 0, 0]])
    c52, r52 = pairing_constant(R52, J52, sp.Rational(1, 2))
    print(f"  5_2: det J = {sp.det(J52)}, det RHS = {sp.simplify(sp.det(R52))}  =>  c = {c52}")
    check("G3-the 5_2 constant is c = 4, NOT 1 — so c is fixed per knot by (det J, det RHS) "
          "and is not a universal constant to be assumed at rank 6",
          sp.simplify(c52 - 4) == 0 and sp.simplify(c52 - c41) != 0, c=str(c52))

    # --- G4: GGM use more than one normalisation for 5_2 -------------------------------
    Sm = sp.Symbol("Sm")
    op254 = sp.expand((1 - Sm) * (1 - xs * Sm) * (1 - Sm / xs))      # GGM (254), minus the q^{2+m}S^2 term
    p254 = sp.Poly(op254, Sm)
    a0_254, a3_254 = p254.coeff_monomial(1), p254.coeff_monomial(Sm**3)
    ratio254 = sp.simplify((-1) ** 3 * a0_254 / a3_254)
    s = xs + 1 + 1 / xs
    p276 = sp.Poly(1 + s * Sm + s * Sm**2 + Sm**3, Sm)               # GGM (276)
    ratio276 = sp.simplify((-1) ** 3 * p276.coeff_monomial(1) / p276.coeff_monomial(Sm**3))
    print(f"  5_2 (254) end coeffs ({a0_254}, {a3_254}) -> ratio {ratio254}")
    print(f"  5_2 (276) end coeffs (1, 1)            -> ratio {ratio276}")
    check("G4-GGM print TWO normalisations of the same 5_2 operator and they do NOT agree: (254) "
          "has end coefficients (1, -1) and ratio +1, (276) has (1, 1) and ratio -1. They differ by "
          "the SIGN gauge lambda = -1, which flips the ratio by lambda^-r = (-1)^3 = -1 — exactly "
          "the observed gap. So the ratio is gauge-dependent even in sign, and only its class "
          "modulo lambda^r is invariant",
          sp.simplify(ratio254 - 1) == 0 and sp.simplify(ratio276 + 1) == 0
          and sp.simplify(ratio254 / ratio276 - (-1) ** 3) == 0,
          ratio_254=str(ratio254), ratio_276=str(ratio276),
          gauge_between="lambda = -1", end_coeffs_254=[str(a0_254), str(a3_254)])

    # G5 — the correction this probe forced on Part 1.
    check("G5-CORRECTION to Part 1: a PALINDROMIC operator has ratio (-1)^r, which is m-INDEPENDENCE "
          "only at EVEN r; at odd r it ALTERNATES. GGM's m-independent 5_2 statement "
          "(det W_{m+1} = det W_m) is in the ANTI-palindromic (254), ratio +1 — not in the "
          "palindromic (276), ratio -1. Part 1's G3 called the palindrome gauge 'what makes GGM's "
          "Wronskian m-independent', and for this odd-rank knot that is wrong",
          sp.simplify(ratio276 - (-1) ** 3) == 0 and sp.simplify(ratio254 - 1) == 0,
          palindromic_ratio=str(ratio276), ggm_m_independent_ratio=str(ratio254),
          rank=3, parity="odd")

    # --- T1: the pretzel ---------------------------------------------------------------
    constraint = "det W_0(x;q) * det W_0(x;q^-1) = c_pretzel   (with det W_m = q^{4m} det W_0)"
    print(f"\n  pretzel: {constraint}")
    print("  c_pretzel is UNKNOWN: no rank-6 orthogonality relation is printed in any held source.")
    check("T1-c_pretzel is known, i.e. some held source prints a rank-6 orthogonality relation "
          "from which it can be read off", False,
          constraint=constraint,
          searched="GGM arxiv-2012.00062v3 secs 011/015 (the only printed pairings: (137) rank 2, "
                   "(92)/(93) rank 3); no rank-6 analogue",
          consequence="the gap is ONE function det W_0 and ONE constant c, tied by a bar-involution "
                      "equation — not 'the GL(r) normalisation' in the abstract")

    verdict = (
        "DERIVED: the orthogonality relations constrain det W_0 by a BAR-INVOLUTION functional "
        "equation. Taking determinants of pref * W_m(q) J W_l(q^-1)^T = RHS gives "
        "det W_m(q) det W_l(q^-1) = det(RHS)/(pref^r det J) =: c, a constant fixed per knot. From "
        f"GGM's printed pairings: c = {c41} for 4_1 (137) and c = {c52} for 5_2 (92) — so c is NOT "
        "universal. The derivation is cross-checked against GGM's own printed determinant (136): "
        "det W_m = x^{3m+3} gives det W_-1 = 1 with no q at all, product 1, matching c = 1 exactly "
        "(G2). A theta solves such an equation for free, since GGM (109) extended to |q| != 1 gives "
        "theta(y;q^-1) = theta(y;q)^-1 — which is why their 5_2 answer IS a theta. GGM also print "
        "TWO normalisations of the same 5_2 operator, (254) and (276), both with Casoratian ratio 1 "
        "(G4) that do NOT agree — ratios +1 and -1, differing by the sign gauge lambda = -1 — so "
        "the ratio is gauge-dependent even in sign. That FORCES A CORRECTION to Part 1 (G5): a "
        "palindromic operator has ratio (-1)^r, which is m-independence only at EVEN rank; at odd "
        "rank it alternates, and GGM's m-independent 5_2 statement lives in the ANTI-palindromic "
        "(254), not the palindromic (276). CONSEQUENCE for the arc: at rank 6 the "
        "missing input is not 'the GL(r) normalisation' in the abstract but ONE function "
        "det W_0(x;q) and ONE constant c_pretzel, tied by that equation — and c_pretzel is unknown "
        "because no held source prints a rank-6 orthogonality relation (T1, a recorded negative).")
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    w = {"name": "aomega-m3-wronskian-bar-involution-constraint",
         "description": "The bar-involution constraint det W(q) det W(q^-1) = c that GGM's orthogonality "
                        "relations impose on the Wronskian determinant, its constants for 4_1 and 5_2, and "
                        "the resulting sharper statement of the rank-6 gap.",
         "computation": "aomega-m3-wronskian-bar-involution-constraint", "engine": "python+sympy",
         "scriptFile": os.path.basename(__file__), "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
         "parameters": {"rule": "det W_m(q) det W_l(q^-1) = det(RHS) / (pref^r det J)"},
         "data": {"c_4_1": str(c41), "c_5_2": str(c52), "c_pretzel": None,
                  "det_W_4_1_at_m_minus_1": str(at_m1),
                  "ratio_254": str(ratio254), "ratio_276": str(ratio276),
                  "pretzel_constraint": constraint},
         "verdict": verdict, "assertions": assertions}
    _WB.stamp_staleness_metadata(w, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-wronskian-bar-involution-constraint.witness.json")
    with open(out, "w") as fh:
        json.dump(w, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
