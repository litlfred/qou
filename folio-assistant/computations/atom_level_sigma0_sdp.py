#!/usr/bin/env python3
"""
Atom-level SDP for σ₀ count per nucleon.

Paper's integer LP at H_3-local level derives 2σ₀/nucleon as optimal
for proton-mass (mass_endomorphism.py → 1.8% error).

Paper's atom-level analysis (atomic-braid-mass.md §20-31) notes that
1σ₀/nucleon is optimum at the ATOMIC level — ~0.04% tighter than 2σ₀.

This script lets SDP decide: run the atom binding prediction for
k=1,2,3 copies of σ₀ per nucleon across D..12C, and measure which
gives minimum |B_predicted - AME| across the test atoms.

Pure SDP, no hand-picked integer LP.
"""
import sys, math, json, itertools
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


def ln_phi_q(v, max_k=500):
    """Euler product log|Φ_q(v)| — session-best numerical method.

    Uses abs() inside log so it handles |v|>=q₀ as well (series
    oscillates but abs log is finite for real v != q_0^k).
    """
    if v == 0: return 0
    s = 0
    for k in range(1, max_k+1):
        f = 1 - qi0**k * v
        if abs(f) < 1e-300: return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * v) < 1e-15: break
    return s


def V_char_div_dim(gen_idx, ordering, shape, sigma0_p=2, sigma0_n=4):
    """V̂^λ_i with explicit proton and neutron σ₀-count parameters."""
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
    gluon_count = sigma0_p if ordering[gen_idx] == 1 else sigma0_n
    if gen_idx < len(sigmas):
        for _ in range(gluon_count):
            prod = prod @ (1.0 * sigmas[gen_idx] + 0.0 * I)
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        if gen_idx < len(sigmas):
            prod = prod @ (c * sigmas[gen_idx] + d * I)
    if sparse:
        chi = float(prod.diagonal().sum())
    else:
        chi = float(np.trace(prod))
    return chi / dim_irrep


def dim_q_hook(partition):
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


def B_log_form(Z, N, sigma0_p=2, sigma0_n=4):
    """Nuclear binding via log form B = Σ_λ w_λ m_e Σ_i ln|Φ_q(V̂^λ_i)|."""
    A = Z + N
    if A < 2: return 0.0
    ordering = ground(Z, N)
    parts = list(partitions_of(A))
    dq = [dim_q_hook(list(p)) for p in parts]
    sum_dq2 = sum(d**2 for d in dq)
    weights = [d**2 / sum_dq2 for d in dq]

    B = 0.0
    for pi, p in enumerate(parts):
        shape = tuple(p)
        w = weights[pi]
        ln_sum = 0.0
        for gi in range(A - 1):
            V = V_char_div_dim(gi, ordering, shape,
                               sigma0_p=sigma0_p, sigma0_n=sigma0_n)
            if V is None: continue
            ln_sum += ln_phi_q(abs(V))
        B += w * M_E_MEV * ln_sum
    return B


AME = {'D':2.224566, 'T':8.481798, '3He':7.718058, '4He':28.295674,
       '6Li':31.994571, '7Li':39.244529, '9Be':58.164980,
       '12C':92.161728}
ATOMS = [('D',1,1), ('T',1,2), ('3He',2,1), ('4He',2,2),
         ('6Li',3,3), ('7Li',3,4), ('9Be',4,5), ('12C',6,6)]

print("="*95)
print("ATOM-LEVEL SDP: σ₀ count per nucleon (proton σ₀_p, neutron σ₀_n)")
print("="*95)
print(f"{'σ₀_p':>5} {'σ₀_n':>5}  " + "  ".join(f"{a:>7}" for a,_,_ in ATOMS) + "   mean_err")
print("-"*110)

results = {}
for sigma0_p, sigma0_n in itertools.product([1, 2, 3, 4], [2, 3, 4, 5, 6]):
    errs = []
    row_B = {}
    for name, Z, N in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        try:
            B = B_log_form(Z, N, sigma0_p, sigma0_n)
        except Exception:
            B = float('nan')
        err = abs(B - AME[name])/Mtot*100 if math.isfinite(B) else float('nan')
        row_B[name] = {'B': B, 'err_pct': err}
        if math.isfinite(err): errs.append(err)
    mean_err = np.mean(errs) if errs else float('nan')
    results[(sigma0_p, sigma0_n)] = {'row': row_B, 'mean_err_pct': mean_err}
    err_str = "  ".join(f"{row_B[n]['err_pct']:7.3f}" if math.isfinite(row_B[n]['err_pct'])
                       else '    nan' for n,_,_ in ATOMS)
    print(f"{sigma0_p:>5} {sigma0_n:>5}  {err_str}   {mean_err:.3f}%")

# Find SDP-optimal (p_count, n_count)
best = min([(k, v['mean_err_pct']) for k, v in results.items() if math.isfinite(v['mean_err_pct'])],
           key=lambda x: x[1])
print("\n" + "="*95)
print(f"SDP-optimal: σ₀_p={best[0][0]}, σ₀_n={best[0][1]}  →  mean err {best[1]:.4f}%")
print("="*95)
b_row = results[best[0]]['row']
for name, Z, N in ATOMS:
    r = b_row[name]
    print(f"  {name:>5}  B_pred={r['B']:>+10.4f}  AME={AME[name]:>+10.4f}  err={r['err_pct']:.4f}%")

out = Path(__file__).parent / "atom-level-sigma0-sdp.witness.json"
out.write_text(json.dumps({
    "computation": "atom-level-sigma0-sdp",
    "description": "Atom-level SDP for per-nucleon σ₀ count.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "best_sigma0_p": best[0][0],
    "best_sigma0_n": best[0][1],
    "best_mean_err_pct": best[1],
    "results_by_config": {f"p{k[0]}_n{k[1]}": v for k, v in results.items()},
}, indent=2, default=str))
print(f"\nWitness: {out}")
