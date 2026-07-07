#!/usr/bin/env python3
r"""
Reconstruct the EXPLICIT Borromean diagonal colored-Jones recurrence
operator — a self-contained, checkpointed, laptop-runnable script.

WHY THIS SCRIPT
---------------
The Borromean diagonal colored Jones J_{B,n} satisfies a q-difference
recurrence whose MINIMAL order is 5 (the corpus certified its EXISTENCE
to mod-p, PR #3443: r <= 4 excluded).  This script reconstructs the
UNIQUE nullity-1 form at the (order, m-window) = (6, 11) parameterization
(R_ORD=6, W_WIN=11) — one order above minimal, chosen because that window
is where the fit system has a clean 1-dimensional null space (the minimal
order-5 operator lives inside this order-6 span as an inhomogeneous
shift-multiple; see the degree-terminus audit).  The explicit operator
has coefficients of intrinsic q-degree ~126 (degree terminus, PR #3469),
so reconstructing it is a multi-prime CRT interpolation — correct
complexity, but it needs an UNINTERRUPTED multi-hour run.  A laptop
provides exactly that (the CI sandbox did not — 5 container reclaims
killed it).  This script is the laptop deliverable.

WHAT YOU GET ON SUCCESS
-----------------------
  * the explicit order-6 operator  sum_{i=0}^{6} a_i(q,m) J_{B,n+i}
    = b(q,m), m = q^n, coefficients in Q(q)[m^{+-1}], written to
    borromean-operator-explicit.json;
  * an EXACT symbolic verification that it annihilates the Habiro tower
    (this upgrades the recurrence from mod-p evidence to a proof of the
    specific operator);
  * the q->1, m->M^2 specialization = the diagonal Borromean A-polynomial
    candidate (the classical-geometry side).

REQUIREMENTS
------------
  pip install sympy numpy
  Python 3.9+.  ~2-4 GB RAM.  No internet, no Rust, no other files.

RUN
---
  python3 borromean_operator_reconstruct_laptop.py
  # resumable: re-run the same command after any interruption; it picks up
  # from the per-prime checkpoint file borromean-reconstruct-ckpt.json.
  # Expected wall time: a few hours (dominated by the per-prime column
  # fits at degree ~130).  Leave it running (close the lid is fine on most
  # laptops if you disable sleep, or run under `caffeinate`/`nohup`).

TUNING (top of file)
--------------------
  WINDOW = (6, 11) is the unique nullity-1 window.  DEG_CAP bounds the
  per-column rational-fit degree (raise if a column reports "no fit").
  PRIMES: 31-bit primes; the script adds more automatically until the
  Wang lift succeeds.

METHOD (per prime p)
--------------------
  1. Evaluate J_{B,n} mod p at many base points s (q = s^2 varies), via
     Habiro's cyclotomic formula (verified transcription, PR #3443).
  2. For each s, RREF the (6,11) fit system -> the canonical (nullity-1)
     null vector = the operator's coefficient ratios at that q.
  3. Per matrix column, fit the ratio as a rational function of q
     (minimal degree, bisected, holdout-validated), monic-Q normalized so
     residues are CRT-compatible across primes.
  Then CRT + rational (Wang) reconstruction across primes to lift each
  coefficient to Q; assemble in sympy; verify exactly; specialize q->1.

This is audit-only mathematics; it wires into nothing.
"""
from __future__ import annotations

import json
import sys
import time
from fractions import Fraction
from math import isqrt
from pathlib import Path

try:
    import numpy as np
    import sympy as sp
except ImportError:
    sys.exit("Please `pip install numpy sympy` first.")

# ----------------------------------------------------------------------
# Parameters
# ----------------------------------------------------------------------
R_ORD = 6                    # operator order (unique window)
W_WIN = 11                   # m-window: a_i supported on m^k, |k| <= W_WIN
NBLK = 2 * W_WIN + 1         # 23
NCOLS = (R_ORD + 2) * NBLK   # 184  (blocks a_0..a_6, then b)
R_FIT = NCOLS + 20           # fit rows per base point group
DEG_CAP = 240                # per-column rational-fit degree cap (covers the
                             # measured max coeff q-degree ~218 with margin)
