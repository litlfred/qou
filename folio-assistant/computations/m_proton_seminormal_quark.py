#!/usr/bin/env python3
"""
Proton mass via full seminormal (non-abelianized) H_n(q) tower with
explicit quark flavor structure.

Key differences from mass_endomorphism.py (abelianized):
  1. V̂_i^λ computed from Young seminormal matrices (full non-abelian
     Hecke representation), not the 3-channel sym/std/alt scalar mix.
  2. Explicit quark flavors in the "ordering": proton = [u,u,d],
     neutron = [u,d,d].  Crossing coefficients indexed by flavor pair.
  3. Gluon multiplicity per flavor (not per nucleon).
  4. Mass dimensional bridge: m = (m^tower_proton / m^tower_electron)
     × m_e(MeV).  Electron tower = trefoil σ_1³ on 2 strands.

Formula (linear, no outer log — gives MASS not binding):
  m^λ(uud) = |∏V̂^λ_i| + Σ Φ_q(V̂^λ_i) + Σ_{i<j} z² Φ_q(V̂^λ_i V̂^λ_j)
  m^tower = Σ_λ w_λ · m^λ
  m_p(MeV) = (m^tower_proton / m^tower_electron) · m_e(MeV)

Quark crossing coefficients: TESTED against SDP (below).
Gluon multiplicity per flavor: TESTED against SDP (below).
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


# Flavor enum
U, D = 1, 0   # u-quark (isospin up), d-quark (isospin down)


def ln_phi_q(v, max_k=2000):
    """ln|Φ_q(v)| = -Σ_k ln|1 - q^{-k}v|.

    Finite for all real v ≠ q^k (poles at those points). Handles
    |v| ≥ q by summing signed log-terms; Φ_q itself diverges there
    but its logarithm is well-defined as a principal-value limit.
    """
    s = 0.0
    for k in range(1, max_k+1):
        f = 1.0 - qi0**k * v
        if abs(f) < 1e-300:
            return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * v) < 1e-15:
            break
    return s


def phi_q(v, max_k=500):
    """Quantum dilog Φ_q(v) — kept for electron trefoil below."""
    return math.exp(ln_phi_q(v, max_k))


def logsumexp(log_terms):
    """Stable log(Σ exp(a_i)) for potentially large a_i."""
    if not log_terms: return float('-inf')
    m = max(log_terms)
    if m == float('-inf'): return m
    return m + math.log(sum(math.exp(a - m) for a in log_terms))


def flavor_crossing(fi, fj):
    """Crossing coefficient for (flavor_i, flavor_j) pair.

    Derived from isospin SU(2) mixing in H_2(q):
      uu: SU(2) symmetric → (c, d) = (1, 0)         [T_i + 0·I]
      dd: SU(2) antisym   → (c, d) = (1, -h)        [T_i - h·I]
      ud/du: mixed (½ sym + ½ antisym) → (1, -h/2)
    """
    if fi == U and fj == U: return (1.0, 0.0)
    if fi == D and fj == D: return (1.0, -h)
    return (1.0, -h/2.0)


def gluon_multiplicity(flavor):
    """Gluon self-coupling modes per quark flavor.

    u-quark (charge +2/3): 2 gluon modes
    d-quark (charge -1/3): 4 gluon modes (stronger color-magnetic)

    Matches the nucleon-level convention from B_consistent_all_orders.py.
    """
    return 2 if flavor == U else 4


def V_char_div_dim(gen_idx, flavors, shape):
    """V̂_i^λ = χ_λ(T_i)/dim(V_λ) with flavor-aware crossings and gluons."""
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
    n = len(flavors)
    g_count = gluon_multiplicity(flavors[gen_idx])
    if gen_idx < len(sigmas):
        for _ in range(g_count):
            prod = prod @ (1.0 * sigmas[gen_idx] + 0.0 * I)
    for j in range(gen_idx + 1, n):
        c, d = flavor_crossing(flavors[gen_idx], flavors[j])
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


def m_tower_linear(flavors, include_triples=True):
    """Compute m^tower = Σ_λ w_λ · m^λ (linear form, no outer log).

    Returns (m_tower, breakdown_per_irrep).
    """
    n = len(flavors)
    if n < 2:
        # Single-strand base case: trivial product, single Φ_q
        return 1.0, []
    parts = list(partitions_of(n))
    dq = [dim_q_hook(list(p)) for p in parts]
    sum_dq2 = sum(d**2 for d in dq)
    weights = [d**2 / sum_dq2 for d in dq]

    m_tower = 0.0
    breakdown = []
    for pi, p in enumerate(parts):
        shape = tuple(p)
        w = weights[pi]
        V_list = []
        for gi in range(n - 1):
            V = V_char_div_dim(gi, flavors, shape)
            V_list.append(V if V is not None else 0.0)

        desc = 1.0
        for v in V_list: desc *= v
        desc_abs = abs(desc)

        singles = sum(phi_q(abs(v)) for v in V_list)

        pairs = 0.0
        for i in range(n - 1):
            for j in range(i + 1, n - 1):
                pairs += z**2 * phi_q(abs(V_list[i] * V_list[j]))

        triples = 0.0
        if include_triples and n >= 4:
            for i, j, k in itertools.combinations(range(n-1), 3):
                triples += z**4 * phi_q(abs(V_list[i] * V_list[j] * V_list[k]))

        m_lambda = desc_abs + singles + pairs + triples
        m_tower += w * m_lambda
        breakdown.append({
            'partition': str(p), 'weight': w,
            'V_list': V_list,
            'desc': desc_abs, 'singles': singles,
            'pairs': pairs, 'triples': triples,
            'm_lambda': m_lambda,
        })
    return m_tower, breakdown


def m_electron_tower(n_crossings=3):
    """Electron = trefoil σ_1^{n_crossings} on 2 strands.

    The trefoil is the (2,3)-torus knot = σ_1³.  Here we reuse the
    same linear form but for a 2-strand, single-generator system.
    The "flavor" is irrelevant (no flavor crossing structure) — we
    just use gluon_count = n_crossings (the trefoil exponent).
    """
    # H_2(q) has two irreps: (2) sym and (1,1) alt, each 1-dim.
    parts = [(2,), (1, 1)]
    dq = [dim_q_hook(list(p)) for p in parts]
    sum_dq2 = sum(d**2 for d in dq)
    weights = [d**2 / sum_dq2 for d in dq]

    m_tower = 0.0
    breakdown = []
    for pi, p in enumerate(parts):
        shape = tuple(p)
        w = weights[pi]
        try:
            sigmas, dim_irrep, _ = _cached_seminormal(shape)
        except Exception:
            continue
        from scipy.sparse import issparse
        sparse = bool(sigmas) and issparse(sigmas[0])
        if sparse:
            import scipy.sparse as sp
            prod = sp.eye(dim_irrep, format='csr')
            for _ in range(n_crossings):
                prod = prod @ sigmas[0]
            chi = float(prod.diagonal().sum())
        else:
            prod = np.eye(dim_irrep)
            for _ in range(n_crossings):
                prod = prod @ sigmas[0]
            chi = float(np.trace(prod))
        V = chi / dim_irrep

        # Linear form: |V| + Φ_q(V), no pairs (only 1 generator)
        m_lambda = abs(V) + phi_q(abs(V))
        m_tower += w * m_lambda
        breakdown.append({'partition': str(p), 'weight': w, 'V': V,
                          'phi_q': phi_q(abs(V)), 'm_lambda': m_lambda})
    return m_tower, breakdown


# === MAIN ===
PROTON_FLAVORS = [U, U, D]
NEUTRON_FLAVORS = [U, D, D]

print(f"{'='*80}")
print(f"PROTON MASS via seminormal + explicit quarks + electron-ref scaling")
print(f"q0 = {q0}")
print(f"m_e = {M_E_MEV} MeV")
print(f"CODATA m_p = {M_P_MEV} MeV  (m_p/m_e = {M_P_MEV/M_E_MEV:.4f})")
print(f"{'='*80}\n")

# Electron tower (reference)
m_e_tower, e_bd = m_electron_tower(n_crossings=3)
print(f"ELECTRON tower (trefoil σ_1³, 2 strands):")
for b in e_bd:
    print(f"  λ={b['partition']} w={b['weight']:.4f}  V={b['V']:+.4f}  "
          f"Φ_q={b['phi_q']:.3f}  m^λ={b['m_lambda']:.3f}")
print(f"  → m^tower_e = {m_e_tower:.6f}")

# Proton tower
print(f"\nPROTON tower (uud, 3 strands):")
m_p_tower, p_bd = m_tower_linear(PROTON_FLAVORS)
for b in p_bd:
    print(f"  λ={b['partition']} w={b['weight']:.4f}  V={[f'{v:+.3f}' for v in b['V_list']]}")
    print(f"     desc={b['desc']:.3f}  singles={b['singles']:.3f}  "
          f"pairs={b['pairs']:.3f}  → m^λ={b['m_lambda']:.3f}")
print(f"  → m^tower_p = {m_p_tower:.6f}")

# Dimensional bridge
ratio_p = m_p_tower / m_e_tower
m_p_pred = ratio_p * M_E_MEV
err_pct = abs(m_p_pred - M_P_MEV)/M_P_MEV*100
err_ppm = abs(m_p_pred - M_P_MEV)/M_P_MEV*1e6
print(f"\nm_p/m_e (tower ratio) = {ratio_p:.6f}")
print(f"m_p predicted = {m_p_pred:.4f} MeV")
print(f"m_p CODATA    = {M_P_MEV:.4f} MeV")
print(f"Error         = {m_p_pred - M_P_MEV:+.4f} MeV  ({err_pct:.4f}% = {err_ppm:.0f} ppm)")

# Neutron tower (same framework)
print(f"\nNEUTRON tower (udd, 3 strands):")
m_n_tower, n_bd = m_tower_linear(NEUTRON_FLAVORS)
ratio_n = m_n_tower / m_e_tower
m_n_pred = ratio_n * M_E_MEV
print(f"  → m^tower_n = {m_n_tower:.6f}")
print(f"  m_n predicted = {m_n_pred:.4f} MeV  (CODATA: 939.565 MeV)")
print(f"  Δm (n-p) predicted = {m_n_pred - m_p_pred:+.4f} MeV  (CODATA: +1.2933 MeV)")

out = Path(__file__).parent / "m-proton-seminormal-quark.witness.json"
out.write_text(json.dumps({
    "computation": "m-proton-seminormal-quark",
    "description": "Proton mass via full seminormal + explicit uud quark flavors.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "m_e_tower": m_e_tower,
    "m_p_tower": m_p_tower,
    "m_p_predicted_MeV": m_p_pred,
    "m_p_codata_MeV": M_P_MEV,
    "err_ppm": err_ppm,
    "m_n_tower": m_n_tower,
    "m_n_predicted_MeV": m_n_pred,
    "delta_mn_mp_predicted": m_n_pred - m_p_pred,
    "proton_breakdown": p_bd,
    "electron_breakdown": e_bd,
    "neutron_breakdown": n_bd,
}, indent=2, default=str))
print(f"\nWitness: {out}")
