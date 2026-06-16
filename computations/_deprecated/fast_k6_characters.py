#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Fast symbolic k=6 characters — deferred simplification, all in q.

Key optimization: store matrix entries as raw sympy expressions,
only call cancel() on the FINAL trace. This avoids O(n_crossings)
GCD calls per matrix entry, giving ~10× speedup for A=7.

Also computes the FULL Markov trace M(q) = Σ w_λ χ_λ/dim_λ
and extracts the spectral LP shadow prices for each partition.

Usage:
    cd computations && python3 fast_k6_characters.py
"""

import sympy as sp
from sympy import cancel, factor, Rational, expand
from collections import defaultdict
import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0_num
from experimental_constants import M_E_MEV

q = sp.Symbol('q', positive=True)
qi = 1/q
h = q - qi


def qint(n):
    if n <= 1: return sp.Integer(n)
    return cancel((q**n - q**(-n)) / h)

def qfac(n):
    r = sp.Integer(1)
    for k in range(1, n+1): r *= qint(k)
    return cancel(r)


# ══════════════════════════════════════════════════════════════
# §1  FAST SPARSE MATRIX (deferred cancel)
# ══════════════════════════════════════════════════════════════

class FastSparse:
    """Sparse matrix — NO cancel on intermediate products."""
    __slots__ = ('dim', 'data')

    def __init__(self, dim):
        self.dim = dim
        self.data = {}

    @staticmethod
    def eye(dim):
        m = FastSparse(dim)
        for i in range(dim):
            m.data[(i,i)] = sp.Integer(1)
        return m

    def trace(self):
        """Trace WITH cancel (only place we simplify)."""
        s = sp.Integer(0)
        for i in range(self.dim):
            s += self.data.get((i,i), sp.Integer(0))
        return cancel(s)

    def mul(self, other):
        """Sparse multiply — NO cancel on entries."""
        result = FastSparse(self.dim)
        # Index other by first coordinate for fast lookup
        other_by_row = defaultdict(list)
        for (k, j), v in other.data.items():
            other_by_row[k].append((j, v))

        for (i, k), a in self.data.items():
            for j, b in other_by_row[k]:
                key = (i, j)
                if key in result.data:
                    result.data[key] = result.data[key] + a * b
                else:
                    result.data[key] = a * b
        return result

    def add_scalar_eye(self, d):
        """self + d*I — fast."""
        result = FastSparse(self.dim)
        result.data = dict(self.data)
        for i in range(self.dim):
            key = (i, i)
            if key in result.data:
                result.data[key] = result.data[key] + d
            else:
                result.data[key] = d
        return result

    def scale(self, c):
        """c * self."""
        result = FastSparse(self.dim)
        for key, val in self.data.items():
            result.data[key] = c * val
        return result

    def nnz(self):
        return len(self.data)

    def simplify_entries(self):
        """Cancel all entries (use sparingly)."""
        new_data = {}
        for key, val in self.data.items():
            v = cancel(val)
            if v != 0:
                new_data[key] = v
        self.data = new_data


# ══════════════════════════════════════════════════════════════
# §2  BUILD SEMINORMAL (with FastSparse)
# ══════════════════════════════════════════════════════════════

def partitions_of(n):
    if n == 0: yield (); return
    def g(n, mx):
        if n == 0: yield (); return
        for i in range(min(n,mx), 0, -1):
            for r in g(n-i, i): yield (i,)+r
    yield from g(n, n)

def young_cells(shape):
    return [(i, j) for i, ri in enumerate(shape) for j in range(ri)]

def young_hooks(shape):
    rows = list(shape)
    max_col = rows[0] if rows else 0
    cols = [sum(1 for r in rows if r > j) for j in range(max_col)]
    return [(rows[i]-j-1) + (cols[j]-i-1) + 1
            for i in range(len(rows)) for j in range(rows[i])]

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

def build_fast_seminormal(shape):
    """Build σ₁,...,σ_{n-1} as FastSparse, symbolic in q."""
    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], dim, syts

    sigmas = []
    for k in range(1, n):
        M = FastSparse(dim)
        processed = set()
        for i in range(dim):
            if i in processed: continue
            rho = contents[syts[i][k+1]] - contents[syts[i][k]]
            a = cancel(h / (1 - q**(-2*rho)))

            swap = dict(syts[i])
            swap[k] = syts[i][k+1]; swap[k+1] = syts[i][k]
            j = next((jj for jj in range(dim) if jj != i and syts[jj] == swap), None)

            if j is None:
                M.data[(i,i)] = a
                processed.add(i)
            else:
                a_prime = cancel(h / (1 - q**(2*rho)))
                b = sp.sqrt(cancel(a * a_prime + 1))
                M.data[(i,i)] = a
                M.data[(j,j)] = a_prime
                M.data[(i,j)] = b
                M.data[(j,i)] = b
                processed.add(i); processed.add(j)
        sigmas.append(M)
    return sigmas, dim, syts


# ══════════════════════════════════════════════════════════════
# §3  NUCLEAR CHARACTER (fast, symbolic)
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

def nuclear_chi_fast(Z, N, sigmas, dim, n_gens, simplify_every=0):
    """Compute χ_λ(nuclear braid) using FastSparse.

    simplify_every: if >0, cancel entries every N crossings
    (prevents expression blowup for large A at cost of speed).
    """
    A = Z + N
    if A <= 1 or dim == 0:
        return sp.Integer(dim)
    ordering = nuclear_ordering(Z, N)
    product = FastSparse.eye(dim)
    count = 0

    for i in range(A-1):
        for j in range(i+1, A):
            c, d = crossing_cd(ordering[i], ordering[j])
            g = (i+j) % n_gens
            # M = c·σ_g + d·I
            M = sigmas[g].scale(c).add_scalar_eye(d)
            product = product.mul(M)
            count += 1
            if simplify_every > 0 and count % simplify_every == 0:
                product.simplify_entries()

    return product.trace()


# ══════════════════════════════════════════════════════════════
# §4  MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    k = 6
    n_gens = k - 1
    nfac = qfac(k)

    CATALAN_G = 0.915965594177219015054603514932
    alpha_num = M_E_MEV * 8 * CATALAN_G

    print("="*70)
    print(f"FAST SYMBOLIC k={k} CHARACTERS — all in q")
    print("="*70)

    # Build seminormal
    print(f"\nBuilding seminormal for partitions of {k}...")
    pdata = {}
    for shape in partitions_of(k):
        t0 = time.time()
        sigmas, dim, syts = build_fast_seminormal(shape)
        dt = time.time() - t0
        dq = dim_q_sym(shape)
        w = cancel(dq**2 / nfac)
        cs = content_sum(shape)
        sc = (shape == conjugate(shape))
        tr_g = cancel(sigmas[0].trace() / dim) if dim > 0 and sigmas else sp.Integer(0)

        pdata[shape] = dict(sigmas=sigmas, dim=dim, dq=dq, w=w,
                            cs=cs, sc=sc, tr_g=tr_g)
        print(f"  {str(shape):>20} dim={dim:>3} tr/dim={factor(tr_g)} ({dt:.2f}s)")

    # Test nuclei: A=2..7
    nuclei = [
        ('D',   1, 1),
        ('3H',  1, 2),
        ('3He', 2, 1),
        ('4He', 2, 2),
        ('6Li', 3, 3),
        ('7Li', 3, 4),
        ('9Be', 4, 5),
    ]

    all_shapes = list(partitions_of(k))

    # For each nucleus, compute ALL partition characters
    for name, Z, N in nuclei:
        A = Z + N
        n_cross = A*(A-1)//2
        print(f"\n{'─'*70}")
        print(f"  {name} (Z={Z}, N={N}, A={A}, {n_cross} crossings)")
        print(f"{'─'*70}")

        # Choose simplify frequency based on A
        simp_every = 0 if A <= 4 else (5 if A <= 6 else 3)

        total_markov = sp.Integer(0)
        partition_contribs = {}

        for shape in all_shapes:
            pd = pdata[shape]
            if pd['dim'] == 0: continue

            t0 = time.time()
            chi = nuclear_chi_fast(Z, N, pd['sigmas'], pd['dim'],
                                   n_gens, simplify_every=simp_every)
            dt = time.time() - t0

            chi_num = complex(chi.subs(q, q0_num)).real

            # Markov contribution
            m = cancel(pd['w'] * chi / pd['dim'])
            m_num = float(m.subs(q, q0_num))
            total_markov += m

            partition_contribs[shape] = {
                'chi': chi, 'chi_num': chi_num,
                'm': m, 'm_num': m_num,
            }

            chi_str = str(factor(chi))
            if len(chi_str) > 50: chi_str = chi_str[:47] + "..."

            print(f"    {str(shape):>20} χ={chi_num:>+12.4f} m={m_num:>+12.8f} ({dt:.1f}s)")

        total_markov = cancel(total_markov)
        tm_num = float(total_markov.subs(q, q0_num))
        print(f"\n    Markov trace M(q₀) = {tm_num:+.10f}")

        # BW contribution: B = -α × ln|M|
        if abs(tm_num) > 1e-300:
            import math
            B_exact = -alpha_num * math.log(abs(tm_num))
            print(f"    B_exact = -α·ln|M| = {B_exact:.4f} MeV")

        # [3,2,1] fraction
        m321 = partition_contribs.get((3,2,1), {}).get('m_num', 0)
        if abs(tm_num) > 1e-15:
            print(f"    [3,2,1] fraction = {m321/tm_num*100:+.4f}%")

    # ── Shadow price table (symbolic) ─────────────────────────
    print(f"\n{'='*70}")
    print(f"SHADOW PRICE TABLE: C_λ = w_λ · tr(σ)/dim")
    print(f"{'='*70}")
    print(f"\n  {'Partition':>20} {'tr(σ)/dim':>25} {'C_λ(q₀)':>12} {'C·m_e':>10} {'C·α':>10}")
    for shape in all_shapes:
        pd = pdata[shape]
        if pd['dim'] == 0: continue
        C = cancel(pd['w'] * pd['tr_g'])
        C_num = float(C.subs(q, q0_num))
        print(f"  {str(shape):>20} {str(factor(pd['tr_g'])):>25} "
              f"{C_num:>+12.6f} {C_num*M_E_MEV*1000:>+8.1f}keV "
              f"{C_num*alpha_num*1000:>+8.1f}keV")

    print("\nDone.")
