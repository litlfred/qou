#!/usr/bin/env python3
"""
MASS FROM QUANTUM DILOGARITHM VOLUME — exact in q, no SnapPy.

The quantum dilogarithm volume of a nucleus N(Z,N) is:

  Φ_q(N) = Σ_{i=0}^{A-2} ln|V̂_i| = ln ∏|V̂_i|

where V̂_i = z·a_i + b_i are the traced volumes from the
transfer matrix chain (already computed by hecke_engine.py).

The mass is:
  𝔪(N) = Φ_q(N) / ℏ_q²

This is:
  - EXACT in q (Laurent polynomial, rational at q = 111/100)
  - The LOG of the Markov trace product (not the product itself)
  - O(A) scaling (intensive, like mass should be)
  - The q-analogue of hyperbolic volume
  - Already in the codebase (quantum-dilogarithm-volume.md)

The Markov trace product ∏V̂_i grows EXPONENTIALLY with A.
Taking the log converts this to LINEAR growth — matching mass.
This is why tr_M (= ∏V̂_i for the standard channel) decayed
to zero: the standard channel V̂_i are < 1, so the product
shrinks. But ln|V̂_i| can be negative or positive, and the
SUM is well-behaved.

We compute Φ_q for all three Hecke channels:
  Φ_sym = Σ ln|λ_sym,i|  (symmetric eigenvalue per crossing)
  Φ_std = Σ ln|V̂_i|      (standard traced volume, standard channel)
  Φ_alt = Σ ln|λ_alt,i|  (alternating eigenvalue per crossing)
  Φ_full = weighted combination

Usage:
    python3 folio-assistant/computations/atom_mass_dilogarithm.py
"""

import math
import sys
import time
from fractions import Fraction
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, HBAR_Q, HBAR_Q_SQ, LN_Q
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV
from witness_base import WitnessBuilder


# ══════════════════════════════════════════════════════════════
# §1  EXACT RATIONAL ENGINE
# ══════════════════════════════════════════════════════════════

class QRat:
    """Exact rational arithmetic at q = 111/100."""
    def __init__(self):
        self.q = Fraction(111, 100)
        self.q_inv = Fraction(100, 111)
        self.ha = self.q - self.q_inv
        self.z = Fraction(4993, 10000)
        self.hbar_q_sq = (1 - self.q_inv) ** 2

    def crossing(self, ti, tj):
        if ti == 1 and tj == 1:
            return Fraction(1), Fraction(0)
        elif ti == 0 and tj == 0:
            return Fraction(1), -self.ha
        else:
            return Fraction(1), -self.ha / 2

    def sym_eigenvalue(self, c, d):
        return c * self.q + d

    def alt_eigenvalue(self, c, d):
        return -c * self.q_inv + d

    def chain_reduce(self, gen_idx, ordering):
        a = Fraction(0)
        b = Fraction(1)
        A = len(ordering)
        for j in range(gen_idx + 1, A):
            c, d = self.crossing(ordering[gen_idx], ordering[j])
            new_a = a * c * self.ha + a * d + b * c
            new_b = a * c + b * d
            a, b = new_a, new_b
        return a, b

    def traced_volume(self, gen_idx, ordering):
        a, b = self.chain_reduce(gen_idx, ordering)
        return self.z * a + b


# ══════════════════════════════════════════════════════════════
# §2  QUANTUM DILOGARITHM VOLUME
# ══════════════════════════════════════════════════════════════

def quantum_dilogarithm_volume(qr, ordering):
    """Φ_q(N) = Σ ln|V̂_i| — the quantum dilogarithm volume.

    Returns (Phi_sym, Phi_std, Phi_alt) for all three channels.
    Each is the sum of log-absolute-values of the per-generator traces.
    """
    A = len(ordering)
    if A <= 1:
        return 0.0, 0.0, 0.0

    phi_sym = 0.0
    phi_std = 0.0
    phi_alt = 0.0

    for i in range(A - 1):
        # Standard channel: ln|V̂_i|
        v_std = float(qr.traced_volume(i, ordering))
        if abs(v_std) > 1e-30:
            phi_std += math.log(abs(v_std))

        # Symmetric and alternating: product of eigenvalues per generator
        sym_prod = 1.0
        alt_prod = 1.0
        for j in range(i + 1, A):
            c, d = qr.crossing(ordering[i], ordering[j])
            sym_prod *= float(qr.sym_eigenvalue(c, d))
            alt_prod *= float(qr.alt_eigenvalue(c, d))

        if abs(sym_prod) > 1e-30:
            phi_sym += math.log(abs(sym_prod))
        if abs(alt_prod) > 1e-30:
            phi_alt += math.log(abs(alt_prod))

    return phi_sym, phi_std, phi_alt


