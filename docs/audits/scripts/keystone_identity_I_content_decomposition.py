#!/usr/bin/env python3
"""Identity I, decomposed: M(n) = n(3n-1)/2 WITHOUT the hook-length formula.

Context
-------
The keystone W_lambda defect closed form
(`docs/audits/2026-06-20-keystone-wlambda-C-n-closed-form.md`,
`WLambdaDefectClosedForm.lean`) is Lean-proved sorry-free EXCEPT for one
carried representation-theoretic input, "Identity I":

    M(n) := (1/n!) sum_{lambda |- n} dim(lambda)^2 * sum_{c in lambda} h_c^2
          = n(3n-1)/2 .

The corpus repeatedly states this "needs SYT-dimension / hook-length
infrastructure not currently in Mathlib -- a multi-session infra fill"
(s5-so3-keystone ledger; 2026-06-20 closed-form audit). That framing assumes
the *hook-length FORMULA* dim(lambda) = n!/prod_c h_c (Frame-Robinson-Thrall,
the hard theorem) is on the critical path.

It is NOT. Identity I factors into two pieces, neither of which uses the
hook-length formula:

  (A) per-partition hook-content identity (a statement about a SINGLE Young
      diagram -- no dimensions, no Plancherel measure, no hook-length formula):

          sum_{c in lambda} h_c^2  =  sum_{c in lambda} c(c)^2  +  n^2 ,

      where c(c) = j - i is the CONTENT of cell (i,j) and h_c its hook length.

  (B) Plancherel content-square mean (the standard Jucys-Murphy result):

          E_Planch[ sum_c c(c)^2 ]  :=  (1/n!) sum_lambda dim(lambda)^2 sum_c c(c)^2
                                     =  binom(n,2)  =  n(n-1)/2 .

      Proof (no fit, no hook-length formula): the power sum of Jucys-Murphy
      elements p_2(X) = sum_{k=1}^n X_k^2 is CENTRAL in C[S_n] and acts on the
      block V_lambda by the scalar sum_c c(c)^2. For a central z = sum_g a_g g,
      the Plancherel average of its scalar omega_lambda(z) equals the
      coefficient a_e of the identity (regular-character orthogonality
      sum_lambda dim(lambda) chi^lambda(g) = n! [g=e]). For z = sum_k X_k^2 the
      only identity contributions are X_k^2 >= (i,k)(i,k) = e for i<k, giving
      a_e = sum_{k=1}^n (k-1) = binom(n,2).

Then, since E_Planch[n^2] = n^2 trivially:

    M(n) = E_Planch[sum h^2] = E_Planch[sum c^2] + n^2
         = binom(n,2) + n^2 = (n^2-n)/2 + n^2 = n(3n-1)/2 .   QED

What this buys for the Lean fill
--------------------------------
The hard Frame-Robinson-Thrall hook-length FORMULA is OFF the critical path.
What remains:
  * (A) needs only Young-diagram + hook + content DEFINITIONS (Mathlib has
        `YoungDiagram`); it is a self-contained combinatorial identity,
        exhaustively verified below and almost certainly already in the
        literature (hook/content power-sum identities).
  * (B) needs the Wedderburn/dimension structure of C[S_n] (the f^lambda as
        block dims, sum_lambda (f^lambda)^2 = n!) + Jucys-Murphy centrality.
        That part is genuine "SYT-dimension infra" -- but it is standard and is
        NOT the hook-length formula.

This script verifies, in EXACT integer / Fraction arithmetic (no mpmath, no
floats, no q_0, no 210 ppb -- nothing archimedean, no fit):

  (A) the per-partition identity  sum h^2 = sum c^2 + n^2  for EVERY lambda |- n,
      n = 1..22  (every single partition, not just the average).
  (B) E_Planch[sum c^2] = binom(n,2)             exactly, n = 1..22.
  (Bx) the JM coefficient-of-identity  sum_{k=1}^n (k-1) = binom(n,2)  and that
       it equals E_Planch[sum c^2]  (the bridge value).
  (D) M(n) = binom(n,2) + n^2 = n(3n-1)/2        exactly, n = 1..22, BOTH by the
      decomposition and by a direct independent computation of M(n).
"""
import sys
from fractions import Fraction
from math import factorial, comb


# ----- exact (q = 1) combinatorics, stdlib only -----
def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, mx), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def conjugate(lam):
    if not lam:
        return ()
    m = max(lam)
    return tuple(sum(1 for r in lam if r > c) for c in range(m))


def hooks(lam):
    """Multiset of hook lengths h(i,j) = arm + leg + 1."""
    lamp = conjugate(lam)
    out = []
    for i, row in enumerate(lam):
        for j in range(row):
            out.append((row - j - 1) + (lamp[j] - i - 1) + 1)
    return out


def contents(lam):
    """Multiset of contents c(i,j) = j - i  (0-indexed i,j)."""
    return [j - i for i, row in enumerate(lam) for j in range(row)]


def dim(lam):
    """f^lambda via the hook-length formula -- used ONLY to compute the
    Plancherel weight for the cross-checks; the DERIVATION of M(n) above does
    not invoke it."""
    n = sum(lam)
    prod = 1
    for h in hooks(lam):
        prod *= h
    return factorial(n) // prod


def M_direct(n):
    """M(n) = (1/n!) sum_lambda dim^2 sum_c h_c^2  (exact Fraction) -- the
    object Identity I is about, computed directly and independently of the
    decomposition."""
    tot = 0
    for lam in partitions(n):
        d = dim(lam)
        tot += d * d * sum(h * h for h in hooks(lam))
    return Fraction(tot, factorial(n))


