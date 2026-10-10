#!/usr/bin/env python3
"""
Extension of α-blend tower formula to isotopes (D, T, ³He, ⁴He).

For each isotope:
  1. Build per-generator V̂_i^(α) using the blend formula with α = G/3
  2. Apply full-jet-filtration tower
  3. Add Frobenius co-Casimir (universal)
  4. Compare predicted atomic mass M(Z,N) to CODATA
  5. Extract binding B = Z·m_p + N·m_n + Z·m_e − M

Reference: docs/alpha-blend-derivation.md
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 50

from hecke_core import (atom_per_generator_volumes, h as H_A_F,
                          z as Z_MARKOV, _step_chain_generic)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
h = Q0 - QI; h_f = float(H_A_F)
z_m = mp.mpf(str(float(Z_MARKOV)))
me = mp.mpf(str(M_E_MEV))
D_W = Q0**4 + 4*Q0**2 + 1
w_s = Q0**2/D_W; w_t = (Q0**2+1)**2/D_W; w_a = Q0**2/D_W
# Alpha from Catalan constant
ALPHA = mp.catalan / 3


def Phi_q(v, max_it=3000):
    if not isinstance(v, mp.mpf): v = mp.mpf(str(float(v)))
    if v >= 1: return mp.mpf('inf')
    p = mp.mpf(1); c = mp.mpf(1)/Q0
    for _ in range(max_it):
        t = mp.mpf(1)-c*v
        if abs(t) < mp.mpf('1e-40'): return mp.mpf('inf')
        p /= t
        if abs(c*v) < mp.mpf('1e-60'): break
        c /= Q0
    return p


def S_chain(chain):
    out = []
    for c, d in chain:
        cf, df = float(c), float(d)
        if abs(cf-1)<1e-10 and abs(df)<1e-10: out.append((1.0, -h_f))
        elif abs(cf-1)<1e-10 and abs(df+h_f)<1e-10: out.append((1.0, 0.0))
        else: out.append((c, d))
    return out


def sym_alt(chain):
    s=a=mp.mpf(1)
    for c, d in chain:
        s*=(mp.mpf(c)*Q0+mp.mpf(d))
        a*=(-mp.mpf(c)/Q0+mp.mpf(d))
    return s, a


def std_za_b(chain):
    zv = mp.mpf(1)/(mp.sqrt(Q0)+mp.sqrt(QI))
    a=mp.mpf(0); b=mp.mpf(1); hv = Q0-QI
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        a, b = a*(cm*hv+dm)+b*cm, a*cm+b*dm
    return zv*a + b


def std_det(chain):
    Dv = mp.mpf(1); hv = Q0-QI
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        Dv *= (dm*(cm*hv+dm) - cm*cm)
    return Dv


def V_blend_generic(chain, alpha=ALPHA):
    """V̂ computed with α-blend formula for arbitrary chain."""
    s_o, a_o = sym_alt(chain); s_s, a_s = sym_alt(S_chain(chain))
    std_o = std_za_b(chain); std_s = std_za_b(S_chain(chain))
    std_frob = (std_o + std_s)/2
    std_det_v = mp.sqrt(mp.fabs(std_det(chain)))
    std_bl = alpha * std_frob + (1 - alpha) * std_det_v
    return w_s*((s_o+s_s)/2) + w_t*std_bl + w_a*((a_o+a_s)/2)


def atom_per_generator_blend(Z, N):
    """For each generator of atom (Z,N), compute V̂^(α) from that
    generator's cumulative chain."""
    A = Z + N
    n_strands = 3*A
    n_gens = n_strands - 1
    ordering = ['p'] * Z + ['n'] * N
    # Build per-generator chains (sub-chains for each gen index)
    # Full braid word built via _step_chain_generic per nucleon
    gen_chains = [[] for _ in range(n_gens)]
    for k in range(A):
        chain_k = _step_chain_generic(ordering[k], ordering[:k], n_gens,
                                        include_inter=True)
        for c, d, g in chain_k:
            gen_chains[g].append((c, d))
    # Compute V̂^(α) per generator
    return [V_blend_generic(gen_chains[g]) for g in range(n_gens)]


