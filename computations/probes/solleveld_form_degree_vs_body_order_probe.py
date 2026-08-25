#!/usr/bin/env python3
"""Does Solleveld's de Rham degree run the same way as the corpus's body order?

Solleveld (arXiv:1108.5286v3 §3.1, bib `solleveld2022`) computes, for the affine
Hecke algebra,

    HH_*(H (x) Gamma)  ~=  (+)_{w in <W'>}  Omega^*(t_{rho_w})^{G_{rho_w}}

i.e. algebraic differential forms of every degree, summed over CONJUGACY CLASSES
of the (extended) Weyl group.  `qou-siin` asks whether that extra de Rham degree
is a home for the body-order series of `conj:binding-manybody-eq-jet-filtration`,

    B(K) = sum_{n>=2} m_e * a_D^(n)(K),

which `prop:jet-filtration-binding-extensive` proves extensive in the body-order
cutoff.  A grading over a partition index is a shape match; this probe asks
whether the DEPTH of that grading moves the right way.

MEASURED HERE: dim t_w = dim( t / (w-1) t ) on the reflection representation of
S_n, per conjugacy class, exactly.  That dimension is the top form degree the
summand at w can carry.

NO FLOAT (AGENTS.md, probes are not exempt): every entry is an int or a
Fraction; the rank is computed by exact Gaussian elimination over Q.  Nothing
here is approximated, so nothing here is reported "to N digits".

PART 2 (added 2026-08-25) tests the surviving route.  The within-class reading
dies on direction; the ACROSS-class reading -- a sum over classes at fixed
degree rather than a degree within one class -- is untouched by that, so it gets
its own test against the one invariant it must satisfy.

Emits no witness: it establishes a combinatorial identity, a direction, and a
growth rate -- not a number any consumer reads.
"""
from math import comb
from itertools import permutations
from fractions import Fraction


def rank_exact(rows, ncols):
    """Rank over Q by Gaussian elimination on Fractions.  No float anywhere."""
    M = [[Fraction(x) for x in r] for r in rows]
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M):
            break
    return r


def cycle_type(p):
    n = len(p)
    seen = [False] * n
    ct = []
    for i in range(n):
        if not seen[i]:
            length, j = 0, i
            while not seen[j]:
                seen[j] = True
                j = p[j]
                length += 1
            ct.append(length)
    return tuple(sorted(ct, reverse=True))


def dim_t_w(p):
    """dim t/(w-1)t on the reflection rep = (perm rep coker) - 1."""
    n = len(p)
    Wm1 = [[(1 if p[j] == i else 0) - (1 if i == j else 0) for j in range(n)]
           for i in range(n)]
    return (n - rank_exact(Wm1, n)) - 1


def main() -> int:
    print(f"{'n':>2} {'cycle type':<20} {'#cycles':>7} {'dim t_w':>8} {'top Omega deg':>14}")
    ok = True
    for n in range(2, 8):
        seen = set()
        for p in permutations(range(n)):
            ct = cycle_type(p)
            if ct in seen:
                continue
            seen.add(ct)
            d = dim_t_w(p)
            ok &= (d == len(ct) - 1)
            print(f"{n:>2} {str(ct):<20} {len(ct):>7} {d:>8} {d:>14}")

    print()
    print("IDENTITY (exact, n = 2..7, every conjugacy class):"
          "  dim t_w = #cycles(w) - 1  ->", "HOLDS" if ok else "FAILS")
    print()
    print("DIRECTION.  The top form degree available at class w is #cycles(w)-1,")
    print("so the grading is DEEPEST on the identity class (n cycles, degree n-1)")
    print("and COLLAPSES to a scalar on an n-cycle (1 cycle, degree 0).")
    print()
    print("Under the natural reading of binding -- an n-body bound cluster merges")
    print("n strands into ONE closure component, i.e. one longer cycle -- more")
    print("binding means FEWER cycles, hence a LOWER top degree.  The body-order")
    print("series needs depth that GROWS with cluster size.  It shrinks.")
    print()
    print("SCOPE-(a), not (b).  This refutes the de Rham degree as the body-order")
    print("index UNDER THAT READING of body order as cycle merging.  It does not")
    print("prove no map exists: a different assignment of body order to cycle")
    print("data, or a sum over classes rather than a degree within one, is")
    print("untouched.  No proved invariant forbids those, so no (b) claim is made.")
    print()
    print("SEPARATELY -- an index-set caution that is NOT an obstruction.")
    print("Solleveld sums over CONJUGACY CLASSES; the corpus's Wedderburn form")
    print("tr_M = sum_lambda y_lambda chi_lambda sums over IRREPS.  For S_n both")
    print("are partitions of n, but they are different roles, paired by the")
    print("character table -- and the corpus's Frobenius pairing already carries")
    print("both indexings, chi_lambda evaluated at the class of rho(beta).  So the")
    print("two index sets meet where the corpus already works; do not read the")
    print("shared word 'partition' as an identification.")
    print()
    across_class()
    return 0


