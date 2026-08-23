"""The general-n Markov condition reduces to a finite CORNER identity.

Context.  `ocneanu_weight_general_n.py` derives the Ocneanu weight closed form and
`OcneanuWeightWenzl.lean` proves it equals `schurPrincipal 2 (q^2) mu / (q^2+1)^|mu|`
at convention D -- which relocates the corpus's one external citation (Wenzl) onto a
single open statement:

    ocneanuWeight satisfies the Markov condition  tr(x sigma_n) = z tr(x)  at general n.

This script reduces that statement to an explicit finite identity in the corner contents
of ONE partition, with no representation theory left in it, and tests the identity.

THE REDUCTION
-------------

For x in H_n, decompose V_lam = (+)_{mu = lam - box} V_mu and let A_mu = P_mu sigma_n P_mu.

  (i)  A_mu commutes with H_{n-1}.  Branching for the Hecke algebra is SIMPLE
       (multiplicity-free), so the commutant of H_{n-1} in End(V_mu) is the
       Gelfand-Tsetlin algebra -- i.e. A_mu is DIAGONAL in the seminormal basis.
  (ii) Its (T,T) entry is the Hoefsmit diagonal entry at the axial distance between n
       and n+1, namely  a(c(lam/mu) - c_T(n))  with  a(d) = (q - q^-1)/(1 - q^{-2d}).
       (`QOU.SchurWeyl.Seminormal.seminormalParam`.)
  (iii) Hence  chi^lam(x sigma_n) = sum_{mu = lam - box} sum_{T in SYT(mu)} x_TT
              a(c(lam/mu) - c_T(n)).
  (iv) Since H_n = (+)_mu End(V_mu), the diagonal entries x_TT range FREELY, so matching
       coefficients in  sum_lam W_lam chi^lam(x sigma_n) = z sum_mu W_mu chi^mu(x)
       is valid pointwise in (mu, T).  T enters only through c_T(n), and n is the largest
       entry of T, so its cell is a REMOVABLE corner of mu.

  =>  ** for every mu |- n and every removable corner r of mu:
            sum_{s addable corner of mu}  W_{mu+s} * a(c(s) - c(r))  =  z * W_mu **

EPISTEMIC STATUS -- read before citing this.
  * The corner identity itself is TESTED below, exactly, at symbolic z (not just
    convention D), for every partition of n = 1..6 and every removable corner.
  * The REDUCTION (steps i-iv) is derived on paper.  Step (i) is the Okounkov-Vershik
    multiplicity-free argument and step (ii) is the Hoefsmit form; both are what
    `seminormalRep` already encodes, but NEITHER IS PROVED IN LEAN.  So proving the
    corner identity in Lean would NOT by itself prove the Markov condition in Lean --
    the reduction is the remaining gap, and it is representation-theoretic, not
    arithmetic.
  * Independent corroboration that the reduction is right: the Markov condition was
    verified numerically by a different route in `ocneanu_weight_general_n.py`
    (tr(sigma_1) = z through n=6, and tr(L_k sigma_{n-1}) = z tr(L_k) used to solve
    n=4,5).  A botched reduction would be very unlikely to yield an identity that holds
    at every partition through n=6.

EXACT ARITHMETIC ONLY -- sympy over Q(q, z).  No float (AGENTS.md NO-FLOAT64).
"""

import sys
import sympy as sp

q, z = sp.symbols('q z')


def parts(n, cap=None):
    if n == 0:
        yield ()
        return
    cap = n if cap is None else min(cap, n)
    for f in range(cap, 0, -1):
        for r in parts(n - f, f):
            yield (f,) + r


def cells(s):
    return [(i, j) for i, r in enumerate(s) for j in range(r)]


def hooks(s):
    rows = list(s)
    mc = rows[0] if rows else 0
    cols = [sum(1 for r in rows if r > j) for j in range(mc)]
    return {(i, j): (rows[i] - j - 1) + (cols[j] - i - 1) + 1 for (i, j) in cells(s)}


def W(s):
    """The derived Ocneanu weight (general z)."""
    if len(s) == 0:
        return sp.Integer(1)
    num = sp.Integer(1)
    den = sp.Integer(1)
    for (i, j) in cells(s):
        num *= q ** (2 * i) * (q ** 2 - 1 - q * z) + q ** (2 * j + 1) * z
    for h in hooks(s).values():
        den *= q ** (2 * h) - 1
    return sp.cancel(sp.together(num / den))


def a(d):
    """`seminormalParam q d = (q - q^-1)/(1 - q^{-2d})`."""
    return (q - 1 / q) / (1 - q ** (-2 * d))


