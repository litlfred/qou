#!/usr/bin/env python3
"""Laplace / log-moment reduction of the Delta_lambda covariance-kernel conjecture
(epic qou-x631).  READ-ONLY analysis producer — no witness wiring, no fit.

Conjecture (Phase-4 target):  cov(k) = sum_{lam |- k} (f^lam)^3 * omega3(lam) <= 0,
  omega3(lam) = sum_box c(box)^2 - C(k,2),   and more generally
  L(t) = sum_lam chi3(lam) (f^lam)^{t+1} <= 0  for all real t >= 0.

This script certifies the *reduction* proved in
docs/audits/2026-07-25-covariance-kernel-laplace-moment-reduction.md :

  (R1) L(t) = sum_{n>=1} M_n t^n / n!,  M_n = sum_lam chi3(lam) f^lam (ln f^lam)^n,
       so  [ M_n <= 0 for all n>=1 ]  ==>  [ L(t) <= 0 for all t>=0 ].
  (R2) M_n = (k!/|C3|) * Cov_Planch( omega3, (ln f)^n )   (since E_Planch[omega3]=0).
  (R3) numerically M_n <= 0 for n=1..12, k=3..17 (no violation).
  (R4) max-dimension shape has omega3 <= 0 (forces M_n<0 as n->infty).
  (R5) n=2 decomposition  Cov(omega3,(ln f)^2) = 2 muL Cov(omega3,ln f) + E[omega3 delta^2]
       with the leading (cited n=1) term negative & dominant, residual positive & shrinking.

chi3(lam) = f^lam * 3 * omega3(lam) / (k(k-1)(k-2))  (Jucys-Murphy central character
of the 3-cycle class), so sign(chi3) = sign(omega3).  All exact where integer.
"""
import math
from fractions import Fraction as Fr

def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield (); return
    for f in range(min(n, mx), 0, -1):
        for r in partitions(n - f, f):
            yield (f,) + r

def hook_dim(lam):
    lam = list(lam); n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    p = 1
    for i, row in enumerate(lam):
        for j in range(row):
            p *= (row - 1 - j) + (conj[j] - 1 - i) + 1
    return math.factorial(n) // p

def omega3(lam, C2):
    return sum((j - i) ** 2 for i, row in enumerate(lam) for j in range(row)) - C2

def check(kmax_moment=17, nmax=12, kmax_int=15):
    print("== (R3) log-moment nonpositivity M_n<=0, n=1..%d ==" % nmax)
    all_ok = True
    for k in range(3, kmax_moment + 1):
        C2 = k * (k - 1) // 2
        atoms = [(hook_dim(l), omega3(l, C2)) for l in partitions(k)]
        maxf = max(f for f, _ in atoms)
        top_om = [o for f, o in atoms if f == maxf][0]
        bad = []
        for n in range(1, nmax + 1):
            Mn = sum((f * f * o) * (math.log(f) ** n) for f, o in atoms)  # ∝ M_n (drop const 3/den)
            norm = sum((f * f * abs(o)) * (math.log(max(f, 2)) ** n) for f, o in atoms)
            if Mn > 1e-9 * max(norm, 1.0):
                bad.append((n, Mn))
        all_ok &= (not bad and top_om <= 0)
        print(f"  k={k:2d}: M_n<=0 (n=1..{nmax}): {'YES' if not bad else 'NO '+str(bad)}"
              f" | max-dim omega3={top_om} ({'<=0' if top_om<=0 else 'POSITIVE!'})")
    print("== (R5) n=2 decomposition: Cov2 = 2 muL Cov1 + resid ==")
    for k in range(4, kmax_moment + 1):
        C2 = k * (k - 1) // 2; kf = math.factorial(k)
        rows = [(omega3(l, C2), hook_dim(l) ** 2 / kf, math.log(hook_dim(l))) for l in partitions(k)]
        muL = sum(p * lf for _, p, lf in rows)
        Cov1 = sum(p * o * lf for o, p, lf in rows)
        Cov2 = sum(p * o * lf * lf for o, p, lf in rows)
        lead = 2 * muL * Cov1
        resid = sum(p * o * (lf - muL) ** 2 for o, p, lf in rows)
        ok = (Cov2 < 0 and lead < 0)
        print(f"  k={k:2d}: Cov2={Cov2:+.3e} lead={lead:+.3e} resid={resid:+.3e}"
              f" ratio|resid/lead|={abs(resid/lead):.3f} {'OK' if ok else 'CHECK'}")
    print("== (R3)/(R4) overall:", "CONFIRMED" if all_ok else "VIOLATION", "==")
    # (R3-int) exact integer S_m = sum chi3 f^m <= 0
    print("== integer S_m = sum chi3 f^m (exact) ==")
    for k in range(3, kmax_int + 1):
        C2 = k * (k - 1) // 2; den = k * (k - 1) * (k - 2)
        atoms = [(hook_dim(l), Fr(hook_dim(l) ** 2 * 3 * omega3(l, C2), den)) for l in partitions(k)]
        vals = [int(sum(w * Fr(f) ** (m - 1) for f, w in atoms)) for m in range(1, 5)]
        assert vals[0] == 0 and all(v <= 0 for v in vals), (k, vals)
        print(f"  k={k:2d}: " + "  ".join(f"S_{m+1}={v}" for m, v in enumerate(vals)))
    return all_ok

if __name__ == "__main__":
    ok = check()
    print("\nRESULT:", "all reduction checks pass" if ok else "FAILED")
