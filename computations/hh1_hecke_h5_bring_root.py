#!/usr/bin/env python3
"""PROBE A (Bring case) — dim HH^1(H_5(q)) at the Bring root of unity.

Follow-on to `hh1_hecke_outer_derivations.py`, whose own closing note says:
"the Bring-specific residue is the H_5 computation (PROBE A, next step)."
Bean `qou-jcmw`. Motivated by
`docs/audits/2026-08-08-qbeta-l2-assessment-post-week-landings.md` §5: the
surviving c_3 carrier is fibre-level and cyclotomic, and the HH^1/cocenter
modules that landed 2026-08-07 sit at the same address. This script runs the
falsifiable prune that audit names.

WHAT IS COMPUTED
    dim HH^1(A) = dim Der(A) - dim Inn(A),  A = H_n(q) balanced Iwahori-Hecke,
    relations  T_i^2 = a T_i + 1  (a = q - q^{-1}),  braid, commuting.
    Der  = { D : D(T_i) free, subject to D(relation) = 0 }   [(n-1)*n! unknowns]
    Inn  = n! - dim Z(A),   Z(A) = { z : T_i z = z T_i for all i }.

WHY THE ANSWER IS RIGOROUS EVEN THOUGH THE ARITHMETIC IS MODULAR
    Every matrix entry lies in Z[zeta] (a is a difference of roots of unity), and
    reduction Z[zeta] -> F_p along a prime above p is a ring homomorphism, so
    every minor reduces and  rank_p <= rank_0.  Hence
        dim Der_p >= dim Der_0,   dim Z_p >= dim Z_0  =>  dim Inn_p <= dim Inn_0,
    and therefore
        dim HH^1_p  >=  dim HH^1_0.
    The modular computation is an UPPER BOUND on the true characteristic-0
    dimension. In particular  HH^1_p = 0  PROVES  HH^1_0 = 0 -- the prune
    direction is exact, not probabilistic. A nonzero modular value is only an
    upper bound (agreement across several unrelated primes is evidence, not
    proof, that it is attained).

SEMISIMPLICITY BOOKKEEPING
    Balanced H_n(q) is semisimple iff [k]_q != 0 for k = 2..n, and
    [k]_q = 0  <=>  q^{2k} = 1  (given q^2 != 1). At a primitive 5th root the
    only vanishing bracket for n = 5 is [5]_q -- exactly the Bring point.

No fit, no free parameter, nothing wired to production: this is a dimension
count. Exact integer/modular arithmetic throughout, so the `_precision.py`
mpmath dps discipline does not apply (there is no floating point in this file).
"""
import json
import os
import sys
from itertools import permutations

import numpy as np

# --------------------------------------------------------------------------
# Symmetric group plumbing
# --------------------------------------------------------------------------


def length(w):
    """Coxeter length = number of inversions."""
    n = len(w)
    return sum(1 for i in range(n) for j in range(i + 1, n) if w[i] > w[j])


def s_gen(n, i):
    """Adjacent transposition s_i swapping i, i+1 (0-indexed)."""
    p = list(range(n))
    p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def left_mult(w, i):
    """s_i . w  as a permutation (compose: j -> s_i(w(j)))."""
    return tuple(j + 1 if j == i else (j - 1 if j == i + 1 else j) for j in w)


def right_mult(w, i):
    """w . s_i  as a permutation (swap positions i, i+1)."""
    v = list(w)
    v[i], v[i + 1] = v[i + 1], v[i]
    return tuple(v)


# --------------------------------------------------------------------------
# Modular linear algebra
# --------------------------------------------------------------------------


def rank_mod(M, p):
    """Rank of an integer matrix over F_p by Gaussian elimination."""
    A = np.array(M, dtype=np.int64) % p
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c]:
                piv = i
                break
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        nz = np.nonzero(A[r + 1:, c])[0]
        if nz.size:
            idx = nz + r + 1
            A[idx] = (A[idx] - np.outer(A[idx, c], A[r])) % p
        r += 1
        if r == rows:
            break
    return r


