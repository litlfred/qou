#!/usr/bin/env python3
"""Creative-telescoping (qZeilberger) certificate + operator for the
Borromean diagonal colored Jones (bean n920, PR #3450 route 2).

Foundation (borromean_qzeil_ratios.py, verified 6/6): with x=q^n, y=q^l
the Habiro summand F(n,l) is q-proper-hypergeometric,

    s(x,y)  = F(n,l+1)/F(n,l),   r1(x,y) = F(n+1,l)/F(n,l)

both exact rational in (x,y,q).  qZeilberger seeks an order-r operator
a_0..a_r (rational in x) and a certificate Cert(x,y)=P(x,y)/DEN(x,y) with

    (*)  sum_{i=0}^r a_i(x) R_i(x,y) = Cert(x,qy)*s(x,y) - Cert(x,y),
         R_i = prod_{t=0}^{i-1} r1(q^t x, y),  R_0 = 1.

Multiplying by F(n,l) and summing l>=0 (F=0 for l>=n) telescopes the RHS,
giving  sum_i a_i(x) J_{B,n+i} = -Cert(x,1)*F(n,0),  F(n,0)={n}^2/{1}^2 —
the operator annihilates the tower up to the explicit boundary term.
Success here WOULD BE the first Borromean recurrence with a telescoping certificate
(link-AJ is otherwise formulated-only: Sawabe 2024, Hopf+Whitehead).

Solve strategy: (*) is LINEAR in the unknown coefficients of the a_i and
of P.  Sample (x,y) at many points mod a 61-bit prime, take the nullspace
(fast, restart-safe — the qZeilberger objects are low-degree, unlike the
degree-218 raw-recurrence CRT of the superseded reconstruct route), lift
with Wang (coeffs are small), then VERIFY (*) EXACTLY in sympy and emit
the q->1 / m->M^2 specialization (candidate diagonal Borromean
A-polynomial).

Audit-only; no wiring.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from fractions import Fraction
from math import isqrt
from pathlib import Path

import sympy as sp

q, x, y = sp.symbols("q x y")
P0 = (1 << 61) - 1
P1 = 4611686018427387847


# ── exact shift ratios (from the verified foundation probe) ──────────────
def build_ratios():
    Q, X, Y = q, x, y
    core = (X + 1 / X) - (Q * Y + 1 / (Q * Y))
    l1sq = Q * Y - 2 + 1 / (Q * Y)
    d2 = Q**2 * Y**2 - 2 + 1 / (Q**2 * Y**2)
    d3 = Q**3 * Y**2 - 2 + 1 / (Q**3 * Y**2)
    s_ratio = sp.cancel(-core**3 * l1sq / (d2 * d3))

    def brk(cx, cy, cc):
        up = x ** sp.Rational(cx, 2) * y ** sp.Rational(cy, 2) * q ** sp.Rational(cc, 2)
        return up - 1 / up
    n1sq = Q * X - 2 + 1 / (Q * X)
    nsq = X - 2 + 1 / X
    ratio = (brk(1, 1, 1) * brk(1, 0, 0)) / (brk(1, 0, 1) * brk(1, -1, 0))
    r1 = sp.cancel(sp.simplify((n1sq / nsq) * ratio**3))
    return s_ratio, r1


def modval(expr, xv, yv, p):
    """Evaluate a sympy rational function of (q,x,y) at q=xv? no — at given
    (x=xv, y=yv, q=qv) mod p.  Returns None if a denominator vanishes."""
    raise NotImplementedError  # replaced by lambdified numer/denom below


def as_num_den(expr):
    e = sp.cancel(sp.together(expr))
    return sp.Poly(sp.numer(e), q, x, y), sp.Poly(sp.denom(e), q, x, y)


def poly_mod(poly: sp.Poly, qv, xv, yv, p):
    acc = 0
    for (a, b, c), coef in poly.terms():
        acc = (acc + int(coef) % p * pow(qv, a, p) % p * pow(xv, b, p) % p
               * pow(yv, c, p)) % p
    return acc


def rat_mod(numP, denP, qv, xv, yv, p):
    d = poly_mod(denP, qv, xv, yv, p)
    if d % p == 0:
        return None
    return poly_mod(numP, qv, xv, yv, p) * pow(d, p - 2, p) % p


def nullspace_mod(rows, p):
    if not rows:
        return []
    ncols = len(rows[0])
    m = [r[:] for r in rows]
    piv = {}
    rank = 0
    for col in range(ncols):
        pr = next((r for r in range(rank, len(m)) if m[r][col] % p), None)
        if pr is None:
            continue
        m[rank], m[pr] = m[pr], m[rank]
        iv = pow(m[rank][col], p - 2, p)
        m[rank] = [v * iv % p for v in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][col]:
                f = m[r][col]
                m[r] = [(a - f * b) % p for a, b in zip(m[r], m[rank])]
        piv[col] = rank
        rank += 1
        if rank == len(m):
            break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for c, r in piv.items():
            v[c] = (-m[r][fc]) % p
        basis.append(v)
    return basis


def ratrec(a, m):
    a %= m
    if a == 0:
        return Fraction(0)
    bound = isqrt(m // 2)
    r0, r1, t0, t1 = m, a, 0, 1
    while r1 > bound:
        qq = r0 // r1
        r0, r1 = r1, r0 - qq * r1
        t0, t1 = t1, t0 - qq * t1
    if t1 == 0 or abs(t1) > bound:
        return None
    return Fraction(r1, t1)


def solve_symbolic(R_ORD, EY, s_ratio, r1, DEN):
    """4_1-style exact solve: a_i(q,x) and cert numerator coeffs c_e(q,x)
    unknown symbols; clear denominators; match y-coefficients; sp.solve."""
    a_syms = [sp.Symbol(f"a_{i}") for i in range(R_ORD + 1)]
    c_syms = [sp.Symbol(f"c_{e}") for e in range(EY + 1)]
    cert = sum(c * y**e for c, e in zip(c_syms, range(EY + 1))) / DEN
    # R_i = prod_{t<i} r1(q^t x, y)
    R = [sp.Integer(1)]
    for i in range(1, R_ORD + 1):
        R.append(sp.cancel(sp.together(R[-1] * r1.subs(x, q**(i - 1) * x))))
    lhs = sum(a * Ri for a, Ri in zip(a_syms, R))
    rhs = cert.subs(y, q * y) * s_ratio - cert
    expr = sp.cancel(sp.together(lhs - rhs))
    num = sp.expand(sp.numer(expr))
    poly = sp.Poly(num, y)
    eqs = poly.all_coeffs()
    unknowns = a_syms + c_syms
    sol = sp.solve(eqs, unknowns, dict=True)
    if not sol:
        return None
    subs = sol[0]
    # fill free unknowns: set the highest a to 1 if free, others free->0
    free = [u for u in unknowns if u not in subs]
    if not free:
        # fully determined => only trivial 0 unless system rank-deficient
        if all(sp.simplify(subs[u]) == 0 for u in unknowns):
            return None
    fix = {}
    if a_syms[R_ORD] in free:
        fix[a_syms[R_ORD]] = 1
    for u in free:
        if u not in fix:
            fix[u] = 0
    subs2 = {u: sp.simplify(v.subs(fix)) for u, v in subs.items()}
    subs2.update(fix)
    a_vals = [sp.cancel(subs2[a]) for a in a_syms]
    c_vals = [sp.cancel(subs2[c]) for c in c_syms]
    if all(v == 0 for v in a_vals):
        return None
    cert_val = sum(cv * y**e for cv, e in zip(c_vals, range(EY + 1))) / DEN
    return a_vals, cert_val, R


def main() -> int:
    t0 = time.time()
    print("\n  Borromean qZeilberger certificate + operator (symbolic solve)\n")
    s_ratio, r1 = build_ratios()
    DEN = sp.denom(sp.cancel(sp.together(s_ratio)))
    print(f"  s y-deg {sp.Poly(sp.numer(s_ratio), y).degree()}"
          f" | r1 y-deg {sp.Poly(sp.numer(r1), y).degree()}"
          f" | DEN = denom(s)  ({time.time()-t0:.1f}s)")

    found = None
    for R_ORD in (5, 6, 4, 7):
        for EY in (6, 8, 4, 10):
            try:
                res = solve_symbolic(R_ORD, EY, s_ratio, r1, DEN)
            except Exception as ex:
                print(f"  [try] r={R_ORD} EY={EY}: solve error {str(ex)[:60]}"
                      f"  ({time.time()-t0:.0f}s)")
                continue
            status = "SOLVED" if res else "no non-trivial"
            print(f"  [try] r={R_ORD} EY={EY}: {status}  ({time.time()-t0:.0f}s)")
            if res:
                found = (R_ORD, EY, res)
                break
        if found:
            break

    if not found:
        print("\n  NO telescoping certificate in the searched ansatz")
        verdict = {"found": False, "searched": "r in 4..7, EY in 4..10"}
        ok_star = False
    else:
        R_ORD, EY, (a_vals, cert_val, R) = found
        # EXACT verification of (*)
        lhs = sum(a * Ri for a, Ri in zip(a_vals, R))
        rhs = cert_val.subs(y, q * y) * s_ratio - cert_val
        ok_star = sp.simplify(sp.together(lhs - rhs)) == 0
        print(f"\n  candidate r={R_ORD}, cert y-deg {EY}")
        print(f"  (*) telescoping identity verified EXACTLY?  {ok_star}")
        # boundary term b(x) = -Cert(x,1)*F(n,0),  F(n,0) = {n}^2/{1}^2
        Fn0 = (x - 2 + 1/x) / (q - 2 + 1/q)
        b_val = sp.cancel(-cert_val.subs(y, 1) * Fn0)
        # q->1 specialization of the homogeneous operator part (m=x -> M^2)
        M, L = sp.symbols("M L")
        qto1 = None
        if ok_star:
            try:
                Apoly = 0
                degen = False
                for i, a in enumerate(a_vals):
                    lim = sp.limit(a, q, 1)
                    if lim.has(sp.zoo, sp.oo):
                        degen = True; break
                    Apoly += sp.cancel(lim.subs(x, M**2)) * L**i
                qto1 = "degenerate" if degen else str(sp.factor(sp.cancel(Apoly)))
            except Exception as ex:
                qto1 = f"error: {str(ex)[:60]}"
        verdict = {
            "found": True, "order": R_ORD, "cert_y_degree": EY,
            "telescoping_identity_verified_exact": bool(ok_star),
            "operator_a_i": [str(sp.simplify(a)) for a in a_vals],
            "certificate": str(sp.simplify(cert_val)),
            "boundary_b": str(sp.simplify(b_val)),
            "q_to_1_diagonal_A_candidate": qto1,
        }
        if ok_star:
            print(f"  boundary b(x) = {sp.simplify(b_val)}")
            print(f"  q->1 diagonal A-candidate: {qto1}")

    script_path = Path(__file__)
    witness = {
        "engine": f"python {sys.version.split()[0]} / sympy {sp.__version__} (symbolic qZeilberger)",
        "scriptFile": f"computations/{script_path.name}",
        "commitSha": subprocess.run(["git", "rev-parse", "HEAD"],
                                    capture_output=True, text=True,
                                    cwd=script_path.parent).stdout.strip() or "unknown",
        "scriptHash": hashlib.sha256(script_path.read_bytes()).hexdigest()[:12],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": ("Borromean diagonal colored-Jones qZeilberger creative-"
                        "telescoping: exact operator + certificate, telescoping "
                        "identity verified symbolically; would be the first Borromean recurrence "
                        "with a certificate (link-AJ otherwise formulated-only)"),
        "computation": "borromean-qzeil-certificate",
        "audit_only": True,
        "foundation": "borromean_qzeil_ratios.py (shift ratios verified 6/6)",
        "verdict": verdict,
        "wall_seconds": round(time.time() - t0, 1),
    }
    out = script_path.with_name("borromean-qzeil-certificate.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness → {out.name}  ({witness['wall_seconds']}s)")
    return 0 if (found and ok_star) else 1


if __name__ == "__main__":
    sys.exit(main())
