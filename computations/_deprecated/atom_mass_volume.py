#!/usr/bin/env python3
"""
Mass from HYPERBOLIC VOLUME of nuclear braid closure.

The topological mass formula: 𝔪(K) = Vol(K) / ℏ_q²

For each atom, we:
1. Build the nuclear braid word from the derived construction
2. Close the braid to get a link
3. Compute hyperbolic volume via SnapPy
4. Apply 𝔪 = Vol / ℏ_q²

This is the CORRECT topological mass functional — it uses the
actual knot/link invariant (hyperbolic volume) rather than
algebraic proxies (L¹, E_hecke, tr_M).

Usage:
    python3 folio-assistant/computations/atom_mass_volume.py
"""

import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, HBAR_Q, HBAR_Q_SQ
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV
from witness_base import WitnessBuilder

try:
    import snappy
    HAS_SNAPPY = True
except ImportError:
    HAS_SNAPPY = False
    print("WARNING: SnapPy not available. Install with: pip install snappy")

HA = q0 - 1.0 / q0
z = 1.0 / (q0**0.5 + q0**(-0.5))
hbar_q = HBAR_Q
hbar_q_sq = HBAR_Q_SQ


# ══════════════════════════════════════════════════════════════
# §1  BRAID WORD CONSTRUCTION
# ══════════════════════════════════════════════════════════════

def b3_braid_word():
    """B₃ = (σ₀σ₁⁻¹)³ as a braid word on 3 strands.
    Convention: positive int = σᵢ, negative int = σᵢ⁻¹.
    SnapPy uses 1-indexed: σ₁, σ₂, ..."""
    # (σ₀σ₁⁻¹)³ in 0-indexed = (σ₁σ₂⁻¹)³ in 1-indexed
    return [1, -2, 1, -2, 1, -2]


def quark_crossing_word(type_i, type_j, gen_1indexed):
    """Typed crossing as braid generator.
    pp → σ_g (positive), nn → σ_g⁻¹ (negative), pn → σ_g (positive, mixed average)."""
    if type_i == type_j == 'u':
        return [gen_1indexed]
    elif type_i == type_j == 'd':
        return [-gen_1indexed]  # inverse
    else:
        return [gen_1indexed]  # mixed: use positive (average of σ and σ⁻¹)


def nucleon_braid_word(quark_types):
    """Build nucleon braid word: B₃ followed by typed quark crossings.
    Returns braid word on 3 strands (1-indexed generators σ₁, σ₂)."""
    word = list(b3_braid_word())
    for i in range(3):
        for j in range(i + 1, 3):
            gen = min(i, j) + 1  # 1-indexed
            if gen > 2:
                gen = 2
            word.extend(quark_crossing_word(quark_types[i], quark_types[j], gen))
    return word


def nuclear_crossing_word(type_i, type_j, gen_1indexed):
    """Inter-nucleon crossing as braid generator."""
    if type_i == type_j == 'p':
        return [gen_1indexed]
    elif type_i == type_j == 'n':
        return [-gen_1indexed]
    else:
        return [gen_1indexed]  # mixed


def atom_braid_word(Z, N):
    """Build the full atomic braid word.

    For A nucleons on n_strands = A strands (simplification):
    each nucleon contributes its internal structure on 3 sub-strands,
    and inter-nucleon crossings connect them.

    For the nuclear braid closure, we work in B_A with generators
    σ₁, ..., σ_{A-1} (1-indexed).

    The nuclear braid encodes:
    - Each nucleon k: 3 quark crossings (internal to nucleon)
    - Each pair (i,j): 1 inter-nucleon crossing

    Since nucleon internal structure uses 3 strands but the nucleus
    has A strands, we embed: nucleon k uses strands (3k-2, 3k-1, 3k)
    ... but that gives 3A strands, which is too many for SnapPy.

    SIMPLIFICATION: treat each nucleon as a POINT on one strand,
    and the nuclear braid is on A strands with inter-nucleon crossings
    only. The nucleon internal volume is added separately.
    """
    A = Z + N
    types = ['p'] * Z + ['n'] * N

    # Proton internal braid: 3 strands
    proton_word = nucleon_braid_word(['u', 'u', 'd'])
    neutron_word = nucleon_braid_word(['u', 'd', 'd'])

    # Nuclear braid: A strands, inter-nucleon crossings
    nuclear_word = []
    for i in range(A):
        for j in range(i + 1, A):
            gen = min(i, j) + 1  # 1-indexed
            if gen > A - 1:
                gen = A - 1
            nuclear_word.extend(nuclear_crossing_word(types[i], types[j], gen))

    # Electron crossings: Z additional crossings
    for e in range(Z):
        gen = (e % max(A - 1, 1)) + 1
        nuclear_word.append(gen)  # positive crossing (Hopf link)
        # Trefoil: σ_g σ_{g+1} σ_g (if g+1 exists)
        if gen < A - 1:
            nuclear_word.extend([gen, gen + 1, gen])

    return {
        'proton_word': proton_word,
        'neutron_word': neutron_word,
        'nuclear_word': nuclear_word,
        'n_strands_nucleon': 3,
        'n_strands_nuclear': A,
        'types': types,
    }


