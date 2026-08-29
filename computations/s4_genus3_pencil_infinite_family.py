#!/usr/bin/env python3
"""How many genus-3 curves admit an S_4 action?  INFINITELY MANY.  (bean qou-8p1a)

Context
-------
The eightfold-way chapter's colour route wanted to reach the Klein quartic by:

    Bring Sigma_4 (genus 4, Aut = S_5)
      --pinch an S_4-invariant cycle-->  nodal, geometric genus 3
      --normalize-->                    Klein quartic (Aut = PSL(2,7))

with the selection step justified by "S_4 survives the pinch and S_4 embeds in
PSL(2,7)".  Two prior results already weakened that:

  1. The Hurwitz-bound phrasing was withdrawn -- an upper bound on |Aut| is not
     a selection principle.
  2. `s4_genus3_competitor_fermat.py` exhibited ONE competitor: the Fermat
     quartic x^4+y^4+z^4, genus 3, |Aut| = 96, containing S_4.  So the S_4
     datum does not separate Klein from Fermat.

Bean qou-8p1a asks how bad it is: is the competitor set {Klein, Fermat} -- in
which case ONE extra invariant settles qou-8pl1 -- or is it large, in which case
the S_4 bridge is nearly vacuous and the colour route needs a different
organising datum?

Result
------
It is large.  Not "a few more curves": an INFINITE one-parameter family.

We prove, in exact rational arithmetic, that the S_4-invariant ternary quartics
form a 2-dimensional vector space -- i.e. a PENCIL of plane curves

    C_lambda :  x^4 + y^4 + z^4 + lambda*(x^2 y^2 + y^2 z^2 + z^2 x^2) = 0

-- and that C_lambda is smooth (hence genus 3, by the genus-degree formula)
for every lambda except the three values {2, -2, -1}, plus the degenerate
member at lambda = infinity.  The Fermat quartic is the member lambda = 0.

NAMING.  This module calls the pencil parameter `L` (Python reserves the word
`lambda`).  The eightfold-way chapter calls it **`t`**, deliberately NOT
`lambda`, because throughout that chapter `lambda` denotes a partition
(`lambda = (3)`, `lambda = (2,1)`, ...) and reusing the glyph for a pencil
coordinate would be a silent notation collision.  `L` here == `t` in the prose.

So "genus 3 and admits S_4" is satisfied by a whole P^1 of curves, not by two.

What is machine-verified here (exact arithmetic, no floating point)
------------------------------------------------------------------
  C1  G := <coordinate permutations, even sign-changes> is a group of order 24
      inside GL_3(Z), and G intersects the scalars only in the identity, so G
      injects into PGL_3 and acts faithfully on P^2.
  C2  Element-order profile of G is {1:1, 2:9, 3:8, 4:6}.  This pins G ~= S_4
      among the fifteen groups of order 24 (in particular it rules out SL(2,3),
      the only other order-24 group with 8 elements of order 3 and 6 of order
      4 -- SL(2,3) has a single involution and eight elements of order 6).
  C3  V_4 = the even sign-changes is normal in G, and the quotient S_3 acts
      faithfully on V_4 \ {1} as the full symmetric group -- the structural
      confirmation G = V_4 : S_3 ~= S_4.
  C4  The commutant of G in M_3(Q) is 1-dimensional (scalars only).  By Schur
      this says the action on the 3-space is ABSOLUTELY IRREDUCIBLE, and it is
      also exactly the input the finiteness argument below needs.
  C5  The space of G-invariant quartic forms is 2-dimensional, spanned by
      q0 = x^4+y^4+z^4 and q1 = x^2y^2+y^2z^2+z^2x^2.  Hence "S_4-invariant
      quartic" cuts out a pencil, not a finite set.
  C6  C_lambda is singular exactly for lambda in {2, -2, -1}:
        - the 2x2 and 3x3 determinants controlling the two nondegenerate cases
          are verified as exact polynomial identities in lambda,
        - and an explicit singular point is exhibited and checked (F = F_x =
          F_y = F_z = 0) at each of the three bad values.
  C7  A smooth plane quartic has genus (4-1)(4-2)/2 = 3.

From "infinitely many lambda" to "infinitely many CURVES"
---------------------------------------------------------
Distinct lambda give distinct curves as subvarieties (q0 and q1 are linearly
independent, so the defining forms are non-proportional).  That alone does not
give infinitely many ISOMORPHISM classes, so here is the argument that does.

Let G = S_4 in PGL_3 as above and suppose g in PGL_3 carries C_lambda to
C_mu.  Then both G and gGg^{-1} are subgroups of Aut(C_mu).

  * Aut(C_mu) is FINITE, because C_mu is a smooth projective curve of genus
    3 >= 2.  (Only finiteness is used.  We deliberately do NOT invoke the
    sharp Hurwitz bound 84(g-1) here: an earlier step of this same arc was
    withdrawn for misusing that bound, and finiteness is all that is needed.)
  * So Aut(C_mu) contains only finitely many subgroups isomorphic to S_4, and
    g is determined, up to the normalizer N := N_{PGL_3}(G), by which one of
    them gGg^{-1} is.
  * N is finite: by C4 the centralizer of G in PGL_3 is trivial (Schur --
    the commutant is scalars, which are trivial in PGL_3), so N = N/C embeds
    into the finite group Aut(S_4).

Hence only finitely many g can occur, and each g yields at most one lambda
(namely the pencil member g^{-1}C_mu).  So {lambda : C_lambda ~= C_mu} is
FINITE for each mu.  A P^1 worth of lambda covered by finite fibres therefore
meets infinitely many isomorphism classes.

Conclusion:  infinitely many pairwise non-isomorphic genus-3 curves admit a
faithful S_4 action.

Verdict for qou-8pl1 / qou-8p1a
-------------------------------
The bean's second branch is the true one.  The S_4 bridge is not merely
"non-selective between two candidates" -- it is nearly VACUOUS as a selection
principle: it fails to cut a P^1 down at all.  Consequently:

  * qou-8p1b (find an invariant separating Klein from Fermat) is, on its own,
    NOT enough to settle qou-8pl1.  Separating two named curves does not
    single out Klein from an infinite family.  That bean needs re-scoping: the
    invariant has to be one the PINCH actually determines, not one that merely
    tells two curves apart.
  * The colour route needs a different organising datum than "S_4 survives".

Scope
-----
scope-(a), same as the Fermat result.  This refutes the S_4 bridge AS AN
ARGUMENT.  It does NOT refute the Bring -> Klein degeneration itself, which
remains open: an infinite family of curves admits S_4, and the Klein quartic
is still free to be the one the pinch produces -- there is simply nothing in
the S_4 datum that says so.

Not verified here (stated as literature, flagged honestly)
----------------------------------------------------------
  * The specific lambda at which the Klein quartic sits in this pencil.  The
    classification implies Klein IS projectively equivalent to some member
    (its canonical model is a plane quartic carrying an irreducible S_4, and
    the two 3-dimensional irreducible representations of S_4 have the same
    image in PGL_3, so its equation must be G-invariant for a conjugate of
    this very G) -- but pinning the value needs arithmetic over Q(sqrt(-7))
    and is not done here.
  * Hyperelliptic genus-3 curves admitting S_4 (e.g. y^2 = x^8 + 14x^4 + 1,
    with Aut of order 48) lie OUTSIDE this pencil, since their canonical map
    is 2:1 onto a conic rather than an embedding.  They only make the
    competitor set larger, so they do not affect the conclusion.

Exact arithmetic only: Fraction / integer / Q(sqrt d) throughout, no floats.
"""
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
_OUT = HERE / "s4-genus3-pencil-infinite-family.witness.json"