def ground_state_ordering(qr, p, n, max_orderings=5000):
    """Find minimum-energy ordering."""
    A = p + n
    total = math.comb(A, p)
    if total <= max_orderings:
        best_energy = None
        best_ordering = None
        for positions in combinations(range(A), p):
            ordering = [0] * A
            for pos in positions:
                ordering[pos] = 1
            energy = sum(float(qr.traced_volume(i, ordering)) for i in range(A - 1))
            if best_energy is None or energy < best_energy:
                best_energy = energy
                best_ordering = ordering
        return best_ordering, "exact"
    else:
        ordering = []
        pi, ni = 0, 0
        for k in range(A):
            if pi < p and (ni >= n or k % 2 == 0):
                ordering.append(1)
                pi += 1
            else:
                ordering.append(0)
                ni += 1
        return ordering, "heuristic"


# ══════════════════════════════════════════════════════════════
# §3  MAIN
# ══════════════════════════════════════════════════════════════

ELEMENTS = {
    1:  ("H",   "¹H",   1, 0),
    2:  ("He",  "⁴He",  2, 2),
    3:  ("Li",  "⁷Li",  3, 4),
    4:  ("Be",  "⁹Be",  4, 5),
    5:  ("B",   "¹¹B",  5, 6),
    6:  ("C",   "¹²C",  6, 6),
    7:  ("N",   "¹⁴N",  7, 7),
    8:  ("O",   "¹⁶O",  8, 8),
    9:  ("F",   "¹⁹F",  9, 10),
    10: ("Ne",  "²⁰Ne", 10, 10),
    11: ("Na",  "²³Na", 11, 12),
    12: ("Mg",  "²⁴Mg", 12, 12),
    13: ("Al",  "²⁷Al", 13, 14),
    14: ("Si",  "²⁸Si", 14, 14),
    15: ("P",   "³¹P",  15, 16),
    16: ("S",   "³²S",  16, 16),
    17: ("Cl",  "³⁵Cl", 17, 18),
    18: ("Ar",  "⁴⁰Ar", 18, 22),
    19: ("K",   "³⁹K",  19, 20),
    20: ("Ca",  "⁴⁰Ca", 20, 20),
}

AME2020_MASS = {
    (1,0): 938.783, (2,2): 3728.401, (3,4): 6535.367, (4,5): 8394.794,
    (5,6): 10255.103, (6,6): 11177.930, (7,7): 13043.781, (8,8): 14899.169,
    (9,10): 17696.901, (10,10): 18622.835,
    (11,12): 21414.830, (12,12): 22341.908, (13,14): 25133.143,
    (14,14): 26060.344, (15,16): 28851.873, (16,16): 29781.800,
    (17,18): 32573.283, (18,22): 37224.719, (19,20): 36294.464,
    (20,20): 37213.777,
}

SNAPPY_VOL_TOTAL = {
    (1,0): 0.0, (2,2): 34.449, (3,4): 81.757, (4,5): 105.648,
    (5,6): 130.466, (6,6): 139.157, (7,7): 164.118, (8,8): 188.130,
}