# ══════════════════════════════════════════════════════════════
# §2  HYPERBOLIC VOLUME VIA SNAPPY
# ══════════════════════════════════════════════════════════════

def braid_volume(word, n_strands):
    """Compute hyperbolic volume of braid closure via SnapPy."""
    if not HAS_SNAPPY:
        return float('nan'), "no_snappy"

    if len(word) == 0:
        return 0.0, "trivial"

    try:
        # SnapPy Link from braid closure
        L = snappy.Link(braid_closure=word)
        M = L.exterior()
        vol = float(M.volume())
        if abs(vol) < 1e-10:
            return 0.0, "non-hyperbolic"
        return vol, "hyperbolic"
    except Exception as e:
        return float('nan'), f"error:{str(e)[:50]}"


# ══════════════════════════════════════════════════════════════
# §3  COMPUTE ATOMS
# ══════════════════════════════════════════════════════════════

ELEMENTS = {
    1:  ("H",   1, 0),
    2:  ("He",  2, 2),
    3:  ("Li",  3, 4),
    4:  ("Be",  4, 5),
    5:  ("B",   5, 6),
    6:  ("C",   6, 6),
    7:  ("N",   7, 7),
    8:  ("O",   8, 8),
}

AME2020_MASS = {
    (1, 0): 938.783,     (2, 2): 3728.401,   (3, 4): 6535.367,
    (4, 5): 8394.794,    (5, 6): 10255.103,  (6, 6): 11177.930,
    (7, 7): 13043.781,   (8, 8): 14899.169,
}

# Known volumes for reference
KNOWN_VOLUMES = {
    'trefoil': 0.0,      # non-hyperbolic (torus knot)
    'figure_eight': 2.02988,
    'borromean': 7.32772,
}


