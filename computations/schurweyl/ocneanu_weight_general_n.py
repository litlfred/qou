"""DERIVE the Ocneanu/Markov weight family at general n, then validate it.

Context.  `ocneanu_weight_validation.py` showed the corpus's `jones_wenzl_weight`
(computations/mass_at_3A_proper.py) never reproduces the Lean-PROVED n = 3 weights
`QOU.SchurWeyl.HeckeMarkov3.markovWeight0/1/2`, across 160 convention combinations.
So the general-n formula is not available by recall.  This script derives it.

THE RESULT
----------

    W_lam(q, z) = prod_{(i,j) in lam} [ q^{2i} (q^2 - 1 - q z) + q^{2j+1} z ]
                  / prod_{(i,j) in lam} [ q^{2 h(i,j)} - 1 ]                 (*)

a product over the cells of lam: numerator affine in z with a per-cell framing
monomial, denominator the q^2-hook product.  Equivalently, pulling the row index
out of the numerator,

    W_lam = q^{2 n(lam)} * prod_x [ (q^2 - 1) + z q (q^{2 c(x)} - 1) ]
                         / prod_x [ q^{2 h(x)} - 1 ],     n(lam) = sum_i i * lam_i,

which is the form in which the derivation below reads it off.

HOW IT WAS OBTAINED (no recall, no fit to an uncheckable target)
---------------------------------------------------------------

  1.  Solve n = 2 from the DEFINING conditions in exact Q(q,z):
        tr(1) = 1                ->  sum_lam d_lam W_lam = 1
        tr(sigma_1) = z          ->  sum_lam W_lam chi^lam(sigma_1) = z
      chi^lam(sigma_1) is exact with no matrix assembly: 1 and 2 sit at axial
      distance +-1, so sigma_1 is DIAGONAL in the seminormal basis with entries
      q (same row) / -q^-1 (same column).  Same convention as the proved n = 3
      weights, (sigma - q)(sigma + q^-1) = 0.

  2.  Read n = 1, 2, 3 as  W_lam = N_lam / prod_x [h(x)]_{q^2}  (denominator
      already confirmed in ocneanu_weight_validation.py) and observe that N_lam
      factors over CELLS through a single content function g(c).  g(0), g(+-1)
      come from n <= 2 and g(+-2) from n = 3; the mixed shape (2,1) introduces no
      new content and is therefore a CONSISTENCY CHECK, not an input.  It passes.

  3.  g is affine in q^{2c}, giving (*) up to a monomial.  The monomial is NOT
      determined by n <= 3 -- every partition of n <= 3 has distinct contents, and
      the first repeat is the two content-0 cells of (2,2).  So:

  4.  Solve n = 4, 5, 6 from scratch (branching down to the previous level, plus
      the Markov relation tr_n(x sigma_{n-1}) = z tr_{n-1}(x) for x drawn from the
      q-Jucys-Murphy elements L_k, which are DIAGONAL in the seminormal basis with
      eigenvalue q^{2 c_T(k)} -- Ram (1997) Thm 4.1, formalized sorry-free as
      QOU.SchurWeyl.seminormalRep_qJM_diag).  Because the L-part is diagonal, the
      trace of L * sigma needs only the diagonal seminormal entry of sigma, so this
      stays a scalar computation.  Comparing against step 3 pins the monomial to
      q^{2 n(lam)} -- the correction is q^2 on exactly (2,2), (3,2), (2,2,1), the
      shapes containing the cell (1,1).

VALIDATION (step 5) is against four conditions, three of them out of sample:
    T1  reproduces the Lean-PROVED n = 3 weights            (input at n <= 3)
    T2  sum_lam d_lam W_lam = 1                             (input at n <= 2)
    T3  branching  W_mu^(n) = sum_{lam = mu+box} W_lam^(n+1) (input only n<=5 solve)
    T4  sum_lam W_lam chi^lam(sigma_1) = z                  (input at n <= 2)

EXACT ARITHMETIC ONLY -- sympy over Q(q, z).  No float anywhere (AGENTS.md
NO-FLOAT64; probes are not exempt).
"""

import sys
import sympy as sp

q, z = sp.symbols('q z')