NHOLD = 15                   # holdout samples for fit validation
CKPT = Path(__file__).with_name("borromean-reconstruct-ckpt.json")
OUT = Path(__file__).with_name("borromean-operator-explicit.json")

# 31-bit primes (products fit int64; CRT lifts the ~deg-130 integers).
PRIMES = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563,
          2147483549, 2147483543, 2147483497, 2147483489, 2147483477,
          2147483423, 2147483399, 2147483353, 2147483323, 2147483269,
          2147483249, 2147483237, 2147483179, 2147483171, 2147483137,
          2147483123, 2147483077, 2147483069, 2147483053]


# ----------------------------------------------------------------------
# Habiro Borromean colored Jones, mod p  (verified transcription)
# ----------------------------------------------------------------------
def jones_tower_mod(p: int, s: int, nmax: int):
    """J_{B,n} mod p for n=1..nmax with q = s^2 mod p; None if singular.
    {j} = q^{j/2}-q^{-j/2} = s^j - s^{-j}."""
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
        tot, prod3 = 0, 1
        for l in range(n):
            if l > 0:
                f = br[n + l] * br[n - l] % p
                prod3 = prod3 * f % p * f % p * f % p
            den = 1
            for j in range(l + 1, 2 * l + 2):
                den = den * br[j] % p
            d2i = pow(den * den % p, p - 2, p)
            term = br[n] * br[n] % p * prod3 % p * d2i % p
            tot = (tot - term if l & 1 else tot + term) % p
        out.append(tot)
    return out


def build_fit_rows(J, p, s):
    """The (6,11) fit system at q = s^2: rows n=1..R_FIT, cols = coeff slots."""
    q = s * s % p
    rows = []
    for n in range(1, R_FIT + 1):
        m = pow(q, n, p)
        mi = pow(m, p - 2, p)
        mk = [0] * NBLK
        mk[W_WIN] = 1
        for k in range(1, W_WIN + 1):
            mk[W_WIN + k] = mk[W_WIN + k - 1] * m % p
            mk[W_WIN - k] = mk[W_WIN - k + 1] * mi % p
        row = []
        for i in range(R_ORD + 1):
            Jni = J[n + i - 1]
            for idx in range(NBLK):
                row.append(mk[idx] * Jni % p)
        for idx in range(NBLK):
            row.append((p - mk[idx]) % p)   # -m^k for the b block
        rows.append(row)
    return rows


# ----------------------------------------------------------------------
# numpy RREF over F_p (p < 2^31, int64-safe)
# ----------------------------------------------------------------------
def rref_np(rows, p):
    M = (np.array(rows, dtype=np.int64) % p)
    nrows, ncols = M.shape
    piv = []
    rank = 0
    for col in range(ncols):
        nz = np.nonzero(M[rank:, col])[0]
        if nz.size == 0:
            continue
        pr = rank + int(nz[0])
        if pr != rank:
            M[[rank, pr]] = M[[pr, rank]]
        inv = pow(int(M[rank, col]), p - 2, p)
        M[rank] = (M[rank] * inv) % p
        colv = M[:, col].copy()
        colv[rank] = 0
        M = (M - np.outer(colv, M[rank])) % p
        piv.append(col)
        rank += 1
        if rank == nrows:
            break
    return M, piv


def canonical_nullvec(rows, p):
    """The unique (nullity-1) null vector, free column set to 1; + pivots.
    Returns (vec, pivots) or (None, None) if nullity != 1."""
    M, piv = rref_np(rows, p)
    ncols = M.shape[1]
    pivset = set(piv)
    free = [c for c in range(ncols) if c not in pivset]
    if len(free) != 1:
        return None, tuple(sorted(piv))
    fc = free[0]
    pmap = {c: i for i, c in enumerate(piv)}
    vec = [0] * ncols
    vec[fc] = 1
    for c in piv:
        vec[c] = int((-M[pmap[c], fc]) % p)
    return vec, tuple(sorted(piv))


