#!/usr/bin/env python3
"""
Proton mass from H_3(q) + linear form + χ/dim V̂.

Applies the same machinery that gave 3He 0.013% binding accuracy
to the proton itself, treated as a 3-quark chain (uud) with 2
generators.

Quark↔nucleon analogy:
  u quark  ←→ 1 in ordering  (like proton in nuclear binding)
  d quark  ←→ 0 in ordering  (like neutron in nuclear binding)

Gluon-count convention from nuclear binding: ordering=1 → 2 gluons,
ordering=0 → 4 gluons.  We test this and also swap it, since the
proton's quark-level gluon coupling may differ from the nuclear-level
gluon coupling.

Crossing coeffs (reused from nuclei):
  uu: (1, 0)      — identical-up quarks, no translation
  dd: (1, -h)     — identical-down quarks, full h
  ud: (1, -h/2)   — mixed, half-h

Formula (linear form = mass_endomorphism_tower §):
  m^λ = |∏V̂^λ| + Σ Φ_q(V̂^λ_i) + Σ_{i<j} z² Φ_q(V̂^λ_i V̂^λ_j)
  m_p(predicted) = Σ_λ w_λ · m_e · ln|m^λ|
"""
import sys, math, itertools, json
from pathlib import Path
from datetime import datetime, timezone
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV, M_P_MEV
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


def phi_q(v, max_k=500):
    return math.exp(ln_phi_q(v, max_k))


def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1: return (1.0, 0.0)      # uu
    elif ti == 0 and tj == 0: return (1.0, -h)     # dd
    else: return (1.0, -h/2.0)                     # ud


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


def V_char_div_dim(gen_idx, ordering, shape, gluon_u, gluon_d):
    """V̂_i^λ = χ_λ(T_i)/dim(V_λ) via seminormal."""
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
    gluon_count = gluon_u if ordering[gen_idx] == 1 else gluon_d
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


def m_particle(ordering, gluon_u, gluon_d, include_triples=False):
    """Total mass prediction in MeV for given quark ordering."""
    A = len(ordering)
    parts = list(partitions_of(A))
    dq = [dim_q_hook(list(p)) for p in parts]
    sum_dq2 = sum(d**2 for d in dq)
    weights = [d**2 / sum_dq2 for d in dq]

    m_total = 0.0
    breakdown = []
    for pi, p in enumerate(parts):
        shape = tuple(p)
        w = weights[pi]
        V_list = []
        for gi in range(A - 1):
            V = V_char_div_dim(gi, ordering, shape, gluon_u, gluon_d)
            V_list.append(V if V is not None else 0.0)

        desc = 1.0
        for v in V_list: desc *= v
        desc_abs = abs(desc)

        singles = sum(phi_q(abs(v)) for v in V_list)

        pairs = 0.0
        for i in range(A - 1):
            for j in range(i + 1, A - 1):
                pairs += z**2 * phi_q(abs(V_list[i] * V_list[j]))

        triples = 0.0
        if include_triples and A >= 4:
            for i, j, k in itertools.combinations(range(A-1), 3):
                triples += z**4 * phi_q(abs(V_list[i] * V_list[j] * V_list[k]))

        m_lambda = desc_abs + singles + pairs + triples
        ln_m = math.log(m_lambda) if m_lambda > 0 else 0.0
        contrib = w * M_E_MEV * ln_m
        m_total += contrib
        breakdown.append({'partition': str(p), 'weight': w,
                          'V_list': V_list, 'ln_m': ln_m,
                          'contrib_MeV': contrib})
    return m_total, breakdown


# Proton = uud, Neutron = udd
PROTON_ORDERING = [1, 1, 0]
NEUTRON_ORDERING = [1, 0, 0]

print(f"{'='*80}")
print(f"PROTON MASS via linear form + χ/dim V̂")
print(f"CODATA m_p = {M_P_MEV} MeV")
print(f"{'='*80}")
print(f"{'gluon_u':>8} {'gluon_d':>8} {'m_p_pred':>12} {'err_pct':>10} {'err_MeV':>10}")
print('-'*60)

best = (None, None, float('inf'), None)
for gu in [1, 2, 3, 4]:
    for gd in [1, 2, 3, 4]:
        mp, bd = m_particle(PROTON_ORDERING, gu, gd)
        err = abs(mp - M_P_MEV)
        err_pct = err/M_P_MEV*100
        marker = ''
        if err < best[2]:
            best = (gu, gd, err, bd)
            marker = ' ←best'
        print(f"{gu:>8} {gd:>8} {mp:>+12.3f} {err_pct:>9.4f}% {err:>+9.3f}{marker}")

print()
print(f"Best: gluon_u={best[0]}, gluon_d={best[1]}, err={best[2]:.3f} MeV"
      f" ({best[2]/M_P_MEV*1e6:.1f} ppm)")
print()
print("Per-irrep breakdown (best config):")
for b in best[3]:
    print(f"  λ={b['partition']} w={b['weight']:.4f}  V={[f'{v:+.4f}' for v in b['V_list']]}"
          f"  ln|m^λ|={b['ln_m']:+.4f}  → {b['contrib_MeV']:+.3f} MeV")

out = Path(__file__).parent / "m-proton-linear-form.witness.json"
out.write_text(json.dumps({
    "computation": "m-proton-linear-form",
    "description": "Proton mass via H_3(q) linear form + χ/dim V̂.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "best_gluon_u": best[0], "best_gluon_d": best[1],
    "best_err_MeV": best[2], "best_err_ppm": best[2]/M_P_MEV*1e6,
    "breakdown": best[3],
}, indent=2, default=str))
print(f"\nWitness: {out}")
