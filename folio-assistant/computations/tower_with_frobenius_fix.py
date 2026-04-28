#!/usr/bin/env python3
"""
Apply Frobenius antipode symmetrization to V̂_0 and compute FIXED
neutron tower mass.

The Frobenius antipode S: σ ↦ σ⁻¹ sends uu ↔ dd in the Hecke algebra.
The S-SYMMETRIZED V̂ is:
  V̂_sym(chain) = (V̂(chain) + V̂(S(chain))) / 2

This is the PROTON/NEUTRON CHIRALITY-INVARIANT combination, as it
treats σ and σ⁻¹ on equal footing.

Hypothesis: using V̂_sym in the tower formula eliminates the
neutron factor-2 gap because the dd-pair's σ⁻¹ contribution is
now averaged with its σ image, giving the same V̂ magnitude as
the proton.
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

from hecke_core import (_PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
                          h as H_A_F, atom_per_generator_volumes, z as Z_MARKOV)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
h = Q0 - QI
z_m = mp.mpf(str(float(Z_MARKOV)))
me = mp.mpf(str(M_E_MEV))


def Phi_q(v, max_it=3000):
    if not isinstance(v, mp.mpf): v = mp.mpf(str(float(v)))
    if v >= 1: return mp.mpf('inf')
    prod = mp.mpf(1); coef = mp.mpf(1)/Q0
    for _ in range(1, max_it+1):
        t = mp.mpf(1) - coef*v
        if abs(t) < mp.mpf('1e-40'): return mp.mpf('inf')
        prod /= t
        if abs(coef*v) < mp.mpf('1e-60'): break
        coef /= Q0
    return prod


def apply_antipode(chain):
    """S: σ ↦ σ⁻¹."""
    h_f = float(H_A_F); out = []
    for c, d in chain:
        c_f, d_f = float(c), float(d)
        if abs(c_f - 1) < 1e-10 and abs(d_f) < 1e-10:
            out.append((1.0, -h_f))
        elif abs(c_f - 1) < 1e-10 and abs(d_f + h_f) < 1e-10:
            out.append((1.0, 0.0))
        else:
            out.append((c, d))
    return out


def V_hat_full_channel(chain, q_val):
    """V̂_full = w_sym·sym + w_std·std + w_alt·alt  (full Wedderburn).

    Per hecke_core convention:
      w_sym = q²/D, w_std = (q²+1)²/D, w_alt = q²/D,  D = q⁴+4q²+1.
    """
    h_val = q_val - mp.mpf(1)/q_val
    qi_val = mp.mpf(1)/q_val
    D = q_val**4 + 4*q_val**2 + 1
    w_sym = q_val**2 / D
    w_std = (q_val**2 + 1)**2 / D
    w_alt = q_val**2 / D

    # Sym channel: product of (c·q + d)
    sym = mp.mpf(1)
    for c, d in chain:
        sym *= (mp.mpf(c)*q_val + mp.mpf(d))
    # Alt channel: product of (-c/q + d)
    alt = mp.mpf(1)
    for c, d in chain:
        alt *= (-mp.mpf(c)/q_val + mp.mpf(d))
    # Std channel: 2×2 transfer
    z_val = mp.mpf(1) / (mp.sqrt(q_val) + mp.sqrt(mp.mpf(1)/q_val))
    a = mp.mpf(0); b = mp.mpf(1)
    for c, d in chain:
        c_m, d_m = mp.mpf(c), mp.mpf(d)
        a_new = a * (c_m * h_val + d_m) + b * c_m
        b_new = a * c_m + b * d_m
        a, b = a_new, b_new
    std = z_val * a + b
    return w_sym*sym + w_std*std + w_alt*alt


def V_sym_frobenius(chain, q_val):
    """Frobenius-symmetrized V̂: (V(chain) + V(S(chain)))/2"""
    V = V_hat_full_channel(chain, q_val)
    V_S = V_hat_full_channel(apply_antipode(chain), q_val)
    return (V + V_S) / 2


def tower_with_V_list(V_list):
    """Compute full-jet-filtration tower with given V̂ values."""
    abs_V = [mp.fabs(mp.mpf(str(float(v)))) for v in V_list]
    n = len(abs_V)
    prod = mp.mpf(1)
    for v in abs_V: prod *= v
    total = prod
    for k in range(1, n + 1):
        for subset in combinations(range(n), k):
            pv = mp.mpf(1)
            for i in subset: pv *= abs_V[i]
            if pv >= 1: continue
            phi = Phi_q(pv)
            span = max(subset) - min(subset) if k >= 2 else 0
            total += z_m**(2*span) * phi
    return total


print("=" * 100)
print("TOWER WITH FROBENIUS ANTIPODE SYMMETRIZATION — fixed neutron?")
print("=" * 100)
print(f"  q_0 = {float(Q0):.8f}")
print()

# Compute V̂_full and V̂_sym_Frobenius for both gens of p and n
V_p_0_orig = V_hat_full_channel(_PROTON_G0, Q0)
V_p_1_orig = V_hat_full_channel(_PROTON_G1, Q0)
V_n_0_orig = V_hat_full_channel(_NEUTRON_G0, Q0)
V_n_1_orig = V_hat_full_channel(_NEUTRON_G1, Q0)

V_p_0_sym = V_sym_frobenius(_PROTON_G0, Q0)
V_p_1_sym = V_sym_frobenius(_PROTON_G1, Q0)
V_n_0_sym = V_sym_frobenius(_NEUTRON_G0, Q0)
V_n_1_sym = V_sym_frobenius(_NEUTRON_G1, Q0)

print(f"  V̂ values (full Wedderburn):")
print(f"    proton  gen 0: orig={float(V_p_0_orig):.6f}  sym_Frob={float(V_p_0_sym):.6f}")
print(f"    proton  gen 1: orig={float(V_p_1_orig):.6f}  sym_Frob={float(V_p_1_sym):.6f}")
print(f"    neutron gen 0: orig={float(V_n_0_orig):.6f}  sym_Frob={float(V_n_0_sym):.6f}")
print(f"    neutron gen 1: orig={float(V_n_1_orig):.6f}  sym_Frob={float(V_n_1_sym):.6f}")
print(f"    Δ gen 0 (n-p): orig={float(V_n_0_orig - V_p_0_orig):+.6f}  sym={float(V_n_0_sym - V_p_0_sym):+.6f}")
print()

# Tower with original V̂
m_p_H_orig = tower_with_V_list([V_p_0_orig, V_p_1_orig])
m_n_H_orig = tower_with_V_list([V_n_0_orig, V_n_1_orig])

# Tower with Frobenius-symmetrized V̂
m_p_H_sym = tower_with_V_list([V_p_0_sym, V_p_1_sym])
m_n_H_sym = tower_with_V_list([V_n_0_sym, V_n_1_sym])

# Calibrate via proton (original)
E0_orig = M_P_MEV / float(m_p_H_orig)
E0_sym = M_P_MEV / float(m_p_H_sym)

print(f"  Tower results (cat-units):")
print(f"  {'method':<30} {'m_p (cat)':>15} {'m_n (cat)':>15}")
print(f"  {'original (σ for uu, σ⁻¹ for dd)':<30} {float(m_p_H_orig):>15.2f} {float(m_n_H_orig):>15.2f}")
print(f"  {'Frobenius-symmetrized':<30} {float(m_p_H_sym):>15.2f} {float(m_n_H_sym):>15.2f}")
print()

print(f"  Calibrated masses (MeV):")
print(f"  {'method':<30} {'E_0':>14} {'m_p':>12} {'m_n':>12} {'err_n':>10}")
print(f"  {'original':<30} {E0_orig:>14.6e} {float(m_p_H_orig)*E0_orig:>12.4f} {float(m_n_H_orig)*E0_orig:>12.4f} "
      f"{(float(m_n_H_orig)*E0_orig - M_N_MEV)/M_N_MEV*100:>+9.3f}%")
print(f"  {'Frobenius-symmetrized':<30} {E0_sym:>14.6e} {float(m_p_H_sym)*E0_sym:>12.4f} {float(m_n_H_sym)*E0_sym:>12.4f} "
      f"{(float(m_n_H_sym)*E0_sym - M_N_MEV)/M_N_MEV*100:>+9.3f}%")
print()

witness = {
    "computation": "tower-with-frobenius-fix",
    "description": (
        "Apply Frobenius antipode symmetrization to V̂ (average with "
        "S(chain)) before computing full-jet tower.  Tests whether "
        "this gives fixed neutron tower."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q_0": Q0_FLOAT,
    "V_p_0_orig": float(V_p_0_orig), "V_p_1_orig": float(V_p_1_orig),
    "V_n_0_orig": float(V_n_0_orig), "V_n_1_orig": float(V_n_1_orig),
    "V_p_0_sym": float(V_p_0_sym), "V_p_1_sym": float(V_p_1_sym),
    "V_n_0_sym": float(V_n_0_sym), "V_n_1_sym": float(V_n_1_sym),
    "m_p_orig_MeV": float(m_p_H_orig)*E0_orig,
    "m_n_orig_MeV": float(m_n_H_orig)*E0_orig,
    "m_p_sym_MeV": float(m_p_H_sym)*E0_sym,
    "m_n_sym_MeV": float(m_n_H_sym)*E0_sym,
    "err_n_orig_pct": (float(m_n_H_orig)*E0_orig - M_N_MEV)/M_N_MEV*100,
    "err_n_sym_pct": (float(m_n_H_sym)*E0_sym - M_N_MEV)/M_N_MEV*100,
}
out = Path(__file__).parent / "tower-with-frobenius-fix.witness.json"
out.write_text(json.dumps(witness, indent=2, default=str))
print(f"  Witness: {out}")