# ---------------------------------------------------------------- combinatorics
def partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    cap = n if cap is None else min(cap, n)
    for first in range(cap, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def cells(s):
    return [(i, j) for i, r in enumerate(s) for j in range(r)]


def hooks(s):
    rows = list(s)
    mc = rows[0] if rows else 0
    cols = [sum(1 for r in rows if r > j) for j in range(mc)]
    return {(i, j): (rows[i] - j - 1) + (cols[j] - i - 1) + 1 for (i, j) in cells(s)}


def dim(s):
    """f^lambda by the hook-length formula -- exact integer."""
    d = sp.factorial(sum(s))
    for h in hooks(s).values():
        d /= h
    return sp.Integer(d)


def syts(s):
    cs = cells(s)
    n = len(cs)
    out = []

    def rec(filled, k):
        if k > n:
            out.append(dict(filled))
            return
        for (i, j) in cs:
            if (i, j) in filled:
                continue
            if i > 0 and (i - 1, j) not in filled:
                continue
            if j > 0 and (i, j - 1) not in filled:
                continue
            filled[(i, j)] = k
            rec(filled, k + 1)
            del filled[(i, j)]

    rec({}, 1)
    return out


def removable(s):
    out = []
    for i in range(len(s)):
        if i + 1 == len(s) or s[i] > s[i + 1]:
            t = list(s)
            t[i] -= 1
            out.append(tuple(x for x in t if x > 0))
    return out


def seminormal_param(d):
    """`QOU.SchurWeyl.Seminormal.seminormalParam q d = (q - q^-1)/(1 - q^{-2d})`.
    This is the DIAGONAL entry of sigma_i on the seminormal vector of a tableau
    whose entries i, i+1 sit at axial distance d.  a(1) = q, a(-1) = -q^-1."""
    return (q - 1 / q) / (1 - q**(-2 * d))


def content_fn(T):
    inv = {v: k for k, v in T.items()}
    return lambda k: inv[k][1] - inv[k][0]


def chi(s, jm=(), sig=None):
    """chi^lam( (prod_{k in jm} L_k) * sigma_sig ), exact.

    L_k is the q-Jucys-Murphy element: diagonal in the seminormal basis with
    eigenvalue q^{2 c_T(k)}.  With the L-part diagonal, the trace of the product
    picks up only the diagonal entry of sigma_sig, so no matrix assembly is needed.
    With jm = () and sig = 1 this is the exact chi^lam(sigma_1) (|axial dist| = 1
    for the pair 1,2, so sigma_1 is itself diagonal)."""
    tot = 0
    for T in syts(s):
        c = content_fn(T)
        t = sp.Integer(1)
        for k in jm:
            t *= q**(2 * c(k))
        if sig is not None:
            t *= seminormal_param(c(sig + 1) - c(sig))
        tot += t
    return sp.cancel(sp.together(tot))


# ------------------------------------------------- the PROVED n = 3 weights
den2 = q**2 + 1
den3 = q**4 + q**2 + 1
PROVED3 = {
    (3,): (q * z + 1) * (q**3 * z + q * z + 1) / (den2 * den3),
    (2, 1): -q * (z - q) * (q * z + 1) / den3,
    (1, 1, 1): q**2 * (z - q) * (z * (q**2 + 1) - q**3) / (den2 * den3),
}
PROVED3 = {k: sp.cancel(sp.together(v)) for k, v in PROVED3.items()}


# ------------------------------------------------------- steps 1, 2, 3
def derive():
    print("=" * 74)
    print("STEP 1 -- solve n = 1, 2 from the defining conditions in exact Q(q,z)")
    print("=" * 74)
    solved = {(1,): sp.Integer(1)}
    print("  n=1: W_(1) = 1                                     [tr(1) = 1]")
    p2 = list(partitions(2))
    ws = sp.symbols('w0 w1')
    sol = sp.solve([sp.Eq(sum(dim(s) * w for s, w in zip(p2, ws)), 1),
                    sp.Eq(sum(w * chi(s, sig=1) for s, w in zip(p2, ws)), z)],
                   ws, dict=True)[0]
    for s, w in zip(p2, ws):
        solved[s] = sp.cancel(sp.together(sol[w]))
        print(f"  n=2: W_{s} = {solved[s]}")
    solved.update(PROVED3)

    print()
    print("=" * 74)
    print("STEP 2 -- N_lam = W_lam * prod_x [h(x)]_{q^2} factors over cells")
    print("=" * 74)

    def hook_den(s):
        d = sp.Integer(1)
        for h in hooks(s).values():
            d *= sum(q**(2 * k) for k in range(h))
        return sp.expand(d)

    g = {}
    for s in [(1,), (2,), (1, 1), (3,), (1, 1, 1)]:
        N = sp.cancel(solved[s] * hook_den(s))
        known, unk = sp.Integer(1), None
        for (i, j) in cells(s):
            c = j - i
            if c in g:
                known *= g[c]
            else:
                assert unk is None
                unk = c
        g[unk] = sp.factor(sp.cancel(N / known))
        print(f"  from {str(s):11s} -> g({unk:+d}) = {g[unk]}")

    N21 = sp.cancel(solved[(2, 1)] * hook_den((2, 1)))
    pred = sp.Integer(1)
    for (i, j) in cells((2, 1)):
        pred *= g[j - i]
    print("  CONSISTENCY (2,1) introduces no new content, prod g(c) reproduces N"
          f"  -> {sp.simplify(sp.expand(N21 - pred)) == 0}")

    print()
    print("=" * 74)
    print("STEP 3 -- g(c) is affine in q^{2c}")
    print("=" * 74)
    for c in sorted(g):
        rhs = sp.cancel(((q**2 - 1) + z * q * (q**(2 * c) - 1)) / (q**2 - 1)
                        * (q**(-2 * c) if c < 0 else 1))
        print(f"  g({c:+d}) = {str(sp.factor(g[c])):28s}  affine form matches: "
              f"{sp.simplify(sp.cancel(g[c] - rhs)) == 0}")
    print()
    print("  With (q^2-1)^n prod_x [h(x)]_{q^2} = prod_x (q^{2h(x)} - 1), this gives")
    print("  W_lam up to a MONOMIAL in q.  Every partition of n <= 3 has distinct")
    print("  cell contents, so n <= 3 cannot pin that monomial -- step 4 does.")
    return solved


# ------------------------------------------------------- step 4: solve upward
def solve_next(prev, n):
    """Solve W^(n) from W^(n-1): branching + Markov  tr_n(x sigma_{n-1}) = z tr_{n-1}(x)
    for x in {1, L_2, ..., L_{n-1}, L_2...L_{n-1}}."""
    ps = list(partitions(n))
    V = sp.symbols(f'V0:{len(ps)}')
    wm = dict(zip(ps, V))
    eqs = []
    for mu in partitions(n - 1):
        eqs.append(sp.Eq(sp.cancel(sum(wm[l] for l in ps if mu in removable(l))
                                   - prev[mu]), 0))
    for x in [()] + [(k,) for k in range(2, n)] + [tuple(range(2, n))]:
        lhs = sum(wm[s] * chi(s, x, n - 1) for s in ps)
        rhs = z * sum(prev[m] * chi(m, x) for m in partitions(n - 1))
        eqs.append(sp.Eq(sp.cancel(sp.together(lhs - rhs)), 0))
    sol = sp.solve(eqs, V, dict=True)
    assert len(sol) == 1, f"n={n}: {len(sol)} solutions"
    missing = [v for v in V if v not in sol[0]]
    assert not missing, f"n={n}: underdetermined, free = {missing}"
    return {s: sp.cancel(sp.factor(sp.together(sol[0][wm[s]]))) for s in ps}


# ------------------------------------------------------- the closed form (*)
def W(s):
    num = sp.Integer(1)
    for (i, j) in cells(s):
        num *= q**(2 * i) * (q**2 - 1 - q * z) + q**(2 * j + 1) * z
    den = sp.Integer(1)
    for h in hooks(s).values():
        den *= q**(2 * h) - 1
    return sp.cancel(sp.together(num / den))


def main():
    NSOLVE = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else NSOLVE + 1
    derive()

    print()
    print("=" * 74)
    print(f"STEP 4 -- solve n = 4..{NSOLVE} from scratch; compare against (*)")
    print("=" * 74)
    true = {3: PROVED3}
    for n in range(4, NSOLVE + 1):
        true[n] = solve_next(true[n - 1], n)
        for s in partitions(n):
            r = sp.cancel(sp.factor(true[n][s] / W(s)))
            flag = "" if r == 1 else f"   <-- (*) off by {r}"
            print(f"  n={n} {str(s):16s} solved/closed-form = {r}{flag}")
    print()
    print("  The row-index monomial q^{2i} inside the numerator of (*) is exactly")
    print("  what makes every ratio 1: it contributes q^{2 n(lam)} overall, and")
    print("  n(lam) differs from the naive below-diagonal content sum precisely on")
    print("  the shapes with a second diagonal cell -- (2,2), (3,2), (2,2,1).")

    print()
    print("=" * 74)
    print(f"STEP 5 -- validate (*) at n = 1..{NMAX}")
    print("=" * 74)
    fails = []

    print("\nT1  reproduces the Lean-PROVED n = 3 weights (markovWeight0/1/2)")
    for s, v in PROVED3.items():
        ok = sp.simplify(sp.cancel(W(s) - v)) == 0
        print(f"    W_{str(s):10s} == proved  -> {ok}")
        if not ok:
            fails.append(f"T1 {s}")

    print("\nT2  sum_lam d_lam W_lam = 1")
    for n in range(1, NMAX + 1):
        ok = sp.simplify(sp.cancel(sp.together(
            sum(dim(s) * W(s) for s in partitions(n)) - 1))) == 0
        print(f"    n={n}: {ok}{'' if n <= 2 else '   <- out of sample'}")
        if not ok:
            fails.append(f"T2 n={n}")

    print("\nT3  branching  W_mu^(n) = sum_{lam = mu + box} W_lam^(n+1)")
    for n in range(1, NMAX):
        bad = [mu for mu in partitions(n)
               if sp.simplify(sp.cancel(sp.together(
                   sum(W(l) for l in partitions(n + 1) if mu in removable(l))
                   - W(mu)))) != 0]
        print(f"    n={n} -> n+1: {'OK' if not bad else 'FAIL ' + str(bad)}"
              f"{'' if n < NSOLVE else '   <- out of sample'}")
        if bad:
            fails.append(f"T3 n={n}")

    print("\nT4  sum_lam W_lam chi^lam(sigma_1) = z")
    for n in range(2, NMAX + 1):
        ok = sp.simplify(sp.cancel(sp.together(
            sum(W(s) * chi(s, sig=1) for s in partitions(n)) - z))) == 0
        print(f"    n={n}: {ok}{'' if n <= 2 else '   <- out of sample'}")
        if not ok:
            fails.append(f"T4 n={n}")

    print()
    print("=" * 74)
    print("VERDICT:", "all tests pass" if not fails else f"FAILURES: {fails}")
    print("=" * 74)
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
