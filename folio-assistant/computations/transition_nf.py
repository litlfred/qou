#!/usr/bin/env python3
"""
Transition NF: tracks which crossings change between parent and daughter.

For β⁻ decay (Z,N) → (Z+1,N-1), exactly ONE neutron converts to proton.
The transition NF captures ONLY the changed crossings:

1. Converting nucleon quarks: udd → uud
   gen 0: dd pair (σ⁻¹) → uu pair (σ)              Δ = +h per crossing
   gen 0: ud pair (mixed) → uu pair (σ)              Δ = +h/2
   gen 1: dd pair (σ⁻¹) → ud pair (mixed)            Δ = +h/2

2. Inter-nucleon crossings with converting nucleon:
   nn → pn: (σ⁻¹) → (mixed)                         Δ = +h/2 per pair
   pn → pp: (mixed) → (σ)                            Δ = +h/2 per pair

3. Spectator crossings: UNCHANGED (cancel in difference)

The transition element T lives in H₃(q) and its NF gives Q.

Reference: def:Q-value-transition
"""

import math
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi, HA as h, q_int
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from hecke_core import (
    build_atom_nf_exact,
    _TR_M_FRAC,
    _H_FRAC,
    check_frobenius,
    knot_factor,
    binding_energy,
)
from pyhecke.gram import (
    hm_exact,
    nf_tr,
    NF_NAMES,
)
from witness_base import WitnessBuilder


F0 = Fraction(0)
F1 = Fraction(1)
Fh = _H_FRAC
Fh2 = Fh / 2


def transition_nf(Z_par, N_par):
    """Compute the transition NF for β⁻: (Z,N) → (Z+1, N-1).

    Builds the FULL parent NF, then applies ONLY the crossing
    changes from the converting neutron (last n in ordering).

    The transition NF = NF(parent) with converting-nucleon crossings
    replaced, then the RATIO parent/daughter gives the transition.

    More precisely: we build both parent and daughter NFs tracking
    the same crossing order, and the transition is the element T
    such that NF(dau) = T × NF(par) in H₃(q).

    Returns: (nf_par, nf_dau, nf_delta, transition_data)
    """
    Z_dau, N_dau = Z_par + 1, N_par - 1
    A = Z_par + N_par

    # Build both NFs with SAME ordering, tracking which crossings differ
    ordering_par = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z_par) or nc >= N_par:
            ordering_par.append('p'); pc += 1
        else:
            ordering_par.append('n'); nc += 1

    # Find the LAST neutron → this is the converting nucleon
    convert_pos = None
    for k in range(A - 1, -1, -1):
        if ordering_par[k] == 'n':
            convert_pos = k
            break

    if convert_pos is None:
        return None

    ordering_dau = list(ordering_par)
    ordering_dau[convert_pos] = 'p'

    # Build NFs tracking per-crossing changes
    nf_par = [F0] * 6; nf_par[0] = F1
    nf_dau = [F0] * 6; nf_dau[0] = F1

    changed_crossings = []

    for k in range(A):
        nuc_par = ordering_par[k]
        nuc_dau = ordering_dau[k]
        is_converting = (k == convert_pos)

        # B₃: 3× σ₀ + 3× σ₁⁻¹ (SAME for par and dau)
        for _ in range(3):
            nf_par = hm_exact(nf_par, F1, F0, 0)
            nf_dau = hm_exact(nf_dau, F1, F0, 0)
        for _ in range(3):
            nf_par = hm_exact(nf_par, F1, -Fh, 1)
            nf_dau = hm_exact(nf_dau, F1, -Fh, 1)

        # Quark crossings
        if is_converting:
            # Parent: neutron (udd)
            nf_par = hm_exact(nf_par, F1, -Fh2, 0)   # ud
            nf_par = hm_exact(nf_par, F1, -Fh2, 0)   # ud
            nf_par = hm_exact(nf_par, F1, -Fh, 1)    # dd
            # Daughter: proton (uud)
            nf_dau = hm_exact(nf_dau, F1, F0, 0)     # uu
            nf_dau = hm_exact(nf_dau, F1, F0, 0)     # uu
            nf_dau = hm_exact(nf_dau, F1, -Fh2, 1)   # ud
            changed_crossings.append(('quark', k, 'udd→uud'))
        else:
            if nuc_par == 'p':
                nf_par = hm_exact(nf_par, F1, F0, 0)
                nf_par = hm_exact(nf_par, F1, F0, 0)
                nf_par = hm_exact(nf_par, F1, -Fh2, 1)
                nf_dau = hm_exact(nf_dau, F1, F0, 0)
                nf_dau = hm_exact(nf_dau, F1, F0, 0)
                nf_dau = hm_exact(nf_dau, F1, -Fh2, 1)
            else:
                nf_par = hm_exact(nf_par, F1, -Fh2, 0)
                nf_par = hm_exact(nf_par, F1, -Fh2, 0)
                nf_par = hm_exact(nf_par, F1, -Fh, 1)
                nf_dau = hm_exact(nf_dau, F1, -Fh2, 0)
                nf_dau = hm_exact(nf_dau, F1, -Fh2, 0)
                nf_dau = hm_exact(nf_dau, F1, -Fh, 1)

        # Inter-nucleon crossings with PREVIOUS nucleons
        for prev in range(k):
            ti_par = ordering_par[prev]
            tj_par = ordering_par[k]
            ti_dau = ordering_dau[prev]
            tj_dau = ordering_dau[k]

            # Parent crossing type
            if ti_par == 'p' and tj_par == 'p': d_par = F0
            elif ti_par == 'n' and tj_par == 'n': d_par = -Fh
            else: d_par = -Fh2

            # Daughter crossing type
            if ti_dau == 'p' and tj_dau == 'p': d_dau = F0
            elif ti_dau == 'n' and tj_dau == 'n': d_dau = -Fh
            else: d_dau = -Fh2

            nf_par = hm_exact(nf_par, F1, d_par, 0)
            nf_dau = hm_exact(nf_dau, F1, d_dau, 0)

            if d_par != d_dau:
                changed_crossings.append(('inter', prev, k,
                    f'{ti_par}{tj_par}→{ti_dau}{tj_dau}'))

    # Electrons (SAME for par and dau — Z_par electrons for parent,
    # Z_dau = Z_par+1 for daughter, so daughter gets ONE MORE electron)
    for _ in range(Z_par):
        nf_par = hm_exact(nf_par, F1, -Fh, 1)
        nf_dau = hm_exact(nf_dau, F1, -Fh, 1)
    # Daughter has one extra electron
    nf_dau = hm_exact(nf_dau, F1, -Fh, 1)
    changed_crossings.append(('electron', '+1'))

    # NF difference
    delta = [nf_par[i] - nf_dau[i] for i in range(6)]
    tr_par = sum(c * t for c, t in zip(nf_par, _TR_M_FRAC))
    tr_dau = sum(c * t for c, t in zip(nf_dau, _TR_M_FRAC))
    tr_delta = sum(c * t for c, t in zip(delta, _TR_M_FRAC))

    return {
        'Z_par': Z_par, 'N_par': N_par,
        'nf_par': [float(x) for x in nf_par],
        'nf_dau': [float(x) for x in nf_dau],
        'nf_delta': [float(x) for x in delta],
        'tr_par': float(tr_par),
        'tr_dau': float(tr_dau),
        'tr_delta': float(tr_delta),
        'tr_ratio': float(tr_par / tr_dau) if tr_dau != 0 else None,
        'ln_ratio': float(Fraction(tr_par / tr_dau).limit_denominator(10**15))
            if tr_dau != 0 and float(tr_par/tr_dau) > 0 else None,
        'changed_crossings': changed_crossings,
        'convert_pos': convert_pos,
    }


