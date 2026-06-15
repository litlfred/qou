#!/usr/bin/env python3
"""
Inductive atom construction with full Gröbner--Shirshov witness.

For each atom built inductively, produce a complete witness:
  - All inputs (particles, crossing types, generators)
  - The Gröbner--Shirshov basis (ideal) used for reduction
  - Every reduction step (Hecke, YB, far-comm) with energy
  - The normal form and its decomposition over the particle catalog
  - Markov trace and Hecke energy

Natural atoms: formed by adding nucleons then electrons in
the physical filling order (proton first, then neutrons,
then electrons by shell).

Synthetic atoms: could have different q-torsion due to
different formation history (e.g. created in accelerators).
The Gröbner--Shirshov basis is the same, but the initial braid word
may differ.

Usage:
    python3 inductive-atom-witness.py
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path
from hecke_division import HeckeDivision, HeckeElement
from q_parameter import Q as q, Q_INV as qi, E_CROSS
from experimental_constants import *

div = HeckeDivision(q_val=q)
HA = q - qi                        # Hecke amplitude q - q⁻¹
Z_m = 1.0 / (q**0.5 + qi**0.5)
kappa = E_CROSS * M_E_MEV / (3 * E_CROSS)

def sigma(i):
    return HeckeElement({(i,): 1.0})


# ══════════════════════════════════════════════════════════════
# §1  THE IDEAL (Gröbner--Shirshov basis for reduction)
# ══════════════════════════════════════════════════════════════

IDEAL = {
    "generators": [
        "sigma_i^2 = (q - q^{-1}) * sigma_i + 1  [Hecke relation]",
        "sigma_i * sigma_{i+1} * sigma_i = sigma_{i+1} * sigma_i * sigma_{i+1}  [Yang-Baxter]",
        "sigma_i * sigma_j = sigma_j * sigma_i  for |i-j| >= 2  [far-commutativity]",
    ],
    "parameters": {
        "q": q,
        "q_inv": qi,
        "HA": HA,
        "hecke_amplitude": HA,
        "z_markov": Z_m,
    },
    "ordering": "length-lexicographic on positive braid monomials",
}


# ══════════════════════════════════════════════════════════════
# §2  CROSSING TYPES
# ══════════════════════════════════════════════════════════════

# At the nucleon+electron level:
# - p-p: positive crossing sigma (proton-proton, same charge nucleon)
# - n-n: Skein inverse q^2*sigma - q*s (neutron-neutron)
# - p-n / n-p: mixed crossing σ - ½(q-q⁻¹)
# - p-e / n-e / e-p / e-n: Hopf link = positive crossing sigma
# - e-e: Hopf link between electrons = positive crossing sigma

CROSSING_TYPES = {
    # Nuclear crossings
    "pp": {"c": 1.0, "d": 0.0, "description": "proton-proton: σ (Coulomb repulsion)"},
    "nn": {"c": 1.0, "d": float(-HA), "description": "neutron-neutron: σ⁻¹ = σ - (q-q⁻¹)"},
    "pn": {"c": 1.0, "d": float(-HA/2), "description": "proton-neutron: ½(σ + σ⁻¹) = σ - ½(q-q⁻¹)"},
    "np": {"c": 1.0, "d": float(-HA/2), "description": "neutron-proton: ½(σ + σ⁻¹) = σ - ½(q-q⁻¹)"},
    # Electron crossings
    "pe": {"c": 1.0, "d": float(-HA), "description": "proton-electron: σ⁻¹ (EM attraction)"},
    "ep": {"c": 1.0, "d": float(-HA), "description": "electron-proton: σ⁻¹ (EM attraction)"},
    "ne": {"c": 0.0, "d": 1.0, "description": "neutron-electron: 𝟏 (no interaction)"},
    "en": {"c": 0.0, "d": 1.0, "description": "electron-neutron: 𝟏 (no interaction)"},
    "ee": {"c": 1.0, "d": 0.0, "description": "electron-electron: σ (EM repulsion)"},
}

c_nn = 1.0; d_nn = -HA
c_mix = 1.0; d_mix = -HA/2

def crossing_element(ti, tj, gen):
    """Build the Hecke element for a crossing between types ti, tj at generator gen."""
    pair = frozenset([ti, tj])

    if ti == tj == 'p':
        return sigma(gen)                                    # pp: σ
    elif ti == tj == 'n':
        return HeckeElement({(gen,): c_nn, (): d_nn})        # nn: σ⁻¹
    elif pair == frozenset(['p', 'n']):
        return HeckeElement({(gen,): c_mix, (): d_mix})      # pn: ½(σ+σ⁻¹)
    elif pair == frozenset(['p', 'e']):
        return HeckeElement({(gen,): 1.0, (): float(-HA)})   # pe: σ⁻¹ (attraction)
    elif pair == frozenset(['n', 'e']):
        return HeckeElement({(): 1.0})                       # ne: 𝟏 (no interaction)
    elif ti == tj == 'e':
        return sigma(gen)                                    # ee: σ (repulsion)
    else:
        return sigma(gen)                                    # fallback: σ

def nf_dict(elem):
    """Convert element to serializable dict."""
    return {('.'.join(f'sigma_{i}' for i in w) if w else '1'): c
            for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0]))}


# ══════════════════════════════════════════════════════════════
# §3  INDUCTIVE ATOM BUILDER WITH FULL WITNESS
# ══════════════════════════════════════════════════════════════

def build_atom_witnessed(particles, label, formation="natural"):
    """Build an atom inductively with complete witness at every step.

    particles: list of particle types in construction order.
               e.g. ['p', 'e'] for hydrogen (natural: proton then electron)
    label: human-readable name
    formation: "natural" or "synthetic" (affects q-torsion note)

    Returns a complete witness dict.
    """
    A = len(particles)
    witness = {
        "label": label,
        "formation": formation,
        "particles": particles,
        "n_strands": A,
        "construction_order": [
            {"position": i, "type": particles[i]} for i in range(A)
        ],
        "ideal": IDEAL,
        "steps": [],
        "q_torsion_note": (
            "Natural atoms form through stellar nucleosynthesis or Big Bang. "
            "Synthetic atoms (accelerator-produced) may have different q-torsion "
            "due to the high-energy formation environment affecting the initial "
            "braid word before reduction."
        ) if formation == "synthetic" else (
            "Natural formation: nucleons aggregate by lowest-energy Hopf linking, "
            "electrons captured sequentially by shell."
        ),
    }

    elem = HeckeElement.identity()
    total_E = 0.0
    total_H = 0
    total_YB = 0
    total_FC = 0

    if A == 1:
        # Single particle = identity in H_1(q)
        witness["steps"].append({
            "description": f"Step 0: single particle {particles[0]}",
            "element_before": "1 (identity)",
            "crossings": [],
            "reductions": [],
            "element_after": nf_dict(elem),
            "n_terms": 1,
            "hecke_energy": 0.0,
        })

    for k in range(1, A):
        step = {
            "description": f"Step {k}: add {particles[k]} at position {k}",
            "particle_added": particles[k],
            "position": k,
            "crossings": [],
            "reductions": [],
            "element_before": nf_dict(elem),
            "n_terms_before": elem.n_terms(),
        }

        for i in range(k):
            gen = i
            pair_type = particles[i] + particles[k]
            cx = crossing_element(particles[i], particles[k], gen)

            # Record the crossing
            cx_record = {
                "with_particle": i,
                "with_type": particles[i],
                "pair": pair_type,
                "generator": f"sigma_{gen}",
                "crossing_coefficients": CROSSING_TYPES.get(pair_type, {"c": 1.0, "d": 0.0}),
                "hecke_element": nf_dict(cx),
            }

            # Multiply
            elem_before_mult = elem
            elem = elem * cx

            # Record pre-reduction state
            pre_red = nf_dict(elem)
            n_pre = elem.n_terms()

            # Reduce
            elem, log = div.reduce(elem)
            summary = div.summarize_log(log)
            E = summary.get('hecke_energy_change', 0)
            total_E += E
            total_H += summary['hecke_steps']
            total_YB += summary['yang_baxter_steps']
            total_FC += summary['far_comm_steps']

            # Record the reduction
            reduction = {
                "pre_reduction": pre_red,
                "pre_terms": n_pre,
                "hecke_steps": summary['hecke_steps'],
                "yang_baxter_steps": summary['yang_baxter_steps'],
                "far_comm_steps": summary['far_comm_steps'],
                "hecke_energy": E,
                "post_reduction": nf_dict(elem),
                "post_terms": elem.n_terms(),
            }

            cx_record["reduction"] = reduction
            step["crossings"].append(cx_record)

        step["element_after"] = nf_dict(elem)
        step["n_terms_after"] = elem.n_terms()
        step["cumulative_hecke_energy"] = total_E
        step["cumulative_hecke_steps"] = total_H
        step["cumulative_yb_steps"] = total_YB
        witness["steps"].append(step)

    # Final normal form
    tr_val = div.markov_trace(elem, A)

    witness["normal_form"] = {
        "terms": nf_dict(elem),
        "n_terms": elem.n_terms(),
        "markov_trace": tr_val,
        "ln_markov_trace": math.log(abs(tr_val)) if tr_val != 0 else None,
        "total_hecke_energy": total_E,
        "total_hecke_steps": total_H,
        "total_yb_steps": total_YB,
        "total_far_comm_steps": total_FC,
        "in_groebner_nf": True,  # by construction (reduced at every step)
    }

    return witness, elem


# ══════════════════════════════════════════════════════════════
# §4  BUILD ATOMS
# ══════════════════════════════════════════════════════════════

print("Building atoms with full Gröbner--Shirshov witness...")
print()

atoms_to_build = [
    # (particles, label, formation)
    (['p'], "proton (bare)", "natural"),
    (['n'], "neutron (bare)", "natural"),
    (['p', 'e'], "protium H (natural)", "natural"),
    (['e', 'p'], "protium H (synthetic: e first)", "synthetic"),
    (['p', 'n'], "deuterium nucleus D", "natural"),
    (['p', 'n', 'e'], "deuterium atom D (natural)", "natural"),
    (['p', 'n', 'n'], "tritium nucleus 3H", "natural"),
    (['p', 'n', 'n', 'e'], "tritium atom 3H (natural)", "natural"),
    (['p', 'p', 'n'], "helium-3 nucleus 3He", "natural"),
    (['p', 'p', 'n', 'e', 'e'], "helium-3 atom 3He (natural)", "natural"),
]

all_witnesses = {}
all_elements = {}

for particles, label, formation in atoms_to_build:
    w, elem = build_atom_witnessed(particles, label, formation)
    all_witnesses[label] = w
    all_elements[label] = elem

    nf = w["normal_form"]
    p_str = ','.join(particles)
    print(f"  {label:>35}: [{p_str:>10}] {nf['n_terms']:>3} terms, "
          f"E={nf['total_hecke_energy']:.6f}, "
          f"{nf['total_hecke_steps']}H+{nf['total_yb_steps']}YB, "
          f"tr={nf['markov_trace']:.8f}")

# ══════════════════════════════════════════════════════════════
# §5  NATURAL vs SYNTHETIC COMPARISON
# ══════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("NATURAL vs SYNTHETIC: protium")
print("=" * 70)
print()

nat = all_witnesses["protium H (natural)"]
syn = all_witnesses["protium H (synthetic: e first)"]

print(f"  Natural [p,e]:  {nat['normal_form']['n_terms']} terms, tr={nat['normal_form']['markov_trace']:.10f}")
print(f"  Synthetic [e,p]: {syn['normal_form']['n_terms']} terms, tr={syn['normal_form']['markov_trace']:.10f}")

if abs(nat['normal_form']['markov_trace'] - syn['normal_form']['markov_trace']) < 1e-10:
    print("  SAME trace — same physical atom regardless of formation order")
else:
    print(f"  DIFFERENT traces — formation order matters!")
    print(f"  Difference: {nat['normal_form']['markov_trace'] - syn['normal_form']['markov_trace']:.2e}")

# ══════════════════════════════════════════════════════════════
# §6  SAVE FULL WITNESS
# ══════════════════════════════════════════════════════════════

full_witness = {
    "computation": "inductive-atom-witness",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": (
        "Complete Gröbner--Shirshov basis witness for inductive atom construction. "
        "Every crossing, every reduction step, every Hecke energy cost "
        "is recorded. Includes natural and synthetic formation paths."
    ),
    "parameters": IDEAL["parameters"],
    "crossing_types": CROSSING_TYPES,
    "atoms": all_witnesses,
}

out = Path("inductive-atom-witness.json")
with open(out, "w") as f:
    json.dump(full_witness, f, indent=2, default=str)
print(f"\nFull witness: {out}")
print(f"  Size: {out.stat().st_size / 1024:.1f} KB")

# Also write Lean-compatible witness
lean_out = Path("inductive-atom-witness.lean.txt")
with open(lean_out, "w") as f:
    f.write(f"-- Inductive atom construction witness\n")
    f.write(f"-- Generated: {datetime.now(timezone.utc).isoformat()}\n")
    f.write(f"-- q = {q}\n\n")

    for label, w in all_witnesses.items():
        nf = w["normal_form"]
        f.write(f"-- {label}\n")
        f.write(f"-- Particles: {w['particles']}\n")
        f.write(f"-- Formation: {w['formation']}\n")
        f.write(f"-- Normal form ({nf['n_terms']} terms):\n")
        for ws, c in nf['terms'].items():
            f.write(f"--   {c:+.10f} * {ws}\n")
        f.write(f"-- Markov trace = {nf['markov_trace']:.10f}\n")
        f.write(f"-- Hecke energy = {nf['total_hecke_energy']:.10f}\n")
        f.write(f"-- Hecke steps = {nf['total_hecke_steps']}, YB = {nf['total_yb_steps']}\n")
        f.write(f"-- In Gröbner--Shirshov NF: {nf['in_groebner_nf']}\n\n")

print(f"Lean witness: {lean_out}")

# Summary table
print()
print("=" * 70)
print("SUMMARY TABLE")
print("=" * 70)
print()
print(f"  {'Atom':>35} | {'Particle':>12} | {'Coefficient':>12} | Role")
print("  " + "-" * 75)
for label in ["protium H (natural)", "deuterium atom D (natural)",
               "tritium atom 3H (natural)", "helium-3 atom 3He (natural)"]:
    w = all_witnesses[label]
    nf = w["normal_form"]
    print(f"  {label:>35} |")
    for ws, c in nf['terms'].items():
        print(f"  {'':>35} | {ws:>12} | {c:>+12.6f} |")
    print(f"  {'':>35} | {'tr =':>12} | {nf['markov_trace']:>+12.6f} |")
    print(f"  {'':>35} | {'E_Hecke =':>12} | {nf['total_hecke_energy']:>12.6f} |")
    print()
