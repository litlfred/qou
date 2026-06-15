#!/usr/bin/env python3
"""
Markov chain free energy Q-values from quark-level Garside vertex volumes.

Physical picture (fluid dynamics):
  - Each crossing = vortex tube in the q-fluid
  - Vertex volume V̂_i = cross-section of the vortex tube at position i
  - Small V̂_i = narrow tube = slow flow = high energy density
  - Free energy F = -Σ log|V̂_i| (sum of log-widths)
  - Beta decay changes one quark flavor (d→u), widening/narrowing tubes
  - Q = |ΔF| × kT, where kT = ln(q) × m_e is the Markov "temperature"

Markov chain interpretation (PR #335):
  - Each crossing is a stochastic step with p₊/p₋ = q²
  - Boltzmann ratio: p₋/p₊ = e^{-2 ln(q)} = q^{-2}
  - "Temperature": kT = 1/(2β) where β = ln(q) per crossing
  - Partition function Z = Π V̂_i = tr_M(Δ_A)
  - Free energy F = -ln|Z| = -Σ ln|V̂_i|

Two-stage Garside construction (quark level):
  Stage 1: Intra-nucleon B₃ crossings (confinement)
    - 3 quarks per nucleon, 3 crossings per nucleon, A nucleons
  Stage 2: Inter-nucleon crossings
    - 3×3 = 9 quark pairs per nucleon pair, C(A,2) nucleon pairs

Both stages use the SAME typed crossing operator:
  C(f_i, f_j; σ_k) = σ_k + d(f_i, f_j)
  where d(u,u) = 0, d(d,d) = -(q-q⁻¹), d(u,d) = d(d,u) = -½(q-q⁻¹)

Usage:
    cd folio-assistant/computations && python3 markov-free-energy-qvalues.py
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from itertools import combinations
from mpmath import mp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h, LN_Q
from experimental_constants import M_E_MEV, Q_TRITIUM_MEV, Q_NEUTRON_MEV

z = 1.0 / (q**0.5 + q**(-0.5))
ln_q = LN_Q  # ln(q₀) ≈ 0.1044

print("MARKOV CHAIN FREE ENERGY Q-VALUES")
print(f"  q₀       = {q:.15f}")
print(f"  ln(q₀)   = {ln_q:.15f}")
print(f"  h = q-q⁻¹ = {h:.15f}")
print(f"  z         = {z:.15f}")
print(f"  m_e       = {M_E_MEV} MeV")
print(f"  kT = ln(q)×m_e = {ln_q * M_E_MEV:.8f} MeV")
print("=" * 72)


# ══════════════════════════════════════════════════════════════
#  TYPED CROSSING COEFFICIENTS
# ══════════════════════════════════════════════════════════════

def typed_d(fi, fj):
    """Crossing coefficient d(f_i, f_j) for quark flavors.

    This is the scalar shift in C(f_i,f_j;σ_k) = σ_k + d(f_i,f_j).
    Same-flavor quarks: identity (u-u) or full amplitude (d-d).
    Mixed: half amplitude.
    """
    if fi == 'u' and fj == 'u':
        return 0.0
    elif fi == 'd' and fj == 'd':
        return -h
    else:
        return -h / 2


# ══════════════════════════════════════════════════════════════
#  VERTEX VOLUME FROM CROSSING CHAIN
# ══════════════════════════════════════════════════════════════

def chain_vertex_volume(quark_ordering, gen_idx):
    """Vertex volume V̂_i at generator position gen_idx.

    The crossing chain at generator σ_i involves all crossings
    between strand i and strands j > i. After Hecke reduction,
    the chain is a_i σ_i + b_i, and the vertex volume is:

        V̂_i = z × a_i + b_i

    We compute (a_i, b_i) iteratively: for each j > i, the
    typed crossing C(f_i, f_j; σ_i) multiplied into the chain
    gives:
        new_a = a × h + a × d + b
        new_b = a + b × d

    This is the Hecke reduction σ² = h·σ + 1 applied at each step.
    """
    n = len(quark_ordering)
    a, b = 0.0, 1.0
    for j in range(gen_idx + 1, n):
        d = typed_d(quark_ordering[gen_idx], quark_ordering[j])
        new_a = a * h + a * d + b
        new_b = a + b * d
        a, b = new_a, new_b
    return z * a + b


def all_vertex_volumes(quark_ordering):
    """Compute all vertex volumes V̂_0, ..., V̂_{n-2} for a quark ordering."""
    n = len(quark_ordering)
    return [chain_vertex_volume(quark_ordering, i) for i in range(n - 1)]


def free_energy(quark_ordering):
    """Free energy F = -Σ log|V̂_i|.

    Negative because: narrow tubes (small V̂_i) → large -log|V̂_i| → high energy.
    Convention: F > 0 means stored energy.
    """
    vols = all_vertex_volumes(quark_ordering)
    F = 0.0
    for V in vols:
        if abs(V) < 1e-300:
            return float('inf')  # degenerate configuration
        F -= mp.log(abs(V))
    return F


# ══════════════════════════════════════════════════════════════
#  QUARK ORDERINGS FOR NUCLEI
# ══════════════════════════════════════════════════════════════

def nucleus_quark_ordering(Z, N):
    """Build the quark-level ordering for a nucleus with Z protons, N neutrons.

    Each proton = [u, u, d], each neutron = [u, d, d].
    The Garside staircase processes all C(3A,2) pairwise crossings
    in right-to-left order.

    Returns: list of quark flavors, length 3A.
    """
    quarks = []
    for _ in range(Z):
        quarks.extend(['u', 'u', 'd'])
    for _ in range(N):
        quarks.extend(['u', 'd', 'd'])
    return quarks


def all_quark_orderings(Z, N):
    """Generate all distinct quark orderings for (Z,N).

    A quark ordering is determined by which 3-quark triples are
    protons vs neutrons, AND the arrangement of nucleons.
    For the ground state search, we permute the nucleon positions.
    """
    A = Z + N
    orderings = []
    # Each permutation of nucleon types gives a different ordering
    for proton_positions in combinations(range(A), Z):
        quarks = []
        for i in range(A):
            if i in proton_positions:
                quarks.extend(['u', 'u', 'd'])
            else:
                quarks.extend(['u', 'd', 'd'])
        orderings.append(quarks)
    return orderings


def find_ground_state(Z, N):
    """Find the ordering that minimizes free energy (ground state).

    The ground state = most tightly bound = LARGEST |Σ log V̂_i|.
    Since F = -Σ log|V̂_i|, ground state maximizes F (most energy stored).

    Wait — for STABLE nuclei, we want the configuration that is
    hardest to decay, i.e., the energy minimum after accounting for
    binding. The Garside free energy F = -Σ log|V̂_i| should be
    MINIMIZED for the ground state (most relaxed vortex configuration).

    Actually: Φ = Σ log|V̂_i| is the log-partition function.
    The ground state MAXIMIZES Φ (widest tubes, most flow, most stable).
    Equivalently, MINIMIZES F = -Φ.
    """
    orderings = all_quark_orderings(Z, N)
    best_F = float('inf')
    best_ord = None
    best_Phi = None
    for quarks in orderings:
        F = free_energy(quarks)
        if F < best_F:
            best_F = F
            best_ord = quarks
            best_Phi = -F  # Φ = Σ log|V̂_i| = -F
    return best_ord, best_Phi, best_F


# ══════════════════════════════════════════════════════════════
#  Q-VALUE FROM FREE ENERGY DIFFERENCE
# ══════════════════════════════════════════════════════════════

def compute_qvalue(Z_par, N_par, Z_dau, N_dau):
    """Compute Q-value for beta decay (Z_par,N_par) → (Z_dau,N_dau).

    Q = |ΔF| × ln(q) × m_e

    where ΔF = F_parent - F_daughter (energy released).
    For β⁻ decay: a neutron converts to proton, releasing energy
    when the daughter has lower free energy (wider tubes, easier flow).
    """
    ord_par, Phi_par, F_par = find_ground_state(Z_par, N_par)
    ord_dau, Phi_dau, F_dau = find_ground_state(Z_dau, N_dau)

    # Vertex volumes
    V_par = all_vertex_volumes(ord_par)
    V_dau = all_vertex_volumes(ord_dau)

    n_par = len(ord_par)
    n_dau = len(ord_dau)

    dF = F_par - F_dau  # > 0 if parent has more stored energy
    dPhi = Phi_dau - Phi_par  # = -dF

    # Q-value formulas
    Q_free_energy = abs(dF) * ln_q * M_E_MEV  # THE formula

    return {
        'ord_par': ord_par,
        'ord_dau': ord_dau,
        'V_par': V_par,
        'V_dau': V_dau,
        'Phi_par': Phi_par,
        'Phi_dau': Phi_dau,
        'F_par': F_par,
        'F_dau': F_dau,
        'dF': dF,
        'dPhi': dPhi,
        'n_crossings_par': n_par - 1,
        'n_crossings_dau': n_dau - 1,
        'Q_free_energy': Q_free_energy,
    }


# ══════════════════════════════════════════════════════════════
#  BENCHMARK DECAYS
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  NUCLEON-LEVEL VERTEX VOLUMES (for comparison)")
print("=" * 72)

# First show nucleon-level results (A strands, typed by p/n)
def nucleon_chain_V(ordering, gen):
    """Nucleon-level vertex volume (p=proton, n=neutron)."""
    A = len(ordering)
    a, b = 0.0, 1.0
    for j in range(gen + 1, A):
        ti, tj = ordering[gen], ordering[j]
        if ti == 'p' and tj == 'p':
            d = 0.0
        elif ti == 'n' and tj == 'n':
            d = -h
        else:
            d = -h / 2
        new_a = a * h + a * d + b
        new_b = a + b * d
        a, b = new_a, new_b
    return z * a + b


def nucleon_free_energy(ordering):
    A = len(ordering)
    vols = [nucleon_chain_V(ordering, i) for i in range(A - 1)]
    return -sum(mp.log(abs(V)) for V in vols if abs(V) > 1e-300), vols


def find_nucleon_gs(Z, N):
    A = Z + N
    best_F = float('inf')
    best_ord = None
    for pp in combinations(range(A), Z):
        o = ['n'] * A
        for p in pp:
            o[p] = 'p'
        F, _ = nucleon_free_energy(o)
        if F < best_F:
            best_F = F
            best_ord = o[:]
    return best_ord, best_F


# ══════════════════════════════════════════════════════════════
#  RUN BENCHMARKS
# ══════════════════════════════════════════════════════════════

decays = [
    # (Z_par, N_par, Z_dau, N_dau, Q_exp_MeV, name)
    (0, 1, 1, 0, Q_NEUTRON_MEV,  'n→p (free neutron)'),
    (1, 2, 2, 1, Q_TRITIUM_MEV,  '³H→³He (tritium)'),
    (2, 4, 3, 3, 3.508,          '⁶He→⁶Li'),
]

print("\n" + "=" * 72)
print("  QUARK-LEVEL GARSIDE FREE ENERGY Q-VALUES")
print(f"  Formula: Q = |ΔF| × ln(q) × m_e")
print(f"         = |ΔΣ log|V̂_i|| × {ln_q:.6f} × {M_E_MEV:.5f} MeV")
print("=" * 72)

results = []

for Z_par, N_par, Z_dau, N_dau, Q_exp, name in decays:
    A = Z_par + N_par

    print(f"\n{'━' * 72}")
    print(f"  {name}  (A={A}, {Z_par}p+{N_par}n → {Z_dau}p+{N_dau}n)")
    print(f"  n_quarks = {3*A}, n_crossings = C({3*A},2) = {3*A*(3*A-1)//2}")
    print(f"{'━' * 72}")

    # Nucleon-level comparison
    nuc_par, nuc_F_par = find_nucleon_gs(Z_par, N_par)
    nuc_dau, nuc_F_dau = find_nucleon_gs(Z_dau, N_dau)
    nuc_dF = nuc_F_par - nuc_F_dau
    nuc_Q = float(abs(nuc_dF) * ln_q * M_E_MEV)
    print(f"\n  Nucleon level (A={A} strands):")
    print(f"    Parent:   {''.join(nuc_par)}, F = {float(nuc_F_par):+.8f}")
    print(f"    Daughter: {''.join(nuc_dau)}, F = {float(nuc_F_dau):+.8f}")
    print(f"    ΔF = {float(nuc_dF):+.8f}")
    print(f"    Q_nuc = |ΔF|×ln(q)×m_e = {nuc_Q:.6f} MeV")
    nuc_err = (nuc_Q / Q_exp - 1) * 100 if Q_exp > 0 else float('nan')
    print(f"    vs exp {Q_exp:.6f} MeV → {nuc_err:+.1f}%")

    # Quark-level computation
    r = compute_qvalue(Z_par, N_par, Z_dau, N_dau)

    # Count quark types
    n_u_par = r['ord_par'].count('u')
    n_d_par = r['ord_par'].count('d')
    n_u_dau = r['ord_dau'].count('u')
    n_d_dau = r['ord_dau'].count('d')

    print(f"\n  Quark level ({3*A} strands):")
    print(f"    Parent:   {n_u_par}u + {n_d_par}d, quarks = {''.join(r['ord_par'])}")
    print(f"    Daughter: {n_u_dau}u + {n_d_dau}d, quarks = {''.join(r['ord_dau'])}")

    # Show vertex volumes (truncated for large A)
    n_show = min(len(r['V_par']), 12)
    print(f"\n    {'Gen':>5s} | {'V̂_par':>12s} | {'V̂_dau':>12s} | {'log|V̂_p|':>10s} | {'log|V̂_d|':>10s}")
    print(f"    {'':->60s}")
    for i in range(n_show):
        lp = mp.log(abs(r['V_par'][i])) if abs(r['V_par'][i]) > 1e-300 else float('-inf')
        ld = mp.log(abs(r['V_dau'][i])) if abs(r['V_dau'][i]) > 1e-300 else float('-inf')
        print(f"    {i:>5d} | {r['V_par'][i]:>+12.6f} | {r['V_dau'][i]:>+12.6f} | {float(lp):>+10.4f} | {float(ld):>+10.4f}")
    if len(r['V_par']) > n_show:
        print(f"    ... ({len(r['V_par']) - n_show} more crossings)")

    print(f"\n    Φ_par = Σ log|V̂_i| = {float(r['Phi_par']):+.8f}")
    print(f"    Φ_dau = Σ log|V̂_i| = {float(r['Phi_dau']):+.8f}")
    print(f"    F_par = -Φ_par     = {float(r['F_par']):+.8f}")
    print(f"    F_dau = -Φ_dau     = {float(r['F_dau']):+.8f}")
    print(f"    ΔF = F_par - F_dau = {float(r['dF']):+.8f}")

    Q = float(r['Q_free_energy'])
    err = (Q / Q_exp - 1) * 100 if Q_exp > 0 else float('nan')
    print(f"\n    *** Q = |ΔF| × ln(q) × m_e = {Q:.6f} MeV")
    print(f"    *** Q_exp                   = {Q_exp:.6f} MeV")
    print(f"    *** Error                   = {err:+.2f}%")

    # Also test alternative scales
    Q_alt1 = float(abs(r['dF']) * h * M_E_MEV)       # scale = h = q - q⁻¹
    Q_alt2 = float(abs(r['dF']) * z**2 * M_E_MEV)    # scale = z²
    Q_alt3 = float(abs(r['dF']) * M_E_MEV)            # scale = 1
    Q_alt4 = float(abs(r['dF']) * (1 - qi) * M_E_MEV)  # scale = ℏ_q

    print(f"\n    Alternative scales:")
    print(f"      Q(h)    = |ΔF|×h×m_e      = {Q_alt1:.6f} MeV ({(Q_alt1/Q_exp-1)*100:+.1f}%)")
    print(f"      Q(z²)   = |ΔF|×z²×m_e     = {Q_alt2:.6f} MeV ({(Q_alt2/Q_exp-1)*100:+.1f}%)")
    print(f"      Q(1)    = |ΔF|×m_e         = {Q_alt3:.6f} MeV ({(Q_alt3/Q_exp-1)*100:+.1f}%)")
    print(f"      Q(ℏ_q)  = |ΔF|×ℏ_q×m_e    = {Q_alt4:.6f} MeV ({(Q_alt4/Q_exp-1)*100:+.1f}%)")

    results.append({
        'name': name,
        'A': A,
        'Z_par': Z_par, 'N_par': N_par,
        'Z_dau': Z_dau, 'N_dau': N_dau,
        'n_quarks': 3 * A,
        'n_crossings': 3 * A * (3 * A - 1) // 2,
        'Phi_par': r['Phi_par'],
        'Phi_dau': r['Phi_dau'],
        'dF': r['dF'],
        'Q_free_energy': Q,
        'Q_exp': Q_exp,
        'error_pct': err,
        'ord_par': ''.join(r['ord_par']),
        'ord_dau': ''.join(r['ord_dau']),
        'nuc_Q': nuc_Q,
        'nuc_err_pct': nuc_err,
    })


# ══════════════════════════════════════════════════════════════
#  SUMMARY TABLE
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  SUMMARY: Q = |ΔF| × ln(q) × m_e")
print("=" * 72)

print(f"\n  {'Decay':>20s} | {'A':>3s} | {'nq':>4s} | {'n_x':>5s} | {'|ΔF|':>10s} | {'Q_calc':>10s} | {'Q_exp':>10s} | {'Err':>8s}")
print(f"  {'':->90s}")
for r in results:
    print(f"  {r['name']:>20s} | {r['A']:>3d} | {r['n_quarks']:>4d} | {r['n_crossings']:>5d} | "
          f"{float(abs(r['dF'])):>10.4f} | {float(r['Q_free_energy']):>10.6f} | {r['Q_exp']:>10.6f} | {float(r['error_pct']):>+7.1f}%")


# ══════════════════════════════════════════════════════════════
#  FLUID DYNAMICS INTERPRETATION
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  FLUID DYNAMICS: VORTEX TUBE CROSS-SECTIONS")
print("=" * 72)
print("""
  Physical picture:
  - Each crossing in the Garside element = vortex tube in q-fluid
  - Vertex volume V̂_i = cross-section area of tube at position i
  - log|V̂_i| = entropy contribution (wider tube = more disorder)
  - F = -Σ log|V̂_i| = free energy (tight tubes = stored energy)
  - Beta decay: d→u changes crossing types, widening some tubes
  - Q = |ΔF| × kT where kT = ln(q) × m_e is the Boltzmann scale

  Why ln(q)?
  - Markov chain: p₊/p₋ = q² (positive crossing preferred by q²)
  - Boltzmann: p₋/p₊ = e^{-ΔE/kT} → ΔE/kT = 2 ln(q)
  - Energy per crossing asymmetry = 2 ln(q) × kT
  - Natural scale: kT = ln(q) (so ΔE = 2 ln²(q) per crossing)
  - Physical units: kT × m_e converts to MeV

  Vortex tube narrowing:
  - More quarks → more crossings → more tubes
  - Each d→d crossing narrows tubes by factor (1 - h) vs u→u
  - Accumulated narrowing → exponentially larger free energy
  - This is why Q(⁶He) >> Q(³H): 153 vs 36 crossings
""")


# ══════════════════════════════════════════════════════════════
#  WITNESS
# ══════════════════════════════════════════════════════════════

witness = {
    'title': 'Markov chain free energy Q-values (quark-level Garside)',
    'formula': 'Q = |ΔF| × ln(q) × m_e, where F = -Σ log|V̂_i|',
    'parameters': {
        'q': q,
        'ln_q': ln_q,
        'h': h,
        'z': z,
        'm_e_MeV': M_E_MEV,
        'kT_MeV': ln_q * M_E_MEV,
    },
    'decays': results,
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'source': 'markov-free-energy-qvalues.py',
}

witness_path = Path(__file__).parent / 'markov-free-energy-qvalues.witness.json'
with open(witness_path, 'w') as f:
    json.dump(witness, f, indent=2, default=str)
print(f"\nWitness: {witness_path.name}")