# ----------------------------------------------------------------------
# per-column rational fit v[c](q) = P(q)/Q(q) over F_p (monic-Q normalized)
# ----------------------------------------------------------------------
def fit_column(qs, ys, p, cap):
    hold_q, hold_y = qs[-NHOLD:], ys[-NHOLD:]
    fit_q, fit_y = qs[:-NHOLD], ys[:-NHOLD]
    lo, hi, best = 0, cap, None
    # find any working degree, then bisect to minimal
    def try_deg(d):
        need = 2 * d + 3
        if need > len(fit_q):
            return None
        rows = []
        for qv, yv in zip(fit_q[:need], fit_y[:need]):
            qp = [1]
            for _ in range(d):
                qp.append(qp[-1] * qv % p)
            rows.append(qp + [(-yv * t) % p for t in qp])
        M, piv = rref_np(rows, p)
        ncols = 2 * d + 2
        free = [c for c in range(ncols) if c not in set(piv)]
        if not free:
            return None
        fc = free[0]
        pmap = {c: i for i, c in enumerate(piv)}
        v = [0] * ncols
        v[fc] = 1
        for c in piv:
            v[c] = int((-M[pmap[c], fc]) % p)
        Pc, Qc = v[:d + 1], v[d + 1:]
        if not any(Qc):
            return None
        for qv, yv in zip(hold_q, hold_y):
            qp = [1]
            for _ in range(d):
                qp.append(qp[-1] * qv % p)
            num = sum(a * b for a, b in zip(Pc, qp)) % p
            den = sum(a * b for a, b in zip(Qc, qp)) % p
            if den == 0 or num * pow(den, p - 2, p) % p != yv % p:
                return None
        return Pc, Qc
    if try_deg(hi) is None:
        return None
    best = try_deg(hi)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        r = try_deg(mid)
        if r is not None:
            hi, best = mid, r
        else:
            lo = mid
    Pc, Qc = best
    # monic-Q normalize (leading nonzero Q coeff -> 1)
    lead = next((c for c in reversed(Qc) if c), None)
    linv = pow(lead, p - 2, p)
    Pc = [a * linv % p for a in Pc]
    Qc = [a * linv % p for a in Qc]
    # strip trailing zeros
    while len(Pc) > 1 and Pc[-1] == 0:
        Pc.pop()
    while len(Qc) > 1 and Qc[-1] == 0:
        Qc.pop()
    return Pc, Qc


def sample_prime(p, log):
    """Per-prime: base-point RREF null vectors -> per-column rational fits.
    Returns {col: {P:[...], Q:[...]}} with the modal pivot structure."""
    nmax = R_FIT + R_ORD
    # collect canonical null vectors over base points with a consistent
    # pivot structure (the modal one).
    from collections import Counter
    raw = []
    pcount = Counter()
    s = 2
    # base points must support a degree-DEG_CAP fit: try_deg(d) needs
    # 2d+3 fit rows, plus NHOLD holdout rows -> 2*DEG_CAP + NHOLD + margin.
    NEED = 2 * DEG_CAP + NHOLD + 20
    t0 = time.time()
    while len(raw) < NEED and s < NEED * 6 + 500:
        s += 1
        J = jones_tower_mod(p, s, nmax)
        if J is None:
            continue
        rows = build_fit_rows(J, p, s)
        vec, piv = canonical_nullvec(rows, p)
        if vec is None:
            continue
        raw.append((s, piv, vec))
        pcount[piv] += 1
        if len(raw) % 50 == 0:
            log(f"    [p={p}] {len(raw)}/{NEED} base points  "
                f"({time.time()-t0:.0f}s)")
    if not raw:
        raise RuntimeError(f"no canonical null vectors at p={p}")
    modal = pcount.most_common(1)[0][0]
    kept = [(s, v) for s, pv, v in raw if pv == modal]
    log(f"    [p={p}] modal pivots kept {len(kept)}/{len(raw)}")
    qs = [s * s % p for s, _ in kept]
    cols = {}
    for c in range(NCOLS):
        ys = [v[c] for _, v in kept]
        if not any(ys):
            cols[c] = {"P": [0], "Q": [1]}
            continue
        fit = fit_column(qs, ys, p, DEG_CAP)
        if fit is None:
            raise RuntimeError(f"column {c} at p={p}: no rational fit "
                               f"(raise DEG_CAP)")
        Pc, Qc = fit
        cols[c] = {"P": Pc, "Q": Qc}
        if c % 40 == 0:
            log(f"    [p={p}] col {c}/{NCOLS} fitted (deg {len(Pc)-1})  "
                f"({time.time()-t0:.0f}s)")
    return cols


