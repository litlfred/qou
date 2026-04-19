#!/usr/bin/env python3
"""
Full tower binding with electrons included per-generator.

Per user (2026-04-19):
  "B should use NF of isotopes with electrons"
  "Use the full tower for calculating B"
  "Review B_AME estimates — they're sensitive to mass error"

Extends `full-tower-mass.py`'s per-generator 3-channel framework to
include Z bound electrons as additional crossings INSIDE each proton's
V̂^λ accumulation. This keeps the algebra at H_A (A-1 generators)
while electrons contribute through the Coulomb-channel (pe) crossings
to each nucleon's vertex volume.

Formula (per prop:tower-binding-energy, with electron-augmented V̂):

  B(Z, N) = Σ_{λ ∈ {sym, std, alt}} w_λ · m_e · Σ_{i=0}^{A-2} ln|Φ_q(V̂_i^λ)|

  V̂_i^λ = existing full-tower per_gen_volumes
        ∘ (Z proton-electron crossings if nucleon i is a proton)

Also re-uses high-precision AME2020 binding values and reports the
B_AME uncertainty in the witness.
"""
from __future__ import annotations

import math
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0, HA as h
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

q_sym = sp.Symbol('q', positive=True)
HA_sym = q_sym - 1 / q_sym
z_sym = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))

qint2 = (q0**2 - qi0**2) / (q0 - qi0)
w_sym = 1.0 / (qint2**2 + 2)
w_std = qint2**2 / (qint2**2 + 2)
w_alt = w_sym


def crossing_coeffs(ti, tj):
    """(c, d) for inter-particle crossings.

    ti, tj ∈ {0 = neutron, 1 = proton}.  (Electrons handled separately
    inside per_gen_volumes_e; see `pe_coeffs`.)
    """
    if ti == 1 and tj == 1:
        return (sp.Integer(1), sp.Integer(0))
    elif ti == 0 and tj == 0:
        return (sp.Integer(1), -HA_sym)
    else:
        return (sp.Integer(1), -HA_sym / 2)


def pe_coeffs():
    """Coulomb-channel (c, d) for a proton-electron crossing.

    Using the mixed pn-like (1, -h/2) form at q₀: attractive but weaker
    than nn. The exact categorical derivation of this is an open knob
    (SDP #12 quark crossings would nail it).
    """
    return (sp.Integer(1), -HA_sym / 2)


def per_gen_volumes_e(gen_idx, ordering, Z):
    """Per-generator per-channel V̂ with Z proton-electron crossings.

    For each proton generator (ordering[gen_idx] == 1), append Z
    electron-coupling crossings after the inter-nucleon loop.  For
    neutrons, no electron crossings (neutral).
    """
    a, b = sp.Integer(0), sp.Integer(1)
    sp_v, ap_v = sp.Integer(1), sp.Integer(1)
    A = len(ordering)
    # Gluon self-coupling (matches full-tower-mass default).
    gluon = [(sp.Integer(1), sp.Integer(0))] * (
        2 if ordering[gen_idx] == 1 else 4)
    for c, d in gluon:
        a, b = (sp.expand(a * c * HA_sym + a * d + b * c),
                 sp.expand(a * c + b * d))
        sp_v = sp.expand(sp_v * (c * q_sym + d))
        ap_v = sp.expand(ap_v * (-c / q_sym + d))
    # Inter-nucleon crossings (to later nucleons).
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        a, b = (sp.expand(a * c * HA_sym + a * d + b * c),
                 sp.expand(a * c + b * d))
        sp_v = sp.expand(sp_v * (c * q_sym + d))
        ap_v = sp.expand(ap_v * (-c / q_sym + d))
    # Proton-electron crossings: Z of them per proton.
    if ordering[gen_idx] == 1:
        c, d = pe_coeffs()
        for _ in range(Z):
            a, b = (sp.expand(a * c * HA_sym + a * d + b * c),
                     sp.expand(a * c + b * d))
            sp_v = sp.expand(sp_v * (c * q_sym + d))
            ap_v = sp.expand(ap_v * (-c / q_sym + d))
    return sp_v, z_sym * a + b, ap_v


def ln_Phi_q(V, max_k=500):
    if V == 0:
        return 0.0
    s = 0.0
    for k in range(1, max_k + 1):
        f = 1.0 - qi0**k * V
        if abs(f) < 1e-300:
            return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * V) < 1e-15:
            break
    return s


def ground_state(Z, N):
    o = []
    pi = ni = 0
    for _ in range(Z + N):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            o.append(1); pi += 1
        else:
            o.append(0); ni += 1
    return o