def E_planch_content_sq(n):
    """E_Planch[sum_c c(c)^2] = (1/n!) sum_lambda dim^2 sum_c c^2 (exact)."""
    tot = 0
    for lam in partitions(n):
        d = dim(lam)
        tot += d * d * sum(c * c for c in contents(lam))
    return Fraction(tot, factorial(n))


def main():
    NMAX = 22
    print("Identity I, decomposed:  M(n) = n(3n-1)/2  without the hook-length formula")
    print("=" * 78)

    # ---- (A) per-partition hook-content identity, EVERY partition ----
    print("\n(A) per-partition:  sum_c h_c^2 = sum_c c(c)^2 + n^2   (every lambda |- n)")
    okA = True
    nparts_total = 0
    worst = None
    for n in range(1, NMAX + 1):
        cnt = 0
        for lam in partitions(n):
            cnt += 1
            sh2 = sum(h * h for h in hooks(lam))
            sc2 = sum(c * c for c in contents(lam))
            if sh2 - sc2 != n * n:
                okA = False
                worst = (lam, sh2, sc2, sh2 - sc2, n * n)
        nparts_total += cnt
    print(f"    checked {nparts_total} partitions over n=1..{NMAX};  "
          f"all satisfy  sum h^2 - sum c^2 = n^2 : {'PASS' if okA else 'FAIL'}")
    if worst:
        print(f"    COUNTEREXAMPLE lambda={worst[0]}: sh2={worst[1]} sc2={worst[2]} "
              f"diff={worst[3]} != n^2={worst[4]}")

    # ---- (B) Plancherel content-square mean = binom(n,2) ----
    print("\n(B) Plancherel mean:  E_Planch[sum_c c(c)^2] = binom(n,2) = n(n-1)/2")
    print(f"    {'n':>3}{'E_Planch[sum c^2]':>20}{'binom(n,2)':>14}{'':>6}")
    okB = True
    for n in range(1, NMAX + 1):
        ec = E_planch_content_sq(n)
        bn = Fraction(comb(n, 2))
        ok = (ec == bn)
        okB = okB and ok
        if n <= 9 or not ok:
            print(f"    {n:>3}{str(ec):>20}{str(bn):>14}{('OK' if ok else 'FAIL'):>6}")
    print(f"    ... E_Planch[sum c^2] = binom(n,2) exact, n=1..{NMAX} : {'PASS' if okB else 'FAIL'}")

    # ---- (Bx) JM coefficient-of-identity  sum_{k=1}^n (k-1) = binom(n,2) ----
    print("\n(Bx) Jucys-Murphy:  a_e(sum_k X_k^2) = sum_{k=1}^n (k-1) = binom(n,2)")
    print("     and it equals E_Planch[sum c^2] (the bridge value).")
    okBx = True
    for n in range(1, NMAX + 1):
        jm = sum(k - 1 for k in range(1, n + 1))           # JM identity-coefficient
        bn = comb(n, 2)
        ec = E_planch_content_sq(n)
        ok = (jm == bn) and (Fraction(jm) == ec)
        okBx = okBx and ok
    print(f"     sum(k-1) = binom(n,2) = E_Planch[sum c^2], n=1..{NMAX} : "
          f"{'PASS' if okBx else 'FAIL'}")

    # ---- (D) M(n) = binom(n,2) + n^2 = n(3n-1)/2,  decomposition vs direct ----
    print("\n(D) M(n):  decomposition  binom(n,2)+n^2  ==  n(3n-1)/2  ==  direct M(n)")
    print(f"    {'n':>3}{'M direct':>12}{'binom+n^2':>12}{'n(3n-1)/2':>12}{'':>6}")
    okD = True
    for n in range(1, NMAX + 1):
        md = M_direct(n)
        decomp = Fraction(comb(n, 2)) + n * n          # (B) + n^2 gap term
        closed = Fraction(n * (3 * n - 1), 2)
        ok = (md == decomp == closed)
        okD = okD and ok
        if n <= 9 or not ok:
            print(f"    {n:>3}{str(md):>12}{str(decomp):>12}{str(closed):>12}"
                  f"{('OK' if ok else 'FAIL'):>6}")
    print(f"    ... all three agree, n=1..{NMAX} : {'PASS' if okD else 'FAIL'}")

    print("\n--- SELF-CHECKS ---")
    print(f"  (A)  per-partition  sum h^2 = sum c^2 + n^2  (all parts)   : {'PASS' if okA else 'FAIL'}")
    print(f"  (B)  E_Planch[sum c^2] = binom(n,2)                        : {'PASS' if okB else 'FAIL'}")
    print(f"  (Bx) JM a_e = sum(k-1) = binom(n,2) = E_Planch[sum c^2]    : {'PASS' if okBx else 'FAIL'}")
    print(f"  (D)  M(n) = binom(n,2)+n^2 = n(3n-1)/2 (decomp == direct)  : {'PASS' if okD else 'FAIL'}")

    print("\n--- RESULT ---")
    print("  Identity I  M(n) = n(3n-1)/2  =  E_Planch[sum c^2] + n^2  =  binom(n,2) + n^2,")
    print("  proved WITHOUT the Frame-Robinson-Thrall hook-length formula:")
    print("    (A) single-diagram hook-content identity  sum h^2 = sum c^2 + n^2,  and")
    print("    (B) the Jucys-Murphy / Plancherel content-square mean  binom(n,2).")
    print("  The hard hook-length FORMULA is OFF the Lean critical path; the residual")
    print("  infra is (A) Young-diagram defs + a combinatorial identity, and (B) the")
    print("  standard C[S_n] Wedderburn-dimension / JM machinery.  No fit; nothing")
    print("  archimedean (q_0 and the 210 ppb target never appear).")

    all_ok = okA and okB and okBx and okD
    print("\nALL CHECKS PASS." if all_ok else "\nSELF-CHECK FAILED.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
