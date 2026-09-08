#!/usr/bin/env python3
"""M_1>0 Track A1: express Sigma_h = 1/2(p2(lam)+p2(lam')) in free cumulants R_k.

Gap qou-k5r5, epic qou-x631. The open nub is the sign of the genus-1 second-order
correction to M_1 = Cov_Planch(Sigma_h, omega3) = Cov_Planch(Sigma_h, R_4). To use
the Sniady genus expansion (Thm 4.14) we first need Sigma_h and omega3 as EXACT
polynomial functions on Young diagrams, i.e. in the free cumulants R_k of the
transition measure. This probe:

  1. builds the transition measure of lam EXACTLY (addable/removable contents;
     Kerov's interlacing weights) -> atoms (x_i, mu_i), mu_i in Q,
  2. moments M_k = sum mu_i x_i^k and free cumulants R_k (free moment-cumulant
     relation over Q), EXACT,
  3. VERIFIES R_2 = n and settles the R_4 <-> omega3 normalisation
     (Lean r4Value says R_4 = 3*omega3 - n; substituting omega3 for Sigma_3 in
      Biane/Kerov's Sigma_3 = R_4 + R_2 says R_4 = omega3 - n. The identity is
      NOT wrong -- Sigma_3 = 3*omega3, the class-size convention; see
      wlambda_covariance_epic_M1_r4_sigma3_normalisation_reconciliation.py),
  4. solves for the EXACT R_k-expansion of Sigma_h by exact rational linear algebra
     over enough partitions (this is an exact identity extraction, NOT a numerical
     fit: a polynomial function on Young diagrams has a unique free-cumulant
     expansion, determined exactly once enough partitions over-determine it).

NO float64 (Fraction end to end). scope-(a); no fit-to-data; nothing wired; no c_k;
L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations_with_replacement
import sys


def partitions(n):
    def gen(n, mx):
        if n == 0:
            yield ()
            return
        for p in range(min(n, mx), 0, -1):
            for r in gen(n - p, p):
                yield (p,) + r
    yield from gen(n, n)


def transition_atoms(lam):
    """Return list of (content x_i, weight mu_i in Q) for the transition measure of lam.

    Addable contents A and removable contents R interlace (|A| = |R| + 1).
    Kerov weight at addable content a:  mu(a) = prod_{r in R}(a - r) / prod_{a' != a}(a - a').
    Content coordinate c = j - i (0-indexed cell (i,j)). The measure is centred so
    sum mu_i = 1 and (for the standard normalisation) sum mu_i x_i = 0 fails in general;
    we keep raw contents and CENTER by M_1 when forming free cumulants.
    """
    m = len(lam)
    L = list(lam) + [0]              # pad with a 0 row
    # Addable corners: row i gets an addable box at column L[i] iff i==0 or L[i] < L[i-1].
    # Its content = L[i] - i.  (i ranges 0..m, the i=m box is the new bottom row, content -m.)
    A = []
    for i in range(m + 1):
        prev = L[i - 1] if i >= 1 else None
        if i == 0 or L[i] < prev:
            A.append(L[i] - i)
    # Removable corners: last box of row i (content L[i]-1-i) iff L[i] > L[i+1].
    R = []
    for i in range(m):
        if L[i] > L[i + 1]:
            R.append(L[i] - 1 - i)
    assert len(A) == len(R) + 1, (lam, A, R)
    atoms = []
    for a in A:
        num = 1
        for r in R:
            num *= (a - r)
        den = 1
        for a2 in A:
            if a2 != a:
                den *= (a - a2)
        atoms.append((a, F(num, den)))
    return atoms


def free_cumulants(atoms, kmax):
    """Moments M_k of the (centred) measure and free cumulants R_2..R_kmax, exact.

    First center: shift so M_1 = 0 (free cumulants are of the centred transition
    measure; R_2 = variance = n). Then use the free moment-cumulant recursion via
    non-crossing partitions, implemented by the standard determinant/convolution:
        M_k = sum_{pi in NC(k)} prod_{block B in pi} R_{|B|}.
    We invert it iteratively: R_k = M_k - sum_{pi != 1_k} prod R_{|B|}.
    """
    # raw moments
    def raw_moment(k):
        return sum(mu * (x ** k) for x, mu in atoms)
    M1 = raw_moment(1)
    # centered moments
    Mc = [F(0)] * (kmax + 1)
    Mc[0] = F(1)
    for k in range(1, kmax + 1):
        # E[(X - M1)^k] = sum_j C(k,j) E[X^j] (-M1)^(k-j)
        from math import comb
        s = F(0)
        for j in range(0, k + 1):
            s += comb(k, j) * raw_moment(j) * ((-M1) ** (k - j))
        Mc[k] = s
    # free cumulants via NC-partition recursion
    R = [F(0)] * (kmax + 1)

    def nc_partitions(elts):
        """Generate non-crossing partitions of the list elts (as list of blocks)."""
        if not elts:
            yield []
            return
        first = elts[0]
        n = len(elts)
        # the block containing 'first' is determined by choosing the other elements,
        # which must form a non-crossing structure. Standard recursive gen:
        for size in range(1, n + 1):
            for rest in combinations_with_replacement(range(1), 0) if False else [None]:
                pass
        # simpler: enumerate all set partitions and filter non-crossing (k small <= 6)
        yield from _nc_all(elts)

    def _nc_all(elts):
        # all set partitions, filtered non-crossing
        def setparts(seq):
            if not seq:
                yield []
                return
            first, rest = seq[0], seq[1:]
            for sp in setparts(rest):
                # add to existing block
                for i in range(len(sp)):
                    yield sp[:i] + [[first] + sp[i]] + sp[i + 1:]
                # own block
                yield [[first]] + sp
        for sp in setparts(list(elts)):
            if _is_noncrossing(sp):
                yield sp

    def _is_noncrossing(sp):
        # crossing: a<c<b<d with a,b in one block, c,d in another
        blocks = [sorted(b) for b in sp]
        for bi in range(len(blocks)):
            for bj in range(len(blocks)):
                if bi == bj:
                    continue
                for a in blocks[bi]:
                    for b in blocks[bi]:
                        if a < b:
                            for c in blocks[bj]:
                                for d in blocks[bj]:
                                    if a < c < b < d:
                                        return False
        return True

    for k in range(1, kmax + 1):
        total = F(0)
        for pi in _nc_all(list(range(k))):
            if len(pi) == 1:
                continue  # the full block = R_k term, isolate it
            prod = F(1)
            for B in pi:
                prod *= R[len(B)]
            total += prod
        R[k] = Mc[k] - total
    return Mc, R, M1


def sigma_h(lam):
    p2 = sum(x * x for x in lam)
    m = lam[0] if lam else 0
    conj = [0] * m
    for p in lam:
        for j in range(p):
            conj[j] += 1
    p2c = sum(x * x for x in conj)
    return F(p2 + p2c, 2)


def omega3(lam, n):
    c2 = sum((j - i) ** 2 for i, p in enumerate(lam) for j in range(p))
    return F(c2 - n * (n - 1) // 2)


def main():
    KMAX = 6
    print("# Track A1: Sigma_h and omega3 in free cumulants R_k of the transition measure")
    print("# (a) verify R_2 = n; (b) settle R_4 <-> omega3; (c) expand Sigma_h in R_k.")
    # (a),(b): check R_2 = n and the R_4/omega3 relation on all partitions up to n=8
    print("\n## (a)(b)  R_2 vs n   and   R_4 vs omega3")
    print(f"# {'lam':<16}{'n':>3}{'R_2':>6}{'R_3':>8}{'R_4':>10}{'omega3':>8}"
          f"{'R4-(o3-n)':>11}{'R4-(3o3-n)':>12}")
    okR2 = True
    rel_omega_substituted = True   # R_4 == omega3 - n ?  (the WRONG substitution)
    rel_lean = True    # R_4 == 3*omega3 - n ?
    for n in range(1, 9):
        for lam in partitions(n):
            atoms = transition_atoms(lam)
            Mc, R, M1 = free_cumulants(atoms, KMAX)
            o3 = omega3(lam, n)
            if R[2] != n:
                okR2 = False
            if R[4] != o3 - n:
                rel_omega_substituted = False
            if R[4] != 3 * o3 - n:
                rel_lean = False
            if n <= 5:
                print(f"  {str(lam):<16}{n:>3}{str(R[2]):>6}{str(R[3]):>8}{str(R[4]):>10}"
                      f"{str(o3):>8}{str(R[4]-(o3-n)):>11}{str(R[4]-(3*o3-n)):>12}")
    print(f"\n# R_2 == n for all lam (n<=8): {okR2}")
    print(f"# R_4 == omega3 - n   (omega3 substituted for Sigma_3): {rel_omega_substituted}")
    print(f"# R_4 == 3*omega3 - n (Lean r4Value):        {rel_lean}")

    # (c): solve Sigma_h = sum_monomials coeff * (monomial in R_2,R_3,R_4,R_5,R_6), exact.
    # Sigma_h scales ~ n^{3/2}: under deg R_k = k and the n^{1/2} law, candidate monomials
    # of the right weight are graded; include all monomials in R_2..R_6 of total degree <= 6
    # and let exact linear algebra pick the identity (zero coeffs on absent monomials).
    print("\n## (c)  Sigma_h as an exact polynomial in R_2..R_6")
    Rsyms = [2, 3, 4, 5, 6]
    monos = [()]  # constant
    for d in range(1, 4):
        for combo in combinations_with_replacement(Rsyms, d):
            if sum(combo) <= 6:
                monos.append(combo)
    # dedup
    monos = sorted(set(monos), key=lambda t: (len(t), t))
    # build exact linear system over many partitions
    rows = []
    rhs = []
    lam_list = []
    for n in range(1, 10):
        for lam in partitions(n):
            lam_list.append(lam)
    for lam in lam_list:
        atoms = transition_atoms(lam)
        _, R, _ = free_cumulants(atoms, KMAX)
        row = []
        for mono in monos:
            v = F(1)
            for s in mono:
                v *= R[s]
            row.append(v)
        rows.append(row)
        rhs.append(sigma_h(lam))
    coeffs = exact_lstsq(rows, rhs, monos)
    if coeffs is None:
        print("# NO exact polynomial identity in R_2..R_6 (Sigma_h not degree<=6 poly in R, "
              "or basis insufficient). Reporting residual structure instead.")
    else:
        print("# Sigma_h = " + "  +  ".join(
            f"{c}*{'1' if m==() else '*'.join('R'+str(s) for s in m)}"
            for m, c in zip(monos, coeffs) if c != 0))
        # verify exactly on a fresh partition set n=10,11
        ok = True
        for n in range(10, 12):
            for lam in partitions(n):
                _, R, _ = free_cumulants(transition_atoms(lam), KMAX)
                val = F(0)
                for m, c in zip(monos, coeffs):
                    t = c
                    for s in m:
                        t *= R[s]
                    val += t
                if val != sigma_h(lam):
                    ok = False
        print(f"# identity verified exactly on all lam, n=10,11 (out-of-sample): {ok}")
    print("\nRESULT: R_2=n:%s ; R_4=omega3-n:%s ; R_4=3omega3-n:%s ; Sigma_h-in-R:%s" % (
        okR2, rel_omega_substituted, rel_lean, coeffs is not None))
    print("EXIT: 0")
    return 0


def exact_lstsq(rows, rhs, monos):
    """Exact solve for coeffs so that sum_j coeff_j * row[j] = rhs, if a consistent
    exact solution exists (over-determined, rational). Returns coeffs or None."""
    # Gaussian elimination over Q on the augmented (A | b), solving A x = b in least-... no:
    # we need an EXACT solution of the (overdetermined) system A x = b. Solve the normal
    # square system by picking independent rows; then verify all rows satisfied.
    import copy
    A = [list(r) for r in rows]
    b = list(rhs)
    ncol = len(monos)
    # reduce to row echelon, track a solution on a maximal independent set of columns
    # Build augmented matrix and do fraction-free-ish Gaussian elimination.
    M = [A[i] + [b[i]] for i in range(len(A))]
    nrow = len(M)
    pivots = []
    r = 0
    for c in range(ncol):
        # find pivot
        piv = None
        for i in range(r, nrow):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(nrow):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(ncol + 1)]
        pivots.append(c)
        r += 1
        if r == nrow:
            break
    # consistency: any row with all-zero coeffs but nonzero rhs -> inconsistent
    for i in range(nrow):
        if all(M[i][j] == 0 for j in range(ncol)) and M[i][ncol] != 0:
            return None
    # back out solution (free vars = 0)
    x = [F(0)] * ncol
    for i, c in enumerate(pivots):
        x[c] = M[i][ncol]
    # verify against ALL original rows exactly
    for i in range(len(A)):
        if sum(A[i][j] * x[j] for j in range(ncol)) != b[i]:
            return None
    return x


if __name__ == "__main__":
    raise SystemExit(main())