# AME Q-values for β⁻ decays
DECAYS = [
    (0, 1, "n→¹H", 0.78233),
    (1, 2, "³H→³He", 0.01861),
    (2, 4, "⁶He→⁶Li", 3.5078),
    (6, 8, "¹⁴C→¹⁴N", 0.15648),
]


if __name__ == "__main__":
    print("TRANSITION NF: β⁻ decay crossing changes")
    print(f"h = q - q⁻¹ = {float(Fh):.6f}")
    print()

    results = []
    for Z, N, name, Q_exp in DECAYS:
        A = Z + N
        print(f"=== {name} (Z={Z},N={N}, A={A}) ===")

        r = transition_nf(Z, N)
        if r is None:
            print("  No neutron to convert"); continue

        print(f"  Converting nucleon at position {r['convert_pos']}")
        print(f"  Changed crossings: {len(r['changed_crossings'])}")
        for cc in r['changed_crossings']:
            print(f"    {cc}")
        print()

        print(f"  NF(parent):   tr_M = {r['tr_par']:>+.8f}")
        print(f"  NF(daughter): tr_M = {r['tr_dau']:>+.8f}")
        print(f"  Δ(NF):        tr_M = {r['tr_delta']:>+.8f}")
        if r['tr_ratio'] is not None:
            print(f"  Ratio par/dau      = {r['tr_ratio']:>+.8f}")
            if r['tr_ratio'] > 0:
                ln_r = math.log(r['tr_ratio'])
                print(f"  ln|ratio|          = {ln_r:>+.8f}")

        # Q from mass difference (categorical binding path)
        B_par = binding_energy(Z, N)
        B_dau = binding_energy(Z+1, N-1)
        M_par = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV - B_par
        if Z == 0:
            M_par = M_N_MEV
        M_dau = (Z+1)*M_P_MEV + (N-1)*M_N_MEV + (Z+1)*M_E_MEV - B_dau
        Q_mass = M_par - M_dau

        print(f"\n  Q(mass diff) = {Q_mass:.5f} MeV")
        print(f"  Q(exp)       = {Q_exp:.5f} MeV")
        print(f"  Error        = {(Q_mass-Q_exp)/Q_exp*100:+.2f}%")
        print()

        r['Q_mass'] = Q_mass
        r['Q_exp'] = Q_exp
        results.append(r)

    # Save witness
    w = WitnessBuilder("transition-nf", engine="python")
    w.set_description(
        "Transition NF for β⁻ decays. Tracks per-crossing changes "
        "between parent and daughter at quark level."
    )
    for r in results:
        w.add_data(f"Z{r['Z_par']}N{r['N_par']}", {
            'tr_par': r['tr_par'],
            'tr_dau': r['tr_dau'],
            'tr_delta': r['tr_delta'],
            'tr_ratio': r['tr_ratio'],
            'n_changed': len(r['changed_crossings']),
            'Q_mass_MeV': round(r['Q_mass'], 6),
            'Q_exp_MeV': r['Q_exp'],
        })
    w.save()
