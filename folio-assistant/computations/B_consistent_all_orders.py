#!/usr/bin/env python3
"""
Test three structurally-consistent B formulas:

(i) LINEAR: match mass-endomorphism-tower exactly, compute m_atom
    vs some reference and difference.
        m^λ = |∏V̂^λ| + Σ Φ_q(V̂^λ_i) + Σ_{i<j} z² Φ_q(V̂^λ_i V̂^λ_j) + ...
        B = Σ_λ w_λ · m_e · (m^λ_free − m^λ_atom)
    (but m_free requires defining "free atom" — use sum of free-nucleon
    masses as baseline.)

(ii) LOG + R-factor: keep log form, add pentagon R-factor correction:
        R(u, v) = Φ_q(uv) / (Φ_q(u) Φ_q(v))
        B = Σ_λ w_λ m_e [Σ ln|Φ_q(V̂_i^λ)| + z² Σ ln|R(V̂_i^λ, V̂_j^λ)|]
    At A ≥ 4, R ≈ 1 + O(ℏ_q²) and correction is small.
    At A ≤ 3, R-factor provides the actual pair contribution.

(iii) Also check: at A = 4+ include |S|=3 triple terms — do they
      ascend to next jet level (via pentagon) or contribute
      non-trivially?
"""
import sys, json, math, itertools
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


def phi_q(v, max_k=500):
    """Φ_q(v) = exp(-Σ ln|1 - q^{-k} v|) — positive real number."""
    return math.exp(ln_phi_q(v, max_k))


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


def V_char_div_dim(gen_idx, ordering, shape, free_mode=False):
    """V̂_i^λ via seminormal. If free_mode=True, skip inter-nucleon crossings."""
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
    gluon_count = 2 if ordering[gen_idx] == 1 else 4
    if gen_idx < len(sigmas):
        for _ in range(gluon_count):
            prod = prod @ (1.0 * sigmas[gen_idx] + 0.0 * I)
    if not free_mode:
        for j in range(gen_idx + 1, A):
            c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
            if gen_idx < len(sigmas):
                prod = prod @ (c * sigmas[gen_idx] + d * I)
    if sparse: chi = float(prod.diagonal().sum())
    else: chi = float(np.trace(prod))
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


def B_log_plus_rfactor(Z, N, include_triples=False):
    """(ii) Log form + pentagon R-factor correction for pair terms."""
    A = Z + N
    if A < 2: return 0.0, {}
    ordering = ground(Z, N)
    parts = list(partitions_of(A))
    dq = [dim_q_hook(list(p)) for p in parts]
    sum_dq2 = sum(d**2 for d in dq)
    weights = [d**2 / sum_dq2 for d in dq]

    B_singletons = 0.0
    B_pair_rfactor = 0.0
    B_triple = 0.0
    breakdown = []
    for pi, p in enumerate(parts):
        shape = tuple(p)
        w = weights[pi]
        V_list = []
        for gi in range(A - 1):
            V = V_char_div_dim(gi, ordering, shape)
            V_list.append(V if V is not None else 0.0)
        # Singletons
        ln_singles = sum(ln_phi_q(abs(v)) for v in V_list)
        # Pair R-factor: z² · [ln|Φ_q(V_i V_j)| - ln|Φ_q(V_i)| - ln|Φ_q(V_j)|]
        pair_correction = 0.0
        for i in range(A - 1):
            for j in range(i + 1, A - 1):
                ln_uv = ln_phi_q(abs(V_list[i] * V_list[j]))
                ln_u = ln_phi_q(abs(V_list[i]))
                ln_v = ln_phi_q(abs(V_list[j]))
                pair_correction += z**2 * (ln_uv - ln_u - ln_v)
        # Triple contribution: z⁴ · [ln|Φ_q(V_i V_j V_k)| - ...]
        triple_correction = 0.0
        if include_triples and A >= 4:
            for i in range(A - 1):
                for j in range(i + 1, A - 1):
                    for k in range(j + 1, A - 1):
                        ln_uvw = ln_phi_q(abs(V_list[i] * V_list[j] * V_list[k]))
                        # BCH-like triple residual
                        triple_correction += z**4 * ln_uvw
        B_singletons += w * M_E_MEV * ln_singles
        B_pair_rfactor += w * M_E_MEV * pair_correction
        B_triple += w * M_E_MEV * triple_correction
        breakdown.append({'partition': str(p), 'weight': w,
                          'V_list': V_list,
                          'ln_singletons': ln_singles,
                          'pair_rfactor': pair_correction,
                          'triple_correction': triple_correction})
    return B_singletons, B_pair_rfactor, B_triple, breakdown