def main():
    qr = QRat()

    print("=" * 140)
    print("MASS FROM QUANTUM DILOGARITHM VOLUME  Φ_q = Σ ln|V̂_i|")
    print(f"q = {qr.q}   HA = {float(qr.ha):.10f}   ℏ_q² = {float(qr.hbar_q_sq):.10f}")
    print("𝔪 = Φ_q / ℏ_q²   (exact in q, intensive, O(A))")
    print("=" * 140)
    print()

    rows = []
    for Z_elem in sorted(ELEMENTS.keys()):
        name, label, Z, N = ELEMENTS[Z_elem]
        A = Z + N
        M_obs = AME2020_MASS.get((Z, N), 0.0)

        t0 = time.time()
        if A <= 1:
            ordering = [1] if Z == 1 else [0]
            method = "trivial"
        else:
            ordering, method = ground_state_ordering(qr, Z, N)

        phi_sym, phi_std, phi_alt = quantum_dilogarithm_volume(qr, ordering)

        # Weighted dilogarithm (1/6 sym + 4/6 std + 1/6 alt)
        phi_full = (phi_sym + 4 * phi_std + phi_alt) / 6.0

        # Mass from each channel
        hq2 = float(qr.hbar_q_sq)
        m_sym = phi_sym / hq2
        m_std = phi_std / hq2
        m_alt = phi_alt / hq2
        m_full = phi_full / hq2

        elapsed = time.time() - t0

        vol_snap = SNAPPY_VOL_TOTAL.get((Z, N), float('nan'))

        row = {
            'label': label, 'name': name, 'Z': Z, 'N': N, 'A': A,
            'phi_sym': phi_sym, 'phi_std': phi_std, 'phi_alt': phi_alt,
            'phi_full': phi_full,
            'm_sym': m_sym, 'm_std': m_std, 'm_alt': m_alt, 'm_full': m_full,
            'M_obs': M_obs, 'vol_snap': vol_snap,
            'elapsed': elapsed,
        }
        rows.append(row)

    # Calibrate: E₀ = M(⁴He) / (Φ_q(⁴He)/ℏ_q²) for each channel
    he = next(r for r in rows if r['label'] == '⁴He')
    E0_sym = he['M_obs'] / he['m_sym'] if abs(he['m_sym']) > 1e-10 else float('nan')
    E0_std = he['M_obs'] / he['m_std'] if abs(he['m_std']) > 1e-10 else float('nan')
    E0_alt = he['M_obs'] / he['m_alt'] if abs(he['m_alt']) > 1e-10 else float('nan')
    E0_full = he['M_obs'] / he['m_full'] if abs(he['m_full']) > 1e-10 else float('nan')

    print(f"CALIBRATION (E₀ = M(⁴He) / 𝔪_channel(⁴He)):")
    print(f"  E₀(sym)  = {E0_sym:.4f}")
    print(f"  E₀(std)  = {E0_std:.4f}")
    print(f"  E₀(alt)  = {E0_alt:.4f}")
    print(f"  E₀(full) = {E0_full:.4f}")
    print()

    # Main table
    print(f"{'Atom':>5} | {'A':>3} | {'Φ_sym':>10} | {'Φ_std':>10} | {'Φ_alt':>10} | {'Φ_full':>10} | "
          f"{'M_pred':>10} | {'M_obs':>10} | {'Δ MeV':>8} | {'Δ%':>7} | {'Vol_sn':>8} | {'Φ_std/Vsn':>8}")
    print("─" * 140)

    for r in rows:
        M_pred = r['m_std'] * E0_std if not math.isnan(E0_std) else float('nan')
        delta = M_pred - r['M_obs'] if not math.isnan(M_pred) else float('nan')
        pct = delta / r['M_obs'] * 100 if r['M_obs'] > 0 and not math.isnan(delta) else float('nan')
        phi_vs = r['phi_std'] / r['vol_snap'] if not math.isnan(r['vol_snap']) and r['vol_snap'] > 0.01 else float('nan')

        d_str = f"{delta:+8.1f}" if not math.isnan(delta) else "    —   "
        p_str = f"{pct:+6.2f}%" if not math.isnan(pct) else "   —  "
        mp_str = f"{M_pred:10.1f}" if not math.isnan(M_pred) else "     —    "
        vs_str = f"{r['vol_snap']:8.3f}" if not math.isnan(r['vol_snap']) else "    —   "
        pv_str = f"{phi_vs:8.4f}" if not math.isnan(phi_vs) else "    —   "

        print(f"{r['label']:>5} | {r['A']:3d} | {r['phi_sym']:+10.4f} | {r['phi_std']:+10.4f} | "
              f"{r['phi_alt']:+10.4f} | {r['phi_full']:+10.4f} | "
              f"{mp_str} | {r['M_obs']:10.1f} | {d_str} | {p_str} | {vs_str} | {pv_str}")

    # Scaling check
    print()
    print("=" * 140)
    print("SCALING: Φ_std / M_obs × 1000 (should be constant if Φ ∝ M)")
    print("=" * 140)
    for r in rows:
        if r['M_obs'] > 0 and abs(r['phi_std']) > 1e-10:
            ratio = r['phi_std'] / r['M_obs'] * 1000
            print(f"  {r['label']:>5}: Φ_std/M × 1000 = {ratio:8.4f}   "
                  f"Φ_sym/M × 1000 = {r['phi_sym']/r['M_obs']*1000:8.4f}   "
                  f"Φ_alt/M × 1000 = {r['phi_alt']/r['M_obs']*1000:8.4f}")

    # Witness
    w = WitnessBuilder("atom-mass-dilogarithm", engine="python")
    w.set_description(
        "Mass from quantum dilogarithm volume Φ_q = Σ ln|V̂_i|. "
        "Exact in q, O(A) scaling. Three channels: sym/std/alt."
    )
    w.add_parameter("q", "111/100")
    w.add_parameter("hbar_q_sq", str(float(qr.hbar_q_sq)))
    w.add_parameter("E0_std", str(E0_std))
    w.add_data("results", rows)
    w.save()


if __name__ == "__main__":
    main()
