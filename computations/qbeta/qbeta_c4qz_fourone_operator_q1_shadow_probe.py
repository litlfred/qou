#!/usr/bin/env python3
"""
c4qz -- I-A q=1 shadow gate: the 4_1 order-2 operator vs the c_k kernel slots.

Formalize-first, decidable, bounded (bean c4qz, PR #3449; pre-statement
committed BEFORE this run in docs/coordination/z-ck-fmap-keystone.md SS4-bis,
commit c9b873b6). Exact symbolic only: NO anchor sweep, NO c_k value, NO fit,
NO wiring.

Identification tested (I-A, color<->rung direct): slot the operator's
normalized homogeneous coefficients

    alpha_1 = -a_1/a_2   <->  kernel a_1-slot  ( = -c_3, bar-ODD )
    alpha_2 = -a_0/a_2   <->  kernel a_2-slot  ( = c_2 = -1, bar-even )

(coefficients verbatim from aj_figure_eight_certificate.py via the P-C15
probe; x = q^N, the classical M held fixed as q -> 1). The operator is
INHOMOGENEOUS (... = b); only the homogeneous part is tested -- caveat
recorded in the ledger pre-statement.

Kill criteria (pre-stated; any failure -> I-A killed, scope-(a) row):
  K1a: alpha_2(q=1, x) == -1 identically in x.
  K1b: alpha_1(q=1, x) = 2 has a real solution x* > 0.
  K2 : alpha_1 bar-ODD, alpha_2 bar-EVEN (up to Laurent-monomial twist)
       under q -> 1/q, x -> 1/x.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def _repo_head_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True,
        ).strip()
    except Exception:
        return None


def _twist_and_sign(expr, q, x):
    """Return (is_monomial_twist, sign) for bar(expr)/expr under q,x -> 1/q,1/x.

    sign = +1 if bar(expr) = +monomial*expr with the monomial evaluating to a
    pure power (bar-even up to twist), -1 if bar(expr) = -monomial*expr.
    """
    b = sp.cancel(sp.together(expr.subs({q: 1 / q, x: 1 / x}, simultaneous=True)))
    ratio = sp.simplify(sp.cancel(sp.together(b / expr)))
    num, den = sp.fraction(sp.together(sp.powsimp(ratio)))
    num, den = sp.expand(num), sp.expand(den)
    if len(sp.Add.make_args(num)) != 1 or len(sp.Add.make_args(den)) != 1:
        return False, 0
    # monomial ratio; extract overall sign
    sign = 1
    if sp.simplify(ratio.subs({q: sp.Rational(3, 2), x: sp.Rational(5, 4)})) < 0:
        sign = -1
    return True, sign


def main():
    q, x = sp.symbols("q x", positive=True)
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # Operator coefficients -- verbatim from aj_figure_eight_certificate.py
    # (same source as the P-C15 probe).
    a0 = (x - 1) * (x**2 * q**3 - 1) / x**6
    a2 = (x * q**2 - 1) * (x**2 * q - 1) / x**6
    a1 = -((x * q - 1) ** 2 * (x * q + 1) * (x**2 * q**2 - x**2 * q + x**2
            - x * q**2 - x * q - x + q**2 + q + 1)) / x**6  # bar-odd upstream

    alpha1 = sp.cancel(sp.together(-a1 / a2))
    alpha2 = sp.cancel(sp.together(-a0 / a2))

    # --- K1a: alpha_2(q=1, x) == -1 identically. ---
    alpha2_q1 = sp.simplify(sp.limit(alpha2, q, 1))
    k1a = sp.simplify(alpha2_q1 + 1) == 0
    check("K1a_alpha2_q1_identically_minus_one", k1a)

    # --- K1b: alpha_1(q=1, x) = 2 has a real root x* > 0. ---
    alpha1_q1 = sp.simplify(sp.limit(alpha1, q, 1))
    sols = sp.solve(sp.Eq(alpha1_q1, 2), x)
    real_pos = [s for s in sols if s.is_real and s.is_positive]
    k1b = len(real_pos) > 0
    check("K1b_alpha1_q1_eq_2_has_real_positive_root", k1b)

    # Structure of the locus (recorded, not asserted as physics): the roots'
    # product/sum, and whether the pair is bar-conjugate (x* * x*' = 1).
    prod_is_one = bool(len(real_pos) == 2
                       and sp.simplify(real_pos[0] * real_pos[1] - 1) == 0)
    check("locus_roots_bar_conjugate_pair_product_one", prod_is_one)

    # --- K2: slot parities up to monomial twist. ---
    mono1, sign1 = _twist_and_sign(alpha1, q, x)
    mono2, sign2 = _twist_and_sign(alpha2, q, x)
    check("K2_alpha1_bar_odd_up_to_monomial_twist", mono1 and sign1 == -1)
    check("K2_alpha2_bar_even_up_to_monomial_twist", mono2 and sign2 == 1)

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "PASS -- I-A's q=1 shadow is NOT excluded (scope-(a) positive). The 4_1 "
        "operator's a_2-slot reproduces c_2 = -1 IDENTICALLY in x at q=1, and its "
        "a_1-slot hits the c_3 -> -2 shadow exactly on the bar-conjugate locus "
        "alpha_1(1,x) = 2 (see result.alpha1_q1 / result.locus). Slot parities match "
        "(alpha_1 bar-ODD, alpha_2 bar-even). NOT a closure, NOT a c_k value, nothing "
        "wired; the identification at q != 1 (I-B cyclotomic re-basing) remains open."
        if all_passed else
        "KILL -- a pre-stated criterion failed; record a scope-(a) refutation row for "
        "I-A in the ledger and fall back to I-B / Z3 carriers. Do NOT run any anchor "
        "sweep."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-c4qz-fourone-operator-q1-shadow",
        "description": "c4qz I-A gate: q=1 shadow of the 4_1 order-2 qZeilberger "
                       "operator slotted into the c_k depth-2 kernel constraints "
                       "(alpha_2 <-> c_2 = -1 identity; alpha_1 <-> -c_3 = 2 locus; "
                       "slot bar-parities). Exact symbolic; kill criteria pre-stated "
                       "in ledger SS4-bis (commit c9b873b6) before the run.",
        "audit_only": True,
        "tier": "structural-exact (symbolic q=1 shadow + bar-parity; no fit, no anchors)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "alpha1": str(alpha1),
            "alpha2": str(alpha2),
            "alpha2_q1": str(alpha2_q1),
            "alpha1_q1": str(alpha1_q1),
            "locus_alpha1_eq_2_solutions": [str(s) for s in sols],
            "locus_real_positive": [str(s) for s in real_pos],
            "inhomogeneity_caveat": "operator is inhomogeneous (=b); homogeneous part tested",
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone, bean c4qz (I-A q=1 shadow gate)",
            "ledger_prestatement": "docs/coordination/z-ck-fmap-keystone.md SS4-bis (commit c9b873b6)",
            "operator_source": "computations/aj_figure_eight_certificate.py (via P-C15 probe)",
            "kernel_constraints": "QOU/BraidKnot/QBetaCKRecursionKernelConstraints.lean",
            "pc15": "docs/audits/2026-07-03-qbeta-pc15-casoratian-bar-parity.md",
            "ea56_exclusion": "QOU/QBeta/ZBarParity.lean + qbeta-z-bar-parity-fmap-class.witness.json",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-c4qz-fourone-operator-q1-shadow.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)

    print("=== c4qz : 4_1 operator I-A q=1 shadow gate ===")
    print("alpha2(q=1,x) :", alpha2_q1, " (expect -1 identically)")
    print("alpha1(q=1,x) :", alpha1_q1, " (locus alpha1 = 2)")
    print("locus roots   :", sols)
    print("ALL PASSED    :", all_passed)
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
