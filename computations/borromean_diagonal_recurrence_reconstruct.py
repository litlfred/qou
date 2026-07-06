#!/usr/bin/env python3
"""Phase 2: symbolic reconstruction of the Borromean diagonal recurrence.

Input: the existence certificates from borromean_diagonal_recurrence_hunt
((5,13), nullity 2) and the follow-up higher-order scan: the UNIQUE
(nullity-1) window (r, W) = (6, 11) — 184 unknowns, canonical operator
up to scale — is the reconstruction target.

Output sought: an explicit operator

    sum_{i=0}^{6} a_i(q, m) J_{B,n+i} = b(q, m),   m = q^n,

with a_i, b in Q(q)[m^{±1}] reconstructed as exact symbolic objects,
then VERIFIED by exact symbolic annihilation against the sympy Habiro
tower (the epistemic step — the fit below is mod-p at sampled q; the
verification is symbolic in q at every checked n), then specialized at
q -> 1 (m -> M^2) to a candidate diagonal Borromean A-polynomial.

Method:
  A. At the Mersenne prime p0 = 2^61 - 1, sample many base points s;
     for each, evaluate the tower mod p0, build the (r,W)-system on
     R fit rows, and compute the REDUCED-ECHELON nullspace basis.
     With a stable pivot structure across samples, the RREF basis
     vectors v1, v2 are CANONICAL rational functions of q = s^2
     evaluated at the sample — entry-wise reconstructable.
  B. For each matrix column c, fit v1[c](q) = P_c(q)/Q_c(q) over F_p0
     by linear algebra (increasing degree until an exact fit validates
     on held-out samples).
  C. Clear denominators -> polynomial coefficient vector; normalize;
     lift the F_p0 polynomial coefficients to Q by rational
     reconstruction (Wang); on failure, CRT with two more primes.
  D. Exact symbolic verification (sympy, s = q^{1/2}): the
     reconstructed operator must annihilate J_{B,n} EXACTLY for all
     checked n (n = 1..Nver), symbolically in q.
  E. q -> 1 specialization of the homogeneous part under m -> M^2.

Honesty: stages A-C are reconstruction heuristics; stage D alone is
the claim-bearing step.  If D fails the run reports the failure — no
partial claim.  Audit-only; no wiring.

RUN RECORD (2026-07-06/07, PR #3443): Stage B fails at DEG_MAX = 118 on
both (5,13) and (6,11) — and a bisected degree probe (1260 samples,
column 6 of the (6,11) window) measured the canonical entry's rational
degree at ~218 (fits at 219±6, excluded at ≤150).  Full reconstruction
therefore needs ~460+ samples/prime with degree-470 eliminations across
184 columns AND multi-prime CRT for the integer lift (single 61-bit
Wang is insufficient at this scale) — recorded in bean n920 as the
phase-2 compute project (Python-mp overnight / Rust tranche /
qZeilberger).  This scaffold is committed as the reproducible method +
run record; the existence certificate (hunt witness) is unaffected.
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

R_ORD = 6
W_WIN = 11
NCOLS = (R_ORD + 2) * (2 * W_WIN + 1)   # 189: blocks a_0..a_5 then b
P0 = (1 << 61) - 1
P1 = 4611686018427387847
P2 = 9223372036854775783
NSAMP = 262          # base points at p0
NHOLD = 12           # held-out validation samples per entry fit
DEG_MAX = 118         # max numerator/denominator degree tried in q
NVER = 16            # symbolic verification range n = 1..NVER


def jones_tower_mod(p: int, s: int, nmax: int) -> list[int] | None:
    sinv = pow(s, p - 2, p)
    br = [0] * (2 * nmax + 2)
    sj, sij = 1, 1
    for j in range(1, 2 * nmax + 2):
        sj = sj * s % p
        sij = sij * sinv % p
        br[j] = (sj - sij) % p
        if br[j] == 0:
            return None
    out = []
    for n in range(1, nmax + 1):
        total = 0
        prod3 = 1
        for l in range(0, n):
            if l > 0:
                f = br[n + l] * br[n - l] % p
                prod3 = prod3 * f % p * f % p * f % p
            den = 1
            for j in range(l + 1, 2 * l + 2):
                den = den * br[j] % p
            den2inv = pow(den * den % p, p - 2, p)
            term = br[n] * br[n] % p * prod3 % p * den2inv % p
            total = (total - term if l & 1 else total + term) % p
        out.append(total)
    return out


def build_rows(J, p, s, n_lo, n_hi):
    rows = []
    q = s * s % p
    for n in range(n_lo, n_hi + 1):
        m = pow(q, n, p)
        minv = pow(m, p - 2, p)
        mk = {0: 1}
        for k in range(1, W_WIN + 1):
            mk[k] = mk[k - 1] * m % p
            mk[-k] = mk[-(k - 1)] * minv % p
        row = []
        for i in range(R_ORD + 1):
            Jni = J[n + i - 1]
            for k in range(-W_WIN, W_WIN + 1):
                row.append(mk[k] * Jni % p)
        for k in range(-W_WIN, W_WIN + 1):
            row.append((-mk[k]) % p)
        rows.append(row)
    return rows


def rref_nullspace(rows, p):
    """RREF nullspace basis + pivot tuple (canonical given column order)."""
    ncols = len(rows[0])
    m = [r[:] for r in rows]
    pivots = {}
    rank = 0
    for col in range(ncols):
        piv = next((r for r in range(rank, len(m)) if m[r][col] % p), None)
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        inv = pow(m[rank][col], p - 2, p)
        m[rank] = [x * inv % p for x in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][col]:
                f = m[r][col]
                m[r] = [(a - f * b) % p for a, b in zip(m[r], m[rank])]
        pivots[col] = rank
        rank += 1
        if rank == len(m):
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for c, r in pivots.items():
            v[c] = (-m[r][fc]) % p
        basis.append(v)
    return basis, tuple(sorted(pivots)), free


def fit_rational(qs, ys, p, holdq, holdy):
    """Fit y(q) = P(q)/Q(q) over F_p, minimal degree, validated on holdout.
    Returns (Pcoeffs, Qcoeffs) lowest-degree-first, or None."""
    for D in range(0, DEG_MAX + 1):
        # unknowns: p_0..p_D, u_0..u_D (Q monic-ish: fix u_D = 1 fallback
        # via nullspace instead: solve homogeneous system in 2D+2 unknowns)
        need = 2 * D + 3
        if need > len(qs):
            return None
        rows = []
        for qv, yv in zip(qs[:need], ys[:need]):
            qp = [1]
            for _ in range(D):
                qp.append(qp[-1] * qv % p)
            row = qp + [(-yv * t) % p for t in qp]
            rows.append(row)
        basis, _, _ = rref_nullspace(rows, p)
        if not basis:
            continue
        v = basis[0]
        P, Q = v[: D + 1], v[D + 1:]
        if all(x == 0 for x in Q):
            continue
        ok = True
        for qv, yv in zip(holdq, holdy):
            qp = [1]
            for _ in range(D):
                qp.append(qp[-1] * qv % p)
            num = sum(c * t for c, t in zip(P, qp)) % p
            den = sum(c * t for c, t in zip(Q, qp)) % p
            if den == 0 or num * pow(den, p - 2, p) % p != yv % p:
                ok = False
                break
        if ok:
            return P, Q
    return None


def ratrec(a: int, m: int):
    """Wang rational reconstruction of a mod m -> Fraction or None."""
    a %= m
    if a == 0:
        return Fraction(0)
    bound = isqrt(m // 2)
    r0, r1 = m, a
    t0, t1 = 0, 1
    while r1 > bound:
        qq = r0 // r1
        r0, r1 = r1, r0 - qq * r1
        t0, t1 = t1, t0 - qq * t1
    if abs(t1) > bound or r1 == 0 and t1 == 0:
        return None
    if t1 == 0:
        return None
    fr = Fraction(r1, t1)
    return fr


def main() -> int:
    t0 = time.time()
    print("\n  Borromean recurrence phase 2 — symbolic reconstruction\n")
    R_FIT = NCOLS + 20
    nmax = R_FIT + R_ORD

    # ── Stage A: sample RREF nullspaces at p0 ──────────────────────────
    samples = []       # (q mod p0, {col: val for v1}) with majority pivots
    pivot_count: dict = {}
    raw = []
    sv = 2
    while len(raw) < NSAMP:
        sv += 1
        J = jones_tower_mod(P0, sv, nmax)
        if J is None:
            continue
        rows = build_rows(J, P0, sv, 1, R_FIT)
        basis, piv, free = rref_nullspace(rows, P0)
        if len(basis) != 1:
            continue
        raw.append((sv, piv, free, basis))
        pivot_count[piv] = pivot_count.get(piv, 0) + 1
        if len(raw) % 40 == 0:
            print(f"  [A] {len(raw)}/{NSAMP} samples  ({time.time()-t0:.0f}s)")
    piv_major = max(pivot_count, key=pivot_count.get)
    kept = [(sv, basis) for sv, piv, free, basis in raw if piv == piv_major]
    print(f"  [A] majority pivot structure: {pivot_count[piv_major]}/{len(raw)} "
          f"samples kept  ({time.time()-t0:.0f}s)")
    # canonical v1 := basis[0] (free col order fixed by column index)
    qs = [sv * sv % P0 for sv, _ in kept]
    vals = {c: [b[0][c] for _, b in kept] for c in range(NCOLS)}

    # ── Stage B: per-column rational-function fit over F_p0 ───────────
    fits = {}
    holdq, holdy_all = qs[-NHOLD:], {c: vals[c][-NHOLD:] for c in vals}
    fitq = qs[:-NHOLD]
    maxD = 0
    for c in range(NCOLS):
        col = vals[c][:-NHOLD]
        if all(x == 0 for x in vals[c]):
            fits[c] = ([0], [1])
            continue
        f = fit_rational(fitq, col, P0, holdq, holdy_all[c])
        if f is None:
            print(f"  [B] FAIL column {c}: no rational fit deg <= {DEG_MAX}")
            return 1
        fits[c] = f
        maxD = max(maxD, len(f[0]) - 1, len(f[1]) - 1)
    print(f"  [B] all {NCOLS} columns fit; max deg = {maxD}  "
          f"({time.time()-t0:.0f}s)")

    # ── Stage C: clear denominators, lift to Q ────────────────────────
    # common denominator = lcm of Q_c as F_p polynomials is hard mod p;
    # instead reconstruct each column's VALUE as Fraction-valued rational
    # function directly: lift P and Q coefficient-wise (normalize each
    # fit so its first nonzero Q-coefficient is 1, which makes the
    # remaining coefficients well-defined rationals).
    import sympy as sp
    qsym = sp.symbols("q")
    entry = {}
    for c, (P, Q) in fits.items():
        lead = next((x for x in Q if x), None)
        if lead is None:
            entry[c] = sp.Integer(0)
            continue
        linv = pow(lead, P0 - 2, P0)
        Pn = [x * linv % P0 for x in P]
        Qn = [x * linv % P0 for x in Q]
        Pf, Qf = [], []
        for coeffs, out in ((Pn, Pf), (Qn, Qf)):
            for x in coeffs:
                fr = ratrec(x, P0)
                if fr is None:
                    print(f"  [C] ratrec FAIL col {c} (needs CRT) — abort")
                    return 1
                out.append(fr)
        num = sum(sp.Rational(f) * qsym**i for i, f in enumerate(Pf))
        den = sum(sp.Rational(f) * qsym**i for i, f in enumerate(Qf))
        entry[c] = sp.cancel(num / den)
    print(f"  [C] all columns lifted to Q(q)  ({time.time()-t0:.0f}s)")

    # cross-validate the lift at a fresh prime/base point
    Jv = jones_tower_mod(P1, 3, nmax)
    rowsv = build_rows(Jv, P1, 3, 1, 1)[0]
    qv = 9  # s=3 -> q=9
    accv = 0
    okcv = True
    for c in range(NCOLS):
        e = entry[c]
        numv = sp.Integer(sp.numer(e).subs(qsym, qv)) % P1
        denv = sp.Integer(sp.denom(e).subs(qsym, qv)) % P1
        if denv == 0:
            okcv = False
            break
        accv = (accv + rowsv[c] * numv * pow(int(denv), P1 - 2, P1)) % P1
    okcv = okcv and accv == 0
    print(f"  [C'] cross-prime spot validation (p1, s=3, n=1): {okcv}")

    # ── Stage D: exact symbolic annihilation ──────────────────────────
    sys.path.insert(0, str(Path(__file__).parent))
    from habiro_borromean_colored_jones import habiro_borromean, s as ssym

    # operator coefficients as functions of (q, m): entry index layout
    def coeff(i, k):
        return entry[i * (2 * W_WIN + 1) + (k + W_WIN)]

    def rhs_coeff(k):
        return entry[(R_ORD + 1) * (2 * W_WIN + 1) + (k + W_WIN)]

    Jsym = {n: habiro_borromean(n) for n in range(1, NVER + R_ORD + 1)}
    all_ok = True
    for n in range(1, NVER + 1):
        msym = ssym ** (2 * n)
        lhs = sp.Integer(0)
        for i in range(R_ORD + 1):
            ai = sum(coeff(i, k) * msym**k for k in range(-W_WIN, W_WIN + 1))
            lhs += ai * Jsym[n + i]
        rhs = sum(rhs_coeff(k) * msym**k for k in range(-W_WIN, W_WIN + 1))
        diff = sp.cancel(sp.together((lhs - rhs).subs(qsym, ssym**2)))
        zero = diff.equals(0) or sp.simplify(diff) == 0
        print(f"  [D] n={n}: exact symbolic annihilation? {zero}"
              f"  ({time.time()-t0:.0f}s)")
        if not zero:
            all_ok = False
            break

    result = {"verified": bool(all_ok), "cross_prime_spot": bool(okcv)}
    if all_ok:
        # ── Stage E: q -> 1 specialization, m -> M^2 ──────────────────
        M, L = sp.symbols("M L")
        Apoly = sp.Integer(0)
        degen = False
        for i in range(R_ORD + 1):
            ai1 = sp.Integer(0)
            for k in range(-W_WIN, W_WIN + 1):
                e = entry[i * (2 * W_WIN + 1) + (k + W_WIN)]
                lim = sp.limit(e, qsym, 1)
                if lim in (sp.zoo, sp.oo, -sp.oo) or lim.has(sp.zoo):
                    degen = True
                    break
                ai1 += lim * M ** (2 * k)
            if degen:
                break
            Apoly += sp.cancel(ai1) * L**i
        if not degen:
            Apoly = sp.factor(sp.cancel(sp.together(Apoly)))
            result["q_to_1_diagonal_A_candidate"] = str(Apoly)
            print(f"\n  [E] q->1 homogeneous specialization (m->M^2):\n"
                  f"      {Apoly}")
        else:
            result["q_to_1_diagonal_A_candidate"] = (
                "DEGENERATE (pole at q=1 in normalized coefficients; "
                "renormalize before specializing)")
            print("  [E] q->1 degenerate under this normalization")
        # serialize the operator
        result["operator"] = {
            f"a_{i}": {str(k): str(coeff(i, k))
                       for k in range(-W_WIN, W_WIN + 1)
                       if coeff(i, k) != 0}
            for i in range(R_ORD + 1)
        }
        result["b"] = {str(k): str(rhs_coeff(k))
                       for k in range(-W_WIN, W_WIN + 1)
                       if rhs_coeff(k) != 0}

    script_path = Path(__file__)
    witness = {
        "engine": f"python {sys.version.split()[0]} / sympy {sp.__version__} "
                  "(mod-p sampling + Wang rational reconstruction)",
        "scriptFile": f"computations/{script_path.name}",
        "commitSha": subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True,
            cwd=script_path.parent).stdout.strip(),
        "scriptHash": hashlib.sha256(script_path.read_bytes()).hexdigest()[:12],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Phase-2 symbolic reconstruction of the Borromean diagonal "
            "colored-Jones recurrence (r=6, W=11, nullity 1): RREF-canonical null "
            "vector sampled mod 2^61-1, per-entry rational-function fit, "
            "Wang lift to Q(q), exact symbolic annihilation check, q->1 "
            "specialization"
        ),
        "computation": "borromean-diagonal-recurrence-reconstruct",
        "audit_only": True,
        "parameters": {"r": R_ORD, "W": W_WIN, "samples": len(kept),
                       "verify_range": f"n=1..{NVER}"},
        "result": result,
        "wall_seconds": round(time.time() - t0, 1),
    }
    out = script_path.with_name(
        "borromean-diagonal-recurrence-reconstruct.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness → {out.name}   wall {witness['wall_seconds']}s")
    print(f"  VERIFIED: {all_ok}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
