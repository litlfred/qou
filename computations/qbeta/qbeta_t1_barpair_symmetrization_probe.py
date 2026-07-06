#!/usr/bin/env python3
"""
T1 (bean 7vfu) -- bar-pair symmetrized evaluation of alpha_1 on the golden locus.

Follows the c4qz kill (I-A raw pointwise slots excluded on slot bar-parity):
the K1b locus x* = (3+sqrt5)/2 = phi^2 is a bar-conjugate pair {x*, 1/x*},
and the full bar involution (q,x) -> (1/q,1/x) PERMUTES the pair -- so the
pair-symmetrized objects

    D(q) = alpha_1(q, x*) - alpha_1(q, 1/x*)   (odd candidate; D(1) = 0 free)
    S(q) = alpha_1(q, x*) + alpha_1(q, 1/x*)   (even candidate; S(1) = 4)

are the canonical parity candidates. Kill criteria pre-stated in ledger
SS4-ter (commit 44b0b82c): T1-K1 D bar-ODD (exact or monomial twist);
T1-K2 S bar-EVEN (exact or monomial twist). Both fail -> raw
pair-symmetrization killed, escalate to I-B.

Exact symbolic (sympy, algebraic radicals). NO anchors, NO c_k value, NO fit.
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


def parity_report(f, q):
    """Exact parity of f(q) under q -> 1/q: 'even', 'odd', or twist analysis."""
    fbar = sp.radsimp(sp.cancel(sp.together(f.subs(q, 1 / q))))
    if sp.simplify(sp.radsimp(fbar - f)) == 0:
        return "even", sp.Integer(1)
    if sp.simplify(sp.radsimp(fbar + f)) == 0:
        return "odd", sp.Integer(-1)
    ratio = sp.simplify(sp.radsimp(sp.cancel(sp.together(fbar / f))))
    num, den = sp.fraction(sp.together(sp.powsimp(ratio)))
    if len(sp.Add.make_args(sp.expand(num))) == 1 and \
       len(sp.Add.make_args(sp.expand(den))) == 1:
        return "monomial-twist", ratio
    return "neither", ratio


def main():
    q, x = sp.symbols("q x", positive=True)
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # Operator coefficients (verbatim, aj_figure_eight_certificate.py lineage).
    a0 = (x - 1) * (x**2 * q**3 - 1) / x**6
    a2 = (x * q**2 - 1) * (x**2 * q - 1) / x**6
    a1 = -((x * q - 1) ** 2 * (x * q + 1) * (x**2 * q**2 - x**2 * q + x**2
            - x * q**2 - x * q - x + q**2 + q + 1)) / x**6
    alpha1 = sp.cancel(sp.together(-a1 / a2))

    xstar = sp.Rational(3, 2) + sp.sqrt(5) / 2      # phi^2, exact
    xstar_inv = sp.radsimp(1 / xstar)               # phi^-2 = (3 - sqrt5)/2
    # sanity: the pair really is bar-conjugate
    check("locus_pair_product_one",
          sp.simplify(xstar * xstar_inv - 1) == 0)

    ev = lambda e, val: sp.radsimp(sp.cancel(sp.together(e.subs(x, val))))
    A = ev(alpha1, xstar)       # alpha_1(q, x*)
    B = ev(alpha1, xstar_inv)   # alpha_1(q, 1/x*)
    D = sp.radsimp(sp.simplify(A - B))
    S = sp.radsimp(sp.simplify(A + B))

    # q=1 sanity (both evaluations hit the c_3 shadow 2 by construction).
    A1 = sp.simplify(sp.limit(A, q, 1))
    B1 = sp.simplify(sp.limit(B, q, 1))
    check("q1_values_both_equal_2", A1 == 2 and B1 == 2)

    # T1-K1: D bar-odd?
    d_par, d_twist = parity_report(D, q)
    k1 = d_par == "odd" or (d_par == "monomial-twist"
                            and sp.simplify(d_twist.subs(q, sp.Rational(3, 2))) < 0)
    check("T1K1_D_bar_odd_exact_or_neg_monomial_twist", k1)

    # T1-K2: S bar-even?
    s_par, s_twist = parity_report(S, q)
    k2 = s_par == "even" or (s_par == "monomial-twist"
                             and sp.simplify(s_twist.subs(q, sp.Rational(3, 2))) > 0)
    check("T1K2_S_bar_even_exact_or_pos_monomial_twist", k2)

    survives = bool(k1)  # the bar-odd channel is the load-bearing one
    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "SURVIVOR -- the pair-difference D(q) = alpha_1(q,x*) - alpha_1(q,1/x*) on the "
        "golden bar-pair locus is a bar-ODD scalar canonically built from the 4_1 "
        "operator on its own c_3-shadow locus (D(1) = 0 as bar-oddness requires). "
        "Feeds Z3/Z4 as a candidate odd carrier ingredient. NOT a closure, NOT a c_k "
        "value, nothing wired; the q!=1 identification (I-B) remains open."
        if survives else
        "KILL -- neither symmetrized combination has clean bar-parity; raw "
        "pair-symmetrization is excluded (scope-(a)). Escalate to I-B re-basing / Z3 "
        "carriers. Do NOT run any anchor sweep."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-t1-barpair-symmetrization",
        "description": "T1 (bean 7vfu): bar-parity of the pair-symmetrized 4_1 operator "
                       "slot alpha_1 over the golden bar-conjugate locus {phi^2, phi^-2}. "
                       "Kill criteria pre-stated in ledger SS4-ter (commit 44b0b82c).",
        "audit_only": True,
        "tier": "structural-exact (symbolic parity over algebraic locus; no fit, no anchors)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "x_star": str(xstar),
            "D": str(D),
            "S": str(S),
            "D_parity": d_par, "D_twist_or_ratio": str(d_twist),
            "S_parity": s_par, "S_twist_or_ratio": str(s_twist),
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone, bean 7vfu (T1)",
            "prestatement": "docs/coordination/z-ck-fmap-keystone.md SS4-ter (commit 44b0b82c)",
            "c4qz_kill": "computations/qbeta/qbeta-c4qz-fourone-operator-q1-shadow.witness.json",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-t1-barpair-symmetrization.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)

    print("=== T1 : bar-pair symmetrization on the golden locus ===")
    print("D parity :", d_par, "| twist/ratio:", d_twist)
    print("S parity :", s_par, "| twist/ratio:", s_twist)
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if survives else 1


if __name__ == "__main__":
    sys.exit(main())