Mat = tuple  # 3x3 tuple-of-tuples of ints


# ---------------------------------------------------------------------------
# Exact dense univariate polynomials over Q (the pencil parameter `lambda`).
# ---------------------------------------------------------------------------
class Poly:
    __slots__ = ("c",)

    def __init__(self, coeffs) -> None:
        c = [Fraction(x) for x in coeffs]
        while len(c) > 1 and c[-1] == 0:
            c.pop()
        self.c = c

    def __add__(self, o: "Poly") -> "Poly":
        n = max(len(self.c), len(o.c))
        return Poly([self[i] + o[i] for i in range(n)])

    def __sub__(self, o: "Poly") -> "Poly":
        n = max(len(self.c), len(o.c))
        return Poly([self[i] - o[i] for i in range(n)])

    def __mul__(self, o: "Poly") -> "Poly":
        out = [Fraction(0)] * (len(self.c) + len(o.c) - 1)
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(o.c):
                    out[i + j] += a * b
        return Poly(out)

    def __getitem__(self, i: int) -> Fraction:
        return self.c[i] if i < len(self.c) else Fraction(0)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Poly) and self.c == o.c

    def __repr__(self) -> str:
        if self.c == [Fraction(0)]:
            return "0"
        parts = []
        for i, a in enumerate(self.c):
            if not a:
                continue
            if i == 0:
                parts.append(f"{a}")
            elif i == 1:
                parts.append(f"{a}*L" if a != 1 else "L")
            else:
                parts.append(f"{a}*L^{i}" if a != 1 else f"L^{i}")
        return " + ".join(reversed(parts))


