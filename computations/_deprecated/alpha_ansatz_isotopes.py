#!/usr/bin/env python3
"""
Alpha-ansatz across isotopes: TREAT α as fitted per isotope, look
for systematic pattern across A, then attempt formal derivation.

Two approaches in one script:

  (1) ANSATZ: for each isotope (D, T, ³He, ⁴He), find the α that
      makes M_predicted = M_CODATA exactly.  Tabulate α(A, Z, N).

  (2) DERIVE: hypothesize α as a function of (A, Z, N, q):
        α(A) = G/3 · f(A)  or
        α(A) = (Vol(K) for atom-knot) / |symmetry|
      and check if optimal α matches.

Working hypothesis: α might depend on A as
   α(A) = G / (3 · A^β)  for some β to be derived.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 40

from hecke_core import (atom_per_generator_volumes, h as H_A_F,
                          z as Z_MARKOV, _step_chain_generic)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
me = mp.mpf(str(M_E_MEV))
h = Q0 - QI; h_f = float(H_A_F)
z_m = mp.mpf(str(float(Z_MARKOV)))
D_W = Q0**4 + 4*Q0**2 + 1
w_s = Q0**2/D_W; w_t = (Q0**2+1)**2/D_W; w_a = Q0**2/D_W


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


def V_blend_chain(chain, alpha):
    s_o, a_o = sym_alt(chain); s_s, a_s = sym_alt(S_chain(chain))
    std_o = std_za_b(chain); std_s = std_za_b(S_chain(chain))
    std_frob = (std_o + std_s)/2
    std_det_v = mp.sqrt(mp.fabs(std_det(chain)))
    std_bl = alpha*std_frob + (1-alpha)*std_det_v
    return w_s*((s_o+s_s)/2) + w_t*std_bl + w_a*((a_o+a_s)/2)


def per_gen_chains(Z, N):
    A = Z+N; n_gens = max(1, 3*A - 1)
    ordering = ['p']*Z + ['n']*N
    gens = [[] for _ in range(n_gens)]
    for k in range(A):
        chain_k = _step_chain_generic(ordering[k], ordering[:k], n_gens, include_inter=True)
        for c, d, g in chain_k:
            gens[g].append((c, d))
    return gens


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


def predict_mass(Z, N, alpha, verbose=False):
    """Mass via full atomic α-blend tower."""
    chains = per_gen_chains(Z, N)
    V_blend = [V_blend_chain(c, alpha) for c in chains]
    if verbose:
        print(f"    V̂ values: {[float(v) for v in V_blend]}")
    # Allow values past pole — Phi_q returns inf so tower diverges; treat as nan
    m_cat = tower_full(V_blend)
    try:
        m_cat_f = float(m_cat)
        if mp.isnan(mp.mpf(str(m_cat_f))) or mp.isinf(mp.mpf(str(m_cat_f))):
            return None
        return m_cat_f
    except (TypeError, ValueError):
        return None


# Calibrate via proton at α = G/3
ALPHA_NUC = mp.catalan / 3
m_p_cat = predict_mass(1, 0, ALPHA_NUC)
E0 = M_P_MEV / m_p_cat


def err_n(alpha, Z, N, ref_mass):
    a = mp.mpf(str(alpha))
    m_cat = predict_mass(Z, N, a)
    if m_cat is None: return float('nan')
    m_MeV = m_cat * E0
    return (m_MeV - ref_mass) / ref_mass * 100


def main() -> int:
    print("=" * 100)
    print("ALPHA-ANSATZ across isotopes — find optimal α per (Z, N)")
    print("=" * 100)
    print(f"  α_nucleon (G/3) = {float(ALPHA_NUC):.8f}")
    print(f"  E_0 (proton calibration) = {E0:.4e} MeV/cat")
    print()

    ISOTOPES = [
        ('p',   1, 0, M_P_MEV),
        ('n',   0, 1, M_N_MEV),
        ('D',   1, 1, 1876.12393),
        ('T',   1, 2, 2809.43215),
        ('³He', 2, 1, 2809.41347),
        ('⁴He', 2, 2, 3728.40133),
    ]

    print(f"  {'iso':<6} {'A':>2} {'M_CODATA':>10} {'α* fit':>12} {'α/(G/3)':>10} "
          f"{'M @ G/3':>12} {'err @ G/3':>12}")

    rows = []
    from scipy.optimize import brentq
    for name, Z, N, M_ref in ISOTOPES:
        # Try fitting α such that mass matches CODATA
        try:
            f = lambda a: err_n(a, Z, N, M_ref)
            # Scan for sign change
            alphas_test = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
            errs = [(a, f(a)) for a in alphas_test]
            errs = [(a, e) for a, e in errs if not (e != e)]   # filter NaN
            # Find sign-change
            alpha_star = None
            for i in range(len(errs)-1):
                if errs[i][1] * errs[i+1][1] < 0:
                    try:
                        alpha_star = brentq(f, errs[i][0], errs[i+1][0])
                    except Exception:
                        alpha_star = None
                    break
            if alpha_star is None:
                # Just report error at G/3
                e_g3 = f(float(ALPHA_NUC))
                m_g3 = predict_mass(Z, N, ALPHA_NUC)
                print(f"  {name:<6} {Z+N:>2} {M_ref:>10.4f} {'—':>12} {'—':>10} "
                      f"{m_g3*E0 if m_g3 else 0:>12.4f} {e_g3:>+11.3f}%")
                rows.append({'iso':name, 'Z':Z, 'N':N, 'A':Z+N,
                              'alpha_optimal':None, 'alpha_over_G3':None,
                              'mass_at_G3':m_g3*E0 if m_g3 else None,
                              'err_at_G3_pct':e_g3})
            else:
                ratio = alpha_star / float(ALPHA_NUC)
                e_g3 = f(float(ALPHA_NUC))
                m_g3 = predict_mass(Z, N, ALPHA_NUC)
                print(f"  {name:<6} {Z+N:>2} {M_ref:>10.4f} {alpha_star:>12.6f} {ratio:>10.4f} "
                      f"{m_g3*E0 if m_g3 else 0:>12.4f} {e_g3:>+11.3f}%")
                rows.append({'iso':name, 'Z':Z, 'N':N, 'A':Z+N,
                              'alpha_optimal':alpha_star,
                              'alpha_over_G3':ratio,
                              'mass_at_G3':m_g3*E0 if m_g3 else None,
                              'err_at_G3_pct':e_g3})
        except Exception as e:
            print(f"  {name:<6} ERROR: {type(e).__name__}: {str(e)[:50]}")

    # Look for pattern in α* across A
    print()
    print(f"  Pattern analysis: α*(A) values and ratios")
    print(f"  {'iso':<6} {'A':>2} {'α*':>12} {'α*·A':>12} {'α*/A':>12} {'α*·A/G':>12}")
    G = float(mp.catalan)
    for r in rows:
        if r.get('alpha_optimal') is not None:
            a = r['alpha_optimal']; A = r['A']
            print(f"  {r['iso']:<6} {A:>2} {a:>12.6f} {a*A:>12.6f} {a/A:>12.6f} {a*A/G:>12.6f}")

    witness = {
        'computation': 'alpha-ansatz-isotopes',
        'description': (
            'Treat α as ansatz: fit per isotope to match CODATA mass; '
            'look for systematic pattern α(A, Z, N).'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'alpha_nucleon': float(ALPHA_NUC),
        'rows': rows,
    }
    out = Path(__file__).parent / "alpha-ansatz-isotopes.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