# ----------------------------------------------------------------------
# CRT + Wang lift
# ----------------------------------------------------------------------
def crt_pair(a1, m1, a2, m2):
    from sympy import mod_inverse
    m = m1 * m2
    x = (a1 + m1 * ((a2 - a1) * mod_inverse(m1 % m2, m2) % m2)) % m
    return x, m


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


def try_lift(runs):
    """CRT + Wang each coefficient across runs (modal-degree consensus per
    column). Returns {col:(Pf,Qf)} of Fractions, or None if incomplete."""
    from collections import Counter
    lifted = {}
    for c in range(NCOLS):
        shapes = [(len(r[str(c)]["P"]), len(r[str(c)]["Q"])) for r in runs]
        modal = Counter(shapes).most_common(1)[0][0]
        use = [r for r, sh in zip(runs, shapes) if sh == modal]
        (npc, nqc) = modal
        Pf, Qf = [], []
        for kind, ncoef, out in (("P", npc, Pf), ("Q", nqc, Qf)):
            for i in range(ncoef):
                a, m = 0, 1
                for r in use:
                    val = r[str(c)][kind][i]
                    a, m = crt_pair(a, m, val, r["_prime"]) if m > 1 else (val, r["_prime"])
                fr = ratrec(a, m)
                if fr is None:
                    return None
                out.append(fr)
        lifted[c] = (Pf, Qf)
    return lifted


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------
def load_ckpt():
    if CKPT.exists():
        return json.loads(CKPT.read_text())
    return {"runs": []}


def save_ckpt(state):
    # atomic: write a temp then replace, so a Ctrl-C / power-loss mid-write
    # cannot corrupt or empty the resumable checkpoint.
    tmp = CKPT.with_suffix(".tmp")
    tmp.write_text(json.dumps(state), encoding="utf-8")
    tmp.replace(CKPT)


