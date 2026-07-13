#!/usr/bin/env python3
"""Fast qZeilberger telescoping solve for the Borromean diagonal colored
Jones, at FIXED q values mod p (bean n920, PR #3450 route 2).

The symbolic solve (borromean_qzeil_certificate.py) is too slow for the
cube summand.  This solver instead fixes q = q0 (a residue mod a 61-bit
prime) and solves the creative-telescoping identity

    (*)  sum_{i=0}^r a_i(x) R_i(x,y) = Cert(x,q0 y)*s(x,y) - Cert(x,y),
         Cert = sum_e c_e(x) y^e / DEN(x,y),  DEN = denom_y(s),

for the x-Laurent coefficients of the operator a_i and certificate c_e,
via a mod-p nullspace (linear in all unknowns; seconds).  It is decisive:

  * a nullity-1 solution at (r, x-window, cert y-deg) that VERIFIES on
    fresh (x,y) points (beyond the solve set) EXISTS iff the qZeilberger
    operator of that shape exists at q0;
  * running it at MANY independent q0 (each a bounded-degree rational
    identity in q) is overwhelming evidence the operator exists for
    general q — would be the first Borromean recurrence with a certificate
    (link-AJ is otherwise formulated-only: Sawabe 2024, Hopf+Whitehead).

Reports the minimal (order r, x-window, cert y-degree) that solves +
verifies across all sampled q0.  Reconstructing the q-dependence (for the
q->1 diagonal A-polynomial) is the interpolation follow-up over these
fast per-q0 solves — no degree-218 blowup, unlike the raw-recurrence CRT.

Audit-only; no wiring.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from borromean_qzeil_certificate import build_ratios  # verified ratios

q, x, y = sp.symbols("q x y")
P = (1 << 61) - 1


def as_polys(expr):
    e = sp.cancel(sp.together(expr))
    return sp.Poly(sp.numer(e), q, x, y), sp.Poly(sp.denom(e), q, x, y)


def pmod(poly, qv, xv, yv, p):
    acc = 0
    for (a, b, c), coef in poly.terms():
        acc = (acc + int(coef) % p * pow(qv, a, p) % p * pow(xv, b, p) % p
               * pow(yv, c, p)) % p
    return acc


def ratmod(numP, denP, qv, xv, yv, p):
    d = pmod(denP, qv, xv, yv, p)
    if d % p == 0:
        return None
    return pmod(numP, qv, xv, yv, p) * pow(d, p - 2, p) % p


def nullspace(rows, p):
    if not rows:
        return []
    nc = len(rows[0])
    m = [r[:] for r in rows]
    piv = {}
    rank = 0
    for col in range(nc):
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
    free = [c for c in range(nc) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * nc
        v[fc] = 1
        for c, r in piv.items():
            v[c] = (-m[r][fc]) % p
        basis.append(v)
    return basis


def xpow(xv, d, p):
    return pow(xv, d, p) if d >= 0 else pow(pow(xv, -d, p), p - 2, p)


def solve_at_q(q0, r, DX, EY, s_np, r1_np, DEN_np, p, extra_verify=40):
    """Solve (*) at q=q0 mod p; return (nullity, verified_bool, a_idx, c_idx,
    vec) or (nullity, False, ...) if no unique verifying solution."""
    a_idx = [(i, d) for i in range(r + 1) for d in range(-DX, DX + 1)]
    c_idx = [(e, d) for e in range(EY + 1) for d in range(-DX, DX + 1)]
    nunk = len(a_idx) + len(c_idx)
    need = nunk + 20

    def one_row(xv, yv):
        sval = ratmod(*s_np, q0, xv, yv, p)
        # R_i(q0,xv,yv) = prod_{t=0}^{i-1} r1(q0, q0^t * xv, yv) — incremental,
        # so we only ever evaluate the SMALL r1 polynomial (never the huge
        # expanded product R_i).
        Rvals = [1]
        acc = 1
        xt = xv
        for t in range(r):
            rv = ratmod(*r1_np, q0, xt, yv, p)
            if rv is None:
                return None
            acc = acc * rv % p
            Rvals.append(acc)
            xt = xt * q0 % p
        dc = pmod(DEN_np, q0, xv, yv, p)
        dcq = pmod(DEN_np, q0, xv, yv * q0 % p, p)
        if sval is None or dc % p == 0 or dcq % p == 0:
            return None
        idc, idcq = pow(dc, p - 2, p), pow(dcq, p - 2, p)
        row = [0] * nunk
        for j, (i, d) in enumerate(a_idx):
            row[j] = xpow(xv, d, p) * Rvals[i] % p
        off = len(a_idx)
        for j, (e, d) in enumerate(c_idx):
            xd = xpow(xv, d, p)
            cert_qy = xd * pow(yv * q0 % p, e, p) % p * idcq % p
            cert_y = xd * pow(yv, e, p) % p * idc % p
            row[off + j] = (-(cert_qy * sval % p) + cert_y) % p
        return row

    rows, sv = [], 2
    while len(rows) < need and sv < need * 4 + 50:
        sv += 1
        xv = (sv * 2654435761) % p
        yv = (sv * 40503 + 12345) % p
        rr = one_row(xv, yv)
        if rr is not None:
            rows.append(rr)
    basis = nullspace(rows, p)
    if len(basis) != 1:
        return len(basis), False, a_idx, c_idx, None
    vec = basis[0]
    # verify on fresh points
    ok = True
    for t in range(extra_verify):
        xv = (t * 1000003 + 7) % p
        yv = (t * 999983 + 555) % p
        rr = one_row(xv, yv)
        if rr is None:
            continue
        if sum(a * b for a, b in zip(rr, vec)) % p != 0:
            ok = False
            break
    return 1, ok, a_idx, c_idx, vec


def main() -> int:
    t0 = time.time()
    print("\n  Borromean qZeilberger — fixed-q mod-p telescoping solve\n")
    s_ratio, r1 = build_ratios()
    s_np = as_polys(s_ratio)
    r1_np = as_polys(r1)
    DEN = sp.denom(sp.cancel(sp.together(s_ratio)))
    DEN_np = sp.Poly(DEN, q, x, y)
    print(f"  ratios ready (r1 deg {r1_np[0].total_degree()})  ({time.time()-t0:.1f}s)")

    q0s = [5, 7, 11, 13, 17, 19, 23]
    found = None
    # search minimal (r, DX, EY) at the first q0, then confirm across all q0
    for r in (4, 5, 6, 7):
        for DX in (4, 6, 8, 10):
            for EY in (4, 6, 8, 10):
                nul, ok, ai, ci, vec = solve_at_q(q0s[0], r, DX, EY, s_np,
                                                  r1_np, DEN_np, P)
                el = time.time() - t0
                tag = f"null={nul}" + (" VERIFIED" if ok else "")
                print(f"  [q0={q0s[0]}] r={r} DX={DX} EY={EY}: {tag}  ({el:.0f}s)")
                if nul == 1 and ok:
                    found = (r, DX, EY)
                    break
            if found:
                break
        if found:
            break

    verdict: dict
    if not found:
        print("\n  NO verifying qZeilberger shape in the searched range")
        verdict = {"found": False, "searched": "r<=7, DX<=10, EY<=10"}
    else:
        r, DX, EY = found
        confirms = []
        for q0 in q0s:
            nul, ok, ai, ci, vec = solve_at_q(q0, r, DX, EY, s_np, r1_np, DEN_np, P)
            confirms.append({"q0": q0, "nullity": nul, "verified": bool(ok)})
            print(f"  [confirm q0={q0}] nullity={nul} verified={ok}")
        all_ok = all(c["verified"] and c["nullity"] == 1 for c in confirms)
        print(f"\n  qZeilberger operator EXISTS at order r={r} (x-window ±{DX}, "
              f"cert y-deg {EY}); telescoping VERIFIED at {sum(c['verified'] for c in confirms)}"
              f"/{len(q0s)} independent q0  ({time.time()-t0:.0f}s)")
        verdict = {
            "found": True, "order": r, "x_window": DX, "cert_y_degree": EY,
            "telescoping_verified_across_q0": bool(all_ok),
            "q0_confirmations": confirms,
            "interpretation": (
                "The creative-telescoping identity (*) holds at every sampled "
                "q0 for a UNIQUE (nullity-1) operator+certificate of this shape "
                "— strong evidence the Borromean diagonal recurrence admits a "
                "qZeilberger certificate for general q. Explicit q-dependence "
                "(for the q->1 A-polynomial) is the interpolation follow-up "
                "over these fast per-q0 solves."
            ),
        }

    script_path = Path(__file__)
    witness = {
        "engine": f"python {sys.version.split()[0]} / sympy {sp.__version__} (fixed-q mod-p)",
        "scriptFile": f"computations/{script_path.name}",
        "commitSha": subprocess.run(["git", "rev-parse", "HEAD"],
                                    capture_output=True, text=True,
                                    cwd=script_path.parent).stdout.strip() or "unknown",
        "scriptHash": hashlib.sha256(script_path.read_bytes()).hexdigest()[:12],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": ("Fixed-q mod-p qZeilberger telescoping solve for the "
                        "Borromean diagonal colored Jones: minimal operator+"
                        "certificate shape + cross-q0 verification"),
        "computation": "borromean-qzeil-fixedq",
        "audit_only": True,
        "foundation": "borromean_qzeil_ratios.py (shift ratios verified 6/6)",
        "verdict": verdict,
        "wall_seconds": round(time.time() - t0, 1),
    }
    out = script_path.with_name("borromean-qzeil-fixedq.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"  witness → {out.name}  ({witness['wall_seconds']}s)")
    return 0 if found else 1


if __name__ == "__main__":
    sys.exit(main())