L = Poly([0, 1])  # the parameter lambda
ONE = Poly([1])


def poly_det3(m) -> Poly:
    """Determinant of a 3x3 matrix of Poly, by cofactor expansion."""
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return (
        a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    )


# ---------------------------------------------------------------------------
# Exact arithmetic in Q(sqrt d): numbers a + b*sqrt(d), a,b in Q.
# ---------------------------------------------------------------------------
class Quad:
    __slots__ = ("a", "b", "d")

    def __init__(self, a, b, d) -> None:
        self.a, self.b, self.d = Fraction(a), Fraction(b), Fraction(d)

    def __add__(self, o: "Quad") -> "Quad":
        return Quad(self.a + o.a, self.b + o.b, self.d)

    def __mul__(self, o: "Quad") -> "Quad":
        # (a+b r)(c+e r) = ac + b e d + (a e + b c) r,  r^2 = d
        return Quad(
            self.a * o.a + self.b * o.b * self.d,
            self.a * o.b + self.b * o.a,
            self.d,
        )

    def __pow__(self, n: int) -> "Quad":
        r = Quad(1, 0, self.d)
        for _ in range(n):
            r = r * self
        return r

    def scale(self, k) -> "Quad":
        k = Fraction(k)
        return Quad(self.a * k, self.b * k, self.d)

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def __repr__(self) -> str:
        return f"({self.a} + {self.b}*sqrt({self.d}))"


# ---------------------------------------------------------------------------
# Exact linear algebra over Q.
# ---------------------------------------------------------------------------
def rref(rows, ncols):
    """Row-reduce a list of rows (lists of Fraction).  Returns (rref, pivots)."""
    m = [list(r) for r in rows]
    pivots = []
    r = 0
    for col in range(ncols):
        piv = None
        for k in range(r, len(m)):
            if m[k][col] != 0:
                piv = k
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        inv = Fraction(1) / m[r][col]
        m[r] = [x * inv for x in m[r]]
        for k in range(len(m)):
            if k != r and m[k][col] != 0:
                f = m[k][col]
                m[k] = [x - f * y for x, y in zip(m[k], m[r])]
        pivots.append(col)
        r += 1
        if r == len(m):
            break
    return m, pivots


def nullspace_dim(rows, ncols) -> int:
    _, pivots = rref(rows, ncols)
    return ncols - len(pivots)


# ---------------------------------------------------------------------------
# The group G = V_4 : S_3 acting on P^2.
# ---------------------------------------------------------------------------
def matmul(a: Mat, b: Mat) -> Mat:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


IDENT: Mat = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def build_group() -> list:
    """G = { diag(e) * P_sigma : prod(e) = +1, sigma in S_3 }, order 24."""
    gens = []
    # coordinate permutations
    for sigma in itertools.permutations(range(3)):
        p = tuple(tuple(1 if sigma[i] == j else 0 for j in range(3)) for i in range(3))
        gens.append(p)
    # even sign changes
    for e in itertools.product((1, -1), repeat=3):
        if e[0] * e[1] * e[2] == 1:
            gens.append(tuple(tuple(e[i] if i == j else 0 for j in range(3)) for i in range(3)))
    # close under multiplication
    G = set(gens)
    G.add(IDENT)
    changed = True
    while changed:
        changed = False
        for a in list(G):
            for b in list(G):
                c = matmul(a, b)
                if c not in G:
                    G.add(c)
                    changed = True
    return sorted(G)


def element_order(g: Mat) -> int:
    n, cur = 1, g
    while cur != IDENT:
        cur = matmul(cur, g)
        n += 1
        if n > 100:
            raise RuntimeError("order blew up")
    return n