def tower_full(V_list):
    abs_V = [mp.fabs(v) for v in V_list]; n = len(abs_V)
    prod = mp.mpf(1)
    for v in abs_V: prod *= v
    total = prod
    for k in range(1, n+1):
        for sub in combinations(range(n), k):
            pv = mp.mpf(1)
            for i in sub: pv *= abs_V[i]
            if pv >= 1: continue
            span = max(sub)-min(sub) if k >= 2 else 0
            total += z_m**(2*span) * Phi_q(pv)
    return total


def main() -> int:
    print("=" * 100)
    print("α-BLEND EXTENSION TO ISOTOPES — α = G/3 (Catalan/3)")
    print("=" * 100)
    print(f"  α = G/3 = {float(ALPHA):.10f}")
    print()

    ISOTOPES = [('proton', 1, 0), ('neutron', 0, 1),
                 ('D', 1, 1), ('T', 1, 2), ('³He', 2, 1),
                 ('⁴He', 2, 2)]

    results = []
    # Calibrate via proton
    V_p_blend = atom_per_generator_blend(1, 0)
    m_p_cat = tower_full(V_p_blend)
    E0 = M_P_MEV / float(m_p_cat)
    print(f"  Calibration: E_0 = m_p_CODATA / proton_tower_blend = {E0:.6e} MeV/cat")
    print()
    print(f"  {'iso':<8} {'V̂ values':<45} {'tower (cat)':>12} {'mass (MeV)':>12} "
          f"{'CODATA':>10} {'err %':>8}")
    for name, Z, N in ISOTOPES:
        V_blend = atom_per_generator_blend(Z, N)
        m_cat = tower_full(V_blend)
        m_MeV = float(m_cat) * E0
        # Reference masses
        CODATA = {'proton': M_P_MEV, 'neutron': M_N_MEV,
                   'D': 1876.12393, 'T': 2809.43215,
                   '³He': 2809.41347, '⁴He': 3728.40133}
        ref = CODATA.get(name)
        err_str = f"{(m_MeV-ref)/ref*100:+.3f}%" if ref else "—"
        ref_str = f"{ref}" if ref else "—"
        V_str = "[" + ",".join(f"{float(v):.3f}" for v in V_blend[:3]) + \
                ("..." if len(V_blend) > 3 else "") + "]"
        print(f"  {name:<8} {V_str:<45} {float(m_cat):>12.2f} {m_MeV:>12.4f} "
              f"{ref_str:>10} {err_str:>8}")
        results.append({
            'isotope': name, 'Z': Z, 'N': N, 'A': Z+N,
            'n_gens': len(V_blend),
            'V_blend': [float(v) for v in V_blend],
            'tower_cat': float(m_cat),
            'mass_MeV': m_MeV,
            'CODATA_MeV': ref,
            'err_pct': (m_MeV - ref) / ref * 100 if ref else None,
        })

    # Derived binding energies (B = Z·m_p + N·m_n + Z·m_e − M)
    print()
    print(f"  Implied binding energies (B = Z·m_p + N·m_n + Z·m_e − M):")
    print(f"  {'iso':<8} {'B_predicted':>12} {'B_AME':>10} {'err (%)':>10}")
    AME_B = {'D': 2.22456612, 'T': 8.481798, '³He': 7.718058,
              '⁴He': 28.29566}
    for r in results:
        iso = r['isotope']
        if iso in AME_B:
            B_ame = AME_B[iso]
            M_pred = r['mass_MeV']
            B_pred = r['Z']*M_P_MEV + r['N']*M_N_MEV + r['Z']*M_E_MEV - M_pred
            err = (B_pred - B_ame) / B_ame * 100
            print(f"  {iso:<8} {B_pred:>12.4f} {B_ame:>10.4f} {err:>+9.2f}%")
            r['B_pred_MeV'] = B_pred
            r['B_AME_MeV'] = B_ame
            r['err_B_pct'] = err

    witness = {
        'computation': 'alpha-blend-isotopes',
        'description': (
            'α-blend tower (α = G/3 Catalan) extended to D, T, ³He, '
            '⁴He. Applies blended V̂^(α) per generator of atom braid; '
            'full-jet-filtration tower; compares atomic masses and '
            'derived binding energies to CODATA.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'alpha': float(ALPHA),
        'E0_MeV_per_cat': E0,
        'isotopes': results,
    }
    out = Path(__file__).parent / "alpha-blend-isotopes.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
