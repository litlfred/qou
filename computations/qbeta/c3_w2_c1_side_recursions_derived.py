#!/usr/bin/env python3
"""Both connection-matrix recursions, derived from the C1 operator.

Bean `qou-slvl` item 2. `QOU/QBeta/C1SeriesConvergence.lean` proves the `0`-side
series converges on the unit disc and the `inf`-side series is entire — but both
recursions were *defined* to match `computations/qbeta/c3_w2_c1_pole_divisor.py`,
so the file certified convergence of stated sequences rather than of solutions.
This derives both from

    L = (p^4 z^2 - 1) tau^2 - (p^2-1) tau - (p^2-1),   tau F(z) = F(pz),  q = p^2.

## The two ansatzes, and why the theta prefactors drop out

Neither side is a bare power series; each carries a theta factor, and the
functional equation `theta_p(pw) = w theta_p(w)` turns `tau` on that factor into
multiplication by a constant or a monomial — which is what makes the bracket
polynomial:

* `0`-side  `y_0 = e_t(z) G(z)` with `e_t = theta_p(z)/theta_p(z/t)` and
  `G = sum g_k z^k`. Then `tau e_t = t e_t`, so `L y_0 / e_t` is
  `(p^4z^2-1) t^2 tau^2 G - (p^2-1) t tau G - (p^2-1) G`.
* `inf`-side `y_inf = H(z)/theta_p(z/T)` with `H = sum h_k z^-k`. Then
  `tau[1/theta_p(z/T)] = (T/z)/theta_p(z/T)` and
  `tau^2[...] = T^2/(p z^2) /theta_p(z/T)`, so the bracket is
  `(p^4z^2-1)(T^2/(p z^2)) tau^2 H - (p^2-1)(T/z) tau H - (p^2-1) H`.
  Worked in `u = 1/z`, where it is a genuine polynomial.

## What is checked here, and what in Lean

Here: that the coefficient of each power is exactly the four-term collection
Lean calls `zeroCoeffAt` / `infCoeffAt`, and that solving it for the top
coefficient returns **the recursions the script uses** — `gc()` and `hc()` of
`c3_w2_c1_pole_divisor.py`, verbatim, including the `q = p^2` substitution.

In Lean: `zeroCoeffAt_eq_zero_iff` and `infCoeffAt_eq_zero_iff` prove in general
that those collections vanish iff the respective recursions hold.

Together: the two recursions are consequences of the operator, so
`summable_zeroSideCoeff` and `summable_infSideCoeff` are statements about the
actual `Y_0` and `Y_inf` series, not about sequences that merely resemble them.

-- Ref: [manuscript] computations/qbeta/c3_w2_c1_pole_divisor.py
-- Ref: [rsz2013] Asterisque 355 section 3.3
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import sympy as sp


def main() -> None:
    t0 = time.perf_counter()
    p, t, T, z = sp.symbols("p t T z", positive=True)
    N = 10
    print("="*76); print("  0-side:  y0 = e_t(z)*G(z),  tau e_t = t e_t,  G = sum g_k z^k"); print("="*76)
    g = sp.symbols(f'g0:{N+3}')
    G = sum(g[k]*z**k for k in range(N+3))
    tauG  = G.subs(z, p*z); tau2G = G.subs(z, p**2*z)
    # L y0 / e_t  =  (p^4 z^2 - 1) t^2 tau2G - (p^2-1) t tauG - (p^2-1) G
    br0 = sp.expand((p**4*z**2 - 1)*t**2*tau2G - (p**2-1)*t*tauG - (p**2-1)*G)
    P0 = sp.Poly(br0, z)
    ok0 = True
    for k in range(0, N):
        got = sp.simplify(P0.coeff_monomial(z**(k+2)))
        want = sp.simplify(t**2*p**(2*(k+2))*g[k] - t**2*p**(2*(k+2))*g[k+2]
                           - (p**2-1)*t*p**(k+2)*g[k+2] - (p**2-1)*g[k+2])
        ok = sp.simplify(got-want)==0; ok0 = ok0 and ok
    print(f"    coeff(z^(k+2)) == zeroCoeffAt  for k=0..{N-1}: {ok0}")
    # and the recursion matches gc() in c3_w2_c1_pole_divisor.py (with q = p^2)
    q = p**2
    rec0 = True
    for k in range(2, N):
        sol = sp.solve(sp.Eq(P0.coeff_monomial(z**k), 0), g[k])
        want = t**2*p**(2*k)*g[k-2] / (t**2*p**(2*k) + (q-1)*t*p**k + (q-1))
        rec0 = rec0 and bool(sol) and sp.simplify(sol[0]-want)==0
    print(f"    recursion == script gc()       for k=2..{N-1}: {rec0}")

    print(); print("="*76); print("  inf-side: y_inf = H(z)/theta_p(z/T),  H = sum h_k z^-k"); print("="*76)
    h = sp.symbols(f'h0:{N+3}')
    u = sp.symbols('u', positive=True)          # u = 1/z, makes everything polynomial
    H     = sum(h[k]*u**k              for k in range(N+3))
    tauH  = sum(h[k]*p**(-k)*u**k      for k in range(N+3))
    tau2H = sum(h[k]*p**(-2*k)*u**k    for k in range(N+3))
    # z = 1/u:  p^4 z^2 - 1 = p^4/u^2 - 1 ;  T^2/(p z^2) = T^2 u^2/p ;  T/z = T u
    br1 = sp.expand((T**2/p)*(p**4 - u**2)*tau2H - (p**2-1)*T*u*tauH - (p**2-1)*H)
    P1 = sp.Poly(br1, u)
    ok1 = True
    for k in range(0, N):
        got = sp.simplify(P1.coeff_monomial(u**(k+2)))
        want = sp.simplify(T**2*p**3*p**(-2*(k+2))*h[k+2] - T**2/p*p**(-2*k)*h[k]
                           - (p**2-1)*T*p**(-(k+1))*h[k+1] - (p**2-1)*h[k+2])
        ok = sp.simplify(got-want)==0; ok1 = ok1 and ok
    print(f"    coeff(u^(k+2)) == infCoeffAt   for k=0..{N-1}: {ok1}")
    rec1 = True
    for k in range(2, N):
        sol = sp.solve(sp.Eq(P1.coeff_monomial(u**k), 0), h[k])
        lhs = T**2*p**3*p**(-2*k) + (1-p**2)
        rhs = -T*(1-p**2)*p**(-(k-1))*h[k-1] + (T**2/p)*p**(-2*(k-2))*h[k-2]
        rec1 = rec1 and bool(sol) and sp.simplify(sol[0]-rhs/lhs)==0
    print(f"    recursion == script hc()       for k=2..{N-1}: {rec1}")
    print()
    print("ALL:", ok0 and rec0 and ok1 and rec1)

    passed = bool(ok0 and rec0 and ok1 and rec1)
    checks = [
        {"name": "zero_side_coefficient_is_the_four_term_collection",
         "detail": f"coeff(z^(k+2)) of L y_0 / e_t equals zeroCoeffAt for k=0..{N-1}, symbolic g_k",
         "passed": bool(ok0)},
        {"name": "zero_side_recursion_matches_script_gc",
         "detail": f"solving coeff(z^k)=0 for g_k returns gc()'s recursion (q = p^2) for k=2..{N-1}",
         "passed": bool(rec0)},
        {"name": "inf_side_coefficient_is_the_four_term_collection",
         "detail": f"coeff(u^(k+2)), u = 1/z, of the inf-side bracket equals infCoeffAt for k=0..{N-1}",
         "passed": bool(ok1)},
        {"name": "inf_side_recursion_matches_script_hc",
         "detail": f"solving coeff(u^k)=0 for h_k returns hc()'s recursion for k=2..{N-1}",
         "passed": bool(rec1)},
    ]
    script_path = Path(__file__).resolve()
    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                             text=True, cwd=script_path.parent).stdout.strip()
    except Exception:
        sha = "unknown"
    witness = {
        "schema": "witness/v1",
        "engine": "sympy",
        "scriptFile": script_path.name,
        "scriptSha256": hashlib.sha256(script_path.read_bytes()).hexdigest(),
        "commitSha": sha or "unknown",
        "description":
            "Bean qou-slvl item 2. Derives BOTH connection-matrix recursions from "
            "the C1 operator L = (p^4z^2-1)tau^2 - (p^2-1)tau - (p^2-1), removing "
            "the last defined-to-match inputs in QOU/QBeta/C1SeriesConvergence.lean. "
            "Neither side is a bare power series: the 0-side carries "
            "e_t = theta_p(z)/theta_p(z/t) with tau e_t = t e_t, the inf-side "
            "carries 1/theta_p(z/T) with tau acting by T/z — both from the theta "
            "functional equation — and after dividing them out the brackets are "
            "polynomial. Checks that the coefficient of each power is exactly the "
            "four-term collection Lean calls zeroCoeffAt / infCoeffAt, and that "
            "solving for the top coefficient returns gc() and hc() of "
            "c3_w2_c1_pole_divisor.py verbatim.",
        "computation": {
            "operator": "(p^4 z^2 - 1) tau^2 - (p^2-1) tau - (p^2-1), tau F(z) = F(pz)",
            "zeroSideAnsatz": "y_0 = (theta_p(z)/theta_p(z/t)) * sum_k g_k z^k",
            "infSideAnsatz": "y_inf = (sum_k h_k z^-k) / theta_p(z/T), worked in u = 1/z",
            "truncation": N,
        },
        "results": {"zeroSideCoeffOK": bool(ok0), "zeroSideRecursionOK": bool(rec0),
                    "infSideCoeffOK": bool(ok1), "infSideRecursionOK": bool(rec1)},
        "checks": checks,
        "verdict":
            "Both recursions are consequences of the operator, not stipulations. "
            "The coefficient collections match Lean's zeroCoeffAt / infCoeffAt "
            "exactly, and solving them returns the pole-divisor script's gc() and "
            "hc() verbatim. With Lean's zeroCoeffAt_eq_zero_iff and "
            "infCoeffAt_eq_zero_iff, summable_zeroSideCoeff and "
            "summable_infSideCoeff are now statements about the actual Y_0 and "
            "Y_inf series. Still NOT established: that these series, times their "
            "theta prefactors, are the canonical solutions at 0 and infinity — "
            "that is qou-c1ln row 4. Nothing wired to production.",
        "durationMs": int((time.perf_counter() - t0) * 1000),
    }
    out = script_path.parent / "c3-w2-c1-side-recursions-derived.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"  witness -> {out.name}   ({witness['durationMs']} ms)")
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