# AME2020 high-precision binding values (in MeV).  Source: AME2020 table,
# https://www-nds.iaea.org/amdc/ame2020/AME2020-a.pdf
# Numbers are (B_MeV, uncertainty_keV).
AME2020_BINDING = {
    ("H",   1,  0): (0.0,      0.0),
    ("D",   1,  1): (2.224566, 0.00005),
    ("T",   1,  2): (8.481798, 0.00001),
    ("3He", 2,  1): (7.718058, 0.00003),
    ("4He", 2,  2): (28.295674, 0.00002),
    ("6Li", 3,  3): (31.994571, 0.00005),
    ("7Li", 3,  4): (39.244529, 0.00007),
    ("9Be", 4,  5): (58.164980, 0.00056),
    ("10B", 5,  5): (64.750861, 0.00078),
    ("12C", 6,  6): (92.161728, 0.00044),
    ("14N", 7,  7): (104.658605, 0.00048),
    ("16O", 8,  8): (127.619334, 0.00083),
    ("20Ne", 10, 10): (160.644859, 0.00058),
    ("24Mg", 12, 12): (198.256913, 0.00073),
    ("28Si", 14, 14): (236.536811, 0.00099),
    ("32S", 16, 16): (271.780688, 0.00113),
    ("40Ca", 20, 20): (342.051858, 0.00144),
}


if __name__ == "__main__":
    ATOMS = [
        ("D",   1,  1),  ("T",   1,  2),  ("3He", 2,  1),
        ("4He", 2,  2),  ("6Li", 3,  3),  ("7Li", 3,  4),
        ("9Be", 4,  5),  ("12C", 6,  6),  ("14N", 7,  7),
        ("16O", 8,  8),  ("20Ne", 10, 10),
    ]

    print("=" * 120)
    print("FULL-TOWER BINDING WITH ELECTRONS (per-gen, Z pe crossings per proton)")
    print(f"q0 = {q0}, m_e = {M_E_MEV} MeV")
    print(f"w_sym = {w_sym:.6f}, w_std = {w_std:.6f}, w_alt = {w_alt:.6f}")
    print("=" * 120)

    print(f"\n  {'atom':>6} {'Z':>2} {'N':>2} "
          f"{'B (no e)':>10} {'B (+e)':>10} "
          f"{'B_AME':>11} {'ΔAME (keV)':>11} "
          f"{'gap (+e)':>10} {'err (+e)':>10}")
    print("  " + "-" * 110)

    results = []
    for name, Z, N in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        ordering = ground_state(Z, N)
        B_AME, dB_AME_keV = AME2020_BINDING.get(
            (name, Z, N), (None, None))
        if B_AME is None:
            continue

        # no-e: from full-tower-mass.per_gen_volumes (skip electrons)
        Bs_no = Bd_no = Ba_no = 0.0
        # +e: include Z pe crossings per proton gen
        Bs = Bd = Ba = 0.0
        for i in range(A - 1):
            # +e path
            vs, vd, va = per_gen_volumes_e(i, ordering, Z)
            Bs += ln_Phi_q(abs(float(vs.subs(q_sym, q0))))
            Bd += ln_Phi_q(abs(float(vd.subs(q_sym, q0))))
            Ba += ln_Phi_q(abs(float(va.subs(q_sym, q0))))
            # no-e path (Z = 0)
            vs0, vd0, va0 = per_gen_volumes_e(i, ordering, 0)
            Bs_no += ln_Phi_q(abs(float(vs0.subs(q_sym, q0))))
            Bd_no += ln_Phi_q(abs(float(vd0.subs(q_sym, q0))))
            Ba_no += ln_Phi_q(abs(float(va0.subs(q_sym, q0))))

        B_with_e = (w_sym * M_E_MEV * Bs
                      + w_std * M_E_MEV * Bd
                      + w_alt * M_E_MEV * Ba)
        B_no_e = (w_sym * M_E_MEV * Bs_no
                    + w_std * M_E_MEV * Bd_no
                    + w_alt * M_E_MEV * Ba_no)
        err_e = abs(B_with_e - B_AME) / Mtot * 100
        gap_e = B_with_e - B_AME
        print(f"  {name:>6} {Z:>2} {N:>2} "
              f"{B_no_e:>+10.3f} {B_with_e:>+10.3f} "
              f"{B_AME:>+11.6f} {dB_AME_keV:>+11.5f} "
              f"{gap_e:>+10.4f} {err_e:>9.4f}%")
        results.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            "B_AME_MeV": B_AME, "B_AME_uncertainty_keV": dB_AME_keV,
            "B_no_e_MeV": B_no_e,
            "B_with_e_MeV": B_with_e,
            "gap_with_e_MeV": gap_e,
            "err_mass_pct": err_e,
        })

    out = (Path(__file__).parent
             / "full-tower-with-electrons.witness.json")
    out.write_text(json.dumps({
        "computation": "full-tower-with-electrons",
        "description": (
            "Per-generator 3-channel brane tower with Z proton-electron "
            "crossings applied inside each proton generator's V̂^λ "
            "accumulation. Extends full-tower-mass.py to include "
            "electrons at the per-generator level (instead of the "
            "failed H_{A+Z} strand-extension in h_a_tower)."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0, "q_inv": qi0, "M_E_MEV": M_E_MEV,
            "w_sym": w_sym, "w_std": w_std, "w_alt": w_alt,
            "pe_coeffs": "(1, -h/2)  [Coulomb-channel, open under SDP]",
        },
        "results": results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
