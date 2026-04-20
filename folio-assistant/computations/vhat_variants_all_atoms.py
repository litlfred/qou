#!/usr/bin/env python3
"""
Test multiple V̂_i^λ variants across D..12C to find uniform formula.

Variants:
  (a) transfer     : z·a_i + b_i  (current full-tower-mass formula)
  (b) char_div_dim : χ_λ(T_i)/dim(V_λ)  (normalized character, wins at A=3)
  (c) char_full    : χ_λ(T_i)  (full trace, no division)
  (d) det_root     : |det ρ_λ(T_i)|^{1/dim}  (geometric mean of eigenvalues)
  (e) largest_eig  : max |eigenvalue ρ_λ(T_i)|
"""
import sys, json, math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV
from mass_at_3A_proper import _cached_seminormal
from hecke_characters import partitions_of

z = 1/(math.sqrt(q0) + 1/math.sqrt(q0))
h = q0 - qi0


def ln_phi_q(v, max_k=500):
    if v == 0: return 0
    s = 0
    for k in range(1, max_k+1):
        f = 1 - qi0**k * v
        if abs(f) < 1e-300: return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * v) < 1e-15: break
    return s


def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1: return (1.0, 0.0)
    elif ti == 0 and tj == 0: return (1.0, -h)
    else: return (1.0, -h/2.0)


def ground(Z, N):
    o=[]; pi=ni=0
    for _ in range(Z+N):
        if pi<Z and (ni>=N or pi/max(Z,1)<=ni/max(N,1)): o.append(1); pi+=1
        else: o.append(0); ni+=1
    return o


def get_Ti_matrix(gen_idx, ordering, shape):
    """Hecke element T_i matrix in irrep λ=shape (seminormal)."""
    try:
        sigmas, dim_irrep, _ = _cached_seminormal(shape)
    except Exception:
        return None, None
    if dim_irrep == 0: return None, None

    from scipy.sparse import issparse, eye as speye
    sparse = bool(sigmas) and issparse(sigmas[0])
    if sparse:
        prod = speye(dim_irrep, format='csr')
        I = speye(dim_irrep, format='csr')
    else:
        prod = np.eye(dim_irrep)
        I = np.eye(dim_irrep)
    A = len(ordering)
    gluon_count = 2 if ordering[gen_idx] == 1 else 4
    if gen_idx < len(sigmas):
        for _ in range(gluon_count):
            prod = prod @ (1.0 * sigmas[gen_idx] + 0.0 * I)
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        if gen_idx < len(sigmas):
            prod = prod @ (c * sigmas[gen_idx] + d * I)
    if sparse:
        prod = prod.toarray()
    return prod, dim_irrep


def V_variants(gen_idx, ordering, shape):
    """Compute all V̂ variants for one (gen_idx, shape)."""
    mat, dim_irrep = get_Ti_matrix(gen_idx, ordering, shape)
    if mat is None:
        return None

    chi = float(np.trace(mat))
    det = float(np.linalg.det(mat))

    # char_div_dim
    char_div = chi / dim_irrep
    # char_full
    char_full = chi
    # det_root (geometric mean of eigenvalues): |det|^{1/dim}
    det_root = abs(det) ** (1.0 / dim_irrep) if dim_irrep > 0 else 0.0

    # largest eigenvalue
    try:
        eigs = np.linalg.eigvals(mat)
        largest = float(max(abs(eigs)))
    except Exception:
        largest = 0.0

    return {
        'chi': chi, 'det': det, 'dim': dim_irrep,
        'char_div_dim': char_div,
        'char_full': char_full,
        'det_root': det_root,
        'largest_eig': largest,
    }