def find_prime_and_root(order, lo):
    """Smallest prime p > lo with p = 1 (mod order), plus a primitive
    `order`-th root of unity in F_p."""

    def is_prime(m):
        if m < 2:
            return False
        for d in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if m % d == 0:
                return m == d
        d, s = m - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            x = pow(a, d, m)
            if x in (1, m - 1):
                continue
            for _ in range(s - 1):
                x = x * x % m
                if x == m - 1:
                    break
            else:
                return False
        return True

    p = lo + (order - (lo % order)) + 1
    while True:
        if p % order == 1 and is_prime(p):
            for g in range(2, 200):
                z = pow(g, (p - 1) // order, p)
                if z != 1 and pow(z, order, p) == 1:
                    # ensure primitive: z^(order/l) != 1 for prime l | order
                    prim = True
                    for l in {2, 3, 5, 7}:
                        if order % l == 0 and pow(z, order // l, p) == 1:
                            prim = False
                            break
                    if prim:
                        return p, z
        p += order


# --------------------------------------------------------------------------
# Hecke algebra regular representation
# --------------------------------------------------------------------------


def hecke_matrices(n, a, p):
    """Left/right multiplication matrices for the generators T_i of H_n,
    in the basis {T_w : w in S_n}, over F_p with Hecke parameter a."""
    basis = sorted(permutations(range(n)), key=lambda w: (length(w), w))
    index = {w: k for k, w in enumerate(basis)}
    N = len(basis)

    L = [np.zeros((N, N), dtype=np.int64) for _ in range(n - 1)]
    R = [np.zeros((N, N), dtype=np.int64) for _ in range(n - 1)]
    for i in range(n - 1):
        for w in basis:
            c = index[w]
            # T_{s_i} * T_w
            u = left_mult(w, i)
            if length(u) > length(w):
                L[i][index[u], c] = 1
            else:
                L[i][index[u], c] = 1
                L[i][c, c] = (L[i][c, c] + a) % p
            # T_w * T_{s_i}
            v = right_mult(w, i)
            if length(v) > length(w):
                R[i][index[v], c] = 1
            else:
                R[i][index[v], c] = 1
                R[i][c, c] = (R[i][c, c] + a) % p
    return basis, index, [m % p for m in L], [m % p for m in R]


def hh1_dim(n, a, p, verbose=False):
    """dim Der, dim Z, dim Inn, dim HH^1 for H_n at parameter a over F_p."""
    basis, index, L, R = hecke_matrices(n, a, p)
    N = len(basis)
    g = n - 1
    I = np.eye(N, dtype=np.int64)

    # ---- centre: z with (L_i - R_i) z = 0
    Zsys = np.vstack([(L[i] - R[i]) % p for i in range(g)])
    dimZ = N - rank_mod(Zsys, p)
    dimInn = N - dimZ

    # ---- derivations: unknowns D_i = D(T_i) in F_p^N, i = 0..g-1
    blocks = []

    def row_block(assign):
        """assign: dict i -> N x N coefficient matrix acting on D_i."""
        row = np.zeros((N, g * N), dtype=np.int64)
        for i, M in assign.items():
            row[:, i * N:(i + 1) * N] = M % p
        return row

    # quadratic  T_i^2 = a T_i + 1  =>  (L_i + R_i - a I) D_i = 0
    for i in range(g):
        blocks.append(row_block({i: (L[i] + R[i] - a * I) % p}))

    # braid  T_i T_j T_i = T_j T_i T_j   (j = i+1)
    for i in range(g - 1):
        j = i + 1
        coef_i = (R[i] @ R[j] + L[i] @ L[j] - L[j] @ R[j]) % p
        coef_j = (L[i] @ R[i] - R[j] @ R[i] - L[j] @ L[i]) % p
        blocks.append(row_block({i: coef_i, j: coef_j}))

    # commuting  T_i T_j = T_j T_i   (|i-j| >= 2)
    for i in range(g):
        for j in range(i + 2, g):
            blocks.append(row_block({i: (R[j] - L[j]) % p,
                                     j: (L[i] - R[i]) % p}))

    Dsys = np.vstack(blocks) % p
    dimDer = g * N - rank_mod(Dsys, p)
    if verbose:
        print(f"      [system {Dsys.shape[0]}x{Dsys.shape[1]}]", file=sys.stderr)
    return dimDer, dimZ, dimInn, dimDer - dimInn


def brackets_vanishing(n, q, p):
    """Which [k]_q vanish for k = 2..n, i.e. q^{2k} = 1."""
    return [k for k in range(2, n + 1) if pow(q, 2 * k, p) == 1]


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    results = {}
    print("dim HH^1(H_n(q)) = dim Der - dim Inn   (modular; upper bound on char 0)\n")

    # Two unrelated primes for cross-checking the nonzero values.
    primes = [find_prime_and_root(20, 5000)[0], find_prime_and_root(20, 60000)[0]]

    for p in primes:
        # zeta_20 gives us zeta_5 = z20^4 and zeta_10 = z20^2 in the same field.
        _, z20 = find_prime_and_root(20, p - 1)
        _, z20 = (p, pow(next(g for g in range(2, 500)
                              if pow(g, (p - 1) // 20, p) != 1
                              and all(pow(pow(g, (p - 1) // 20, p), 20 // l, p) != 1
                                      for l in (2, 5))),
                         (p - 1) // 20, p))
        z5 = pow(z20, 4, p)
        z10 = pow(z20, 2, p)
        assert pow(z5, 5, p) == 1 and z5 != 1
        assert pow(z10, 10, p) == 1 and pow(z10, 5, p) != 1

        print(f"--- F_{p} ---")
        points = [
            ("q = zeta_5   (Bring, [5]_q=0)", z5),
            ("q = zeta_10  ([5]_q=0)", z10),
            ("q = 3        (generic)", 3 % p),
        ]
        for label, qv in points:
            a = (qv - pow(qv, p - 2, p)) % p
            vanish = brackets_vanishing(5, qv, p)
            der, dz, inn, hh1 = hh1_dim(5, a, p)
            ss = "non-semisimple" if vanish else "semisimple"
            vstr = str(vanish) if vanish else "none"
            print(f"  H_5  {label:32s} [k]=0 for k={vstr:<8} {ss:15s}"
                  f" dim Der={der:3d} dim Z={dz:2d} dim Inn={inn:3d}"
                  f"  dim HH^1 = {hh1}")
            results.setdefault(label, {})[str(p)] = {
                "dim_Der": int(der), "dim_Z": int(dz),
                "dim_Inn": int(inn), "dim_HH1": int(hh1),
                "vanishing_brackets": vanish,
            }
        print()

    # n=3 regression against the merged hand-coded producer (expects 0/1/1/0).
    print("--- regression vs hh1_hecke_outer_derivations.py (n=3) ---")
    p3, _ = find_prime_and_root(12, 5000)
    g12 = next(g for g in range(2, 500)
               if pow(g, (p3 - 1) // 12, p3) != 1
               and all(pow(pow(g, (p3 - 1) // 12, p3), 12 // l, p3) != 1
                       for l in (2, 3)))
    z12 = pow(g12, (p3 - 1) // 12, p3)
    z4, z6 = pow(z12, 3, p3), pow(z12, 2, p3)
    n3 = {}
    for label, qv in [("generic q=3", 3 % p3), ("q=i  ([2]_q=0)", z4),
                      ("q=zeta_6 ([3]_q=0)", z6)]:
        a = (qv - pow(qv, p3 - 2, p3)) % p3
        der, dz, inn, hh1 = hh1_dim(3, a, p3)
        print(f"  H_3  {label:22s} dim Der={der} dim Z={dz} dim Inn={inn}"
              f"  dim HH^1 = {hh1}")
        n3[label] = {"dim_Der": int(der), "dim_Z": int(dz),
                     "dim_Inn": int(inn), "dim_HH1": int(hh1)}

    bring = results["q = zeta_5   (Bring, [5]_q=0)"]
    hh1_vals = {v["dim_HH1"] for v in bring.values()}
    verdict_zero = hh1_vals == {0}

    print("\n" + "=" * 72)
    if verdict_zero:
        print("VERDICT: dim HH^1(H_5(zeta_5)) = 0 over every prime tested.")
        print("Because modular rank can only DROP, 0 is an upper bound on the")
        print("characteristic-0 dimension => dim HH^1(H_5(zeta_5)) = 0 EXACTLY.")
        print("There is NO outer derivation at the Bring root of unity, so the")
        print("HH^1 -> HH_0 route to the c_3 carrier has no source class.")
        print("The bar-parity test (part 2 of bean qou-jcmw) is MOOT: an empty")
        print("space has no class whose parity could be tested.")
    else:
        print(f"VERDICT: dim HH^1(H_5(zeta_5)) <= {sorted(hh1_vals)} (modular upper bound).")
        print("Nonzero => the route survives this prune; part 2 of qou-jcmw")
        print("(bar-parity of the outer class acting on the cocenter) is now the")
        print("gate, and the char-0 value needs an exact Q(zeta_5) confirmation.")
    print("=" * 72)

    witness = {
        "schema": "qou-probe/v1",
        "probe": "PROBE-A (Bring case): dim HH^1(H_5(q)) at the 5th root of unity",
        "bean": "qou-jcmw",
        "description": (
            "dim HH^1(H_5(q)) = dim Der - dim Inn at q = zeta_5 and zeta_10 "
            "(both [5]_q = 0, the n=5 non-semisimple locus), with a generic-q "
            "control and an n=3 regression against the merged hand-coded "
            "producer. Tests whether the fibre-level cyclotomic c_3 carrier has "
            "an outer-derivation source class."),
        "method": (
            "Regular representation of balanced H_n(q) (T_i^2 = a T_i + 1, "
            "a = q - q^{-1}) built programmatically on the basis {T_w}; Der = "
            "nullspace of the Leibniz constraints imposed on D(T_i) by the "
            "quadratic, braid and commuting relations; Inn = n! - dim Z(A). "
            "Exact modular linear algebra over F_p with p = 1 mod 20."),
        "rigour_note": (
            "All entries lie in Z[zeta]; reduction mod a prime above p is a ring "
            "homomorphism so rank_p <= rank_0, hence dim HH^1_p >= dim HH^1_0. "
            "A modular value of 0 therefore PROVES the characteristic-0 value is "
            "0. A nonzero modular value is only an upper bound."),
        "primes": primes,
        "results_H5": results,
        "regression_H3": n3,
        "verdict": (
            "scope-(b) structural exclusion, invariant cited = vanishing of "
            "HH^1(H_5(zeta_5)): no outer derivation exists at the Bring root, so "
            "the HH^1-class route to the c_3 carrier has no source object. "
            "Bar-parity sub-test moot."
            if verdict_zero else
            "route survives: outer class exists at the Bring root; bar-parity "
            "test is the next gate."),
        "wired_to_production": False,
        "fit_performed": False,
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "hh1-hecke-h5-bring-root.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