def B_linear_form(Z, N, include_triples=False):
    """(i) Linear form matching mass-endomorphism-tower.

    For binding, treat m_free as sum of free-nucleon Wedderburn weights
    (trivial contribution); m_atom uses full V̂^λ. Difference gives B.

    Simplified: use m_atom directly as B (approximation valid when
    m_free baseline is already in the Z·m_p + N·m_n part of M(Z,N)).
    """
    A = Z + N
    if A < 2: return 0.0, {}
    ordering = ground(Z, N)
    parts = list(partitions_of(A))
    dq = [dim_q_hook(list(p)) for p in parts]
    sum_dq2 = sum(d**2 for d in dq)
    weights = [d**2 / sum_dq2 for d in dq]

    B = 0.0
    B_desc = 0.0; B_single = 0.0; B_pair = 0.0; B_triple = 0.0
    for pi, p in enumerate(parts):
        shape = tuple(p)
        w = weights[pi]
        V_list = []
        for gi in range(A - 1):
            V = V_char_div_dim(gi, ordering, shape)
            V_list.append(V if V is not None else 0.0)

        # Descended term: |∏V̂|
        desc = 1.0
        for v in V_list: desc *= v
        desc_contrib = abs(desc)

        # Singleton: Σ Φ_q(V_i)
        singles_linear = sum(phi_q(abs(v)) for v in V_list)

        # Pair: Σ z² Φ_q(V_i V_j)
        pairs_linear = 0.0
        for i in range(A - 1):
            for j in range(i + 1, A - 1):
                pairs_linear += z**2 * phi_q(abs(V_list[i] * V_list[j]))

        # Triple (optional): z⁴ Φ_q(V_i V_j V_k)
        triples_linear = 0.0
        if include_triples and A >= 4:
            for i, j, k in itertools.combinations(range(A-1), 3):
                triples_linear += z**4 * phi_q(abs(V_list[i] * V_list[j] * V_list[k]))

        m_lambda = desc_contrib + singles_linear + pairs_linear + triples_linear

        # Take LOG for binding (since B in MeV is log-scale)
        # Or use direct m? Let me try ln|m_λ| which is the natural "binding"
        if m_lambda > 0:
            ln_m_lambda = math.log(m_lambda)
            B_contrib = w * M_E_MEV * ln_m_lambda
        else:
            B_contrib = 0.0
        B += B_contrib

        B_desc += w * M_E_MEV * math.log(max(desc_contrib, 1e-10))
        B_single += w * M_E_MEV * math.log(max(singles_linear, 1e-10))
        B_pair += w * M_E_MEV * math.log(max(pairs_linear, 1e-10)) if pairs_linear > 0 else 0
        B_triple += w * M_E_MEV * math.log(max(triples_linear, 1e-10)) if triples_linear > 0 else 0
    return B, {'desc_log': B_desc, 'single_log': B_single,
               'pair_log': B_pair, 'triple_log': B_triple}


AME = {'D':2.224566, 'T':8.481798, '3He':7.718058, '4He':28.295674,
       '6Li':31.994571, '7Li':39.244529, '9Be':58.164980,
       '12C':92.161728}
ATOMS = [('D',1,1), ('T',1,2), ('3He',2,1), ('4He',2,2),
         ('6Li',3,3), ('7Li',3,4)]

print(f"{'='*130}")
print("Consistent B formulas with all-subset terms (V̂ = χ_λ/dim)")
print(f"{'='*130}\n")
print(f"{'atom':>5} {'A':>2}  "
      f"{'B_singles':>10} {'B_+pair_R':>12} {'B_+tri_R':>12}  "
      f"{'B_lin':>10} {'B_lin+tri':>10}  "
      f"{'AME':>9}")
print('-'*95)

results = []
for name, Z, N in ATOMS:
    A = Z + N
    Mtot = A * 938.272
    B_AME = AME[name]

    # (ii) log + R-factor variants
    Bs, Bp_R, Bt_R, _ = B_log_plus_rfactor(Z, N, include_triples=False)
    _, _, Bt_R_tr, _ = B_log_plus_rfactor(Z, N, include_triples=True)
    B_singles_only = Bs
    B_log_plus_pair = Bs + Bp_R
    B_log_plus_pair_triple = Bs + Bp_R + Bt_R_tr

    # (i) linear form
    B_lin, _ = B_linear_form(Z, N, include_triples=False)
    B_lin_tri, _ = B_linear_form(Z, N, include_triples=True)

    e_s = abs(B_singles_only - B_AME)/Mtot*100
    e_p = abs(B_log_plus_pair - B_AME)/Mtot*100
    e_t = abs(B_log_plus_pair_triple - B_AME)/Mtot*100
    e_lin = abs(B_lin - B_AME)/Mtot*100
    e_lin_tri = abs(B_lin_tri - B_AME)/Mtot*100

    print(f"{name:>5} {A:>2}  "
          f"{B_singles_only:>+9.3f} ({e_s:.3f}%)  "
          f"{B_log_plus_pair:>+9.3f} ({e_p:.3f}%)  "
          f"{B_log_plus_pair_triple:>+9.3f} ({e_t:.3f}%)  "
          f"{B_lin:>+9.3f} ({e_lin:.3f}%)  "
          f"{B_lin_tri:>+9.3f} ({e_lin_tri:.3f}%)  "
          f"{B_AME:>+9.4f}")

    results.append({'atom': name, 'A': A, 'B_AME': B_AME,
                    'B_singles_only': B_singles_only, 'err_singles': e_s,
                    'B_log_plus_pair_Rfactor': B_log_plus_pair, 'err_pair_R': e_p,
                    'B_log_plus_triple_Rfactor': B_log_plus_pair_triple, 'err_tri_R': e_t,
                    'B_linear_form': B_lin, 'err_linear': e_lin,
                    'B_linear_with_triples': B_lin_tri, 'err_lin_tri': e_lin_tri})

out = Path(__file__).parent / "B-consistent-all-orders.witness.json"
out.write_text(json.dumps({
    "computation": "B-consistent-all-orders",
    "description": "Consistent B formulas: log+R-factor (ii), linear form (i), with triples.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "results": results,
}, indent=2, default=str))
print(f"\nWitness: {out}")