def V_transfer_1d(gen_idx, ordering, shape):
    """Transfer-chain formula for 1-dim irreps (sym, alt)."""
    A = len(ordering)
    sym_v = 1.0
    ap_v = 1.0
    gluon_count = 2 if ordering[gen_idx] == 1 else 4
    for _ in range(gluon_count):
        sym_v *= 1.0*q0 + 0.0
        ap_v *= -1.0/q0 + 0.0
    for j in range(gen_idx+1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        sym_v *= c*q0 + d
        ap_v *= -c/q0 + d
    if shape == (len(ordering),):  # sym (A)
        return sym_v
    elif all(s == 1 for s in shape):  # alt (1^A)
        return ap_v
    return None


def V_transfer_std_A3(gen_idx, ordering):
    """Transfer-chain z·a + b for H_3 std only."""
    if len(ordering) != 3: return None
    a, b = 0.0, 1.0
    gluon_count = 2 if ordering[gen_idx] == 1 else 4
    for _ in range(gluon_count):
        a, b = a*1.0*h + a*0.0 + b*1.0, a*1.0 + b*0.0
    for j in range(gen_idx+1, 3):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        a, b = a*c*h + a*d + b*c, a*c + b*d
    return z * a + b


def dim_q_hook(partition):
    import sympy as sp
    q_sym = sp.Symbol('q', positive=True)
    def qi(n): return (q0**n - q0**(-n))/(q0 - qi0)
    def qf(n):
        r = 1
        for k in range(1, n+1): r *= qi(k)
        return r
    n = sum(partition)
    num = qf(n)
    den = 1
    for i in range(len(partition)):
        for j in range(partition[i]):
            arm = partition[i] - 1 - j
            leg = sum(1 for k in range(i+1, len(partition)) if partition[k] > j)
            den *= qi(arm + leg + 1)
    return num/den


def B_atom_variant(Z, N, variant):
    A = Z + N
    if A < 2: return 0.0
    ordering = ground(Z, N)
    parts = list(partitions_of(A))

    # Weights d_q² / Σ d_q²
    dq = [dim_q_hook(list(p)) for p in parts]
    sum_dq2 = sum(d**2 for d in dq)
    weights = [d**2 / sum_dq2 for d in dq]

    B = 0.0
    for pi, p in enumerate(parts):
        shape = tuple(p)
        w = weights[pi]
        ln_sum = 0.0
        for gi in range(A - 1):
            if variant == 'transfer':
                if len(shape) == 1 or all(s == 1 for s in shape):
                    V = V_transfer_1d(gi, ordering, shape)
                    if V is None: continue
                    ln_sum += ln_phi_q(abs(V))
                elif A == 3 and shape == (2, 1):
                    V = V_transfer_std_A3(gi, ordering)
                    if V is None: continue
                    ln_sum += ln_phi_q(abs(V))
                else:
                    # No transfer-chain formula for this shape — use char_div_dim fallback
                    vr = V_variants(gi, ordering, shape)
                    if vr is None: continue
                    ln_sum += ln_phi_q(abs(vr['char_div_dim']))
            else:
                vr = V_variants(gi, ordering, shape)
                if vr is None: continue
                V = vr[variant] if variant in vr else vr['char_div_dim']
                ln_sum += ln_phi_q(abs(V))
        B += w * M_E_MEV * ln_sum
    return B


ATOMS = [('D',1,1,2.224566), ('T',1,2,8.481798), ('3He',2,1,7.718058),
         ('4He',2,2,28.295674), ('6Li',3,3,31.994571),
         ('7Li',3,4,39.244529), ('9Be',4,5,58.164980),
         ('12C',6,6,92.161728)]

VARIANTS = ['transfer', 'char_div_dim', 'char_full', 'det_root', 'largest_eig']

print(f"{'='*130}")
print("V̂ VARIANTS across D..12C")
print(f"{'='*130}\n")
hdr = f"{'atom':>5} {'A':>2} " + " ".join(f"{v:>14}" for v in VARIANTS) + f" {'AME':>10}"
print(hdr)
print('-'*len(hdr))

results = []
for name, Z, N, B_AME in ATOMS:
    A = Z + N
    Mtot = A * 938.272
    row_B = [B_atom_variant(Z, N, v) for v in VARIANTS]
    errs = [abs(b - B_AME)/Mtot*100 for b in row_B]
    best_idx = int(np.argmin(errs))
    line = f"{name:>5} {A:>2} "
    for i, b in enumerate(row_B):
        star = '*' if i == best_idx else ' '
        line += f"{b:>+8.2f} ({errs[i]:.3f}%){star} "
    line += f" {B_AME:>9.4f}"
    print(line)
    results.append({'atom': name, 'Z': Z, 'N': N, 'A': A, 'B_AME': B_AME,
                    'B_per_variant': dict(zip(VARIANTS, row_B)),
                    'err_per_variant': dict(zip(VARIANTS, errs)),
                    'best_variant': VARIANTS[best_idx],
                    'best_err_pct': errs[best_idx]})

print("\n\nBest variant per atom:")
for r in results:
    print(f"  {r['atom']:>5} (A={r['A']}): {r['best_variant']:>15}  err={r['best_err_pct']:.4f}%")

# Cross-variant summary: which is uniformly best?
print("\nAverage err per variant (across atoms):")
for v in VARIANTS:
    avg = np.mean([r['err_per_variant'][v] for r in results])
    print(f"  {v:>15}: mean err = {avg:.4f}%")

out = Path(__file__).parent / "vhat-variants-all-atoms.witness.json"
out.write_text(json.dumps({
    "computation": "vhat-variants-all-atoms",
    "description": "Test 5 V̂_i^λ variants across D..12C.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "variants": VARIANTS, "results": results,
}, indent=2, default=str))
print(f"\nWitness: {out}")
