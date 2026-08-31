#!/usr/bin/env python3
"""Creative-telescoping certificate for the 4_1 annihilator (bean pko4).

The one remaining Lean `sorry` in QOU/BraidKnot/AJFigureEight.lean is the
general-N annihilation.  Its standard proof is a qZeilberger certificate:
a rational function Cert(q, x, y) (x = q^N, y = q^k) with

  (*)  a2(x)*r2(x,y) + a1(x)*r1(x,y) + a0(x)
          = Cert(x, q*y) * s(x,y) - Cert(x, y)

where, for the Habiro-Le summand F(N,k) = q^{Nk} (q^{-N-1};q^{-1})_k
(q^{-N+1};q)_k (termwise equal to the Newton form, proved in Lean):

  s(x,y)  = F(N,k+1)/F(N,k) = x * (1 - 1/(q*x*y)) * (1 - q*y/x)
  r1(x,y) = F(N+1,k)/F(N,k)
          = y * (1 - 1/(q*x*y))/(1 - 1/(q*x)) * (1 - 1/x)/(1 - y/x)
  r2(x,y) = F(N+2,k)/F(N,k) = r1(x,y) * r1(q*x, y)

Multiplying (*) by F(N,k) and summing k = 0..K-1 (K large; the tower
terminates, F(N,k) = 0 for k >= N) telescopes the RHS to
G(N,K) - G(N,0) -> -Cert(x, 1), so consistency REQUIRES

  (**)  b(x) = -Cert(x, 1)

against the verified inhomogeneous part b — an independent cross-check.

This script SOLVES for Cert by linear algebra over Q(q, x) (polynomial
ansatz in y over a guessed denominator, coefficients matched exactly with
sympy), then VERIFIES (*) exactly and (**) exactly.  The certificate is
the data the Lean proof of the sorry will transcribe (follow-on tranche):
(*) is a rational-function identity (field_simp + ring modulo denominator
hypotheses) and the telescoping sum is a Finset.sum induction.

Audit-only; no production wiring.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE / "substrate"))

import sympy as sp

q, x, y = sp.symbols("q x y")

# verified operator (aj-figure-eight-operator-construct-verify.witness.json)
a0 = (x - 1) * (x**2 * q**3 - 1) / x**6
a1 = -((x * q - 1) ** 2 * (x * q + 1)
       * (x**4 * q**4 - x**3 * q**3 - x**2 * q**3 - x**2 * q - x * q + 1)) \
     / (x**8 * q**2)
a2 = (x * q**2 - 1) * (x**2 * q - 1) / x**6
b = (x * q + 1) * (x**2 * q - 1) * (x**2 * q**3 - 1) / (x**7 * q)

s_ratio = x * (1 - 1 / (q * x * y)) * (1 - q * y / x)
r1 = y * (1 - 1 / (q * x * y)) / (1 - 1 / (q * x)) * (1 - 1 / x) / (1 - y / x)
r2 = sp.together(r1 * r1.subs(x, q * x))


def try_ansatz(deg_lo: int, deg_hi: int, den):
    """Cert = sum_{i=deg_lo}^{deg_hi} c_i(x) y^i / den(x,y); solve (*)."""
    # build symbol list manually (negative indices)
    cs = [sp.Symbol(f"c_{i}") for i in range(deg_lo, deg_hi + 1)]
    cert = sum(c * y**i for c, i in zip(cs, range(deg_lo, deg_hi + 1))) / den
    lhs = a2 * r2 + a1 * r1 + a0
    rhs = cert.subs(y, q * y) * s_ratio - cert
    expr = sp.together(sp.cancel(sp.together(lhs - rhs)))
    num = sp.expand(sp.numer(expr))
    poly = sp.Poly(num, y)
    eqs = [sp.cancel(c) for c in poly.all_coeffs()]
    sol = sp.solve(eqs, cs, dict=True)
    if not sol:
        return None
    subs = sol[0]
    if len(subs) < len(cs):
        # underdetermined: set remaining free c's to 0
        subs = {**{c: 0 for c in cs}, **subs}
    return sp.cancel(cert.subs(subs))


def main() -> int:
    t0 = time.monotonic()
    print("\n  4_1 creative-telescoping certificate search (bean pko4)\n")

    # pole structure determined by exact orbit reconstruction at (q,x)=(3/2,7):
    # poles at y = x and y = q*x, numerator ~ y (see session log / bean pko4)
    den_candidates = [
        ("(y-x)(y-qx)", (y - x) * (y - q * x)),
        ("(1-y/x)(1-q y/x)", (1 - y / x) * (1 - q * y / x)),
    ]
    cert = None
    used = None
    for dname, den in den_candidates:
        for lo, hi in ((0, 3), (-1, 3), (0, 4), (-1, 4), (-2, 4)):
            got = try_ansatz(lo, hi, den)
            if got is not None and got != 0:
                cert = got
                used = (dname, lo, hi)
                break
        if cert is not None:
            break
    if cert is None:
        print("  NO certificate in the ansatz family — enlarge ansatz (record + stop)")
        return 1
    print(f"  certificate found: denominator {used[0]}, y-degrees [{used[1]}..{used[2]}]")
    print(f"  Cert(q,x,y) = {sp.simplify(cert)}")

    # exact verification of (*)
    lhs = a2 * r2 + a1 * r1 + a0
    rhs = cert.subs(y, q * y) * s_ratio - cert
    ok_star = sp.simplify(sp.together(lhs - rhs)) == 0
    print(f"\n  (*) verified exactly?  {ok_star}")

    # (**) b(x) == -Cert(x, 1)
    ok_b = sp.simplify(sp.together(b + cert.subs(y, 1))) == 0
    print(f"  (**) b(x) == -Cert(x,1)?  {ok_b}")

    elapsed = time.monotonic() - t0
    verdict = (
        ("CERTIFICATE FOUND AND VERIFIED: the qZeilberger certificate for the "
         "4_1 annihilator exists in closed form; (*) and the boundary identity "
         "b = -Cert(x,1) both check exactly. This is the complete input for "
         "discharging the Lean general-N sorry (rational identity + telescoping "
         "sum induction) — Lean transcription is the follow-on tranche.")
        if (ok_star and ok_b) else
        "PARTIAL: certificate candidate found but a check failed — do not use."
    )
    print(f"\n  VERDICT: {verdict}\n  ({elapsed:.1f}s)")

    payload = {
        "description": (
            "Creative-telescoping (qZeilberger) certificate for the verified 4_1 "
            "annihilator: Cert(q,x,y) with a2*r2 + a1*r1 + a0 = Cert(x,qy)*s - "
            "Cert(x,y) and b = -Cert(x,1), all exact."
        ),
        "computation": "aj_figure_eight_certificate",
        "audit_only": True,
        "context": {
            "discharges": "QOU/BraidKnot/AJFigureEight.lean general-N annihilation sorry (Lean transcription = follow-on)",
            "operator_witness": "aj-figure-eight-operator-construct-verify.witness.json",
            "term": "Habiro-Le F(N,k); termwise = Newton form (Lean-proved)",
        },
        "ratios": {"s": str(sp.simplify(s_ratio)), "r1": str(sp.simplify(r1)),
                   "r2": "r1(x,y)*r1(q*x,y)"},
        "certificate": {
            "denominator": used[0], "y_degree_range": [used[1], used[2]],
            "Cert": str(sp.simplify(cert)),
        },
        "verified_star_identity": bool(ok_star),
        "verified_boundary_b_eq_neg_cert_at_1": bool(ok_b),
        "verdict": verdict,
        "tier": "structural-exact (symbolic identities; no fit)",
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = (
        WitnessBuilder.wrap_legacy(
            "aj-figure-eight-certificate", payload,
            script_path=__file__, engine="sympy",
            engine_version=sp.__version__, start_time=t0,
        )
        # The two symbolic identities this script exists to check. Both were
        # already computed above and already gate the exit code
        # (`return 0 if (ok_star and ok_b) else 1`); recording them only as
        # payload keys left the witness claiming `allPassed: true` over an
        # empty assertion list (bean `qou-srvu`). Each is exact — sympy
        # `simplify(...) == 0` — so there is no tolerance to choose.
        .add_assertion(
            "star_identity_a2r2_a1r1_a0_eq_telescoped_cert",
            ok_star, True,
            source="exact: sp.simplify(sp.together(lhs - rhs)) == 0",
        )
        .add_assertion(
            "boundary_b_eq_neg_cert_at_y_1",
            ok_b, True,
            source="exact: sp.simplify(sp.together(b + cert.subs(y, 1))) == 0",
        )
        .save()
    )
    print(f"  Witness: {out}")
    return 0 if (ok_star and ok_b) else 1


if __name__ == "__main__":
    sys.exit(main())
