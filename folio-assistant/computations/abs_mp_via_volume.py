#!/usr/bin/env python3
"""
ABSOLUTE m_p VIA SnapPy hyperbolic volume of the proton braid closure.

Goal: derive m_p from m_e and q_0 alone (no m_p calibration input).

Path: m(K) = Vol(K) / ℏ_q²  (paper topological-mass-formula)
where K = closure of the proton braid β_p in B_3.

Steps:
  1. Build proton braid word (uud quark content + B_3 prefix).
  2. SnapPy: closure → link → hyperbolic volume.
  3. Compute m_pred = Vol / ℏ_q² in some natural unit, scale via m_e
     to MeV.  Compare to m_p_CODATA = 938.272 MeV.

If Vol/(m_e · ℏ_q²) = m_p / m_e at q_0 to within experimental
precision, m_p is fully derived from {m_e, q_0, braid topology}.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

try:
    import snappy
    HAS_SNAPPY = True
except Exception as e:
    HAS_SNAPPY = False
    print(f"snappy unavailable: {e}")
    sys.exit(1)

from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = mp.mpf(str(Q0_FLOAT)); QI = mp.mpf(1)/Q0
hbar_q = 1 - QI                         # paper's quantum Planck constant
hbar_q_sq = hbar_q * hbar_q
G = mp.catalan

print("=" * 100)
print("ABSOLUTE m_p VIA SnapPy HYPERBOLIC VOLUME")
print("=" * 100)
print(f"  q_0    = {Q0_FLOAT}")
print(f"  ℏ_q    = 1 - 1/q_0 = {float(hbar_q):.10f}")
print(f"  ℏ_q²   = {float(hbar_q_sq):.10f}")
print(f"  m_e    = {M_E_MEV} MeV")
print(f"  m_p_CODATA = {M_P_MEV} MeV")
print(f"  m_n_CODATA = {M_N_MEV} MeV")
print()


def b3_braid_word():
    """B_3 = (sigma_1 sigma_2^-1)^3 — Borromean prefix."""
    return [1, -2, 1, -2, 1, -2]


def nucleon_braid_word(quark_types):
    """B_3 prefix + typed quark crossings.
    quark_types: list of 3 chars (e.g. 'uud' for proton)."""
    word = list(b3_braid_word())
    for i in range(3):
        for j in range(i + 1, 3):
            gen = min(i + 1, 2)
            t_i, t_j = quark_types[i], quark_types[j]
            if t_i == t_j == 'u':
                word.append(gen)
            elif t_i == t_j == 'd':
                word.append(-gen)
            else:
                word.append(gen)  # mixed (ud) = positive
    return word


def vol_of_braid_closure(word, n_strands=3):
    """Compute hyperbolic volume of the closure of a braid word."""
    M = snappy.Manifold("Braid:" + str(word))
    try:
        vol = float(M.volume())
        return vol, M
    except Exception as ex:
        return None, str(ex)


def main():
    print("─" * 100)
    print("Probe 1: proton braid (uud)")
    print("─" * 100)
    p_word = nucleon_braid_word(['u', 'u', 'd'])
    print(f"  Proton braid word: {p_word}")
    vol_p, M_p = vol_of_braid_closure(p_word)
    if vol_p is not None:
        print(f"  Vol(K_p) = {vol_p:.10f}")
        print(f"  m(K_p) = Vol(K_p)/ℏ_q² = {vol_p/float(hbar_q_sq):.4f} (dimensionless)")
        ratio = vol_p / float(hbar_q_sq) / M_E_MEV
        print(f"  m(K_p) [in m_e units] = {ratio:.4f}")
        print(f"  m_p_CODATA / m_e = {M_P_MEV / M_E_MEV:.4f}  (target)")
        print(f"  Direct  Vol(K_p)/ℏ_q² (MeV via *m_e?) = {(vol_p/float(hbar_q_sq))*M_E_MEV:.4f} MeV")
        print(f"  Ratio m(K_p) / m_p_CODATA = {(vol_p/float(hbar_q_sq))*M_E_MEV/M_P_MEV:.4f}")
    else:
        print(f"  proton volume computation failed: {M_p}")
    print()

    print("─" * 100)
    print("Probe 2: neutron braid (udd)")
    print("─" * 100)
    n_word = nucleon_braid_word(['u', 'd', 'd'])
    print(f"  Neutron braid word: {n_word}")
    vol_n, M_n = vol_of_braid_closure(n_word)
    if vol_n is not None:
        print(f"  Vol(K_n) = {vol_n:.10f}")
        m_kn = vol_n/float(hbar_q_sq)
        print(f"  m(K_n) [dimensionless] = {m_kn:.4f}")
        print(f"  m(K_n) * m_e = {m_kn * M_E_MEV:.4f} MeV")
    else:
        print(f"  neutron volume computation failed: {M_n}")
    print()

    if vol_p is not None and vol_n is not None:
        print("─" * 100)
        print("Probe 3: np splitting from volumes")
        print("─" * 100)
        delta_vol = vol_n - vol_p
        delta_m_dimensionless = delta_vol / float(hbar_q_sq)
        print(f"  Vol(K_n) - Vol(K_p) = {delta_vol:+.6f}")
        print(f"  Δm/m_e (volume-based) = {delta_m_dimensionless:+.6f}")
        print(f"  Δm (volume-based · m_e) = {delta_m_dimensionless * M_E_MEV:+.6f} MeV")
        print(f"  CODATA Δm_{{n-p}} = {M_N_MEV - M_P_MEV:+.6f} MeV")
        if delta_m_dimensionless != 0:
            print(f"  ratio = {(delta_m_dimensionless * M_E_MEV)/(M_N_MEV - M_P_MEV):+.4f}")

    print()
    print("─" * 100)
    print("Probe 4: B_3 prefix alone (Borromean rings, Vol = 8G)")
    print("─" * 100)
    b3_word = b3_braid_word()
    print(f"  B_3 braid word: {b3_word}")
    vol_b3, M_b3 = vol_of_braid_closure(b3_word)
    if vol_b3 is not None:
        print(f"  Vol(B_3) = {vol_b3:.10f}")
        print(f"  8G       = {float(8*G):.10f}")
        print(f"  match? Vol(B_3)/(8G) = {vol_b3 / float(8*G):.6f}")
        m_b3 = vol_b3/float(hbar_q_sq)
        print(f"  m(B_3) = Vol/ℏ_q² = {m_b3:.4f} (dimensionless)")
        print(f"  m(B_3) · m_e = {m_b3 * M_E_MEV:.4f} MeV")
    else:
        print(f"  B_3 volume failed: {M_b3}")


if __name__ == "__main__":
    main()
