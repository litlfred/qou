#!/usr/bin/env python3
"""
Alternative V̂_i^λ definition: normalized character χ_λ(T_i) / dim(V_λ).

Current formula uses:
  V̂_i^sym = ∏_j (c_j q + d_j)   (product of eigenvalues, 1-dim)
  V̂_i^std = z·a_i + b_i          (transfer-chain 2x2 reduction, 2-dim)
  V̂_i^alt = ∏_j (-c_j/q + d_j)  (product, 1-dim)

These coincide with `tr_λ(ρ_λ(T_i))/dim(V_λ)` for 1-dim irreps
but NOT for std (2-dim). Testing whether the normalized-character
definition is the correct per-gen V̂.

If χ_std(σ_0σ_1σ_0) = 0 (verified), the normalized character
V̂_std for words containing σ_0σ_1σ_0 would vanish, potentially
explaining the empirical ρ(std, A<4) suppression.
"""
import sys, json, math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV
from mass_at_3A_proper import _cached_seminormal

z = 1/(math.sqrt(q0) + 1/math.sqrt(q0))
h = q0 - qi0
qint2 = (q0**2 - qi0**2)/(q0 - qi0)
W_SYM = 1/(qint2**2 + 2); W_STD = qint2**2/(qint2**2 + 2); W_ALT = W_SYM


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


def V_via_char_norm(gen_idx, ordering, shape):
    """V̂_i^λ = χ_λ(T_i) / dim(V_λ) via seminormal matrices."""
    try:
        sigmas, dim_irrep, _ = _cached_seminormal(shape)
    except Exception:
        return None
    if dim_irrep == 0: return None

    from scipy.sparse import issparse, eye as speye
    sparse = bool(sigmas) and issparse(sigmas[0])
    if sparse:
        prod = speye(dim_irrep, format='csr')
        I = speye(dim_irrep, format='csr')
    else:
        prod = np.eye(dim_irrep)
        I = np.eye(dim_irrep)

    A = len(ordering)
    # Apply gluon at gen_idx
    gluon_count = 2 if ordering[gen_idx] == 1 else 4
    if gen_idx < len(sigmas):
        for _ in range(gluon_count):
            prod = prod @ (1.0 * sigmas[gen_idx] + 0.0 * I)
    # Inter-nucleon crossings to later nucleons at gen_idx
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        if gen_idx < len(sigmas):
            prod = prod @ (c * sigmas[gen_idx] + d * I)
    if sparse:
        chi = float(prod.diagonal().sum())
    else:
        chi = float(np.trace(prod))
    return chi / dim_irrep


