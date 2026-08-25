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

Emits no witness: it establishes a combinatorial identity and a direction, not a
number any consumer reads.
"""
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