def addable(s):
    out = []
    rows = list(s)
    for i in range(len(rows) + 1):
        prev = rows[i - 1] if i > 0 else None
        cur = rows[i] if i < len(rows) else 0
        if prev is None or cur < prev:
            t = list(rows)
            if i < len(t):
                t[i] += 1
            else:
                t.append(1)
            out.append((tuple(t), cur - i))
    return out


def removable(s):
    out = []
    rows = list(s)
    for i in range(len(rows)):
        nxt = rows[i + 1] if i + 1 < len(rows) else 0
        if rows[i] > nxt:
            t = list(rows)
            t[i] -= 1
            out.append((tuple(v for v in t if v > 0), (rows[i] - 1) - i))
    return out


def main():
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    fails = []

    print("=" * 74)
    print(f"TEST 1 -- the corner identity at SYMBOLIC z, n = 1..{NMAX}")
    print("=" * 74)
    print("  sum_{s addable} W_{mu+s} a(c(s) - c(r))  ==  z W_mu,  per removable corner r")
    for n in range(1, NMAX + 1):
        bad = []
        for mu in parts(n):
            for (_, cr) in removable(mu):
                lhs = sum(W(nu) * a(cs - cr) for (nu, cs) in addable(mu))
                if sp.simplify(sp.cancel(sp.together(lhs - z * W(mu)))) != 0:
                    bad.append((mu, cr))
        print(f"    n={n:2d}  ({len(list(parts(n))):3d} partitions): "
              f"{'OK' if not bad else 'FAIL ' + str(bad)}")
        if bad:
            fails.append(f"symbolic n={n}")

    print()
    print("=" * 74)
    print("TEST 2 -- convention D, two rows: the identity is (at most) TWO equations")
    print("=" * 74)
    zD = q ** 3 / (q ** 2 + 1)
    x = q ** 2

    def br(j):
        return sum(x ** i for i in range(j)) if j > 0 else sp.Integer(0)

    def Wd(m, k):
        return sp.cancel(x ** k * br(m - k + 1) / (1 + x) ** (m + k))

    print("  mu = (m,k), k <= m.  addable: (0,m) c=m; (1,k) c=k-1 [k<m]; (2,0) c=-2 [WEIGHT 0]")
    print("                       removable: (0,m-1) c=m-1 [m>k]; (1,k-1) c=k-2 [k>0]")
    print()
    print("  R1  (r in row 0, needs m > k):  W_(m+1,k) a(1) + W_(m,k+1) a(k-m) = z_D W_(m,k)")
    print("  R2  (r in row 1, needs k > 0):  W_(m+1,k) a(m-k+2) + W_(m,k+1) a(1) = z_D W_(m,k)")
    print("      (the W_(m,k+1) term is absent when k = m, where (1,k) is not addable)")
    print()
    bad1 = []
    bad2 = []
    for m in range(1, 10):
        for k in range(0, m + 1):
            if m > k:
                lhs = Wd(m + 1, k) * a(1) + (Wd(m, k + 1) * a(k - m) if k < m else 0)
                if sp.simplify(sp.cancel(lhs - zD * Wd(m, k))) != 0:
                    bad1.append((m, k))
            if k > 0:
                lhs = Wd(m + 1, k) * a(m - k + 2) + (Wd(m, k + 1) * a(1) if k < m else 0)
                if sp.simplify(sp.cancel(lhs - zD * Wd(m, k))) != 0:
                    bad2.append((m, k))
    print(f"    R1, m <= 9 all k: {'OK' if not bad1 else 'FAIL ' + str(bad1)}")
    print(f"    R2, m <= 9 all k: {'OK' if not bad2 else 'FAIL ' + str(bad2)}")
    if bad1:
        fails.append("R1")
    if bad2:
        fails.append("R2")
    print()
    print("  a(1) = q  exactly, so R1's first coefficient is just q.")
    print()
    print("  These are the two statements a Lean proof of the Markov condition at")
    print("  convention D would discharge -- explicit rational identities in q with the")
    print("  PROVED bracket closed form W_(m,k) = x^k [m-k+1]_x / (1+x)^{m+k}")
    print("  (`QOU.SchurWeyl.schurPrincipal_twoRow`).  What they would NOT discharge is")
    print("  the REDUCTION above, which is representation-theoretic and unformalised.")

    print()
    print("=" * 74)
    print("VERDICT:", "all tests pass" if not fails else f"FAILURES: {fails}")
    print("=" * 74)
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