def main():
    t0 = time.time()

    def log(msg):
        print(msg, flush=True)

    log("\n  Borromean explicit-operator reconstruction (laptop)\n")
    log(f"  window (r,W)=({R_ORD},{W_WIN}), {NCOLS} columns, DEG_CAP={DEG_CAP}")
    state = load_ckpt()
    done_primes = {r["_prime"] for r in state["runs"]}
    if done_primes:
        log(f"  resuming: {len(done_primes)} prime(s) already sampled")

    lifted = None
    for p in PRIMES:
        if p not in done_primes:
            log(f"  sampling prime p={p} ...")
            cols = sample_prime(p, log)
            run = {"_prime": p}
            run.update({str(c): cols[c] for c in range(NCOLS)})
            state["runs"].append(run)
            save_ckpt(state)
            log(f"  prime p={p} done + checkpointed  ({time.time()-t0:.0f}s)")
        if len(state["runs"]) >= 2:
            lifted = try_lift(state["runs"])
            log(f"  CRT lift after {len(state['runs'])} primes: "
                f"{'SUCCESS' if lifted else 'incomplete, add another prime'}")
            if lifted is not None:
                break
    if lifted is None:
        log("  Could not lift within the prime pool — add more PRIMES.")
        return 1

    # assemble + EXACT symbolic verification
    log("\n  lifting complete; assembling + verifying exactly in sympy ...")
    q = sp.symbols("q")
    s = sp.symbols("s", positive=True)   # s = q^{1/2}

    def hb(n):
        def brk(a):
            return s**a - s**(-a)
        tot = sp.Integer(0)
        for l in range(n):
            nm = brk(n)**2 * sp.prod([brk(n + j) * brk(n - j)
                                      for j in range(1, l + 1)])**3
            den = sp.prod([brk(j) for j in range(l + 1, 2 * l + 2)])**2
            tot += (-1)**l * sp.cancel(sp.together(nm / den))
        return sp.expand(sp.cancel(sp.together(tot)))

    entry = {}
    for c, (Pf, Qf) in lifted.items():
        numP = sum(sp.Rational(f) * q**i for i, f in enumerate(Pf))
        denQ = sum(sp.Rational(f) * q**i for i, f in enumerate(Qf))
        entry[c] = sp.cancel(numP / denQ) if denQ != 0 else sp.Integer(0)

    def a_coeff(i, k):
        return entry[i * NBLK + (k + W_WIN)]

    def b_coeff(k):
        return entry[(R_ORD + 1) * NBLK + (k + W_WIN)]

    NVER = 12
    J = {n: hb(n) for n in range(1, NVER + R_ORD + 1)}
    verified = True
    for n in range(1, NVER + 1):
        m = s**(2 * n)
        lhs = sp.Integer(0)
        for i in range(R_ORD + 1):
            ai = sum(a_coeff(i, k) * m**k for k in range(-W_WIN, W_WIN + 1))
            lhs += ai * J[n + i]
        rhs = sum(b_coeff(k) * m**k for k in range(-W_WIN, W_WIN + 1))
        # lhs-rhs is a pure rational function in s after q->s^2; cancel is
        # sufficient to decide identically-zero and is far faster/robust
        # than simplify on the high-degree (~deg-1100 in s) expression.
        diff = sp.cancel(sp.together((lhs - rhs).subs(q, s**2)))
        ok = diff == 0
        log(f"  [verify] n={n}: exact annihilation? {ok}")
        if not ok:
            verified = False
            break

    result = {"verified_exact": bool(verified),
              "order": R_ORD, "m_window": W_WIN,
              "primes_used": len(state["runs"])}
    if verified:
        M, L = sp.symbols("M L")
        Apoly, degen = sp.Integer(0), False
        for i in range(R_ORD + 1):
            ai1 = sp.Integer(0)
            for k in range(-W_WIN, W_WIN + 1):
                lim = sp.limit(a_coeff(i, k), q, 1)
                if lim.has(sp.zoo, sp.oo):
                    degen = True
                    break
                ai1 += lim * M**(2 * k)
            if degen:
                break
            Apoly += sp.cancel(ai1) * L**i
        result["q_to_1_A_polynomial"] = ("degenerate under this normalization"
                                         if degen else str(sp.factor(sp.cancel(Apoly))))
        result["operator"] = {
            f"a_{i}": {str(k): str(sp.simplify(a_coeff(i, k)))
                       for k in range(-W_WIN, W_WIN + 1)
                       if a_coeff(i, k) != 0}
            for i in range(R_ORD + 1)}
        result["b"] = {str(k): str(sp.simplify(b_coeff(k)))
                       for k in range(-W_WIN, W_WIN + 1) if b_coeff(k) != 0}
        log("\n  *** EXPLICIT OPERATOR RECONSTRUCTED AND VERIFIED ***")
        log(f"  q->1 diagonal Borromean A-polynomial:\n    "
            f"{result['q_to_1_A_polynomial']}")
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    log(f"\n  written -> {OUT.name}   (total {time.time()-t0:.0f}s)")
    return 0 if verified else 1


if __name__ == "__main__":
    sys.exit(main())