def V_via_transfer(gen_idx, ordering):
    """Current per_gen_volumes (transfer-chain) formula — reference."""
    a_val, b_val = 0.0, 1.0
    sp_v, ap_v = 1.0, 1.0
    A = len(ordering)
    gluon_count = 2 if ordering[gen_idx] == 1 else 4
    for _ in range(gluon_count):
        a_val, b_val = a_val*1.0*h + a_val*0.0 + b_val*1.0, a_val*1.0 + b_val*0.0
        sp_v *= 1.0*q0 + 0.0
        ap_v *= -1.0/q0 + 0.0
    for j in range(gen_idx+1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        a_val, b_val = a_val*c*h + a_val*d + b_val*c, a_val*c + b_val*d
        sp_v *= c*q0 + d
        ap_v *= -c/q0 + d
    return sp_v, z*a_val + b_val, ap_v


AME = {'D':2.224566, 'T':8.481798, '3He':7.718058, '4He':28.295674}

ATOMS = [('D',1,1),('T',1,2),('3He',2,1),('4He',2,2)]
# partitions_of for small A + channel names
PARTITIONS = {
    2: [((2,), 'sym'), ((1,1), 'alt')],
    3: [((3,), 'sym'), ((2,1), 'std'), ((1,1,1), 'alt')],
    4: [((4,), 'sym'), ((3,1), '(3,1)'), ((2,2), '(2,2)'),
        ((2,1,1), '(2,1,1)'), ((1,1,1,1), 'alt')],
}


def B_char_norm(Z, N, partitions_with_names):
    A = Z + N
    ordering = ground(Z, N)
    parts = partitions_with_names

    # Use H_A Wedderburn weights (normalized)
    from hecke_characters import partitions_of
    # Compute d_q² per partition
    import sympy as sp
    q_sym = sp.Symbol('q', positive=True)
    def qint(n, q): return (q**n - q**(-n))/(q - 1/q)
    def qfact(n, q):
        r = 1
        for k in range(1, n+1): r *= qint(k, q)
        return r
    def dq(partition, q):
        n = sum(partition)
        num = qfact(n, q)
        den = 1
        for i in range(len(partition)):
            for j in range(partition[i]):
                arm = partition[i] - 1 - j
                leg = sum(1 for k in range(i+1, len(partition)) if partition[k] > j)
                den *= qint(arm + leg + 1, q)
        return num/den
    dq_vals = [dq(list(p), q0) for (p, _) in parts]
    sum_dq2 = sum(d**2 for d in dq_vals)
    weights = [d**2 / sum_dq2 for d in dq_vals]

    B = 0
    breakdown = []
    for i, (p, name) in enumerate(parts):
        w = weights[i]
        ln_sum = 0
        V_list = []
        for gi in range(A - 1):
            V_i = V_via_char_norm(gi, ordering, p)
            if V_i is None:
                continue
            V_list.append(V_i)
            ln_sum += ln_phi_q(abs(V_i))
        contrib = w * M_E_MEV * ln_sum
        B += contrib
        breakdown.append({'partition': str(p), 'channel': name,
                          'weight': w, 'V_per_gen': V_list,
                          'ln_sum': ln_sum, 'B_contrib': contrib})
    return B, breakdown


print(f"{'='*100}")
print("V̂ = χ_λ(T_i)/dim_λ (normalized character per-gen)")
print(f"{'='*100}\n")
print(f"{'atom':>5} {'B_char':>10} {'B_transfer(current)':>20} {'AME':>10} "
      f"{'err_char':>9} {'err_curr':>9}")
print('-'*75)

results = []
for name, Z, N in ATOMS:
    A = Z + N
    if A not in PARTITIONS: continue
    B_AME = AME[name]
    Mtot = A * 938.272
    B_char, breakdown = B_char_norm(Z, N, PARTITIONS[A])

    # Also compute current formula for comparison
    ordering = ground(Z, N)
    Bs_cur = Bd_cur = Ba_cur = 0
    for gi in range(A-1):
        sv, dv, av = V_via_transfer(gi, ordering)
        Bs_cur += ln_phi_q(abs(sv))
        Bd_cur += ln_phi_q(abs(dv))
        Ba_cur += ln_phi_q(abs(av))
    # Use H_3 3-channel weights for current (matches full-tower-mass)
    if A == 2:
        B_cur = 0.5 * M_E_MEV * (Bs_cur + Ba_cur)  # H_2 natural
    elif A == 3:
        B_cur = W_SYM * M_E_MEV * Bs_cur + W_STD * M_E_MEV * Bd_cur + W_ALT * M_E_MEV * Ba_cur
    elif A == 4:
        # A=4: use the Wedderburn weights we computed + H_3 3-ch mask
        B_cur = W_SYM * M_E_MEV * Bs_cur + W_STD * M_E_MEV * Bd_cur + W_ALT * M_E_MEV * Ba_cur

    err_char = abs(B_char - B_AME)/Mtot*100
    err_cur = abs(B_cur - B_AME)/Mtot*100
    print(f"{name:>5} {B_char:>+10.4f} {B_cur:>+20.4f} {B_AME:>+10.4f} "
          f"{err_char:>8.4f}% {err_cur:>8.4f}%")
    results.append({'atom': name, 'Z': Z, 'N': N, 'A': A, 'B_AME': B_AME,
                    'B_char_norm': B_char, 'B_transfer_current': B_cur,
                    'err_char_pct': err_char, 'err_current_pct': err_cur,
                    'breakdown': breakdown})
    for b in breakdown:
        print(f"      {b['partition']:>10} (w={b['weight']:.3f}): V={b['V_per_gen']}, "
              f"ln_sum={b['ln_sum']:.3f}, B={b['B_contrib']:+.3f} MeV")

out = Path(__file__).parent / "vhat-char-normalized.witness.json"
out.write_text(json.dumps({
    "computation": "vhat-char-normalized",
    "description": "Test alternative V̂_i^λ = χ_λ(T_i)/dim(V_λ) via seminormal vs current transfer-chain formula z·a+b.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "results": results,
}, indent=2, default=str))
print(f"\nWitness: {out}")
