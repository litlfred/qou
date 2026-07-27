import sys
from pathlib import Path
HERE = Path("/Users/litlfred/space_cats/qou/computations").resolve()
sys.path.insert(0, str(HERE))
import sympy as sp
from partition_utils import hook_lengths_with_cells as hook_lengths
from per_irrep_pole_atom_crystal import chi_pole_order_crystal
from canonical_braid_crossings import atom_canonical_crossings

def n_lambda(partition):
    return sum(i * partition[i] for i in range(len(partition)))

def classical_dim(partition):
    n = sum(partition)
    cells = hook_lengths(partition)
    nfact = 1
    for k in range(2, n + 1): nfact *= k
    hprod = 1
    for (_, _, h) in cells: hprod *= h
    return nfact // hprod

def partitions_of(n):
    if n == 0: return [[]]
    result = []
    def rec(remaining, max_part, prefix):
        if remaining == 0:
            result.append(list(prefix))
            return
        for k in range(min(remaining, max_part), 0, -1):
            rec(remaining - k, k, prefix + [k])
    rec(n, n, [])
    return result

def get_leading_term(expr, u):
    if expr == 0: return None, 0
    expr = sp.simplify(expr)
    if expr == 0: return None, 0
    try:
        n_, d_ = sp.fraction(expr)
        n_poly = sp.Poly(n_, u); d_poly = sp.Poly(d_, u)
        n_low = min(m[0] for m in n_poly.monoms()) if n_poly.monoms() else 0
        d_low = min(m[0] for m in d_poly.monoms()) if d_poly.monoms() else 0
        return n_low - d_low, n_poly.coeff_monomial(u**n_low) / d_poly.coeff_monomial(u**d_low)
    except:
        return None, 0

def wenzl_y_leading(partition, u):
    Q = u**4
    z = u / (u**2 + 1)
    q = u**2
    X = q * z / (1 - Q + q * z)
    def schur_p(p):
        cells = hook_lengths(p)
        prod = Q ** n_lambda(p)
        for (i, j, h) in cells:
            c = j - i
            prod *= (1 - X * Q ** c) / (1 - Q ** h)
        return prod
    s_self = schur_p(list(partition))
    n = sum(partition)
    norm = sum(classical_dim(mu) * schur_p(list(mu)) for mu in partitions_of(n))
    return get_leading_term(s_self / norm, u)

u = sp.Symbol('u', positive=True)
n = 6
crossings = tuple(atom_canonical_crossings(1, 1))
parts = partitions_of(n)
for lam in parts:
    ord_chi, coeff_chi, _ = chi_pole_order_crystal(tuple(lam), n, crossings)
    if ord_chi is None: continue
    ord_y, coeff_y = wenzl_y_leading(tuple(lam), u)
    if ord_y is None: continue
    total_ord = ord_y + ord_chi
    total_coeff = coeff_y * coeff_chi
    print(f"Lam: {tuple(lam)} | ord: {total_ord} | coeff: {total_coeff}")