def is_scalar(g: Mat) -> bool:
    return (
        g[0][1] == g[0][2] == g[1][0] == g[1][2] == g[2][0] == g[2][1] == 0
        and g[0][0] == g[1][1] == g[2][2]
    )


# ---------------------------------------------------------------------------
# Action on quartic forms.
# ---------------------------------------------------------------------------
def quartic_monomials():
    out = []
    for a in range(5):
        for b in range(5 - a):
            out.append((a, b, 4 - a - b))
    return out


MONOS = quartic_monomials()
MIDX = {m: i for i, m in enumerate(MONOS)}


def signed_perm_data(g: Mat):
    """For a signed permutation matrix, return (col_of_row, sign_of_row)."""
    cols, signs = [], []
    for i in range(3):
        nz = [(j, g[i][j]) for j in range(3) if g[i][j] != 0]
        if len(nz) != 1:
            raise RuntimeError("not a signed permutation matrix")
        j, s = nz[0]
        cols.append(j)
        signs.append(s)
    return cols, signs


def quartic_action_matrix(g: Mat):
    """15x15 matrix of  F -> F o g  on quartic forms, in the MONOS basis."""
    cols, signs = signed_perm_data(g)
    M = [[Fraction(0)] * 15 for _ in range(15)]
    for idx, a in enumerate(MONOS):
        sign = 1
        newexp = [0, 0, 0]
        for i in range(3):
            if a[i]:
                sign *= signs[i] ** a[i]
                newexp[cols[i]] += a[i]
        M[MIDX[tuple(newexp)]][idx] = Fraction(sign)
    return M


def form_vector(terms):
    """Build the 15-vector of a quartic given {exponent-triple: coeff}."""
    v = [Fraction(0)] * 15
    for e, c in terms.items():
        v[MIDX[e]] = Fraction(c)
    return v


Q0 = form_vector({(4, 0, 0): 1, (0, 4, 0): 1, (0, 0, 4): 1})
Q1 = form_vector({(2, 2, 0): 1, (2, 0, 2): 1, (0, 2, 2): 1})


# ---------------------------------------------------------------------------
# The pencil and its singular members.
# ---------------------------------------------------------------------------
def F_and_partials(x, y, z, lam, one):
    """F and its three partials at (x,y,z) for parameter lam.

    Arguments are Quad numbers over a common sqrt(d); `lam` and `one` too.
    F   = x^4+y^4+z^4 + lam*(x^2y^2 + y^2z^2 + z^2x^2)
    F_x = 4x^3 + 2*lam*x*(y^2+z^2)      (and cyclic)
    """
    x2, y2, z2 = x * x, y * y, z * z
    F = (
        x2 * x2
        + y2 * y2
        + z2 * z2
        + lam * (x2 * y2 + y2 * z2 + z2 * x2)
    )
    Fx = (x2 * x).scale(4) + (lam * x * (y2 + z2)).scale(2)
    Fy = (y2 * y).scale(4) + (lam * y * (x2 + z2)).scale(2)
    Fz = (z2 * z).scale(4) + (lam * z * (x2 + y2)).scale(2)
    return F, Fx, Fy, Fz


