#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Symbolic nuclear characters at k=6 for A=2..7 — all in q, sparse.

Each seminormal matrix σ_g has at most 2 nonzeros per row (the
Hoefsmit block structure: 1×1 diagonal or 2×2 blocks). We store
only nonzero entries as dicts, multiplying via sparse products.

This avoids the O(dim³) dense sympy Matrix multiply and gives
O(dim × nnz) per crossing — critical for dim=16 ([3,2,1]).

Usage:
    cd folio-assistant/computations && python3 symbolic_k6_characters.py
"""

import sympy as sp
from sympy import cancel, factor, Rational
from collections import defaultdict
import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0_num

q = sp.Symbol('q', positive=True)
qi = 1/q
h = q - qi


# ══════════════════════════════════════════════════════════════
# §1  SPARSE SYMBOLIC MATRIX (dict-of-dicts)
# ══════════════════════════════════════════════════════════════

class SparseSym:
    """Sparse symbolic matrix stored as {(i,j): expr}."""
    __slots__ = ('dim', 'data')

    def __init__(self, dim):
        self.dim = dim
        self.data = {}

    def __setitem__(self, key, val):
        i, j = key
        v = cancel(val)
        if v != 0:
            self.data[(i,j)] = v
        elif (i,j) in self.data:
            del self.data[(i,j)]

    def __getitem__(self, key):
        return self.data.get(key, sp.Integer(0))

    @staticmethod
    def eye(dim):
        m = SparseSym(dim)
        for i in range(dim):
            m.data[(i,i)] = sp.Integer(1)
        return m

    def trace(self):
        return sum(self.data.get((i,i), sp.Integer(0)) for i in range(self.dim))

    def __mul__(self, other):
        """Sparse matrix multiply."""
        if isinstance(other, SparseSym):
            result = SparseSym(self.dim)
            # Group self by row, other by col
            self_rows = defaultdict(list)
            for (i,k), v in self.data.items():
                self_rows[i].append((k, v))
            other_cols = defaultdict(list)
            for (k,j), v in other.data.items():
                other_cols[j].append((k, v))

            # For each (i,j): sum over k where both have entries
            accum = defaultdict(lambda: sp.Integer(0))
            for i, row_entries in self_rows.items():
                for k, a_ik in row_entries:
                    # Find all j where other[k,j] ≠ 0
                    for (k2, j), b_kj in other.data.items():
                        if k2 == k:
                            accum[(i,j)] = accum[(i,j)] + a_ik * b_kj

            for key, val in accum.items():
                v = cancel(val)
                if v != 0:
                    result.data[key] = v
            return result
        else:
            # Scalar multiply
            result = SparseSym(self.dim)
            for key, val in self.data.items():
                v = cancel(val * other)
                if v != 0:
                    result.data[key] = v
            return result

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        result = SparseSym(self.dim)
        result.data = dict(self.data)
        for key, val in other.data.items():
            if key in result.data:
                v = cancel(result.data[key] + val)
                if v != 0:
                    result.data[key] = v
                else:
                    del result.data[key]
            else:
                result.data[key] = val
        return result

    def nnz(self):
        return len(self.data)


# ══════════════════════════════════════════════════════════════
# §2  YOUNG TABLEAUX + SEMINORMAL (sparse)
# ══════════════════════════════════════════════════════════════

def partitions_of(n):
    if n == 0: yield (); return
    def g(n, mx):
        if n == 0: yield (); return
        for i in range(min(n,mx), 0, -1):
            for r in g(n-i, i): yield (i,)+r
    yield from g(n, n)

def young_cells(shape):
    cells = []
    for i, ri in enumerate(shape):
        for j in range(ri):
            cells.append((i, j))
    return cells

def young_hooks(shape):
    rows = list(shape)
    max_col = rows[0] if rows else 0
    cols = [sum(1 for r in rows if r > j) for j in range(max_col)]
    hooks = []
    for i in range(len(rows)):
        for j in range(rows[i]):
            hooks.append((rows[i]-j-1) + (cols[j]-i-1) + 1)
    return hooks

def qint(n):
    if n <= 1: return sp.Integer(n)
    return cancel((q**n - q**(-n)) / h)

def qfac(n):
    r = sp.Integer(1)
    for k in range(1, n+1): r *= qint(k)
    return cancel(r)

def dim_q_sym(shape):
    n = sum(shape)
    return cancel(qfac(n) / sp.prod([qint(hk) for hk in young_hooks(shape)]))

def content_sum(shape):
    return sum(j-i for i, ri in enumerate(shape) for j in range(ri))

def conjugate(shape):
    if not shape: return ()
    return tuple(sum(1 for r in shape if r >= c+1) for c in range(shape[0]))

def standard_young_tableaux(shape):
    n = sum(shape)
    cells = young_cells(shape)
    nc = len(cells)
    contents = [c-r for r,c in cells]
    results = []
    def _fill(entry, filled, avail):
        if entry > n:
            results.append(dict(filled)); return
        for ci in range(nc):
            if not avail[ci]: continue
            r, c = cells[ci]
            if c > 0:
                left = next((k for k,(rr,cc) in enumerate(cells) if rr==r and cc==c-1), None)
                if left is not None and avail[left]: continue
            if r > 0:
                above = next((k for k,(rr,cc) in enumerate(cells) if rr==r-1 and cc==c), None)
                if above is not None and avail[above]: continue
            filled[entry] = ci; avail[ci] = False
            _fill(entry+1, filled, avail)
            del filled[entry]; avail[ci] = True
    _fill(1, {}, [True]*nc)
    return results, cells, contents


def build_sparse_seminormal(shape):
    """Build σ₁,...,σ_{n-1} as SparseSym matrices, symbolic in q."""
    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], dim, syts

    sigmas = []
    for k in range(1, n):
        M = SparseSym(dim)
        processed = set()
        for i in range(dim):
            if i in processed: continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k+1]
            rho = contents[ci_k1] - contents[ci_k]
            a = cancel(h / (1 - q**(-2*rho)))

            swap = dict(syts[i])
            swap[k] = ci_k1; swap[k+1] = ci_k
            j = next((jj for jj in range(dim) if jj != i and syts[jj] == swap), None)

            if j is None:
                M[i,i] = a
                processed.add(i)
            else:
                a_prime = cancel(h / (1 - q**(2*rho)))
                b_sq = cancel(a * a_prime + 1)
                b = sp.sqrt(b_sq)
                M[i,i] = a
                M[j,j] = a_prime
                M[i,j] = b
                M[j,i] = b
                processed.add(i); processed.add(j)
        sigmas.append(M)
    return sigmas, dim, syts


# ══════════════════════════════════════════════════════════════
# §3  NUCLEAR CHARACTER (sparse, symbolic)
# ══════════════════════════════════════════════════════════════

def crossing_cd(ti, tj):
    if ti == 1 and tj == 1:   return sp.Integer(1), sp.Integer(0)
    elif ti == 0 and tj == 0: return sp.Integer(1), -h
    else:                     return sp.Integer(1), -h/2

def nuclear_ordering(Z, N):
    ordering = []; pc = nc = 0
    for k in range(Z+N):
        if (k%2==0 and pc<Z) or nc>=N:
            ordering.append(1); pc += 1
        else:
            ordering.append(0); nc += 1
    return ordering

def nuclear_chi_sparse(Z, N, sigmas, dim, n_gens):
    A = Z + N
    if A <= 1 or dim == 0:
        return sp.Integer(dim)
    ordering = nuclear_ordering(Z, N)
    I = SparseSym.eye(dim)
    product = SparseSym.eye(dim)

    for i in range(A-1):
        for j in range(i+1, A):
            c, d = crossing_cd(ordering[i], ordering[j])
            g = (i+j) % n_gens
            M = sigmas[g] * c + I * d
            product = product * M

    return cancel(product.trace())


# ══════════════════════════════════════════════════════════════
# §4  MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    k = 6
    n_gens = k - 1
    nfac = qfac(k)

    print("="*70)
    print(f"SYMBOLIC k={k} CHARACTERS — sparse seminormal, all in q")
    print("="*70)

    # Build all partitions
    print(f"\nBuilding sparse seminormal for partitions of {k}...")
    pdata = {}
    for shape in partitions_of(k):
        t0 = time.time()
        sigmas, dim, syts = build_sparse_seminormal(shape)
        dt = time.time() - t0
        dq = dim_q_sym(shape)
        w = cancel(dq**2 / nfac)
        cs = content_sum(shape)
        sc = (shape == conjugate(shape))

        # Per-generator trace (should be same for all g by symmetry)
        if dim > 0 and sigmas:
            tr_g = cancel(sigmas[0].trace() / dim)
        else:
            tr_g = sp.Integer(0)

        pdata[shape] = dict(sigmas=sigmas, dim=dim, dq=dq, w=w,
                            cs=cs, sc=sc, tr_g=tr_g)
        nnz = sigmas[0].nnz() if sigmas else 0
        print(f"  {str(shape):>20} dim={dim:>3} nnz/gen={nnz:>3} "
              f"tr/dim={factor(tr_g)}  ({dt:.2f}s)")

    # Test nuclei: A=2..7
    nuclei = [
        ('D',   1, 1),
        ('3H',  1, 2),
        ('3He', 2, 1),
        ('4He', 2, 2),
        ('6Li', 3, 3),
        ('7Li', 3, 4),
    ]

    all_shapes = list(partitions_of(k))

    print(f"\n{'='*70}")
    print(f"CHARACTERS χ_λ(q) — sparse computation")
    print(f"{'='*70}")

    results = {}  # (name, shape) → chi(q)

    for name, Z, N in nuclei:
        A = Z + N
        n_cross = A*(A-1)//2
        print(f"\n  {name} (Z={Z}, N={N}, A={A}, {n_cross} crossings)")

        for shape in all_shapes:
            pd = pdata[shape]
            if pd['dim'] == 0: continue

            t0 = time.time()
            chi = nuclear_chi_sparse(Z, N, pd['sigmas'], pd['dim'], n_gens)
            dt = time.time() - t0

            chi_factored = factor(chi)
            chi_num = complex(chi.subs(q, q0_num)).real
            results[(name, shape)] = chi

            chi_str = str(chi_factored)
            if len(chi_str) > 60:
                chi_str = chi_str[:57] + "..."

            print(f"    {str(shape):>20} χ(q₀)={chi_num:>+12.4f}  "
                  f"{chi_str}  ({dt:.1f}s)")

    # ── Markov trace and shadow prices per nucleus ────────────
    print(f"\n{'='*70}")
    print(f"MARKOV TRACE AND [3,2,1] CONTRIBUTION")
    print(f"{'='*70}")

    from experimental_constants import M_E_MEV
    CATALAN_G = 0.915965594177219015054603514932
    alpha_num = M_E_MEV * 8 * CATALAN_G

    for name, Z, N in nuclei:
        A = Z + N
        T_iso = abs(N-Z)/2.0
        TT1 = T_iso*(T_iso+1)

        total_markov = sp.Integer(0)
        chi_321 = results.get((name, (3,2,1)), sp.Integer(0))
        m_321 = cancel(pdata[(3,2,1)]['w'] * chi_321 / 16)
        m_321_num = float(m_321.subs(q, q0_num))

        for shape in all_shapes:
            pd = pdata[shape]
            if pd['dim'] == 0: continue
            chi = results.get((name, shape), sp.Integer(0))
            total_markov += pd['w'] * chi / pd['dim']

        total_markov = cancel(total_markov)
        tm_num = float(total_markov.subs(q, q0_num))

        print(f"\n  {name} (T={T_iso}, T(T+1)={TT1:.2f}):")
        print(f"    Markov trace M(q₀) = {tm_num:+.8f}")
        print(f"    m_321(q₀) = {m_321_num:+.8f}  ({m_321_num/tm_num*100:+.2f}% of total)" if abs(tm_num) > 1e-15 else f"    m_321(q₀) = {m_321_num:+.8f}")
        print(f"    m_321(q) = {factor(m_321)}")

    print("\nDone.")