def partitions_by_partcount(n):
    """dict: #parts -> number of partitions of n with that many parts."""
    out = {}

    def rec(rem, mx, k):
        if rem == 0:
            out[k] = out.get(k, 0) + 1
            return
        for p in range(min(rem, mx), 0, -1):
            rec(rem - p, p, k + 1)

    rec(n, n, 0)
    return out


def across_class():
    """PART 2 -- the surviving route: sum ACROSS classes at fixed degree.

    rank HH_j = sum_{lam |- n} C(#parts(lam) - 1, j),  since dim t_w = c(w) - 1
    and Omega^j of a d-dimensional space is free of rank C(d, j).
    """
    print("=" * 68)
    print("PART 2 -- the ACROSS-class route (the one PART 1 leaves open)")
    print("=" * 68)
    print()
    print("  rank HH_j  =  sum_{lam |- n} C(#parts(lam) - 1, j)")
    print()
    print(f"{'n':>3} {'#classes':>9} {'top deg':>8}  {'rank at j = 0..5':<40}")
    for n in range(2, 16):
        pc = partitions_by_partcount(n)
        R = [sum(c * comb(k - 1, j) for k, c in pc.items()) for j in range(6)]
        print(f"{n:>3} {sum(pc.values()):>9} {max(pc)-1:>8}  {str(R):<40}")

    print()
    print("OBSERVATION 1 -- the degree-0 piece reduces to the corpus's centre.")
    print("rank HH_0 = #classes = p(n), and the corpus's Wedderburn centre is")
    print("indexed by irreps, also p(n).  So the affine object RESTRICTS in degree")
    print("0 to exactly the per-lambda form the corpus already uses, and adds")
    print("degrees 1..n-1 on top.  That is the 'graded home' shape wanted.")
    print("CAUTION: p(n) counts classes and irreps BY DEFINITION, so this is a")
    print("count agreement, not a structural identification.  It shows the")
    print("reduction is dimensionally consistent; it proves nothing more.")
    print()
    print("OBSERVATION 2 -- the route PASSES the invariant that killed PART 1.")
    print("prop:jet-filtration-binding-extensive needs the number of available")
    print("graded pieces to GROW with the body-order cutoff A.  The atom word")
    print("sits in H_{3A}(q), so n = 3A and the top degree is 3A - 1:")
    print()
    print(f"{'A':>3} {'n = 3A':>7} {'top degree':>11} {'body orders needed':>19}")
    for A in range(1, 9):
        print(f"{A:>3} {3*A:>7} {3*A-1:>11} {max(0, A-1):>19}")
    print()
    print("3A - 1 >= A - 1 for every A, and both grow linearly.  So the across-")
    print("class grading has room for the body-order series where the within-")
    print("class degree did not.  ROOM IS NOT A MAP: no assignment of body order")
    print("to degree is exhibited here, and finding one is the open work.")
    print()
    print("OBSERVATION 3 -- the real blocker is structural, not numerical.")
    print("Solleveld's theorem is about the AFFINE Hecke algebra.  The corpus's")
    print("atom word lives in the FINITE H_{3A}(q), which is semisimple at")
    print("generic q -- so for it the whole grading COLLAPSES to degree 0 and")
    print("none of the above exists.  Using any of this requires the inductive")
    print("limit, and markov-trace-inductive-limit.lean says of exactly that:")
    print("  \"The full operator-theoretic construction (von Neumann inductive")
    print("   limit on the infinite-dim affine Hecke algebra) is the open R&D")
    print("   content.\"")
    print("So the route survives every test applied here and then waits on a")
    print("bridge the corpus has already marked open.  That is where it stands.")


if __name__ == "__main__":
    raise SystemExit(main())