def main():
    print("=" * 120)
    print("MASS FROM HYPERBOLIC VOLUME OF NUCLEAR BRAID CLOSURE")
    print(f"q₀ = {q0:.10f}   ℏ_q = {hbar_q:.10f}   ℏ_q² = {hbar_q_sq:.10f}")
    print(f"SnapPy: {'available' if HAS_SNAPPY else 'NOT available'}")
    print("=" * 120)
    print()
    print(f"Topological mass formula: 𝔪(K) = Vol(K) / ℏ_q²")
    print(f"  ℏ_q² = {hbar_q_sq:.10f}")
    print(f"  Energy scale: 1 Hecke unit = m_p / (Vol(proton_braid) / ℏ_q²)")
    print()

    # First: compute nucleon braid volumes
    print("─" * 120)
    print("NUCLEON BRAID VOLUMES:")
    proton_word = nucleon_braid_word(['u', 'u', 'd'])
    neutron_word = nucleon_braid_word(['u', 'd', 'd'])

    print(f"  Proton braid word ({len(proton_word)} generators): {proton_word}")
    print(f"  Neutron braid word ({len(neutron_word)} generators): {neutron_word}")

    vol_p, status_p = braid_volume(proton_word, 3)
    vol_n, status_n = braid_volume(neutron_word, 3)

    print(f"  Vol(proton closure)  = {vol_p:.10f}  [{status_p}]")
    print(f"  Vol(neutron closure) = {vol_n:.10f}  [{status_n}]")

    mass_p = vol_p / hbar_q_sq if not math.isnan(vol_p) else float('nan')
    mass_n = vol_n / hbar_q_sq if not math.isnan(vol_n) else float('nan')
    print(f"  𝔪(proton)  = Vol/ℏ_q² = {mass_p:.4f} Hecke units")
    print(f"  𝔪(neutron) = Vol/ℏ_q² = {mass_n:.4f} Hecke units")

    # Calibrate: E₀ such that 𝔪(proton) × E₀ = m_p (MeV)
    if mass_p > 0 and not math.isnan(mass_p):
        E0 = M_P_MEV / mass_p
    else:
        E0 = float('nan')
    print(f"  E₀ = m_p / 𝔪(proton) = {E0:.4f} MeV")
    if not math.isnan(mass_n) and not math.isnan(E0):
        mn_derived = mass_n * E0
        print(f"  Derived m_n = {mn_derived:.3f} MeV (CODATA: {M_N_MEV:.3f}, Δ={mn_derived-M_N_MEV:+.3f})")
    print()

    # Reference volumes
    print("─" * 120)
    print("REFERENCE KNOT VOLUMES (SnapPy):")
    for name, expected in KNOWN_VOLUMES.items():
        if name == 'trefoil':
            word, ns = [1, 2, 1], 3
        elif name == 'figure_eight':
            word, ns = [1, -2, 1, -2], 3
        elif name == 'borromean':
            word, ns = [1, -2, 1, -2, 1, -2], 3
        else:
            continue
        vol, status = braid_volume(word, ns)
        print(f"  {name}: Vol = {vol:.6f}  (expected: {expected:.5f})  [{status}]")
    print()

    # Compute nuclear braid volumes
    print("=" * 120)
    print("NUCLEAR BRAID VOLUMES")
    print("=" * 120)

    rows = []
    for Z_elem in sorted(ELEMENTS.keys()):
        name, Z, N = ELEMENTS[Z_elem]
        A = Z + N
        M_obs = AME2020_MASS.get((Z, N), 0.0)

        t0 = time.time()
        braid_data = atom_braid_word(Z, N)

        # Compute volumes
        # 1. Nuclear braid (A strands)
        vol_nuc, status_nuc = braid_volume(braid_data['nuclear_word'], A)

        # 2. Total volume = Z × Vol(proton) + N × Vol(neutron) + Vol(nuclear)
        # The nucleon internal volumes are additive (independent subbraids)
        if not any(math.isnan(v) for v in [vol_p, vol_n, vol_nuc]):
            vol_total = Z * vol_p + N * vol_n + vol_nuc
        else:
            vol_total = float('nan')

        # 3. Mass from volume
        mass_vol = vol_total / hbar_q_sq if not math.isnan(vol_total) else float('nan')
        M_derived = mass_vol * E0 if not math.isnan(mass_vol) and not math.isnan(E0) else float('nan')
        delta = M_derived - M_obs if not math.isnan(M_derived) else float('nan')
        delta_pct = delta / M_obs * 100 if M_obs > 0 and not math.isnan(delta) else float('nan')

        elapsed = time.time() - t0

        row = {
            'name': name, 'Z': Z, 'N': N, 'A': A,
            'nuclear_word_len': len(braid_data['nuclear_word']),
            'vol_nuclear': vol_nuc,
            'vol_total': vol_total,
            'status': status_nuc,
            'mass_hecke': mass_vol,
            'M_derived': M_derived,
            'M_obs': M_obs,
            'delta': delta,
            'delta_pct': delta_pct,
            'elapsed': elapsed,
        }
        rows.append(row)

        print(f"{'─' * 120}")
        print(f"  {name} (Z={Z}, N={N}, A={A})")
        print(f"    Nuclear braid: {len(braid_data['nuclear_word'])} generators on {A} strands")
        print(f"    Vol(nuclear braid)  = {vol_nuc:.6f}  [{status_nuc}]")
        print(f"    Vol(total)          = {vol_total:.6f}  "
              f"(= {Z}×{vol_p:.4f} + {N}×{vol_n:.4f} + {vol_nuc:.4f})")
        print(f"    𝔪 = Vol/ℏ_q²       = {mass_vol:.4f}")
        if not math.isnan(M_derived):
            print(f"    M_derived           = {M_derived:.1f} MeV")
            print(f"    M_observed          = {M_obs:.1f} MeV")
            print(f"    Δ = {delta:+.1f} MeV ({delta_pct:+.2f}%)")
        print(f"    time: {elapsed:.2f}s")

    # Summary
    print()
    print("=" * 120)
    print("SUMMARY: Vol/ℏ_q² MASS vs AME2020")
    print("=" * 120)
    print(f"{'Atom':>4} | {'A':>3} | {'Vol(nuc)':>10} | {'Vol(total)':>10} | "
          f"{'𝔪=V/ℏ²':>10} | {'M_derived':>12} | {'M_obs':>12} | {'Δ MeV':>8} | {'Δ%':>8}")
    print("─" * 120)
    for r in rows:
        vol_str = f"{r['vol_nuclear']:.4f}" if not math.isnan(r['vol_nuclear']) else "   nan   "
        vt_str = f"{r['vol_total']:.4f}" if not math.isnan(r['vol_total']) else "   nan   "
        m_str = f"{r['mass_hecke']:.4f}" if not math.isnan(r['mass_hecke']) else "   nan   "
        md_str = f"{r['M_derived']:.1f}" if not math.isnan(r['M_derived']) else "  nan  "
        d_str = f"{r['delta']:+.1f}" if not math.isnan(r['delta']) else "  nan  "
        dp_str = f"{r['delta_pct']:+.2f}%" if not math.isnan(r['delta_pct']) else "  nan  "
        print(f"{r['name']:>4} | {r['A']:3d} | {vol_str:>10} | {vt_str:>10} | "
              f"{m_str:>10} | {md_str:>12} | {r['M_obs']:12.1f} | {d_str:>8} | {dp_str:>8}")

    # Witness
    w = WitnessBuilder("atom-mass-volume", engine="snappy")
    w.set_description(
        "Mass from hyperbolic volume of nuclear braid closure. "
        "𝔪 = Vol(K)/ℏ_q². Computed via SnapPy 3.3.2."
    )
    w.add_parameter("q0", str(q0))
    w.add_parameter("hbar_q_sq", str(hbar_q_sq))
    w.add_parameter("vol_proton", str(vol_p))
    w.add_parameter("vol_neutron", str(vol_n))
    w.add_parameter("E0_MeV", str(E0))
    w.add_data("results", rows)
    w.save()


if __name__ == "__main__":
    main()