def main() -> int:
    print("=" * 74)
    print("qou-8p1a : how many genus-3 curves admit S_4?")
    print("=" * 74)

    checks: dict[str, bool] = {}

    # -- C1 : the group ----------------------------------------------------
    G = build_group()
    checks["C1_order_24"] = len(G) == 24
    closed = all(matmul(a, b) in set(G) for a in G for b in G)
    checks["C1_closed"] = closed
    scalars_in_G = [g for g in G if is_scalar(g)]
    checks["C1_faithful_in_PGL3"] = scalars_in_G == [IDENT]
    print(f"\nC1  |G| = {len(G)}, closed = {closed}, "
          f"G n scalars = {{I}} : {checks['C1_faithful_in_PGL3']}")

    # -- C2 : element-order profile ---------------------------------------
    profile: dict[int, int] = {}
    for g in G:
        o = element_order(g)
        profile[o] = profile.get(o, 0) + 1
    expected = {1: 1, 2: 9, 3: 8, 4: 6}
    checks["C2_order_profile_is_S4"] = profile == expected
    print(f"C2  element-order profile = {dict(sorted(profile.items()))} "
          f"(S_4 expects {expected}) : {checks['C2_order_profile_is_S4']}")

    # -- C3 : V_4 normal, S_3 acts faithfully -----------------------------
    V4 = [g for g in G if all(g[i][j] == 0 for i in range(3) for j in range(3) if i != j)]
    checks["C3_V4_order_4"] = len(V4) == 4
    Gs = set(G)
    inv = {g: next(h for h in G if matmul(g, h) == IDENT) for g in G}
    normal = all(matmul(matmul(g, v), inv[g]) in set(V4) for g in G for v in V4)
    checks["C3_V4_normal"] = normal
    nontriv = [v for v in V4 if v != IDENT]
    induced = set()
    for g in G:
        perm = tuple(nontriv.index(matmul(matmul(g, v), inv[g])) for v in nontriv)
        induced.add(perm)
    checks["C3_S3_full_on_V4"] = len(induced) == 6
    print(f"C3  |V_4| = {len(V4)}, normal = {normal}, "
          f"induced action on V_4\\{{1}} has order {len(induced)} (want 6)")

    # -- C4 : commutant is scalars (absolute irreducibility) ---------------
    # Solve  X g = g X  for all g in G;  X in M_3(Q) is 9 unknowns X[i][j].
    rows = []
    for g in G:
        # (Xg - gX)[r][c] = sum_k X[r][k] g[k][c] - sum_k g[r][k] X[k][c]
        for r in range(3):
            for c in range(3):
                row = [Fraction(0)] * 9
                for k in range(3):
                    row[3 * r + k] += g[k][c]
                    row[3 * k + c] -= g[r][k]
                rows.append(row)
    commutant_dim = nullspace_dim(rows, 9)
    checks["C4_commutant_is_scalars"] = commutant_dim == 1
    print(f"C4  dim of commutant of G in M_3(Q) = {commutant_dim} "
          f"(1 = scalars only => absolutely irreducible)")

    # -- C5 : invariant quartics form a pencil -----------------------------
    rows = []
    for g in G:
        A = quartic_action_matrix(g)
        for i in range(15):
            row = [A[i][j] - (Fraction(1) if i == j else Fraction(0)) for j in range(15)]
            rows.append(row)
    inv_dim = nullspace_dim(rows, 15)
    checks["C5_invariant_space_dim_2"] = inv_dim == 2

    def in_nullspace(v):
        return all(
            sum(row[j] * v[j] for j in range(15)) == 0 for row in rows
        )

    checks["C5_q0_invariant"] = in_nullspace(Q0)
    checks["C5_q1_invariant"] = in_nullspace(Q1)
    # independence of q0, q1
    _, piv = rref([Q0, Q1], 15)
    checks["C5_q0_q1_independent"] = len(piv) == 2
    print(f"C5  dim of S_4-invariant quartics = {inv_dim} (want 2)")
    print(f"    q0 = x^4+y^4+z^4 invariant           : {checks['C5_q0_invariant']}")
    print(f"    q1 = x^2y^2+y^2z^2+z^2x^2 invariant  : {checks['C5_q1_invariant']}")
    print(f"    q0, q1 linearly independent          : {checks['C5_q0_q1_independent']}")
    print("    => the S_4-invariant quartics are a PENCIL")
    print("       C_L : x^4+y^4+z^4 + L*(x^2y^2+y^2z^2+z^2x^2) = 0")

    # -- C6 : which members are singular? ----------------------------------
    # A singular point needs, for each coordinate, either that coordinate = 0
    # or  2*(its square) + L*(sum of the other two squares) = 0.
    #
    # Case A  exactly one coordinate nonzero (say x): condition reads 2x^2 = 0,
    #         impossible.  So no singular point ever arises here.
    # Case B  exactly two nonzero (say x,y; z=0): need the 2x2 system
    #         [[2,L],[L,2]] to kill (x^2, y^2) nontrivially -> det = 4 - L^2.
    # Case C  all three nonzero: need [[2,L,L],[L,2,L],[L,L,2]] singular
    #         -> det = (2-L)^2 * (2+2L).
    two = Poly([2])
    detB = poly_det3([[two, L, Poly([0])],
                      [L, two, Poly([0])],
                      [Poly([0]), Poly([0]), ONE]])   # pad to 3x3 with a 1
    detB_expected = Poly([4, 0, -1])                  # 4 - L^2
    checks["C6_detB_identity"] = detB == detB_expected

    detC = poly_det3([[two, L, L], [L, two, L], [L, L, two]])
    detC_expected = (two - L) * (two - L) * (Poly([2, 2]))   # (2-L)^2 (2+2L)
    checks["C6_detC_identity"] = detC == detC_expected
    print(f"\nC6  det(case B) = {detB}   (want 4 - L^2)      : "
          f"{checks['C6_detB_identity']}")
    print(f"    det(case C) = {detC}")
    print(f"      = (2-L)^2 (2+2L)                        : "
          f"{checks['C6_detC_identity']}")

    # roots of the two determinants
    bad = sorted({Fraction(2), Fraction(-2), Fraction(-1)})
    print(f"    => singular candidates L in {[str(b) for b in bad]}")

    # exhibit an explicit singular point at each bad L, and verify exactly
    witnesses = {}
    singular_ok = True
    #   L = -2 : point (1:1:0)     over Q
    #   L = -1 : point (1:1:1)     over Q
    #   L =  2 : point (1:i:0)     over Q(sqrt(-1))
    cases = [
        (Fraction(-2), (1, 0), (1, 0), (0, 0), 1, "(1:1:0)"),
        (Fraction(-1), (1, 0), (1, 0), (1, 0), 1, "(1:1:1)"),
        (Fraction(2), (1, 0), (0, 1), (0, 0), -1, "(1:i:0)"),
    ]
    for lam_val, xc, yc, zc, d, label in cases:
        lam = Quad(lam_val, 0, d)
        one = Quad(1, 0, d)
        x = Quad(xc[0], xc[1], d)
        y = Quad(yc[0], yc[1], d)
        z = Quad(zc[0], zc[1], d)
        F, Fx, Fy, Fz = F_and_partials(x, y, z, lam, one)
        ok = F.is_zero() and Fx.is_zero() and Fy.is_zero() and Fz.is_zero()
        singular_ok &= ok
        witnesses[str(lam_val)] = {"point": label, "F_and_all_partials_vanish": ok}
        print(f"    L = {str(lam_val):>2} : singular point {label:<8} "
              f"F=Fx=Fy=Fz=0 : {ok}")
    checks["C6_explicit_singular_points"] = singular_ok

    # a couple of smooth spot-checks: the kernel conditions fail, so no
    # singular point exists -- verified by the determinants being nonzero.
    smooth_samples = [Fraction(0), Fraction(1), Fraction(3), Fraction(-3),
                      Fraction(1, 2), Fraction(7)]
    smooth_ok = True
    for lam_val in smooth_samples:
        dB = sum(detB[i] * lam_val ** i for i in range(len(detB.c)))
        dC = sum(detC[i] * lam_val ** i for i in range(len(detC.c)))
        ok = dB != 0 and dC != 0
        smooth_ok &= ok
    checks["C6_samples_smooth"] = smooth_ok
    print(f"    smooth spot-checks {[str(s) for s in smooth_samples]} : {smooth_ok}")

    # -- C7 : genus --------------------------------------------------------
    genus = (4 - 1) * (4 - 2) // 2
    checks["C7_genus_3"] = genus == 3
    print(f"\nC7  smooth plane quartic genus = (4-1)(4-2)/2 = {genus}")

    all_ok = all(checks.values())
    print("\n" + "=" * 74)
    print(f"ALL CHECKS PASS : {all_ok}")
    print("=" * 74)
    print("""
VERDICT (bean qou-8p1a)
-----------------------
The S_4-admitting genus-3 curves are NOT a short list.  They include the
pencil C_L for every L outside {2, -2, -1}: an infinite one-parameter family,
of which the Fermat quartic (L = 0) is a single member.  Since the fibres of
L -> [C_L] in moduli are finite (see the module docstring: Aut of a genus-3
curve is finite, and N_{PGL_3}(S_4) is finite because the commutant computed
in C4 is scalars), infinitely many pairwise non-isomorphic genus-3 curves
admit a faithful S_4 action.

CONSEQUENCE FOR THE SIBLING BEANS
  * qou-8p1b as written ("find an invariant separating Klein from Fermat")
    is no longer sufficient to settle qou-8pl1 -- separating two named curves
    says nothing about an infinite family.  Re-scope it: the invariant must be
    one the PINCH determines, not merely one that tells two curves apart.
  * qou-8p1c (period matrix) is likewise not the bottleneck: the bottleneck is
    that the S_4 datum carries almost no information, so no amount of
    invariant-computing on two hand-picked curves closes the argument.

SCOPE: scope-(a).  The BRIDGE ARGUMENT is refuted, not the degeneration.
""")

    payload = {
        "schema": "witness/v1",
        "description": (
            "The S_4 bridge is nearly vacuous: the S_4-invariant ternary "
            "quartics form a pencil, so infinitely many pairwise "
            "non-isomorphic genus-3 curves admit S_4. Bean qou-8p1a "
            "(parent qou-8pl1)."
        ),
        "computation": {
            "script": "computations/s4_genus3_pencil_infinite_family.py",
            "arithmetic": "exact Fraction / Z / Q(sqrt d); no floating point",
        },
        "data": {
            "group": {
                "construction": "G = V_4 : S_3 < GL_3(Z), even sign changes and coordinate permutations",
                "order": len(G),
                "element_order_profile": {str(k): v for k, v in sorted(profile.items())},
                "isomorphism_type": "S_4",
                "pins_S4_because": (
                    "profile {1:1,2:9,3:8,4:6} is unique to S_4 among the fifteen "
                    "groups of order 24; SL(2,3) shares the 3- and 4-counts but "
                    "has one involution and eight elements of order 6"
                ),
                "faithful_in_PGL3": checks["C1_faithful_in_PGL3"],
                "commutant_dim_in_M3Q": commutant_dim,
                "absolutely_irreducible": checks["C4_commutant_is_scalars"],
            },
            "pencil": {
                "invariant_quartic_space_dim": inv_dim,
                "basis": ["x^4 + y^4 + z^4", "x^2y^2 + y^2z^2 + z^2x^2"],
                "family": "C_L : x^4+y^4+z^4 + L*(x^2y^2+y^2z^2+z^2x^2) = 0",
                "parameter_name_note": (
                    "this module calls the pencil parameter L (Python reserves "
                    "'lambda'); the eightfold-way chapter calls it t, "
                    "deliberately not lambda, which denotes a partition there"
                ),
                "singular_parameters": ["2", "-2", "-1"],
                "singular_point_witnesses": witnesses,
                "degenerate_member": "L = infinity (the form q1 alone)",
                "smooth_member_genus": genus,
                "fermat_quartic_is_member": "L = 0",
            },
            "verdict": (
                "Infinitely many pairwise non-isomorphic genus-3 curves admit a "
                "faithful S_4 action, so 'S_4 survives the pinch' has essentially "
                "no selecting power for the Klein quartic."
            ),
            "moduli_argument": (
                "Distinct L give non-proportional defining forms. For fixed mu, "
                "{L : C_L iso C_mu} is finite because Aut(C_mu) is finite (genus "
                ">= 2) and N_{PGL_3}(S_4) is finite (its centralizer is trivial by "
                "the scalar commutant in C4, so it embeds in Aut(S_4)). Finite "
                "fibres over a P^1 meet infinitely many isomorphism classes. "
                "NOTE: only finiteness of Aut is used -- the sharp Hurwitz bound "
                "is deliberately avoided, an earlier step of this arc having been "
                "withdrawn for misusing it."
            ),
            "consequence_for_siblings": {
                "qou-8p1b": (
                    "insufficient as written -- separating Klein from Fermat does "
                    "not single out Klein from an infinite family; re-scope to an "
                    "invariant the pinch itself determines"
                ),
                "qou-8p1c": (
                    "not the bottleneck -- period matrices of two hand-picked "
                    "curves cannot close an argument whose datum is this weak"
                ),
            },
            "not_verified_here": [
                "the value of L at which the Klein quartic sits in this pencil "
                "(needs arithmetic over Q(sqrt(-7)))",
                "hyperelliptic genus-3 curves admitting S_4, which lie outside "
                "the pencil and only enlarge the competitor set",
            ],
            "scope": (
                "scope-(a). Refutes the S_4 bridge AS AN ARGUMENT for the "
                "Bring->Klein degeneration. Does NOT refute the degeneration "
                "itself, which remains open."
            ),
            "all_checks_pass": all_ok,
            "checks": checks,
        },
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        payload, script_path=__file__, engine=None, q0_anchor=False)
    _OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {_OUT.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
